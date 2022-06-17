# criar um programa que leia algo pelo teclado e mostre na tela o seu tipo primitvo e todas as informações possiveis sobe ele

from curses.ascii import isupper
import this


pedido = input('Digite algo: ')

if pedido.isnumeric() == True:
    print('o numero que você digitou é o {}'.format(pedido), 'e por não haver um tipo especifico definido ele é do tipo', type(pedido))

elif pedido.isalpha():
    print("você digitou algo do tipo alfabetico, e ele é considerado", type(pedido), 'por não haver um tipo definido')

elif pedido.isalnum():
    print("você digitou algo do tipo alfa-numerico, e ele é considerado", type(pedido), 'por não haver um tipo definido')

print('Abaixo algumas outras informações sobre oque foi digitado.')

print('É tudo maiusculo?', pedido.isupper())

print('É tudo minusculo?', pedido.islower())
    
print('Só tem espaços?', pedido.isspace())

print('Está capitalixada?', pedido.istitle()) #com a inicial maiuscula

   
