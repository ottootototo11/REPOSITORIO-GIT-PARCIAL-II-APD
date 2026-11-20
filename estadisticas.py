
NOTA_APROBACION: int = 6

def cantidad_total(alumnos: dict[str, dict]) -> int:
    """Devuelve la cantidad total de alumnos registrados."""
    return len(alumnos)


def promedio_notas(alumnos: dict[str, dict]) -> float:
    """Devuelve el promedio de notas (0 si no hay alumnos).

    Args:
        alumnos: Diccionario de alumnos.

    Returns:
        Promedio de las notas finales.
    """
    if not alumnos:
        return 0.0
    total = sum(datos["nota"] for datos in alumnos.values())
    return total / len(alumnos)


def alumnos_mayor_nota(alumnos: dict[str, dict]) -> list[tuple[str, dict]]:
    """Devuelve el/los alumnos con la mayor nota (puede haber empate).

    Args:
        alumnos: Diccionario de alumnos.

    Returns:
        Lista de tuplas (dni, datos). Vacía si no hay alumnos.
    """
    if not alumnos:
        return []
    maxima = max(datos["nota"] for datos in alumnos.values())
    return [(dni, datos) for dni, datos in alumnos.items() if datos["nota"] == maxima]


def contar_aprobados(alumnos: dict[str, dict]) -> int:
    """Cuenta los alumnos con nota mayor o igual a 6."""
    return sum(1 for datos in alumnos.values() if datos["nota"] >= NOTA_APROBACION)


def contar_desaprobados(alumnos: dict[str, dict]) -> int:
    """Cuenta los alumnos con nota menor a 6."""
    return sum(1 for datos in alumnos.values() if datos["nota"] < NOTA_APROBACION)


def mostrar_estadisticas(alumnos: dict[str, dict]) -> None:
    """Imprime por pantalla todas las estadísticas.

    Args:
        alumnos: Diccionario de alumnos.
    """
    print("\n--- ESTADÍSTICAS ---")
    if not alumnos:
        print("No hay alumnos registrados.")
        return

    print(f"Cantidad total de alumnos: {cantidad_total(alumnos)}")
    print(f"Promedio de notas: {promedio_notas(alumnos):.2f}")
    for dni, datos in alumnos_mayor_nota(alumnos):
        print(f"Mayor nota: {datos['nombre']} {datos['apellido']} (DNI {dni}) - {datos['nota']}")
    print(f"Aprobados (>= {NOTA_APROBACION}): {contar_aprobados(alumnos)}")
    print(f"Desaprobados (< {NOTA_APROBACION}): {contar_desaprobados(alumnos)}")
