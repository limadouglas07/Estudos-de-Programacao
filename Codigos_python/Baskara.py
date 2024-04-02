#4- Escreva um programa em Python que calcule as duas raízes de uma equação de 2º grau ax²+bx+c,
#conhecendo os valores dos coeficientes da mesma (a, b, c). Suponha que as raízes são reais.
#Lembre-se que para calcular as duas raízes.

import math
from operator import neg

a = float(input("Digite aqui o coeficiente de a:"))
b = float(input("Digite aqui o coeficiente de b:"))
c = float(input("Digite aqui o coeficiente de c:"))


delta = (b**2) - 4 * a * -abs(c)  # Transforma um valor positivo em um número negativo #
print(f"O valor de delta é {delta}")

x1 = (-b + math.sqrt(delta)) / (2 * a)
x2 = (-b - math.sqrt(delta)) / (2 * a)

print(f"O valor das raizes de x1 é :{x1} e o valor de x2 é: {x2}")
