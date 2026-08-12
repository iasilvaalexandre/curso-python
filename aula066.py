"""
Argumetos nomeados e nao nomeados em fucoes Python
Argumeto nomeado tem nome com sinal de igual
Argumeto nao nomeado recebe apenas o argumento (valor)
"""

def soma(x, y, z):

# Difinicicao
    print(f'{x=} y={y} {z=}' , '|', 'x + y + z =', x + y + z)



soma (1, 2, 3)
soma (1, y=2, z=5)

print(1, 2, 3, sep='-')