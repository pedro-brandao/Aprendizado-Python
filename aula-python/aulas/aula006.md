
# Tipos primitivos em python
- Toda linguagem de programação tem de inicio 4 tipos primitivos basicos que são inteiros, boleanos, strings e flutuantes.

--- ----
int() - inteiros (1, 2, 3, 4, 5, 6...)<br>
float() - flutuantes (1.0, 2.0, 3.0, 4.0, 5.0...)<br>
bool() - boleanos (True, False) sempre com a iniial em maiuscula<br>
str() - strings ('olá', 'oi', 'tudo bem'...)<br>
--- ----

## Codigo antes dos tipo primitivo
~~~python
numero_1 = input('digite um numero aleatorio')
numero_2 = input('digite outro numero aleatorio')

soma = numero_1 + numero_2

print('a soma vale', soma)
~~~

## Codigo depois do tipo primitivo
~~~python
number_1 = int(input('digite um número aleatório'))
numero_2 = int(input('digite outro numero aleatorio'))

soma = numero_1 + numero_2

print('a soma entre {}'.format(numero_1), 'e', '{}'.format(numero_2), 'vale', '{}'.format(soma) #!!!meu codigo!!!
print('a soma entre {} e {} vale {}'.format(numero_1, numero_2, soma)) #!!!codigo do guanabara!!!
~~~
Após fechar parenteses eu uso o metodo .format(), incluindo dentro o resultado que eu quero dentro dos couchetes.
--- ---


Tipo string com numero, seria a mesma coisa que não passar tipo na variavel. Pois o número será considerado como texto.
~~~python
n = str(input('Digite um numero!'))
print(type(n))
~~~
Tipo int com numero, retorna apenas numeros inteiros.
~~~python
n = int(input('Digite um numero!'))
print(type(n))
~~~
Tipo float com numero, retorna apenas numeros com ponto flutuante.
~~~python
n = float(input('Digite um numero!'))
print(type(n))
~~~
Tipo bool com numero, no tipo boleano ele veifica se foi adicionado algum numero, caso sim ele retorna True, caso não, retorna False
~~~python
n = bool(input('Digite um numero!'))
print(n)
print(type(n))
~~~
--- ---


### O metodo isnumeric(), retorna se é possivel converter o valor colocado em numerico.
~~~python
n = input('Digite algo!')<br>
print(n.isnumeric()) #True se sim e False se não<br>

#n = 3 - True<br>
#n = 3a - False<br>
~~~
--- ---


### O metodo isalpha(), retorna se é possivel converter o valor colocado em alfabetico.
~~~python
n = input('Digite algo!')
print(n.isalpha()) #True se sim e False se não<br>

#n = a,b,c - True<br>
#n = 3a - False<br>
~~~
--- ---

### O metodo isalnum(), retorna se é possivel converter o valor colocado em alfabetico e numerico.
~~~python
n = input('Digite algo!')
print(n.isalanum()) #True se sim e False se não<br>

n = a,b,c - #True
n = 3a - #True
n = " " - #False
~~~