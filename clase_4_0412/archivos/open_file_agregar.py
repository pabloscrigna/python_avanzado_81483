# Abrir el archivo modo agregar (append)

file = open("archivo_escritura.txt", "a")

file.write("\nTercera linea\n")
file.write("Cuarta linea")

# cerramos el archivo
file.close()