---
Created: 2023-09-18T20:14
Parent item:
  - "[[Linear Time-Invarient Systems]]"
---
## Introduction to LTI systems

첫 번째로 할일은 각종 system의 특성을 알고 있는 것입니다!

- Memoryless
- Inversibility
- Causality
- Stabiliy
- Time-invarient
- Linearity

이제 들어가 봅시다.

  

이전에 배웠듯이, 하나의 DT signal은 다음과 같이 표시할 수 있습니다.

> $x[n] = \sum_{k=-\infty}^\infty x[k]\delta[n-k]$﻿

여기서 $x[k]$﻿는 단순히 magnitude의 역할만 하고, 함수의 역할을 나타내는 것은 $\delta[n-k]$﻿임을 기억합시다.

여기서 시스템 $T()$﻿를 정의해봅시다.

> $x[n] \to T()\to y[n] \\ \delta[n] \to T() \to h[n]$﻿

$y[n]$﻿은 $x[n]$﻿를 시스템에 통과시켰을 때 나오는 결과이고, $h[n]$﻿은 unit impulse function $\delta[n]$﻿를 시스템에 통과시켰을 때 나오는 impulse response입니다.

이 때, 시스템 $T()$﻿가 Linear하고, Time-invarient 하다고 가정하면 다음과 같이 정리할 수 있습니다.

> $y[n] = T(\sum_{k=-\infty}^\infty x[k]\delta[n-k])$﻿
> 
> $\\ =\sum_{k=-\infty}^\infty x[k]T(\delta[n-k]) $﻿
> 
> $$﻿

결국 $x[n]$﻿과 $h[n]$﻿만 알면 $y[n]$﻿를 구할 수 있다는 결론이 나옵니다!