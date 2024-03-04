---
Created: 2023-11-27T11:43
---
## The Body Effect

![[Screenshot_2023-11-29_at_11.47.41_PM.png]]

- $V_{TH}$﻿는 source - body 에 존재하는 negative bias로 인해 증가할 수 있다
- 뭐 $V_{TH}$﻿가 증가하면 문턱 전압이 높아지는 것은 맞지만, ($V_G > V_{TH}$﻿여야 하므로)
    
    $V_{TH}$﻿가 negative bias 로 인해 감소하더라도 문턱 전압이 높아지는 이유는 뭔가?
    
    → depletion region이 넓어져서
    

## Channel-length Modulation

![[Screenshot_2023-11-29_at_11.56.40_PM.png]]

- pinch-off point는 $V_{DS}$﻿가 줄어들면 슬쩍 source로 이동
    - inversion-layer channel length는 $V_{DS}$﻿가 증가할수록 줄어듭니다.
- 따라서 $\lambda$﻿만큼 current가 linear하게 증가합니다.

## $\lambda $﻿ and $L$﻿

![[Screenshot_2023-11-30_at_12.02.58_AM.png]]

- channel length가 짧을수록 body effect의 영향이 크다.

## MOSFET Large-Signal Models ($V_{GS} > V_{TH}$﻿)

![[Screenshot_2023-11-30_at_12.04.28_AM.png]]

- $V_{DS}<<2(V_{GS}-V_{TH})$﻿
    - purely resistor가 된다 → $V_{DS}$﻿가 이렇게 작으면 $I_D$﻿가 있긴해?
- $V_{DS}<V_{D,sat}$﻿
    - triode region 범위 내부에서… $I_D$﻿가 존재합니다.
- $V_{DS}>V_{D,sat}$﻿
    - saturation region 범위 내부에서… $I_D$﻿는 constant

## MOSFET Transconductance

![[Screenshot_2023-11-30_at_12.23.15_AM.png]]

- $g_m$﻿ 는 $v_{in}$﻿에 의한 $i_{out}$﻿의 비를 나타내는 값입니다. → transconductance → VCCS
- 그래서 $g_m$﻿은 $I_D$﻿를 $V_{GS}$﻿에 대해 편미분한 값이다.
- $\beta$﻿는 무한이기 때문에 CCCS가 아님

## MOSFET Small-Signal Model (Saturation Region of Operation)

![[Screenshot_2023-11-30_at_12.27.32_AM.png]]

- Saturation에서 $I_D$﻿에 대한 $V_{DS}$﻿의 기울기가 $r_o$﻿이다.

## PMOS Transistor

![[Screenshot_2023-11-30_at_12.48.46_AM.png]]

- 부호만 다르지 기능은 다 같다.

## PMOS I-V Equations

![[Screenshot_2023-11-30_at_12.50.59_AM.png]]

- 역시 부호만 다르지 등식은 다 같다.

## CMOS Technology

![[Screenshot_2023-11-30_at_12.51.55_AM.png]]

- NMOS랑 PMOS를 같이 씁니다.

- 도핑하는 법….. 4번 하면 된다고?

## Comparison between BJT and MOSFET

![[Screenshot_2023-11-30_at_12.53.42_AM.png]]

- BJT는 exponential로 증가
- MOSFET은 quadratic으로 증가
    - Gate Current가 0이라 $\beta$﻿가 무한대이다 → CCCS는 아님
- 결국 amplifier로써는 BJT가 낫다