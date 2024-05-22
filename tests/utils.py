"""
This module contains utility functions for the tests.
"""

import random
import socket
import string
from typing import Dict, List, Tuple

from fakenos.core.host import Host


def get_running_hosts(hosts: Dict[str, Host]) -> Dict[str, bool]:
    """
    Get the running hosts in the network.
    """
    return {host_name: host.running for host_name, host in hosts.items()}


def get_free_port():
    """It returns a free port."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", 0))
        return s.getsockname()[1]


def generate_random_string(length):
    """Generate a random string with the given length."""
    letters = string.ascii_letters
    return "".join(random.choice(letters) for i in range(length))


def get_random_available_platform():
    """Get a random available platform."""
    platforms = get_platforms_from_md()
    return random.choice(platforms)


def get_platforms_from_md() -> List[str]:
    """Get the platforms in the platforms.md file."""
    platforms = []
    with open("docs/platforms.en.md", "r", encoding="utf-8") as file:
        for line in file:
            if line.startswith("- ["):
                platform = line[1:].strip()  # Remove the dash and whitespace
                if "❌" in platform:
                    continue
                # Get the word in between brackets, eg. "aruba_eos" from "[aruba_eos]"
                platform = platform.split("[")[1].split("]")[0]
                platforms.append(platform)
    return platforms


def get_host_commands(host: Host) -> Tuple:
    """
    Get the commands of the host.
    It gets the initial, enable and config commands.
    """
    initial_commands, enable_commands, config_commands = [], [], []
    for command, options in host.nos.commands.items():
        if not hasattr(options, "prompt"):
            continue
        prompts = options["prompt"]
        new_prompt = options.get("new_prompt", None)
        if (
            new_prompt
            or "alias" in options
            or isinstance(options.get("output", ""), bool)
            or command in ["exit", "quit", "logout"]
        ):
            continue
        if isinstance(prompts, str):
            prompts = [prompts]
        for prompt in prompts:
            if prompt == host.nos.initial_prompt:
                initial_commands.append(command)
            elif host.nos.enable_prompt and prompt == host.nos.enable_prompt:
                enable_commands.append(command)
            elif host.nos.config_prompt and prompt == host.nos.config_prompt:
                config_commands.append(command)
    return initial_commands, enable_commands, config_commands
