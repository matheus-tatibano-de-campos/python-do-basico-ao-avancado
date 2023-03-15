"""
List comprehension

- Utilizando List Comprehension nós podemos gerar novas listas com dados processados a patir de outro iterável...
# sintaxe da List Comprehension

[ dado for dado in iterável ]


# Exemplos

numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]

print(res)


Para entender melhor o que está acontecendo devemos dividir a expressão em duas partes:

- A primeira parte: for numero in numeros
- A segunda parte: numero * 10




res = [numero / 2 for numero in numeros]
print(res)

def funcao(valor):
    return valor * valor

res = [funcao(numero) for numero in numeros]

print(res)

# List Comprehension versos Lup

# Loop

numeros = [1, 2, 3, 4, 5]
numeros_dobrados = []
for numero in numeros:
    numero_dobrados = numero * 2
    numeros_dobrados.append(numero_dobrados)

print(numeros_dobrados)

# List Comprehension
print([numero * 2 for numero in numeros])

# Outros Exemplos

nome = 'Geek University'

print([letra.upper() for letra in nome])

# Outro exemplos

def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome
amigos = ['maria', 'julia', 'pedro', 'guilherme', 'vanessa']

print([caixa_alta(amigo) for amigo in amigos])

# Exemplo

print([numero * 3 for numero in range(1, 10)])

# Exemplo

print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])

print([str(numero) for numero in [1, 2, 3, 4, 5]])

"""





