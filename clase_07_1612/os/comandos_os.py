import os


# listdir

archivos = os.listdir("/tmp")

print("archivos: ", archivos)


# getcwd

dir_actual = os.getcwd()

print("directorio actual: ", dir_actual)

# mkdir

carpeta = "nueva_carpeta"

# os.mkdir(carpeta)

# path.exists

if os.path.exists("nueva_carpeta"):
    print("Existe el path: nueva_carpeta")
else:
    print("no existe")