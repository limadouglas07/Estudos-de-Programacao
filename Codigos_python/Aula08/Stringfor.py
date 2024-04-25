texto = input("Digite algo:")
invertida = ""
for letra in texto:
    invertida = letra + invertida
print(invertida)

s = "ABC"
print(s + "C")
idade = 18
print("João tem {} anos de idade" .format(idade))
print("João tem tem %05d anos de idade" % idade)

numero = 12.34
print("%f" % numero)
print("%.3f" % numero)
print("%8.3f" % numero)
print("%08.3f" % numero)

nome = "James Kirk"
idade = 28
print("%s tem %d anos de idade" %(nome ,idade))
print(f"{nome} tem {idade:03d}anos de idade.")
print("{} tem {:03d} anos de idade.".format(nome, idade))
