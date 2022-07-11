# Utilizando Modulos em Python

## Oque são modulos em Python?
Primeiro precisamos entender oque são os modulos:
Os modulos são como acessorios para o python, o python inicalmente vem limpo, com apenas as ferramentas necessarias para serem executadas. Dai vem os modulos, que são como complementos, Estes modulos em python são chamados de bibliotecas.
<br>
<br>
Podemos entender os modulos da seguinte forma, digamos que o nosso corpo seja a linguagem e as comidas, bebidas e doces sejam os modulos.
<br>
<br>
Da mesma forma em que durante o dia necessitamos inserir estes alimentos em nosso corpo, assim são os modulos, nós só inserimos eles mediante a necessidade.
<br>
<br>
Trazendo para a programação isso é chamado de importação de bibliotecas.
<br>
<br>
Vou agora para um exemplo prático! Digamos que eu tenha estas três "bibliotecas".
- **Comida**.
	- Hambuguer
  - Pizza
  - Hot dog
  - Sopa
<br>
- **Bebida**.
	- Milkshake
  - Coca-cola
  - Agua
<br>
- **Doces**.
	- Pudim
  - Arroz doce
  - Torta
  - Bolo
<br>
Para eu importar qualquer destas bibliotecas eu uso o seguinte comando:
~~~python
import comida
~~~
  <br>
Desta forma o python irá importar todas as comidas desta biblioteca.
<br>
Para utilizarmos as bibliotecas eu importo todas as que iremos utilizar no inicio do código.
<br>
Mas devemos entender que quando importamos alguma biblioteca, é importado tudo 
o conteúdo que há nela, mas... como fazemos se nós quisermos apenas uma funcionalidade dela?
<br><br>
Mas digamos que eu queira importar apenas o pudim da biblioteca doces, como devo fazer?
<br><br>
Basta eu utilizar o comando da seguinte forma.

~~~python
from doce import pudim
~~~
Existem duas formas básicas de importar uma biblioteca, uma forma mais generalista que é sendo bem explicito com o "import", e sendo especifico com uma funcionalidade com "from ... import ...".
--- ---
### Vamos a um exemplo prático de uma biblioteca real.
No python assim que ele é instalado juntamente com ele está incluso uma biblioteca chamada `math` que significa matematica.
<br>
Nas aulas anteriores eu aprendi os operadores básicos de matematica do python, já essa biblioteca vêem com diversas outras funcionalidades que não vêm como padrão. Desta biblioteca eu posso utilizar as seguintes funcionalidades `ceil`, `floor`, `trunc`, `pow`, `sqrt`, `factorial` que faz arredondamentos de numero flutuantes para cima.
---  ---
`ceil`: Faz arredondamento de numeros flutuates para cima.
<br>
`floor`: Faz arredondamento de numeros flutuantes para baixo.
<br>
`trunc`: Trava numeros flutuantes, não considerando a virgula/ponto
<br>
`pow`: Faz potenciação do numero indicado. Funciona semelhantemente aos 2 *
<br>
`sqrt`: Calcula raiz quadrada. (square root).
<br>
`factorial`: Faz calculo de fatorial.
<br>
<br>
E para fazer os usos destas funcionalidades basta eu fazer como apresentado acima. Usando o from import. E caso eu queira importar mais de uma funcionalidade basta eu utilizar a ",".
~~~python
from math import ceil
~~~
~~~python
from math import floor, sqrt
~~~
<br> Mas caso eu queira importar todas as funcionalidades de `math` eu só preciso importar ela.
~~~python
import math
~~~

## Prática!
~~~python
import math
num = int(input('Digite um numero: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual á {}'.format(num, raiz))
# O resultado podendo ser arrendondado para cima com o ceil.
print('A raiz de {} é igual á {}'.format(num, math.ceil(raiz)))
 ~~~
 
Desta forma importando todas as funcionalidades da biblioteca eu tenho mais recursos, mas também preciso de mais memoria.

## Metodo from import
~~~python
from math import sqrt
num = int(input('Digite um numero: '))
raiz = sqrt(num)
print('A raiz de {} é igual á {}'.format(num, raiz))
# O resultado podendo ser arrendondado para cima com o ceil.
print('A raiz de {} é igual á {}'.format(num, math.ceil(raiz)))
~~~

Desta forma eu estou impotando apenas o metodo sqrt da biblioteca math.<br>
Portanto, desta formas eu não preciso chamar math.sqrt na variavel "raiz" <br>
Basta eu utilizar apenas:<br>
raiz = sqrt(num).

## Encontrando as bibliotecas.
Para eu encontrar as bibliotexas padrões do Python, basta clicar no link abaixo.<br>
https://docs.python.org/3/library/index.html
<br>
<br>
**_Agora irei importar numeros randomicos com a biblioteca ramdom._**
<br>
Essa biblioteca gera numeros aleatorios, podemos ver ambaixo o codigo importando a biblioteca inteira.
<br>
~~~python
import ramdom
num = ramdom.ramdom()
print(num)
~~~
Desta forma ele retorna sempre um numero float aleatorio entre 0 e 1. então a resposta ficará semelhante a essa:
<br>
0.352830
<br>
<br>
Eu também posso utilizar o `randint`, que randomiza numeros inteiros, e posso passar o intervalo dos valores que preciso que ele percorra.
~~~python
import ramdom
num = ramdom.ramdint(1, 10) # Metodo randint para numeros inteiros.
print(num)
~~~
Desta forma ele fica randomizando apenas entre 1 e 10 como eu solicitei acima.
<br>
<blockquote>
Uma Dica! Se eu apertar Ctrl + Space. após digitar "import" é me retornado todas as bibliotecas instaladas e que eu posso instalar, Desta forma fica melhor para visualização das bibliotecas.<br>
Com este comando eu conseguirei verificar uma grande variedade de bibliotecas python.
</blockquote>

---
### Utilizando Bibliotecas Pypi
Mas todas estas são apenas uma parte, pois eu posso acessar o Pypi pelo proprio site da Python e ter acesso a inumeras bibliotecas.
Basta acessar o site https://pypi.org/ <br>
No Pypi diversos desenvolvedores podem criar suas proprias bibliotecas e divulgarem lá, portanto é posivel ter bibliotecas de diversos conteúdos.<br>
Vou utilizar uma chamada **emoji** para demostração, esta biblioteca tem uma funcionalidade bem simples, ela basicamente mostra emoji.<br>
Mas caso eu queira importar ela diretamente eu não coseguirei, para isso eu preciso instalar a biblioteca.
~~~bash
pip install emoji
~~~~
Desta forma eu instalo a biblioteca escolhida.<br>
Após isso basta eu importar ela em meu código.
~~~python
import emoji
~~~
Para que eu veja quais ferramentas eu consigo usar atravé da biblioteca, basta eu acessar as sheets da biblioteca em questão.<br>
Exemplo:<br>
No caso da biblioteca emoji eu busco a ***emoji-cheat-sheet*** na pagina https://www.webfx.com/tools/emoji-cheat-sheet/ <br>
Após a imoportação do modulo emoji eu posso utilizar da seguinte forma: <br>
~~~python
import emoji
print(emoji.emojize("Olá Mundo! :earth_americas:", use_aliases=True))
~~~
Desta forma eu tenmho o resultado um print na tela de "Olá Mundo!" com o emoji do globo no final.<br>
