# 1- Faça um programa em Python que imprima os números pares entre 0 e 100

contador = 0

while contador <= 100:
    print(contador)
    contador = contador + 2


# 2- Faça um programa em Python que imprima os números de 1 a 50 de 1 em 1 e de 52 a100 de 2 em 2.

contador = 1


while contador <= 100:
    if contador <= 50:
        print(contador)
    contador = contador + 1
    if contador>=50:
        print(contador)
        contador = contador + 1


    
