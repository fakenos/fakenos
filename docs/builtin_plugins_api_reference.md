## NOS Plugins

NOS plugins are at the heart of FakeNOS, they are what enables to realize its
full potential.

### Cisco IOS

::: fakenos.plugins.nos.cisco_ios
    rendering:
      show_if_no_docstring: true
	  heading_level: 4
	  show_object_full_path: false

## Servers Plugins

Servers Plugins acts as an access layer, simulating device connections.

### ParamikoSshServer

::: fakenos.plugins.servers.ssh_server_paramiko.ParamikoSshServer
    rendering:
	  heading_level: 4
	  show_object_full_path: false

## Shell Plugins

Shell Plugins act as a plumbing between servers plugins and NOS plugins,
gluing, connecting them together.

### CMDShell

::: fakenos.plugins.shell.cmd_shell.CMDShell
    rendering:
	  heading_level: 4
	  show_object_full_path: false

## Tape Plugins

Idea - Tape Plugins will allow to record interactions with real devices and build
NOS plugins automatically using gathered data.