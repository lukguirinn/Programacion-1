

import random


def cargar_juegos(ruta: str) -> list:
    """
    Lee los videojuegos almacenados en un archivo CSV.

    Parametros:
        ruta (str): Ruta del archivo.

    Retorno:
        list: Lista de diccionarios con los videojuegos.
    """
    juegos = []

    with open(ruta, "r") as archivo:
        datos = archivo.read()

    datos_limpios = datos.strip()
    lista_juegos = datos_limpios.split("\n")

    for i in range(1, len(lista_juegos)):
        valores = lista_juegos[i].split(",")

        unidades_vendidas = int(valores[5])

        if unidades_vendidas >= 0:
            videojuego = {
                "codigo_identificador": valores[0],
                "nombre": valores[1],
                "genero": valores[2],
                "precio": float(valores[3]),
                "stock": int(valores[4]),
                "unidades_vendidas": unidades_vendidas
            }

            juegos = juegos + [videojuego]
        else:
            print("Se omitio un videojuego con unidades vendidas negativas.")

    return juegos


def guardar_juegos(juegos: list, ruta: str) -> None:
    """
    Guarda todos los videojuegos en un archivo CSV.

    Parametros:
        juegos (list): Lista de videojuegos.
        ruta (str): Ruta del archivo.

    Retorno:
        None.
    """
    with open(ruta, "w") as archivo:
        archivo.write("codigo_identificador,nombre,genero,precio,stock,unidades_vendidas\n")

        for i in range(len(juegos)):
            videojuego = juegos[i]

            linea = (
                videojuego["codigo_identificador"] + "," +
                videojuego["nombre"] + "," +
                videojuego["genero"] + "," +
                str(videojuego["precio"]) + "," +
                str(videojuego["stock"]) + "," +
                str(videojuego["unidades_vendidas"]) + "\n"
            )

            archivo.write(linea)


def generar_codigo(juegos: list) -> str:
    """
    Genera un codigo identificador unico de siete digitos.

    Parametros:
        juegos (list): Lista de videojuegos existentes.

    Retorno:
        str: Codigo identificador generado.
    """
    codigo = str(random.randint(1000000, 9999999))
    repetido = True

    while repetido == True:
        repetido = False

        for i in range(len(juegos)):
            if juegos[i]["codigo_identificador"] == codigo:
                codigo = str(random.randint(1000000, 9999999))
                repetido = True

    return codigo


def validar_numero_decimal(numero: str) -> bool:
    """
    Valida si una cadena representa un numero decimal.

    Parametros:
        numero (str): Texto ingresado.

    Retorno:
        bool: True si es valido, False en caso contrario.
    """
    numero = numero.replace(",", ".")
    valido = True

    if numero == "":
        valido = False
    elif numero.count(".") > 1:
        valido = False
    else:
        numero_limpio = numero.replace(".", "")

        if numero_limpio.isdigit() == False or numero == ".":
            valido = False

    return valido


def alta_videojuego(juegos: list) -> list:
    """
    Registra un nuevo videojuego en el catalogo.

    Parametros:
        juegos (list): Lista de videojuegos existentes.

    Retorno:
        list: Lista actualizada.
    """
    generos = ["RPG", "DEPORTES", "CARRERAS", "AVENTURA", "ESTRATEGIA"]

    nombre = input("Ingrese el nombre del videojuego: ").strip()

    while len(nombre) < 3 or len(nombre) > 50:
        print("El nombre debe tener entre 3 y 50 caracteres.")
        nombre = input("Ingrese el nombre: ").strip()

    print("\nGeneros disponibles:")

    for i in range(len(generos)):
        print(generos[i].title())

    genero = input("Ingrese el genero: ").strip().upper()

    while genero not in generos:
        print("Genero invalido.")
        genero = input("Ingrese el genero: ").strip().upper()

    precio_texto = input("Ingrese el precio: ")

    while validar_numero_decimal(precio_texto) == False:
        print("Precio invalido.")
        precio_texto = input("Ingrese el precio: ")

    precio = float(precio_texto.replace(",", "."))

    while precio <= 0:
        print("El precio debe ser mayor a cero.")
        precio_texto = input("Ingrese el precio: ")

        while validar_numero_decimal(precio_texto) == False:
            print("Precio invalido.")
            precio_texto = input("Ingrese el precio: ")

        precio = float(precio_texto.replace(",", "."))

    stock_texto = input("Ingrese el stock inicial: ")

    while stock_texto.isdigit() == False or int(stock_texto) < 0:
        print("Stock invalido.")
        stock_texto = input("Ingrese el stock inicial: ")

    stock = int(stock_texto)

    codigo = generar_codigo(juegos)

    videojuego = {
        "codigo_identificador": codigo,
        "nombre": nombre.title(),
        "genero": genero.title(),
        "precio": precio,
        "stock": stock,
        "unidades_vendidas": 0
    }

    juegos = juegos + [videojuego]

    print("\nVideojuego registrado correctamente.")
    print("Codigo identificador:", codigo)

    return juegos


def mostrar_juegos_disponibles(juegos: list) -> None:
    """
    Muestra los videojuegos que tienen stock disponible.

    Parametros:
        juegos (list): Lista de videojuegos.

    Retorno:
        None.
    """
    hay_stock = False

    print("\nVIDEOJUEGOS DISPONIBLES")

    for i in range(len(juegos)):
        if juegos[i]["stock"] > 0:
            print(
                juegos[i]["codigo_identificador"],
                juegos[i]["nombre"],
                juegos[i]["genero"],
                juegos[i]["precio"],
                juegos[i]["stock"]
            )

            hay_stock = True

    if hay_stock == False:
        print("No hay videojuegos disponibles.")


