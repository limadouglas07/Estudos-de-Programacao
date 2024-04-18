decimal = int(input("Digite um número inteiro da base decimal:"))
binario = ''

while decimal != 0:
    resto = decimal % 2
    binario =str(resto) + binario
    decimal = decimal // 2
print("A conversão para binário é %s." %binario)