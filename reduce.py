"""
Reduce

OBS: A partir do Python3+ a função reduce() mão é mais uma função integrada (built-in) agora temos que importar
e utilizar  esta função a partir do módulo 'functools'

Guido Van Rossum: Utilize a função reduce() se voce realmnte precisar dela, em todo caso, 99% das vezes um lop for
é mais legivel


Para entender o reduce()
# Imagine que você tem uma coleção de dados:

dados = [a1, a2, a3, .... an]

# e você tem uma função que recebe dois parâmetros:

def funcao(x,y):
    return x * y

Assim como map() e filter(), a reduce(). recebe dois parâmetros: a função eo iteravel

reduce(função, dados)


A função reduce(), funciona da seguinte forma:
    Passo 1-  res1 = f(a1, a2) # aplica a função nos dois primeiros elementos da coleção e guarda os resultados
    Passo 2 - res2 = f(res1, a3) # Aplica a função passando o resultado mais o terceiro elemento, e guarda o res

    Isso é repetido até o final.
    Passo 3: res3 = f(res2, a4)
    -
    -
    -
    Passo n resn = f(resm, an)
Ou seja, em cada passo ela aplica a função passando como primeiro argumento  o resultado da aplicação anterior. no final
reduce() irá retornar o resultado final.

Alternativamente poderiamos ver a função reduce() como :

funcao(funcao(funcao(a1, a2), a3), a4), ....), an)
"""

# Como funciona na prática ?
# Vamos utilizar a funcao reduce() para multiplicar todos os numeros de uma list

from functools import  reduce

dados = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29]

# Para utilizar o reduce() nós precisamos de uma função que receba dois parâmetros
multi = lambda x, y:  x * y

res = reduce(multi,dados)
print(res)

# Utilizando um loop normal

res = 1

for n in dados:
    res = res * n
print(res)