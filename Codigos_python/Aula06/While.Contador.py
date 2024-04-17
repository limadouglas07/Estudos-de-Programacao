contador = 0

while contador < 100:
    contador += 1
    if contador == 6:
        print("Não vou mostrar o número 6..")
        continue
    print(contador)
    if contador == 40:
        break