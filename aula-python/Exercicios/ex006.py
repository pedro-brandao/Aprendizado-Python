#  Crie um algoritmo que leia um numero e mostre seu dobro, triplo e raiz quadrada

numero = int(input('Digite um numero:'))

dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1/2)

# Meu codigo
print('Você escolheu o numero {}, o dobro dele é o {}, o triplo é {} e a raiz quadrada dele é {}'.format(numero, dobro, triplo, raiz))

# Codigo guanabara
print('Você escolheu o numero {}, \no dobro dele é o {}, \no triplo é {} \ne a raiz quadrada dele é {}'.format(numero, (numero*2), (numero*3), (numero**(1/2))))

# pow(numero, (1/2)) - Outra forma de calcular a raiz quarada
