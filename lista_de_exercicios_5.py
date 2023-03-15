"""
# 1 - Crie uma função que receba como parâmetro um número inteiro e devolve o seu dobro

def double(number):
    print(number * 2)

print(double(2))


# 2 - Faça uma função que rece a data atual( dia, mes e ano inteiro) e exiba na tela no formato textual por extenso.
#exemplo data 01/01/2000 immprimir 1 de janeiro de 2000

import datetime


def imprimir_data_por_extenso(dia, mes, ano):
    # criar objeto datetime com os parâmetros recebidos
    data = datetime.datetime(ano, mes, dia)

    # obter string da data formatada no padrão desejado
    data_formatada = data.strftime('%d de %B de %Y')

    # exibir a string da data formatada na tela
    print(data_formatada)

imprimir_data_por_extenso(10, 3, 2023)


# 3 - faça uma função para verificar se um número é positivo ou negativo, Sendo que o valor de retorno sera 1 se positivo
# e -1 se negativo e 0 se for 0

def verifica_positivo_negativo(num):
    if num < 0:
        print(-1)
    elif num > 0:
        print(1)
    else:
        print(0)

verifica_positivo_negativo(0)


# 4 faça uma função para verificar se um número é um quadrado perfeito, um quadrado perfeito é um numero inteiro não
#  negativo que pode ser expresso como o quadrado de outro numero inteiro ex 1, 4, 9

import math

def eh_quadrado_perfeito(n):
    raiz = int(math.sqrt(n))
    return raiz**2 == n

print(eh_quadrado_perfeito(9))
print(eh_quadrado_perfeito(10))
print(eh_quadrado_perfeito(16))



# 5 - Faça uma função e um programa de teste para o cálculo do volume de uma esfera, o raio é passado por parametro
v = 4/3 * pi * R**3

def calcula_volume_esfera(raio):
    volume = 4/3 * 3.14 * raio**3
    return volume

print(calcula_volume_esfera(2))

# 6 - Faça uma função que receba 3 números inteiros como parametros,
# representado horas, minutis e segundo e os converta em segundos

def converte_minuto(hora, minuto, segundo):
    hora_convertida = hora * 3600
    minuto_convertido = minuto * 60
    total = hora_convertida + minuto_convertido + segundo
    return total

print(converte_minuto(1, 1, 1))


# 7 - Faça uma função que receba uma temperatura em graus Celsius e retorne-a convertida em graus Fahrenheit.
# formula  é F = c * (9.0/5.0) + 32

def converte_celsius_fahrenheit(celius):
    fahrenheit = celius * (9/5) + 32
    return fahrenheit

print(converte_celsius_fahrenheit(18))

# 8 sejam a e b os catetos de um triângulo, onde a hipotenusa é obtida pela equação:
# hipo = raizquadrada de a**2 + b** faça uma funcao que receba os valores e a e b e calcule  a hipotenusa

import math
def calcula_hipotenusa(a,b):
    hipotenusa = math.sqrt(a**2 + b**2)
    return hipotenusa

print(calcula_hipotenusa(3,4))

# 9 - Faça uma função que receba a altura e o raio de um cilindro circular e retorne o volume do cilindro
# O volume de um cinlindro é v = pi * raio**2 * altura

def calcula_volume_cilindro(raio, altura):
    volume = 3.14 * raio**2 * altura
    return volume

print(calcula_volume_cilindro(3,4))

# 10 - Faça uma função que receba dois números e retorne qual deles é o maior

def retorna_maior(num1, num2):
    if num1 > num2:
        print(f'O {num1} é maior que {num2}')
    else:
        print(f'O {num2} é maior que {num1}')

retorna_maior(8,3)

# 11 - Elabore uma função que receba três notas e uma letra, se for A , calcule a media aritmetica, se for P
# calcule a media ponderada  com pesos 5 3 e 2

def calcula_nota(nota1, nota2, nota3, letra):
    if letra == 'a' or letra == 'A':
        media = (nota1 + nota2 + nota3) / 3
        print(f'A média aritmética é:{media}')
    elif letra == 'p' or letra == 'P':
        media_ponderada = (nota1 * 5 + nota2 * 3 + nota3 * 2) / 10
        print(f'A media ponderada é {media_ponderada}')

calcula_nota(10,8,7,'p')


# 12 - Escreva uma função que receba um número inteiro maior que zero e retorne a soma de todos os seus algarismos, por exemplo
# ao numero 251 correponderá ao valor 8 ( 2 + 5 +1) se for menor q zero encerre o programa

def retorna_soma_algarismos(num):
    if num < 0:
        print('Digite um numero maior que zero')
    elif num > 0:
        numero_str = str(num)
        soma = 0
        for caracter in numero_str:
            algarismo = int(caracter)
            soma += algarismo
        return soma


print(retorna_soma_algarismos(113))

# 13 - Faça uma função que receba dois valores númericos e um simbolo, este simbolo representa a operação a ser efeturada
# se o simbolo for + deve ser feito aficao se for - uma subtração se for / uma divisao se for * uma multiplicacao

def calculadora(num1, num2, simbolo):
    if simbolo == '+':
        return num1 + num2

    elif simbolo == '-':
        return num1 - num2

    elif simbolo == '/':
        return num1 / num2

    else:
        simbolo == '*'
        return num1 + num2


print(calculadora(2, 7, '+'))
print(calculadora(2, 7, '-'))
print(calculadora(2, 7, '/'))
print(calculadora(2, 7, '*'))

# 14 - Faça uma função que receba a distancia em Km e a quantidade de litros de gasolina consumido, calcule o consumo km/l
# e escreva uma emsangem

def calcular_consumo(distancia, litros):
    consumo = distancia / litros
    if consumo < 8:
        print(f'Venda o carro consumo:{consumo:.2f} Km/l')
    elif 8 <= consumo < 12:
        print(f'Econômico:{consumo:.2f } Km/l')
    else:
        print(f'Super econômico {consumo:.2f} Km/l')


calcular_consumo(100, 2)


# 15 Crie um programa que receba três valores (obrigatoriamente maior q zero), representando as medidas do três lados de
#de um triangulo elabore funções para
# (a) determinar se eles lados formam um triangulo
# O comprimento de cada lado de um triangulo é menor do que a soma dos outros dois lados
# (b) Determinar e mostrar o tipo de triangulo caso as medidas formem um triangulo
# chama-se EQUIlátero o triangulo que tem três lados iguais
# denimina-se ISÓSCELES o triangulo que tem o comprimento de dois lados iguais
# ESCALENO se tiver os 3 lados diferentes

def verifica_triangulo(lado1, lado2, lado3):
    if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
        return True
    else:
        return False

def verifica_tipo_triangulo(lado1, lado2, lado3):

    if lado1 == lado2 == lado3:
        return 'EQUILÁTERO'
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        return 'ISÓCELES'
    else:
        return 'ESCALENO'

lado1 = float(input("Digite o primeiro lado do triângulo: "))
lado2 = float(input("Digite o segundo lado do triângulo: "))
lado3 = float(input("Digite o terceiro lado do triângulo: "))

if lado1 > 0 and lado2 > 0 and lado3 > 0:
    if verifica_triangulo(lado1, lado2, lado3):
        print(f"Os lados {lado1}, {lado2} e {lado3} formam um triângulo {verifica_tipo_triangulo(lado1, lado2, lado3)}")
    else:
        print("Os lados informados não formam um triângulo")
else:
    print("Os valores informados devem ser maiores que zero")

# 16 - Faça uma função chamada desenhaLinha ela deve desenhar uma linha na tela usando varios limbolos ex(=====)
# a função recebe por parametro quantos sinais de iguais serão mostrado

def desenha_linha(num):
    linha = ''
    for i in range(num):
        linha += '='
    print(linha)

desenha_linha(5)
desenha_linha(25)


# 17 - Faça uma funcao que receba dois numeros inteiros positivos por parametro e renorne a soma dos numeros

def som_numero(num1, num2 ):
    if num1 < 0 or num2 < 0:
        print('Apenas numeros Positivos')
    else:
        soma = num1 + num2
        return soma
print(som_numero(-2,3))


# 18 - Faça uma função que receba por parametro dois valores x e z e calcule e reotorne o resultado de x elevado a z

def numero_elevado(num1,potencia):
    resultado = num1 ** potencia
    return resultado

print(numero_elevado(2,3))
print(numero_elevado(5,2))


# 19 - Faça uma função que retorne o maior fator primo de um número

def maior_fator_primo(num):
    fator = 2
    while fator * fator <= num:
        if num % fator == 0:
            num /= fator
        else:
            fator += 1
    return int(num)

print(maior_fator_primo(20))
print(maior_fator_primo(49))

# 20 - Faça um algoritmo que receba um numero inteiro n e calcule o seu fatorial

def calcula_fatorial(numero):
    resultado = 1
    for n in range(1, numero + 1):
        resultado *= n

    print(resultado)

calcula_fatorial(5)


# 21 - Escreva uma função para determinar a quantidade de números primos abaixo de N

def conta_primos_abaixo(numero):
    if numero < 2:
        return 0
    primos = [True] * numero
    primos[0] = primos[1] = False
    for i in range(2, int(numero**0.5) + 1):
        if primos[i]:
            for j in range(i*i, numero, i):
                primos[j] = False
    return sum(primos)

print(conta_primos_abaixo(10))


# 22 - Crie uma função que receba como parâmetro um valor inteiro e gere como saida n linhas
#como pontos de exclamação

def gera_linha(num):
    linha = ''
    for i in range(num):
        linha += '!'
        print(linha)

gera_linha(5)
"""
# 23 - escreva uma função que gera um triangulo lateral de altura 2*n -1 e n largura  por exemplo a saida para n =4

def geraTrianguloLateral(n):
    for i in range(n):
        linha = "!" * (i+1)
        print(linha)
    for i in range(n-2, -1, -1):
        linha = "!" * (i+1)
        print(linha)

geraTrianguloLateral(12)
