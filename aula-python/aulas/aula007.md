# Operadores aritimeticos
~~~python
(+) - Adição
(-) - Subtração
(*) - Multiplicação
(/) - Divisão
(**) - Potencia/exponenciação
(//) - Divisão inteira
(%) - Modulo/Resto da divisão
~~~
 --- ---
 ## Usando os operadores
~~~python
print(5 + 2)  # 7
print(5 - 2)  # 3
print(5 * 2)  # 10
print(5 / 2)  # 2.5
print(5 ** 2)  # 25 Elevado ao quadrado
print(5 // 2)  # 2
print(5 % 2)  # 1
~~~
 --- ---
## Ordem de precedencia/impotancia das somas

 1 - ()<br>
 2 - **<br>
 3 - *, /, //, %<br>
 4 - +, -<br>


## Exemplos
~~~python
print(5 + 3 * 2)  # 11, pois a ordem de precedencia começa com a multiplicação
print(3 * 5 + 4 ** 2)  # 31
print(3 * (5 + 4) ** 2)  # 243
~~~

## Praticas
~~~python
print(5 + 4)
print(5 ** 2)  # ao quadrado
print(5 ** 3)  # ao cubo
print(pow(4, 3))  # outra forma ao cubo, mas eu perco a ordem de precedencia
print(19 // 2)
print(19 / 2)
print(19 % 2)
print((30 + 10) * 4 / 5)<br>
~~~
## para eu calcular raiz quadrada ou cubica
~~~python
print(81**(1/2))  # RAIZ QUADRADA - eu calculando o valor final dividido por meio eu encontro a raiz quadrada, mas devo seguir a ordem de precedencia
print(127**(1/3))  # RAIZ CUBICA
~~~
## Usando operador (*) com strings
~~~python
print("olá" * 5)  # retorna olá 5x
~~~
## Alguns macetes
~~~python
nome = input('Digite um nome:')
print('prazer em te conhecer {:=^20}!'.format(nome))
~~~
Desta forma ele coloca o nome em 20 caracteres alinhado ao meio com os sinais de = antes e depois o nome, podendo ser usado > para alinhar a direita e < para alinhas a esquerda
~~~python
numero_1 = int(input('Digite um valor:'))
numero_2 = int(input('digite outro numero:'))

soma = numero_1 + numero_2
divisao = numero_1 / numero_2
multiplicacao = numero_1 * numero_2
divi_inteira = numero_1 // numero_2
divi_resto = numero_1 % numero_2
exponenciacao = numero_1 ** numero_2
~~~
Para eu quebrar linha em python eu uso (\n) e para continuar na linha, eu vou no fim do código e coloco (end='').
~~~python
print('A soma entre os valores escolhidos é {}\n, a divisão é {}\n e a multiplicação é {:.3f}'.format(soma, divi, mult))
print('O resultado da divisão inteira dos numeros escolhidos é {0}\n, o resto da divisão é {1} \n e a exponenciação é {2}'.format(divi_int, divi_res, expo))
~~~
