# PARTE 1: CARGAR DATOS
def cargar_datos(lineas_archivo):
    generos_peliculas = []
    peliculas_por_genero = {}
    info_peliculas = []

    for linea in lineas_archivo:
        # Se divide la linea por comas con split
        partes = linea.split(",")

        if len(partes) != 5:
            print(f"Línea ignorada (formato incorrecto): {linea}")
            continue  # Ignoramos la linea si tiene el formato incorrecto

        titulo = partes[0].strip()
        popularidad = float(partes[1].strip())
        voto_promedio = float(partes[2].strip())
        cantidad_votos = int(partes[3].strip())
        generos = partes[4].strip().split(";")

        # Aca agregamos generos unicos a generos_peliculas
        for genero in generos:
            if (
                genero and genero not in generos_peliculas
            ):  # Aca se comprueba: 1° genero no esta vacio. 2° si genero "NO" esta en generos_peliculas
                generos_peliculas.append(genero)  # Agrega genero al final de la lista.

            # Aseguramos que se relacione cada genero con las peliculas que lo tienen
            if genero not in peliculas_por_genero:
                peliculas_por_genero[genero] = (
                    []
                )  # Si el genero no esta en el diccionario {}, se inicializa una lista vacia para ese genero
            peliculas_por_genero[genero].append(
                titulo
            )  # Agrega el titulo actual a la lista correspondiente de genero

        # Agregamos la información de la pelicula a info_peliculas
        info_peliculas.append(
            (titulo, popularidad, voto_promedio, cantidad_votos, generos)
        )

    # el for de linas termina aqui
    # Convertimos peliculas_por_genero a una lista de tuplas
    peliculas_por_genero = [
        (genero, peliculas_por_genero[genero]) for genero in generos_peliculas
    ]

    return generos_peliculas, peliculas_por_genero, info_peliculas


# PARTE 2: COMPLETAR CONSULTAS
def obtener_puntaje_y_votos(nombre_pelicula):
    # Cargamos las lineas con la data del archivo
    lineas_archivo = leer_archivo()

    # Recorremos cada linea del archivo
    for linea in lineas_archivo:
        partes = linea.strip().split(",")

        # Verificar si la linea tiene mas de un elemento y coincide con el nombre de la pelicula
        if len(partes) > 1 and partes[0].strip() == nombre_pelicula:
            puntaje_promedio = float(partes[2])  # Extrae datos
            cantidad_votos = int(partes[3])  # Extrae datos
            return puntaje_promedio, cantidad_votos

    # Si no se encontro la pelicula después de recorrer todo el archivo
    print(f"El nombre de la película ({nombre_pelicula}) no se encuentra en el archivo")
    return "no hay", "no hay"


def filtrar_y_ordenar(genero_pelicula):
    # Usamos las estructuras cargadas
    lineas_archivo = leer_archivo()
    _, peliculas_por_genero, _ = cargar_datos(
        lineas_archivo
    )  # Entiendo que se puede utilizar guion_bajo para reemplazar variables que no usare

    # Buscar las peliculas por el genero proporcionado
    for genero, peliculas in peliculas_por_genero:
        if genero == genero_pelicula:
            # Ordenar las peliculas alfabéticamente en orden inverso
            return sorted(peliculas, reverse=True)

    # Si el genero no existe, devolver una lista vacia
    return ["No hay peliculas"]


def obtener_estadisticas(genero_pelicula, criterio):
    # Cargar las lineas con la data del archivo
    lineas_archivo = leer_archivo()
    _, _, info_peliculas = cargar_datos(lineas_archivo)

    # Filtrar peliculas por el género dado
    peliculas_filtradas_por_genero = [
        pelicula for pelicula in info_peliculas if genero_pelicula in pelicula[4]
    ]

    if not peliculas_filtradas_por_genero:
        print(f"No se encontraron películas del género {genero_pelicula}")
        return [None, None, None]

    # Seleccionar el indice correcto segun el criterio
    if criterio == "popularidad":
        indice = 1
    elif criterio == "voto promedio":
        indice = 2
    elif criterio == "cantidad votos":
        indice = 3
    else:
        print("Criterio no válido")
        return [None, None, None]

    # Se extraen los valores correspondientes al criterio
    valores = [pelicula[indice] for pelicula in peliculas_filtradas_por_genero]
    # Calcular maximo, minimo y promedio
    maximo = max(valores)
    minimo = min(valores)
    promedio = sum(valores) / len(valores)

    return [maximo, minimo, promedio]


