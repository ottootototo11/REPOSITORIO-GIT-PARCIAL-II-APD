
import archivos
import validaciones

def pedir_dni_nuevo(alumnos: dict[str, dict]) -> str:
    """Pide un DNI válido que todavía no esté registrado.

    Args:
        alumnos: Diccionario de alumnos existentes.

    Returns:
        DNI válido y no duplicado.
    """
    while True:
        dni = input("DNI: ").strip()
        if not validaciones.validar_dni(dni):
            print("Error: el DNI debe tener solo números (7 u 8 dígitos).")
        elif validaciones.dni_existe(dni, alumnos):
            print("Error: ya existe un alumno con ese DNI.")
        else:
            return dni


def pedir_texto(etiqueta: str) -> str:
    """Pide un texto (nombre o apellido) hasta que sea válido.

    Args:
        etiqueta: Nombre del campo que se muestra al usuario.

    Returns:
        Texto válido, con la primera letra de cada palabra en mayúscula.
    """
    while True:
        texto = input(f"{etiqueta}: ").strip()
        if validaciones.validar_texto(texto):
            return texto.title()
        print(f"Error: el campo {etiqueta.lower()} solo admite letras y no puede estar vacío.")


def pedir_edad() -> int:
    """Pide una edad entera no negativa hasta que sea válida.

    Returns:
        Edad válida.
    """
    while True:
        entrada = input("Edad: ").strip()
        try:
            edad = int(entrada)
        except ValueError:
            print("Error: la edad debe ser un número entero.")
            continue
        if validaciones.validar_edad(edad):
            return edad
        print(f"Error: la edad debe estar entre 0 y {validaciones.EDAD_MAXIMA}.")


def pedir_nota() -> float:
    """Pide una nota entre 0 y 10 hasta que sea válida.

    Returns:
        Nota válida (int si es un número entero, float si tiene decimales).
    """
    while True:
        entrada = input("Nota final (0-10): ").strip().replace(",", ".")
        try:
            nota = float(entrada)
        except ValueError:
            print("Error: la nota debe ser un número.")
            continue
        if validaciones.validar_nota(nota):
            return int(nota) if nota.is_integer() else nota
        print("Error: la nota debe estar entre 0 y 10.")


def pedir_dni_existente(alumnos: dict[str, dict]) -> str | None:
    """Pide un DNI y verifica que corresponda a un alumno registrado.

    Args:
        alumnos: Diccionario de alumnos.

    Returns:
        El DNI si existe, o None si no se encontró (ya informa el error).
    """
    dni = input("DNI del alumno: ").strip()
    if not validaciones.dni_existe(dni, alumnos):
        print("No se encontró ningún alumno con ese DNI.")
        return None
    return dni


def formatear_alumno(dni: str, datos: dict) -> str:
    """Devuelve el texto de un alumno con el formato sugerido.

    Args:
        dni: DNI del alumno (clave del diccionario).
        datos: Diccionario con nombre, apellido, edad y nota.

    Returns:
        Texto de varias líneas listo para imprimir.
    """
    return (
        f"DNI: {dni}\n"
        f"Nombre: {datos['nombre']}\n"
        f"Apellido: {datos['apellido']}\n"
        f"Edad: {datos['edad']}\n"
        f"Nota: {datos['nota']}"
    )

def registrar_alumno(alumnos: dict[str, dict]) -> None:
    """Registra un alumno nuevo y guarda el archivo.

    Args:
        alumnos: Diccionario de alumnos (se modifica).
    """
    print("\n--- REGISTRAR ALUMNO ---")
    dni = pedir_dni_nuevo(alumnos)
    alumnos[dni] = {
        "nombre": pedir_texto("Nombre"),
        "apellido": pedir_texto("Apellido"),
        "edad": pedir_edad(),
        "nota": pedir_nota(),
    }
    archivos.guardar_alumnos(alumnos)
    print("Alumno registrado correctamente.")


def listar_alumnos(alumnos: dict[str, dict]) -> None:
    """Muestra todos los alumnos registrados.

    Args:
        alumnos: Diccionario de alumnos.
    """
    print("\n--- LISTA DE ALUMNOS ---")
    if not alumnos:
        print("No hay alumnos registrados.")
        return
    for dni, datos in alumnos.items():
        print(formatear_alumno(dni, datos))
        print()


def buscar_alumno(alumnos: dict[str, dict]) -> None:
    """Busca un alumno por DNI y lo muestra.

    Args:
        alumnos: Diccionario de alumnos.
    """
    print("\n--- BUSCAR ALUMNO ---")
    dni = pedir_dni_existente(alumnos)
    if dni is not None:
        print(formatear_alumno(dni, alumnos[dni]))


def modificar_alumno(alumnos: dict[str, dict]) -> None:
    """Modifica nombre, apellido, edad o nota de un alumno y guarda el archivo.

    Args:
        alumnos: Diccionario de alumnos (se modifica).
    """
    print("\n--- MODIFICAR ALUMNO ---")
    dni = pedir_dni_existente(alumnos)
    if dni is None:
        return

    print(formatear_alumno(dni, alumnos[dni]))
    print("\n¿Qué desea modificar?")
    print("1. Nombre\n2. Apellido\n3. Edad\n4. Nota\n5. Cancelar")
    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        alumnos[dni]["nombre"] = pedir_texto("Nuevo nombre")
    elif opcion == "2":
        alumnos[dni]["apellido"] = pedir_texto("Nuevo apellido")
    elif opcion == "3":
        alumnos[dni]["edad"] = pedir_edad()
    elif opcion == "4":
        alumnos[dni]["nota"] = pedir_nota()
    elif opcion == "5":
        print("Modificación cancelada.")
        return
    else:
        print("Opción incorrecta.")
        return

    archivos.guardar_alumnos(alumnos)
    print("Alumno modificado correctamente.")


def eliminar_alumno(alumnos: dict[str, dict]) -> None:
    """Elimina un alumno por DNI (con confirmación) y guarda el archivo.

    Args:
        alumnos: Diccionario de alumnos (se modifica).
    """
    print("\n--- ELIMINAR ALUMNO ---")
    dni = pedir_dni_existente(alumnos)
    if dni is None:
        return

    print(formatear_alumno(dni, alumnos[dni]))
    confirmacion = input("¿Seguro que desea eliminarlo? (s/n): ").strip().lower()
    if confirmacion == "s":
        del alumnos[dni]
        archivos.guardar_alumnos(alumnos)
        print("Alumno eliminado correctamente.")
    else:
        print("Eliminación cancelada.")
