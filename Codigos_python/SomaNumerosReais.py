print("Digite aqui dez número:")

soma = 0.0
for i in range(10):
    soma = soma + float(input("número %d:" % (i + 1)))
    print(soma)
    
    
soma = 0
for i in range (1,101):
    soma+=i
print("Soma todos os números entre 1 e 100 é %d"%soma)