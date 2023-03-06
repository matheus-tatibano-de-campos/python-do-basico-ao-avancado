"""


# 1 - Faça um programa que o determine o mostre os cincos primeiros multiplos de 3 considerando números maiores que 0
for num in range(3, 16, 3):
    print(num)

 # 2 - Um programa que escreva na tela de 1 a 100 3 vezes
for num in range(1, 101):
    print(num)

numero = 1

while numero < 101:
    print(numero)
    numero = numero + 1

i = 1

while True:
    print(i)
    i += 1
    if i > 100:
        break

# 3 - Fazer um programa em while de 10 a 0 e escreva Fim no final da execução
numero = 10

while numero >= 0:
    print(numero)
    numero = numero - 1
print("FIM!")

# 4 - Escreva um programa que declare um inteiro iniciando em 0 incremente de 1000 em 1000 ate 100mil

for numero in range(0, 100000, 1000):
    print(numero)

# 5 - Faça um programa que peça ao usuario digitar 10 valores e some-os
soma = 0
for i in range(10):
    valor = int(input("Digite um valor: "))
    soma += valor

print("A soma dos valores é:", soma)

# 6 - Faça um programa que peça ao usuario digitar 10 valores e imprima sua media
soma = 0
for i in range(10):
    valor = int(input("Digite um valor: "))
    soma += valor / 10

print("A soma dos valores é:", soma)

# 7 - Faça um programa que peça ao usuario digitar 10 valores ignorando negativos e imprima sua média
soma = 0
contagem = 0
for i in range(10):
    valor = int(input("Digite um valor: "))
    soma += valor / 10
    if valor >= 0:
        soma += valor
        contagem += 1

if contagem > 0:
    media = soma / contagem
    print("A média dos valores positivos é:", media)
else:
    print("Digite um valor POSITIVO")



# 9 - faça um programa que leia um número inteiro N e deposi imprima os n primeiros numeros naturais impares

n = int(input("Digite um número inteiro: "))
# Inicializa o contador de números ímpares e o número atual
cont_impares = 0
num_atual = 1
# Loop para imprimir os N primeiros números ímpares
while cont_impares < n:
    if num_atual % 2 == 1:  # Verifica se o número atual é ímpar
        print(num_atual)
        cont_impares += 1  # Incrementa o contador de números ímpares
    num_atual += 1  # Incrementa o número atual

# 10 - Faça um programa que calcule e mostre a soma dos 50 primeiros naturais pares
soma = 0

for i in range(1, 51):
    if i % 2 == 0:
        soma += i
        print(soma)

# 11 - Faça um programa que leia um número inteiro positivo e imprima todos os naturia de 0 ate N em ordem crescente
num = int(input("Digite um numero inteiro positivo:"))
for i in range(1, num+1):
    print(i)

# 12 -Faça um programa que leia um número inteiro positivo e imprima todos os naturia de 0 ate N em ordem decrescente
num = int(input("Digite um numero inteiro positivo:"))
for i in range(num, -1, -1):
    print(i)

# 13 - faça um programa que leia um número inteiro positivo par e retorne os numero pares ate N
numero = int(input("Digite um numero inteiro positivo par:"))
if numero % 2 != 0:
    print('O número digitado não é par')
else:
    for numero in range( 0, numero+1, 2):
        print(numero)

# 14 - Faça um programa que leia um número inteiro positivo par N e imprima-os em ordem decrescente
numero = int(input("Digite um numero inteiro positivo par:"))
if numero % 2 != 0:
    print('O número digitado não é par')
else:
    for numero in range(numero, -1, -2):
        print(numero)

# 15 - Faça um programa que leia um número inteiro positivo impar N e imprima todos numeros impartes ate N
numero = int(input("Digite um numero inteiro positivo par:"))
if numero % 2 == 0:
    print('O número digitado não é impar')
else:
    for numero in range(1, numero+1, 2):
        print(numero)

# 16 - Faça um programa que leia um número inteiro positivo impar N e imprima todos numeros impartes ate N decrescente
numero = int(input("Digite um numero inteiro positivo par:"))
if numero % 2 == 0:
    print('O número digitado não é impar')
else:
    for numero in range(numero, -1, -2):
        print(numero)

# 17 - Faça um programa que leia um número inteiro positivo n e calcule a soma dos n primeiros numeros

numero = int(input("Digite um numero inteiro positivo:"))
if numero <= 0:
    print("O número digitado não é positivo.")
else:
    soma = 0
    for i in range(1, numero+1):
        soma += i
print(soma)

# 18 - Escreva um algoritmo que leia certa quantidade de números e imprima o maior deles e quantas vezes o maior número foi lido, a quantidade de números a serem lidos deve ser fornecida pelo usuario
qnt = int(input("Digite a quantidade de números a serem lidos:"))
maior = float('-inf')
maior_lido = 0
for i in range(qnt):
    numero = float(input("Digite um número: "))
    if numero > maior:
        maior = numero
        maior_lido = 1
    elif numero == maior:
        maior_lido += 1
print("Maior número:", maior)
print("Quantidade de vezes que o maior número foi lido:", maior_lido)

# 19 - Escreva um programa que leia um número inteiro entre 100 e 999 e imprima na saida a cada um dos algarismos que compõem o numero
numero = (input("Digite um númro inteiro entre (100 e 999):"))
print(numero[0])
print(numero[1])
print(numero[2])

# 20 - Ler uma sequendia de numeros inteiros e determinar se eels sao pares ou nao, devera ser informado o numero de dados lidos e numeros de valores pares o processo termina quando for digitado o numero 1000
numeros_lidos = 0
numeros_pares = 0

while True:
    numero = int(input("Digite um número inteiro (ou 1000 para sair): "))
    if numero == 1000:
        break
    numeros_lidos += 1
    if numero % 2 == 0:
        numeros_pares += 1
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")

print(f"Foram lidos {numeros_lidos} números, dos quais {numeros_pares} são pares.")

# 21 -
numero1 = int(input("Digite o primeiro numero:"))
numero2 = int(input("Digite o segundo numero:"))
multiplica_impar = 1
soma = 0
for numero in range(numero1, numero2 +1):
    if numero % 2 == 0:
        soma += numero
    else:
        multiplica_impar *= numero
if numero1 %2 == 0:
    soma += numero1
else:
    multiplica_impar *= numero1
if numero2 %2 == 0:
    soma += numero2
else:
    multiplica_impar *= numero2

print(f"Soma dos números pares: {soma}")
print(f"Multiplicação dos números ímpares: {multiplica_impar}")

# 22 - Um programa que permita introduzir uma sequencia arbitraria de notas (10 a 20) e que mostre na tela a média aritmética , o programa encerra ao digitar uma nota fora do padrao
notas = []
while True:
    nota = float(input("Digite uma nota (entre 10 e 20): "))
    if nota < 10 or nota > 20:
        print("Nota fora do padrão. Encerrando programa.")
        break
    notas.append(nota)

if len(notas) > 0:
    media = sum(notas) / len(notas)
    print("Média aritmética das notas: {:.2f}".format(media))
else:
    print("Nenhuma nota foi digitada.")

# 23 - Faça um algoritmo que leia um número positivo e imprima seus divisores
numero = int(input("Digite um número inteiro positivo:"))
for i in range(1, numero//2 + 1):
    if numero % i == 0:
        print(i)

# 24 - Faça um algoritmo que leia um número positivo e imprima a soma de todos seus dividores com exceção dele propio /
numero = int(input("Digite um número inteiro positivo:"))
soma = 0
for i in range(1, numero):
    if numero % i == 0:
        soma += i
print("A soma dos divisores de", numero, "é:", soma)

# 25 - Faça um programa que some todos os números naturais abaixo de 1000 que são multiplos de 3 ou 5
soma = 0
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        soma += i
print("A soma de todos multiplos de 3 ou 5 ate 1000 é:", soma)

# 26 Faça um algoritmo que encontre o primeiro multiplo de 11, 13 ou 17 apos o número dado
num = int(input("Digite um número: "))
i = num + 1

while True:
    if i % 11 == 0 or i % 13 == 0 or i % 17 == 0:
        print("O primeiro múltiplo de 11, 13 ou 17 após", num, "é:", i)
        break
    i += 1

# 27 - Faça um programa que leia um valor n inteiro e positivo , calcule e mostre o valor e. conforme a formula e = 1+ 1/1!+1/2!+1/3!+1/n!
num = int(input("Digite um número: "))
e = 1 + 1/1+1/2+1/3+1/num
print(e)

"""