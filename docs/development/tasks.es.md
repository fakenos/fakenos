Para facilitar el desarrollo, se han desarrollado varias tareas pequeñas. Por favor, siéntase libre de añadir más. Todas esas tareas se pueden encontrar en el archivo `tasks.py`. Para ejecutarlas, puede usar el siguiente comando:
```bash
invoke <task_name>
```

Las tareas disponibles son:

-  `tests`: Creará un contenedor Docker que realizará todas las pruebas necesarias para asegurar que el código pase todas las pruebas, convenciones de formato, etc. Está destinado a ayudar a garantizar un buen mantenimiento del proyecto. Existe un flag que es `--local` para que no se ejecute en un contenedor Docker.

-  `gen-docs-platform-commands`: Genera automáticamente la documentación para una plataforma. Originalmente estaba destinado a documentar todos los comandos en la primera versión del proyecto, pero se puede utilizar para documentar cualquier plataforma.

-  `netmiko-check`: Netmiko es una librería ampliamente utilizada en el mundo de la automatización de red. FakeNOS pretende ser utilizada como una librería de testing para esta, y como tal, es importante asegurarse de que todas las plataformas disponibles son compatibles con Netmiko. Esta tarea genera un script que se puede utilizar para probar la compatibilidad de una plataforma con Netmiko. Si todo va bien, dirá `¡Todo correcto! ✅`.