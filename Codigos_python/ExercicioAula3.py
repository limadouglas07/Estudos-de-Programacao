#Faça um programa em Python que calcule e mostre o valor do volume do tronco de uma pirâmide,
# para isso o programa deve solicitar ao usuário os valores da altura do tronco da pirâmide (h)
# , o valor da base menor (Bmenor) e o da base maior (Bmaior) ecalcular a seguinte
# expressão:volume =h/3*(Bmaior**2 + Bmenor**2 + (Bmaior**2 * Bmenor**2)**0.5)
import math

h = float(input("Digite a altura do tronco:"))
Bmenor = float(input("Digite o valor da base menor:"))
Bmaior = float(input("Digite o valor da base maior:"))

volume = h/3*(Bmaior**2 + Bmenor**2 + (Bmaior**2 * Bmenor**2)**0.5)
print("O volume do tronco de uma pirâmide é {:.0f}cm3".format(volume))

# Crie um programa em Python que solicite o valor em horas para o usuário ,
# calcule e mostre o valor em minutos, sabendo que 1 hora tem 60 minutos.

horas = float(input("Digite a hora:"))
minutos = horas * 60
print("{:.0f} horas tem {:.0f} minutos".format(horas, minutos))

#3- Crie um programa em Python que solicite ao usuário a sua idade expressa em anos ,meses e dias (variáveis separadas).
# Calcule e mostre a idade expressa apenas em dias. Para isso considere 1 ano = 365 dias, 1 mês = 30 dias.#

ano = int(input("Digite aqui o ano:"))
mes = int(input("Digite aqui o mês:"))
dia = int(input("Digite aqui o dia:"))
anoatual = 2024

calculo = (anoatual-ano) * 365
print("Você nasceu no ano de {} no mês {} e dia {} e tem {} dias de vida".format(ano, mes, dia, calculo))


#4-Escreva um programa em Python para calcular o valor de uma prestação em atraso(prestacao).
#Para isso, obtenha o valor da prestação (valorPrestacao), a porcentagem demulta pelo atraso (multa) e a quantidade de dias de atraso (qtdeDias).
#Calcular e mostrar ovalor da prestação atualizado,
#sabendo que:prestacao=valorPrestacao+(valorPrestacao*(multa/100)*qtdeDia.


valorPrestacao = float(input("Digite o valor da prestação:"))
qtdeDias = int(input("Digite aqui os dias em atraso:"))
multa = 2
prestacao = valorPrestacao+(valorPrestacao*(multa/100)*qtdeDias)
print("O valor da prestação atualizado é R${:.2f}".format(prestacao))

#5- Faça uma programa em Python que peça do usuário um valor em graus para um ângulo.
# Converta-o para radianos e, usando funções da biblioteca math, imprima o seno,cosseno e tangente deste ângulo.
import math

angulo = float(input("Digite aqui o ângulo:"))
radianos = math.radians(angulo)
seno = math.sin(angulo)
cosseno = math.cos(angulo)
tangente = math.tan(angulo)

print("O seno é{} o cosseno é{} e tangente é{}".format(seno, cosseno, tangente))