def registrar_venta(juegos: list) -> list:
    """
    Registra la venta de un videojuego y actualiza su stock.

    Parametros:
        juegos (list): Lista de videojuegos.

    Retorno:
        list: Lista actualizada.
    """
    mostrar_juegos_disponibles(juegos)

    codigo = input("\nIngrese el codigo del videojuego: ").strip()
    posicion = -1

    for i in range(len(juegos)):
        if juegos[i]["codigo_identificador"] == codigo:
            posicion = i

    if posicion == -1:
        print("El codigo ingresado no existe.")
    elif juegos[posicion]["stock"] == 0:
        print("El videojuego no tiene stock disponible.")
    else:
        cantidad_texto = input("Ingrese la cantidad a vender: ")

        while cantidad_texto.isdigit() == False or int(cantidad_texto) <= 0 or int(cantidad_texto) > juegos[posicion]["stock"]:
            print("Cantidad invalida.")
            cantidad_texto = input("Ingrese la cantidad a vender: ")

        cantidad = int(cantidad_texto)

        juegos[posicion]["stock"] = juegos[posicion]["stock"] - cantidad
        juegos[posicion]["unidades_vendidas"] = juegos[posicion]["unidades_vendidas"] + cantidad

        print("Venta registrada correctamente.")

    return juegos


def consultar_estadisticas(juegos: list) -> None:
    """
    Calcula y muestra estadisticas del catalogo.

    Parametros:
        juegos (list): Lista de videojuegos.

    Retorno:
        None.
    """
    if len(juegos) == 0:
        print("No hay videojuegos registrados.")
    else:
        mayor_venta = juegos[0]["unidades_vendidas"]
        posicion_mayor = 0

        for i in range(1, len(juegos)):
            if juegos[i]["unidades_vendidas"] > mayor_venta:
                mayor_venta = juegos[i]["unidades_vendidas"]
                posicion_mayor = i

        print("\nVIDEOJUEGO MAS VENDIDO")
        print(juegos[posicion_mayor]["nombre"])
        print("Unidades vendidas:", mayor_venta)

        generos = ["RPG", "Deportes", "Carreras", "Aventura", "Estrategia"]
        unidades_genero = [0, 0, 0, 0, 0]

        for i in range(len(juegos)):
            for j in range(len(generos)):
                if juegos[i]["genero"].upper() == generos[j].upper():
                    unidades_genero[j] = unidades_genero[j] + juegos[i]["unidades_vendidas"]

        mayor_genero = unidades_genero[0]
        posicion_genero = 0

        for i in range(1, len(unidades_genero)):
            if unidades_genero[i] > mayor_genero:
                mayor_genero = unidades_genero[i]
                posicion_genero = i

        print("\nGENERO CON MAS VENTAS")
        print(generos[posicion_genero])
        print("Unidades vendidas:", mayor_genero)

        valor_inventario = 0
        sin_stock = 0

        for i in range(len(juegos)):
            valor_inventario = valor_inventario + juegos[i]["stock"] * juegos[i]["precio"]

            if juegos[i]["stock"] == 0:
                sin_stock = sin_stock + 1

        porcentaje_sin_stock = sin_stock * 100 / len(juegos)

        print("\nVALOR TOTAL DEL INVENTARIO:", valor_inventario)
        print("Videojuegos sin stock:", sin_stock)
        print("Porcentaje sin stock:", porcentaje_sin_stock, "%")

        print("\nPROMEDIO DE PRECIOS POR GENERO")

        for i in range(len(generos)):
            suma_precios = 0
            cantidad_juegos = 0

            for j in range(len(juegos)):
                if juegos[j]["genero"].upper() == generos[i].upper():
                    suma_precios = suma_precios + juegos[j]["precio"]
                    cantidad_juegos = cantidad_juegos + 1

            if cantidad_juegos > 0:
                promedio = suma_precios / cantidad_juegos
                print(generos[i], ":", promedio)
            else:
                print(generos[i], ": Sin videojuegos registrados")


def ordenar_catalogo(juegos: list, criterio: str, ascendente: bool) -> list:
    """
    Ordena el catalogo segun el criterio seleccionado.

    Parametros:
        juegos (list): Lista de videojuegos.
        criterio (str): Nombre, genero o precio.
        ascendente (bool): True ascendente, False descendente.

    Retorno:
        list: Lista ordenada.
    """
    for i in range(len(juegos) - 1):
        for j in range(i + 1, len(juegos)):
            if criterio == "nombre":
                valor_i = juegos[i]["nombre"].upper()
                valor_j = juegos[j]["nombre"].upper()
            elif criterio == "genero":
                valor_i = juegos[i]["genero"].upper()
                valor_j = juegos[j]["genero"].upper()
            else:
                valor_i = juegos[i]["precio"]
                valor_j = juegos[j]["precio"]

            if (ascendente == True and valor_i > valor_j) or (ascendente == False and valor_i < valor_j):
                aux = juegos[i]
                juegos[i] = juegos[j]
                juegos[j] = aux

    return juegos


def mostrar_catalogo(juegos: list) -> None:
    """
    Muestra todos los videojuegos del catalogo.

    Parametros:
        juegos (list): Lista de videojuegos.

    Retorno:
        None.
    """
    if len(juegos) == 0:
        print("No hay videojuegos registrados.")
    else:
        print("\nCATALOGO DE VIDEOJUEGOS")

        for i in range(len(juegos)):
            print("\nVideojuego:", i + 1)
            print("Codigo:", juegos[i]["codigo_identificador"])
            print("Nombre:", juegos[i]["nombre"])
            print("Genero:", juegos[i]["genero"])
            print("Precio:", juegos[i]["precio"])
            print("Stock:", juegos[i]["stock"])
            print("Unidades vendidas:", juegos[i]["unidades_vendidas"])
