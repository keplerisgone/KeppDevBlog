---
Created: 2023-09-21T20:47
Parent item:
  - "[[2학년 2학기/전자회로(1)/PN Junction Diode\\|PN Junction Diode]]"
---
## PN Junction Diode

![[Media/Untitled 39.png|Untitled 39.png]]

N-type으로 doping한 semiconductor와 P-type으로 doping한 semiconductor를 접합시키면 PN Junction Diode가 됩니다.

다이오드의 기호는 오른쪽에 나와있는 것과 같습니다. bar와 삼각형으로 이루어져있는데, 다이오드에서 전류는 항상 삼각형에서 bar로 흐릅니다.

즉, bar 부분이 Cathode (-), 삼각형 부분이 Anode (+)입니다.

## Diode Operating Region

![[Media/Untitled 1 30.png|Untitled 1 30.png]]

Diode에 전압을 걸어주는 다양한 상황을 Diode Operating Region이라고 하는데, 다음과 같은 세 가지 상황이 존재합니다.

- PN Junction in Equilibrium
    - 걸어주는 전압이 0일 때입니다. Depletion Region(이따 나옴)을 가지며, Built-in Potential 을 가집니다.
- Reverse Bias
    - 다이오드와 반대의 방향으로 전압이 걸린 경우입니다.
    - Junction Capacitance를 가지는데, 이 원리에 대해서는 다음에 나옵니다.
    - 전류 I가 아주 약간의 negative constant를 갖습니다.
- Forward Bias
    - 다이오드과 같은 방향으로 전압이 걸린 경우입니다.
    - 이 때는 I와 V를 계산하게 되는데, 이에 대해서는 나중에 알아봅시다.
    - exponential current를 가집니다. (그래프 참고)

## Carrier Diffusion across Junction

![[Media/Untitled 2 29.png|Untitled 2 29.png]]

n-side의 major carrier는 electron, p-side의 major carrier는 hole입니다. 따라서, PN Junction Diode에서 각 carrier concentration은 다음과 같이 나타납니다.

따라서, concentration의 차이에 따른 Diffusion이 발생, Diffusion current가 발생합니다.

또한, 중간의 구역에서 electron와 hole의 recombination이 일어나 depletion region을 형성합니다.

## Depletion Region

![[Media/Untitled 3 28.png|Untitled 3 28.png]]

중간의 free electrons와 Free holes가 결합해 생긴 공간입니다. carrier의 농도가 매우매우매우 적어 insulator의 기능을 합니다.

중간에는 ionized된 donor와 acceptor가 존재하긴 하지만, 이들은 Carrier(electrons, holes)와 달리 immobile하기 떄문에 전류를 흐르게 할 수는 없습니다.

계속 이들이 결합하다보면 Depletion Region이 점점 더 넓어지게 되고, 이에 따라 recombination이 멈추게 됩니다.

두 개의 carrier가 가득한 공간을 quasineutral region이라고 합니다. 두 개의 전류가 흐르는 판과 띄어져 있는 공간… 이거 완전 capacitor 아닙니까? 따라서 잘 처리된 PN Junction Diode는 capacitor와 비슷한 역할을 합니다.

### Carrier Drift across the Junction

![[Media/Untitled 4 21.png|Untitled 4 21.png]]

Depletion Region에서는 이온들에 의해 charge density가 0이 아니기 때문에, Electric field로 인한 drift current가 발생하게 됩니다.

### Depletion Approximation

![[Media/Untitled 5 17.png|Untitled 5 17.png]]

두 region에 의해 발생하는 Electric field의 방향과 세기가 모두 같음을 이용합니다.

결론적으로 말하면, 두 region의 너비의 비와 donor, acceptor concentraion를 각각 곱한 값은 같습니다.

### Built-in Potential $V_0$﻿

평형 상태에서는 drift current와 diffusion current이 평형을 이루어 전류가 흐르지 않습니다. 이 때, ==평형은== ==$V_D=0$==﻿==을 의미합니다==.

평형 상태에서 Depletion region에 걸리는 전압을 ==Built-in Potential==이라고 합니다. 계산은 다음과 같습니다.

![[Media/Untitled 6 15.png|Untitled 6 15.png]]

상온에서는 700~800mV의 값을 가집니다.

## Under reverse bias

![[Media/Untitled 7 13.png|Untitled 7 13.png]]

Reverse bias 상태의 경우, 반대 방향으로 전압을 걸어줬기 때문에 carrier가 전압을 따라 이동해 Depletion region의 크기가 매우 커지게 됩니다. (==중요한 것은== ==$W_{dep}\propto V_R !$==﻿==)==

