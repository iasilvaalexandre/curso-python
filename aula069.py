"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""

x = 1


def escopo():
    # global x  # Declarando que a variavel x é global
    x = 10  # Atribuindo um novo valor a variavel global x

    def outra_funcao():
        global x  # Declarando que a variavel x é global
        x = 11  # Atribuindo um novo valor a variavel global x  
        y = 2  # Variavel local a funcao outra_funcao
        print(x, y)

    outra_funcao()
    print(x)  # Acessando a variavel global x


print(x)  
escopo()  
print(x)

