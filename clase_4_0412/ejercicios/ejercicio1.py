# Hacer una funcion que tome como argumento una lista de numeros y retorne el menor valor de la lista.


def menor(numeros: list)-> int:
    
    if not numeros:
        return None

    menor = numeros[0]
    for numero in numeros:
        if numero < menor:
            menor = numero

    return menor    


lista = [5, 7, 8, 9, 4]

resultado = menor(lista)

print("menor: ", resultado)