#1- Escreva um algoritmo que solicite um número ao usuário. Caso seja digitado um valor entre 0 e 9, mostre: “valor #correto”, caso contrário mostre: “valor incorreto.

n = int(input("Digite aqui um número:"))

if n>=0 and n<=9:
    print("Valor correto")
else:
    print("Valor incorreto")


