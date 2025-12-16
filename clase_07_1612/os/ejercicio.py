# Desarrollar un script buscar_archivos.py que reciba
# como argumentos la ruta a una carpeta y una extensión
# para buscar archivos dentro de ella. Luego debe
# mostrar los archivos que terminen con dicha extensión
# en la carpeta indicada. Por ejemplo, en el caso siguiente
# se listan los archivos con extensión “.exe” en la carpeta
# llamada “carpeta”:
#
# Si no se pasan los dos argumentos correspondientes,
# el programa debe indicar el error en la consola y
# finalizar


# python buscar_archivos.py /tmp exe


import os


# os.sys.argv

directorio = os.sys.argv[1] # directorio 
extension = os.sys.argv[2]  # extension


archivos = os.listdir(directorio)

for para recorrer la lista
    
