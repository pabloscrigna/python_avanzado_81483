# copiar.py archivo_origen archivo_destino
# copiar.py pepe.txt raul.txt
import sys

argumentos = sys.argv  # lista con los argumentos 

if len(argumentos) < 3:
    print("Usage: copiar origen destino")
    exit(1)

print("Nombre del programa:", argumentos[0])

origen = argumentos[1]
destino = argumentos[2]

with open(origen, "r") as file:
    datos_a_copiar = file.read()

with open(destino, "w") as file:
    file.write(datos_a_copiar)


print("Archivo copiado")

