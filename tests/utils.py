import random
import socket
import string

from fakenos.core.host import Host


def get_running_hosts(hosts: dict[str, Host]) -> dict[str, bool]:
    """
    Get the running hosts in the network.
    """
    return {host_name: host.running for host_name, host in hosts.items()}


def get_free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", 0))
        return s.getsockname()[1]


def generate_random_string(length):
    letters = string.ascii_letters
    return "".join(random.choice(letters) for i in range(length))


def get_random_available_platform():
    platforms = get_platforms_from_md()
    return random.choice(platforms)

def get_platforms_from_md() -> list[str]:
    """Get the platforms in the platforms.md file."""
    platforms = []
    with open("docs/platforms.md", "r") as file:
        for line in file:
            if line.startswith("- ["):
                platform = line[1:].strip()  # Remove the dash and whitespace
                if "❌" in platform:
                    continue
                # Get the word in between brackets, eg. "aruba_eos" from "[aruba_eos]"
                platform = platform.split("[")[1].split("]")[0]
                platforms.append(platform)
    return platforms
