# cli.py
# Interfaz de línea de comandos del conversor de unidades.
# Uso: python cli.py VALOR CLAVE   |   python cli.py --listar

import argparse
import sys
from typing import Optional, Sequence

from conversor import CONVERSIONES, convertir


def construir_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="conversor",
        description="Conversor de unidades de línea de comandos",
    )
    parser.add_argument(
        "valor_entrada",
        nargs="?",
        type=float,
        help="Valor numérico a convertir",
    )
    parser.add_argument(
        "clave_conversion",
        nargs="?",
        help="Clave de conversión (ej. c2f, km2mi). Usa --listar para verlas todas",
    )
    parser.add_argument(
        "--listar",
        action="store_true",
        help="Muestra las conversiones disponibles",
    )
    return parser


def listar_conversiones() -> None:
    # Imprime la tabla de conversiones disponibles
    print("Conversiones disponibles:")
    conversiones_ordenadas = sorted(CONVERSIONES.items())
    for clave_conversion, (_, descripcion_conversion) in conversiones_ordenadas:
        print(f"  {clave_conversion:8s} {descripcion_conversion}")


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = construir_parser()
    argumentos_cli = parser.parse_args(argv)

    if argumentos_cli.listar:
        listar_conversiones()
        return 0

    # Sin --listar se requieren ambos argumentos posicionales
    if (
        argumentos_cli.valor_entrada is None
        or argumentos_cli.clave_conversion is None
    ):
        parser.print_usage()
        print("Error: se requieren VALOR y CLAVE (o usa --listar)", file=sys.stderr)
        return 2

    try:
        valor_convertido = convertir(
            argumentos_cli.valor_entrada,
            argumentos_cli.clave_conversion,
        )
    except (ValueError, KeyError) as error_conversion:
        mensaje_error = (
            error_conversion.args[0]
            if isinstance(error_conversion, KeyError)
            else str(error_conversion)
        )
        print(f"Error: {mensaje_error}", file=sys.stderr)
        return 1

    print(valor_convertido)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
