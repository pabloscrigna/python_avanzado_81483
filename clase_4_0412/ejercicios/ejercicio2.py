# hacer una funcion que tome como argumento un str y retorne el caracter que mas veces aparec
# y la cantidad de veces
# "hola!!!"   --> !, 3
# 


def max_caracter(frase: str)-> tuple:

    letras = {}

    for caracter in frase:   # qqwertyyyy
        if caracter in letras:
            letras[caracter] += 1
        else:
            letras[caracter] = 1

    maximo_valor = 0
    maximo_key = ""

    for key, value in letras.items():
        if value > maximo_valor:
            maximo_valor = value
            maximo_key = key

    return maximo_key, maximo_valor


print(max_caracter("qwertyyyyyy"))
