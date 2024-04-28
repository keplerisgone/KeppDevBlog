---
Created: 2023-08-31T21:57
---
라플라스 변환은 CTFT의 확장판이다!

LTI를 아직까지 기억하신다면 아시겠지만, LTI system은 원래 exponential input에 대한 system의 결과를 출력하는 것이었습니다.

여기서 $s=j\omega$﻿ 를 적용한 특수한 경우가 바로 CTFT입니다!

![[Screenshot_2023-11-15_at_9.28.52_PM.png]]

CTFT는 다음과 같은 수식으로 표현할 수 있습니다.

> $X(j\omega)=\int^\infty_{-\infty}x(t)e^{-j\omega t}dt$﻿

![[Screenshot_2023-11-20_at_4.20.14_PM.png]]

여기서 complex number $s$﻿를 생각해봅시다.

CTFT는 $s=j\omega$﻿, 즉 pure imaginary number인 경우만 생각합니다.

Laplace transform은 complex number $s$﻿인 경우로 확장하여 생각하는 transform입니다.

$s=\sigma+j\omega$﻿ 로 생각하여 식을 전개하면, $x'(t)=x(t)e^{-\sigma t}$﻿의 FT가 Laplace transform임을 증명할 수 있습니다.

따라서 수식은 다음과 같습니다.

> $X(s)=\int^\infty_{-\infty}x(t)e^{-st}dt$﻿

위의 integral을 계산할 때 convergence 조건을 만족하는 s의 범위를 ROC(Regions of convergence)라고 합니다.

LT 에서는 LT 표현식이 같아도 ROC와 같이 표현해야 합니다.

## ROC

![[Screenshot_2023-11-20_at_4.30.08_PM.png]]

ROC는 $x'(t)$﻿가 convergence하게 만드는 $s$﻿의 범위입니다.

- right sided signal → pole의 오른쪽에 region이 생깁니다.
- left sided signal → pole의 왼쪽에 region이 생깁니다.

pole과 zero

- pole은 LT에서 $x(t)e^{-\sigma t}=1$﻿를 만드는 값을 말합니다.
    - right라면 pole의 right, left라면 pole의 left
- zero는 $X(s)=0$﻿를 만드는 $s$﻿값을 말합니다.

여기서 ROC에 pure imaginary($Re =0$﻿)인 부분이 포함되지 않을 경우, 해당 신호의 CTFT는 존재하지 않습니다. → absolutly integrality

right sided signal인 경우는 causal.

stability는 jw축을 포함하는지로 결정.

## Basic Laplace Tranform Pairs

![[Screenshot_2023-11-20_at_4.38.07_PM.png]]

그냥 계산해.

## Inverse Laplace Transform

증명은 니가 알아서….가 아니라 교재에 나와있어용

![[Screenshot_2023-11-20_at_4.40.38_PM.png]]

$\sigma$﻿는 ROC에 포함되어야 합니다.

또한 Inverse를 진행할 때 가능한 경우의 ROC를 고려하여 Inverse LT 를 진행해야 합니다.

그리고 가장 중요한 것은 내가 아는 폼으로 나누어서 변환하는 것

## Properties of the LT

![[Screenshot_2023-11-20_at_4.43.17_PM.png]]

ROC 범위 중요!!

## LT of elementary Function

![[Screenshot_2023-11-20_at_4.43.40_PM.png]]

## Summary

![[Screenshot_2023-11-20_at_4.44.50_PM.png]]