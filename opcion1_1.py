import pandas as pd
ruta = "C:\\Users\\JOCAMI\\PycharmProjects\\untitled\\proyecto 2\\"

#                   opcion 1.1            funciones adicionales
def crear_archivo_txt():                                        #sobrescribe el archivo vacio creado por primera vez
    favoritos = open(ruta + "mis_favoritos.txt","w")            #creando uno nuevo con identificadores de
    favoritos.write("id|cancion|artistas|popularidad|duracion" + "\n")     #id|cancion|artistas|popularidad|duracion
    favoritos.close()

def guardar_archivos_txt(datos_id):                             #compara y guarda canciones
    ids = []
    canciones_id = pd.read_csv("mis_favoritos.txt", sep="|") #enconding = "utf8")      guarda las id de todas las canciones
    for id in canciones_id["id"]:                                                      #en la lista de favoritos
        ids.append(id)

    clave = input("Ingrese clave: ")                #ingresa la id de la musica a guardar
    if clave == "":                                  #comprobacion de dato
        print("Dato vacio")
    elif clave not in ids:                                                      #abre el archivo en modo de a para agregar
        favoritos = open(ruta + "mis_favoritos.txt", "a")                       #datos nuevos
        archivo = datos_id[clave]
        favoritos.write(clave + "|")                                # id
        favoritos.write(archivo["cancion"] + "|")                   # nombre cancion
        favoritos.write(",".join(archivo["artistas"]) + "|")        # artistas
        favoritos.write(str(archivo["popularidad"]) + "|")          # popularidad
        favoritos.write(archivo["duracion"])                        # duracion
        favoritos.write("\n")
        favoritos.close()
        print("Registro agregado a favoritos")
    else:
        print("El registro ya exite en la lista de favoritos")                  #comprobacion de datos

