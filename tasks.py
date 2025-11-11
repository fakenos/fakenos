"""
This file contains the Invoke tasks for the project.
The tasks are used to run tests, build the Docker image,
and run the development environment. The tasks can be
run locally or within the Docker container.
"""

import os
import sys
import time
import tomllib

from invoke import task
from netmiko import ConnectHandler
import yaml

from fakenos import FakeNOS

if sys.version_info < (3, 11):
    sys.exit("Please make sure to run this with Python 3.11 or higher.")


def strtobool(val: str) -> bool:
    """Convert a string representation of truth to true (1) or false (0).

    Args:
        val (str): String representation of truth.

    Returns:
        bool: True or False
    """
    val = val.lower()

    # Check for valid truth values
    if val in ("y", "yes", "t", "true", "on", "1"):
        return True

    # Check for valid false values
    if val in ("n", "no", "f", "false", "off", "0"):
        return False

    # Raise an error if the value is not valid
    raise ValueError(f"Invalid truth value: {val}")


def is_truthy(arg: str | bool) -> bool:
    """Convert "truthy" strings into Booleans.

    Examples:
        >>> is_truthy("yes")
        True

    Args:
        arg (str): Truthy string (True values are y, yes, t, true, on
                    and 1; false values are n, no,
        f, false, off and 0. Raises ValueError if val is anything else.
    """
    if isinstance(arg, bool):
        return arg
    return bool(strtobool(arg))


with open("pyproject.toml", "rb") as f:
    PYPROJECT_CONFIG = tomllib.load(f)
TOOL_CONFIG = PYPROJECT_CONFIG["project"]

# Can be set to a separate Python version to be used
# for launching or building image
PYTHON_VER = os.getenv("PYTHON_VER", "3.13")
# Name of the docker image/image
IMAGE_NAME = os.getenv("IMAGE_NAME", TOOL_CONFIG["name"])
# Tag for the image
IMAGE_VER = os.getenv("IMAGE_VER", f"{TOOL_CONFIG['version']}-py{PYTHON_VER}")
# Gather current working directory for Docker commands
PWD = os.getcwd()
# Local or Docker execution provide "local" to
# run locally without docker execution
INVOKE_LOCAL = is_truthy(os.getenv("INVOKE_LOCAL", "False"))


def run_cmd(context, exec_cmd, local=INVOKE_LOCAL, port=None):
    """Wrapper to run the invoke task commands.

    Args:
        context ([invoke.task]): Invoke task object.
        exec_cmd ([str]): Command to run.
        local (bool): Define as `True` to execute locally

    Returns:
        result (obj): Contains Invoke result from running task.
    """
    if is_truthy(local):
        print(f"LOCAL - Running command: {exec_cmd}")
        result = context.run(exec_cmd, pty=True)
    else:
        print(
            f"DOCKER - Running command: {exec_cmd} \
              container {IMAGE_NAME}:{IMAGE_VER}"
        )
        if port:
            result = context.run(
                f"docker run -it -p {port} -v {PWD}:/local \
                    {IMAGE_NAME}:{IMAGE_VER} sh -c '{exec_cmd}'",
                pty=True,
            )
        else:
            result = context.run(
                f"docker run -it -v {PWD}:/local \
                    {IMAGE_NAME}:{IMAGE_VER} sh -c '{exec_cmd}'",
                pty=True,
            )
    return result


@task(
    help={
        "cache": "Whether to use Docker's cache \
            with building images (default enabled)",
        "force_rm": "Always remove intermediate images",
        "hide": "Supress output from Docker",
    }
)
def build(context, cache=True, force_rm=False, hide=False):
    """Build a Docker image."""
    print(f"Building image {IMAGE_NAME}:{IMAGE_VER}")
    command = f"docker build --tag {IMAGE_NAME}:{IMAGE_VER} --build-arg PYTHON_VER={PYTHON_VER} -f Dockerfile ."

    if not cache:
        command += " --no-cache"
    if force_rm:
        command += " --force-rm"

    result = context.run(command, hide=hide)
    if result.exited != 0:
        print(
            f"Failed to build image \
              {IMAGE_NAME}:{IMAGE_VER}\nError: {result.stderr}"
        )


@task
def clean(context):
    """Remove the project specific image."""
    print(f"Attempting to forcefully remove image {IMAGE_NAME}:{IMAGE_VER}")
    context.run(f"docker rmi {IMAGE_NAME}:{IMAGE_VER} --force")
    print(f"Successfully removed image {IMAGE_NAME}:{IMAGE_VER}")


@task
def rebuild(context):
    """Clean the Docker image and then rebuild without using cache."""
    clean(context)
    build(context, cache=False)


