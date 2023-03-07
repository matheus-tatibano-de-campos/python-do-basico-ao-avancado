"""
Listas

Listas em Python funinal como vetores/matrizes (arrays) em outras linguagens, com a diferença
de serem DINÂMICO e podermos colocar QUALQUER tipo de dado.

Linguagens C/Java: Arrays
    -Possuem tamanho e tipo de dado fixo:
    ou seja, nestas linguagens se voce criar um array do tipo int e com tamanho 5, este array
     será SEMPRE do tipo inteiro e podera ter SEMPRE no máximo 5 valores.

Já em python:

- Dinâmico: Não possuem tamanho fixo:  ou seja, podemos criar a lista e simplemente ir adicionando elementos;
- Qualquer tipo de dado: Não possuem tipo de dado fixo ou seja, podemos colocar qualquer tipo de dado

As listas em Python são representadas por colchetes: []

lista1 = [1, 99, 4, 22, 15, 44, 42, 27]

lista2 = ['g', 'e', 'e', 'k', '', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

print(lista5)
# Podemos facilmente checar se determinado valor está contido na lista
num = 7
if 8 in lista4:
    print('encontrei o numero', {num})
else:
    print("Não encontrei o numero", {num})

# podemos facilmente ordenar umas lista
lista1.sort()
print(lista1)

# Podemos facilmente contar o número de ocorrencias de um valor em uma lista
print(lista1.count(1))
print(lista5.count('e'))

# Adicionan elementos em listas, utilizamos a função append

Para adicionar elementos em listas, utilizamos a função append



print(lista1)
lista1.append(42)
print(lista1)

#OBS: Com append, nós so conseguimos adicionar 1 elemento por vez
#  lista1.append(32, 23, 56) # ERRO

lista1.append([8, 3, 1]) # coloca a lista como elemento único (sublista)
print(lista1)

if [8, 3, 1] in lista1:
    print("Encontrei a lista")
else:
    print("Não encontrei a lista")
lista1.extend([123, 44, 67]) # Coloca cada elemento da lista como valor adicional a lista
print(lista1)

# Podemos inserir um novo elemento na lista informando a posição do indice
# OBS: Isso não substitui o valor inicial. O esmo será deslocado para a direita da lista.
lista1.insert(2, 'Novo valor')
print(lista1)

# Podemos facilmente juntar duas listas

lista6 = lista1 + lista2
# lista1.extend(lista2) outro metodo de chegar no mesmo resultado
print(lista6)

# Podemos facilmente inverter uma lista
lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)
# ou utilizando o slice
print(lista1[::-1])
print(lista2[::-1])

# Podemos contar quantos elementos existem dentro da lista
print(len(lista1))

# Podemos remover facilmente o ultimo elemento de uma lista
# OBS: o pop não apenas remove o ultimo elemento , como tambem o retorna
print(lista5)
lista5.pop()
print(lista5)

# Podemos remover um elemento pelo indice
# OBS: os elementos a direita desse indice seraão deslocados para a esquerda.
# OBS: se nao houver elemento no indice informado teremos o erro Index error.
lista5.pop(2)
print(lista5)

# Podemos remover todos os elementos, (zerar a lista)
print(lista5)
lista5.clear()
print(lista5)

# Podemos facilmente repetir elementos em uma lista
nova = [1, 2, 3]
print(nova)
nova = nova*3
print(nova)

# Podemos facilmente converter uma string para uma lista

# Exemplo 1
curso = 'programção em python: Essencial'
print(curso)
curso = curso.split()
print(curso)

# OBS: por padrão, o split separa os elemento da lista pelo espaço entre eleas.

# Exemplo 2
curso = 'Programaçao,em,Python:,Essencial'
print(curso)
curso = curso.split(',')
print(curso)

lista6 = ['Programaçao', 'em' ,'Python:', 'Essencial']
print(lista6)

# Abaixo estamos falando: Pega a lista6, coloca espaço entre cada elemento e transforma em uma string
curso = ' '.join(lista6)
print(curso)

# Abaixo estamos falando: Pega a lista6, coloca um cifrão entre cada elemento e trasforma em uma string
curso = '$'.join(lista6)
print(curso)

# Podemso realmente colocar qualquer tipo de dado em uma lista, inclusive misturando esses dados
lista6 = [1, 2.34, True, 'geek', 'G', [1, 2, 3], 12323123]
print(lista6)
print(type(lista6))

# Iterando sobe listas

# exemplo I
for elemento in lista2:
    print(elemento)


# Exemplo 2 - Utilizando while

carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair:")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)
for produto in carrinho:
    print(produto)


# Utilizando variaveis em listas
numeros = [1, 2, 3, 4, 5]
print(numeros)
num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)

# Fazemos acesso aos elementos de forma indexada

cores = ['verde', 'amarelo', 'azul', 'branco']

print(cores[0]) # verde
print(cores[1]) # amarelo
print(cores[2]) # azul
print(cores[3]) # branco

# Fazer acesso aos elementos de forma indexada inversa
# OBS: Para enenter melhor o indice negativo, pense na lista como um círculo, onde
# o final do elemento está ligado ao inicio da lista
print(cores[-1]) # branco
print(cores[-2]) # azul
print(cores[-3]) # amarelo
print(cores[-4]) # verde

cores = ['verde', 'amarelo', 'azul', 'branco']

for cor in cores:
    print(cor)
indice = 0
while indice <len (cores):
    print(cores[indice])
    indice = indice + 1

# Gerar indice em um for
for indice, cor in enumerate(cores):
    print(indice, cor)

# Listas aceitam valores repetidos
lista = []
lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)
lista.append(42)
print(lista)

# outros metodos nao tao importante mas tambem uteis
# Encontrar o indice de um elemento na lista

numeros = [5, 6, 7, 8, 9, 10]

# Em qual indice está o valor 6 ?
print(numeros.index(6))

# Em qual indice da lista esta o valor 9?
print(numeros.index(9))

# OBS: Caso não tenha este elemento na lista, será apresentado erro ValueError

# OBS: Retorna o indice do primeiro elemento encontrado
print(numeros.index(5))

# Podemos fazer busca dentro de um range, ou seja qual indice começar a buscar
print(numeros.index(5, 1)) # buscando a partir do indice 1
print(numeros.index(5, 2)) # buscando a partir do indice 2
print(numeros.index(5, 3)) # buscando a partir do indice 3
#print(numeros.index(5, 4)) # buscando a partir do indice 4
# OBS: Caso não tenha este elemento na lista, será apresentado erro ValueError

# Podemos fazer busca dentro de um range, inicio/fim
print(numeros.index(8, 3, 6)) # Buscar o indice do valor 8, entre os indices 3 e 6

# Revisão slicing

# lista[inicio:fim:passo]
# range(inicio:fim:passo)

# Trabalhando com slice de lista com o parâmetro 'inicio'

lista = [1, 2, 3, 4]
print(lista[1:])  # Iiniciando no indice 1 e pegando todos os elementos restantes

# Trabalhando com slice de lista com o parâmetro 'fim'
print(lista[:2])  # começa em 0 pega até o indice 2 - 1

print(lista[:4])  # começa em 0, pega até o indice 4 - 1

print(lista[1:3])  # comeca em 1, pega ate  o indice 3 - 1

# Trabalhando com slice de lista com o parâmetro 'passo'

print(lista[1::2])  # Comeca em 1, e vai ate  o final de 2 em 2

print(lista[::2])  # Começa em 0, vai ate o final, de 2 em 2

 # invertendo valores em uma lista

nomes = ['geek', 'university']

nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)

nomes = ['geek', 'university']

nomes.reverse()
print(nomes)

# Soma *, valor maximo, valor minimo, tamanho
# * Se os valores forem todos inteiros ou reais

lista = [1, 2, 3, 4, 5, 6]
print(sum(lista)) # soma
print(max(lista)) # maximo valor
print(min(lista)) # minimo valor
print(len(lista)) # tamanho da lista

# Transformar uma lista em tupla
lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))


# Desempacotamento de listas
lista = [1, 2, 3]
num1, num2,  num3 = lista
print(num1)
print(num2)
print(num3)

# OBS: Se tivermos um número diferente de elementos na lista, ou varáveis para receber os dados, teremos ValueError


# Copiando uma lista para outra (shallow Copy e Deep Copy)

# Forma 1 Deep Copy

lista = [1, 2, 3]
print(lista)

nova = lista.copy()

print(nova)

nova.append(4)

print(lista)
print(nova)

# Ao utilizarmos lista.copy() copiamos os dados da lista para uma nova lista, mas elas
# ficaram totalmente independetes, ou seja modificando uma lista, nao afeta a outra
# em Python isso é chamado de Deep Copy ( ou copia profunda)
"""
# Forma 2 shallow Copy
lista = [1, 2, 3]
print(lista)

nova = lista

print(nova)

nova.append(4)
print(lista)
print(nova)

# Veja que utilizamos a cópia via atribuição e copiamos os dados da lista para a nova lista, mas
# Após realizar modificação em uma das listas essa modificação se refletiu em ambas as listas
# Issso em Python é chamado de shallow Copy