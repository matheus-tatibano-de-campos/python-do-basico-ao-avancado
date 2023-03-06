"""
Estruturas Lógicas: and (e), or (ou), not (não), is (é)

Operadores unários:
     -not, is
Operadores binários:
     -and, or
     para o 'not' o valor booleano é invertido, ou seja  true vira false, false vira true
"""
ativo = True
logado = True

# se não estiver ativo faça isso
if not ativo:
    print("Você precisa ativar sua conta. Por favor, cheque seu e-mail")
else:
    print('bem vindo usuario')

# ativo é verdadeiro ?
print(ativo is True)

