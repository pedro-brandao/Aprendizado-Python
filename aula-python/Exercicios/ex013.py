''' Faça um programa que pegue o salario de um funcionario e mostre seu novo salario com 15% de aumento '''

salario = float(input('Digite seu salario atual:'))
por_aumento = int(input('Digite a porcentagem do seu aumento:'))

poraum = por_aumento / 100

aumento = (salario * poraum) + salario

print('Seu salario com aumento é {}'.format(aumento))