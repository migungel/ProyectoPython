ruta = "C:\\Users\\JOCAMI\\PycharmProjects\\untitled\\proyecto 2\\"

#               opcion 3
def eliminar_registro(clave):                           #elimina los registros de mis_favoritos
    global ruta
    favoritos = open(ruta + "mis_favoritos.txt", "r")       #abre el archivo en modo lectura
    ids = ""
    for linea in favoritos:                                 #almacena cada linea en una variable
        id = linea.split("|")                               #y compara con la id agragada, guarda las lineas que no
        if clave != id[0]:                                  #tienen la id pedida a borrar
            ids += linea
    favoritos.close()

    favoritos = open(ruta + "mis_favoritos.txt", "w")       #recrea el archivo solo con los datos que no se
    favoritos.write(ids)                                    #se quisieron borrar
    favoritos.close()
    print("La cancion fue eliminada")












