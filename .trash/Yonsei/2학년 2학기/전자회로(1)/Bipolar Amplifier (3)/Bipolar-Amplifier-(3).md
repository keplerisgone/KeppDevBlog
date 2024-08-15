---
Created: 2023-10-31T22:33
---
## Bad Input Connection

![[Screenshot_2023-10-31_at_11.37.40_PM.png]]

그렇다고 이렇게 바로 Input을 연결해버리면 $V_X=V_{BE}$﻿이 너무 낮아지기 때문에 heavy saturation에 빠지게 됩니다.

## Using of Coupling Capacitor

![[Screenshot_2023-10-31_at_11.39.35_PM.png]]

왜 coupled나면… DC와 AC를 couple시켜서 따로 분리하는 전략을 사용하기 때문입니다.

> [!important]  
> bypass capacitor와의 차이는 무엇일까요?얘는 차단의 역할, bypass 는 흘려주는역할  

## DC and AC Analysis

![[Screenshot_2023-10-31_at_11.45.04_PM.png]]

DC에서는 capacitor가 open되고, AC일 때는 capacitor가 short됩니다.

## Bad Output Connection

그렇다고 스피커를 그냥 output에 꽂아버리면 collector current가 transistor로 들어가지 않아 심각하게 낮아집니다. → heavy saturation

![[Screenshot_2023-10-31_at_11.48.06_PM.png]]

## Use of Coupling Capacitor at Output

![[Screenshot_2023-10-31_at_11.49.36_PM.png]]

따라서 output 단에도 capacitor를 연결해 biasing이 가능하도록 합니다.

## CE Stage with Robust Biasing

![[Screenshot_2023-10-31_at_11.55.21_PM.png]]

## Elimination of Emitter Degeneration for AC Signals

![[Screenshot_2023-11-01_at_12.02.47_AM.png]]

> [!important]  
> Emitter Degeneration은 정말 좋은 방법이지만 gain을 줄인다는 단점이 있습니다. 그래서 옆에 capacitor를 달아서 고주파 영역에서 회로를 short시켜서 @import url('https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.css')RER_ERE​﻿를 없앱니다. 그래서 값이 오른쪽처럼 계산됩니다.  

## Complete CE Stage

![[Screenshot_2023-11-01_at_12.09.30_AM.png]]

이제 inevitable resistance를 달아서 종합적으로 생각해봅시다.

## Summary of CE Concepts

![[Screenshot_2023-11-02_at_11.35.02_PM.png]]

Loss와 variation을 줄이고 gain을 최대한 높이기 위한 회로의 진화과정입니다.

순서대로 Emitter Degeneration → bypass capacitor & Coupling capacitor

## Common Base(CB) Amplifier

![[Screenshot_2023-11-02_at_11.40.26_PM.png]]

Base terminal이 fixed 되어 있고, emitter에 input이 달려있으며 collector에 output이 달려있습니다.

## SSM Analysis of CB core

![[Screenshot_2023-11-02_at_11.43.36_PM.png]]

gain은 CE stage에서와 값이 동일하지만 부호가 다릅니다.

> $A_v=g_mR_C$﻿

## Tradeoff between Gain and Headroom

![[Screenshot_2023-11-02_at_11.46.30_PM.png]]

gain에 $R_C$﻿가 포함돼있기 때문에 이를 높이면 gain도 높아질 것이라고 생각할 수 있지만, $R_C$﻿를 계속 올린다면 $V_{CE}$﻿가 낮아져 active mode에서 벗어나게 됩니다.

이렇게 내려가다가 $V_{CC}-V_{BE}=V_{RC}$﻿이 되는 순간에 edge of saturation이 됩니다.

## Simple CB Stage Example

![[Screenshot_2023-11-02_at_11.50.33_PM.png]]

위는 $V_{out}$﻿의 변화로 온도의 변화를 측정하는 thermometer입니다. ($V_T$﻿의 변화를 측정하는 거임)

왼쪽 회로의 가장 큰 문제점은 power source가 두 개라는 건데, 이를 voltage divider를 이용해 해결한 회로가 바로 오른쪽입니다.

## Input impedance of a CB Stage

![[Screenshot_2023-11-02_at_11.54.49_PM.png]]

CB stage에서의 input impedance는 $1/g_m$﻿으로, CE에서의 $\beta/g_m = r_\pi$﻿보다 몹시 작습니다.

이게 작아짐에도 쓰는 이유는 current buffer, amplifier에 쓰이기 때문ㅇㅇ

## CB Stage with cource Resistance

![[Screenshot_2023-11-02_at_11.59.50_PM.png]]

어쩔 수 없는 source resistance를 연결하면 gain이 다음과 같이 됩니다.

$A_v=R_C/(g_m^{-1}+R_S)$﻿

## Output impedance of a CB Stage

![[Screenshot_2023-11-03_at_12.02.54_AM.png]]

CE stage와 같다.

## Av of CB Stage with Base Resistance

![[Screenshot_2023-11-03_at_12.04.44_AM.png]]

base resistance를 연결한 회로에서는 gain이 다음과 같이 줄어듭니다.

또한 CE Stage에서의 gain과 부호밖에 차이나지 않습니다.

## Voltage Gain: CE vs CB Stages

![[Screenshot_2023-11-03_at_12.08.34_AM.png]]

CB stage에서와 CE stage에서의 voltage gain은 값은 같지만 부호가 다릅니다.

## Input impedance of CB stage with Base Resistance

![[Screenshot_2023-11-03_at_12.11.04_AM.png]]

저렇게 계산됩니다만, $R_B$﻿의 값은 작고 $\beta+1$﻿의 값은 크기 때문에 별로 영향을 끼치지 않습니다.

## Input Impedance Seen at Emitter vs Base

![[Screenshot_2023-11-03_at_12.12.19_AM.png]]

CB 에서는 큰 영향을 끼치지 않는 것이 CE stage에서는 큰 영향을 끼칩니다.

## Input impedance example

![[Screenshot_2023-11-03_at_12.14.01_AM.png]]