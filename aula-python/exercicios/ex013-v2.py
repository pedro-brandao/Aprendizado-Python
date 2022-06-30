''' Faça um programa que pegue o valor de um produto e passe 10% de desconto a vista e 15% de juros a prazo '''

preco = float(input("Digite o valor do produto! R$"))

pagamento = int(input("Qual a forma de pagamento? Digite 1 = A Vista ou 2 = A Prazo: "))

desconto = preco - (preco * 10 / 100)

taxa = preco + (preco * 15 / 100)

if pagamento == 1:
	print("Você optou em pagar a vista e essa opção desbloqueou um desconto de 10% ficando o valor final em R${:.2f}".format(desconto))

elif pagamento == 2:
	print("Você irá pagar a prazo e essa opção tem 15% de taxa, ficando em R${:.2f} deseja mesmo seguir?".format(taxa))
