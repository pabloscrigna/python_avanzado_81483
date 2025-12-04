# Abrir el archivo en modo lectura

try:
    file = open("texto_1.txt", "r")
except FileNotFoundError:
    print("el archivo no existe")
    exit(1)

# leo todo el archivo
texto = file.read()

# muestro contenido del archivo
print("contenido del archivo: ", texto)

# cierro el archivo
file.close()