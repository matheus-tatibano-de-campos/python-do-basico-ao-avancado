"""
Conjuntos

- Conjuntos em qualquer linguagem de programação, estamos fazendo referencia a teoria dos conjuntos
da matematica.
- aqui no Python, os conjuntos são chamados de Sets.

Dito isto, da mesma forma que na matematica:
- Sets (conjuntos) não possuem valores duplicados
- Sets (conjuntos) não possuem valores ordenados
- Elementos nao são acessados via indice, ou seja conjuntos não são indexados.

Conjuntos são bons para se utilizar quando precisamos armazenar elementos
mas não nos importamos com a ordenação deles. Quando não precisamos se preocupar
com . chave, valores e itens duplicados.

Os conjuntos (sets) são referenciados em Python com chaves {}

Diferença entre Conjuntos  (Set) e Mapas ( Dicionarios ) em Python:
        - um  dicionario tem chave/valor
        - um conjunto tem apenas valor;
        # Definindo um conjunto:

# Forma 1

s = set({1, 2, 3, 4, 5, 6, 7, 2, 3}) # repare que temos valores repetidos

print(s)
print(type(s))

# OBS: Ao criar um conjunto, caso seja adicionado um valor ja existente
#  o mesmo sera IGNORADO e não fara parte do junto e nao gera erro

# Forma 2  Mais comum

s = {1, 2, 3, 4, 5, 5}
print(s)
print(type(s))

# Podemos verificar se determinado elemento está contido no conjunto

if 3 in s:
    print('Tem o 3')

else:
    print('Não tem o 3')

# Importante lembrar que, além de não termos valores duplicados, não temos ordem

# Listas aceitam valores duplicados, então temos 10 elementos

lista = [99, 2, 34, 23, 2, 1, 14, 56, 5, 34]
print(f'lista: {lista} COM {len(lista)} elementos')

# Tuplas aceitam valores duplicados, então temos 10 elementos
tupla = (99, 2, 34, 23, 2, 1, 14, 56, 5, 34)
print(f'lista: {tupla} COM {len(tupla)} elementos')

# Dicionarios não aceitam chaves dupliacadas, então temos 8 elementos
dicionario = {}.fromkeys([99, 2, 34, 23, 2, 1, 14, 56, 5, 34], 'dict')
print(f'Dicionario: {dicionario} COM {len(dicionario)} elementos')

# Conjuntos não aceitam valores duplicados, então temos 8 elementos
conjunto = {99, 2, 34, 23, 2, 1, 14, 56, 5, 34}
print(f'Conjunto: {conjunto} COM {len(conjunto)} elementos')

# Assim como todo outro conjunto Pyhton Podemos colocar tipos de dados misturados em Set

s = {1.,  'b',  True, 34.23, 44}
print(s)
print(type(s))

# Podemos interar sobre um Set normalmente
for valor in s:
    print(valor)

# Usos interessantes com Set

# Imagine que fizemos um formulario de cadastro de visitantes em uma feira ou museu. E os visitantes
# Informam manualmente as cidade de onde vieram.

# nós adicionamos cada cidade em uma lista python.
# já que em uma lista podemos adicionar novos elementos e ter repetição

cidades = ['Belo horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'São Paulo', 'Cuiaba']

print(cidades)
print(len(cidades))

# Agora precisamos saber quantas ciades distintas , ou seja cidades unicas temos.
# o que voce faria ? Faria um loop na lista ?

# Podemos utilizar o set para isso:
print(len(set(cidades)))

s = {1, 2, 3}

s.add(4)
s.add(4) # Duplicidade não gera erro, simplesmente  é ignorado e não é adicionado
print(s)

# Adicionando elementos em um conjunto

s = {1, 2, 3}
print(s)

# Forma 1
s.remove(3) # NÃO é indice !! informamos o valor a ser removido
print(s)

# OBS: Caso o valor não seja encontrado gera o  KeyError. Nenhum valor é retornado

# Forma 2

s.discard(22)

print(s)
# OBS: Se o valor não for encontrado, nenhum erro é gerado.

# Copiando um conjunto para outro..

# Forma 1 Deep Copy
novo = s.copy()
print(novo)

novo.add(4)
print(novo)
print(s)

# Forma 2 Shallow copy

novo = s
novo.add(4)
print(novo)
print(s)

s = {1, 2, 3}
print(s)

# Podemos remover todos os itens de um conjunto

s.clear()
print(s)


estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# Precisamos gerar um conjunto com nomes de estudantes unicos

# forma 1 Utilizando union

unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)

# Forma 2 - Utilizando o caractere pipe |
unicos2 = estudantes_python | estudantes_java
print(unicos2)

# Vejam que alguns alunos estudam python e java

# gerar um conjunto de estudantes que estão em ambos os cursos

# forma 1 Utilizando intersectioon
ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

#  Forma 2 utilizando o &

ambos2 = estudantes_python & estudantes_java
print(ambos2)

# Metodos matematicos de conjuntos

# Imagine que temos dois conjuntos : Um contendo estudantes de Python e oum
# Contendo estudantes de java

# Gerar um conjunto de estudantes que não estão no outro curso

so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)

"""

# soma*, valor Maximo*, Valor Minimo*, Tamanho
# * se os valores forem todos inteiros ou iguais

s = {1, 2, 3, 4, 5, 6}
print(sum(s))
print(max(s))
print(min(s))
print(len(s))

