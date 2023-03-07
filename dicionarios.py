"""
Dicionários

OBS: em algumas linguagens de programação. os dicionarios pyhton sao conhecidos por MAPAS.

Dicionários são coleções do tipo chave/valor.
[0, 1, 2]                (0, 1, 2)
[1, 2, 3]                (1, 2, 3)
Dicionarios são representados por chaves { }
print(type({}))
OBS: Sobre dicionarios
    - Chave e valor são separados por dois pontos 'chave:valor';
    - Tanto chave quanto valor podem ser de qualquer tipo de dado;
    - Podemos misturar tipos de dados;

# Criação de dicionarios

# Forma 1  (mais comum)


print(paises)
print((type(paises)))

# Forma 2 (menos comum)
paises = dict(br ='Brasil', eua='Estados Unidos', py ='Paraguay')
print(paises)
print(type(paises))

# Acessando elementos
# forma 1 - Acessando via chave, da mesma forma que lista/tupla
print(paises['br'])
print(paises['py'])

# OBS: Caso tentamos fazer um acesso utilizando uma chave que naão existe, teremos o erro de KeyError

# Forma 2 via get - Recomendada
print(paises.get('br'))
print(paises.get('ru'))

# Caso o get não encontre o objeto com a chave informada, sera retornado o valor None, e nao sera gerado KeyError
pais = paises.get('ru')

if pais:
    print(f'Encontrei o país {pais}')
else:
    print('Não encontrei o país')


# Podemso definir um valor padrão para caso não encontremos o objeto com a chave informada
pais = paises.get('py', 'Não encontrado')

print(f'Encontrei o país {pais}')

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

# Podemos verificar se determinada chave se encontra em um dicionario

print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)
if 'ru' in paises:
    russia = paises['ru']

# Podemos utilizar qualquer tipo de dado, (int, float, string, boolean) , inclusive lista, tupla, dicionario, como chaves
# de Dicionarios.

# Tuplas por exemplo são bastante interessante de serem utilizados como chave de dicionarios, pois sao IMUTAVEIS
localidades = {
    (35.6984, 09.548): 'Escritorio em Tókio',
    (40.5484, 19.448): 'Escritorio em Nova York',
    (33.4954, 57.848): 'Escritorio em São Paulo',
}

print(localidades)
print(type(localidades))

# Adicionar elementos em um dicionário

receita = {'Jan': 100, 'fev': 120, 'mar': 300}
print(receita)
print(type(receita))

# Forma 1 (Mais Comum)

receita['abr'] = 350

print(receita)

# Forma 2

novo_dado = {'mai': 500}
receita.update(novo_dado) # receita.update({'mai': 500})
print(receita)

# Atualizando dados em um dicinário

# Forma 1

receita['mai'] = 550

print(receita)

# Forma 2

receita.update({'mai': 600})
print(receita)

# CONCLUSÃO 1: a forma de adicionar novos elementos ou atualizar dados em um dicionario é a mesma.
# CONCLUSÃO 2: Em dicionarios, NÃO podemos ter chaves repeteidas.

# Remover dados de um dicionário
receita = {'Jan': 100, 'fev': 120, 'mar': 300}

print(receita)
# Forma 1 - Mais comum

ret = receita.pop('mar')
print(ret)

print(receita)

# OBS 1: Aqui precisamos sempre informar a chave, e caso não encontre o elemento, um KeyError é retornado.
# OBS 2: Ao removermos um objeto o valor deste objeto é sempre retornado

# Forma 2 - menos comum

del receita['fev']

print(receita)

# Se a chave nao exister sera gerado um KeyError
# OBS: Neste caso o valor removido não é retornado.
"""

# Imagine que voce tem um comércio eletronico, onde temos um carrinho de compras na qual adicinamos produtos
"""
Carrinho de compras:
    produto1:
        - nome
        - quantidade
        - preço
    produto2:
         - nome
        - quantidade
        - preço

# - Poderiamos utilizar uma lista para isso ? SIM

carrinho = []

produto1 = ['Playstation4', 1, 2300.00]
produto2 = ['God of war', 1, 130.00]

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

# 2  - Poderiamos utilizar um Tupla para isso ? SIm
produto1 = ('Plaistation4', 1, 2300.00)
produto2 = ('Gof of War4', 1, 150.00)

carrinho = (produto1, produto2)
print(carrinho)
# Teriamos que saber qual é o indice de cada informação no produto.

# 3 - Poderiamos utilizar um Dicionario para isso ? Sim

carrinho = []

produto1 = {'nome': 'Playstation4', 'quantidade': 1, 'preco': 2300.00}
produto2 = {'nome': 'God of war', 'quantidade': 1, 'preco': 150.00}
carrinho.append(produto2)
carrinho.append(produto1)

print(carrinho)
# Desta forma facilmente adicionamos ou removemos produtos no carrinho e em cada produto
# Podemos ter a certeza sobre cada informação.

# Limpar o dicionario (Zerar dados)

d.clear()
print(d)

# Copiando um dicionario para outro

# Forma 1 Deep Copy

novo = d.copy()
print(novo)

novo['d'] = 4
print(d)
print(novo)

# Métodos de dicionarios.

d = dict(a=1, b=2, c=3)

print(d)
print(type(d))

# Forma 2 Shallow Copy
novo = d

print(novo)
novo['d'] = 4
print(d)
print(novo)
"""

# Forma não usual de criação de dicionarios

outro = {}.fromkeys('a', 'b')

print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

# O método fromkeys recebe dois parametros: um iteravel e um valor.
# Ele vai gerar para cada valor do iteravel uma chave e ira atribuir a esta chave o valor informado.

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1, 11), 'novo')
print(veja)
