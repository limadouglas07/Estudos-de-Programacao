contador = 0

while contador < 45:
    contador += 1

    if contador == 6:
        print("Não vou mostrar o número 6..")
        continue

    if contador >= 10 and contador <= 27:
        print("Não vou mostrar", contador)
        continue

    print(contador)
    if contador == 40:
        break