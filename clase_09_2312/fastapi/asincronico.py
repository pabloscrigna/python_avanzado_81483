import asyncio
import time

async def tarea(numero):
    print(f"Iniciando tarea {numero}")
    await asyncio.sleep(5)
    print(f"Finalizando tarea {numero}")

async def main():
    inicio = time.time()

    await asyncio.gather(
        tarea(5),
        tarea(5),
        tarea(5)
    )

    fin = time.time()
    print(f"Tiempo total: {fin - inicio} segundos")

asyncio.run(main())