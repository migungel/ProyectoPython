#                   opcion 1
import spotipy

def search (criterio, limite = 10):             #implementacion de la funcion search
    resultados = []                             #que retornara el diccionario de resultados de la busqueda
    diccionario = {}                            #con un limite de 10
    canciones = []
    sp = spotipy.Spotify()
    results = sp.search(q=criterio, limit=limite)
    for musica in results['tracks']['items']:
        artistas = ""
        cancion = ""
        cancion += "%s" % musica["name"]
        if musica["name"] not in canciones:         #crea una lista de listas de los resultados
            canciones.append(musica["name"])
        for artist in musica['artists']:
            artistas += "%s" % artist['name']
        resultados.append([musica['name'],musica['popularity'],musica['preview_url'],musica['duration_ms'],artistas,musica['id']])

    for i in range(len(canciones)):
        artistas2 = []  #lista de artistas a ser presentados en el diccionario
        for j in range(len(resultados)):
            if canciones[i] == resultados[j][0]:
                if resultados[j][4] not in artistas2:
                    artistas2.append(resultados[j][4])
                diccionario[canciones[i]] = {"popularidad": resultados[i][1],       #crea un diccionario a partir de los resultados
                                             "url": resultados[i][2],               #de las lista anterior
                                             "duracion": resultados[i][3],
                                             "artistas": artistas2,
                                             "id": resultados[i][5]
                                             }
    return diccionario

def preparar_datos (dic_l):                             #prepara los datos en un nuevo diccionario con clave
    resultados = {}                                     #de las id de las canciones
    for musica in dic_l:
        cancion = dic_l[musica]
        resultados[cancion["id"]] = {"cancion": musica,
                     "popularidad" : cancion["popularidad"],
                     "duracion" : cancion["duracion"],
                     "artistas" : cancion["artistas"]}
    return resultados

def presentar_resultados (datos_id):                    #presenta los datos de manera adecuada
    for datos in datos_id:                              #presentacion visual de todos los resultados
        print("#####################################################################")
        print("id:", datos)
        print("cancion:", datos_id[datos]["cancion"])
        print("artistas:",", ".join(datos_id[datos]["artistas"]))
        print("popularidad:", datos_id[datos]["popularidad"])
        print("duracion:", datos_id[datos]["duracion"])
    print("#####################################################################")


def tiempo(busqueda):                                   #funcion extra implementada para transformar los
    for musica in busqueda:                             #milisegundos a un formato de horas, minutos y segundos
        milisegundos = busqueda[musica]["duracion"]
        horas = int((int(milisegundos)/1000) / 3600)#tansforma a horas
        minutos = int(int((int(milisegundos)/1000) - (horas * 3600)) / 60)#tansforma a minutos
        seg = int(int(milisegundos)/1000 - ((horas * 3600) + (minutos * 60)))#tansforma a segundos
        if horas <= 0:#condicionante en caso de que la musica dure menos de 1 hora
            busqueda[musica]["duracion"] = "%02d:%02d" %(minutos, seg)
        elif horas >= 1:#condicionante en caso de que la musica dure mas de 1 hora
            busqueda[musica]["duracion"] = "%02d:%02d:%02d" %(horas, minutos, seg)



