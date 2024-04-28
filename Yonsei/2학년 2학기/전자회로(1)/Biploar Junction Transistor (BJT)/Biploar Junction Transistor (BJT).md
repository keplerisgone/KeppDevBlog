---
Created: 2023-10-04T19:49
Parent item:
  - "[[Bipolar transistors]]"
---
![[Screenshot_2023-10-04_at_7.51.47_PM.png]]

이전의 아이디어에서, dependent current source를 exponential한 형태로 바꿔봅시다. (Diode Current by Diffusion)

이렇게 출발해서 만들어진 것이 바로 BJT입니다.

## Reverse-Biased PN Junction as a Current Source

![[Screenshot_2023-10-04_at_8.00.10_PM.png]]

PN 다이오드에 reverse bias 전압을 걸어주면, depletion region에서 electron injection = Minority Carrier injection이 일어나 reverse current가 증가하게 됩니다.

이 때 injection되는 eletron = minority carrier의 수가 많을 수록 current의 세기가 증가합니다. reverse bias voltage의 크기는 상관없습니다!

> [!important]  
> 물론 일반적인 상황에서 전류가 걸리는 것은 아니고, 외부에서 electron이 많이 공급되어 inject되어야 reverse current가 증가하는 것으로 보입니다.  

## BJT Structure and circuit symbol

![[Screenshot_2023-10-04_at_8.01.58_PM.png]]

BJT의 구조는 다음과 같습니다. npn 형태로 다이오드가 접합되어 있으며, 순방향이 걸려있는 쪽이 Base-Emitter, 역방향이 걸려있는 쪽이 Collector-Base입니다.

symbol의 뜻은 역시나 전류의 방향을 나타냅니다.

## NPN BJT Operation

![[Screenshot_2023-10-04_at_8.12.25_PM.png]]

1. ==BE에 순방향 바이어스==를 걸어줍니다. Emitter junction에서 전자가 빠져나와 Collector junction으로 이동합니다.
2. ==CB에는 역방향 바이어스==가 걸려있습니다. 위의 예시처럼 Electron injection이 일어나 reverse current가 흐르게 됩니다.

또한 일반적인 다이오드의 연결로 표현할 수는 없습니다.

> [!important]  
> 일반적인 다이오드로 표현할 수 없는 이유는, BJT에서의 Base는 너무나도 작기 때문입니다. Base가 너무나도 작기 때문에 hole의 움직임은 무시됩니다.  

![[Screenshot_2023-10-04_at_8.16.28_PM.png]]

각 성분들을 설명하면 다음과 같습니다.

- $I_C$﻿ : 컬렉터 전류입니다. Emitter에서 빠져나간 전자가 Collector junction의 역방향 바이어스를 만나 전류가 흐르게 됩니다. 이는 Diffusion에 의한 것입니다.
- $I_B$﻿ : 베이스 전류입니다. Base의 major carrier인 hole이 emitter에서 빠져나온 전자와 일부 결합하여 흐르게 되는 전류입니다. 사회의 해악입니다.
- current gain $\beta = {I_C \over I_B}$﻿ 입니다.

## Base current

![[Screenshot_2023-10-04_at_8.24.10_PM.png]]

Base current는 Base의 hole이 injection되거나 recombination되면 발생합니다.

- Emitter에서 방출된 전자가 Base의 hole을 만나 recombination
- hole이 base에서 방출됨, Emitter로 이동

존재 자체가 loss current입니다.

  

전체적인 과정을 정리하면 다음과 같습니다.

1. emitter에서 방출된 전자는 collector junction까지 도달 (Base가 얆기 때문)
    1. 이는 Diffusion 때문, (collector junction에서는 E field 때문에 전자가 쓸려나가서 없을 것)
2. built-in E field를 만남 (reverse bias 때문)
3. collector로 전자가 이동, Collector current가 생성!

## BJT Design

curretn gain을 높이기 위해서는 base current를 줄이고, collector current를 증가시켜야 합니다.

$I_B$﻿ 는 recombination을 줄이면 되므로..

- Base를 얇게 만듭니다.
- Base를 약하게 도핑시킵니다.

$I_C$﻿ 는 minority carrier를 늘리면 되므로..

- Emitter를 강하게 도핑시킵니다.

## Carrier Transport in Base

![[Screenshot_2023-10-04_at_8.26.52_PM.png]]

Base를 무조건 얇게 만들어야 linear 하게 다룰 수 있습니다. 그렇지 않으면 eletron의 농도가 exponential하게 감소하기 때문에, linear하게 다룰 수 없습니다.

![[Screenshot_2023-10-04_at_8.29.15_PM.png]]

## Collector current

![[Screenshot_2023-10-04_at_8.30.15_PM.png]]

input voltage에 따른 collector current도 구할 수 있습니다. → voltage controlled current source

물론 base가 얇아야겠죠?

## Emitter current

![[Screenshot_2023-10-04_at_8.31.02_PM.png]]

Emitter current는 KCL을 이용해 구합니다.

## Simple BJT amplifier

BJT는 amplifier의 기능도 겸하고 있습니다!

![[Screenshot_2023-10-05_at_9.02.40_PM.png]]

![[Screenshot_2023-10-05_at_9.07.30_PM.png]]

## BJT as a constant current source

BJT의 $I_C$﻿는 $V_{CE}$﻿의 영향을 받지 않고 오로지 $V_{BE}$﻿의 영향을 받기 때문에, constant current source로서 기능할 수 있습니다.

![[Screenshot_2023-10-05_at_9.09.36_PM.png]]

### Constraint on Load Resistance

![[Screenshot_2023-10-05_at_9.11.49_PM.png]]

Load resistance의 값을 키우지 않는 이유는, 이 값이 커질수록 $V_x$﻿의 값이 줄어들어 transistor가 작동하지 않기 때문입니다.

### BJT I-V Characteristics

![[Screenshot_2023-10-05_at_10.12.08_PM.png]]

두 가지 모델이 있습니다.

- $V_{BE}$﻿가 변하는 경우
    - $I_C$﻿의 관계식 덕분에 $V_{BE}$﻿가 변함에 따라 $I_C$﻿또한 바뀝니다.
- $V_{CE}$﻿가 변하는 경우
    - 미리 고정된 $V_{BE}$﻿의 값에 따라 $I_C$﻿가 고정됩니다.