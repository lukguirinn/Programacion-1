
from funciones import *


ruta = "juegos.csv"


juegos = cargar_juegos(ruta)

opcion = 0

while opcion != 5:

    print("\n========== GESTION DE VIDEOJUEGOS ==========")
    print("1 - Alta de videojuego")
    print("2 - Registrar una venta")
    print("3 - Consultar estadísticas")
    print("4 - Mostrar catálogo ordenado")
    print("5 - Salir")

    opcion_texto = input("\nIngresá una opción: ")

    while opcion_texto.isdigit() == False or int(opcion_texto) < 1 or int(opcion_texto) > 5:
        print("Opción inválida.")
        opcion_texto = input("Ingresá una opción entre 1 y 5: ")

    opcion = int(opcion_texto)

    if opcion == 1:

        juegos = alta_videojuego(juegos)
        guardar_juegos(juegos, ruta)

    elif opcion == 2:

        juegos = registrar_venta(juegos)
        guardar_juegos(juegos, ruta)

    elif opcion == 3:

        consultar_estadisticas(juegos)

    elif opcion == 4:

        print("\nCriterios de ordenamiento:")
        print("Nombre")
        print("Género")
        print("Precio")

        criterio = input("Ingresá el criterio: ").strip().lower()

        while criterio != "nombre" and criterio != "genero" and criterio != "precio":
            print("Criterio inválido.")
            criterio = input("Ingresá nombre, género o precio: ").strip().lower()

        orden = input("¿Ascendente o descendente? ").strip().lower()

        while orden != "asc" and orden != "desc":
            print("Orden inválido.")
            orden = input("Ingresá Asc o Desc: ").strip().lower()

        if orden == "asc":
            ascendente = True
        else:
            ascendente = False

        juegos = ordenar_catalogo(juegos, criterio, ascendente)

        mostrar_catalogo(juegos)

    elif opcion == 5:

        print("\nFinalizando el programa...")

print("\nPrograma finalizado.")
