#Escreva uma mensagem que recebe um nome e salde a pessoa no final

nome = input("qual seu nome?")
pergunta = input("Como você vai?")
resposta_positiva = "bem"

print("Olá","Que bom ter você por aqui {}!".format(nome)) #{}.format(nome)

if pergunta == resposta_positiva:
    print("Que bom que está bem!")
else:
    print("Mas porque não está bem?")


