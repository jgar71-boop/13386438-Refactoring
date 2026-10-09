# Conversor de unidades

## Clonar el repositorio

```sh
git clone https://github.com/jgar71-boop/13386438-Refactoring.git
cd 13386438-Refactoring
```

`git clone` configura automáticamente el remote `origin`. Si ya tienes una
copia local inicializada con Git pero todavía no tiene un remote, agrégalo así:

```sh
git remote add origin https://github.com/jgar71-boop/13386438-Refactoring.git
git remote -v
```

## Requisitos previos

- Python 3.8 o superior. El repositorio no define una matriz oficial de
  versiones ni un límite máximo; Python 3.14.8 es la versión usada para validar
  el proyecto actualmente.
- No se requieren dependencias externas para ejecutar el conversor: usa la
  biblioteca estándar de Python.
- Para ejecutar las pruebas se necesita `pytest>=8.0`, declarado en
  `requirements.txt`. En el entorno de validación se usa pytest 9.1.1.

## Preparar el entorno

En macOS o Linux:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

En Windows (PowerShell):

```powershell
py -3 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Ejecutar las pruebas

Desde la raíz del repositorio, con el entorno virtual activado, ejecuta toda la
suite:

```sh
python -m pytest -q
```

Para ver cada prueba mientras corre:

```sh
python -m pytest -v
```

Para ejecutar solo el archivo de pruebas del conversor:

```sh
python -m pytest tests/test_conversor.py -q
```

También puedes llamar al Python del entorno virtual sin activarlo.

macOS o Linux:

```sh
.venv/bin/python -m pytest -q
```

Windows (PowerShell):

```powershell
.venv\Scripts\python.exe -m pytest -q
```

## Ejecutar el linter

Ruff es opcional y no forma parte de las dependencias de ejecución. Con el
entorno virtual activado, instálalo y analiza el proyecto desde su raíz:

```sh
python -m pip install ruff
python -m ruff check .
```
