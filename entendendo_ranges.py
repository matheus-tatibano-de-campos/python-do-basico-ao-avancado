"""
Ranges

- Precisamos entender o loop for para usar o ranges
- precisamos entender melhor o ranges para trabalhar melhor com o loop for

Ranges são utilizados para gerar sequencias numericas, não de forma aleatoria más sim de maneira especificada

Formas gerais:

range(valor_de_parada)

obs: valor_de_parada não inclusive (iniciando padrao 0, e passo de 1 em 1

#forma 1
for num in range(11):
    print(num)

# forma 2

range(valor_de_inicio, valor_de_parada)
OBS: valor_de_parada não inclusive (inicio especificado pelo usuario, e passo de 1 em 1

for num in range(3, 11):
    print(num)
# Forma 3
range(valor_de_inicio, valor_de_parada)
OBS: valor_de_parada não inclusive (inicio especificado pelo usuario, e passo especificado pelo usuario)

# Exemplo forma 3
for num in range(5, 51, 5):
    print(num)

# Forma 4 (inversa)
range(valor_de_inicio, valor_de_parada)
OBS: valor_de_parada não inclusive (inicio especificado pelo usuario, e passo especificado pelo usuario)
"""
# exemplo forma 4
for num in range(10, 0, -1):
    print(num)