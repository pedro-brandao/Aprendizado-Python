# Crie um conversor de temperatura de graus celcius em Fahrenheit

c = float(input("Digite quantos graus celsius estão fazendo hoje:"))
f = ((9 * c) / 5)+32

print(f)

# (1 x 9) / 5) + 32 = 33.8

# Codigo Prof. Guanabara
c = float(input('Digite quantos graus celsius estão fazendo hoje: '))
f = ((9 * c) / 5) + 32
# f = 9 * c / 5 +32

print('A temperatura de {}´C corresponde a {}´F!'.format(c,f))