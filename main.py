
import alumnos
import archivos
import estadisticas


def mostrar_menu() -> None:
    """Imprime el menú de opciones."""
    print("\n======== GESTIÓN DE ALUMNOS ========\n")
    print("1. Registrar alumno")
    print("2. Listar alumnos")
    print("3. Buscar alumno")
    print("4. Modificar alumno")
    print("5. Eliminar alumno")
    print("6. Ver estadísticas")
    print("7. Salir")


def main() -> None:
    """Carga los datos del JSON y ejecuta el menú hasta que el usuario sale."""
    datos = archivos.cargar_alumnos()

    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "1":
            alumnos.registrar_alumno(datos)
        elif opcion == "2":
            alumnos.listar_alumnos(datos)
        elif opcion == "3":
            alumnos.buscar_alumno(datos)
        elif opcion == "4":
            alumnos.modificar_alumno(datos)
        elif opcion == "5":
            alumnos.eliminar_alumno(datos)
        elif opcion == "6":
            estadisticas.mostrar_estadisticas(datos)
        elif opcion == "7":
            print("¡Hasta luego!")
            break
        else:
            print("Opción incorrecta. Elija un número del 1 al 7.")


if __name__ == "__main__":
    main()
