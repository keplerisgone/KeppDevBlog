---
Created: 2023-11-11T21:05
---
## Bad Connections

![[Screenshot_2023-11-11_at_9.08.47_PM.png]]

이렇게 연결하면 DC 때 capacitor가 open 돼버려 Emitter current가 흐르지 않게 됩니다. 그러면 트랜지스터가 동작하지 않잖아.

![[Screenshot_2023-11-11_at_9.12.08_PM.png]]

이렇게 연결하면 input이 ground 쪽으로 바로 가기 때문에 output이 나오지 않게 됩니다.

## Proper Biasing for CB stage

더 나은 방법은 엄청 큰 저항을 Emitter에 달아주는 것입니다.

이렇게 하면 ground에 가는 저항은 줄이면서 capacitor의 역할을 수행하게 할 수 있습니다.

![[Screenshot_2023-11-11_at_9.15.23_PM.png]]

물론 이 때문에 input impedance가 낮아지긴 합니다.

![[Screenshot_2023-11-11_at_9.18.17_PM.png]]

## Creation of Vb

![[Screenshot_2023-11-11_at_9.22.32_PM.png]]

base voltage를 만들어내기 위해서는 주로 resistive voltage divider를 사용하는데, 이는 gain을 줄입니다.

따라서 뒤에 bypass capacitor를 달아 AC에서는 ground로 연결시킵니다.

### Example of CB Stage with Bias

![[Screenshot_2023-11-11_at_9.26.57_PM.png]]

## Emitter Follower

이제 common collector를 배울 차례인데, 이는 Emitter Follower라고 따로 불립니다.

![[Screenshot_2023-11-16_at_10.49.34_PM.png]]

- Input은 Base에 존재합니다.
- Output은 Emitter에 존재합니다.
    - 여기서 Emitter resistance가 없다면 $V_{out}=0$﻿이기 때문에, $R_E$﻿는 항상 존재해야 합니다.
- 둘이 같은 common collector를 공유한다고 해서 common collector amplifier!

## Emitter Follower Core

![[Screenshot_2023-11-16_at_10.52.17_PM.png]]

Emitter Follower에서 KVL을 적용해보면 다음과 같은 식을 얻을 수 있습니다.

> $-V_{BE}=V_{out}-V_{in}$﻿

여기서 $V_{in}$﻿이 증가하면 emitter current가 증가하므로 $V_{out}$﻿ 또한 함께 증가하는 것을 알 수 있습니다. → 이건 무조건입니다.

따라서 해당 회로를 level shift라고 부릅니다.

또 하나 주목할 점은 $V_{in}$﻿이 항상 $V_{out}$﻿보다 $V_{BE}$﻿만큼 크다는 것.

그래서 Emitter는 항상 Base의 값을 따라가려고 하는데… 그래서 Emitter Follower라고 불립니다.

그래서 항상 $A_v \le 1$﻿ 입니다.

## Small-Signal model of Emitter Follower

![[Screenshot_2023-11-16_at_11.00.44_PM.png]]

early effect를 고려하지 않는다면 voltage gain은 다음과 같습니다.

> $A_v=R_E/(R_E+g_m^{-1})$﻿

증명 과정은 위를 참조해라.

> [!important]  
> 여기서 @import url('https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.css')RER_ERE​﻿를 current source로 바꾸면 위의 식에서 @import url('https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.css')RE=∞R_E=\inftyRE​=∞﻿ 가 되기 때문에 gain이 1이 됩니다!![[Screenshot_2023-11-16_at_11.03.43_PM.png]]  

## Emitter Follower as a Voltage Divider

![[Screenshot_2023-11-16_at_11.06.09_PM.png]]

- Emitter Follower의 Thevenin voltage, resistance를 구하면 다음과 같습니다.
    
    $V_{in}, g_m^{-1}$﻿ !
    
    이유는 I/O impedance와 위의 슬라이드 참고.
    

## Emitter Follower with Source Resistance

![[Screenshot_2023-11-16_at_11.10.52_PM.png]]

Source resistance가 있는 경우는 다음과 같습니다.

> ![[Screenshot_2023-11-16_at_11.11.15_PM.png]]
> 
>   

여기서 $R_{thev}$﻿ 가 미치는 영향은 꽤 작습니다. (값이 작아서)

## Input Impedamce of Emitter Follower

![[Screenshot_2023-11-16_at_11.13.33_PM.png]]

CE stage with Emitter degeneration 과 같습니다.

![[Screenshot_2023-11-16_at_11.13.53_PM.png]]

## Effect of BJT Current Gain

![[Screenshot_2023-11-16_at_11.15.21_PM.png]]

- 전류를 $\beta +1$﻿ 만큼 증폭시킵니다.
    - 절대 전압을 증폭시키지 않습니다.
- load Impedance가 $\beta +1$﻿만큼? 증폭?
- 따라서 buffer 라고 불립니다.
    - Load effect를 감소시킵니다.

## Emitter Follower as a Buffer

![[Screenshot_2023-11-16_at_11.18.49_PM.png]]

- input impedance를 높이고,
- output impedance를 낮춰 load resistance에 의한 gain degradation을 낮춥니다.

## Output Impedance of Emitter Follower

![[Screenshot_2023-11-16_at_11.23.02_PM.png]]

작다.

## Emitter Follower with Early Effect

![[Screenshot_2023-11-16_at_11.29.55_PM.png]]

- early effect를 고려한다면, $r_O$﻿를 고려해야 합니다.
- Emitter Resistance에 병렬로 연결하면 됩니다.

## Emitter Follower with Biasing

![[Screenshot_2023-11-16_at_11.32.34_PM.png]]

- 대개 $R_1$﻿과 $R_2$﻿에 흐르는 전류가 base current보다 높게 설정되어야 함
- $V_{CC}$﻿와 $V_B$﻿ 가 비슷하게 정해질 수 있음
    - collector가 그대로 $V_{CC}$﻿에 연결되어 있어 항상 $V_{CE}>V_{BE}$﻿ 가 될 수 있음
- 오른쪽처럼 biasing하면 편하다 → 근데 divider가 없어서 $\beta$﻿의 영향을 받지 않을까?
    - 그래서 $R_E$﻿에 걸리는 전압을 $R_BI_b$﻿보다 높게 한다.

> [!important]  
> 이게 진짜 복잡한데…Input load equation 에 따르면 @import url('https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.css')β\betaβ﻿ 값이 감소해도 @import url('https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.css')RER_ERE​﻿에서의 전압강하는 @import url('https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.css')RBIBR_BI_BRB​IB​﻿만큼 줄어들 것이므로 @import url('https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.css')IC=IEI_C=I_EIC​=IE​﻿의 값은 영항을 많이 받지 않는다.![[Screenshot_2023-11-16_at_11.53.24_PM.png]]  

- 근데 문제점은 $V_{BE}$﻿의 동작점이 $V_{CC}$﻿에 의존한다는 것…

## Supply-Independent Biasing

![[Screenshot_2023-11-16_at_11.42.02_PM.png]]

위 문제를 해결한 Biasing입니다. 위의 값들이 고정되어 있기 때문에 $V_{CC}$﻿의 영향을 받지 않습니다.