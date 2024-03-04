---
Created: 2023-11-17T01:28
---
## Outline

![[Screenshot_2023-11-17_at_1.30.05_AM.png]]

## Moore’s Law

![[Screenshot_2023-11-17_at_1.30.22_AM.png]]

2년마다 하나의 칩에 들어갈 수 있는 트랜지스터의 개수가 두 배가 된다

## Pros and Cons of BJT and MOSFETs

![[Screenshot_2023-11-17_at_1.31.51_AM.png]]

- BJT
    - gm이 다 높기 떄문에 amplifier로서는 더 낫다
    - turn on voltage를 예측할 수 있다
    - bandwidth가 넓다
    - 고주파수 대역에서 높은 효과를 보인다
    - gain이 높다
    - 높은 전력?에서도 동작이 가능
    - 더 linear하다
    - 아날로그 회로에서 강점을 보임
- MOSFET
    - 더 빠르다 → 스위치로서는 얘가 더 낫다
    - device to device variation으로 고통받지 않는다
    - 격자로 설계하기가 쉽다 (이건 나중에 배움) → 대칭성과 관련있다
    - 노이즈가 적다
    - 더 작게 만들 수 있다
    - 디지털 회로에서 강점을 보인다

## The MOSFET

![[Screenshot_2023-11-17_at_1.32.28_AM.png]]

- Electric field → drift current를 이용해 전류를 보내는 소자
- symmetric device → 연결이 쉽다 BJT는 아니다. → 격자로 짜기가 쉽다
- treshold voltage는 뭔가 바닥

## N-Channel MOSFET Structure

![[Screenshot_2023-11-17_at_1.39.26_AM.png]]

- p- substrate - p-type 도핑. - body라고도 부름
- source와 drain은 n-type 도핑
- Insulator는 SiO2로 이루어짐
    - 여기가 capacitor 역할을 하는 부분
    - 두께가 낮아질수록
- Circuit symbol
    
    ![[Screenshot_2023-11-17_at_1.42.09_AM.png]]
    

## Idea of MOS Transistor

![[Screenshot_2023-11-17_at_1.42.56_AM.png]]

- cap을 빌드 → 두 단에 전하가 걸리게 한다
- electric field를 제공 - charge를 이동시킨다
- 다른 배터리에 연결해 전류를 연결 → 모아놓은 charge의 이동

## Channel Formation

![[Screenshot_2023-11-17_at_1.46.22_AM.png]]

두가지 경우로 나누어서 생각해봅시다.

- $V_G$﻿ (gate voltage) $<$﻿ $V_{TH} $﻿ (Treshold voltage)
    - insulator에서 hole을 밀어내고, 음이온이 생겨 depletion region이 생깁니다. 이 때는 전류가 흐르지 않는다
- $V_G > V_{TH}$﻿
    - insulator에서 electron이 나와 conduction layer에 쌓입니다. → inversion layer가 생김
    - inversion layer의 전자가 source에서 drain으로 움직이며 전류가 흐릅니다.
    - $V_G$﻿의 값이 올라가면 전자의 농도가 올라가 전류의 세기가 증가합니다.

## Voltage-Dependent Resistor

![[Screenshot_2023-11-17_at_1.47.51_AM.png]]

- Drain에 voltage source가 있는 경우 ($V_G$﻿를 고정시키고)
    - $V_D$﻿이 증가함에 따라 linear로 $I_D$﻿가 증가
    - $V_G$﻿의 값이 증가함에 따라 $I_D$﻿가 증가, 저항이 낮아짐
- channel은 저항의 직렬 연결로 생각할 수 있습니다.

## Channel L/W Dependence

![[Screenshot_2023-11-17_at_1.48.20_AM.png]]

- channel의 길이가 줄어들수록 저항이 낮아지므로 기울기는 커짐
- width가 늘어나면 저항이 줄어들기 때문에 (단면적의 증가) 기울기가 커짐

## Comparison: BJT vs MOSFET

![[Screenshot_2023-11-17_at_1.48.44_AM.png]]

