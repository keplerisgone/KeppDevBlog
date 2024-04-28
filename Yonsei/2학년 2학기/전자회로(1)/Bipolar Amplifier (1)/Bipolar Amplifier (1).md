---
Created: 2023-10-16T18:15
---
## Voltage Amplifier

![[Screenshot_2023-10-29_at_8.23.38_PM.png]]

voltage amplifier가 잘 동작하려면, input impedance는 무한대에 가깝고, output impedance는 0에 가까워야합니다.

![[Screenshot_2023-10-29_at_8.23.45_PM.png]]

그래야만 input이 온전하게 전달되고 → output이 들어온 만큼 나오기 때문입니다.

## I/O Impedances

그렇다면 input/output impedance는 어떻게 판별할 수 있을까요?

![[Screenshot_2023-10-29_at_8.26.28_PM.png]]

impedance는 측정하고 싶은 port에 test source를 연결한 뒤 테스트 전압과 전류의 비로 구합니다.

하지만 input은 independent source들을 모두 zero로 만들어 회로가 open되고, output의 경우에는 외부 회로가 연결되어 회로가 short로 취급된다는 점이 다릅니다.

또한 I/O Impedance는 small-signal model에서 취급되는 것입니다.

I/O impedance는 각 노드에서 계산이 가능합니다.

## Impedance seen at the Collector

Collector에서의 Output impedance는 다음과 같이 계산됩니다.

(input impedance 같은 경우는 Base에 다른 회로가 연결되어 있지 않기 때문에 $r_\pi$﻿로 동일함)

![[Screenshot_2023-10-29_at_8.34.02_PM.png]]

$r_O$﻿의 값과 같습니다.

## Impedance seen at the Emitter

Emitter에서 측정한 Output impedance의 값은 다음과 같습니다.

![[Screenshot_2023-10-29_at_8.35.20_PM.png]]

Emitter에 test source를 연결합니다.

그 후 KCL을 적용해 전압과 전류의 비율을 계산하면 됩니다.

transconductance의 역수와 값이 같네요!

> [!important]  
> Base에서의 Impedance를 구하지 않는 이유는 뭘까요?아니 상식적으로 생각을 해봤을 때 input 들어오는 곳에서 output을 측정하고 싶겠어요???  

## Biasing of BJT

1. BJT가 active region가 되어야 합니다.
2. 그 뒤 small-signal model의 parameter를 bias condition을 이용해 구합니다.

## Bad Biasing

![[Screenshot_2023-10-29_at_9.02.12_PM.png]]

위의 예시에서는 output으로 나와야 하는 전압이 존재해야 하지만 input으로 들어가는 값이 너무 작기 때문에 biasing이 되지 못했고, amplifier로서 동작하지 않습니다.

biasing의 두 조건을 만족하지 못합니다.

![[Screenshot_2023-10-29_at_9.03.20_PM.png]]

이 경우는 우선 회로가 short되어 있기 때문에 전류가 amplifier로 들어가지 않고, 그리고 $V_{BE}$﻿가 저렇게 커버리면 회로가 탑니다.

## Biasing with Base Resistor

Base 부분에 굉장히 큰 저항을 달아 Biasing하는 방법입니다.

![[Screenshot_2023-10-29_at_9.13.20_PM.png]]

이 때의 Biasing 조건은 다음과 같습니다.

> $V_{CC}-\beta(V_{CC}-V_{BE}/R_B)R_C>V_{BE}$﻿

따라서 해당 Biasing은 온도, $\beta$﻿, parameter 들의 값에 영향을 크게 받는 것을 알 수 있습니다.

## REsistive Divider

![[Screenshot_2023-10-29_at_9.17.51_PM.png]]

위의 방법을 개량한 형태로, $\beta$﻿의 값에 의존하지 않습니다.

> [!important]  
> Base Current를 무시합니다.  

## Acounting for Base Current

위에서 $V_{BE}$﻿가 저항의 식으로 표현되는 것을 보고 이를 Thevenin으로 바꾼 형태입니다.

