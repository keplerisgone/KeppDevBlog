---
Created: 2023-10-29T18:52
Parent item:
  - "[[The Continuous-tIme Fourer Transform]]"
---
## Recall

![[Screenshot_2023-10-29_at_6.53.32_PM.png]]

## Linearity

![[Screenshot_2023-10-29_at_6.54.04_PM.png]]

적분 정의로 증명합시다.

## Time shifting

일정한 time만큼 옮기면, $e^{-jw_0t}$﻿만큼 곱해집니다.

![[Screenshot_2023-10-29_at_6.57.04_PM.png]]

## Conjugation and Conjugate Symmetry

켤레복소수를 만들면 FT에도 켤레복소수를 적용해야합니다.

![[Screenshot_2023-10-29_at_6.58.37_PM.png]]

만약 signal이 real이라면, conjugation을 진행한 값은 같습니다.

![[Screenshot_2023-10-29_at_6.59.03_PM.png]]

- both real and even
    - conjugation 한 것이 원본과 같습니다.
- both real and odd
    - pure imaginary and odd입니다.

## Differentiation

![[Screenshot_2023-10-29_at_7.06.02_PM.png]]

미분하면 위에가 내려오겠지!

## Integration

![[Screenshot_2023-10-29_at_7.06.21_PM.png]]

적분은 미분의 inverse이기 때문에 단순히 jw의 역수를 곱하는 것으로 생각해도 되지만, 적분상수의 존재를 고려해야 합니다.

## Time and Frequency Scaling

![[Screenshot_2023-10-30_at_6.03.57_PM.png]]

적분 식에서 $\tau=at$﻿를 대입해서 증명합니다.

## Duality

![[Screenshot_2023-10-30_at_6.06.37_PM.png]]

square function ↔ sink function 사이의 변환이 가능합니다.

이는 time domain, frequency domain에서 모두 마찬가지입니다.

그리고… time domain과 frequency domain 사이의 변환을 다룹니다.

![[Screenshot_2023-10-30_at_6.09.52_PM.png]]

Duality를 적용한 Differentiaion과 multiplication은 다음과 같습니다.

![[Screenshot_2023-10-30_at_6.15.35_PM.png]]

## Parseval’s Relation

단순히 말하자면 frequency domain에서의 Energy를 $2\pi$﻿로 나눈 것과 time domain에서의 Energy는 같다는 정의입니다. 증명은 conjugation을 이용한 definition으로 합니다.

![[Screenshot_2023-10-30_at_6.17.17_PM.png]]