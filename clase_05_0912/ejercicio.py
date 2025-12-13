# dada una frase y un diccionario con con los pesos de las palabras
# calcular el porcentaje de positividad del texto
# Buscar las palabras que estan en la frase y calcular el promedio segun el peso del diccionario
# si la palabra no esta en el diccionario el peso es cero



# frase = "estoy en un mundo feliz"
# 
# peso_total = 5 + 0 + 0 + 0 + 10 = 15
# promedio = 15/5
# 
# diccionario_pesos = {
#     "estoy": 5,
#     "feliz": 10
# }
# 
# lista_palabras = split de frase
# 
# cantidad_palabras = len(lista_palabras)
# 
# for palabra in lista_palabras:
# 
#     diccionario_pesos[palabra] ??? 
# 
#     diccionario_pesos.get(palabra)  -----> None
#     diccionario_pesos.get(palabra, 0)
# 
#     hay que llevar un acumulado
# 
# 
# promedio = acumulado / cantidad_palabras
# 
# 

diccionario_pesos = {
    "estoy": 5,
    "feliz": 10
}


def positividad(frase: int) -> float:

    acumulador = 0
    lista_palabras = frase.split()

    for palabra in lista_palabras:
        valor = diccionario_pesos.get(palabra, 0)    # acumulador += diccionario_pesos.get(..)
        acumulador += valor      # acumulador = acumulador + valor

    cantidad_palabras = len(lista_palabras)
    promedio = acumulador / cantidad_palabras
    
    return promedio 


frase = "estoy en un mundo feliz"


promedio = positividad(frase)

print("promedio", promedio)
