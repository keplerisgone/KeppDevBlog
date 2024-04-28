---
Created: 2023-12-07T12:48
---
## Basic Op Amp

![[Screenshot_2023-12-09_at_7.24.49_PM.png]]

- two inputs and one input
- open-loop gain
    - 회로가 open 돼있어서 그런가
- Difference between single transistor biasing circuit (advantage)
    - high imput Impedance
    - better gain
    - mathematical operator
    - more noise insensitive
    - best amp (can stack)

## Inverting / Non-inverting Op Amp

![[Screenshot_2023-12-09_at_7.26.20_PM.png]]

- 왼쪽 그림은 $A_0 >0$﻿ → non-inverting, 부호를 바꾸지 않음
- 오른쪽은 $A_0<0$﻿ → inverting, 부호를 바꿈
    - 이 경우는 CS stage와 CE stage의 gain 부호를 바꾸기 위해서 사용할 수 있다

## simple CMOS OP-Amp

![[Screenshot_2023-12-09_at_7.27.05_PM.png]]

여기서 굳이 gain을 계산해야 하는 이유는??

output voltage is extremely high!

## Unity Gain Amplifier

- $V_{out}$﻿이 negative sign에 연결된 amp
- gain은 1보다 낮지만, $A_0$﻿은 엄청 크니까 1에 가깝다고 볼 수 있다
    - follower와 비슷하다
- voltage를 멀리까지 전달해야 할 때 쓰인다
    
    ![[Screenshot_2023-12-09_at_7.40.08_PM.png]]
    

## Noninverting Amplifier (ideal)

![[Screenshot_2023-12-09_at_8.03.15_PM.png]]

- voltage divider에 의해 저런 gain이 나온다
- closed loop gain이라고 한다
- addition의 역할을 한다
    - independent with openloop gain ($A_0$﻿)

## Noninverting Amplifier (non-ideal)

![[Screenshot_2023-12-09_at_8.03.24_PM.png]]

- $A_0$﻿에 영향을 받게 된다 - 그래도 크니까 영향은 잘 안 받음

## Inverting Amplifier

![[Screenshot_2023-12-09_at_8.03.32_PM.png]]

- positive에 0이 걸려있으니까 inverting이긴 한데
- 이 때는 저항의 비에 영향을 받는다
- scaling의 역할을 한다

## Complex Impedances Around the Op Amp

![[Screenshot_2023-12-09_at_8.03.40_PM.png]]

- 위의 inverting, scaling은 impedance에도 성립한다

## Integrator

![[Screenshot_2023-12-09_at_8.03.48_PM.png]]

- LPF에 Op-amp를 단 것이라고 생각하면 된다
    - 물론 filter는 gain이 0과 1 사이지만..
- Op-amp를 이용한 버전은 gain이 1이상일 수 있다!
- integrate를 할 수 있어요
    - 증명은 미방을 풀어서 합니다

## Differentiator

![[Screenshot_2023-12-09_at_8.03.56_PM.png]]

- HPF에 OP-amp를 단것이라고 생각한다
- 역시 gain이 1이상일 수 있다
- 증명은 미방을 풀어서…

## Nonidealities: Speed Limitation

![[Screenshot_2023-12-09_at_8.04.02_PM.png]]

- 그래도 $A_0$﻿가 무한대는 아니기에 주파수가 오를 수록 gain이 줄어드는 문제가 발생
    - roll-off
    - 가 발생하는 freq. : cut-off frequency = open loop break point
    - 정확히는 -20dB가 됐을 때 (dB = $20\log(V_o/V_i)$﻿)
- band width를 늘리려면….
    
    - open-loop gain을 closed-loop gain으로 만든다