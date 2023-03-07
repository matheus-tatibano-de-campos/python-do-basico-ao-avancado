"""
Modulo Collections Counter (contador)

Collections -> Hight-Performance Container Datetypes

Counter -> Recebe um iteravel como parametro e cria um objeto do tipo collections counter que é parecido
com um dicionario, contendo como chave o elemento da lista passado como parametro e como valor a quantidade
de ocorrencias desse elemento.

# Realizando o import

from collections import Counter

# PODEMOS UTILIZAR QUALQUER ITERAVEL AQUI USAMOS UMA LISTA
lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 5, 3, 45, 66, 66, 43, 34]

# Utilizando o counter
res = Counter(lista)
print(type(res))
print(res)
# Counter({1: 5, 3: 5, 2: 4, 5: 4, 4: 3, 66: 2, 45: 1, 43: 1, 34: 1})

# Veja que, para cada elemento da lista,  o Counter criou uma chave, e deu o valor com a quantidade de ocorrencias

# Exemplo 2

print(Counter('Geek University'))
# Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})
"""
from collections import Counter

# Exemplo 3

texto = """ Alexandre Banza foi um oficial militar tenente-Coronel e político da República Centro-Africana.
 Serviu no exército francês durante a Primeira Guerra da Indochina antes de se juntar às forças armadas da República Centro-Africana.
  Como comandante da base militar Campo Kassaï em 1965, Banza ajudou Jean-Bédel Bokassa a derrubar o governo do presidente David Dacko.
  Bokassa recompensou Banza nomeando-o como ministro de Estado e ministro das Finanças do seu no novo governo. 
  Banza rapidamente estabeleceu a reputação do novo regime no exterior e estabeleceu relações diplomáticas com outros países.
"""

palavras = texto.split()
# print(palavras)

res = Counter(palavras)
print(res)

# Encontrando as 5 palavras com mais ocorrencia no texto
print(res.most_common(5))
