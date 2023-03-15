"""
# 1- 1 atribua o seguinte valor a este vetor 1, 0, 5, -2, -5, 7
# 2 armazene em uma variavel inteire simples a soma entre os valores das posiçoes  a[0], a[1] e a[5] do vetor e motre na tela a soma
# 3 modifique o vetor de posicao 4, atribuindo a esta posicao o valor 100
# 4 mostre na tela  cada valor do vetor A um em cada linha:

# atribui o valor 1, 0, 5, -2, -5, 7 ao vetor A
A = [1, 0, 5, -2, -5, 7]

# armazena a soma dos valores das posições 0, 1 e 5 do vetor A em uma variável
soma = A[0] + A[1] + A[5]

# mostra na tela a soma
print("A soma dos valores nas posições 0, 1 e 5 do vetor é:", soma)

# modifica o valor da posição 4 do vetor A
A[4] = 100

# mostra na tela cada valor do vetor A um em cada linha
for i in A:
    print(i)

# 2 - Crie um programa que le 6 valores inteiros  e mostre-os na tela

numeros = []

for i in range(6):
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)

print("Os números digitados foram:")
for numero in numeros:
    print(numero)

# 3 - Ler um conjunto de números reais, armazenando-o em um vetor e calcular o quadrado dos componentes deste vetor,
# Armazenando o resultado em outro vetorm os conjuntos tem 10 elementos cada, imprima todos conjuntos
vetor1 = []

for i in range(10):
    numero = float(input("Digite um número real:"))
    vetor1.append(numero)

vetor2 = []

for numero in vetor1:
    numero_qd = numero ** 2
    vetor2.append(numero_qd)
print("O vetor lido é:", vetor1)
print("O vetor dos quadrados é:", vetor2)

# 4 - Faça um programa que leia um vetor de 8 posiçôes e, em seguida leia também dois valores X e Y
# quaisquer correspondentes as duas posições no vetor. Ao final seu programa deverá escrever a soma dos valores
# encontrados nas respectivas posições X e Y

vetor = []
for i in range(8):
    numero = float(input("Digite um número:"))
    vetor.append(numero)
x = int(input('Digite um numero inteiro:'))
y = int(input('Digite um numero inteiro:'))

soma = vetor[x] + vetor[y]
print(f"A soma dos valores nas posições {x} e {y} é {soma}")

# 5 - Leia um vetor de 10 posições. Contar e escrever quantos valores pares ele possui

vetor = []
numeros_pares = 0
for i in range(10):
    numero = float(input("Digite um número:"))
    if numero % 2 == 0:
        numeros_pares += 1
    else:
        pass
    vetor.append(numero)
print(f'A quantidade de números pares no vetor é {numeros_pares}')

# 6 - Faça um programa que receba um vetor com 10 posições. Em seguida deverá
# ser impresso o maior e o menor elemento do vetor

vetor = []
for i in range(10):
    numero = float(input("Digite um número:"))
    vetor.append(numero)

print(max(vetor))
print(min(vetor))

# 7 - Escreva um programa que leia 10 numeros inteiros e o armazene em um vetor, imprima o vetor
# o maior elemento e a posição que ele se encontra

vetor = []
for i in range(10):
    numero = float(input("Digite um número:"))
    vetor.append(numero)

n_max = max(vetor)
print(max(vetor))
print(vetor.index(n_max))


# 8 - Crie um programa que lê 6 valores inteiros e, em seguida mostre na tela os valores lidos
# na ordem inversa

vetor = []
for i in range(6):
    numero = float(input("Digite um número:"))
    vetor.append(numero)

print(vetor[::-1])

# 9 - Crie um programa que leia 6 valores inteiros pares. e em seguida mostre na tela os valores
# lidos na ordem inversa

vetor = []
for i in range(6):
    numero = float(input("Digite um número:"))
    if numero %2 == 0:
        vetor.append(numero)
    else:
        print('Este não é um valor par')

print(vetor[::-1])

# 10 - Faça um programa para ler 15 notas armazene em um vetor, calcule e imprima a media geral

vetor = []
for i in range(15):
    numero = float(input("Digite uma nota:"))
    vetor.append(numero)

soma = sum(vetor)
notas = len(vetor)
media = soma / notas
print(f"A media das notas é {media}")

# 11 - Faça um programa que preencha um vetor com 10 numeros reais, calcule e mostre a quantidade
# de numeros negativos e a soma dos numeros positivos dese vetor

vetor = []
numeros_negativo = 0
for i in range(10):
    numero = float(input("Digite um número:"))
    if numero > 0:
        vetor.append(numero)
    else:
        numeros_negativo += 1

print(sum(vetor))
print(f'A quantidade de números negativos é{numeros_negativo}')

# 12 - Fazer um programa para ler 5 valores e mostrar todos valores lidos juntamente com o maior o menor e a media

vetor = []

for i in range(5):
    numero = float(input("Digite um número:"))
    vetor.append(numero)
maior = max(vetor)
menor = min(vetor)
qnt = len(vetor)
soma = sum(vetor)
media = soma / qnt
print(f"Os valores são: {vetor} o maior é {maior} o menor {menor} a média é {media}")

# 13 - Fazer um programa para ler 5 valores, mostrar a posicao do maior e do menor valor

vetor = []

for i in range(5):
    numero = float(input("Digite um número:"))
    vetor.append(numero)
maior = max(vetor)
menor = min(vetor)
posicao_maior = vetor.index(maior)
posicao_menor = vetor.index(menor)
print(f'O menor valor se encontra  no index {posicao_maior} e o menor no {posicao_menor}')

# 14 - Fazer um programa que leia um vetor de 10 posições veficiar se existe valores iguais e escrevelos

vetor = []

for i in range(10):
    numero = int(input("Digite um número inteiro: "))
    vetor.append(numero)

repetidos = set()

for numero in vetor:
    if vetor.count(numero) > 1:
        repetidos.add(numero)

if len(repetidos) > 0:
    print("Os valores repetidos são:")
    for numero in repetidos:
        print(numero)
else:
    print("Não foram encontrados valores repetidos.")

# 15 - Leia um vetor de 20 números inteiros escreva os elementos do vetor eliminando elementos repetidos

vetor = []
for i in range(20):
    numero = int(input("Digite um número inteiro: "))
    vetor.append(numero)

lista_unicos = []
for elemento in vetor:
    if elemento not in lista_unicos:
        lista_unicos.append(elemento)

print("Elementos únicos do vetor:", lista_unicos)

# 16 - Faça um programa que lleia  em vetor de 5 posiçoes e depois um codigo se for zero finaliza o progra,a
# se for 1 mostre o vetor na ordem se for 2 mostre o na ordem inversa se for diferente disso mostre comando invalido

vetor = []
for i in range(5):
    numero = int(input("Digite um número inteiro: "))
    vetor.append(numero)

print('escolha uma opção:')
print('1 - mostre o vetor na ordem')
print('2 - mostra o vetor na ordem inversa')
print('0 - finaliza o programa')

opcao = int(input('Digite a opçao:'))

if opcao == 1:
    print(vetor)
elif opcao ==2:
    print(vetor[::-1])
elif opcao == 0:
    pass

else:
    print('Opção Invalida!')

# 17 - Leia um vetor de 10 posições e atribua o valo - oara todos elementos que possuirem valor negativo
vetor = []
for i in range(10):
    numero = int(input("Digite um número inteiro: "))
    if numero < 0:
        numero = 0
    vetor.append(numero)
print(vetor)

# 18 - Leia um vetor de 1o números leia um numero x conte os multipls de um numero x num vetor e mostre os na tela

vetor = []
multiplos = []
for i in range(4):
    numero = int(input("Digite um número inteiro: "))
    vetor.append(numero)

x = int(input("Digite o valor de x:"))
for numero in vetor:
    if numero % x == 0:
        multiplos.append(numero)

if len(multiplos) == 0:
    print(f"Não há múltiplos de {x} no vetor.")
else:
    print(f"Múltiplos de {x} no vetor: {multiplos}")

# 19 - Faça um vetor de tamamnho 50 preenchido com o seguinte valor (i+5*i)%(i+1) sendo i a posição do elemento
vetor = []
for i in range(50):
    numero = (i + 5 * i) % (i +1)
    vetor.append(numero)
print(vetor)

# 20 - Escreva um pograma que leia numeros inteiro do intervalo [0,50} e os armazene em um vetor com 10 posições
# Preencha um segundo vetor com apenas os numeros impares
# do primeiro vetor imprima os 2 vetores 2 elementos por linha

vetor = []
vetor2 = []
for i in range(10):
    numero = int(input('Digite um numero entre 0 e 50 :'))
    if numero > 0 and numero < 50:
        vetor.append(numero)
for numero in vetor:
    if numero % 2 == 1:
        vetor2.append(numero)

print('Números:   ', end='')
for i, num in enumerate(vetor):
    if i > 0 and i % 2 == 0:
        print()
    print(f'{num:>2} ', end='')
print()

print('Ímpares:   ', end='')
for i, num in enumerate(vetor2):
    if i > 0 and i % 2 == 0:
        print()
    print(f'{num:>2} ', end='')
print()

# 21 - Faça um programa que recebe do usuario dois vetores A,B com 10 números inteiros, crie um vetor C e calcule C = A - B

vetorA = []
vetorB = []
vetorC = []

for i in range(10):
    numero = int(input("Digite um número inteiro: "))
    vetorA.append(numero)

for i in range(10):
    numero = int(input("Digite um número inteiro: "))
    vetorB.append(numero)

for i in range(10):
    sub = vetorA[i] - vetorB[i]
    vetorC.append(sub)
print(vetorC)

# 22 - Faça um programa que leia dois vetores de 10 posiçoes e calcule outro vetor contendo nas posiç~es pares os valores do primeiro e nas posições impares o valores do segundo vetor
vetorA = []
vetorB = []
vetorC = []

for i in range(10):
    numero = int(input("Digite um número inteiro: "))
    vetorA.append(numero)

for i in range(10):
    numero = int(input("Digite um número inteiro: "))
    vetorB.append(numero)

for i in range(10):
    if i % 2 == 0:
        vetorC.append(vetorA[i])
    else:
        vetorC.append(vetorB[i])


print(vetorC)

# 23 - Ler dois conjustos de números reais armazenando-os em vetores e calcular o produto escalar entre eles
# Os conjuntos tem 5 elementos cada, imprimr os dois conjuntos eo produto escaolar
# o protudo escalar é dado x1 * y1 + x2 * y2
vetorA = []
vetorB = []
produto = 0

for i in range(5):
    numero = int(input("Digite um número inteiro: "))
    vetorA.append(numero)

for i in range(5):
    numero = int(input("Digite um número inteiro: "))
    vetorB.append(numero)

for i in range(5):
    produto += vetorA[i] * vetorB[i]

print(f'Vetor A{vetorA}')
print(f'Vetor B{vetorB}')
print(f'O produto escalar é: {produto}')

# 24 - Faça um programa que leia dez conjuntos de dois valores , o primeiro representa os alunos, e o segundo representa a altura em metros,
#encontre o aluno mais baixo, o maus alto e moste o numero do aluno mais baixo e alto juntamente com sua altura

num_alunos = 10
alturas = []


for i in range(num_alunos):
    aluno = i + 1
    altura = float(input(f"Digite a altura do aluno {aluno}: "))
    alturas.append((aluno, altura))


mais_baixo = alturas[0]
mais_alto = alturas[0]

for aluno, altura in alturas:
    if altura < mais_baixo[1]:
        mais_baixo = (aluno, altura)
    elif altura > mais_alto[1]:
        mais_alto = (aluno, altura)

print(f"O aluno mais baixo é o {mais_baixo[0]} com {mais_baixo[1]:.2f}m")
print(f"O aluno mais alto é o {mais_alto[0]} com {mais_alto[1]:.2f}m")

# 25 - Faça um programq que preencha um vetor de tamanho 100 com os 100 primeiros naturais que nao são multiplos de 7 ou que terminam em 7

vetor = []
numero = 1
while len(vetor) < 100:
    if numero % 7 != 0 and numero % 10 != 7:
        vetor.append(numero)
    numero += 1

print(vetor)

# 26 - Faça um programa que calcule o desvio padrao de um vetor v contendo n = 10 numeros, onde m é a media do vetor

import math

vetor = []

for i in range(5):
    numero = int(input("Digite um número inteiro: "))
    vetor.append(numero)

media = sum(vetor)/len(vetor)

soma_difs = sum([(x-media)**2 for x in vetor])

desvio_padrao = math.sqrt(soma_difs/(len(vetor)-1))
print(f"O desvio padrão do vetor {vetor} é {desvio_padrao:.2f}.")

# 27 - Leia 10 números inteiros e armazene em um vetor. em seguida escreve os elementos que sao primos e suas posições no vetor


def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


vetor = []

for i in range(10):
    num = int(input(f"Digite o {i+1}o número: "))
    vetor.append(num)

primos = []
for i, num in enumerate(vetor):
    if eh_primo(num):
        primos.append((num, i))

if primos:
    print("Os números primos no vetor são:")
    for num, pos in primos:
        print(f"{num} (posição {pos})")
else:
    print("Não há números primos no vetor.")

# 28 - Leia 10 números  inteiros e armazene em um vetoe v crie dois novos vetores copie os valores impares de v  para v1 e v2 tem no maximo 10 elementos
#mas nem todos os elementos são utilizados, no final escreva os elementos utilizados de v1 e v2

vetor = []
vetor1 = []
vetor2 = []

for i in range(10):
    numero = int(input("Digite um número inteiro: "))
    vetor.append(numero)
    if numero % 2 == 0:
        vetor1.append(numero)
    else:
        vetor2.append(numero)

print("Valores utilizados de v1:", vetor1[:len(vetor1)])  # lista os elementos de v1
print("Valores utilizados de v2:", vetor2[:len(vetor2)])

# 29 - Faça um programaq que receba 6 números inteiros e mostre:
# Os números pares digitados
# A soma dos números pares digitados
# A quantidade de numeros impares digitados;

vetor = []
pares = []
impares = []
soma = 0
qnt_impares = 0

for i in range(6):
    numero = int(input("Digite um número inteiro: "))
    vetor.append(numero)
    if numero % 2 == 0:
        soma += numero
        pares.append(numero)
    else:
        impares.append(numero)
        qnt_impares += 1
print(f'Os pares são {pares} a soma dos pares {soma} a quantidade de números impares é {qnt_impares}')

# 30 - Faça um programa que leia dois vetores de 10 elementos, Crie um vetor que seja a intersecção entre os 2 vetores
# ou seja que contém apenas os números que estão em ambos, não deve ter números repetidps

vetor = []
vetor1 = []
vetor2 = []

for i in range(10):
    numero = int(input(f"Digite o {i+1}  número inteiro: "))
    vetor1.append(numero)

for i in range(10):
    numero = int(input(f"Digite o {i+1}  número inteiro: "))
    vetor2.append(numero)

conj1 = set(vetor1)
conj2 = set(vetor2)

intersecao = conj1.intersection(conj2)

lista_intersecao = sorted(list(intersecao))

print("Vetor de interseção: ", lista_intersecao)

# 31 - Faça um programa que leia dois vetores de 10 elementos crie um vetor que seja a uniao entre os 2 vetores anteriores
# nao deve conter elementos repetidos

vetor = []
vetor1 = []
vetor2 = []

for i in range(10):
    numero = int(input(f"Digite o {i+1}  número inteiro: "))
    vetor1.append(numero)

for i in range(10):
    numero = int(input(f"Digite o {i+1}  número inteiro: "))
    vetor2.append(numero)

conj1 = set(vetor1)
conj2 = set(vetor2)
conj3 = conj1 | conj2
print(conj3)

# 32 - Leia dois vetores de inteiros x e y cada um com 5 elementos (garanta que o usuario nao adicione elemento repetidos,
# calcule e mostre os vetores abaixo
# soma entre  x e y de todos elementos
# produto ente x e y multiplicacao de cada elemento da mesma posicao
# diferença ente x e y apenas os elementos que aparecem nos dois vetores
# Uniao entre x e y todos os elemetnos de x e todos elementos de y que nao estao em x


vetor = []
vetor1 = []
vetor2 = []
soma = 0
multi = 0


for i in range(5):
    numero = int(input(f"Digite o {i+1}  número inteiro: "))
    vetor1.append(numero)

for i in range(5):
    numero = int(input(f"Digite o {i+1}  número inteiro: "))
    vetor2.append(numero)

for i in range(5):
    soma += vetor1[i] + vetor2[i]

for i in range(5):
    multi += vetor1[i] * vetor2[i]


uniao = vetor1.copy()
for elemento in vetor2:
    if elemento not in vetor1:
        uniao.append(elemento)

difference_1 = set(vetor).difference(set(vetor2))
difference_2 = set(vetor2).difference(set(vetor))

list_difference = list(difference_1.union(difference_2))

print("Soma de x e y:", soma)
print("Produto de x e y: ", multi)
print("Diferenca entre x e y: ", list_difference)
print("Uniao entre x e y: ", uniao)

# 33 - Faça um programa que leia um vetor de 15 posiloes e o compacte, ou seja elimine as posiçoes com valor zero
#para isso todos os elementos a frente do valor zero devem ser movidos para tras do vetor


vetor = []
for i in range(15):
    vetor.append(int(input(f"Digite o valor da posição {i+1}: ")))

i = 0
while i < len(vetor):
    if vetor[i] == 0:
        vetor.pop(i)
    else:
        i += 1

while len(vetor) < 15:
    vetor.append(0)

print("Vetor compactado: ", vetor)

# 34 - Peça ao usuario digitar dez valores números e ordene por ordem creascente esses valores, mostre na tela o valor digitado

vetor = []
for i in range(5):
    vetor.append(int(input(f"Digite o valor da posição {i+1}: ")))
vetor.sort()
print(vetor)

# 35 - Escreva um programa que leia um número inteiro positivo n e em seguida imprima n linhas do comando triangulo de pascal

n = int(input("Digite o número de linhas do Triângulo de Pascal que deseja imprimir: "))

pascal = [[1], [1, 1]]

for i in range(2, n):
    linha = [1]
    for j in range(1, i):
        linha.append(pascal[i-1][j-1] + pascal[i-1][j])
    linha.append(1)
    pascal.append(linha)

for linha in pascal:
    print(linha)

# 36 - Leia uma matriz 4x 4, conte e escreva quantos valroes maiores que 10 ela possui

# Lê a matriz 4x4
matriz = []
for i in range(4):
    linha = []
    for j in range(4):
        valor = int(input(f"Digite o valor da posição ({i},{j}): "))
        linha.append(valor)
    matriz.append(linha)

# Conta quantos valores são maiores que 10
contagem = 0
for linha in matriz:
    for valor in linha:
        if valor > 10:
            contagem += 1

# Escreve o resultado
print(f"A matriz possui {contagem} valores maiores que 10.")

# 37 - Declare uma matriz 5 x 5 Preencha com 1 a diagonal principal e com 0 os demais elementos , escreva ao final a matriz obtida

matriz = [[0 for j in range(5)] for i in range(5)]

for i in range(5):
    matriz[i][i] = 1

for i in range(5):
    for j in range(5):
        print(matriz[i][j], end=" ")
    print()

# 38 - Faça um origrana que preencha uma matriz 4 x 4 com o produto do valor da linha e da coluna de cada elemento, em seguida imprima na tela a matriz

matriz = [[0 for j in range(4)] for i in range(4)]

for i in range(4):
    for j in range(4):
        matriz[i][j] = i * j

for i in range(4):
    for j in range(4):
        print(matriz[i][j], end=" ")
    print()
"""
# 39 - Leia uma matriz 4 x 4  imprima  a matriz e retorne a localização ( linha coluna) do maior valor.

# Lê a matriz de entrada
matriz = []
for i in range(4):
    linha = list(map(int, input().split()))
    matriz.append(linha)

# Imprime a matriz
print("Matriz:")
for linha in matriz:
    print(linha)

# Encontra o maior valor e sua localização
maior_valor = matriz[0][0]
maior_linha = 0
maior_coluna = 0
for i in range(4):
    for j in range(4):
        if matriz[i][j] > maior_valor:
            maior_valor = matriz[i][j]
            maior_linha = i
            maior_coluna = j

# Imprime a localização do maior valor
print(f"O maior valor é {maior_valor} e está na linha {maior_linha} e coluna {maior_coluna}.")
