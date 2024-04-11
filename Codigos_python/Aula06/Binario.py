binario = input("Digite o binário:")
potencia = len(binario) - 1
decimal = 0

for digito in binario:
    decimal = decimal + int(digito) * 2 **  potencia
    potencia = potencia - 1 
print("A conversão do binário {} para decimal é {}:".format(binario,decimal))

    