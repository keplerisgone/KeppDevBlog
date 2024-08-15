---
Created: 2023-12-02T23:12
---
## NMOS Cascode Stage

![[Screenshot_2023-12-02_at_11.13.14_PM.png]]

- NMOS를 직렬로 연결했다 이거 완전 그거랑 똑같은데 아래에 load resistance 대신에 MOS 연결한 거
- 아무튼 $R_{out}$﻿의 값은 다음과 같대요

## PMOS Cascode Stage

![[Screenshot_2023-12-02_at_11.43.11_PM.png]]

## Short-Citcuit Transconductance

![[Screenshot_2023-12-02_at_11.43.41_PM.png]]

- 어느 회로에서나 성립하는 transconductance
- input voltage에 따른 output current의 비이다

## Transconductance Example

![[Screenshot_2023-12-02_at_11.42.57_PM.png]]

- 아니 근데 왜 output 단에서의 current를 측정할 수 있는 것이죠

## MOS Cascode Amplifier

![[Screenshot_2023-12-02_at_11.43.54_PM.png]]

- 위의 $i_{out}$﻿은 $i_{D2}, i_{D1}$﻿과 같다!
- 따라서 gain을 transconductance에 따른 gain을 계산하면 다음과 같다

## PMOS Cascode Current source as Load

![[Screenshot_2023-12-02_at_11.46.04_PM.png]]

- 위의 current source를 PMOS로 대체해보았다
- 역시 계속 쌓을 수록 gain이 증가하지만 트랜지스터의 수는 늘어나겠지
    - ideal current source에 가까워지기 때문

> [!important]  
> Diode Connected device- two terminal device이고 @import url('https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.css')VGS=VDSV_{GS}=V_{DS}VGS​=VDS​﻿이기 때문에 diode의 특성을 지님 -resistance 측면에서 봐도… ![[Screenshot_2023-12-05_at_2.46.40_PM.png]]  

## Concept of a Current Mirror

![[Screenshot_2023-12-05_at_2.47.07_PM.png]]

- single transistor로는 수많은 variation이 생김
    - $I_D$﻿가 대표적
- 그래서 전류를 보내는 current mirror를 설계
- always in saturation

> [!important]  
> 어케 variation을 줄인다는 거임 - 아래에 나옴  

## MOS Current Mirror

![[Screenshot_2023-12-05_at_2.47.18_PM.png]]

- MOS 두 개를 이용해서 전류를 보냄
- $W/L$﻿의 비율에 따라 전류가 결정되므로 variation을 줄인다는 거니
- 근데 DCD가 아닌 경우는 voltage가 define되지 않으므로 mirror가 아님
    
    ![[Screenshot_2023-12-05_at_2.47.34_PM.png]]
    

## Current Scaling

![[Screenshot_2023-12-05_at_2.48.00_PM.png]]

- $W/L$﻿을 이용해 전류를 바꿀 수 있다
- 아니 근데 gate current는 0이잖아
    - 그래서 편한건데.
- Good current source!

![[Screenshot_2023-12-05_at_2.48.09_PM.png]]

## BJT Current Mirror Circuitry

![[Screenshot_2023-12-05_at_2.48.19_PM.png]]

- BJT로 설계하는 Current MIrror
- always in forward active
- 여기는 Area가 관여 ($I_{S,1}/I_{S,REF}=A_{E,1}/A_{E,REF}$﻿)
- 근데 여기는 base current가 있음
    - 아 진짜
- 물론 장점이 있다 - amp라던가 공간차지 라던가
- DCD가 아니면 안 된다 - Vx가 정의되지 않음, 그리고 모든 transistor가 cutoff가 된다
    
    ![[Screenshot_2023-12-05_at_2.48.31_PM.png]]
    

## Multiple Copies of I_REF

![[Screenshot_2023-12-05_at_2.49.12_PM.png]]

- 엉,

## Current Scaling

![[Screenshot_2023-12-05_at_2.49.19_PM.png]]

- transistor의 개수로 복사 가능
- 전류가 복사가 된다고

![[Screenshot_2023-12-05_at_2.49.31_PM.png]]

## Fractional Scaling

![[Screenshot_2023-12-05_at_2.49.40_PM.png]]

- 줄일 수도 있다
- DCD 의 개수에 따라서 줄어들긴 한다

![[Screenshot_2023-12-05_at_2.49.50_PM.png]]

## Effect of Base Currents

![[Screenshot_2023-12-05_at_2.50.24_PM.png]]

- base currnet를 어쩔 것인가
- 뭐 어쩌구 저쩌구 계산하면…
    
    - non-ideal : $I_{copy} = {nI_{REF}\over 1 + 1/\beta (n+1)}$﻿
    - ideal : $I_{copy} = nI_{REF}$﻿
    
    ![[Media/Untitled 40.png|Untitled 40.png]]
    
    - 아래의 $1/\beta(n+1)$﻿ term이 오류를 일으킴

## Improved Mirroring Accuracy

![[Screenshot_2023-12-09_at_7.21.22_PM.png]]

- 위에 트랜지스터 하나를 더 연결함으로써 $I_{copy}$﻿가 저래 되기 때문에 에러가 줄어듦
- $I_{copy}={nI_{REF}\over 1+{1\over \beta^2} (n+1)}$﻿
- 증명은 니가해

## What else

![[Screenshot_2023-12-09_at_7.21.34_PM.png]]

- advantage of CMOS Current mirror
    - gate current가 없어서 계산하기 쉽다
    - lower power application is required
- disadvantage ‘’
- advantage of BJT Current mirror
    - excellent current replication accuracy
- disadvantage ‘’
    - complicated to design - we should consider $\beta$