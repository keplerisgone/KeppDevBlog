---
Created: 2023-09-13T21:01
Parent item:
  - "[[Signals and Systems]]"
---
Systems with and without memory

Invertibility and inverse systems

Causality

Stability

Time Invariance

Linearity

## Systems with and without memory

- ==Memoryless== : 메모리가 존재하지 않는 시스템입니다. 주로 input - output의 관계만 성립할 때 사용합니다.
    - ==Identity system== : 그냥 단순하게 input = output 인 시스템
- ==System with memory== : 말그대로 메모리가 존재하는 시스템입니다. _과거의 값_이 필요한 경우에는 이러한 값을 저장할 메모리가 필요합니다. signal은 결국 시간에 따른 함수들이고, 이를 적분해 값을 얻는 행위 또한 결국 과거의 값이 필요한 작업이므로 메모리가 필요한 대표적인 경우라고 볼 수 있습니다.

## Invertibility and inverse systems

==Invertible== 하다는 것은 시스템을 거꾸로 되돌릴 수 있는지 여부를 뜻합니다. 정확히는, _한 시스템을 통과해 나온 결과가 다른 시스템을 거쳐서 원래의 인풋으로 돌아올 수 있는가?_ 가 기준이 됩니다.

예를 들어, $ y(t)=2x(t)$﻿ 라는 시스템은 $y(t)$﻿ 가 $x(t)=1/2y(t)$﻿ 라는 시스템을 거쳐 다시 $x(t)$﻿로 돌아올 수 있지만, $y(t)=x(t)^2$﻿ 같은 경우는 역으로 확실하게 돌아올 수 있는 시스템이 없으므로 (음수와 양수 루트 시스템 두 개가 존재합니다) invertible 하지 않습니다.

![[Screenshot_2023-09-13_at_9.16.06_PM.png]]

사실 Inverse function의 존재여부를 확인하는 것과 마찬가지로, 하나의 시스템이 일대일대응이면 됩니다.

## Causality

![[Media/Untitled 45.png|Untitled 45.png]]

==Causality==는 _인과관계_라는 뜻으로, system의 output이 미래의 시그널이 아닌 현재와 과거의 시그널에만 영향을 받는 system을 뜻합니다.

- causal system : $y[n]=\sum_{k=-\infty}^nx[n]$﻿ , 미래의 값에 따라 바뀌지 않습니다.
- uncausal system : $y[n]=x[n]+x[n+1]$﻿, $n+1$﻿의 값이 미래입니다.

## Stability

![[Media/Untitled 1 34.png|Untitled 1 34.png]]

system이 ==stable==하다는 것은 input에 따른 결과가 divergent 하지 않다는 것입니다.

다르게는 BIBO Stability라고도 표현할 수 있는데, 이는 Bounded In - Bounded Out이라는 뜻으로, 유한한 범위 내의 입력값을 넣었을 때 유한한 범위의 output이 나옴을 의미합니다. 수식으로 표현하면 다음과 같습니다.

> $|x(t)| < B_1, \ |y(t)| < B_2$﻿ 이다.

> [!important]  
> Accmulator 저거 뭐임결과를 저장하는 장치래 근데 이게 왜 unstable함?  

## Time Invariance

![[Media/Untitled 2 33.png|Untitled 2 33.png]]

Time invarient하다는 것은 delayed 된 input을 넣었을 때 output 또한 delayed 된 상태로 나오는 시스템을 의미합니다.

## Linearity

![[Media/Untitled 3 32.png|Untitled 3 32.png]]

system이 Linear이다 (선형적이다) 라는 것은 해당 system에 대해 superposition이 성립함을 의미합니다. superposition(중첩 원리)이 성립한다는 것은 다음과 같습니다.

> $\begin{matrix} x_1(t) \to y_1(t) \\ x_2(t) \to y_2(t) \end{matrix} \Rightarrow \begin{matrix} x_1(t) + x_2(t) \to y_1(t) + y_2(t) \\ ax_1(t) \to ay_1(t) \end{matrix}$﻿

즉, additivity와 Scaling(homogeneity) 가 성립하면 됩니다.

실제로 $y[n] = 2x[n] + 3$﻿ 은 굉장히 linear해보이지만, 뒤의 $3$﻿이 Zero-input response이기 때문에(초기값) 성립하지 않습니다.

사실 위의 superposition에서 모두가 0을 넣어도 동작해야하므로, $(x[n], y[n]) = (0,0)$﻿이 성립해야하긴 합니다.