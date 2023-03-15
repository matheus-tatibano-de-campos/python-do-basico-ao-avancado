"""
**kwargs

Poderíamos chamar este parâmetro de **xis, mas por conveção chamamos de **kwargs

este é so um parâmetro, mas diferente do *args que coloca os valores extras em uma tupla
o **kwargs exige que utilizemos paramêtros nomeados, e transforma esses parâmetros extras
em um dicionario.

# Exemplo

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')


cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')

# OBS: Os parâmetros  *args e **kwargs não são obrigatorios.

cores_favoritas()

cores_favoritas(geek='navy')

# Exemplo mais complexo

def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Voce Recebeu um cumprimento Pythonico Geek'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'Não tenho certeza quem você é...'

print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='oi'))
print(cumprimento_especial(geek='especial'))

# nas nossas funções , podemos ter (NESTA ORDEM):

- Parâmetros obrigatorios:
- *args;
- Parametros default (não Obrigatorios);
- ** Kwargs



def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)

minha_funcao(8, 'Julia')
minha_funcao(18, 'Felicity', 4, 5, 6, solteiro=True)
minha_funcao(34, 'Matheus', eu='Não', voce='Vai')
minha_funcao(19, 'Carla', 9, 4, 3, java=False, python=True)

# Entenda por quê é importante manter a ordem dos parâmetros na declaração


# função com a ordem correta de parâmetros
# def mostra_info(a, b, *args, instrutor='geek', **kwargs):
#   return [a, b, args, instrutor, kwargs]


#Função com a ordem incorreta de parâmetros
def mostra_info(a, b,  instrutor='geek', *args, **kwargs):
    return [a, b, args, instrutor, kwargs]


print(mostra_info(1, 2, 3, sobrenome='University', cargo= 'Instrutor'))

# Desempacotar com **kwargs


def mostra_noms(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {'nome': 'Felicity', 'sobrenome': 'jones'}

print(mostra_noms(**nomes))
"""


def soma_multiplos_numeros(a, b, c, **kwargs):
    print(a + b + c)


lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}

soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*conjunto)

dicionario = dict(a=1, b=2, c=3)

soma_multiplos_numeros(**dicionario)

# OBS: Os nomes da chave em um dicionario, devem ser  o mesmo do parâmetro da funcao;

# dicionario = dict(d=1, e=2, f=3) # TypeError
#soma_multiplos_numeros(**dicionario) # TypeError

dicionario = dict(a=1, b=2, c=3, nome='Geek')
soma_multiplos_numeros(**dicionario, lang='Python')