---
Created: 2023-09-20T19:45
Parent item:
  - "[[Linear Time-Invarient Systems]]"
---
## Convolution Integral

이전의 convilution sum과 목표는 같습니다.

증명법을 먼저 써볼게요.

> $x(t)$﻿ is CT signal.
> 
> $x(t) = \int_{-\infty}^\infty x(\tau)\delta(t-\tau)d\tau$﻿, $y(t) = T(x(t))$﻿.
> 
> $y(t)=T(\int_{-\infty}^{\infty}x(\tau)\delta(t-\tau)d\tau)$﻿, 이 때 system $T()$﻿ 가 linear, Time-invarient 하다고 하면 다음이 성립합니다.
> 
> $y(t)=\int_{-\infty}^{\infty}x(\tau)T(\delta(t-\tau))d\tau$﻿, $T(\delta(t)) = h(t)$﻿로 정의하면 TI 이므로 $T(\delta(t-\tau))=h(t-\tau)$﻿가 성립합니다.
> 
> 즉, 다음이 성립합니다!
> 
> $\therefore y(t)=\int_{-\infty}^\infty x(\tau)h(t-\tau)d\tau$﻿

이제 input signal $x(t)$﻿와 $h(t)$﻿ 만 뭔지알면 output을 구할 수 있습니다!

사실 전략은 convolution sum과 같이 _겹치는 부분의 모든 합_을 구하는 것으로 동일합니다. 그 적분값이 $y(t)$﻿가 됩니다.