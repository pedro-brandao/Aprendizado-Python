# Crie um programa que pegue duas notas de um aluno e mostre a média dele

primeira_nota = float(input('Digite uma nota:'))
segunda_nota = float(input('Digite uma segunda nota:'))

media = (primeira_nota + segunda_nota) / 2

print('As suas notas deram média de {}'.format(media))

if media >= 7:
    print('Parabéns você passou')

elif media >= 6:
    print('Você passou raspando')

elif media <= 5:
    print('Você foi reprovado!')

