#Libreria para leer archivos
import json
#leer archivo
archivo = open("quiz.json", "r")
#guardar jason
contenido = json.load(archivo)
archivo.close()