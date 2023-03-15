"""
Entendo o *args

- O *args é um parâmetro, como outro qualquer, Isso significa que voce poderá
chamar  de qualquer coisa , desde que comece com asteristico.

exemplo:

*xis

mas por convenção utilizamos *args para defini-lo

mas o que é o *args ?

O parâmetro * args utilizado em uma função, coloca os valores extras informados como entrada em uma tupla.
entao desde já lembre-se tuplas são imutaveis.

# Exemplos

def soma_todos_numeros(num1, num2, num3=3):
    return num1 + num2 + num3

print(soma_todos_numeros(4, 6, 9))

print(soma_todos_numeros(4, 6))

print(soma_todos_numeros(4, 6, 9, 5))  # TypeError

# Entendendo o args


def soma_todos_numeros(nome, email, *args):
    return sum(args)


print(soma_todos_numeros('Angelia', 'Jolie'))
print(soma_todos_numeros('Angelia', 'Jolie', 1))
print(soma_todos_numeros('Angelia', 'Jolie', 1, 2))
print(soma_todos_numeros('Angelia', 'Jolie', 1, 2, 3))
print(soma_todos_numeros(1, 4, 8, 65))

# Outro exemplo de utilização do *args


def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem vingo Geek'
    return 'Eu não tenho certeza quem você é...'


print(verifica_info())
print(verifica_info(1, True, 'University', 'Geek'))
print(verifica_info(1, 'University', 3.145))
"""


def soma_todos_numeros(*args):
    return sum(args)


print(soma_todos_numeros())
print(soma_todos_numeros(3, 4, 5, 19))

numeros = [1, 2, 4, 5, 6, 7]

# Desempacotador

print(soma_todos_numeros(*numeros))

# OBS: O asteristico serve para que informemos ao Pyhton que estamos
# Passando como argumento uma coleçao de dados. Desta forma ele saberá.
# que precisará desempacotar estes dados, antes da operacao
