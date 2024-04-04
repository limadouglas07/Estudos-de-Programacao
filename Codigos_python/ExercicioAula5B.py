idade = int(input("Digite aqui a sua idade:"))

if idade < 16 :
    print("não-eleitor ")
elif idade >= 18 and idade <=65:
    print("eleitor obrigatório ")
elif idade >= 16 and idade < 18:
    print ("eleitor facultativo")
else:
    print("eleitor facultativo")