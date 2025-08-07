## Otimização de Código

- Substitui segmentos de código ineficientes e as substitui por instruções eficientes

	- Eliminação de desvios e branches redundantes / inalcançáveis.
	- Eliminação de recursos não utilizados, como variáveis, funções, rótulos não referenciados, etc.
	- Simplificação de códigos redundantes
	- Simplificação de expressões e propriedades algébricas

1. Otimize os códigos intermediários a seguir apresentando as heurísticas utilizadas em cada caso
## Geração e Código Alvo

- Assembly: linguagem de montagem
- Assembler: transforma a linguagem de montagem em linguagem de máquina
- Linker


## Perguntas





(FCC, 2019) Um compilador está verificando se uma variável foi declarada somente uma vez, se foi declarada antes do seu primeiro uso, se foi declarada e nunca foi usada e se os tipos de dados em uma expressão aritmética são compatíveis. Essas verificações são realizadas na fase de)

- ANALISE SEMANTICA


(AOCP, 2018) O compilador é o programa responsável por traduzir o código-fonte de uma linguagem de programação de alto nível para uma linguagem de programação de baixo nível. Sobre o compilador e as etapas realizadas por esse programa, analise as assertivas e assinale a alternativa que aponta a(s) correta(s).

  

I. A etapa de análise léxica tem como função a identificação dos elementos componentes do programa, os também chamados símbolos léxicos.

  

II. A etapa de análise sintática visa determinar se o conjunto de símbolos léxicos encontrados pertencem à gramática da linguagem de programação.

  

III. A etapa de análise semântica tem como objetivo verificar se a execução do programa faz sentido para o usuário.

  

IV. A etapa de otimização de código realiza a síntese do código escrito pelo programador, visando a uma melhora de desempenho na execução do programa.


- I e II


(SUGEP – UFRPE, 2018) Durante a compilação de um código-fonte, a fase do compilador que é responsável por produzir uma sequência de _tokens_ é a:

- Análise Léxica

(CESPE – CEBRASPE, 2013 - adaptada) Considere a gramática a seguir:

S -> S + S | S - S | 0 | 1 | ... | 9 e S como o único símbolo não terminal.

Nessa situação, a expressão 7 – 4 + 3 possibilita a criação de quantas árvores de derivação distintas?

- 2

(FCC, 2016) A compilação é o processo de tradução de um programa escrito em uma linguagem fonte em um programa equivalente em linguagem de máquina. Nesse processo, o programa fonte normalmente passa pelas fases:

  

I. Identificação de sequências de caracteres de entrada e produção de uma sequência de elementos de saída, os _tokens_. Nesta fase, verifica-se se cada caractere do programa fonte pertence ao alfabeto da linguagem, identificando os _tokens_ e desprezando comentários e espaços em branco. Os _tokens_ constituem classes de símbolos, tais como palavras reservadas, delimitadores, identificadores etc.

  

II. Identificação de sequências de símbolos que constituem estruturas como expressões e comandos, através de uma varredura, ou _parsing_, da representação interna do programa fonte, produzindo uma estrutura em árvore, chamada árvore de derivação.

  

III. Verificação das estruturas quanto ao sentido, ou seja, se o programa não possui erros de significado. Por exemplo, verifica se um identificador declarado como variável é utilizado como tal, se existe compatibilidade entre operandos e operadores em expressões etc.

  

Os itens I, II e III referem-se, correta e respectivamente, às fases:


- Lexica, Sintatica e Semantica

I - A técnica de eliminação de código morto é uma importante estratégia de otimização utilizada por compiladores

  

**PORQUE**

  

II - A eliminação de código morto remove instruções e blocos de código que nunca são executados, reduzindo o tamanho do código e melhorando a eficiência do programa.


- I e II estao corretas e a II e uma explicacao da II


Em relação ao método LL(1) de análise sintática usando a tabela M, qual das seguintes afirmações é verdadeira?

- O método LL(1) usa uma pilha para auxiliar na análise sintática do código-fonte.

Considere o código a seguir escrito em C:

  

int main() {

     int number@;

     number@ = 10;

     printf("%d\n", number@);

     return 0;

 }

  

O erro presente nesse código será identificado em qual etapa do processo de compilação?

- Analise Lexica


Considere o código a seguir escrito em C:

  

int main() {

     int a = 5

     printf("%d\n", a);

     return 0;

 }

  

O erro presente nesse código será identificado em qual etapa do processo de compilação?

- Analise Sintatica

Considere o código a seguir escrito em C:

  

int main() {

     int a = 5;

     char b = 'A';

     printf("%d\n", a + b);

     return 0;

 }

  

O erro presente nesse código será identificado em qual etapa do processo de compilação?

- Analise Semantica