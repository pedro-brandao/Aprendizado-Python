''' Faça um programa que pegue o salario de um funcionario e mostre seu novo salario com 15% de aumento '''

salario = float(input('Digite seu salario atual:'))
por_aumento = int(input('Digite a porcentagem do seu aumento:'))

poraum = por_aumento / 100

aumento = (salario * poraum) + salario

print('Seu salario com aumento de {}% é de R${:.2f}'.format(por_aumento, aumento))


# Código Prof. Guanabara

salario = float(input('Qual é o salario do funcionario? R$'))
novo salario + (salario * 15 / 100)

print('Um funcionario que ganhava R${:.f}, com 15% de aumento, passa a receber R${:.f}'.format(salario, novo))