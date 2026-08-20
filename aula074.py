"""
Closure e funcoes que retornam outras funcoes
"""

def criar_saudacao (saudacao):
    def saudar (nome):
        return f'{saudacao}, {nome}'
    return saudar

falar_bom_dia = criar_saudacao ('Bom Dia')
falar_boa_noite = criar_saudacao ('Boa noite')

for nome in ['Maria', 'Jose', 'Igor', 'Luiz']:
    print (falar_bom_dia(nome))