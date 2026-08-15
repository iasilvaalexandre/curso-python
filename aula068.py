"""
Escopo de funcoes em Python
Escopo significa o local onde aquele codigo pode atingir, ou seja, onde aquela variavel ou funcao pode ser acessada.
Existe o espoco global e o escopo local. O escopo global é aquele que pode ser acessado de qualquer lugar do codigo, ja o escopo local é aquele que so pode ser acessado dentro da funcao.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""

x = 1


def escopo():
    global x  # Declarando que a variavel x é global
    x = 10  # Atribuindo um novo valor a variavel global x

    def outra_funcao():
        global x  # Declarando que a variavel x é global
        x = 11  # Atribuindo um novo valor a variavel global x  
        y = 2  # Variavel local a funcao outra_funcao
        print(x, y)

    outra_funcao()
    print(x)  # Acessando a variavel global x


print(x)  # Acessando a variavel global x
escopo()  # Chamando a funcao escopo
print(x)  # Acessando a variavel global x