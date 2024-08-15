---
Created: 2023-10-19T21:09
Parent item:
  - "[[Bipolar transistors]]"
---
## BJT Operation Region

![[Screenshot_2023-10-19_at_9.11.31_PM.png]]

읽으십시오.

사실상 summary

## Transconductance

![[Screenshot_2023-10-19_at_9.13.44_PM.png]]

voltage signal을 얼마나 current signal로 잘 바꾸는가?

따라서 $V_{T}$﻿와 output current라고 할 수 있는 $I_C$﻿의 비율로 나타납니다. 따라서 그래프로 나타내면 다음과 같습니다.

![[Screenshot_2023-10-20_at_3.04.55_AM.png]]

작은 voltage input이 들어갔을 때 $I_C$﻿ output은 얼마나 증폭되는가? 를 비율로 나타낸 것입니다.

원래는 exponential이지만 approximation으로 linear하게 만든 것입니다.

또한 $V_{BE}$﻿가 고정되어 있다면 변수는 $I_S$﻿에 해당하기 때문에, BJT의 개수에 따라 $g_m$﻿의 값은 달라집니다.

## Derivation of small-Signal Model

![[Screenshot_2023-10-20_at_4.41.01_PM.png]]

하나의 terminal만이 input으로 작용하고, 하나는 output으로 작용합니다. 나머지 하나의 걸리는 voltage는 고정되어 있습니다.

Small-Signal model에서는 DC source가 Grounded 됩니다.

> [!important]  
> active device는 superposition이 적용되서 이런 짓을 해도 되는 건가요?  

## BJT Design

![[Screenshot_2023-10-20_at_4.47.07_PM.png]]

실제로 $V_{BE}$﻿가 고정되어 있으면 $I_C$﻿$V_{CE}$﻿의 영향을 받지 않는다고 배웠습니다.

하지만 실제 회로에서는 $I_C$﻿은 $V_{CE}$﻿의 영향을 받습니다. 원리는 다음과 같습니다.

1. $V_{CE}$﻿가 증가하면 depletion region의 너비가 증가하고, 이에 따라 concentration 곡선의 기울기가 가팔라집니다.
2. diffusion이 심하게 일어납니다.
3. collector current가 증가합니다.

## Early Effect

early effect는 $V_{CE}$﻿가 증가하면 collector current하는 현상을 말합니다.

Early effect를 수식으로 표현하면 다음과 같습니다.

![[Screenshot_2023-10-20_at_4.52.56_PM.png]]

$V_{CE}$﻿의 변화가 $I_C$﻿에 미치는 영향을 수식으로 나타낸 term이 뒤의 $V_X/V_A$﻿입니다.

Small signal model에서 early effect는 $r_o$﻿로 나타납니다. $r_o$﻿은 output impedence라고 하며, 이곳에 흡수되는 에너지가 추가적인 output이 됩니다.

## BJT in Saturation Mode

$V_{CE}$﻿가 감소함에 따라, Collector-base junction이 forward bias에 있게 됩니다. 이러면 BJT가 active되지 않기 때문에 current gain이 줄게 됩니다.

![[Screenshot_2023-10-20_at_5.06.15_PM.png]]

이를 회로로 표현하면 다음과 같은데, C-B가 forward일 경우 전류가 빠져나가 gain이 줄어드는 경우를 나타낸 것입니다.

$\beta$﻿ 또한 saturation의 speed에 영향을 줍니다.

## The PNP Transistor

![[Screenshot_2023-10-20_at_5.15.18_PM.png]]

PNP transistor는 NPN Transistor와 달리 P - N - P type으로 doping된 semiconductor를 접합해놓은 것입니다.

polarity 성질을 제외한 모든 기능은 NPN transistor와 동일합니다.

## Large Signal model for PNP BJT

![[Screenshot_2023-10-20_at_5.18.04_PM.png]]

## PNP BJT Biasing

![[Screenshot_2023-10-20_at_5.47.48_PM.png]]

emitter는 base 보다 더 높게 biasing 되어있어야 합니다.

## Small-Signal Analysis

![[Screenshot_2023-10-20_at_5.49.32_PM.png]]

Small-Signal Analysis 는 NPN과 동일합니다.