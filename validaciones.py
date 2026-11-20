
EDAD_MAXIMA: int = 120
NOTA_MINIMA: int = 0
NOTA_MAXIMA: int = 10


def validar_dni(dni: str) -> bool:
    """Verifica que el DNI tenga solo dígitos y entre 7 y 8 caracteres.

    Args:
        dni: DNI ingresado como texto.

    Returns:
        True si el formato es válido, False en caso contrario.
    """
    return dni.isascii() and dni.isdigit() and 7 <= len(dni) <= 8


def validar_texto(texto: str) -> bool:
    """Verifica que un nombre o apellido no esté vacío y solo tenga letras y espacios.

    Args:
        texto: Nombre o apellido a validar.

    Returns:
        True si es válido, False en caso contrario.
    """
    return texto.strip().replace(" ", "").isalpha()


def validar_edad(edad: int) -> bool:
    """Verifica que la edad no sea negativa (y que sea razonable).

    Args:
        edad: Edad del alumno.

    Returns:
        True si 0 <= edad <= EDAD_MAXIMA, False en caso contrario.
    """
    return 0 <= edad <= EDAD_MAXIMA


def validar_nota(nota: float) -> bool:
    """Verifica que la nota esté dentro del rango 0-10.

    Args:
        nota: Nota final del alumno.

    Returns:
        True si NOTA_MINIMA <= nota <= NOTA_MAXIMA, False en caso contrario.
    """
    return NOTA_MINIMA <= nota <= NOTA_MAXIMA


def dni_existe(dni: str, alumnos: dict[str, dict]) -> bool:
    """Indica si un DNI ya está registrado (sirve para evitar duplicados).

    Args:
        dni: DNI a buscar.
        alumnos: Diccionario de alumnos cuyas claves son los DNI.

    Returns:
        True si el DNI ya existe, False si no.
    """
    return dni in alumnos