![[Screenshot_2023-11-17_at_1.49.06_AM.png]]

- BJT는 diffusion에 의해서 전류가 발생
- MOSFET은 drift에 의해서 전류가 발생
- → $I_C$﻿가 더 크니깐 BJT가 amp로써는 더욱 좋다

## MOS Capacitor

![[Screenshot_2023-11-17_at_1.49.25_AM.png]]

- MOS의 구조는 capacitor와 같다

## MOSFET in ON State

![[Screenshot_2023-11-17_at_1.50.00_AM.png]]

- $C=Q/V$﻿ 임을 이용
- $C_{ox}$﻿는 gate capacitance per unit area
- $V_{GS}-V_{TH}$﻿는 overide voltage ($V_{DS}$﻿) → 어차피 $V_{TH}$﻿보다는 높으므로

## MOSFET as Voltage-Controlled Resistor

![[Screenshot_2023-11-17_at_1.50.28_AM.png]]

- $t_{inv}$﻿는 thickness겠지?
- 아무튼 Resistance는 저렇게 구할 수 있다~
- 작은 $V_{DS}$﻿에서만 한정임

## MOSFET Channel Potential Variation

![[Screenshot_2023-11-17_at_1.50.53_AM.png]]

- $V_D$﻿가 존재할 때만!
- 이거는 단순한 KVL에 의해서도 알 수 있듯이 Source로 갈수록 voltage가 줄어든다.
- 그렇다면 반대로 $Q_{inv}$﻿는…

## Maximum Output Impedance

![[Screenshot_2023-11-29_at_9.45.40_PM.png]]

- 줄어드는 voltage에 따른 새로운 식이 생김
    - $Q_{inv} (y)=C_{ox}[V_{GS}-V_{TH}-V_C(y)]$﻿
- 전류는 charge의 속도이므로
    - $I_D = WQ_{inv}(y)\cdot v(y)$﻿
    - $v(y) = \mu_nE=\mu_n {dV_C(y) \over dy}$﻿ → drift current니깐..

## Drain Current

![[Screenshot_2023-11-29_at_9.51.01_PM.png]]

- $V_{DS} < V_{GS} - V_{TH}$﻿일 경우에만,
- 식이 저렇게 나옴 → $I_D$﻿는$ $﻿ $V_{DS}$﻿에 quadratic하다
    
    ![[Screenshot_2023-11-29_at_9.55.42_PM.png]]
    
    - $V_{GS}$﻿가 constant 할 경우
    - maximum value는 $V_{DS} = V_{GS} - V_{TH}$﻿일 경우

## Inversion layer Pinch-off

![[Screenshot_2023-11-29_at_9.58.15_PM.png]]

- $V_{DS} = V_{GS} - V_{TH}$﻿일 경우는 $Q=0$﻿이기 때문에 움직일 charge가 존재하지 않음
    - → channel이 pinch-off 되었다
- $V_{DS}$﻿가 계속 높아질 경우에는 $Q=0$﻿인 지점이 source로 계속 이동함
    - 이때는 $L_1 -L$﻿에서 depletion region이 존재
- BJT와의 차이점?
    
    ![[Screenshot_2023-11-29_at_10.03.25_PM.png]]
    

## Current Flow in Pinch-off Region

![[Screenshot_2023-11-29_at_10.05.06_PM.png]]

- pinch-off region에서는 depletion region이 생기므로, Electric field가 생긴다
- Electric field에 의해 pinch-off 에 존재하는 charge가 이동하므로 → constant한 current

> [!important]  
> length가 줄어들지 않나요?엄청 조금 줄어들어서 상관없음  

## Drain Current Saturation

![[Screenshot_2023-11-29_at_10.07.36_PM.png]]

- 그래서 그래프가 저렇게 된단다

## MOSFET Regions of Operation

![[Screenshot_2023-11-29_at_10.14.20_PM.png]]

- 왼쪽은 quadratic으로 증가하는 triode region
- 오른쪽은 constant한 saturation region
- 아래는 상태를 추정하는 법

![[Screenshot_2023-11-29_at_10.16.05_PM.png]]