![[Screenshot_2023-10-29_at_9.19.21_PM.png]]

==Base current가 0에 가깝다는 것을 기반으로 합니다. (그래서== ==$V_{thev}$==﻿==와== ==$R_{Thev}$==﻿==가 붙을 수 있는 것)==

하지만 Base current를 처음에는 무시하여 계산하였더라도, $I_C$﻿와 $V_{BE}$﻿의 점화식으로 $I_B$﻿의 값을 좀 더 정확히 계산할 수 있습니다. 한 번은 다시 계산합시다!

## Emitter Degeneration Biasing

Emitter에 저항을 달아 Biasing 하는 방법입니다.

![[Screenshot_2023-10-29_at_9.38.42_PM.png]]

계산식을 보면 $V_T$﻿가 존재하지 않아 온도에 영향을 적게 받는 것을 알 수 있고, 무엇보다 식이 Linear 한 것을 알 수 있습니다!

하지만 gain이 reduce된다는 점에서 좋은 amp는 아니네요…

## Self-Biasing Technique

![[Screenshot_2023-10-29_at_9.47.22_PM.png]]

Collector에 연결되어 있는 것을 Base에 끌어다 연결하는 Biasing입니다.

![[Screenshot_2023-10-29_at_9.47.52_PM.png]]

식은 다음과 같으며, 디자인 조건은 다음과 같습니다.

1. $R_C$﻿가 $R_B/\beta$﻿보다 훨씬 클 것.
2. $\Delta V_{BE} << V_{CC}- V_{BE}$﻿ 일 것.

모든 Bias Technique을 종합하면 다음과 같습니다. 진화과정 같네요.

![[Screenshot_2023-10-29_at_9.49.54_PM.png]]

## PNP BJT Biasing Techniques

NPN과 저항을 달아주는 부위가 같습니다. 기능 또한 동일합니다.

![[Screenshot_2023-10-29_at_9.51.37_PM.png]]

## Possible way to have Amplifier configurations

input/output terminal의 조합은 이론상 3x3이 가능하지만, active mode를 고려한다면 가능한 조합은 세 개뿐입니다.

다음 과정을 통해 세 가지 topology에 대해서 알아봅시다.

## Common-Emiter (CE) Topology

![[Screenshot_2023-10-29_at_9.56.32_PM.png]]

Base가 input, Collector가 output인 Topology입니다.

Common-Emitter인 이유도 Emitter가 가만히 있어서래요.

## Voltage gain / Headroom Tradeoff

- voltage gain은 평소와 같이 계산하면 됩니다.
- voltage headroom이란 Saturation 상태에서 Voltage가 얼마나 Swing할 수 있는가? 를 나타내는 것입니다.
    - gain이 계속 증가하면 좋겠지만, Headroom 때문에 계속 증가할 수는 없습니다. 이를 Trade-off라고 합니다.
- gain와 impedance 사이의 상관관계, 하나를 얻으면 하나를 잃습니다.

![[Screenshot_2023-10-29_at_10.17.04_PM.png]]

## Inclusion of the Early Effect

Early effect를 고려한다면 SSM에 $r_O$﻿가 추가된다는 사실을 기억하시나요?

추가된 $r_o$﻿로 인해 $R_{out}$﻿와 voltage gain의 값이 달라집니다.

![[Screenshot_2023-10-31_at_9.26.17_PM.png]]

## Intrinsic Gain

위의 Early effect를 고려한 회로에서 $R_c$﻿를 무한대로 보내면 $A_v$﻿의 값이 최대가 되는데, 이 때 얻어지는 gain을 intrinsic gain이라고 합니다.

$I_C$﻿에 의존하지 않습니다.

![[Screenshot_2023-10-31_at_9.28.07_PM.png]]

## Current Gain, $A_I$﻿

당연하게도 $i_{out}$﻿과 $i_{in}$﻿의 비율입니다. Common-emitter stage에서는 $\beta$﻿와 같습니다.

![[Screenshot_2023-10-31_at_9.29.55_PM.png]]