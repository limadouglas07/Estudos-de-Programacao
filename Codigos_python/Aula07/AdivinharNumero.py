import random
numero = random.randint(0,100)
chute = -1
contador = 0

while chute != numero:
    chute = int(input("Digite o número de 0 a 100?:"))
    contador+= 1
    if numero == chute:
        print("Você acertou!!!")
    elif numero > chute:
        print("O número é maior")
    else:
        print("O número é menor")
print("Fim do jogo!!! você tentou {} tentativas!!!!".format(contador))




