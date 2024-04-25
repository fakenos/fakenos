"""
This script is used to update and fulfill all the possible platforms in
an automatic way. It extracts the information from NTC-Templates tests
commands, which are the output from the real devices. The script works
with the following steps:
1. Download the NTC-Templates repository.
2. Extract all the available platforms which are in the tests files.
3. For each platform, it will create a new .yaml file which have the commands
and the output for each device.
4. The script will update the platforms.yaml file with the new platforms.
5. The script will update the tests/core/test_fakenos.py file with the
   new tests.
"""

import os
import re
import subprocess

import requests
from ruamel.yaml import YAML

tmp_ntc_templates_dir: str = "/tmp/ntc-templates"
netmiko_platforms_url: str = "https://raw.githubusercontent.com/ktbyers/netmiko/develop/PLATFORMS.md"
platforms_folder: str = "fakenos/plugins/nos/platforms"


def clone_or_update_repository(repo_url, target_dir):
    """
    Clone or update a git repository into a target directory.
    If the directory exists, the repository will be updated.
    If the directory doesn't exist, the repository will be cloned.
    """
    if os.path.exists(target_dir):
        try:
            subprocess.check_call(["git", "-C", target_dir, "pull"])
            print(f"Repository updated successfully in {target_dir}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to update the repository. Error: {e}")
    else:
        try:
            subprocess.check_call(["git", "clone", repo_url, target_dir])
            print(f"Repository cloned successfully into {target_dir}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to clone the repository. Error: {e}")


def get_directories_in_folder(folder_path):
    """Get the name of all the directories in a folder."""
    return [name for name in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, name))]


def get_files_with_extension_in_folder(folder_path, extension, fulldir=True):
    """Get the name of all the files with a certain extension in a folder."""
    files = [
        name
        for name in os.listdir(folder_path)
        if os.path.isfile(os.path.join(folder_path, name)) and name.endswith(extension)
    ]
    if fulldir:
        return [os.path.join(folder_path, name) for name in files]
    return files


def check_platforms_in_md(md_file):
    """
    Check which platforms from the given list are also
    mentioned in the specified markdown file.
    """
    with open(md_file, "r", encoding="utf-8") as file:
        content = file.read()
    match = re.search(r"###### Supported SSH device_type values\n((?:.|\n)*?)\n\n", content)
    if match:
        platforms = match.group(1).split("\n")
        platforms = [platform.strip() for platform in platforms]
        platforms = [platform for platform in platforms if "-" in platform]
        platforms = [platform.strip().replace("- ", "") for platform in platforms]
        return platforms
    return []


def download_and_extract_platforms(url: str, local_path: str) -> list[str]:
    """
    Download a file from the given URL and extract the platforms from it.
    The platforms are extracted from the section
    under "Supported SSH device_type values".
    """
    response = requests.get(url, timeout=30)
    with open(local_path, "w", encoding="utf-8") as file:
        file.write(response.text)
    return check_platforms_in_md(local_path)


def get_commands(platform_name: str) -> dict[str, str]:
    """
    Get the commands and outputs from the tests files for a specific platform.
    """
    commands: dict = {}
    test_folders = get_directories_in_folder(f"{tmp_ntc_templates_dir}/tests/{platform_name}")
    for test_file in test_folders:
        command, output = get_command_and_output(test_file, platform_name)
        commands[command] = output
    return commands


def get_command_and_output(test_file: str, platform_name: str) -> tuple[str, str]:
    """
    Get the commands and outputs from a specific test file for a platform.
    """
    filename: str = get_files_with_extension_in_folder(
        f"{tmp_ntc_templates_dir}/tests/{platform_name}/{test_file}", ".raw"
    )[0]
    content: str = ""
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
    command = test_file.replace("_", " ")
    return command, content


def get_commands_parsed(platform_name: str, commands: dict) -> dict:
    """
    Parse the commands and outputs to be used in the YAML file.
    """
    base_commands = {
        "enable": {
            "output": "null",
            "new_prompt": f"{platform_name}#",
            "help": "enter enable mode",
            "prompt": f"{platform_name}>",
        }
    }
    extra_commands = {
        command: {
            "output": output,
            "help": f'execute the command "{command}"',
            "prompt": [f"{platform_name}>", f"{platform_name}#"],
        }
        for command, output in commands.items()
    }
    return {**base_commands, **extra_commands}


def generate_platform_yaml(platform_name: str, commands: dict):
    """
    Generate a YAML file for a platform with the given commands and outputs.
    """
    commands = get_commands_parsed(platform_name, commands)
    yaml = YAML()
    yaml_content = {"name": platform_name, "initial_prompt": f"{platform_name}>", "commands": commands}
    with open(f"{platforms_folder}/{platform_name}.yaml", "w", encoding="utf-8") as file:
        yaml.dump(yaml_content, file)


clone_or_update_repository("https://github.com/networktocode/ntc-templates", tmp_ntc_templates_dir)

platforms: list[str] = get_directories_in_folder(f"{tmp_ntc_templates_dir}/tests")

available_netmiko_platforms = download_and_extract_platforms(netmiko_platforms_url, "/tmp/PLATFORMS.md")
common_platforms = set(platforms) & set(available_netmiko_platforms)
print(f"Available platforms in Netmiko & NTC-Templates: {common_platforms}")

with open("docs/platforms.md", "w", encoding="utf-8") as file:
    file.write("## Available Platforms\n\n")
    for platform in common_platforms:
        file.write(f"- {platform}\n")

commands: dict = {}
for platform in common_platforms:
    commands[platform] = get_commands(platform)

for platform, commands in commands.items():
    generate_platform_yaml(platform, commands)
