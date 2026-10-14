import random

# PUNTO 1: GENERAR PATENTE

def generar_letra() -> str:
    """
    Genera una letra mayúscula aleatoria utilizando ASCII.

    Parámetros:
        No recibe parámetros.

    Retorna:
        str: Una letra mayúscula entre A y Z.
    """
    codigo = random.randint(65, 90)
    letra = chr(codigo)
    return letra


def generar_numero() -> str:
    """
    Genera un dígito numérico aleatorio utilizando ASCII.

    Parámetros:
        No recibe parámetros.

    Retorna:
        str: Un carácter numérico entre 0 y 9.
    """
    numero = random.randint(0, 9)
    caracter = chr(numero + 48)
    return caracter


def generar_patente() -> str:
    """
    Genera una patente con el formato LLNNNLL.

    Parámetros:
        No recibe parámetros.

    Retorna:
        str: Una patente con dos letras, tres números y dos letras.
    """
    patente_nueva = ""

    patente_nueva = patente_nueva + generar_letra()
    patente_nueva = patente_nueva + generar_letra()

    patente_nueva = patente_nueva + generar_numero()
    patente_nueva = patente_nueva + generar_numero()
    patente_nueva = patente_nueva + generar_numero()

    patente_nueva = patente_nueva + generar_letra()
    patente_nueva = patente_nueva + generar_letra()

    return patente_nueva


def patente_repetida(lista_patentes: list, patente_nueva: str) -> bool:
    """
    Comprueba si una patente ya existe en la lista.

    Parámetros:
        lista_patentes (list): Lista de patentes almacenadas.
        patente_nueva (str): Patente que se desea comprobar.

    Retorna:
        bool: True si existe, False si no existe.
    """
    existe_patente = False

    for i in range(len(lista_patentes)):
        if lista_patentes[i] == patente_nueva:
            existe_patente = True

    return existe_patente


def agregar_patentes(lista_patentes: list, cantidad_solicitada: int) -> list:
    """
    Agrega la cantidad solicitada de patentes sin repetir.

    Parámetros:
        lista_patentes (list): Lista de patentes almacenadas.
        cantidad_solicitada (int): Cantidad de patentes nuevas a generar.

    Retorna:
        list: Lista actualizada con las nuevas patentes.
    """
    contador_generadas = 0

    while contador_generadas < cantidad_solicitada:
        patente_nueva = generar_patente()

        if patente_repetida(lista_patentes, patente_nueva) == False:
            lista_patentes = lista_patentes + [patente_nueva]
            contador_generadas = contador_generadas + 1

    return lista_patentes


# PUNTO 2: BUSCAR PATENTES

def convertir_mayusculas(texto: str) -> str:
    """
    Convierte las letras minúsculas de un texto en mayúsculas.

    Parámetros:
        texto (str): Texto que se desea convertir.

    Retorna:
        str: Texto con las letras convertidas a mayúsculas.
    """
    texto_convertido = ""

    for i in range(len(texto)):
        caracter = texto[i]

        if caracter >= "a" and caracter <= "z":
            for codigo in range(65, 91):
                letra_mayuscula = chr(codigo)
                letra_minuscula = chr(codigo + 32)

                if caracter == letra_minuscula:
                    caracter = letra_mayuscula

        texto_convertido = texto_convertido + caracter

    return texto_convertido


def validar_patente(patente: str) -> bool:
    """
    Valida que una patente tenga el formato LLNNNLL.

    Parámetros:
        patente (str): Patente que se desea validar.

    Retorna:
        bool: True si el formato es correcto, False si es incorrecto.
    """
    formato_correcto = True

    if len(patente) != 7:
        formato_correcto = False

    else:
        if patente[0] < "A" or patente[0] > "Z":
            formato_correcto = False

        if patente[1] < "A" or patente[1] > "Z":
            formato_correcto = False

        if patente[2] < "0" or patente[2] > "9":
            formato_correcto = False

        if patente[3] < "0" or patente[3] > "9":
            formato_correcto = False

        if patente[4] < "0" or patente[4] > "9":
            formato_correcto = False

        if patente[5] < "A" or patente[5] > "Z":
            formato_correcto = False

        if patente[6] < "A" or patente[6] > "Z":
            formato_correcto = False

    return formato_correcto


