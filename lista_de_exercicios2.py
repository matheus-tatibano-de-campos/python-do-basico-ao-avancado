"""
# 1 - Faça um programa que receba dois numeros e mostre qual é o maior
numero1 = float(input("Digite um numero"))
numero2 = float(input("Digite outro numero"))
if numero1 > numero2:
    print("o maior numero é:", {numero1})
else:
    print("O maior numero é", {numero2})

# 2 - Leia um número se ele for positivo calcule a raiz quadrada, se for negativo mostre numero inválido
import math
numero = float(input("Digite um número positivo:"))
raiz = math.sqrt(numero)
if numero > 0:
    print("A raiz quadrada é:", {raiz})
else:
    print("Número inválido")

# 3 -Leia um numero real, se for positivo imprima a raiz quadrada, caso contrario  imprima o numero ao quadrado
import math
numero = float(input("Digite um número positivo:"))
if numero > 0:
    raiz = math.sqrt(numero)
    print("A raiz quadrada é:", {raiz})
else:
    numero_ao_quadrado = numero ** 2
    print("O numero ao quadrado é:", {numero_ao_quadrado})

# 4 - Faça um programa que leia um número positivo, calcule e mostre ele ao quadrado e sua raiz quadrada
import math

if numero > 0:
    numero_ao_quadrado = numero ** 2
    raiz = math.sqrt(numero)
    print("A raiz quadrada é:", {raiz})
    print("O numero ao quadrado é:", {numero_ao_quadrado})
else:
    pass

# 5 - Faça um programa que receba um número inteiro e verifique se este numero é par ou impar
numero = int(input("Digite um número inteiro:"))
if numero % 2 == 0:
    print("Numero par")
else:
    print("Numero é impar")

# 6 - Escreva um programa que recebe 2 numeros inteiros , mostre na tela o maior, assim como a diferença existente entre eles
numero1 = int(input("Digite 1 numéro inteiro:"))
numero2 = int(input("Digite 1 numéro inteiro:"))
if numero1 > numero2:
    maior = numero1
else:
    maior = numero2
diferença = abs(numero1 - numero2)

print("A diferença entre os números é", {diferença})

# 7 - Faça um programa que receba 2 numeros e mostre o maior, caso sejam iguais mostre "numeros iguais"

if numero1 > numero2:
    maior = numero1
    print(" O maior numero é: ", {maior})
elif numero2 > numero1:
    maior = numero2
    print(" O maior numero é: ", {maior})
elif numero1 == numero2:
    print(" Os numeros sao iguais")

# 8 -Faça um programa que leia 2 notas (0.0 a 10.0)e exiba na tela a media entre elas se a nota nao for valida informe ao usuario
nota1 = float(input("Digite uma nota :"))
nota2 = float(input("Digite outra  nota:"))
if nota1 and nota2 < 0 > 10:
    media = (nota1 + nota2) / 2
    print("A media das notas é", {media})
else:
    print("Nota inválida!")

# 9 -Leia um salário e o valor de uma prestação, se o valor for maior que 20% do salario, o emprestimo será negado
salario = float(input("Digite o salario:"))
prestaçao = float(input("Digite o valor da parcela:"))
porcentagem_do_salario = salario / 5
if porcentagem_do_salario < prestaçao:
    print("Emprestimo não concedido")
else:
    print("Emprestimo concedido")

# 10 - Faça um programa que receba a altura e o sexo de uma pesao e calcule seu peso ieal
sexo = input("Por gentileza escolha seu sexo: (masculino) ou (feminino):")
altura = float(input("Ensina sua altura:"))
if sexo == 'feminino':
    imc = (62.1 * altura) - 44.7
    print("Para voce mulher seu peso ideal é:", {imc})
else:
    imc = (72.7 * altura) - 58
    print("Para voce homem seu peso ideal é:", {imc})

# 11 - Escreva um programa que leia um número inteiro maior que zero, se for menor que zero digite Npumero inválido
numero1 = int(input("Digite um numero inteiro:"))
numero2 = int(input("Digite  outro numero inteiro:"))
numero3 = int(input("Digite  outro numero inteiro:"))
if numero1 < 0 or numero2 < 0 or numero3 < 0:
    print("Número inválido")
else:
    soma = numero1 + numero2 + numero3
    print("A soma de todos seus algarismo é:", {soma})

# 12 - Leia um número inteiro se for negativo digite 'Numero inválido'  caso contratio calcule seu logaritmo
import math
numero = int(input("Digite um número inteiro:"))

if numero < 0:
    print("Número inválido!")
else:
    log = math.log10(numero)
    print("O logaritmo dese número é:", {log})

# 13 - Faça um algoritmo que calcule a média ponderada das notas de 3 provas , a primeira e segunda prova tem peso 1 , a terceira peso 2, se for maior que 60 aluno aprovado
nota1 = float(input("Digite a nota da primeira prova:"))
nota2 = float(input("Digite a nota da segunda prova:"))
nota3 = float(input("Digite a nota da terceira prova:"))
media_ponderada = (nota1 + nota2 + nota3 * 2) / 3
if media_ponderada < 60:
    print(" Nota final", {media_ponderada}, "Aluno reprovado!")
else:
    print(" Nota final", {media_ponderada}, "Aluno aprovado :)")

# 14 -
nota1 = float(input("Digite a primeira nota  (entre 0 e 10):"))
nota2 = float(input("Digite a segunda nota (entre 0 e 10):"))
nota3 = float(input("Digite a terceira nota (entre 0 e 10):"))
media_ponderada = (nota1 * 2 + nota2 * 3 + nota3 * 5) / 10
if media_ponderada >= 5:
    print("Aluno Aprovado", {media_ponderada})
elif media_ponderada > 3 < 4.9:
    print("Aluno em Recuperação", {media_ponderada})
elif media_ponderada > 0 < 2.9:
    print("Aluno Reprovado! ):", {media_ponderada})
print(media_ponderada)

# 15 - Usando switch escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente ao numero domingo 1 sabado = 7
diaSemana = int(input("Digite um número de 1 a 7 para obter o dia da semana correspondente: "))

if diaSemana == 1:
    print("Domingo")
elif diaSemana == 2:
    print("Segunda-feira")
elif diaSemana == 3:
    print("Terça-feira")
elif diaSemana == 4:
    print("Quarta-feira")
elif diaSemana == 5:
    print("Quinta-feira")
elif diaSemana == 6:
    print("Sexta-feira")
elif diaSemana == 7:
    print("Sábado")
else:
    print("Número inválido. Digite um número de 1 a 7.")

#16 - Usando switch escreva um programa que leia um número entre 1 e 12 e imprima o mes correspondente
dia_mes = int(input("Digite um número de 1 a 12 para obter o mês correspondente: "))

if dia_mes == 1:
    print("Janeiro")
elif dia_mes == 2:
    print("Fevereiro")
elif dia_mes == 3:
    print("Março")
elif dia_mes == 4:
    print("Abril")
elif dia_mes == 5:
    print("Maio")
elif dia_mes == 6:
    print("Junho")
elif dia_mes == 7:
    print("Julho")
elif dia_mes == 8:
    print("Agosto")
elif dia_mes == 9:
    print("Setembro")
elif dia_mes == 10:
    print("Outubro")
elif dia_mes == 11:
    print("Novembro")
elif dia_mes == 12:
    print("Dezembro")
else:
    print("Número inválido. Digite um número de 1 a 12.")

# 17 - Faça um programa que calcule e mostre a área de um trapézio
base_maior = float(input("Digite a base maior do trapézio:"))
base_menor = float(input("Digite a base menor do trapézio:"))
altura = float(input("Digite a altura do trapézio:"))
if base_maior <=0 or base_menor <= 0:
    print("A base maior e menor deve ser maior que zero")
else:
    area = (base_maior + base_menor) * altura / 2
    print("A area do trapézio é:", {area})

# 18 - Faça um programa que tenha 4 opçoes para o usuario escolher com as operacoes básicas, entao pergunte 2 valores, e mostre o resultado
print("Escolha uma opção:")
print("1- Adição:")
print("2- Subtração:")
print("3- Multiplicação:")
print("4- Divisão:")
escolha = int(input("Digite a opçao desejada:"))
num1 = float(input("Digite um numero:"))
num2 = float(input("Digite outro número"))

if escolha == 1:
    soma = float(num1 + num2)
    print("A soma dos  números é:", {soma})
elif escolha == 2:
    sub = float(num1 - num2)
    print("A Subtração dos números é:", {sub})
elif escolha == 3:
    mult = float(num1 * num2)
    print("A Multiplicação dos  números é:", {mult})
elif escolha == 4:
    div = float(num1 / num2)
    print("A Divisão dos números é:", {div})
else:
    print("Tecla inválida, digite um número")

# 19 - faça um programa para verificar se um determinado numeeo inteiro é divisivel por 3 ou por 5 mas nao simultaneamente pelos 2
numero = int(input("Digite um número inteiro:"))
if numero % 3 == 0 and numero %5 == 0:
    print("Numero divisivel por 3 e por 5", {numero})
elif numero % 3 == 0:
    print("Número divisivel por 3", {numero})
elif numero % 5 == 0:
    print("Número divisivel por 5", {numero})
else:
    print("Número nao é divisivel por 3 nem por 5")

# 20 - Dados três valores, A, B, C
A = float(input("Digite o valor de A:"))
B = float(input("Digite o valor de B:"))
C = float(input("Digite o valor de C:"))
if A == B and B == C:
    print("Esse é um triângulo EQUILÀTERO!")
elif A == B or B == C or C == A:
    print("Esse é um triângulo ISÒCELES!")
else:
    A != B or B != C or A != C
    print("Esse é um triângulo  ESCALENO")

# 21 - Escreva o menu de opções abaixo e execute a operacao escolhida, escreva um mensagem de erro se for opção inválida
print("Escolha a opção:")
print("1- Soma de 2 números")
print("2- Diferença entre 2 números (maior pelo menor)")
print("3- Produto entre 2 números")
print("4- Divisão entre 2 números ( o denominador não pode ser zero.")
escolha = int(input("Digite a opção escolhida:"))
numero1 = float(input("Digite o primeiro número:"))
numero2 = float(input("Digite o segundo número:"))
if escolha == 1:
    soma = numero1 + numero2
    print("A soma dos 2 números é:", {soma})
elif escolha == 2:
    diferenca = abs(numero1 - numero2)
    print("A diferençã entre os 2 números é:", {diferenca})
elif escolha == 3:
    produto = numero1 * numero2
    print("O produto dos 2 números é:", {produto})
elif escolha == 4 and numero2 != 0:
    divisao = numero1 / numero2
    print("A divisão dos 2 números é:", {divisao})
else:
    print("Digite um número valido!")

# 22- Leia a idade e o tempo de serviço de um trabalhador e escreve se ele pode ou não se aposentar (ter mais de 65 anos ter trabalhado por 30 anos ou ter pelo menos 60 e ter trabalahdo 25
idade = int(input("Digite a sua idade atual:"))
tempo_contribuido = int(input("Digite o tempo trabalhado em anos:"))
if tempo_contribuido >= 30:
    print("Aposentado por tempo de trabalho")
elif idade >= 65:
    print("Aposentado por idade")
elif idade >= 60 and tempo_contribuido >= 25:
    print("Aposentado por tempo e idade")
else:
    print("Não atende os requisitos para aposentar!")

# 23 - Determine se  um ano lido é bissexto ou nao
ano = int(input("Digite um ano:"))
calculo_bissexto = ano %400 == 0
if  ano %400 == 0:
    print("Esse ano é bissexto", {ano})
elif ano % 4 == 0 and  ano % 100 != 0:
    print("Esse é um ano bissexto", {ano})

# 24 - Calcular o valor do produto sobre os imposto mg 7% sp 12% rj 15% ms8%
produto = float(input("Digite o Valor do produto:"))
estado = input("Digite o estado para envio:")
imposto_mg = 7/100
imposto_sp = 12/100
imposto_rj = 15/100
imposto_ms = 8/100
if estado == 'mg':
    valor_mg = produto * imposto_mg
    valor_final_mg = produto + valor_mg
    print("O Produduto para MG fica em:", {valor_final_mg})
elif estado == 'sp':
    valor_sp = produto * imposto_sp
    valor_final_sp = produto + valor_sp
    print("O Produduto para SP fica em:", {valor_final_sp})
elif estado == 'rj':
    valor_rj = produto * imposto_rj
    valor_final_rj = produto + valor_rj
    print("O Produduto para RJ fica em:", {valor_final_rj})
elif estado == 'ms':
    valor_ms = produto * imposto_ms
    valor_final_ms = produto + valor_ms
    print("O Produduto para MS fica em:", {valor_final_ms})
else:
    print("Infelizmente não atendemos o seu estado")

# 26 - Leia a distancia em km e a quantidade em litros de gasolina consumida por um carro, e calcule o consumo km/l
distancia = float(input("Digite a distancia em KM:"))
litros_usados = float(input("Digite quantos litros de gasolina foram utilizados:"))
consumo = distancia / litros_usados
if consumo < 8:
    print("Venda o carro!")
elif 8 <= consumo <= 12:
    print("Econômico!")
else:
    print("Super Econômico!")
"""
# 27 - Escreva um programa que dada a idade de um nadador  classifica entre  infantil (5 a 7) infantilB (8 a 10) juvenil
idade = int(input("Digite a idade do nadador:"))
if 5 <= idade <= 7:
    print("Categoria Infantil A")
elif 8 <= idade <=10:
    print("Categoria Infantil B")
elif 11 <= idade <= 13:
    print("Categoria Juvenil A")
elif 14 <= idade <= 17:
    print("Categoria Juvenil B")
else:
    print("Categoria Sênior")