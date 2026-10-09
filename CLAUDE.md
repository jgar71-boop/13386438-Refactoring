# Instrucciones del proyecto

## Contexto

Proyecto Python para convertir temperaturas, distancias y masas. La lógica está
en `conversor.py`; `cli.py` expone las conversiones por línea de comandos, y
`tests/` contiene las pruebas con pytest.

## Preparar el entorno

Desde la raíz del proyecto, en macOS o Linux:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Comandos habituales

Ejecutar todas las pruebas:

```sh
python -m pytest -q
```

Listar conversiones y ejecutar una conversión:

```sh
python cli.py --listar
python cli.py 100 c2f
```

Ejemplos de claves: `c2f`, `f2c`, `km2mi`, `mi2km`, `kg2lb` y `lb2kg`.
La CLI devuelve código `0` si la operación termina correctamente, `1` ante un
error de conversión y `2` si faltan argumentos.

## Convenciones

- Mantener los cálculos y validaciones en `conversor.py`; reservar `cli.py` para
	argumentos, presentación y códigos de salida.
- Mantener las claves de conversión existentes y el registro `CONVERSIONES` como
	punto central para despachar operaciones.
- Usar nombres descriptivos en `snake_case` para funciones y variables, y
	`UPPER_SNAKE_CASE` para constantes. Añadir anotaciones de tipos a funciones
	nuevas o modificadas.
- En `convertir()`, rechazar entradas no finitas (`NaN`, `inf`, `-inf`) antes de
	ejecutar la conversión y rechazar resultados no finitos antes del redondeo.
	Usar `ValueError` para valores inválidos y `KeyError` para claves desconocidas.
- No imprimir desde las funciones de conversión. La CLI debe encargarse de los
	mensajes, escribir errores en `stderr` y mostrar el mensaje original de la
	excepción sin manipular su representación. Mantener los códigos de salida:
	`0` para éxito, `1` para errores de conversión y `2` para argumentos faltantes.
- Mantener el redondeo de salida centralizado en `convertir()` salvo que se
	actualice explícitamente el contrato y sus pruebas.
- Añadir pruebas pytest para conversiones nuevas, valores conocidos, límites,
  negativos, valores no finitos, overflow y claves desconocidas. Para cambios en
  la CLI, comprobar también el mensaje en `stderr` y el código de retorno.
- Preferir la biblioteca estándar; si se añade una dependencia externa,
	declararla en `requirements.txt`.
- Mantener los cambios acotados al comportamiento solicitado y no editar el
	entorno virtual ni los archivos generados.
