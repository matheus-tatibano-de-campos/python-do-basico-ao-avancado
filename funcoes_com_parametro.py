"""
Funções com Parâmetro (de entrada)

- Funções que recebem dados para serem processados dentro da mesma;

Se a gente pensar em um programa qualquer, geralmente temos:
entrada -> processamento -> Saida

Se a gente pensar em uma função, ja sabemos que temos funções que:
- Não possuem entrada;
- Não possuem saída;
- Possuem entrada mas não possuem saída;
- Não possuem entrada mas possuem saída;
- Possuem entrada e sáida;

# Refatorando uma função


def quadrado(numero):
    return numero ** 2


print(quadrado(5))
print(quadrado(2))
print(quadrado(3))

print(quadrado()) # TypeError faltando argumento

# Refatorando a função


def cantar_parabens(aniversariante):
    print('Parabens pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print(f'Viva o {aniversariante}')

cantar_parabens('Fozao')


# Funções pode ter n parâmetros de entrada. Ou seja podemos receber como entrada
# em uma função quantos parametros forem necessários. Eles são separados por vírgula

# Exemplo


def soma(a,b):
    return a + b


def multiplicação(num1, num2):
    return num1 * num2


def outra(num1, b, msg):
    return (num1 + b) * msg


print(soma(2, 5))
print(soma(10, 20))

print(multiplicação(3, 7))
print(multiplicação(2, 8))

print(outra(1, 2, 'Geek '))
print(outra(5, 4, 'Python '))

# Nomeando parâmetros


def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'


print(nome_completo('Angelina', 'Jolie'))

# A diferença entre Parâmetro e Argumentos

# Parametros são variaeis declaradas na definicao de uma funcao
# Argumentos são dados passados durante a execucao de uma funcao

# A oprdem os parametros importa!

nome = 'Felicity'
sobrenome = 'Jones'
print(nome_completo(sobrenome, nome))

# Argumentos nomeados (keyword Arguments)

# Caso utilizemos nomes dos parâmetros nos argumentos para informa-los, podemos
# Utilizar qualquer ordem.

print(nome_completo(nome= 'Angelina', sobrenome='jolie'))
print(nome_completo(nome=nome, sobrenome=sobrenome))
print(nome_completo(sobrenome='Marques', nome='Marcia'))
"""
# Erro comum na utilização do return

def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total


lista = [1, 2, 3, 4, 5, 6, 7]
print(soma_impares(lista))

tupla = (1, 2, 3, 4, 5, 6, 7)
print(soma_impares(tupla))