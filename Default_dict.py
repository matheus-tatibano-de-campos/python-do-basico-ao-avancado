"""
Modulo Collection - Default Dict

# Recape Dicionarios

dicionario = {'curso': 'Programação em Python: Essencial'}

print(dicionario)
print(dicionario['curso'])
print(dicionario['outro']) # ??? KeyError

Default Dict -> ao criar um dicionario utilizando-o nós informamos um valor default,
podendo uilizar um lambda para isso. Este valor será uitlizado sempre que nao houver
um valor definido. Caso tentemos acessar uma chave que nao existe, essa chave sera criada
e o valor default sera atribuido.
"""

# fazendo o import
from collections import  defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['curso'] = 'programação em Python: Essencial'

print(dicionario)

print(dicionario['outro']) # KeyError no dicionario comum, mas aqui não

print(dicionario)