---
Created: 2023-10-09T17:14
Parent item:
  - "[[Fourier Series Representation of Periodic Signals]]"
---
## Frequency shaping Filters

LTI System을 파형을 바꾸기 위해 사용합니다.

- 특정 주파수를 없애기 위해서
- 파형의 변화를 보기 위해서

### example I : Derivative of the input

$y(t) = dx(t)/dt, H(j\omega)=j\omega$﻿

### example II : simple DT filter

$y[n] = 1/2(x[n]+x[n-1])$﻿

## Freq. Selective Filters

파형중 특정 주파수를 뽑아내기 위해서 사용합니다.

- constant input
    
    ![[Screenshot_2023-10-09_at_7.26.11_PM.png]]
    
- High frequency
    
    ![[Screenshot_2023-10-09_at_7.26.27_PM.png]]
    
- selective filters
    
    ![[Screenshot_2023-10-09_at_7.26.51_PM.png]]