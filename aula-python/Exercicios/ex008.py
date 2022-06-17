# Crie um programa que receba um valor em metros e converta ele em centimetros e milimetros

metro = int(input('Digite um valor para conversão:'))

kilometro = metro * 0.001
hectometro = metro * 0.01
decametro = metro * 0.1
decimetro = metro * 10
centimetro = metro * 100
milimetro = metro * 1000

print('Você escolheu {} metro(s), ele em centimetro fica {}CN e em milimetros {}MM'.format(metro, centimetro, milimetro))


# pedido do professor Guanabara
print(kilometro, "kilometro")
print(hectometro, "hectometro")
print(decametro, "decametro")
print(decimetro, "decimetro")
print(centimetro, "centimetro")
print(milimetro, "milimetro")
'''
Milimetro
Centimetro
Decimetro
Metros
Decametro
Hectometro
Kilometro
'''