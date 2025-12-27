import time


def tarea(numero):
    print(f"Iniciando tarea {numero}")
    time.sleep(numero)
    print("finalizando tarea")


inicio = time.time()

tarea(5)
tarea(5)
tarea(5)

fin = time.time()

print(fin-inicio)
