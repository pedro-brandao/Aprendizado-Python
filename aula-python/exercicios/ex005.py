# Faça um programa que leia um numero e mostre na tela o seu sucessor e o seu antecessor.

numero = int(input('Digite um numero:'))

soma = numero + 1
sub = numero - 1

# Meu coodigo
print('Você escolheu o numero {}, e o antecessor dele é {} e o sucessor é o {}'.format(numero, sub, soma))

# Codigo Guanabara, substitui as variaveis para econimizar memoria
print('Você escolheu o numero {}, e o antecessor dele é {} e o sucessor é o {}'.format(numero, (numero-1), (numero+1)))
