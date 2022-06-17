# Crie um programa que leia quanto a pessoa tem na carteira e quantos dolares ela pode comprar.

carteira = float(input('Digite quanto você tem na sua carteira: R$:'))
dolar = float(4.99)

soma = (1 / dolar) * carteira

print('Oque você tem compra {:.2f} US$ Dolar(es)'.format(soma))

# Resposta do Prof. Guanabara
dinheiro = carteira / 4.99
print('Oque você tem compra {:.2f} US$ Dolar(es)'.format(soma))

