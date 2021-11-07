# criação de uma classe triângulo
class Triangulo:
  def __init__(self, lado1, lado2, lado3):
    self.lado1 = lado1
    self.lado2 = lado2
    self.lado3 = lado3

# função para validar o triângulo e informar sua classificação
def fazer_triangulo():
  while True:
    lado1 = int(input("Digite o primeiro lado do triângulo: "))
    lado2 = int(input("Digite o segundo lado do triângulo: "))
    lado3 = int(input("Digite o terceiro lado do triângulo: "))
    lados = Triangulo(lado1, lado2, lado3)
    if lados.lado1 < lados.lado2 + lados.lado3 and lados.lado2 < lados.lado1 + lados.lado3 and lados.lado3 < lados.lado1 + lados.lado2:
      print("As informações são válidas para formar um triângulo!")
      if lados.lado1 == lados.lado2 == lados.lado3:
        print("Esse triângulo formado é equilátero!")
      elif (lados.lado1 != lados.lado2 == lados.lado3) or (lados.lado2 != lados.lado1 == lados.lado3) or (lados.lado3 != lados.lado1 == lados.lado2):
        print("Ess triângulo formado é isósceles!")
      else:
        print("Esse triângulo formado é escaleno!")
    else:
      print("As informações não são válidas para formar um triângulo")
      break

# chamada da função
fazer_triangulo()