valor = float(input("Digite o valor da compra:"))
percentual = float(input("qual o valor do percentual:"))
valornovo= valor*(1+percentual/100)
print("O valor R${:.2f} com acréscimo de {:.1f}% é de R$ {:.2f}".format(valor, percentual,valornovo))
