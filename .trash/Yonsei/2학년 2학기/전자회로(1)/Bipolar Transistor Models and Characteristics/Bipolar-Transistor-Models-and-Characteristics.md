---
Created: 2023-10-19T20:19
Parent item:
  - "[[Bipolar transistors]]"
---
## Simple BJT Amplifier configuration

일반적인 BJT에서, Collector 부분에 Load Resistance를 달아 output voltage를 확인할 수 있고, 이는… VCCS를 보여주는 근거가 됩니다!

![[Screenshot_2023-10-19_at_8.30.08_PM.png]]

## BTJ as a Constant Current Source

![[Screenshot_2023-10-19_at_8.32.38_PM.png]]

자주 간과할 수도 있는데, BJT에서 output current는 $V_{BE}$﻿에만 의존하고, $V_{CE}$﻿에 의존하지 않습니다.

따라서 $V_{BE}$﻿만 고정되어 있다면 BJT는 constant source로 여길 수도 있습니다. 위 사진처럼요!

> [!important]  
> 이를 Large Signal model이라고 합니다. 속이 뻥~![[Screenshot_2023-10-19_at_8.52.15_PM.png]]  

## Constraint on Load Resistance

![[Screenshot_2023-10-19_at_8.48.28_PM.png]]

$\beta$﻿를 올리고 싶으면 Load Resistance ($R_L$﻿)을 올리는 방법 또한 존재합니다.

하지만 저항을 계속 올리다보면 $V_X$﻿(Collector 쪽에 걸리는 전압)이 낮아져 더이상 BJT가 active 상태에 있지 않습니다. (reverse bias가 아니게 되기 때문)

→ 미련한 방법!

## BJT I-V chacteristics

![[Screenshot_2023-10-19_at_8.51.20_PM.png]]

- $V_{CE}$﻿가 아니라, $V_{BE}$﻿만이 $I_C$﻿에 관여한다!