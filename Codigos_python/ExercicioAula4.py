#2- Crie um algoritmo que solicite ao usuário o seu turno de trabalho e a quantidade de horas trabalhadas, calcule
# e mostre o valor do salário. Considere os valores de horas a seguir, de acordo com o turno de trabalho.
# Caso o turno seja igual a ‘N’ (utilize um caractere para representar) o valor da hora trabalhada é R$ 45,00,
# caso contrário é R$37,50.

turno = str(input("Digite aqui o seu turno: 'N' para noturno e 'V' para vespertino:"))
horastrabalho = float(input("Digite as horas trabalhadas:"))

if turno == "N":
    print("Você irá receber o salário de R${:.2f}".format(45*horastrabalho)+" Reais pelo trabalho...")
else:
    print("Você irá receber o salário de R${:.2f}".format(37.50*horastrabalho)+" Reais pelo trabalho...")




