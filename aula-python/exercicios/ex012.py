''' Escreva um programa que leia o preço de um produto e mostre seu novo preço com 5% de desconto. '''

valor = float(input('Digite o valor do produto:'))

porcentagem = 5 / 100 #podendo ser 10*5/100 = 0.5

final = valor * porcentagem

valor_final = valor - final

print(valor_final)


# Programa Prof. Guanabara

preco = float(input("Qual é o valor do produto? R$"))
novo = preco - ( preco * 5 / 100)

print('O produto que custava R${:.f}, na promoção de 5% vai custar R${:.2f}'.format(preco, novo))