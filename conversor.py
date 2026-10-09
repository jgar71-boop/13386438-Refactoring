import math

# conversor.py
# Módulo principal del conversor de unidades.
# Contiene las funciones de conversión y el registro de conversiones disponibles.

# Factores de conversión (valores de referencia internacionales)
FACTOR_KM_A_MILLAS = 0.621371
FACTOR_KG_A_LIBRAS = 2.20462

# Límite físico inferior para temperaturas en grados Celsius
CERO_ABSOLUTO_C = -273.15


def celsius_a_fahrenheit(temperatura_celsius: float) -> float:
    # Valida que la temperatura sea físicamente posible
    if temperatura_celsius < CERO_ABSOLUTO_C:
        raise ValueError("Temperatura por debajo del cero absoluto")
    return temperatura_celsius * 9 / 5 + 32


def fahrenheit_a_celsius(temperatura_fahrenheit: float) -> float:
    # Convierte grados Fahrenheit a Celsius
    temperatura_celsius = (temperatura_fahrenheit - 32) * 9 / 5
    if temperatura_celsius < CERO_ABSOLUTO_C:
        raise ValueError("Temperatura por debajo del cero absoluto")
    return temperatura_celsius


def _validar_valor_no_negativo(valor: float, nombre_magnitud: str) -> None:
    if valor < 0:
        raise ValueError(f"{nombre_magnitud} no puede ser negativa")


def km_a_millas(distancia_kilometros: float) -> float:
    # Las distancias negativas no tienen sentido físico
    _validar_valor_no_negativo(distancia_kilometros, "La distancia")
    return distancia_kilometros * FACTOR_KM_A_MILLAS


def millas_a_km(distancia_millas: float) -> float:
    _validar_valor_no_negativo(distancia_millas, "La distancia")
    return distancia_millas / FACTOR_KM_A_MILLAS


def kg_a_libras(masa_kilogramos: float) -> float:
    # Las masas negativas no tienen sentido físico
    _validar_valor_no_negativo(masa_kilogramos, "La masa")
    return masa_kilogramos * FACTOR_KG_A_LIBRAS


def libras_a_kg(masa_libras: float) -> float:
    _validar_valor_no_negativo(masa_libras, "La masa")
    return masa_libras / FACTOR_KG_A_LIBRAS


# Registro central: clave de conversión -> (función, descripción)
CONVERSIONES = {
    "c2f": (celsius_a_fahrenheit, "Celsius a Fahrenheit"),
    "f2c": (fahrenheit_a_celsius, "Fahrenheit a Celsius"),
    "km2mi": (km_a_millas, "Kilómetros a millas"),
    "mi2km": (millas_a_km, "Millas a kilómetros"),
    "kg2lb": (kg_a_libras, "Kilogramos a libras"),
    "lb2kg": (libras_a_kg, "Libras a kilogramos"),
}


def convertir(valor_entrada: float, clave_conversion: str) -> float:
    # Punto de entrada único para todas las conversiones
    configuracion_conversion = CONVERSIONES.get(clave_conversion)
    if configuracion_conversion is None:
        claves_disponibles = ", ".join(sorted(CONVERSIONES))
        raise KeyError(
            f"Conversión no soportada: {clave_conversion}. "
            f"Usa una de: {claves_disponibles}"
        )
    funcion_conversion, _ = configuracion_conversion
    if not math.isfinite(valor_entrada):
        raise ValueError("El valor de entrada debe ser finito")

    resultado_conversion = funcion_conversion(valor_entrada)
    if not math.isfinite(resultado_conversion):
        raise ValueError("El resultado de la conversión no es finito")

    # Redondeamos a 4 decimales para una salida consistente
    return round(resultado_conversion, 4)
