"""
Introdução as funcoes (def) em Python
Replicar determinada ação ao londo do seu codigo
Elas podem receber valores para parametros (argumetos)
e retornar um valor especifico.
Por padrao, funcoes Python retornam None (nada)
"""

# def imprimir (a, b, c):
#     print(a, b, c)


# imprimir(1, 2, 3)
# imprimir(4, 5, 6)

def saudacao (nome='Voce é novo aqui ? Qual seu nome?'):
    print (f'Olá, {nome}!')
    
saudacao('Alice')
saudacao('Bob')
saudacao()