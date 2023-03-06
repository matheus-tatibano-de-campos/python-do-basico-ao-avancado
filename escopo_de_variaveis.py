"""
Escopo de variaveis

Dois casos de escopo:

1 - Variáveis globais;
    - Variáveis globais são reconhecidas, ou seja  o seu escopo compreende , todo o o programa.

2 - Variáveis locais
    - Variáveis locais são reconhecidas apenas no blco onde foram declaras, ou seja seu escopo
    está limitada ao bloco onde foi declarado.

Para declarar Variáveis em Python fazemos:

nome_da_variavel = varlor_da_variavel

python é uma linguagem de tipagem dinâmica. Isso significa que
ao declarar uma variaável, nós não colocamos o tipo de dado dela
este tipo é inferido ao atribuirmos o valor da mesma
"""

numero = 42
print(numero)
print(type(numero))

numero = "Geek"
print(numero)
print(type(numero))

numero = 42
# novo = 0
if numero > 10:
    novo = numero + 10 # A variável 'novo' está declarada localmente dentro do bloco do if
    print(novo)
print(novo)
