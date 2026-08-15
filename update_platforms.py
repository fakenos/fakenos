"""
This script updates bundled platform YAML files from NTC Templates test
fixtures. It performs the following steps when executed directly:
1. Download the NTC-Templates repository.
2. Extract all the available platforms which are in the tests files.
3. For each platform, create a new .yaml file containing the commands
   and the output for each device.
"""

import os
import re
import subprocess
import tempfile
from typing import Dict, List, Tuple

import requests

# pylint: disable=import-error
from ruamel.yaml import YAML

tmp_ntc_templates_dir: str = os.path.join(tempfile.gettempdir(), "ntc-templates")
netmiko_platforms_url: str = "https://raw.githubusercontent.com/ktbyers/netmiko/develop/PLATFORMS.md"
platforms_folder: str = "fakenos/plugins/nos/platforms_yaml"


def clone_or_update_repository(repo_url: str, target_dir: str) -> None:
    """
    Clone or update a git repository into a target directory.
    If the directory exists, the repository will be updated.
    If the directory doesn't exist, the repository will be cloned.
    """
    if os.path.exists(target_dir):
        subprocess.check_call(["git", "-C", target_dir, "pull"])
        print(f"Repository updated successfully in {target_dir}")
    else:
        subprocess.check_call(["git", "clone", repo_url, target_dir])
        print(f"Repository cloned successfully into {target_dir}")


def get_directories_in_folder(folder_path: str) -> List[str]:
    """Get the name of all the directories in a folder."""
    return [name for name in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, name))]


def get_files_with_extension_in_folder(folder_path: str, extension: str, fulldir: bool = True) -> List[str]:
    """Get the name of all the files with a certain extension in a folder."""
    files = [
        name
        for name in os.listdir(folder_path)
        if os.path.isfile(os.path.join(folder_path, name)) and name.endswith(extension)
    ]
    if fulldir:
        return [os.path.join(folder_path, name) for name in files]
    return files


def check_platforms_in_md(md_file: str) -> List[str]:
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


def download_and_extract_platforms(url: str, local_path: str) -> List[str]:
    """
    Download a file from the given URL and extract the platforms from it.
    The platforms are extracted from the section
    under "Supported SSH device_type values".
    """
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    with open(local_path, "w", encoding="utf-8") as file:
        file.write(response.text)
    return check_platforms_in_md(local_path)


def get_commands(platform_name: str) -> Dict[str, str]:
    """
    Get the commands and outputs from the tests files for a specific platform.
    """
    commands: dict = {}
    test_folders = get_directories_in_folder(f"{tmp_ntc_templates_dir}/tests/{platform_name}")
    for test_file in test_folders:
        command, output = get_command_and_output(test_file, platform_name)
        commands[command] = output
    return commands


def get_command_and_output(test_file: str, platform_name: str) -> Tuple[str, str]:
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


def generate_platform_yaml(platform_name: str, commands: dict) -> None:
    """
    Generate a YAML file for a platform with the given commands and outputs.
    """
    commands = get_commands_parsed(platform_name, commands)
    yaml = YAML()
    yaml_content = {
        "name": platform_name,
        "initial_prompt": f"{platform_name}>",
        "commands": commands,
    }
    with open(f"{platforms_folder}/{platform_name}.yaml", "w", encoding="utf-8") as file:
        yaml.dump(yaml_content, file)


def main() -> None:
    """Update platform YAML files from shared Netmiko and NTC Templates data."""
    clone_or_update_repository("https://github.com/networktocode/ntc-templates", tmp_ntc_templates_dir)
    platforms = get_directories_in_folder(os.path.join(tmp_ntc_templates_dir, "tests"))
    netmiko_platforms_file = os.path.join(tempfile.gettempdir(), "netmiko-platforms.md")
    available_netmiko_platforms = download_and_extract_platforms(netmiko_platforms_url, netmiko_platforms_file)
    common_platforms = sorted(set(platforms) & set(available_netmiko_platforms))
    print(f"Available platforms in Netmiko & NTC-Templates: {common_platforms}")

    for platform in common_platforms:
        generate_platform_yaml(platform, get_commands(platform))


if __name__ == "__main__":
    main()
