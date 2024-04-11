num = 0
contador = 0
soma = 0

while num!= -1:
    num = float(input("Digite um número (-1) para sair:"))
    if num != -1:
     soma+= num
     contador+= 1
media = soma/contador
print("A média é {:.2f}".format(media))
