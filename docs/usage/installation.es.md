# Instalación

## PyPi (Recomendado)
FakeNOS ha sido publicado en PyPi. Para instalarlo usando `pip` solo tienes que ejecutar el siguiente comando
```bash
python3 -m pip install fakenos
```

## Git
Los siguientes métodos no se recomiendan a menos que estés haciendo desarrollo. Si este es el caso, entonces recomendamos seguir el método `poetry`, ya que tiene todas las características y hará que tu proceso de desarrollo sea más fácil.

### Usando pip
Antes de instalar de esta manera, necesitas descargar e instalar [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git). Si ya has instalado `git` solo tienes que ejecutar el siguiente comando:
```bash
python3 -m pip install git+https://github.com/fakenos/fakenos
```

# Usando poetry (Recomendado para dev)
FakeNOS utiliza [Poetry](https://python-poetry.org/) para gestionar dependencias y entornos virtuales. Sigue los pasos a continuación para instalar FakeNOS usando Poetry:

```{ .bash .annotate }
python3 -m pip install poetry                  # (1)
git clone https://github.com/fakenos/fakenos   # (2)
cd fakenos                                     # (3)
poetry install                                 # (4)
```

1.  Instala Poetry
2.  Clona el repositorio de FakeNOS de la rama principal de GitHub
3.  Navega hasta la carpeta fakenos
4.  Ejecuta poetry para crear el entorno virtual e instalar las dependencias
