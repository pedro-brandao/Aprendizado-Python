
#crie um simulador de financiamento de carro.

valor = float(input('Digite o valor do carro!:'))

pagamento = str(input('Digite a forma de pagamento. 1 - A Vista e 2 - Financiado: (Lembre-se, valores financiados tem 4.2% de jurtos por parcela): '))

if pagamento == str(1):
	desconto = valor - (valor * (15 / 100))
	print('Parabéns! Pagamento A vista tem desconto de 15%, você pagara {:2f}'.format(desconto))
	
elif pagamento == str(2):
	parcela = int(input('Em quantas parcelas você deseja pagar? "Digite apenas numeros" :'))
	juros = parcela + (parcela * 4.2 / 100)
	print('Você pagara um total de {} neste carro!'.format(parcela+juros))