def buscar_patente(lista_patentes: list, patente_buscada: str) -> bool:
    """
    Busca una patente dentro de la lista almacenada.

    Parámetros:
        lista_patentes (list): Lista de patentes almacenadas.
        patente_buscada (str): Patente que se desea encontrar.

    Retorna:
        bool: True si la encuentra, False si no existe.
    """
    encontrada = False

    for i in range(len(lista_patentes)):
        if lista_patentes[i] == patente_buscada:
            encontrada = True

    return encontrada


# PUNTO 3: INFORMAR ESTADISTICAS

def buscar_patente_vieja(lista_patentes: list) -> str:
    """
    Busca la patente con el menor número central.

    Parámetros:
        lista_patentes (list): Lista de patentes almacenadas.

    Retorna:
        str: Patente con el menor número central.
    """
    patente_vieja = lista_patentes[0]

    for i in range(len(lista_patentes)):
        numero_actual = int(lista_patentes[i][2:5])
        numero_viejo = int(patente_vieja[2:5])

        if numero_actual < numero_viejo:
            patente_vieja = lista_patentes[i]

    return patente_vieja


def buscar_patente_nueva(lista_patentes: list) -> str:
    """
    Busca la patente con el mayor número central.

    Parámetros:
        lista_patentes (list): Lista de patentes almacenadas.

    Retorna:
        str: Patente con el mayor número central.
    """
    patente_nueva = lista_patentes[0]

    for i in range(len(lista_patentes)):
        numero_actual = int(lista_patentes[i][2:5])
        numero_nuevo = int(patente_nueva[2:5])

        if numero_actual > numero_nuevo:
            patente_nueva = lista_patentes[i]

    return patente_nueva


def informar_porcentaje_letras(lista_patentes: list) -> None:
    """
    Calcula e informa el porcentaje de patentes por letra inicial.

    Parámetros:
        lista_patentes (list): Lista de patentes almacenadas.

    Retorna:
        None: Muestra el porcentaje correspondiente a cada letra.
    """
    if len(lista_patentes) > 0:
        for codigo in range(65, 91):
            letra = chr(codigo)
            contador_letras = 0

            for j in range(len(lista_patentes)):
                if lista_patentes[j][0] == letra:
                    contador_letras = contador_letras + 1

            porcentaje = contador_letras * 100 / len(lista_patentes)

            print(letra, ":", round(porcentaje, 2), "%")
    else:
        print("No hay patentes almacenadas.")


# PUNTO 4: ORDENAR PATENTES

def ordenar_patentes(lista_patentes: list, criterio: str) -> list:
    """
    Ordena las patentes utilizando el método burbuja.

    Parámetros:
        lista_patentes (list): Lista de patentes que se desea ordenar.
        criterio (str): Criterio de ordenamiento, ASC o DESC.

    Retorna:
        list: Lista de patentes ordenadas según el criterio.
    """
    lista_ordenada = lista_patentes

    for i in range(len(lista_ordenada) - 1):
        for j in range(len(lista_ordenada) - 1 - i):

            if criterio == "ASC":
                if lista_ordenada[j] > lista_ordenada[j + 1]:
                    auxiliar = lista_ordenada[j]
                    lista_ordenada[j] = lista_ordenada[j + 1]
                    lista_ordenada[j + 1] = auxiliar

            else:
                if lista_ordenada[j] < lista_ordenada[j + 1]:
                    auxiliar = lista_ordenada[j]
                    lista_ordenada[j] = lista_ordenada[j + 1]
                    lista_ordenada[j + 1] = auxiliar

    return lista_ordenada
