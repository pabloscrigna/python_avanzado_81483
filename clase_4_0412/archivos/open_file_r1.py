# Abrir el archivo en modo lectura

file = open("texto.txt", "r")

# leo todo el archivo
texto = file.read()

# muestro contenido del archivo
print("contenido del archivo: ", texto)

# cierro el archivo
file.close()