---
Created: 2023-08-31T21:29
Sub-item:
  - "[[Ideal Diode]]"
  - "[[Applications of Diode]]"
---
### DC bias calculation

- 목표 : Diode operating point를 찾자!
- exponential calculation : 많은 iteration이 필요
- constant diode model : $V_{d,on}$﻿이 700mV를 넘기면 $V_D=V_{D,on}$﻿

### Ideal diode

![[Screenshot_2023-10-02_at_12.24.27_AM.png]]

$V_{D,on}$﻿이 0인 다이오드, deplation region이 형성되지 않습니다.

따라서 $V_D=V_{anode}-V_{cathode}$﻿가 0만 넘을 경우 바로 short circuit이 되는 다이오드입니다. 그래프의 형태는 다음과 같습니다.

![[Screenshot_2023-10-02_at_12.36.50_AM.png]]

$V_D<0$﻿일 때 저항이 $\infty$﻿, $V_D>0$﻿일 때 저항이 0임을 보여주는 사진입니다.

저항이 0인 상태에서는 옴의 법칙이 성립합니다.

### Diode Implementation of OR Gate

이러한 다이오드의 특징을 이용해 OR gate를 설계할 수 있습니다.

두 개의 다이오드를 병렬로 연결해, 둘 중 하나의 다이오드에 $V_D>0$﻿인 전압이 걸린다면 전류가 흐르는 회로를 설계할 수 있습니다.

![[Screenshot_2023-10-02_at_12.57.50_AM.png]]