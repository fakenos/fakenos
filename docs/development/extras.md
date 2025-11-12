# Extras
In this section, we describe other things that may be useful for application development.

## Development CLI
One of the biggest problems we have identified when developing is that we make a small change and we would like it to be immediately reflected in the application. For this reason, we have created an option in the CLI that allows you to load the application in development mode and automatically reload it each time a change is made in the code. IT is only made for the commands, as it is the part that it most demanding. This is designed for the development of new platforms, so files that are outside the `fakenos/plugins/nos/` folder will not be reflected in the application.

The command is as follows:

```bash
fakenos --reload-commands
```

!!! warning
    Changes are additive. This means that if you introduce a new command, you will see the change reflected and the same if you modify the commmand. But if you delete a command, it will not be removed from the application until the server is restarted.

This is achieved by setting an environment variable called "FAKENOS_RELOAD_COMMANDS". If this is found, then hot-reload will be activated. If it is not found, then it will not be activated. At the end of the CLI, the variable will be removed.