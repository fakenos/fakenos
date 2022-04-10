# Fake Network Operating Systems - FakeNOS

> "Reality is merely an illusion, albeit a very persistent one."
> 
> ~ Albert Einstein

FakeNOS created to simulate Network Operating Systems interactions.

## How to Generate SSH private key

By default FakeNOS uses default private key embedded with the package, making that
key publicly available, which is insecure. Instead of default key FakeNos can locally
generate SSH key located at 

**Linux**

Use the command `ssh-keygen -A` in terminal to generate all of your SSH keys. Once the command is run,
you can find the RSA key in the following location: `~/.ssh/id_rsa` a.k.a. `/home/username/.ssh/id_rsa`.
Supply above path as `ssh_key_file` argument to FakeNOS server configuration.

Alternatively can use `ckeygen -t rsa -f ssh-keys/ssh_host_rsa_key` command to generate private key. 

**Windows 10**

Press Windows Key, type `Manage Optional Features`. If OpenSSH Client & Server is in the list, you're all set.
If either is not, click on "Add a feature" and search for `OpenSSH`, click on them to install.
Next, open cmd as administrator. Enter the command `ssh-keygen` and follow the on screen prompts.
The location of the key will be displayed. Supply displayed path as `ssh_key_file` argument to FakeNOS
server configuration. If you put a password, include it as the `ssh_key_file_password` parameter.

## FakeNOS inspired by and borrowed from

- [sshim](https://pythonhosted.org/sshim/) - library for testing and debugging SSH automation clients
- [PythonSSHServerTutorial](https://github.com/ramonmeza/PythonSSHServerTutorial) - tutorial on creating paramiko based SSH server
- [fake-switches](https://github.com/internap/fake-switches) - pluggable switch/router command-line simulator
- [ncs-netsim](https://developer.cisco.com/docs/nso/guides/#!the-network-simulator) - tool to simulate a network of devices
- [cisshgo](https://github.com/tbotnz/cisshgo) - concurrent SSH server to emulate network equipment for testing purposes
