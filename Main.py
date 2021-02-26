from pathlib import Path #importamos la función pATH para obtener la ruta de la direccion en donde se encuentra cada archivo
from time import time #importamos la función time para capturar tiempos

tiempo_ejecucioni = time()

direccion = "C:/Users\pc\Desktop\Actividad 1\Files"
archivo = Path(direccion)
totaltempfiles = 0

txt = open ('a1_teamA.txt','a+')
txt.truncate(0)
txt.write ("--------------RUTA ARCHIVO---------------------" + "        "  + "------TIEMPO-----"  + "\n")

for fichero in archivo.iterdir():
    tiempo_inicial = time()
    p = open (fichero, errors= "ignore").read() #Abre el archivo y lo lee
    #p = open (fichero) #Solamente abre el archivo
    tiempo_final = time()
    tiempo_ejecucion = round(tiempo_final - tiempo_inicial, 6)
    txt.write (str(fichero) + "         " + str(tiempo_ejecucion) + "\n")
    totaltempfiles += tiempo_ejecucion

tiempo_ejecucionf = time()
tiempo_total = round(tiempo_ejecucionf - tiempo_ejecucioni, 6)
txt.write ("\n" + "Tiempo Total en abrir los archivos: " + str(round(totaltempfiles,4)) + "\n")
txt.write ("Tiempo Total de ejecucion: " + str(tiempo_total) + "\n")
txt.close()