![[Media/Untitled 8 11.png|Untitled 8 11.png]]

여기서 기억해야 할 것! PN Junction Diode는 Capacitor와 유사하게 동작합니다. Capacitor는 두 개의 plate 사이의 거리에 의해 capacitance가 정해지는 것이 기억나실 겁니다.

마찬가지로, Diode에 걸어주는 reverse bias 전압 $V_R$﻿에 따라 region의 너비 $W_{dep}$﻿이 결정된다면, $V_R$﻿에 따라 $C_j$﻿ (Junction Capacitance)가 결정될 것입니다!

![[Media/Untitled 9 2.png|Untitled 9 2.png]]

이렇게 걸어주는 reverse 전압에 따라 C를 달리할 수 있는 것을 voltage controlled oscillator라고 하고, Varactor (Varient capacitor…?) 로서 동작합니다.

## Under Forward Bias

![[Media/Untitled 10 2.png|Untitled 10 2.png]]

다이오드의 방향으로 전압을 걸면 발생합니다. carrier들이 밀려나 ==minority carrier injection==이 발생, region의 너비가 줄어듭니다!

### Minority Carrier Injection

![[Media/Untitled 11 2.png|Untitled 11 2.png]]

이는 region의 너비가 줄어듦으로써 발생합니다. 각 carrier들이 Diffusion을 통해 건너가는 것을 말합니다.

이 때 concentraion은 exponentially 감소하는데, 이는 Forward Bias 에서 전류가 exponential한 이유입니다!

## I-V Characteristics of a PN Junction

![[Media/Untitled 12 2.png|Untitled 12 2.png]]

위의 그래프는 각 상황에서의 전류를 나타냅니다.

### Reverse breakdown

![[Media/Untitled 13 2.png|Untitled 13 2.png]]

Reverse bias가 계속해서 증가할때(절대값이!) 어느순간 전류가 와장창 음수로 가버려 전류가 흐르게 되는 현상입니다. 두 가지 종류가 있습니다.

- ==Zener breakdown==은 갑자기 굉장히 P와 N이 고농도가 되어서 높은 전기장을 형성했을 때 발생합니다. (이를 tunneling이라고 합니다.) 너무 갑작스레 에너지를 얻어버린 carrier들이 공유 결합을 끊어버려 EHP를 증가시킵니다.
- ==Avalanche breakdown==은 Zener보다 적당히 덜 도핑되었을 때, 단순한 E field의 가속으로 carrier가 빠르게 움직일 때 발생합니다. (공유결합은 끊지 않습니다. Zener 쪽이 얼마나 강한거야) 달려가는 carrier들은 다른 carrier와 부딪히며 연쇄 반응을 일으킵니다.

## Constant Voltage diode Model

![[Media/Untitled 14 2.png|Untitled 14 2.png]]

따로 있는 법칙같은 것은 아니고, 회로를 Linear하게 생각하기 위해 만든 일종의 모델입니다. (그러면서 정작 다이오드는 선형이 아님)

실제 diode는 exponential한 결과를 보이지만, 편하게 생각하기 위해서 $V_{D,on}$﻿ 이상으로 다이오드 전압이 들어가면, ==$V_D=V_{D,on}$==﻿==으로 취급하기로 합시다!==

여기서 $V_{D,on}$﻿은 평형 상태의 built-in potential을 뜻합니다. 잘 보면 값도 700~800mV죠?

왜 쓰냐면… exponential model은 iteration을 요구합니다. 계산이 굉장히 힘듭니다.

## Small-Signal Analysis

small-signal resistance를 근사적으로 구하기. Taylor series 이용!

![[Media/Untitled 15 2.png|Untitled 15 2.png]]

어쨌든 small signal 에서 $r_d= {V_T \over I_D}$﻿ 입니다.

> [!important]  
> 이게 한참 이해가 안 됐었습니다.다이오드는 비선형(non-linear) 소자입니다. 따라서 이를 선형으로 생각하기 위해서, 정말 작은 신호에 대해서(small signal) 다이오드를 작은 저항으로 생각하기로 합시다. (resistance)그래서 굳이 미분한 다음에 Talyer series를 이용해 근사를 구하는겁니다!왜 굳이 미분을 하냐면 옴의 법칙에서 기울기가 저항의 역수이기 때문!  

## Small Sinusoidal Analysis

![[Media/Untitled 16 2.png|Untitled 16 2.png]]

하나의 작은 amplitude를 가지고 있는 sinusoidal wave는 DC wave로 처리할 수 있습니다. 결국 옴의 법칙을 적용할 수 있다는 이야기입니다!