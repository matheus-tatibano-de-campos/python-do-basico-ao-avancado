"""
Definindo Funções

- Funções são pequenos partes de  código que realizam tarefas especificas;
- Pode ou não receber uma entrada de dados e retornar uma saida de dados:
- Muito uteis para executar procedimentos similares repetidas vezes;

OBS: Se voce escrever uma função que realiza várias tarefas dentro dela;
é bom fazer uma verificação  para que a funcao seja simplificada.

Já utilizamos várias funções desde que iniciamos este curso:
- print()
- len()
- max()
- min()
- count()
- e muitas outras;
"""

# Exemplo de utilização de funções:

#cores = ['verde', 'vermelho', 'amarelo', 'preto']

# Utilizando uma funcao integrada ( Built-in) do Python print()

#print(cores)

#curso = 'Programação em Python: Essencial'

#print(curso)

#cores.append('roxo')

#print(cores)

# curso.append('mais dados...' # atributeError
# print(curso)

#cores.clear()
#print(cores)

# DRY - Don't Repeat Youself - Não repita você mesmo / Não repita seu código.

# Como definir Funções;
"""
Em Pyhton a forma geral de definir uma função é:
def nome_da_função(parametro_de_entrada):
    bloco_da_funcao

onde:

nome_da_funcao -> SEMPRE , com letras minusculas, e se for nome composto, separado por underline, (snake Case)
parametros_de_entrada -> Opicionais, onde tendo mais de um, cada um separado por virgula, podendo ser opicionais ou nao:
bloco_da_funcao -> Tambem chamado de corpo da funcao ou implementação é onde o processamento da função acontece.
Neste bloco, pode ter ou não retorno da função.

OBS: Veja que para definir uma função usamos a palavra reservada 'def' informando ao Pyhton que estamos definindo uma 
função. Tambem abrimos o bloco de código com o já conhecido dois pontos: que é utilizado em Pyhton para definir blocos.
 
"""

# Definindo a primeira função


def diz_oi():
    print('oi')

"""
OBS:
1 - Veja que, dentro das nossas funções podemos utilizar outras funções:
2 - Veja que nossa função só executa uma tarefa, ou seja a unica coisa que ela faz é dizer oi;
3 - Veja que está função não recebe nenhum parametro de entrada.
4 - Veja que está função nao retorna nada;
"""

# Utilizando funções
# Chamando a função
diz_oi()

"""
ATENÇÃO:
Nunca esqueça de utilizar o parênteses ao executar uma função.
"""

# Exemplo 2

def cantar_parabens():
    print('Parabens pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print('Viva o anivesariante')

# fon n in range(5):
#    cantar_parabens()

#Em Pyhton, podemos inclusive criar variaveis do tipo de uma função e executar esta função atraves da variavel


canta = cantar_parabens

canta()
