"""
Tipo Booleano

Algebra Booleana, criada por George Boole

2 constantes, Verdadeiro ou Falso

True -> Verdadeiro
False -> Falso

OBS: Sempre com a inicial maiuscula

Errado:

true, false

Certo:

True, False
"""

ativo = False

print(ativo)

"""
Operações básicas:
"""
# Negação (not)
"""
Fazendo a negação, so o resultado for verdadeiro o resultado será falso, se 
for falso usando a negação o resultado sera verdadeiro, sempre o contrátario
"""
print(not ativo)
logado = False

# Ou (or):
"""
È uma operação bínaria, ou seja um depende de dois valores, ou um ou ooutro deve ser verdadeiro.

True or True -> True
True or False -> True
False or True -> True
False or False -> False
"""
print(ativo or logado)

# E (and):
"""
Também é uma operação binaria, ou seja depende de dos valores. Ambos precisam ser verdadeiro

True or True -> True
True or False -> False
False or True -> False
False or False -> False
"""