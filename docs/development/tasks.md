In order to make it easier the development, several small tasks have been develop. Please
feel free to add more. All those tasks can be found in the `tasks.py`. In order to run them,
you can use the following command:
```bash
invoke <task_name>
```

The available tasks are:

-  `tests`: It will create a docker that will perform all the needed tests to ensure that the code passes all the tests, format conventions, etc. It is intended to help ensure a good maintainance of the project.

-  `gen-docs-platform-commands`: Generate automatically the documentation for a platform. It was originally intended to document all the commands in the first version of the project, but it can be used to document any platform.

-  `netmiko-check`: Netmiko is a core library in Network Automation. FakeNOS intends to be a testing library for it, and as such, it is important to ensure that the available platforms are compatible with Netmiko. This task generates a script that can be used to test the compatibility of a platform with Netmiko. If it goes well, it will say `Everything is OK! ✅`.