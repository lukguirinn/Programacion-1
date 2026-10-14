from funciones import agregar_patentes
from funciones import convertir_mayusculas
from funciones import validar_patente, buscar_patente
from funciones import buscar_patente_vieja, buscar_patente_nueva
from funciones import informar_porcentaje_letras, ordenar_patentes


lista_patentes = []
opcion = "S"
patentes_generadas = False

while opcion == "S":

    print("\n===== SISTEMA DE PATENTES =====")
    print("1. Generar patentes.")
    print("2. Buscar patente.")
    print("3. Informar estadísticas.")
    print("4. Ordenar y mostrar patentes.")
    print("5. Salir.")
    print("==============================")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        cantidad_solicitada = int(input(
            "Ingrese la cantidad de patentes que desea generar: "
        ))

        if cantidad_solicitada > 0:
            lista_patentes = agregar_patentes(lista_patentes,cantidad_solicitada)

            patentes_generadas = True

            print("\nPatentes almacenadas:")

            for i in range(len(lista_patentes)):
                print(lista_patentes[i])

            print("Total de patentes:", len(lista_patentes))

        else:
            print("La cantidad debe ser mayor que cero.")

    elif opcion == "2":
        if patentes_generadas == False:
            print("Primero debe generar las patentes.")

        else:
            patente_buscada = input(
                "Ingrese la patente que desea buscar: "
            )

            patente_buscada = convertir_mayusculas(patente_buscada)

            if validar_patente(patente_buscada) == False:
                print("Formato de patente incorrecto.")

            else:
                if buscar_patente(lista_patentes, patente_buscada) == True:
                    print("La patente fue encontrada.")
                else:
                    print("La patente no fue encontrada.")

    elif opcion == "3":
        if patentes_generadas == False:
            print("Primero debe generar las patentes.")

        else:
            patente_vieja = buscar_patente_vieja(lista_patentes)
            patente_nueva = buscar_patente_nueva(lista_patentes)

            print("La patente más vieja es:", patente_vieja)
            print("La patente más nueva es:", patente_nueva)

            print("\nPorcentaje según letra inicial:")
            informar_porcentaje_letras(lista_patentes)

    elif opcion == "4":
        if patentes_generadas == False:
            print("Primero debe generar las patentes.")

        else:
            criterio = input("Ingrese el criterio (ASC/DESC): ")
            criterio = convertir_mayusculas(criterio)

            while criterio != "ASC" and criterio != "DESC":
                print("Criterio incorrecto. Ingrese ASC o DESC.")

                criterio = input("Ingrese el criterio (ASC/DESC): ")
                criterio = convertir_mayusculas(criterio)

            lista_patentes = ordenar_patentes(
                lista_patentes,
                criterio
            )

            if criterio == "ASC":
                print("Patentes ordenadas ASCENDENTEMENTE:")
            else:
                print("Patentes ordenadas DESCENDENTEMENTE:")

            for i in range(len(lista_patentes)):
                print(lista_patentes[i])

    elif opcion == "5":
        print("Programa finalizado.")

    else:
        print("Opción incorrecta.")

    if opcion != "5":
        opcion = "S"