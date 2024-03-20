# Sistemas Digitais - Combinacionais e Sequenciais

## Eletronica Digital - Expressões Booleanas

    NOTA #1
    A + B (OU)
    A * B (E)

* **NOT gate**

![](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Not-gate-en.svg/1200px-Not-gate-en.svg.png)

|  A | Ā |
|----|---|
|  0 | 1 | 
|  1 | 0 | 


* AND gate

![](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Logic-gate-and-us.svg/2000px-Logic-gate-and-us.svg.png)

|  A | B |  A * B|
|----|---|-------|
|  0 | 0 |    0  |
|  0 | 1 |    0  |
|  1 | 0 |    0  |
|  1 | 1 |    1  |

* **OR gate**

![](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Or-gate-en.svg/1280px-Or-gate-en.svg.png)

|  A | B |  A * B|
|----|---|-------|
|  0 | 0 |    0  |
|  0 | 1 |    1  |
|  1 | 0 |    1  |
|  1 | 1 |    1  |

* **XOR gate**

![](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Xor-gate-en.svg/2560px-Xor-gate-en.svg.png)

|  A | B |  A * B|
|----|---|-------|
|  0 | 0 |    0  |
|  0 | 1 |    1  |
|  1 | 0 |    1  |
|  1 | 1 |    0  |

* **NAND gate**

![](https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/Nand-gate-en.svg/2000px-Nand-gate-en.svg.png)


|  A | B |  A * B|
|----|---|-------|
|  0 | 0 |    1  |
|  0 | 1 |    1  |
|  1 | 0 |    1  |
|  1 | 1 |    0  |


### Identidades 

* Comutatividade:

$$A + B = B + A$$

* Associatividade:
$$(A + B) + C = A + (B + C)$$

* Distributividade

$$A\cdot (B + C) = A \cdot B + A \cdot C$$

* De Morgan

$$\overline{A \cdot B} = \overline{A} + \overline{B}$$

$$\overline{A + B} = \overline{A} \cdot \overline{B}$$

* Expressões Auxiliares

### Mapa de Karnaugh

[Karnaugh Map, Wikipedia](https://en.wikipedia.org/wiki/Karnaugh_map)

[Vídeo sobre o Mapa de Karnaugh](https://www.youtube.com/watch?v=xB99jX9QMOE)

## Prática

Para essa prática, foram usados três circuitos integrados, o *SN7402*, *SN7404* e o *SN7408*, para montar, a partir do vídeo abaixo, um circuito de um display de 2 bits.

[Vídeo sobre a prática do display de 7 segmentos](https://www.youtube.com/watch?v=_fl-PbZxvhs)

![Circuitos Integrados Booleanos](imagens/bool_circuits.png)

Abaixo, o circuito final:

![Prática do Display](imagens/pratica-display.png)

## Contador Combinacional

A estrutura anterior funciona, porém funciona apenas para dois bits, e sua escalabilidade não é muito efetiva, dependendo de um grande espaço para alocar mais bits. 

Para solucionar isso, existe um circuito integrado, o **TC4511BP**, que acumula todo o circuito acima em um único chip, com entradas para até 4 bits. Abaixo, o circuito foi feito com esse circuito 

![Alt text](imagens/combinacional.png )

## Contador Sequencial
l
![](imagens/contador_sequencial.gif)

![7490 pinout](imagens/7490_pinout.png)

## 555

O 555 funciona a base de dois comparadores. Ele começa o carregamento de um capacitor por dois resistores, até chegar em um ponto que, ao ser colocado em um comparador, faz com que o 555 mude o ponto de comparação para o segundo comparador, que então é novamente carregado, seguindo o mesmo processo. Esse carregamento e descarregamento sucessivo pelos dois comparadores gera esse comportamento oscilatório. 

### Astável

Uma das configurações do 555 é a configuração astável:

![Alt text](imagens/astavel_555.png)


O pinout de um 555 é:

![Alt text](imagens/555_pinout.png)

Abaixo, um circuito montado com 555 em configuração astável:

![](imagens/555_circuito.gif)

### Monoestável

Também foi feita a montagem *monoestável*:

![Alt text](imagens/555_mono.png)

Nessa montagem, o contador incrementa quando se é apertado o botão.

![Alt text](imagens/555_mono_circuito.png)
