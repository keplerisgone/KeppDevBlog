---
Created: 2023-11-06T15:18
Parent item:
  - "[[DT Fourier Tranform]]"
---
## Periodicity

> $X(e^{j(\omega+2\pi)})=X(e^{jw})$﻿

CTFT는 periodic 하지 않지만, DTFT에서는 주기성이 성립합니다. DTFT의 정의에 따라 계산하면 주기성이 생깁니다.

## Linearity

선형성이 성립합니다.

> $ax_1[n]+bx_2[n] \longleftrightarrow aX_1(e^{jw})+bX_2(e^{jw})$﻿

이는 CTFT, FS와 마찬가지로 적분의 정의를 이용합니다.

## Time/Freq. Shifting

> $x[n-n_0] \longleftrightarrow e^{-jwn_0}X(e^{jw})$﻿

> $e^{jw_0n}x[n] \longleftrightarrow X(e^{j(w-w_0)})$﻿

이 또한 DTFT의 정의를 이용합니다.

## Conjugation and conjugate symmetry

![[Screenshot_2023-11-06_at_3.29.38_PM.png]]

그냥 사진을 보십시오

## Differencing and Accumulation

> $x[n]-x[n-1] \longleftrightarrow (1-e^{-jw})X(e^{jw})$﻿

![[Screenshot_2023-11-06_at_3.35.14_PM.png]]

## Time Reversal

![[Screenshot_2023-11-06_at_3.35.50_PM.png]]

## Time expansion

![[Screenshot_2023-11-06_at_3.36.28_PM.png]]

DT signal은 자체적으로 time scaling이 안됨

→ 이런 방법으로 scaling합니다

![[Screenshot_2023-11-06_at_3.38.14_PM.png]]

띄엄띄엄 하는 방식으로 합니다. 주파수 도메인에서도 띄엄띄엄 됩니다.

time domain에서 띄울 수록 freq domain에서는 좁아집니다.

![[Screenshot_2023-11-06_at_3.39.22_PM.png]]

## Differentiation in Frequency

![[Screenshot_2023-11-06_at_3.40.03_PM.png]]

## Parseval’s relation

![[Screenshot_2023-11-06_at_3.40.51_PM.png]]