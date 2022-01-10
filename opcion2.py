
#               opcion 2
def mis_favoritos(archivo):                         #lee el archivo mis_favoritos y los presenta de manera adecuada
    informacion = {}                                #como la opcion 1.1 de presenta datos
    for linea in archivo:
        datos = linea.split("|")
        if datos[0] != "id":                        #evita que salga la linea id|cancion|artistas|popularidad|duracion
            informacion[datos[0]] = {               #crea un diccionario nuevo para ser presentado
            "cancion":datos[1],
            "artistas": datos[2],
            "popularidad": datos[3],
            "duracion": datos[4]
            }

    for datos in informacion:                       #presenta los datos correctos con arreglos
        print("#####################################################################")
        print("id:", datos)
        print("cancion:", informacion[datos]["cancion"])
        print("artistas:",informacion[datos]["artistas"])
        print("popularidad:", informacion[datos]["popularidad"])
        print("duracion:", informacion[datos]["duracion"])
    print("#####################################################################")
