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