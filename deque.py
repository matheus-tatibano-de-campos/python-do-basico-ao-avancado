"""
Modulo Collections - Deque

Podemos dizer que o deque é uma lista de alta performance.

"""

# Importando
from collections import  deque

# Criando deque

deq = deque('Geek')

print(deq)

# Adicionando elementos no deque

deq.append('y') # Adiciona no final

print(deq)

deq.appendleft('K') # Adiciona no Começo da lista
print(deq)

# Remover elementos
print(deq.pop()) # Remove e retorna o ultimo elemento

print(deq)

print(deq.popleft())

print(deq)