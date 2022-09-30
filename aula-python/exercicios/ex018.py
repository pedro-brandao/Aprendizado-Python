'''
Faça um programa que leia um angulo qualquer e mostre na tela o valo do seno, cosseno e tangente desse angulo.
'''

angulo = float(input("Digite o angulo que você quer: "))
seno = math.sin(math.radians(angulo))

print("O angulo {} tem SENO de {}".format(angulo, seno))