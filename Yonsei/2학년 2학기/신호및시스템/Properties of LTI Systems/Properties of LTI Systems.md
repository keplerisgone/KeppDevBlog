---
Created: 2023-09-20T19:56
Parent item:
  - "[[Linear Time-Invarient Systems]]"
---
모든 성질은 impulse response $h(t)$﻿ (or $h[n]$﻿) 에 의해서 결정됩니다.

## Commutative property

![[Media/Untitled 44.png|Untitled 44.png]]

변수 치환을 이용합니다.

## Distributive property

![[Media/Untitled 1 33.png|Untitled 1 33.png]]

분배법칙이 성립합니다.

## Associative property

![[Media/Untitled 2 32.png|Untitled 2 32.png]]

결합법칙 또한 성립합니다. impulse response에 대해서도 성립합니다. non-linear한 시스템들에 대해서만 성립하지 않는다는 것을 알아둡시다.

### Memoryless

메모리가 필요없어.

## Invertibility

![[Media/Untitled 3 31.png|Untitled 3 31.png]]

역 시스템을 구할 수 있는지 여부입니다. 위의 그림 하나만 머리에 박아놓읍시다.

### time shift

> $y(t)=x(t-t_0), h(t)=\delta(t-t_0)$﻿

나중에 밥먹듯이 쓰이는 signal shift 입니다. 잘 기억해 둡시다.

이를 이용해 다음을 도출할 수 있습니다.

> $x(t-t_0)=x(t)\ * \ \delta(t-t_0)=x(t)\ * \ h(t),$﻿

inverse system $h_1(t)$﻿는

> $h_1(t)\ *\ h(t) = \delta(t-t_0)\ * \ \delta(t+t_0)=\delta(t)$﻿

inverse system과 일반 system의 convolution 결과는 impulse function이 나와야 합니다. ($x(t)\ * \ \delta(x)=x(t)$﻿니깐요)

## Causality

![[Media/Untitled 4 24.png|Untitled 4 24.png]]

과거와 현재의 signal 값에만 system이 의존하는지의 여부입니다. _미래의 signal 값을 요구하지 않음_입니다.

단순히 $h(t)$﻿, $h(n)$﻿들이 왼쪽에 값이 있냐 없느냐를 판단하면 됩니다.

수학적으로 생각해보면 $h$﻿가 음수쪽에 값을 가질 경우 convolution sum에서는 $n+a(a>0)$﻿까지 더해야 하기 때문이고, integral에서도 마찬가지입니다.

그냥 기하학적으로 생각해보면 $h$﻿를 뒤집어서 계산할 때 더 미래로 가서 계산해야 모든 $y$﻿를 구할 수 있습니다.

## Stability (BIBO Stability)

![[Media/Untitled 5 20.png|Untitled 5 20.png]]

Bounded in, Bounded Out, 증명 논리만 알아두면 딱히 상관없을 것 같습니다.

### Unit Step Response of an LTI System

![[Screenshot_2023-09-25_at_7.16.03_PM.png]]

stability, causuality와 관련,

$x[n]=u[n]$﻿을 집어넣었을 때 뭐가 나올까? 라는 아이디어, $s[n]$﻿는 $u[n]$﻿와 $h[n]$﻿의 convolution sum.