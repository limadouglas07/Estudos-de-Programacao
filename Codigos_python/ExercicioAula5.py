totalcompra = float(input("Digite o valor total da compra:"))
parcelas = int(input("Digite aqui o número de parcelas 2/4/6/8:"))

if parcelas == 2:
    total = (totalcompra * 1.03)/2
    print("O valor das duas parcelas de {} é R$ {:.2f}".format(parcelas, total))
elif parcelas == 4:
    total = (totalcompra * 1.07)/4
    print("O valor das duas parcelas de {} é R$ {:.2f}".format(parcelas, total))
elif parcelas == 6:
    total = (totalcompra * 1.09)/6
    print("O valor das duas parcelas de {} é R$ {:.2f}".format(parcelas, total))
elif parcelas == 8:
    total = (totalcompra * 1.12)/8
    print("O valor das duas parcelas de {} é R$ {:.2f}".format(parcelas, total))
else:
    print("Dados inválidos!!!!")   
    
    
    
# Programa para calcular o final da placa e imprimir o rodízio da semana.#

placa = int(input("Digite aqui a sua placa:"))
digito = placa % 10

if digito == 1 or digito == 2:
    rodizio = "Segunda-Feira"
elif digito == 3 or digito == 4:
    rodizio = "Terça-Feira"
elif digito == 5 or digito == 6:
    rodizio = "Quarta-Feira"
elif digito == 7 or digito == 8:
    rodizio = "Quinta-Feira"
else:
    rodizio = "Sexta-Feira"
print("Este veículo está com rodízio na {} ".format(rodizio))


# Laço For
animais =[ 'gato','cachorro','leão','camelo']
for a in animais:
    print(a,"string de tamanho", len(a))
    
sequencia = [0,1,2,3,4,5]
for num in sequencia:
    print(num)
    
for i in range(10):
    print(i, end=" ")

for i in range (3,8):
    print(i,end=" ")
    
for i in range (0,21,2):
    print(i, end =" ")