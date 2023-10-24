# 18-08-2023


## Amplificador Inversor

    
![](https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Op-Amp_Inverting_Amplifier.svg/300px-Op-Amp_Inverting_Amplifier.svg.png)

* $G = -\frac{R_f}{R_{in}}$
* Resistência de entrada : $R_{in}$

## Amplificador Não-inversor
        

![](https://www.allaboutcircuits.com/uploads/articles/one-op-amp-two_resistors.jpg) 

* $G = 1 + \frac{R_2}{R_1}$
* $Resistência de entrada = \inf$

## Amplificador Seguidor de Tensão

![](https://www.learningaboutelectronics.com/imagens/Seguidor-de-tensao.png)

* $G = 1$
* $R_{in} = \inf$ 

## Amplificador Somador


![](https://professoreletrico.com/wp-content/uploads/2018/12/amplificador-somador-com-ampop.png)

* $V_{out} = -R_F(\frac{V_{in1}}{R_1} + \frac{V_{in2}}{R_2})$

## Esquema Amp OP

![](https://www.learningaboutelectronics.com/images/LM741_pinout_diagram.jpg)


## Problemas na diferença entre Amplificador inversor e não-inversor

Usando um divisor de tensão com um amplificador inversor:
    
![Alt text](ampop1.png)

* R3 e R4 estão em paralelo pela terra, portanto a resistência equivalente é, pela regra: 
$R_{eq} = \frac{1}{R3} + \frac{1}{R1}$, portanto a resistência não é linear, e nem o ganho.

* $ G = -\frac{R2}{Req}$

Uma maneira de se contornar isso é realizar essa montagem com um amplificador não-inversor:

![Alt text](ampop2.png)

* Nessa configuração, os resistores não estão em paralelo, portanto o crescimento é linear

# 01-09-2023

## Amplificador de Diferenças

O Amplificador de Diferenças é outra configuração de montagem com o Amp Op.

![Amplificador Diferencial](https://materiais.imd.ufrn.br/materialV2/assets/imagens/circuitos-eletronicos/circuitos_eletronicos_a10_f05_a.png)

Essa configuração, a partir de duas tensões de entrada $V_+$ e $V_-$, retorna $V_{out} =\frac{R_2}{R_1} (V_2 - V_1)$.


## Limite de Frequência do Amp Op

O Amp Op possui um limite de frequência de operação. O usado nesse caso, *LM741*, parece ter um limite que começa a aparecer a partir de 8kHz, chegando em um limite a partir de 150kHz. 
