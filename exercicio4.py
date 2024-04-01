#Digite um valor entre 0 e 9, mostre: “valor correto”, caso contrário mostre: “valor incorreto”

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


#3- Faça um programa em Python que obtenha o valor de uma compra, calcular e mostrar o valor da compra considerando o desconto, conforme descrito abaixo:para compras acima de R$ 200 a loja dá um desconto de 20% para as abaixo disso não tem desconto, mostre o valor da compra.

compra = float(input("Digite aqui o valor da compra R$:"))

if compra > 200:
    desconto = compra * 0.80
    print("Você pagará o valor R$:{}".format(desconto))
else:
    print("Sua compra não possui desconto..o valor a pagar é de R${}".format(compra))


#4- Escreva um programa em Python que solicite ao usuário os valores de três contas de consumo (p.ex. água, luz e telefone) e o valor de seu salário. Verifique se o salário ésuficiente para pagar as três contas, caso não seja apresente a mensagem “Salário insuficiente!”. Caso seja, apresente o valor que restou do salário após pagar as contas.#

agua = float(input("Digite aqui o valor da conta de Água R$:"))
luz = float(input("Digite aqui o valor da conta de Luz R$:"))
telefone = float(input("Digite aqui o valor da conta de Telefone R$:"))
salario = float(input("Digite o valor do salário R$:"))

conta = agua + luz + telefone

if salario > conta:
    saldo = salario - conta
    print("O valor que sobrou é de R${}".format(saldo))
else:
    print("Salário Insuficiente!!!")
    
#Testando clone do git....
