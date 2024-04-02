#1- Desenvolva um programa em Python que solicite ao usuário os valores dos lados
#de um retângulo e calcule e mostre seu perímetro e sua área.#

b= float(input("Digite aqui a base:"))
h= float(input("Digite aqui a haltura:"))

perimetro = 2*(b+h)
area = b * h

print("O Perímetro de um retângulo é :", perimetro)
print("A área do quadrado é :", area)


# 2- Escreva um programa em Python que solicite ao usuário o salário atual e mostre o
# salário acrescido de 5% de comissão.

salario = float(input("Digite aqui o seu salário:"))
acrescimo = ((salario*5)/100)+salario

print("O Valor do Salário acrescido de 5% é de:", acrescimo)


#3- Escreva um programa em Python que solicite ao usuário a distância entre duas cidades
#e o tempo de viagem. Oprograma deverá calcular e exibir a velocidade média de um carro
#que vai de uma cidade para outra. Utilize a fórmula.

distanciacidades = float(input("Digite aqui a distancia das cidades para sua viagem:"))
tempodeviagem = float(input("Digite aqui o tempo de viagem:"))

velocidademedia= distanciacidades/tempodeviagem

print("A velocidade média do carro é de:{:.0f}".format(velocidademedia),"Km/h")


#4- Escreva um programa em Python que calcule as duas raízes de uma equação de 2º grau ax²+bx+c,
#conhecendo os valores dos coeficientes da mesma (a, b, c). Suponha que as raízes são reais.
#Lembre-se que para calcular as duas raízes.

import math

a = float(input("Digite aqui o coeficiente de a:"))
b = float(input("Digite aqui o coeficiente de b:"))
c = float(input("Digite aqui o coeficiente de c:"))

delta = (b**2) - 4 * a * c
print(f"O valor de delta é {delta}")

x1 = (-b + math.sqrt(delta)) / (2 * a)
x2 = (-b - math.sqrt(delta)) / (2 * a)

print(f"O valor das raizes de x1 é :{x1} e o valor de x2 é: {x2}")



# 5- Escreva um programa em Python que leia a cotação do dólar (taxa de conversão),
# leia um valor em dólares e converta e mostre o valor equivalente em Reais.

dolardodia = float(input("Digite a cotação do dia:"))
quantia = float(input("Digite aqui a quantidade em dólares:"))

conversao = dolardodia * quantia
print("O valor do seu dinheiro em reais é R${:.2f}".format(conversao))

#6- Escreva um programa em Python que leia um valor representando o gasto realizado por um cliente do
# restauranteComaBem e visualize o valor total a ser pago, considerando os 10% do garçom.
valor = float(input("Digite aqui o valor do seu gasto:"))
totalvalor = ((valor*10)/100) + valor
print("O valor a ser pago com a taxa de 10% é:R${:.2f}".format(totalvalor))


#7- Escreva um programa em Python que obtenha umatemperatura em graus Celsius
#, calcule e mostre a respectivatemperatura
# nas escalas Fahrenheit e Kelvin. Utilize asfórmulas abaixo:

celcius = float((input("Digite aqui a temperatura em °C:")))

tf = 1.8 * celcius + 32
tk = celcius + 273
print("A temperatura em Fahrenheit é {}°F".format(tf))
print("A temperatura em Kelvin é {}°K".format(tk))

















