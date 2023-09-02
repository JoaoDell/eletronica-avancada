# Relatório Aula 18-08

A aula de 18/08 teve como tarefa introduzir conceitos básicos da montagem de circuitos com Amplificadores Operacionais, também chamados de Amp Ops. Amplificadores Operacionais tem como consequência de uso a amplificação, de acordo com um fator $G$, da diferença entre dois sinais de entrada $V_{+}$ e $V_{-}$, pela seguinte regra:

$$V_{out} = G(V_{+} - V_{-})$$

Apropriando-se dessa regra e se utilizando dos mais variados componentes, é possível fazer inúmeras montagens com efeitos diferentes. Nessa aula, trabalhou-se a montagem de **quatro** circuitos amplificadores:

* Inversor
* Não-inversor
* Seguidor de Tensão
* Somador

A seguir, uma descrição dos circuitos e suas características.

## Amplificador Inversor

O circuito amplificador inversor, o qual tem a seguinte configuração:



Tem como principal resultado a amplificação da tensão de entrada, porém com uma inversão de sinal. Esse circuito possui as seguintes características:

* $G = -\frac{R_2}{R_1}$
* $R_{in} = R_1$

## Amplificador Não-inversor

O circuito amplificador não-inversor, o qual tem a seguinte configuração:


Tem o mesmo efeito de amplificação do anterior, porém sem a inversão do sinal. Esse circuito possui as seguintes características:

* $G = 1 + \frac{R_2}{R_1}$
* $R_{in} = \inf$

## Amplificador Seguidor de Tensão

O circuito Seguidor de Tensão

* $G = 1$
* $R_{in} = \inf$ 

## Amplificador Somador

O circuito Somador, que tem a configuração abaixo, tem como consequência uma tensão de saída $V_{out}$ que é a soma de uma série de tensões de entrada $V_{i}$.

Esse circuito possui as seguintes características:

* $V_{out} = -R2(\frac{V_{in1}}{R_1} + \frac{V_{in3}}{R_3})$

## Esquema Amp OP

Um modelo de Amp Op amplamente usado é o *LM741*. Esse modelo possui a seguinte configuração, de acordo com seu [datasheet](https://www.ti.com/product/LM741?utm_source=google&utm_medium=cpc&utm_campaign=asc-null-null-GPN_EN-cpc-pf-google-wwe&utm_content=LM741&ds_k=LM741&DCM=yes&gclid=Cj0KCQjwl8anBhCFARIsAKbbpyRzscwE3QhwxczKOPpnxIKsg2oaLicwu4Jt7w2XJUlao5dN3vT-nDQaAl6YEALw_wcB&gclsrc=aw.ds):

![Pinagem do LM741](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/LM741_Pinout_Square-it.svg/2560px-LM741_Pinout_Square-it.svg.png)

## Problemas na diferença entre Amplificador inversor e não-inversor

Usando um divisor de tensão com um amplificador inversor:



* R3 e R4 estão em paralelo pela terra, portanto a resistência equivalente é, pela regra: 
$R_{eq} = \frac{1}{R3} + \frac{1}{R1}$, portanto a resistência não é linear, e nem o ganho.

* $ G = -\frac{R2}{Req}$

Uma maneira de se contornar isso é realizar essa montagem com um amplificador não-inversor:

* Nessa configuração, os resistores não estão em paralelo, portanto o crescimento é linear