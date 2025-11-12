# Adding new platforms
FakeNOS is designed to be easily extensible. It is designed in such 
a way that adding new platforms is simple and can be done using different
methods. At the moment, it is possible only using Python modules or YAML files.

!!! tip
    There is implemented a hot-reloader that automatically reloads Python modules
    and YAML files when they are modified inside `fakenos/plugins/nos`. To run it
    simply do `fakenos --reload-commands`.

## YAML files
This is preferred way in case that the platform you want to implement is not
existing yet. The great advantage of this method is that it is fairly simple
to add new platforms. However, it is not as flexible as the Python module method
as it is not possible to implement dynamic behavior.

The YAML files are located in the `fakenos/plugins/nos/platforms_yaml` directory.


## Python modules
This method is more flexible than the YAML files method. It is possible to implement
dynamic behavior and to use the full power of Python. However, it is a little more difficult to
implement. The Python modules are located in the `fakenos/plugins/nos/platforms_py` package.