# NO ES NECESARIO MODIFICAR DESDE AQUI HACIA ABAJO


def solicitar_accion():
    print("\n¿Qué desea hacer?\n")
    print("[0] Revisar estructuras de datos")
    print("[1] Obtener puntaje y votos de una película")
    print("[2] Filtrar y ordenar películas")
    print("[3] Obtener estadísticas de películas")
    print("[4] Salir")

    eleccion = input("\nIndique su elección (0, 1, 2, 3, 4): ")
    while eleccion not in "01234":
        eleccion = input("\nElección no válida.\nIndique su elección (0, 1, 2, 3, 4): ")
    eleccion = int(eleccion)
    return eleccion


def leer_archivo():
    lineas_peliculas = []
    with open("./peliculas.csv", "r", encoding="utf-8") as datos:
        for linea in datos.readlines()[1:]:
            lineas_peliculas.append(linea.strip())
    return lineas_peliculas


def revisar_estructuras(generos_peliculas, peliculas_por_genero, info_peliculas):
    print("\nGéneros de películas:")
    for genero in generos_peliculas:
        print(f"    - {genero}")

    print("\nTítulos de películas por genero:")
    for genero in peliculas_por_genero:
        print(f"    genero: {genero[0]}")
        for titulo in genero[1]:
            print(f"        - {titulo}")

    print("\nInformación de cada película:")
    for pelicula in info_peliculas:
        print(f"    Nombre: {pelicula[0]}")
        print(f"        - Popularidad: {pelicula[1]}")
        print(f"        - Puntaje Promedio: {pelicula[2]}")
        print(f"        - Votos: {pelicula[3]}")
        print(f"        - Géneros: {pelicula[4]}")


def solicitar_nombre():
    nombre = input("\nIngrese el nombre de la película: ")
    return nombre


def solicitar_genero():
    genero = input("\nIndique el género de película: ")
    return genero


def solicitar_genero_y_criterio():
    genero = input("\nIndique el género de película: ")
    criterio = input(
        "\nIndique el criterio (popularidad, voto promedio, cantidad votos): "
    )
    return genero, criterio


def main():
    lineas_archivo = leer_archivo()
    datos_cargados = True
    try:
        generos_peliculas, peliculas_por_genero, info_peliculas = cargar_datos(
            lineas_archivo
        )
    except TypeError as error:
        if "cannot unpack non-iterable NoneType object" in repr(error):
            print(
                "\nTodavía no puedes ejecutar el programa ya que no has cargado los datos\n"
            )
            datos_cargados = False
    if datos_cargados:
        salir = False
        print("\n********** ¡Bienvenid@! **********")
        while not salir:
            accion = solicitar_accion()

            if accion == 0:
                revisar_estructuras(
                    generos_peliculas, peliculas_por_genero, info_peliculas
                )

            elif accion == 1:
                nombre_pelicula = solicitar_nombre()
                ptje, votos = obtener_puntaje_y_votos(nombre_pelicula)
                print(f"\nObteniendo puntaje promedio y votos de {nombre_pelicula}")
                print(f"    - Puntaje promedio: {ptje}")
                print(f"    - Votos: {votos}")

            elif accion == 2:
                genero = solicitar_genero()
                nombres_peliculas = filtrar_y_ordenar(genero)
                print(f"\nNombres de películas del género {genero} ordenados:")
                for nombre in nombres_peliculas:
                    print(f"    - {nombre}")

            elif accion == 3:
                genero, criterio = solicitar_genero_y_criterio()
                estadisticas = obtener_estadisticas(genero, criterio)
                print(f"\nEstadísticas de {criterio} de películas del género {genero}:")
                print(f"    - Máximo: {estadisticas[0]}")
                print(f"    - Mínimo: {estadisticas[1]}")
                print(f"    - Promedio: {estadisticas[2]}")

            else:
                salir = True
        print("\n********** ¡Adiós! **********\n")


if __name__ == "__main__":
    main()
