"""
Loop for

Loop é uma estrutura de repetição.
For -> Uma dessas estruturas

C ou Java

for (int i = 0; i < limitador; i ++) {
    execução do loop
    }

Python
for item in interavel:
    execução do loop

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis

Exemplos de iteráveis:
- String
    nome = 'geek University'
- Lista
    lista = [1, 2, 3, 4, 5,]
- Range
   numeros = range(1,10)
"""
nome = 'Geek University'
lista = [1, 2, 3, 4, 5]
numeros = range(1,10) #temos que transformar em uma lista
"""

# Exemplo de for 1 (Iterando sobre uma String)
for letra in nome:
    print(letra)

# Exemplo de for 2 (Iterando sobre uma lista)
for numero in lista:
    print(numero)

# Exemplo de for 3 (Iterando sobre um range)
for numero in range(1, 10):
    print(numero)

# Exemplo de ENUMERATE:

for indice, letra in enumerate(nome):
    print(nome[indice])

for indice, letra in enumerate(nome):
    print(letra)

for _, letra in enumerate(nome):
    print(letra)
    
OBS: quando nao precisamos de um valor, podemos descarta-lo utilizando um underline (_)

qtd =  int(input("Qauntas vezes sse loop vai rodar?))
soma = 0

for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor:'))
    soma = soma + num
print(f"a soma é {soma}')

nome = 'geek university'
for letra in nome:
    print(letra, end='') # nao pula a linha, esta setando o final das letras para um espaço em branco
"""



