# test_conversor.py
# Suite de pruebas del conversor (parcial: no cubre todas las funciones)

from typing import Callable

import pytest

from cli import main
from conversor import (
    celsius_a_fahrenheit,
    convertir,
    kg_a_libras,
    km_a_millas,
    libras_a_kg,
    millas_a_km,
)


def test_celsius_a_fahrenheit_punto_ebullicion() -> None:
    # 100 °C es el punto de ebullición del agua: 212 °F
    assert celsius_a_fahrenheit(100) == 212


def test_celsius_a_fahrenheit_punto_congelacion() -> None:
    # 0 °C corresponde a 32 °F
    assert celsius_a_fahrenheit(0) == 32


def test_km_a_millas_valor_conocido() -> None:
    # 10 km son aproximadamente 6.21 millas
    assert km_a_millas(10) == pytest.approx(6.21371)


@pytest.mark.parametrize(
    ("funcion_conversion", "valor_negativo", "mensaje_esperado"),
    [
        (km_a_millas, -1, "La distancia no puede ser negativa"),
        (millas_a_km, -1, "La distancia no puede ser negativa"),
        (kg_a_libras, -1, "La masa no puede ser negativa"),
        (libras_a_kg, -1, "La masa no puede ser negativa"),
    ],
)
def test_conversiones_rechazan_valores_negativos(
    funcion_conversion: Callable[[float], float],
    valor_negativo: float,
    mensaje_esperado: str,
) -> None:
    with pytest.raises(ValueError, match=mensaje_esperado):
        funcion_conversion(valor_negativo)


@pytest.mark.parametrize(
    "valor_entrada",
    [float("nan"), float("inf"), float("-inf")],
)
def test_convertir_rechaza_entradas_no_finitas(valor_entrada: float) -> None:
    with pytest.raises(ValueError, match="valor de entrada debe ser finito"):
        convertir(valor_entrada, "c2f")


def test_convertir_rechaza_resultados_no_finitos() -> None:
    with pytest.raises(ValueError, match="resultado de la conversión no es finito"):
        convertir(2.1e307, "c2f")


def test_cli_muestra_el_mensaje_original_de_clave_invalida(
    capsys: pytest.CaptureFixture[str],
) -> None:
    codigo_salida = main(["5", "xyz"])
    salida = capsys.readouterr()

    assert codigo_salida == 1
    assert salida.err.startswith("Error: Conversión no soportada: xyz.")
    assert not salida.err.startswith("Error: '")


def test_convertir_clave_invalida() -> None:
    # Una clave inexistente debe producir un KeyError
    with pytest.raises(KeyError):
        convertir(5, "leguas2parsecs")
