'''
Faça um programa que leia o comprimento do cateto oposto e a do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa.
'''

# ------------- Codigo Prof. Guanabara sem modulos -------------------
from math import hypot

co = float(input("Digite o valor do cateto oposto: "))
ca = float(input("Digite o valor do cateto adjacente: "))

hi = (co ** 2 + ca ** 2 ) ** (1/2)

print('A hipotenusa vai medir {:.2f}'.format(hi))

# ------------- Codigo Prof. Guanabara com modulos -------------------
''' Usando Modulos '''

co = float(input("Digite o valor do cateto oposto: "))
ca = float(input("Digite o valor do cateto adjacente: "))

hip = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hip))