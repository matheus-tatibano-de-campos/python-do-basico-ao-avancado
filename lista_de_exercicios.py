"""
# 1- Faça um programa que leia um número inteiro e o imprima
num = int(input("Digite um numero:"))
print("O número digitado foi:", num)

# 2- Faça um programa que leia um número real e o imprima
num = float(input("Digite um numero decimal:"))
print("O número digitado foi:", num)


# 3 - Peça ao usuário para digitar três valores inteiros e imprima a soma deles
numero1 = int(input("Digite um valor inteiro:"))
numero2 = int(input("Digite outro valor inteiro:"))
numero3 = int(input("Digite outro valor inteiro:"))
resultado = numero1 + numero2 + numero3
print("A soma dos três numeros digitados é", resultado)


# 4 - Leia um número real e imprima a o resultado do quadrado desse número
num = float(input("Digite um numero decimal:"))
num_ao_quadrado = num **2
print("O numero digitado elevado ao quadrado é:", num_ao_quadrado)


# 5 - Leia um número real e imprima a quinta parte deste número.
num = float(input("Digite um numero decimal:"))
resultado = num / 5
print("A quinta parte do número digitado é:", resultado)

# 6 - Leia uma temperatura em graus Celsius e apresente-a  convertida em graus Fahrenheit
celsius = float(input("Digite a  temperatura em Celsius:"))
fahrenheit = celsius *(9/5)+32
print("A temperatura em Fahrenheit é:", fahrenheit)

# 7 - Leia uma temperatura em graus Fahrenheit e apresente-a  convertida em graus Celsius
fahrenheit = float(input("Digite a  temperatura em Fahrenheit:"))
celsius =  5*(fahrenheit - 32)/9
print("A temperatura em Celsius é:", celsius)

# 8 - Leia uma temperatura em graus Kelvin e apresente-a  convertida em graus Celsius
kelvin = float(input("Digite a  temperatura em Kelvin:"))
celsius = kelvin - 273.15
print("A temperatura em Celsius é:", celsius)

# 9 - Leia uma temperatura em graus Celsius e apresente-a  convertida em graus Kelvin
celsius = float(input("Digite a  temperatura em Celsius:"))
kelvin = celsius + 273.15
print("A temperatura em Kelvin é:", kelvin)

# 10 - Leia uma velocidade em Km/h e apresente-a convertida em m/s
kmh = float(input("Digite a velocidade em Km/h:"))
ms = kmh / 3.6
print("A velocidade em metros por segundo é de:", ms)

# 11- Leia uma velocidade em mt/s e apresente-a convertida em Km/h
ms = float(input("Digite a velocidade em mt/s:"))
kmh = ms * 3.6
print("A velocidade em metros por segundo é de:", kmh)

# 12 - Leia uma distancia em milhas e apresente-a convertida em quilometros
milhas = float(input("Digite a disância em milhas:"))
km = float(milhas * 1.61)
print("A distância em quilômetros é de:", km)

# 13- Leia uma distancia em quilômetros e a converta em milhas
km = float(input("Digite a disância em quilômetros:"))
milhas = float(km / 1.61)
print("A distância em Milhas é de:", milhas)

# 14 - Leia um ângulo em graus e apresente-o convertido em radianos
graus = float(input("Digite o ângulo em graus:"))
radianos = graus * (3.14/180)
print("O grau em radianos é:", radianos)

# 15 - Leia um ângulo em radianos e apresente-o convertido em graus
radianos = float(input("Digite o ângulo em radianos:"))
graus = radianos * (180/3.14)
print("O angulo  em graus  é:", graus)

# 16 - Leia um valor de comprimento em polegadas e apresente-o convertido em centimentros
polegadas = float(input("Digite o comprimento em polegadas:"))
centimentros = polegadas * 2.54
print("O comprimento em centimetros é de:", centimentros)

# 17 - Leia um valor de comprimento em centimentros e apresente-o convertido em polegadas
centimentros = float(input("Digite o comprimento em centimentros:"))
polegadas = centimentros / 2.54
print("O comprimento em polegadas é de:", polegadas)

# 18 -Leia um valor de volume em metros cúbicos m3 e apresente-o em litros
mt3= float(input("digite o volume em metros cúbicos:"))
litros = mt3* 1000
print("O volume em litros é de:", litros)

# 19 -Leia um valor de volume em litros  e apresente-o em metros cúbicos m3
litros= float(input("digite o volume em litros:"))
mt3 = litros / 1000
print("O volume em metros cúbicos  é de:", mt3)

# 20 - Leia um valor em massa em quilogramas e apresente-o convertido em libras
quilogramas = float(input("Digite a massa em quilogramas:"))
libras = quilogramas * 2.205
print("A massa em libras é de:", libras )

# 21 - Leia um valor em massa em libras e apresente-o convertido em quilogramas
libras = float(input("Digite a massa em libras:"))
quilogramas = libras / 2.205
print("A massa em quilogramas é de:", quilogramas)

# 22 - Leia um valor de comprimento em jardas e apresente-o convertido em metros
jardas = float(input("Digite o comprimento em jardas:"))
metros =  0.91 * jardas
print("O comprimento convertido para metros é de:", metros)

# 23 - Leia um valor de comprimento em metros e apresente-o convertido em jardas
metros = float(input("Digite o comprimento em metros:"))
jardas = metros / 0.91
print("O comprimento convertido para jardas é de:", jardas)

# 24 - Leia um valor de área em metros quadrados m2 e apresente-o convertido acres
m2 = float(input("Digite a área em metros quadrados:"))
acres = m2 * 0.000247
print("A área em acres corresponde a:", acres)

# 25 - Leia um valor de área em acres  e apresente-o convertido metros quadrados m2
acres = float(input("Digite a área em  acres:"))
m2 = acres * 4048.58
print("A área em m2 corresponde a:", m2)

# 26 - Leia um valor de área em metros quadrados e apresente-o convertido em hectares
m2 = float(input("Digite a area em metros quadrados:"))
hectares = m2 * 0.0001
print("A área em hectares é de:", hectares)

# 27 - Leia um valor de área em hectares e apresente-o convertido em metros quadrados
hectares = float(input("Digite a area em hectares:"))
m2 = hectares * 10000
print("A área em m2 é de:", m2)

# 28 - Faça a leitura de três valores e apresente como resultado a soma dos quadrados dos três  numeros lidos
num1 = float(input("Digite o primeiro numero:"))
num2 = float(input("Digite o segundo numero:"))
num3 = float(input("Digite o terceiro numero:"))
num1_ao_quadrado = num1 ** 2
num2_ao_quadrado = num2 ** 2
num3_ao_quadrado = num3 ** 2
resultado = num1_ao_quadrado + num2_ao_quadrado + num3_ao_quadrado
print("A soma do quadrado dos 3 valores é de:", resultado)

# 29 - Leia quatro notas, calcule a média aritmética e imprima o resultado
nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))
nota3 = float(input("Digite a terceira nota:"))
nota4 = float(input("Digite a quarta nota:"))
media = (nota1 + nota2 + nota3 + nota4) / 4
print("A média aritmética é de:", media)

# 30- Leia um valor real e a cotação do dólar, em seguida, imprima o valor correspondente em dolar
valor1 = float(input("Digite o valor em real:"))
dolar_hoje = float(input("Digite a cotação do dolar hoje:"))
valor_em_dolar = valor1 * dolar_hoje
print("O valor em dolar hoje é de:", valor_em_dolar)

# 31 - Leia um numero inteiro e imprima o seu antecessor e o seu sucessor.
num1 = int(input("Digite um numero inteiro:"))
antecessor = int(num1 - 1)
sucessor = int(num1 + 1)
print("O numero antecessor  ao numero digitado o numero digitado e seu sucessor sao respectivamente ", antecessor, num1, sucessor)

# 32 - Leia um numero inteiro e imprima a soma do sucessor de seu triplo com o antecessor de seu dobro
num1 = int(input("Digite um numero inteiro:"))
triplo_mais_um = (num1 * 3) + 1
dobro_menos_um = (num1 * 2) - 1
soma = triplo_mais_um + dobro_menos_um
print("A soma  do sucessor do seu triplo com o antecessor do seu dobro é:", soma)

# 33 - Leia o tamanho do lado de um quadrado e imprima como resultado sua área
lado = float(input("Digite o tamanho do lado do quadrado:"))
area = lado ** 2
print("A área do quadrado é:", area)

# 34 - Leia o valor do raio de um círculo e calcule e iprima a área do círculo correspondente
raio = float(input("Digite o valor do raio:"))
area = 3.14 * (raio**2)
print("A area do círculo é de:", area)

# 35- Faça um programa que receba os valores de A e Be calculo o valor da hipotenusa
import math
a = float(input("Digite o valor de A:"))
b = float(input("Digite o valor de B:"))
a_ao_quadrado = a**2
b_ao_quadrado = b**2
hipotenusa = math.pow(a_ao_quadrado + b_ao_quadrado, 1/2)
print("A hipotenusa de A e B é:", hipotenusa)

# 36 - Leia a altura e o raio de um cilindro circular e imprima o volume do cilindro
altura = float(input("Digite a altura do cilindro:"))
raio = float(input("Digite o raio do cilindro:"))
volume = ((3.14 * raio**2) * altura)
print("O volume do cilindro é de:", volume)

# 37 - faça um programa que leia o valor de um produto e imprima o valor com desconto, tendo em vista o desconto foi de 12%
valor = float(input("Digite o valor do produto:"))
desconto = 12 / 100
valor_com_desconto = valor - (desconto * valor)
print("O valor do produto com desconto é:", valor_com_desconto)

# 38 - Leia o salário de um funcionário e calcule e imprima o valor do salario novo, com aumento de 25%
salario = float(input("Digite o salario:"))
aumento = 25 / 100
novo_salario = salario + (salario * aumento)
print("O salário com aumento é:", novo_salario)

# 39 - A importancia de 780.000,00 será dividida entre 3 ganhadores, 1# 46% do total, 2# 32%, o terceiro fica com o resto
premio = 780_000_00
porcentagem1 = 46 / 100
porcentagem2 = 32 / 100
ganhador1 = porcentagem1 * premio
sobra_premio = premio - ganhador1
ganhador2 = porcentagem2 * premio
ganhador3 = premio - ganhador1 - ganhador2
print(f"o ganhador 1 levou {ganhador1}, o ganhador2 levou {ganhador2}, o ganhador 3 levou {ganhador3}")

# 40 - Faça um programa que solicite o número de dias trabalhados pelo encanador e imprima o valor a ser pago com desconto de 8%
dias = int(input("Digite a quantidade de dias a ser trabalhados:"))
valor = float(dias * 30.00)
desconto = 8/100
valor_com_desconto = desconto * valor
valor_final = valor - valor_com_desconto
print("O valor liquido a ser pago é de:", valor_final)

# 41 - faça um programa que leia o valor da hora de trabalho e numero de horas trabalhadas no mês, imprima o valor adicionando 10% sobre o valor
valor_hora = float(input("Digite o valor da  sua hora de trabalho:"))
quantidade_de_horas = float(input("Digite a quantidade de horas de trabalho durante o mês:"))
salario_base = valor_hora * quantidade_de_horas
bonus = 10/100
calculo_bonus_salario = salario_base * bonus
salario_final = salario_base + calculo_bonus_salario
print("O salario com bonus é de:", {salario_final})

# 42 - Receba o salário de um funcionario, calcule e imprima o salario com 5% de bonus, e tirando 7% de imposto do salario base
salario = float(input("Digite o salario base do funcionario:"))
taxa_imposto = 7/100
taxa_bonus = 5/100
salario_bonus = salario * taxa_bonus
salario_com_bonus = salario + salario_bonus
salario_imposto = salario * taxa_imposto
salario_com_imposto = salario - salario_imposto
salario_final = salario_com_bonus - salario_imposto
print("O salario final é de:", salario_final)

# 43 - Escreva um programa que ajuda para vendedores total com desconto 10% valor de cada parcela em 3x sem juros, comissao 5%
valor_da_compra = float(input("Digite o valor da compra:"))
desconto_a_vista = 10/100
comissão = 5/100
compra_a_vista = valor_da_compra * desconto_a_vista
valor_da_compra_a_vista = valor_da_compra - compra_a_vista
calculo_comissao = valor_da_compra_a_vista * comissão
calculo_parcelado = float(valor_da_compra / 3)
calculo_comissao_parcelado = valor_da_compra * comissão
print("O valor da compra a vista é de:",{valor_da_compra_a_vista}, "o valor de cada parcela fica em:", {calculo_parcelado}, "e a comissão a vista é de:", {calculo_comissao}, "o valor da comissão parcelado é de:",{calculo_comissao_parcelado})

# 44 - Receba a altura do degrau de uma escada , e a altura que o usuario deseja alcançar, e calcule a quantidade de degraus
alt_degrau = float(input("Digite a altura de cada degrau:"))
altura_desejada = float(input("Digite a distancia que deseja alcançar:"))
qnt_degraus = altura_desejada / alt_degrau
print("Para chegar na altura de", {altura_desejada}, "você ira precisar de ", {qnt_degraus}, "degraus")

# 45 -Faça um programa para converter uma letra maiúscula em minúscula
letra = input("Digite uma letra:")
letra_maiscula = letra.upper()
print("A letra maiúscula é:", {letra_maiscula})

# 46 - Faça um programa que leia um número inteiro positivo de três digitos (100 - 999) imprima o numero invertido
numeros = input("Digite três digitos de (100 a 999):")
numeros_invertido = numeros[::-1]
print("O número gerado é de:", {numeros_invertido})

# 47 - Leia um número inteiro de 4 dígitos de (1000 a 9999) e imprima 1 dígito por linha
numeros = (input("Digite um número de 4 dígitos de (1000 a 9999): "))
numero1 = numeros[0]
numero2 = numeros[1]
numero3 = numeros[2]
numero4 = numeros[3]
print(" O primeiro numero é:", {numero1})
print(" O segundo numero é:", {numero2})
print(" O terceiro numero é:", {numero3})
print(" O quarto numero é:", {numero4})

# 48 - Leia um valor inteiro em segundos, e imprima-o em horas, minutos e segundos
valor = int(input("Digite o valor em segundos:"))
segundos = valor / 1
minutos = segundos / 60
horas = minutos / 60
print("valor em horas é de:", {horas}, "o valor em minutos é:", {minutos}, "o valor em segundos é", {segundos})

# 49 - faça um programa que leia o horário(hora,minuto, segundo) de inicio e a duração em segundos de uma experiencia
hora_inicio = int(input("Digite a hora de inicio:"))
minuto_inicio = int(input("Digite os minutos de inicio:"))
segundo_inicio = int(input("Digite os segundos de inicio:"))
tempo_de_duração = int(input("Digite a duração da experiencia em segundos:"))
total_segundos = hora_inicio * 3600 + minuto_inicio * 60 + segundo_inicio + tempo_de_duração
hora_final = total_segundos // 3600
minuto_final = (total_segundos % 3600) // 60
segundo_final = (total_segundos % 3600) % 60
print(print("O horário final é:", hora_final, "horas,", minuto_final, "minutos e", segundo_final, "segundos."))

# 50 - Implemente um programa que calcule o ano  de nascimento de uma pessoa a partir de sua idade atual e do ano atual
idade = int(input("Digite sua idade atual:"))
data_atual = int(input("Digite o ano atual:"))
data_nascimento = data_atual - idade
print("Você nasceu na data de:", data_nascimento)

# 51 - Escreva um programa que leia as coordenadas x e y de pontos no R2 e calcule a sua distancia da origem (0,0)
import math
x = float(input("Digite a coordenada x do ponto: "))
y = float(input("Digite a coordenada y do ponto: "))
distancia = math.sqrt(x**2 + y**2)
print("A distância do ponto (", x, ",", y, ") à origem é:", distancia)

# 52 - Três amigos jogaram na loteria, Caso eles ganhem o prêmio deve ser dividido proporcionalmente pelo valor de cada aposta, faça um programa que leia o valor do premio, o valor que cada um investiu, e imprima quanto cada um deveria receber
valor_do_premio = float(input("Digite o valor do prêmio:"))
apostador1 = float(input("Digite o valor que o primeiro apostador investiu:"))
apostador2 = float(input("Digite o valor que o segundo apostador investiu:"))
apostador3 = float(input("Digite o valor que o terceiro apostador investiu:"))
valor_total_investido = apostador1 + apostador2 + apostador3
parte1 = valor_do_premio * (apostador1 / valor_total_investido)
parte2 = valor_do_premio * (apostador2 / valor_total_investido)
parte3 = valor_do_premio * (apostador3 / valor_total_investido)
print("O primeiro amigo deve receber R$", parte1)
print("O segundo amigo deve receber R$", parte2)
print("O terceiro amigo deve receber R$", parte3)

# 53 - Faça um programa para ler as dimensões de um terreno (comprimento e largura), e o preço do metro de tela, imprima o custo para certar o terreno
comprimento = float(input("Digite o Comprimento do terreno:"))
largura = float(input("Digite a Largura do terreno:"))
preço_da_tela = float(input("Digite o valor do metro da tela:"))
perimentro = largura * 2 + comprimento * 2
custo_final = perimentro * preço_da_tela
print("O valor par cercar todo terreno é de:", {custo_final})
"""
