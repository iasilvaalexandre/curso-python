"""
Valores padrao para parametros
Ao definir uma função, os parametros podem
ter valores padrao. Caso o valor nao seja
enviado para o parametro, o valor padrao sera
usado.
refatorar : editar seu codigo para melhorar a legibilidade, simplicidade e manutenibilidade.
"""

def soma(x, y, z=None):
   if z is not None:
      print(f'{x=} {y=} {z=}', x + y + z)
   else:
      print(f'{x=} {y=}' , x + y)


soma (1, 2)
soma (3, 5)
soma (100, 200)
soma (7, 9, 0)  
soma ( y=9, z=0, x=7)