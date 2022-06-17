''' Faça um programa que leia a largura e a altura de uma parede em metros,
    calcule a sua area e a quantidade de tinta necessaria para pinta-la,
    sabendo que cada litro de tinta, pinta uma area de 2m2.
'''

lar_par = float(input('Digite a largura da parede:')) 
alt_par = float(input('Digite a altura da parede:'))

mts_quad = lar_par * alt_par # Tamanho da parede lar x alt

print("sua parede tem {}x{} e sua area é de {}m2".format(lar_par,alt_par,mts_quad))

litro = 2

valor = mts_quad / litro

print('Você gastará {} litro(s) de tinta para pintar a sua parede.'.format(valor))
