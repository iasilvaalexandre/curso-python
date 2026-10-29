# from sys import path

# import aula099_package.modulo
# from aula099_package import modulo
# from aula099_package.modulo import *

# # from aula099_package.modulo import soma_do_modulo

# # print(*path, sep='\n')
# print(aula099_package.modulo.soma_do_modulo(1, 2))
# print(aula099_package.modulo.soma_do_modulo(1, 2))
# print(modulo.soma_do_modulo(1, 2))
# print(variavel)
# print(nova_variavel)

# from aula099_package.modulo import soma_do_modulo , fala_oi, variavel, nova_variavel

# print(__name__)
# fala_oi()
from aula099_package import *
import aula099_package

print(aula099_package.soma_do_modulo(1, 2))
aula099_package.qualquer_coisa()