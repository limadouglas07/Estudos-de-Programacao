nota1= float(input("Digite a sua nota:"))
nota2= float(input("Digite a sua nota:"))

media = (nota1+nota2)/2

if media>=6:
    print('Você foi Aprovado!!! com média {:.2f}'.format(media))
else:
    print("Você foi Reprovado!!! com média {:.2f}".format(media))

