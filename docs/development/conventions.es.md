# Convenciones
Esta sección tiene la intención de explicar brevemente todas las herramientas utilizadas dentro del proyecto. Estas herramientas están principalmente allí para asegurar que el código esté escrito y probado correctamente.

## General: Poetry
Poetry es una herramienta para gestionar las dependencias de Python y empaquetar proyectos. Simplifica el proceso de gestión de dependencias proporcionando una manera consistente y declarativa de especificarlas en un archivo `pyproject.toml`. Poetry también gestiona la creación del entorno virtual, la construcción del paquete y la publicación. A menudo es preferido por los desarrolladores por su facilidad de uso e integración con otras herramientas del ecosistema de Python.

Todas las configuraciones del proyecto se pueden encontrar en el `pyproject.toml`. Aquí tienes algunos comandos básicos:

- `poetry install`: úsalo para instalar todas las dependencias.
- `poetry update`: úsalo para actualizar las dependencias.
- `poetry shell`: entra en el intérprete creado usando poetry install.

## Tests: Pytest
Pytest es un marco de pruebas para Python que facilita la escritura de pruebas simples y escalables. Te permite escribir casos de prueba como funciones Python regulares, usando aserciones para verificar los resultados esperados. Pytest proporciona características potentes como fixtures para configurar entornos de prueba, pruebas parametrizadas y complementos para extender la funcionalidad. Es ampliamente utilizado en la comunidad de Python por su simplicidad, flexibilidad y extenso ecosistema de complementos.

Para ejecutar las pruebas haz lo siguiente
```bash
pytest
```

## Comprobación de seguridad: Bandit
Bandit es una herramienta de seguridad para código Python que detecta problemas de seguridad y vulnerabilidades comunes. Analiza el código Python estáticamente para identificar posibles amenazas de seguridad como el uso inseguro de módulos, llamadas a funciones inseguras y riesgos de seguridad potenciales. Bandit proporciona un conjunto de complementos que comprueban diversos problemas de seguridad y se pueden integrar fácilmente en flujos de trabajo de desarrollo, ayudando a los desarrolladores a identificar y solucionar problemas de seguridad temprano en el proceso de desarrollo. Es una herramienta valiosa para mejorar la postura de seguridad de las aplicaciones y bibliotecas de Python.

Para ejecutar la herramienta bandit haz lo siguiente:
```bash
bandit -c pyproject.toml -r .
```

## Formateo básico: Black
Black es un formateador de código Python que formatea automáticamente tu código Python según un conjunto estricto de reglas de formato. Asegura un estilo de código consistente en un proyecto aplicando automáticamente el formato como la indentación, la longitud de línea y el espaciado. Black sigue el principio de "formateo de código sin configuración", lo que significa que aplica sus reglas de formato de manera uniforme sin requerir ninguna configuración o ajuste manual. A menudo se utiliza para imponer un estilo de código consistente en proyectos de Python y para ahorrar tiempo a los desarrolladores mediante la automatización del proceso de formato de código.

Para ejecutar la herramienta black haz lo siguiente:
```bash
black .
```

## Complejidad y cumplimiento del código: Flake8
Flake8 es una herramienta popular de Python que combina múltiples herramientas de linting y comprobación de estilo de Python en un solo paquete. Ejecuta varias comprobaciones en el código Python para posibles errores, violaciones de estilo de código y adhesión a las directrices de estilo PEP 8. Flake8 integra herramientas como PyFlakes, pycodestyle (anteriormente conocido como pep8) y el comprobador de complejidad McCabe, permitiendo a los desarrolladores detectar errores y hacer cumplir los estándares de codificación en su base de código Python. Se utiliza comúnmente como parte del flujo de trabajo de desarrollo para mantener la calidad del código y la legibilidad.

Para ejecutar flake8 haz lo siguiente:
```bash
flake8 .
```

## Linting del código: Pylint
Pylint es una herramienta de linting de código Python que analiza el código fuente para detectar errores de programación, problemas de estilo de código y convenciones de codificación. Pylint comprueba el código Python para posibles problemas como errores de sintaxis, variables no utilizadas, nombres de variables no convencionales y otras violaciones de las directrices de codificación. Es una herramienta valiosa para mejorar la calidad del código, identificar problemas de codificación y mantener la coherencia en los estándares de codificación.

Para ejecutar la herramienta pylint haz lo siguiente:
```bash
pylint fakenos
```

## Cobertura de código: coverage
La cobertura es una herramienta utilizada en el desarrollo de software para medir el grado en que se ejecuta el código fuente de un programa durante las pruebas. Ayuda a los desarrolladores a comprender hasta qué punto sus pruebas ejercen el código fuente proporcionando métricas de cobertura de código, normalmente expresadas como un porcentaje. Las herramientas de cobertura siguen qué líneas o ramas de código se ejecutan durante las pruebas y generan informes que destacan las áreas que están cubiertas y las que no lo están. Esta información permite a los desarrolladores identificar rutas de código no probadas y mejorar la efectividad de sus esfuerzos de pruebas.

Para ejecutar la cobertura en conjunto con pytest haz lo siguiente:
```bash
coverage run -m pytest
```

Generará un informe que se puede ver en `coverage report -m` o `coverage html`.