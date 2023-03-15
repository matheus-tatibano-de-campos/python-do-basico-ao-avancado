"""
Sorted

OBS: Não confunda, apesar do nome, com a funcão sort() que ja estudamos em Listas. o  sort()
so funciona em listas

Podemos utilizar o sorted() com quaqluer iteravel.

como o própio nome diz, sorted() serve para ordenar.

OBS: o sorted, SEMPRE retorna uma lista com os elementos do iterável ordenados

# Exemplo

numeros = [6, 2, 8, 1]
print(numeros)
print(sorted(numeros))
print(numeros)


numeros = [6, 2, 8, 1]
print(numeros)

# Adicionando parâmetros ao sorted()
print(sorted(numeros, reverse=True)) # Ordena do maior para o menor

# Podemos utilizar  o sorted() para coisas mais complexas

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorro", "Vou sair hoje"]},
    {"username": "gal", "tweets": []},
]

print(usuarios)

# Ordenando por username - ordem Alfabética
print(sorted(usuarios, key=lambda usuario: usuario['username'], reverse=True))

# Ordenando pelo numero de tweets
print(sorted(usuarios, key=lambda usuario: len(usuario['tweets'])))

"""

# Ultimo exemplo

musicas = [
    {'titulo': 'Thunderstruck', 'tocou': 3},
    {'titulo': 'Dead Skin Mask', 'tocou': 2},
    {'titulo': 'Back in Black', 'tocou': 4},
    {'titulo': "Too olf to rock'in'rool, too yong to die", 'tocou': 32},
]

# Ordena da menos tocada para a mais tocada
print(sorted(musicas, key=lambda musica: musica['tocou']))

# Ordena da mais tocada para a menos tocada
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))
