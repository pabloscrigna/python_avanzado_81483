# Abrir el archivo en modo lectura
file = open("texto.txt", "r")

# Vamos a leer las lineas del archivo
lineas = file.readlines()

# muestro contenido del archivo
print("file readlines:", lineas)

# linea por linea
for linea in lineas:
    print("linea", linea)

# cierro el archivo
file.close()