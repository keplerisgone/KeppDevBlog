---
Created: 2023-10-03T14:32
Parent item:
  - "[[Diode model and circuits]]"
---
## Ideal Diode

![[Screenshot_2023-10-03_at_2.35.30_PM.png]]

$V_D$﻿가 0보다 크면 저항이 0이고, $V_D$﻿가 0보다 작으면 저항이 $\infty$﻿인 회로처럼 작용하는 다이오드입니다. 그림으로 표시하면 다음과 같습니다.

![[Screenshot_2023-10-03_at_2.36.42_PM.png]]

따라서 Resistor와 함께 연결된 다이오드는 역방향의 전류를 차단하는 역할을 겸합니다.

forward bias로 전압이 연결된 경우는 옴의 법칙을 따릅니다.

## Small-Signal Analysis

![[Screenshot_2023-10-03_at_2.40.49_PM.png]]

아주 작은 크기의 신호를 생각하는 경우, Linear Approxmation을 통해 해당 bias point에서의 전류를 계산할 수 있습니다.

## Diode Implementation of OR Gate

![[Screenshot_2023-10-03_at_2.43.59_PM.png]]

non-ideal한 diode의 특성을 이용하면($V_D>V_{D,on}$﻿이면 $V_D=0.7V$﻿) OR 게이트를 만들 수 있습니다.

두 다이오드를 ==병렬로 연결==하면 됩니다!

병렬로 연결된 두 다이오드 중 하나에만 $V_{D,on}$﻿이상의 전압을 걸어준다면 $V_{out}$﻿ 이 0 이상이 됩니다.

> [!important]  
> AND gate는?