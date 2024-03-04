---
Created: 2023-10-29T18:23
Parent item:
  - "[[The Continuous-tIme Fourer Transform]]"
---
## Aperiodic signals and Fourier Transform

![[Screenshot_2023-10-29_at_6.28.43_PM.png]]

aperiodic signal은 비주기함수입니다. 비주기함수는 Fourier series로 나타낼 수 없지만, Fourier transform을 이용하면 Fourier series로 나타낼 수 있습니다.

Transform의 형태는 다음과 같습니다.

![[Screenshot_2023-10-29_at_6.30.22_PM.png]]

> $X(jw)=\int^\infty_{-\infty}x(t)e^{-jwt}dt$﻿

coefficient와는 다음과 같은 관계를 가집니다. 주기의 역수를 곱한 값…

![[Screenshot_2023-10-29_at_6.32.41_PM.png]]

## Examples

- unit impulse
    
    ![[Screenshot_2023-10-29_at_6.36.56_PM.png]]
    
- square function
    
    ![[Screenshot_2023-10-29_at_6.37.32_PM.png]]
    

## Inverse FT

일반적인 FT와는 달리 $e^{jwt}$﻿를 곱해 적분하면 됩니다.

![[Screenshot_2023-10-29_at_6.39.48_PM.png]]