@task(help={"local": "Run locally or within the Docker container"})
def pytest(context, local=INVOKE_LOCAL):
    """Run pytest test cases."""
    exec_cmd = "pytest"
    run_cmd(context, exec_cmd, local=local)


@task(help={"local": "Run locally or within the Docker container"})
def ruff(context, local=INVOKE_LOCAL):
    """Run ruff to check that Python files adherence to ruff standards."""
    exec_cmd = "ruff check --diff"
    run_cmd(context, exec_cmd, local=local)
    exec_cmd = "ruff format --diff"
    run_cmd(context, exec_cmd, local=local)


@task(help={"local": "Run locally or within the Docker container"})
def yamllint(context, local=INVOKE_LOCAL):
    """Run yamllint to check YAML files."""
    exec_cmd = "yamllint ."
    run_cmd(context, exec_cmd, local=local)


@task(help={"local": "Run locally or within the Docker container"})
def bandit(context, local=INVOKE_LOCAL):
    """Run bandit to validate basic static code security analysis."""
    exec_cmd = "bandit -c pyproject.toml --recursive ./"
    run_cmd(context, exec_cmd, local=local)


@task
def cli(context):
    """Enter the image to perform troubleshooting or dev work."""
    dev = f"docker run -it -v {PWD}:/local {IMAGE_NAME}:{IMAGE_VER} /bin/bash"
    context.run(dev, pty=True)


@task(help={"local": "Run locally or within the Docker container"})
def tests(context, local=INVOKE_LOCAL):
    """Run all tests."""
    ruff(context, local=local)
    # yamllint(context, local=local)
    bandit(context, local=local)
    pytest(context, local=local)

    print("All tests have passed successfully! ✅")


@task
def docs(context, local=INVOKE_LOCAL):
    """Build and serve docs locally for development."""
    exec_cmd = "mkdocs serve -v --dev-addr=0.0.0.0:8001"
    run_cmd(context, exec_cmd, local=local, port="8001:8001")


WARNING_MESSAGE = """
!!! warning
    This is automatically generated. In case of any issues,
    please refer to the source code or, even better,
    open an issue on the GitHub repository. Thanks! 🤗📖
"""


# pylint: disable=unused-argument
@task
def gen_docs_platform_commands(ctx):
    """
    Generate platform specific commands in the docs.
    """
    platforms_folder: str = "fakenos/plugins/nos/platforms"
    files: list[str] = os.listdir(platforms_folder)
    platforms: list[str] = [platform.split(".yaml")[0] for platform in files]

    for platform in platforms:
        print(f"Generating Platform: {platform}")
        if os.path.exists(f"docs/platforms/{platform}.md"):
            continue
        with open(f"{platforms_folder}/{platform}.yaml", "r", encoding="utf-8") as file:
            data = yaml.safe_load(file)
        with open(f"docs/platforms/{platform}.md", "w", encoding="utf-8") as platforms_file:
            platforms_file.write(f"# {platform}\n\n")
            platforms_file.write(WARNING_MESSAGE)
            platforms_file.write("## Platforms:\n\n")
            platforms_file.write("## Commands\n\n")
            for command, details in data["commands"].items():
                platforms_file.write(f"### {command}\n\n")
                output = details["output"]
                if output is None:
                    platforms_file.write("**Output:** None\n\n")
                else:
                    platforms_file.write("**Output:**\n```\n" + repr(output) + "\n```\n\n")
                platforms_file.write(f"**Help:** {details['help']}\n\n")
                platforms_file.write("**Prompt:**\n")
                prompts = details["prompt"]
                if not isinstance(prompts, list):
                    prompts = [prompts]
                for prompt in prompts:
                    platforms_file.write(f"- {prompt}\n")
                platforms_file.write("\n")


# pylint: disable=unused-argument
@task(help={"device_type": "The device type to connect to."})
def netmiko_check(ctx, device_type: str):
    """
    This is a task for debugging possible problems with Netmiko logins.
    """
    init_time = time.time()
    inventory = {
        "hosts": {
            "host1": {
                "username": "user",
                "password": "user",
                "platform": device_type,
                "port": 6000,
            }
        }
    }

    credentials = {
        "host": "localhost",
        "username": "user",
        "password": "user",
        "port": 6000,
        "device_type": device_type,
    }

    net = FakeNOS(inventory=inventory)
    net.start()

    with ConnectHandler(**credentials):
        time.sleep(1)

    net.stop()

    print("Everything is OK! ✅")
    print(f"Time spent: {time.time() - init_time:.2f}s")
