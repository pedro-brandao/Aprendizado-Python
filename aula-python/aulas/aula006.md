
# Tipos primitivos em python
- Toda linguagem de programação tem de inicio 4 tipos primitivos basicos que são inteiros, boleanos, strings e flutuantes.

--- ----
int() - inteiros (1, 2, 3, 4, 5, 6...)<br>
float() - flutuantes (1.0, 2.0, 3.0, 4.0, 5.0...)<br>
bool() - boleanos (True, False) sempre com a iniial em maiuscula<br>
str() - strings ('olá', 'oi', 'tudo bem'...)<br>
--- ----

## Codigo antes dos tipo primitivo
numero_1 = input('digite um numero aleatorio')<br>
numero_2 = input('digite outro numero aleatorio')<br>

soma = numero_1 + numero_2<br>

print('a soma vale', soma)<br>


## Codigo depois do tipo primitivo
numero_1 = int(input('digite um numero aleatorio'))<br>
numero_2 = int(input('digite outro numero aleatorio'))<br>

soma = numero_1 + numero_2<br>

print('a soma entre {}'.format(numero_1), 'e', '{}'.format(numero_2), 'vale', '{}'.format(soma) !!!meu codigo!!!<br>
print('a soma entre {} e {} vale {}'.format(numero_1, numero_2, soma)) #!!!codigo do guanabara!!!<br>

(Após fechar parenteses eu uso o metodo .format(), incluindo dentro o resultado que eu quero dentro dos couchetes).
--- ---


(tipo string com numero, seria a mesma coisa que não passar tipo na variavel)<br>
n = str(input('Digite um numero!'))<br>
print(type(n))<br>

(tipo int com numero, retorna apenas numeros inteiros)<br>
n = int(input('Digite um numero!'))<br>
print(type(n))<br>

(tipo float com numero, retorna apenas numeros com ponto flutuante).<br>
n = float(input('Digite um numero!'))<br>
print(type(n))<br>

(tipo bool com numero, no tipo boleano ele veifica se foi adicionado algum numero, caso sim ele retorna True, caso não, retorna False)<br>
n = bool(input('Digite um numero!'))<br>
print(n)<br>
print(type(n))<br>

--- ---


### O metodo isnumeric(), retorna se é possivel converter o valor colocado em numerico.

n = input('Digite algo!')<br>
print(n.isnumeric()) #True se sim e False se não<br>

#n = 3 - True<br>
#n = 3a - False<br>

--- ---


### O metodo isalpha(), retorna se é possivel converter o valor colocado em alfabetico.

n = input('Digite algo!')<br>
print(n.isalpha()) #True se sim e False se não<br>

#n = a,b,c - True<br>
#n = 3a - False<br>

--- ---


### O metodo isalnum(), retorna se é possivel converter o valor colocado em alfabetico e numerico.

n = input('Digite algo!')<br>
print(n.isalanum()) #True se sim e False se não<br>

n = a,b,c - True<br>
n = 3a - True<br>
n = " " - False<br>
