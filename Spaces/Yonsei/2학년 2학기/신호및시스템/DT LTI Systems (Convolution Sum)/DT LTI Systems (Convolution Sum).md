---
Created: 2023-09-18T20:29
Parent item:
  - "[[Linear Time-Invarient Systems]]"
---
## Shifting property

Convoltion sum을 구하기 위해서는 unit step function이나 unit impulse function을 잡아끌거나 뒤집는 테크닉이 필요합니다.

## Convolution sum

![[Media/Untitled 42.png|Untitled 42.png]]

![[Media/Untitled 1 32.png|Untitled 1 32.png]]

앞서 [[Introduction to LTI systems]]에서 봤다시피,

> $y[n] =\sum x[k]h[n-k]$﻿

으로 표현할 수 있습니다. 이를 Convolution sum이라고 하고, $y[n]=x[n]\ * \ h[n]$﻿으로 표시합니다.

단순히 생각하면, $h[n]$﻿(혹은 $x[n]$﻿)을 $n=0$﻿에 대하여 뒤집고, 한 칸씩 shift합니다.

이 때 겹치는 모든 칸을 곱해서 더합니다.

## Example

![[Media/Untitled 2 31.png|Untitled 2 31.png]]

![[Media/Untitled 3 30.png|Untitled 3 30.png]]

![[Media/Untitled 4 23.png|Untitled 4 23.png]]

이거왜 종ㄴㅇㅇㅇㅇㅇㅇ나 어렵냐

![[Media/Untitled 5 19.png|Untitled 5 19.png]]

차라리 얘가 쉬움