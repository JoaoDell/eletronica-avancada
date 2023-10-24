# 15-09-2023

## Filtros 

Filtros são condicionadores de sinal que bloqueiam frequências não desejadas. São úteis para filtrar sinais de entrada para leitores digitais, entre outras coisas.

* **Passa-baixa** (PB ou BP): Passa apenas frequências baixas.
* **Passa-alta** (PA ou HP): Passa apenas frequências altas.
* **Passa-frequência** (PF ou BP): Passa apenas uma faixa de frequências  específica desejada.
* **Rejeita-frequência** (RF ou BR): Refeita apenas uma faixa de frequências específica desejada.

```
    NOTA #1

    A impendância é uma generalização do conceito da resistência, levando em consideração a fase que um sinal de saída ganha em relação à entrada. Ela é definida como: 
    Z = R + iX 
        * R : Resistência
        * X : Reatância  
        * Reatância em um indutor: iwL
        * Reatância em um capacitor: 1\iwC
        * Entende-se reatância como uma fase adicionada à corrente, enquanto a resistência é um limitador.
```

A frequência de corte geralmente é escolhida como a frequência a qual houve queda de tensão igual a $-3dB$:

![Queda de um filtro passa-baixa](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/Butterworth_response.png/350px-Butterworth_response.png)

O ganho, representado em decibéis ($dB$), é dado por:

$G = 10log(\frac{P_o}{P_i})$

Que pode ser reescrito em função das tensões de entrada e saída como:

$G = 10log((\frac{V_o}{V_i})^2)$

$G = 20log(\frac{V_o}{V_i})$

No caso de $-3dB$:

$G = -3 = 20log(\frac{V_o}{V_i})$

$\frac{-3}{20} = -0.15 = log(\frac{V_o}{V_i})$

$10^{-0.15} = 0.7 = \frac{V_o}{V_i}$

A queda de tensão não é íngreme, e sim uma rampa: Porém, existem níveis de filtros que intensificam a inclinação da queda dos filtros.

![Níveis de filtros](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Butterworth_orders.png/350px-Butterworth_orders.png)

* Filtro de primeira ordem: $-20\frac{dB}{Dec}$
* Filtro de segunda ordem: $-40\frac{dB}{Dec}$

É possível também colocar filtros em série para intensificar a inclinação, ao invés de usar filtros de ordem diferente, apesar de isso não transformar esse conjunto em um conjunto de segunda ordem. Um jeito de mitigar isso e isolar dois filtros em série é colocar um AmpOp seguidor de tensão, que tem impedância infinita, entre eles.

```
    NOTA #2
    Componentes passivos: componentes que não são alimentados separadamente. Como exemplo, existem os capacitores, resistores.

    Componentes ativos: componentes que são alimentados separadamente. Como exemplo, existe o amplificador operacional.
```

## RC

Filtro passa baixa mais comum.

![Filtro passa-baixa](https://upload.wikimedia.org/wikipedia/commons/e/e7/Low_pass_filter.png)

# 22-09-2023

## Filtro Passa-Frequência

* L = 1 uH
* R = 1 kO
* C = 10 nF

$f_{Res}$ =  1.75 MHz

Frequência de passagem: $1.5 MHz < f < 1.9 MHz$

* C = 100 nF

$f_{Res}$ =  520 kHz 

Frequência de passagem: $477 kHz < f < 557 kHz$


* C = 220 nF

$f_{Res}$ =  345 kHz 

Frequência de passagem: $298 kHz < f < 376 kHz$

## Filtro Rejeita-Frequência

* L = 1 uH
* R = 1 kO
* C = 220 nF

$f_{queda}$ =  700 Hz

Frequência de passagem: $700 Hz < f$


    