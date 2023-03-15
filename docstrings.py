"""
Documentando funções com Docstrings

OBS: Podemos ter acesso a documentação de uma função em Pyhton
utilizando a propriedade especial __doc__

Podemos ainda fazer acesso a documentação a função help()

"""


# Exemplos

def diz_oi():
    """Uma função simples que retorna a string , 'Oi!"""
    return 'Oi'

def exponencial(numero, potencia=2):
    """
    Função que retorna por padrão o quadrado de 'número' ou 'numero' a 'potencia' informada.
    :param numero: Número que desejamos gerar o exponencial.
    :param potencia: Potencia que queremos gerar o exponencial. por padrão é 2
    :return: Retorna o exponencial de 'nùmero' por potencia.
    """
    return  numero ** potencia