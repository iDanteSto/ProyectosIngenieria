
from pathlib import Path #importamos la función pATH para obtener la ruta de la direccion en donde se encuentra cada archivo
from time import time #importamos la función time para capturar tiempos
import re


def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext


tiempo_ejecucioni = time()

direccion = Path().absolute()
archivos = Path(direccion)
totaltempfiles = 0
txt = open ('a2_teamA.txt','a+')
txt.truncate(0)
txt.write ("--------------RUTA ARCHIVO---------------------" + "        "  + "------TIEMPO-----"  + "\n")


for fichero in archivos.iterdir():
    print(fichero)
    tiempo_inicial = time()
    raw_html = open(fichero, errors= "ignore").read() #Abre el archivo y lo lee
    clean_text = cleanhtml(raw_html)
    group_file = open('grouped_text.txt','a+')
    group_file.write(clean_text)
    tiempo_final = time()
    tiempo_ejecucion = round(tiempo_final - tiempo_inicial, 6)
    txt.write (str(fichero) + "         " + str(tiempo_ejecucion) + "\n")
    totaltempfiles += tiempo_ejecucion

tiempo_ejecucionf = time()
tiempo_total = round(tiempo_ejecucionf - tiempo_ejecucioni, 6)
txt.write ("\n" + "Tiempo Total en quitar las etiquetas HTML: " + str(round(totaltempfiles,4)) + "\n")
txt.write ("Tiempo Total de ejecucion: " + str(tiempo_total) + "\n")
txt.close()
