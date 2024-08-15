---
Created: 2023-10-04T23:05
Parent item:
  - "[[Fourier Series Representation of Periodic Signals]]"
---
$x(t)$﻿가 주기 $T$﻿를 가지고, fundamental frequency $w_0$﻿를 가지고 있다고 가정해봅시다.

## Linearity

![[Screenshot_2023-10-04_at_11.09.00_PM.png]]

서로 다른 신호의 FS coefficient간에 supoerpositon이 성립합니다.

## Time Shifing

![[Screenshot_2023-10-04_at_11.13.09_PM.png]]

어떤 한 신호를 $t_0$﻿만큼 이동했을 때, 이동한 신호의 FS coefficient는 _무언가가_가 곱해집니다.

## Time reversal

![[Screenshot_2023-10-04_at_11.17.48_PM.png]]

Time을 반전시킨 신호는 FS coefficient에 $-k$﻿를 대입한 것과 같은 계수를 가집니다.

## Time Scaling

![[Screenshot_2023-10-04_at_11.22.52_PM.png]]

Time에 scaling 작업을 하면, 그만큼 주기가 줄어들고, 진동수가 늘어납니다.

## Multiplication

![[Screenshot_2023-10-04_at_11.23.40_PM.png]]

두 신호를 곱하면, 해당 신호의 FS coefficient는 두 신호의 coefficient의 convolution이 됩니다.

## Conjugation and conjugate symmetry

![[Screenshot_2023-10-04_at_11.27.20_PM.png]]

다음 조건을 만족하면 신호를 conjugation한 것의 coefficient는 $-k$﻿를 대입하고 conjugation한 것과 같습니다.

## Parseval’s Relation for CT periodic signals

![[Screenshot_2023-10-04_at_11.30.12_PM.png]]

한 신호의 average power는 FS coefficient를 모두 제곱해 더한 것과 같습니다.

## Differentiation and Integration

![[Screenshot_2023-10-10_at_7.57.14_PM.png]]