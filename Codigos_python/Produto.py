produto = str(input("Digite aqui o produto:"))
valor = float(input("Digite o valor da compra:"))

if valor < 10:
    print("O produto é a {} e o valor de venda é R$ {}".format(produto, valor * .70 + valor))
elif valor >= 10 and valor < 30:
    print("O produto é a {} e o valor de venda é R$ {}".format(produto, valor * .50 + valor))
elif valor >= 30 and valor < 50:
    print("O produto é a {} e o valor de venda é R$ {}".format(produto, valor * .40 + valor))
else:
    print("O produto é a {} e o valor de venda é R$ {}".format(produto, valor * .30 + valor))