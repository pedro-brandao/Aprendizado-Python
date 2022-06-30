#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado


dias = int(input('Digite quantos dias você ficou com o carro: '))

km = float(input('Digite quantos KM você rodou: '))

val_dia = dias * 60.00

val_km = km * 0.15

total = val_dia + val_km

print(total)

#Codigo guanabara
dias = int(input('Digite quantos dias você ficou com o carro: '))

km = float(input('Digite quantos KM você rodou: '))

pago = (dias * 60.00) + (km * 0.15)

print(pago)