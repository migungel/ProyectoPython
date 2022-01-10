#importar todas las funciones de cada opcion
from opcion1 import search, preparar_datos, presentar_resultados, tiempo
from opcion1_1 import crear_archivo_txt, guardar_archivos_txt
from opcion2 import mis_favoritos
from opcion3 import eliminar_registro
from opcion4 import mostrar_top


def menu():                 #menu del programa
    opcion = int(input ("""
Opción 1: Buscar música
Opción 2: Ver mi archivo de favoritos
Opción 3: Eliminar música de mi archivo de favoritos
Opción 4: Top 10 de mi archivo de favoritos
Opción 5: Salir del sistema

Opcion: """))
    return opcion


menu_p = 0
ruta = "C:\\Users\\JOCAMI\\PycharmProjects\\untitled\\proyecto 2\\"
opciones = [1,2,3,4,5]
while menu_p == 0:                          #inicio del programa con la funcion menu
    opcion = menu()
    if opcion == 1:                             #inicio de la opcion 1
        opciones1 = [1,2]
        criterio = input("Busqueda: ")          #creacion del diccionario
        busqueda = search(criterio)
        tiempo(busqueda)                        #y preparacion
        datos_id = preparar_datos(busqueda)
        presentar_resultados(datos_id)
        op1 = 0

        while op1 == 0:                     #inicio de la opcion 1.1
            opcion1 = int(input("""
    Opción 1: Agregar un resultado a archivo mis favoritos
    Opción 2: Regresar al menú principal
    Opcion: """))

            if opcion1 == 1:
                favoritos = open(ruta  + "mis_favoritos.txt", "a")      #crear un archivo vacio y verificar el archivo favoritos
                favoritos = open(ruta + "mis_favoritos.txt", "r")       #leer archivo
                mis_fav = favoritos.read()
                if mis_fav == "":                                       #condicionantes para crear el archivo con identificadores
                    crear_archivo_txt()                                 #y agregar datos nuevos
                    guardar_archivos_txt(datos_id)
                else:
                    guardar_archivos_txt(datos_id)                      #en caso de que el archivo exista agregar archivos nuevos
                favoritos.close()

            if opcion1 == 2:                                #salir al menu principal
                op1 = 1

            if opcion1 not in opciones1:                    # validacion de una opcion fuera de las opciones del menu
                print("Opcion no valida")


    if opcion == 2:                                         #inicio de la opcion 2
        opciones2 = [1]
        favoritos = open(ruta + "mis_favoritos.txt", "r")
        fav = mis_favoritos(favoritos)                      #leer el archivo favoritos para presentarlos
        favoritos.close()                                   #de manera ordenada y arreglada
        op2 = 0

        while op2 == 0:                                     #submenu 2
            opcion2= int(input("""
    Opcion 1: Regresar al menu principlal
    Opcion: """))
            if opcion2 == 1:                                #regresar al menu principal
                op2 = 1

            if opcion2 not in opciones2:  # validacion de una opcion fuera de las opciones del menu
                print("Opcion no valida")

    if opcion == 3:                                      #inicio de la opcion 3
        opciones3 =[1,2,3]
        op3 = 0
        while op3 == 0:                             #inicio de la opcion 3.1 para eliminar
            opcion3 = int(input("""
    Opción 1: Eliminar un registro
    Opción 2: Regresar al menú principal
    Opcion: """))

            if opcion3 == 1:                                #ingreso de clave a er eliminada
                clave = input("Ingrese id a eliminar: ")
                eliminar_registro(clave)

            if opcion3 == 2:                            #regresar al menu
                op3 = 1

            if opcion3 not in opciones3:  # validacion de una opcion fuera de las opciones del menu
                print("Opcion no valida")


    if opcion == 4:                                    #inicio de la opcion 4
        mostrar_top()                                   #presentar grafico


    if opcion == 5:                                     #opcion 5, salir del programa
        menu_p = 5

    if opcion not in opciones:                          #validacion de una opcion fuera de las opciones del menu
        print("Opcion no valida")

