# Añadir nuevas plataformas
FakeNOS está diseñado para ser fácilmente extensible. Está diseñado de tal manera
que añadir nuevas plataformas es simple y se puede hacer utilizando diferentes
métodos. Por el momento, solo es posible utilizar módulos de Python o archivos YAML.

!!! tip 
    Hay implementado un hot-reloader que recarga automáticamente los módulos de Python
    y YAML cuando se modifican dentro de `fakenos/plugins/nos`. Para ejecutarlo
    simplemente hacer `fakenos --reload-commands`.

## Archivos YAML
Este es el método preferido en caso de que la plataforma que desea implementar no
exista todavía. La gran ventaja de este método es que es bastante simple
añadir nuevas plataformas. Sin embargo, no es tan flexible como el método de módulos de Python
ya que no es posible implementar un comportamiento dinámico.

Los archivos YAML se encuentran en el directorio `fakenos/plugins/nos/platforms_yaml`.

## Módulos de Python
Este método es más flexible que el método de archivos YAML. Es posible implementar
comportamiento dinámico y utilizar todo el potencial de Python. Sin embargo, es un poco más difícil de
implementar. Los módulos de Python se encuentran en el paquete `fakenos/plugins/nos/platforms_py`.
