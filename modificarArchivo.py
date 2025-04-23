import json
from datetime import datetime

# Leer archivo
archivo = open("quiz.json", "r", encoding="utf-8")
contenido = json.load(archivo)
archivo.close()

# Acceder correctamente al lugar donde está "Programacion 1"
sede3_info = contenido["Unisangil"]["Sedes"][2]
semestre_ii = sede3_info["Facultades"][1]["Falcultad de Ciencias Naturales e Ingenierias"][0]["Ingenieria de Sistemas"][1]["SemestreII"]

# Pedir nuevo nombre
username = input("Ingrese el nuevo nombre de materia: ")

# Buscar y reemplazar
for i, item in enumerate(semestre_ii):
    if isinstance(item, dict) and "Programacion 1" in item:
        datos_materia = item["Programacion 1"]
        semestre_ii[i] = {username: datos_materia}
        break

# Agregar fecha de modificación
contenido["Fecha de Modificacion"] = str(datetime.now())

# Guardar archivo nuevo
archivo = open("quiz1.json", "w", encoding="utf-8")
json.dump(contenido, archivo, indent=4, ensure_ascii=False)
archivo.close()
