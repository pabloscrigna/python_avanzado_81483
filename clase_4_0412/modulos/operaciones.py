def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def multiplicacion(a, b):
    return a * b


def division(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a / b


def potencia(a, b):
    return a**b


if __name__ == "__main__":
    print("__name__ operaciones: ", __name__)
    print("resta: ", resta(8,5))