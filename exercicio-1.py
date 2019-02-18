# # Exercicio 1

n1 = float(input('Digite o primero número:'))
n2 = float(input('Digite o segundo número:'))


soma = n1+n2
 print(soma) # 'A soma dos números é" +str(soma)'

subtração = n1-n2
print(subtração)

multiplicação = n1*n2
print(multiplicação)

divisão = n1/n2
print(divisão)

# Exercicio 2

n1 = float(input('Digite o primero número:'))
n2 = float(input('Digite o segundo número:'))
n3 = float(input('Digite o terceiro número:'))
n4 = float(input('Digite o quarto número:'))

média = (n1 + n2 + n3 + n4)/4
print(média)

# Exercicio 3

n1 = int(input('Digite a temperatura em graus e receba o resultado em Fahrenheit.'))

F = (n1 * 9/5) + 32
print(F)

# Exercicio 4

palavra = input('Digite uma palavra:')
letra = input('Digite uma letra:')

print(palavra.count(letra))

# Exercicio 5

quantidade = int(input("Digite quantos números terá no calculo"))
#  Com lista:

lista = []

for i range(quantidade):
    num = float(input("Digite o número"))
    lista.append(num)

print(lista)

for numero in lista:
    soma = soma + numero

media = soma/quantidadepir
print("A média será: "+str(media))