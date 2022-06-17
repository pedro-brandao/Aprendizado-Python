'''
- Tipos primitivos em python
- Toda linguagem de programação tem de inicio 4 tipos primitivos basicos que são inteiros, boleanos, strings e flutuantes.

----------------------------------------------------------------
int() - inteiros (1, 2, 3, 4, 5, 6...)
float() - flutuantes (1.0, 2.0, 3.0, 4.0, 5.0...)
bool() - boleanos (True, False) sempre com a iniial em maiuscula
str() - strings ('olá', 'oi', 'tudo bem'...)
----------------------------------------------------------------

'''

# Codigo antes dos tipo primitivo
numero_1 = input('digite um numero aleatorio')
numero_2 = input('digite outro numero aleatorio')

soma = numero_1 + numero_2

print('a soma vale', soma)


# Codigo depois do tipo primitivo
numero_1 = int(input('digite um numero aleatorio'))
numero_2 = int(input('digite outro numero aleatorio'))

soma = numero_1 + numero_2

#print('a soma entre {}'.format(numero_1), 'e', '{}'.format(numero_2), 'vale', '{}'.format(soma)) !!!meu codigo!!!
print('a soma entre {} e {} vale {}'.format(numero_1, numero_2, soma)) #!!!codigo do guanabara!!!

# - após fechar parenteses eu uso o metodo .format(), incluindo dentro o resultado que eu quero dentro dos couchetes
# ------------------------------------------------------------------------------------------------------------------


#tipo string com numero, seria a mesma coisa que não passar tipo na variavel
n = str(input('Digite um numero!'))
print(type(n))

#tipo int com numero, retorna apenas numeros inteiros
n = int(input('Digite um numero!'))
print(type(n))

#tipo float com numero, retorna apenas numeros com ponto flutuante
n = float(input('Digite um numero!'))
print(type(n))

#tipo bool com numero, no tipo boleano ele veifica se foi adicionado algum numero, caso sim ele retorna True, caso não, retorna False
n = bool(input('Digite um numero!'))
print(n)
print(type(n))

# ---------------------------------------------------------------------------------------------------


# O metodo isnumeric(), retorna se é possivel converter o valor colocado em numerico.

n = input('Digite algo!')
print(n.isnumeric()) #True se sim e False se não

#n = 3 - True
#n = 3a - False

# ---------------------------------------------------------------------------------------------------


# O metodo isalpha(), retorna se é possivel converter o valor colocado em alfabetico.

n = input('Digite algo!')
print(n.isalpha()) #True se sim e False se não

#n = a,b,c - True
#n = 3a - False

# ---------------------------------------------------------------------------------------------------


# O metodo isalnum(), retorna se é possivel converter o valor colocado em alfabetico e numerico.

n = input('Digite algo!')
print(n.isalanum()) #True se sim e False se não

#n = a,b,c - True
#n = 3a - True
#n = " " - False
