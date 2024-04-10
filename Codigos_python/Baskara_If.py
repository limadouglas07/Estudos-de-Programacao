idade = int(input("Digite aqui a sua idade:"))

if idade < 16 :
    print("não-eleitor ")
elif idade >= 18 and idade <= 65:
    print("eleitor obrigatório ")
elif idade >= 16 and idade < 18:
    print ("eleitor facultativo")
else:
    print("eleitor facultativo")



#Leia três valores inteiros (variáveis a, b e c) e efetue o cálculo da equação de segundo grau,
# apresentando: as duas raízes, quando for possível efetue o cálculo (delta positivo ou zero);
# a mensagem "Não há raízes reais", se não for possível fazer o cálculo (delta negativo);
# e a mensagem "Não é equação do segundo grau", se o valor de a for igual azero.

a = float(input("Digite aqui o coeficiente de a:"))
b = float(input("Digite aqui o coeficiente de b:"))
c = float(input("Digite aqui o coeficiente de c:"))

while a == 0:
    print("Não é equação de Segundo grau!!!")
    a = float(input("Digite aqui o coeficiente de a:"))
    b = float(input("Digite aqui o coeficiente de b:"))
    c = float(input("Digite aqui o coeficiente de c:"))
delta = (b ** 2) - (4 * a * c)
x1 = (((-1) * b) + (delta ** 0.5)) / (2 * a)
x2 = (((-1) * b) - (delta ** 0.5)) / (2 * a)

if delta >= 0:
    print("Não há raizes reais")
else:
    print("Delta Negativo")
print("O valor de delta é {}".format(delta))
print("O valor de X1 é{:.2f}".format(x1))
print("O valor de X2 é{:.2f}".format(x2))