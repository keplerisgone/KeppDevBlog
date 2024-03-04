---
Created: 2023-09-25T19:24
Parent item:
  - "[[Linear Time-Invarient Systems]]"
---
## Linear constant-coefficient differential equations

![[Screenshot_2023-09-25_at_7.26.54_PM.png]]

- system을 differential equation으로 표현할 수 있습니다.
- system을 causal 하다고 정의하고, auxiliary condition을 정하면 system을 특정할 수 있습니다.

## General Nth order LCCDE

Nth order LCCDE의 general form은 다음과 같습니다.

![[Screenshot_2023-09-25_at_7.32.17_PM.png]]

$N=0$﻿을 가정하면 (ODE가 아닌 그냥 식) $y(t)$﻿는 위와 같이 정리할 수 있습니다.

하지만 $N>0$﻿일 경우에는 Homogeneous solution과 initial condition을 다음과 같이 설정합니다.

![[Screenshot_2023-09-25_at_7.35.17_PM.png]]

이는 나중에 더 자세히 배웁니다.

## Linear const-coeff difference equations (DT case)

DT에서는 difference가 ${dy[n] \over dn} = y[n-1]...$﻿과 같이 정의됩니다. 따라서 DT에서의 LCCDE는 다음과 같이 정의됩니다.

![[Screenshot_2023-09-25_at_7.37.42_PM.png]]

오른쪽은 homogeneous.

식을 $y[n]$﻿에 대해 정리하면 다음과 같습니다.

![[Screenshot_2023-09-25_at_7.41.35_PM.png]]

recursive equation으로 이를 풀면 됩니다.

$N=0$﻿인 경우는 non-recursive eq.이 나옵니다. 과거의 값이 필요하지 않습니다.

![[Screenshot_2023-09-25_at_7.42.42_PM.png]]

이 때의 system $h[n]$﻿은 범위가 존재하기 때문에 FIR이라고 불립니다.

## Block diagram representations of first-order systems

- DT
    
    ![[Screenshot_2023-09-25_at_7.46.15_PM.png]]
    
- CT
    
    ![[Screenshot_2023-09-25_at_7.46.39_PM.png]]