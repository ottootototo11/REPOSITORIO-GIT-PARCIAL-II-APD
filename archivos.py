
import json
import os
RUTA_ARCHIVO: str = os.path.join(os.path.dirname(os.path.abspath(__file__)), "alumnos.json")


def cargar_alumnos() -> dict[str, dict]:
    """Carga los alumnos desde alumnos.json.

    Si el archivo no existe, devuelve un diccionario vacío (la primera vez
    que se ejecuta el programa). Si el archivo está dañado, avisa y también
    devuelve un diccionario vacío en lugar de romper el programa.

    Returns:
        Diccionario {dni: {"nombre", "apellido", "edad", "nota"}}.
    """
    if not os.path.exists(RUTA_ARCHIVO):
        return {}

    try:
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except (json.JSONDecodeError, OSError):
        print("Aviso: no se pudo leer alumnos.json. Se inicia con datos vacíos.")
        return {}


def guardar_alumnos(alumnos: dict[str, dict]) -> None:
    """Guarda todos los alumnos en alumnos.json (sobrescribe el contenido anterior).

    Args:
        alumnos: Diccionario de alumnos a persistir.
    """
    with open(RUTA_ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(alumnos, archivo, indent=4, ensure_ascii=False)
