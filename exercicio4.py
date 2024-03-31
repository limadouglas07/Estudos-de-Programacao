#1- Escreva um algoritmo que solicite um número ao usuário. Caso seja digitado um valorentre 0 e 9, mostre: “valor correto”, caso contrário mostre: “valor incorreto”

n = int(input("Digite aqui um número:"))
if n>=0 and n<=9:
    print("Valor correto")
else:
    print("Valor incorreto")


#2- Crie um algoritmo que solicite ao usuário o seu turno de trabalho e a quantidade de horas trabalhadas, calcule e mostre o valor do salário. Considere os valores de horas a seguir, de acordo com o turno de trabalho. Caso o turno seja igual a ‘N’ (utilize um caractere para representar) o valor da hora trabalhada é R$ 45,00, caso contrário R$37,50#

turno = (input("Digite aqui o turno: N "))
h = int(input("Digite as horas trabalhadas:"))

if turno == "N" or turno == "n":
    horas = h * 45.00
    print("Suas horas trabalhadas foram de {}".format(horas))
else:
    horas = h * 37.50
    print("Suas horas trabalhadas foram de {}".format(horas))