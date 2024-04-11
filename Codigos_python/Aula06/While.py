contador = 1
mediaDaSala = 0
while contador <= 10:
    n1 = float(input("Digite aqui a n1:"))
    n2 = float(input("Digite aqui a n2:"))
    media = (n1+n2)/2
    mediaDaSala +=media
    contador+= 1
    print("A média é {}".format(media))
mediaDaSala /= contador - 1
print("A média da sala é {}".format(mediaDaSala))
