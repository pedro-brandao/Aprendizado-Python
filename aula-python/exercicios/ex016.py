
'''
Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
'''
# ex: digite um numero: 6.127 > o numero 6.127 tem 6 como porção inteira.

from math import floor

num = float(input('Digite um numero flutuante!:'))

real = floor(num)

print('O numero digitado arredondado é {}.'.format(real))


# Prof. Guanabara
'''
######  metodo importando  ######
from math import trunc

num = float(input('Digite um numero flutuante!:'))

real = trunc(num)

print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, real))

######  metodo sem importar  ######

num_2 = float(input("Digite um numero!:"))

print("O valor digitado foi {} e a sua parte inteira é {}".format(num, int(num)))

'''

