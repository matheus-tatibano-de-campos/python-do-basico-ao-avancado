"""
tuplas (tuple)

Tuplas são basntate parecidas com listas

Existem basicamente duas diferenças ba´sicas:

1 - As tuplas são representadas por parenteses ()

2 - As tuplas são imutaveis : Isso significa que ao se criar uma Tupla ela nao muda.
 Toda alteração gera uma nova tupla

# CUIDADO 1: As tuplas são representadas por () . mas veja:

tupla1 = (1, 2, 3, 4, 5, 6)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)
print(type(tupla2))

# CUIDADO 2: Tuplas com 1 elemento

tupla3 = (4) # Isso não é uma tupla!
print(tupla3)
print(type(tupla3))

tupla4 = (4,) # isso é uma tupla
print(tupla4)
print(type(tupla4))

tupla5 = 5,
print(tupla5)
print(type(tupla5))
# CONCLUSÃO: Podemos definir que tuplas são definidas pela virgula e não pelo uso de parênteses
(4) -> não é tupla
4, -> é tupla
(4,) -> è tupla

# Podemos gerar uma tupla dinamicamente com range(inicio,fim,passo)
tupla = tuple(range(11))
print(tupla)
print(type(tupla))

# Desempacotamente de tupla
tupla = ('Geek University', 'Programção em Python: Essencial')

escola, curso = tupla
print(escola)
print(curso)
# OBS: gera (ValueError) se colocarmos um numero diferente de elementos para desempacotar.
# Métodos oara adição e remoção de elementos nas tuplas não existem, dado o fato das tuplas serem imutaveis.

# Soma*, Valor Mãximo*, Valor Mínimo* e Tamanho
# * Se os valores forem todos inteiros ou reais

tupla = (1, 2, 3, 4, 5, 6, 'b')
print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

# Concatenação de tuplas
tupla1 = (1, 2, 3)
print(tupla1)
tupla2 = (4, 5, 6)
print(tupla2)

print(tupla1 + tupla2) # Tuplas são imutáveis
print(tupla1)
print(tupla2)
tupla3 = tupla1 + tupla2
print(tupla3)
print(tupla1)
print(tupla2)

tupla1 = tupla = tupla2 # tuplas são imutaveis, mas podemso sobreescrever seu valor
print(tupla1)

# Verificar se determinado elemento esta contido na tupla
tupla = (1, 2, 3)
print(3 in tupla)

# Iterando sobre uma tupla
tupla = (1, 2, 3)
for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)

# Contando elementos dentro de uma tupla

tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')
print(tupla.count('c'))

escola = tuple('Geek University')
print(escola)
print(escola.count('e'))

# Dicas na utilização de tuplas

# Devemos utilizar tuplas SEMPRE que não precisarmos modificar os dados contidos em uma coleção

# Exemplo 1
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

# O Acesso a elementos de uma tupla também é semelhante a de uma lista

print(meses[5])

# Iterar com while
i = 0

while i < len(meses):
    print(meses[i])
    i = i + 1
# Verificamos em qual elemento está na tupla
print(meses.index('Junho'))

# OBS: caso o elemento nao exista, será gerado ValueError.

# Slicing

# Tupla[inicio:fim:passo]
print(meses[5:9])

# Por quê utilizar tuplas?
# - Tuplas são mais rapidas que listas.
# - Tuplas deixam seu código mais seguro.

# Copiando uma tupla para outra

tupla = (1, 2, 3)
print(tupla)

nova = tupla # Na tupla nao temos o problema de shallow Copy
print(nova)
print(tupla)

outra = (4, 5, 6)

nova = nova + outra
print(nova)
print(tupla)
"""






