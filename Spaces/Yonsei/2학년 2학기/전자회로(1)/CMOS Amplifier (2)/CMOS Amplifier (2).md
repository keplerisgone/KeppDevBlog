---
Created: 2023-12-02T22:33
---
## Common-Gate Amplifier Stage

![[Screenshot_2023-12-02_at_10.33.41_PM.png]]

- Output이 Drain에 연결, Input이 Source에 연결되어 둘이 Gate를 공유하고 있는 CMOS Amplifier입니다.
- $V_{RD}$﻿가 감소하면 $V_{out}$﻿이 줄어들어 $I_D$﻿가 증가한다

## Operation in Saturation Region

![[Screenshot_2023-12-02_at_10.35.34_PM.png]]

- MOSFET이 Saturation에 있도록 하기 위해서는 $V_{out}$﻿이 $V_b-V_{TH}$﻿ 아래로 떨어지면 안 됩니다.
- 만약 $V_{out}$﻿이 이하로 떨어진다면 Triode region이나 cutoff에 돌입하게 되는데, 이러면 Headroom effect를 겪게 됩니다.
    - $R_D$﻿를 높임으로서 gain을 올리고자 했다면 headroom에 부딪히게 되는거지

## I/O Impedances of CG Stage

![[Screenshot_2023-12-02_at_10.39.14_PM.png]]

- 나는 이런거 그냥 외워

> [!important]  
> @import url('https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.css')λ≠0\lambda \ne 0λ=0﻿일 떄는 어떡하냐  

## CG Stage with source Resistance

![[Screenshot_2023-12-02_at_10.39.34_PM.png]]

- $v_X$﻿를 이용해서 아무튼 $A_v$﻿를 계산하면 다음과 같습니다.
- body effect를 고려한 gain은 다음과 같습니다.
    
    ![[Screenshot_2023-12-02_at_10.44.57_PM.png]]
    

## CG Stage with Biasing

![[Screenshot_2023-12-02_at_10.47.03_PM.png]]

- 이거는 Gate에 Voltage divider로 biasing한 경우
    - 근데 이거는 Gate에 voltage drop을 주는 경우이기 때문에 gain과 impedance에 영향을 주지 않는다.
    - 그냥 Saturation을 위해 voltage를 전달하기 위함!!

## CG Stage with Gate Resistance

![[Screenshot_2023-12-02_at_10.50.02_PM.png]]

- Gate는 상관없다고!

## CG Stage Example

![[Screenshot_2023-12-02_at_10.50.37_PM.png]]

## Source Follower Stage

![[Screenshot_2023-12-02_at_10.51.54_PM.png]]

- input이 gate에 있고 output이 source에 달려있는 CMOS amplifier이다
- 제일 어려운 부분은 $R_L$﻿과 $r_o$﻿이 병렬이라는 점이다

## Source Follower Exampler

![[Screenshot_2023-12-02_at_10.55.51_PM.png]]

- 아래에 Load resistance 대신에 transitor를 연결하는 경우는 Impedance가 $r_{o2}$﻿이다

## $R_{out}$﻿ of Source Follower

![[Screenshot_2023-12-02_at_10.57.54_PM.png]]

- output impedance의 경우는 load resistance와 위의 imdepance의 병렬 연결

## Source Follower with Biasing

![[Screenshot_2023-12-02_at_11.00.05_PM.png]]

- $V_{DD}$﻿에 의해서 이 MOSFET은 saturation 상태에 있게 됩니다
    - 뭐 아무튼 자세히 설명하자면
    - $V_G$﻿는 $I_G=0$﻿ 이기 때문에 $V_{DD}$﻿와 값이 같음
    - $V_S$﻿는 KVL에 의해 저런 값이 됨
    - 그런데 saturation 조건을 만족하므로 저렇게 됨
- 근데 이거 왜 씀????
    
    ![[Screenshot_2023-12-02_at_11.04.09_PM.png]]
    
    gain을 높여요
    

## Supply-Independent Biasing

![[Screenshot_2023-12-02_at_11.06.14_PM.png]]

- 아래에다 current source 를 붙여서 언제나 saturation으로 만드는 방법
- ideal한 경우는 Load resistance가 무한대이기 때문에 gain이 저렇게 나옴
- non-ideal한 경우는 MOSFET을 붙인 경우인데 Load resistance가 $r_{o2}$﻿임 (물론 감마가 0이 아닐 때)

## MOSFET Amplifier Design

![[Screenshot_2023-12-02_at_11.08.02_PM.png]]

- BJT와 거의 일치
    - DC면 on/off 상태를 결정하는데 쓰인다
    - AC면 parameter를 계산하는데 쓰인다

## MOSFET models

![[Screenshot_2023-12-02_at_11.11.04_PM.png]]

- Large-signal model
- Small-signal model

## Comparison of Amplifier Topologies

![[Screenshot_2023-12-02_at_11.11.52_PM.png]]

- 그렇대

## Examples

![[Screenshot_2023-12-02_at_11.12.14_PM.png]]

![[Screenshot_2023-12-02_at_11.12.22_PM.png]]

![[Screenshot_2023-12-02_at_11.12.34_PM.png]]

> [!important]  
> 알고보니 연달아서 세 개 있을 떄는 친절하게 body effect 줄여준거봐 진짜 ㅗㅈㅅ같다