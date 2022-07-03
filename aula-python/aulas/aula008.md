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
- **Bebida**.
	- Milkshake
  - Coca-cola
  - Agua
- **Doces**.
	- Pudim
  - Arroz doce
  - Torta
  - Bolo
<br>
Para eu importar qualquer destas bibliotecas eu uso o seguinte comando:
<br>
`import comida`
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
<br>
`from doce import pudim`
<br><br>
Existem duas formas básicas de importar uma biblioteca, uma forma mais generalista que é sendo bem explicito com o "import", e sendo especifico com uma funcionalidade com "from ... import ...".
<br><br>
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
<br>
`from math import ceil`
<br>
`from math import floor, sqrt`
<br> Mas caso eu queira importar todas as funcionalidades de `math` eu só preciso importar ela.
<br>
`import math`.
## Prática!
<code>
import math
num = int(input('Digite um numero: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual á {}'.format(num, raiz))
# O resultado podendo ser arrendondado para cima com o ceil.
print('A raiz de {} é igual á {}'.format(num, math.ceil(raiz)))
 </code>
 Desta forma importando todas as funcionalidades da biblioteca eu tenho mais recursos, mas também preciso de mais memoria.
 <br>

