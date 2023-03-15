
indice = 13
soma = 0
k = 0

for i in range(13):
    k += 1
    soma = soma + k
print(soma)


def fibonacci(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def verifica_fibonacci(num):

    n = 0
    while fibonacci(n) <= num:
        if fibonacci(n) == num:
            return True
        n += 1
    return False

num = int(input("Digite um número inteiro: "))
if verifica_fibonacci(num):
    print(f"{num} pertence à sequência de Fibonacci.")
else:
    print(f"{num} não pertence à sequência de Fibonacci.")
"""
a) 1, 3, 5, 7, 9

b) 2, 4, 8, 16, 32, 64, 128

c) 0, 1, 4, 9, 16, 25, 36, 49

d) 4, 16, 36, 64, 100

e) 1, 1, 2, 3, 5, 8, 13

f) 2,10, 12, 16, 17, 18, 19, 20
"""
"""
distância = 50 km
velocidade = 110 km/h

Assim, o tempo que o carro leva para chegar ao ponto de encontro é:

tempo = distância / velocidade = 50 / 110 = 0,4545 horas

o caminhão leva um total de 10 minutos extras (ou 0,1667 horas) para percorrer a distância entre as cidades
distância = 50 km
velocidade = 80 km/h
tempo = distância / velocidade + tempo dos pedágios = 50 / 80 + 0,1667 = 0,7917 horas

Para o carro:

distância até Ribeirão Preto = 50 km - (velocidade x tempo) = 50 - (110 x 0,4545) = 1,3635 km

Para o caminhão:

distância até Ribeirão Preto = 50 km - (velocidade x tempo) = 50 - (80 x 0,7917) = 14,664 km

Assim, podemos concluir que o carro está mais próximo da cidade de Ribeirão Preto
no momento em que os veículos se cruzam na rodovia.
"""
string = "Espero que tenham gostado"
tamanho = len(string)
string_invertida = ""

for i in range(tamanho):
    string_invertida += string[tamanho - i - 1]

print(string_invertida)
