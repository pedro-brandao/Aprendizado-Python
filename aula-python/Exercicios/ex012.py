''' Escreva um programa que leia o preço de um produto e mostre seu novo preço com 5% de desconto. '''

valor = float(input('Digite o valor do produto:'))

porcentagem = 5 / 100

final = valor * porcentagem

valor_final = valor - final

print(valor_final)