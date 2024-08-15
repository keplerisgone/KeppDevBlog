---
Created: 2023-09-08T21:01
Parent item:
  - "[[Introduction & Review of Basic Circuit theory]]"
---
Ohm’s Law

Kirchhoff’s Laws

Kirchhoff’s Current Law (KCL)

Kirchhoff’s Voltage Law (KVL)

Node-Voltage method

Thevenin & Norton Equivalents

Thevenin Equivalents

Norton Equivalents

Source Transformation

Capacitor

Inductor

RLC Circuit

General solution

RLC circuit

> [!important]  
> Passive/Active Devices의 정의가 무엇인가요  

## Ohm’s Law

> $V=IR$﻿

- Passive sign convention
    
    ![[Screenshot_2023-09-08_at_9.08.36_PM.png]]
    
    한 번 sign을 고정하면 계속 고정할 수 있다
    

## Kirchhoff’s Laws

### Kirchhoff’s Current Law (KCL)

![[Screenshot_2023-09-08_at_9.09.39_PM.png]]

대충 하나의 노드에서 오고가는 전류의 합은 0이라는 뜻

### Kirchhoff’s Voltage Law (KVL)

![[Screenshot_2023-09-08_at_9.12.33_PM.png]]

하나의 Mesh current에 의한 voltage의 합은 0이다.
	오해의 소지가 좀 있는데, *하나의 mesh current*라기 보다는 한 바퀴로 보는게 낫다

## Node-Voltage method

일단 Node-Voltage equations는 찾고자 하는 변수의 개수 - 1 개만 있으면 모든 변수를 찾아낼 수 있습니다.

![[Screenshot_2023-09-08_at_9.20.39_PM.png]]

> [!important]  
> planar/nonplanar 의 정의는 무엇인가요  

## Thevenin & Norton Equivalents

이 둘은 동치인 회로를 뜻합니다. 정확한 정의는 해당 자리에 해당 회로를 끼워도 동일한 역할을 수행할 수 있는 회로르 뜻합니다. 이들은 소스 하나와 저항 하나로 이루어져 있습니다.

### Thevenin Equivalents

Voltage Source로 바꾸는 회로

![[Screenshot_2023-09-08_at_9.32.01_PM.png]]

### Norton Equivalents

Current Source로 바꾸는 회로

![[Screenshot_2023-09-08_at_9.34.11_PM.png]]

### Source Transformation

![[Screenshot_2023-09-08_at_9.36.25_PM.png]]

대충 잘 바꾸면 된다는 뜻

## Capacitor

![[Screenshot_2023-09-08_at_9.39.23_PM.png]]

Capacitor는 떨어진 두 개의 얇은 판으로, 전압이 변화하면 전류가 흐르는 소자입니다.

Capacitor의 Power는 $v(t)i(t)$﻿로 나타나고, 에너지는 power를 시간에 대해 적분한 형태이므로, $\int^t_0p(t)dt=\frac{1}{2}Cv(t)^2$﻿ 로 나타납니다. 증명은 니가 손으로 써보세요.

![[Screenshot_2023-09-08_at_9.40.52_PM.png]]

## Inductor

capacitor와의 차이점을 중점으로 알아봅시다.

![[Screenshot_2023-09-08_at_9.41.51_PM.png]]

Capacitor는 자기장을 이용해 전기에너지를 저장하고, inductor는 전류를 이용해 자기 에너지를 저장합니다. open/short circuit의 차이도 볼만 합니다.

## RLC Circuit

RLC 회로에 KCL, KVL을 적용하여 ODE를 풀면 전류/전압을 쉽게 구할 수 있습니다.

RL circuit

![[Screenshot_2023-09-08_at_9.53.34_PM.png]]

![[Screenshot_2023-09-08_at_9.53.55_PM.png]]

RL circuit

![[Screenshot_2023-09-08_at_9.54.27_PM.png]]

### General solution

![[Screenshot_2023-09-08_at_9.54.44_PM.png]]

차라리 공수를 복습하십시오

### RLC circuit

RLC부터는 ODE가 second-order입니다.

![[Screenshot_2023-09-08_at_10.04.08_PM.png]]

또한 voltage source가 periodic 할 경우에는 해 또한 파동의 형태로 바뀝니다. 다만 R을 추가했을 경우에는 voltage가 수렴합니다. 이것도 사실 $t>\infty$﻿ 일 때 priodic한 부분이 사라져서 그렇긴 합니다.