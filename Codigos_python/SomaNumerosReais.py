

soma = 0
for i in range(10):
    n = float(input("Digite aqui o número %d:"%(i+1)))
    soma = soma + n
print("A soma total dos números digitados é {}".format(soma))    
    
soma = 0
for i in range (1,101):
    soma+=i
print("Soma todos os números entre 1 e 100 é %d"%soma)