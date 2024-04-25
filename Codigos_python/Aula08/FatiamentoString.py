numero = input("Digite algo:")
print(numero[::-1]) # Imprime de trás para frente
print(numero[::]) # Imprime normal

a = "Fizeram a atividade?"
print(a.replace("atividade" , "exercicio"))
print(a)

a = a.replace("atividade" , "tarefa")
print(a)
print(a.lower())
print(a.upper())

texto = input("Digite uma frase:")
lista = texto.split()
print(lista)
print("A frase tem {} palavras".format(len(lista)))