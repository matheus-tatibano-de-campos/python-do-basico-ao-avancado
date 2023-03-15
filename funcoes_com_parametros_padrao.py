"""
Funçoes com Parametros Padrão (default Parameters)

- Funções onde a passagem de parametro seja opicional;

#Exemplo de funcao onde a passagem de  parametro seja opicional:
print('Geek University')
print()

# Exemplo de funcao onde a passagem de paramatro seja Obrigatoria
def quadrado(numero):
    return numero ** 2


print(quadrado(3))
print(quadrado()) # TypeError

def exponencial(numero=2, potencia=2):
    return numero ** potencia


print(exponencial(2, 3))  # 2 * 2 * 2 = 8
print(exponencial(3, 2))  # 3 * 3 = 9

print(exponencial(3))  # Por padrão eleve ao quadrado
print(exponencial(3, 5))  # Eleva a potencia informada pelo usuario

# OBS
# Se  o usuario passar somente 1 parametro, este sera atribuido ao parametro numero, e sera calculado o quadrado deste número
# se o usuario passar 2 argumentos, o primeiro sera atribuido ao parametro numero, e o segundo ao parametro potencia, entao
# Sera calculada a esta potencia.

print(exponencial())

# Obs: Em funções Python, os parâmetros com valores default (padrão) DEVEM sempre estar ao final da declaração

# Erro!
def teste(num=2, potencia):
    return num ** potencia
# ARRUMANDO
def teste(potencia, num=2):
    return num ** potencia

print(teste(6))

def soma(num1, num2):
    return num1 + num2


print(soma(3, 4))
print(soma(4))  # TypeError
print(soma())  # TypeError

# Exemplo mais complexo

def mostra_informacao(nome='geek', instrutor=False):
    if nome == 'geek' and instrutor:
        return ' Bem vindo instrutor geek'
    elif nome == 'geek':
        return  "Eu pensei que voce era instrutor"
    return f'ola {nome}'

print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao('Ozzy'))
print(mostra_informacao(nome='Stephani'))


# Por quê utilizar parâmetros com valor default ?

- nos permite ser mais flexivies nas funções:
- Evita erros com parâmetros incorretos
- Nos permite trabalhar com exemplos mais legivies de código

# quais tipo de dados podemos utilizar como valores default para parâmetros ?
- Qualquer tipo de dado:
    - Numeros, strings, floats, booleanos, listas, tuplas, dicionaios, funcoes, etc:

    # Exemplo
def soma(num1, num2):
    return num1 + num2

def mat(num1, num2, fun=soma):
    return fun(num1, num2)

def subtracao(num1, num2):
    return  num1 - num2


print(mat(2, 3))
print(mat(2, 2, subtracao))

# Escopo - Evitar problemas e confusões..

# Variaveis globais
# Variaveis locais

instrutor = 'Geek'  # Variavél global

def diz_oi():
    instrutor = 'Python'  # Variavel local
    return f'Oi {instrutor}'

print(diz_oi())

# Obs: Se tivermos uma variavel local com o mesmo nome da variavel global, a local tera preferencia!!


def diz_oi():
    prof = 'Geek' # Variável local
    return f'Olá {prof}'


print(diz_oi())


total = 0

def incrementa():
    total = total + 1  # UnboundLocalError ( A variavel local esta sendo utilizada pra processamento sem ter sido inicializada)
    return total


print(incrementa())

# ATENÇÃO com variaveis globais, ( Se puder evitar, é melhor)
total = 0

def incrementa():
    global total  # Avisando que queremos utilizar a variavel global
    total = total + 1
    return total


print(incrementa())
print(incrementa())
print(incrementa())


"""

# Podemos ter funções que são declaradas dentro de funções, e tambem tem uma forma especial de escopo de variavel


def fora():
    contador = 0

    def dentro():
        nonlocal contador

        contador = contador + 1
        return contador
    return dentro()

print(fora())
print(fora())
print(fora())





