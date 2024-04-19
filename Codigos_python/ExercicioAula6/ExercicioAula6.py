# 1- Faça um programa em Python que imprima os números pares entre 0 e 100
#contador = 0

while contador <= 100:
   print(contador)
   contador = contador + 2


# 2- Faça um programa em Python que imprima os números de 1 a 50 de 1 em 1 e de 52 a100 de 2 em 2.

contador = 1

while contador <= 100:
    if contador <= 50:
        print(contador)
        contador = contador + 1
    if contador >= 50:
        print(contador)
        contador = contador + 1

#3- Faça um programa em Python que leia um valor n, inteiro e positivo, calcule e mostre a seguinte
# soma:S = 1 + 1/2 + 1/3 + 1/4 +...

contador = 0
for i in range(1, int(input("Digite o valor de n: ")) + 1):
  contador += 1 / i
print("S = {}".format(contador))


#4- Escreva um algoritmo que leia um grupo de valores reais e determine quantos valores são
#positivos e quantos são negativos
#Determine, também, qual é o menor desses valores. Utilize o comando de repetição que desejar.

lista = []
count = 0

quant = int(input("Digite a quantiade de número que deseja digitar: "))
while quant != count:
   numero = lista.append(float(input("Digite um número: ")))
   count += 1
print("Lista: ", lista, "\nMaior: ", max(lista), "\nMenor: ", min(lista))


# 5- Temos um grupo de pessoas. Escreva um programa em Python que leia o sexo e a altura de cada pessoa,
# calcule e mostre a altura média das mulheres e dos homens separadamente.
# Utilize o comando de repetição que desejar

alturaHomem = 0
alturaMulher = 0
homem = 0
mulher = 0
for cont in range(1, 5):
    sexo = input('Masculino ou Feminino ? [M/F]').upper()[0]
    altura = float(input('Digite a sua altura : '))
    print('-'*20)
    if sexo == 'M':
        alturaHomem += altura
        homem = homem + 1

    if sexo == 'F':
        alturaMulher += altura
        mulher = mulher + 1
print("A altura média dos homens é {:.2f} Metros e a altura média das mulheres é {:.2f} Metros \n"
      .format(alturaHomem/homem , alturaMulher/mulher))


