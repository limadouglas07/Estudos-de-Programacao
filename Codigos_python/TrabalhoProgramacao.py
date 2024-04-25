dividendo = int(input("Digite aqui um número na base decimal:"))
numero_digitado = dividendo
quociente = 1
lista = []

while quociente >= 1:
    resto = dividendo % 2
    lista.insert(0, resto)
    quociente = dividendo // 2
    dividendo = quociente

binario = ''.join([str(item) for item in lista])
print("A base decimal ", numero_digitado, "em binário é", binario)



dividendo = int(input("Digite aqui um número na base decimal:"))
numero_digitado = dividendo
quociente = 1
lista = []
while quociente >= 1:
    resto = dividendo % 8
    lista.insert(0, resto)
    quociente = dividendo // 8
    dividendo = quociente
binario = ''.join([str(item) for item in lista])
print("A base decimal ", numero_digitado, "em Octal é", binario)



hexadecimal = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]
n = int(input("Digite aqui um número na base decimal:"))
r = []
while n > 0:
    r.append(hexadecimal[(n % 16)])
    n = n // 16
for i in range(len(r)-1,-1,-1):
    print(r[i], end="")
