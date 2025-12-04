# Abrir el archivo modo escritura

file = open("archivo_escritura.txt", "w")

file.write("Primera linea de mi archivo\n")
file.write("Segunda linea")

# cerramos el archivo
file.close()
