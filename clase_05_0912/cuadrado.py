class Rectangulo:

  def __init__(self, lado_a, lado_b):
    self.lado_a = lado_a
    self.lado_b = lado_b

  def area(self):
    return self.lado_a * self.lado_b

  def perimetro(self):
    return 2 * (self.lado_a + self.lado_b)


class Cuadrado(Rectangulo):
  
    def __init__(self, lado):
      super().__init__(lado, lado)

    

# Clase Rectangulo
figura1 = Rectangulo(6, 5)

print(f"lado A: {figura1.lado_a}  -- perimetro: {figura1.perimetro()}")

# clase Cuadrado
figura2 = Cuadrado(5, 5)

print(f"lados: {figura2.lado_a} -- {figura2.lado_b}")
print(f"perimetro del cuadrado: {figura2.perimetro()}")