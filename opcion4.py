#                   opcion 4
import pandas as pd
import matplotlib.pyplot as plt
ruta = "C:\\Users\\JOCAMI\\PycharmProjects\\untitled\\proyecto 2\\"

def mostrar_top(valor = 10):                                    #mostrar el grafico de top 10 de canciones por popularidad
    global ruta
    df = pd.read_csv(ruta + "mis_favoritos.txt", sep="|", index_col="cancion")      #implentacion de un dataframe para llamar
    tabla = df[["popularidad"]]                                                     #a las variables por cancion
    popularidad = tabla.sort_values(by="popularidad", ascending=False)                  #los ordena por popularidad de mayor
    popularidad.head(valor).plot(kind='bar', legend=None, title="Top 10 canciones")     #a menor
    plt.gcf().subplots_adjust(bottom=0.5)   #ajusta el fondo del grafico
    plt.legend()
    plt.show()                                                                          #presenta el grafico
