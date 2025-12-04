# Abrir el archivo en modo lectura
file = open("texto.txt", "r")

# linea por linea
linea = file.readline()

while linea:
    print("linea: ", linea)

    linea = file.readline()

# cierro el archivo
file.close()