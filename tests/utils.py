import random
import socket
import string

from fakenos.core.host import Host


def get_running_hosts(hosts: dict[str, Host]) -> dict[str, bool]:
    """
    Get the running hosts in the network.
    """
    return {host_name: host.running for host_name, host in hosts.items()}

def get_platforms() -> list[str]:
    """
    It gets the current supported platforms.
    """
    platforms = []
    with open('platforms.md', 'r') as file:
        for line in file:
            if line.startswith('-'):
                platform = line[1:].strip()  # Remove the dash and whitespace
                if "❌" in platform:
                    continue
                platform = platform.split(' ')[0]  # Get the first word
                platforms.append(platform)
    return platforms


def get_free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 0))
        return s.getsockname()[1]
    
def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

def get_random_available_platform():
    platforms = get_platforms()
    return random.choice(platforms)