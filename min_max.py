"""
Min e Max

max() -> Retorna o maior valor em iterável ou o maior de dois ou mais elementos.

# Exemplos
lista = [1, 8, 4, 99, 34, 129]

print(max(lista))  # 129

tupla = (1, 8, 4, 99, 129)
print(max(tupla))  # 129

conjunto = {1, 8, 4, 99, 129}
print(max(conjunto))  # 129

dicinario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 129}
print(max(dicinario))  # f

dicinario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 129}
print(max(dicinario.values()))  # 129

print(max(3, 34))  # 34

va1 = int(input('Digite o valor de x:'))
val2 = int(input('Digite o valor y:'))

print(max(va1, val2))

print(min(4, 67, 54))

print(min('a', 'ab', 'abc'))

print(min('a', 'b', 'c', 'g'))

print(min(3.145, 5.789))

print(min('Geek University'))

# Outros Exemplos

nomes = ['Arya', 'Samson', 'Tim', 'Dora', 'Ollivander']

print(max(nomes))  # Tim

print(min(nomes))  # Arya

print(max(nomes, key=lambda  nome: len(nome)))  # Ollivander

print(min(nomes, key=lambda  nome: len(nome)))  # Tim

"""

musicas = [
    {'titulo': 'Thunderstruck', 'tocou': 3},
    {'titulo': 'Dead Skin Mask', 'tocou': 2},
    {'titulo': 'Back in Black', 'tocou': 4},
    {'titulo': "Too olf to rock'in'rool, too yong to die", 'tocou': 32},
]

print(max(musicas, key=lambda musica: musica['tocou']))
print(min(musicas, key=lambda musica: musica['tocou']))

# Desafio Imprimir somento o nome da musica mais e menos tocou

print(max(musicas, key=lambda musica: musica['tocou'])['titulo'])
print(min(musicas, key=lambda musica: musica['tocou'])['titulo'])

# Desafio como encontrar a musica mais tocada e a menos tocada sem  usar max()  min()  e lambda()

max = 0
for musica in musicas:
    if musica['tocou'] > max:
        max = musica['tocou']

for musica in musicas:
    if musica['tocou'] == max:
        print(musica['titulo'])

min = 9999
for musica in musicas:
    if musica['tocou'] < min:
        min = musica['tocou']

for musica in musicas:
    if musica['tocou'] == min:
        print(musica['titulo'])

