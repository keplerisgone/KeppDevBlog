---
Created: 2023-11-14T00:04
Parent item:
  - "[[Sampling]]"
---
흐름은 이렇습니다.

$x_c(t)$﻿를 sampling 하면 $x_p(t)$﻿,

$x_p(t)$﻿를 DT로 바꾸면 $x_d[n]$﻿,

$x_d[n]$﻿을 시스템에 통과시키면 $y_d[n]$﻿,

$y_d[n]$﻿을 다시 CT로 표현하면 $y_c(t)$﻿ 입니다.

![[Screenshot_2023-11-14_at_12.07.51_AM.png]]

이를 FT를 사용해 이들간의 관계를 나타내봅시다.

![[Screenshot_2023-11-14_at_7.12.08_PM.png]]

그래프를 이용해 예시를 표현해보면 맞는 것을 알 수 있습니다.

![[Screenshot_2023-11-14_at_7.13.25_PM.png]]

각 과정을 간단하게 알아봅시다. 직접 신호를 예시로 들어볼게요

![[Screenshot_2023-11-15_at_8.39.42_PM.png]]

![[Screenshot_2023-11-15_at_8.40.16_PM.png]]

1. 가장 왼쪽 위는 원본 CT의 FT입니다.
2. 그 아래는 sampling을 진행한 뒤의 FT입니다. 원본 신호와 동일한 모양이지만 주기함수가 되었습니다.
    1. impulse train과 곱했으니 freq. domain에서는 convolution이 되어야 합니다
3. 그 아래가 가장 중요!! sampling한 것을 DT 시그널로 바꾸기 위해서는 $wT=\Omega$﻿를 적용시켜야 합니다. 샘플링한 간격을 정수로 바꿔준다고 생각하면 됩니다.
4. 다음은 zero-order hold와 reconstruction를 진행하는 filter에 통과시켜 $y_d[n]$﻿을 만듭니다.
    1. 여기서의 오메가는 왜 cut-off freq.일까요?
5. 그 후 역시나 $\Omega /T=w$﻿을 이용해 다시 도메인을 바꿔줍니다. 신호는 $y_p(t)$﻿가 됩니다.
6. 마지막으로 LPF에 통과시켜 만들고자 했던 $y_c(t)$﻿를 만들어 줍니다.

이 때 사용하는 filter에 대한 정보는 다음과 같습니다.

![[Screenshot_2023-11-15_at_8.58.40_PM.png]]

차이점은 변수 값이랑 그 뭐냐… 주기함수냐 아니냐?

중요한 점 요약본은 다음과 같다.

![[Screenshot_2023-11-15_at_9.03.22_PM.png]]