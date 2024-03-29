"""
Funções com retorno

numeros = [1, 2, 3]

ret_pop = numeros.pop()

print(f'retorno de pop:{ret_pop})
ret_pr = print(numeros)
print(f'retorno de print:{ret_pr})

OBS: Em Python, quando uma função não retorna nenhym valor, o retorno é None.

OBS: Funções Python que retornam valores devem retornar estes valores com a palavra reservada return

OBS: Não precisamos necessariamente uma variável para receber o retorno de uma função. Podemos passar a execução da
função para outras funções

# Vamos refatorar esta função para que ela retorne o valor

def quadrado_de_7():
    return 7*7

# Criamos uma variavel para receber o retorno da função
ret = quadrado_de_7()

print(f'Retorno {ret}')
print(f'Retorno: {quadrado_de_7()}')

# Refatorando a primeira função


def diz_oi():
    return 'Oi '


alguem = 'Pedro!'
print(diz_oi() + alguem)

# OBS Sobre a palavra return
1 - Ela finaliza a função. ou seja ela sai da execução da função
2 - Podemos ter, em uma função diferentes return.
3 - Podemos, em uma função retornar qualquer tipo de dado e até mesmo múltiplos valores;

# Exemplo 1 - Ela finaliza a função. ou seja ela sai da execução da função

def diz_oi():
    print('Estou sendo executado antes do retorno...')
    return 'oi'
    print('Estou sendo executado apos o retorno')


print(diz_oi())

# Exemplo 2 - Podemos ter, em uma função diferentes return.


def nova_funcao():
    variavel = True
    if variavel:
        return 4
    elif variavel is None:
        return  3.2
    return 'b'


print(nova_funcao())


# Exemplo 3 - Podemos, em uma função retornar qualquer tipo de dado e até mesmo múltiplos valores;

def outra_funcao():
    return 2, 3, 4, 5

# num1, num2, num3, num4 = outra_funcao()


print(outra_funcao())
print(type(outra_funcao()))

# Vamos criar uma função para jogar a moeda

from random import  random

def joga_moeda():
    # Gera um número pseudo-randômico entre o e 1
    if random() > 0.5:
        return 'cara'
    return 'coroa'

print(joga_moeda())
"""

# Erros comuns na utilização do retorno, que na verdade nem é erro mas sim codificação desnecessaria

def eh_impar():
    numero = 5
    if numero % 2 != 0:
        return True

    return False

print(eh_impar())







