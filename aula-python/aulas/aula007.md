# Operadores aritimeticos

(+) - Adição<br>
(-) - Subtração<br>
(*) - Multiplicação<br>
(/) - Divisão<br>
(**) - Potencia/exponenciação<br>
(//) - Divisão inteira<br>
(%) - Modulo/Resto da divisão<br>


 --- ---
 ## Usando os operadores

print(5 + 2)  # 7<br>
print(5 - 2)  # 3<br>
print(5 * 2)  # 10<br>
print(5 / 2)  # 2.5<br>
print(5 ** 2)  # 25 #Elevado ao quadrado<br>
print(5 // 2)  # 2<br>
print(5 % 2)  # 1<br>

 --- ---
## Ordem de precedencia/impotancia das somas

 1 - ()<br>
 2 - **<br>
 3 - *, /, //, %<br>
 4 - +, -<br>


## Exemplos

print(5 + 3 * 2)  # 11, pois a ordem de precedencia começa com a multiplicação<br>
print(3 * 5 + 4 ** 2)  # 31<br>
print(3 * (5 + 4) ** 2)  # 243<br>


## Praticas

print(5 + 4)<br>
print(5 ** 2)  # ao quadrado<br>
print(5 ** 3)  # ao cubo<br>
print(pow(4, 3))  # outra forma ao cubo, mas eu perco a ordem de precedencia<br>
print(19 // 2)<br>
print(19 / 2)<br>
print(19 % 2)<br>
print((30 + 10) * 4 / 5)<br>

## para eu calcular raiz quadrada ou cubuca

print(81**(1/2))  # RAIZ QUADRADA - eu calculando o valor final dividido por meio eu encontro a raiz quadrada, mas devo seguir a ordem de precedencia<br>
print(127**(1/3))  # RAIZ CUBICA

## Usando operador (*) com strings

print("olá" * 5)  # retorna olá 5x


## Alguns macetes

nome = input('Digite um nome:')<br>
print('prazer em te conhecer {:=^20}!'.format(nome))<br><br>
Desta forma ele coloca o nome em 20 caracteres alinhado ao meio com os sinais de = antes e depois o nome, podendo ser usado > para alinhar a direita e < para alinhas a esquerda


numero_1 = int(input('Digite um valor:'))<br>
numero_2 = int(input('digite outro numero:'))<br>

soma = numero_1 + numero_2<br>
divi = numero_1 / numero_2<br>
mult = numero_1 * numero_2<br>
divi_int = numero_1 // numero_2<br>
divi_res = numero_1 % numero_2<br>
expo = numero_1 ** numero_2<br>

Para eu quebrar linha em python eu uso (\n) e para continuar na linha, eu vou no fim do código e coloco (end='').<br>
print('A soma entre os valores escolhidos é {}\n, a divisão é {}\n e a multiplicação é {:.3f}'.format(soma, divi, mult))<br>
print('O resultado da divisão inteira dos numeros escolhidos é {0}\n, o resto da divisão é {1} \ne a exponenciação é {2}'.format(divi_int, divi_res, expo)).<br>
