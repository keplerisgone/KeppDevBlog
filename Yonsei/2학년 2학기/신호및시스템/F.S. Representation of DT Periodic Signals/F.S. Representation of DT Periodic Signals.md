---
Created: 2023-10-09T16:11
Parent item:
  - "[[Fourier Series Representation of Periodic Signals]]"
---
이제는 DT Signal을 FS로 나타내봅시다.

## Linear Combinations of Harmonicaly Related Complex Exponentials

![[Screenshot_2023-10-09_at_4.23.35_PM.png]]

Recall, DT의 Harmonical은 다음과 같이 표현할 수 있습니다.

> $\phi_k[n]=e^{jkw_0n}=e^{jk(2\pi/N)n}$﻿

## General Periodic Sequences

CT signal 또한 Fundamental Frequency가 동일한 주기 함수의 합이었던 만큼, DT signal도 동일한 방식으로 나타냅니다.

> $x[n]=\sum_ka_k\phi_k[n]=\sum_ka_ke^{jkw_0n}$﻿

![[Screenshot_2023-10-09_at_4.23.43_PM.png]]

또한 DT는 CT와 달리 Finite Sum으로 표시됩니다. 어차피 $N$﻿이상으로 가면 값이 다 똑같기 때문입니다.

> $x[n]=\sum_{k=<N>}a_k\phi_k[n]=\sum_{k=<N>}a_ke^{jkw_0n}$﻿

$k=\langle N\rangle$﻿의 뜻은 $k$﻿가 주기가 $N$﻿일 때 한 주기만큼 더하는 것을 뜻합니다.

예를 들어, 주기가 5인 함수에서는 0~4 혹은 1 ~ 5까지 더하는 것이 허용됩니다.

DT에 대한 FS를 구했으면, 마찬가지로 $k=\langle N\rangle$﻿만큼 해를 구하면 DT signal을 표현할 수 있습니다.

## How to Determine $a_k?$﻿

![[Screenshot_2023-10-09_at_4.24.31_PM.png]]

그냥 니가 증명해보십시오

## Summary

![[Screenshot_2023-10-09_at_4.25.54_PM.png]]

## Partial sum of DT Squre wave & Gibbs Phenomenon

Gibbs phenomenon이란 squre wave를 FS로 표현할 때 불연속인 지점에서 오류가 발생하는 현상을 말합니다.

![[Media/Untitled 43.png|Untitled 43.png]]

이를 해결하기 위해 Partial sum을 도입합시다. 식은 다음과 같습니다.

![[Screenshot_2023-10-09_at_4.41.22_PM.png]]

주기가 even일 때와 odd일 때 달라지는 것만 유의합시다.