"""
Tipo string
Em python, um dado é considerado do tipo string sempre que:

-Estiver entre aspas simples -> 'uma string', '12', 'true', 'True', '33.2'
-Sempre que estiver em aspas duplas "uma string", "12", "true", "True", "33.2"
-Sempre que estiver em áspas simples triplas  '''uma string''', '''12''', '''true''', '''True''', '''33.2'''
"""
nome = "Geek University"
print(nome)
print(type(nome))

nome = "Gina's Bar"
print(nome)
print(type(nome))

nome = 'Angelina Jolie'
print(nome)
print(type(nome))

# Pulando linha na string
nome = """Angelina 
Jolie"""
print(nome)
print(type(nome))

nome = "Geek University"
print(nome.upper())

nome = "Geek University"
print(nome.split())

nome = "Geek University"
print(nome[0:4])
print(nome[5:15])

print(nome[::-1]) # inverte a string com emtodo pythonico