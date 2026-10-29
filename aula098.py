import importlib

import aula098_m

print(aula098_m.variavel)


for i in range(10):
    importlib.reload
    print(i)

print("Fim do programa")