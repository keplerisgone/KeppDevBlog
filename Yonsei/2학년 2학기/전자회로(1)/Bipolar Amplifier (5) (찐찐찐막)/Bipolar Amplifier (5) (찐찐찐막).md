---
Created: 2023-11-16T23:59
---
## Ideal Current Source

![[Screenshot_2023-11-17_at_12.17.27_AM.png]]

Ideal current source의 가장 큰 특징은 일정한 전류를 내보내면서, output impedance가 무한이라는 점입니다!

## Boosting the Output Impedance

![[Screenshot_2023-11-17_at_12.25.03_AM.png]]

emitter degeneration 등 다양한 biasing은 output impedance를 낮춰 gain을 높이는 역할을 하지만, headroom 이 줄어들어 saturation에 빠질 위험성이 높습니다.

## Cascode stage

![[Screenshot_2023-11-17_at_12.27.42_AM.png]]

왜 쓰냐

- $V_{b2}$﻿가 constant이므로 $V_{C2}$﻿가 constant, headroom issue가 사라집니다.
- 저항보다 작은 공간을 차지한다.

![[Screenshot_2023-11-17_at_12.34.33_AM.png]]

또한 base-emitter voltage가 상수이므로 하나의 저항처럼 취급할 수 있습니다.

## Maximum output Impedance

![[Screenshot_2023-11-17_at_12.35.33_AM.png]]

그리고 $r_{O2}$﻿가 아무리 높아도 $r_{\pi1}$﻿에 의해 output impedance가 조절됩니다.

## PNP Cascode Stage

![[Screenshot_2023-11-17_at_12.50.11_AM.png]]

- PNP를 쓰는 이유
    - $g_m$﻿과 $V_A$﻿가 낮아서 안전

## Diode-Connected Device

![[Screenshot_2023-11-17_at_12.56.34_AM.png]]

> [!important]  
> 이게 뭐임  

## False Cascodes

![[Screenshot_2023-11-17_at_12.57.50_AM.png]]

Emitter와 Emitter를 연결하면 cascode가 아니게 됩니다.

## Short-Circuit Transconductance

![[Screenshot_2023-11-17_at_1.02.27_AM.png]]

어떤 회로에서의… $i_{out}/v_{in}$﻿을 저거라고 한다.

single BJT configuration에서 저것은 $g_m$﻿이다

## Voltage Gain of a Linear Circuit

![[Screenshot_2023-11-17_at_1.05.24_AM.png]]

등가회로를 보면 $v_{out}=-i_{out}R_{out}=-G_{m}v_{in}R_{out}$﻿이고,

$A_v=-G_mR_{out}$﻿

## Determination of Voltage Gain

![[Screenshot_2023-11-17_at_1.08.54_AM.png]]

그냥 공식적용

## Comparison of CE and Cascode Stages

![[Screenshot_2023-11-17_at_1.13.13_AM.png]]

좋다~

## Voltage Gain of Cascode Amplifier

![[Screenshot_2023-11-17_at_1.16.14_AM.png]]

## Practical Cascode Stage

![[Screenshot_2023-11-17_at_1.17.18_AM.png]]

하지만 current source에서는 output impedance가 무한대가 아니기 때문에 다음과 같이 나타납니다.

## Improved Cascode Stage

![[Screenshot_2023-11-17_at_1.22.40_AM.png]]

계속 위로 쌓으면 gain이 올라갑니다

## Cascode Stage Rout

![[Screenshot_2023-11-17_at_1.27.18_AM.png]]