---
Created: 2023-11-30T20:56
---
## Basic MOSFET Amplifier

![[Screenshot_2023-11-30_at_11.19.03_PM.png]]

- Small-signal model에서 높은 gain을 얻기 위해서는 MOSFET이 saturation region에 있어야 합니다.

> [!important]  
> 왜요??headroom 임마  

## MOSFET Biasing

![[Screenshot_2023-11-30_at_11.22.45_PM.png]]

- 이 때 Gate와 Drain에 voltage를 걸기 위해서 voltage divider를 사용합니다.
- 그래서 위에 방정식을 이용해서 변수를 찾을 수도 있음

## Self-Biased MOSFET Stage

![[Screenshot_2023-12-01_at_12.35.57_AM.png]]

- $I_G$﻿는 0이니까 $R_G$﻿에 걸리는 전압도 0이다
- 그리고 $R_G$﻿는 크니깐 $R_{out}$﻿은 그냥…

## MOSFET as Current Sources

![[Screenshot_2023-12-01_at_12.39.42_AM.png]]

- saturation에서는 MOSFET이 Current source로 동작합니다.
    - constant current source
- 다만
- NMOS는 open circuit에 연결된 current source, PMOS는 $V_{DD}$﻿에 연결된 current source로 취급됩니다.

## Common-Source Stage, no body effect

![[Screenshot_2023-12-02_at_3.22.26_PM.png]]

- Common-Source : Source를 공유하는 amplifier
- SSM 에서는 v_1이 open
- $R_{in}$﻿는 Gate에 존재하기 때문에 ($I_G=0$﻿) 무한대.
- $R_{out}$﻿는 $R_D$﻿과 가깝다.

## Common-Source Stage with Body Effect

![[Screenshot_2023-12-02_at_3.25.42_PM.png]]

- $r_o$﻿와 병렬 연결이라고 취급하면 됨

## CS Gain Variation with L

![[Screenshot_2023-12-02_at_3.27.51_PM.png]]

- 아무튼 L의 루트값이랑 비례
- voltage gain과 headroom은 current source를 달아놓음으로서 줄일 수 있다

## CS Stage with Current-Source Load

![[Screenshot_2023-12-02_at_3.29.26_PM.png]]

- 그러면 current source를 PMOS로 대체하면 되지 않을까?
- I/O Impedance는 다음과 같다
    
    ![[Screenshot_2023-12-02_at_3.46.10_PM.png]]
    

## CS Stage with Diode-Connected Load

![[Screenshot_2023-12-02_at_10.12.30_PM.png]]

- 위의 Diode-Connected device가 $R_D$﻿의 역할을 하니깐 $R_D$﻿는 Source에서의 Impedance로 볼 수 있음
- body effect 뭐라그러냐 그거를 고려할 때는 병렬 연결로 취급할 것
- PMOS를 Load로 연결하는 경우는 다음과 같다
    
    ![[Screenshot_2023-12-02_at_10.15.18_PM.png]]
    

## CS Stage with Degeneration

![[Screenshot_2023-12-02_at_10.17.28_PM.png]]

- Source에 저항이 연결된 경우 gain이 줄어든다
- diode-connected device같은 경우는 source impedance가 저리된다
    
    ![[Screenshot_2023-12-02_at_10.20.44_PM.png]]
    

## CS Stage with Degeneration and its output impedance

![[Screenshot_2023-12-02_at_10.21.11_PM.png]]

- Degeneration은 output impedance를 높이는 역할을 합니다.
    
    ![[Screenshot_2023-12-02_at_10.27.54_PM.png]]
    

## CS Stage with DEgeneration by Inclusion Gate Resistance

![[Screenshot_2023-12-02_at_10.29.55_PM.png]]

- Gate에는 resistance가 연결되어도 딱히 gain이나 impedance에 영향을 주지는 않습니다.
    - 그래서 BJT보다 수십배 편하다
- 다음은 예시이다
    
    ![[Screenshot_2023-12-02_at_10.32.47_PM.png]]