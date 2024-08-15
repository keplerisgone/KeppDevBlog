---
Created: 2023-11-01T10:00
---
교수님에게 남은 마지막 양심

Introduction

Current density and Ohm’s Law

Governing Equation

Deeper look into the Governing Equation

Relation between Vd and E

Relationship between J and E

Flow of current

Resistance

Real world ohm’s law

Electromotive Force and Kirchhoff’s Voltage Law

Equation of Continuity and Kirchhoff’s Current laws

Power dissipiation

Boundary conditions

Duality of J and D

## Introduction

![[Screenshot_2023-11-01_at_2.02.37_PM.png]]

- Conduction
    
    일반적인 charge의 움직임(electron, hole)에 의한 전류로, Ohm’s law를 적용할 수 있습니다.
    
- Convention
    
    vacuum 상태에서의 electron에 의한 전류로, thunder가 대표적인 예시입니다. Ohm’s law의 적용을 받지 않습니다.
    
- Electrolytic
    
    ion의 움직임에 의한 전류로, Ohm’s Law를 적용받으나 집중적으로 이야기할 주제는 아닙니다.
    

## Current density and Ohm’s Law

- Current Density
    
    말 그대로 전류의 밀도입니다.
    
    - dimension
        
        1,2,3 차원으로 나눌 수 있고, 1차원은 사실상 밀도가 아닌 그냥 전류 $I$﻿이고, 2차원은 surface current density, 3차원은 volume current density입니다.
        
    
    ![[Screenshot_2023-11-01_at_2.02.58_PM.png]]
    
    적분하면 전류가 나옵니다. 전류는 단위 시간당 해당 지점을 통과한 전하의 개수입니다. 따라서 특정 지점의 전하량을 시간에 대해 미분한 값으로 나타냅니다.
    

## Governing Equation

결국 전하가 움직이는 것은 E field 때문입니다. 이를 수식으로 나타내면 다음과 같습니다.

> $\vec{J}=\sigma\vec{E}$﻿

이를 Governing Equation이라고 합니다.

$\sigma$﻿는 conductivity로, 해당 물질 내부에서 전하가 얼마나 잘 움직이는 지를 나타내는 상수입니다.

일단은 증명 과정만 보고, 나중에 자세히 살펴봅시다.

![[Screenshot_2023-11-01_at_2.06.57_PM.png]]

## Deeper look into the Governing Equation

> [!important]  
> 이 때는 ideal conductor가 아닌 good conductor를 생각해야 합니다. E field가 내부에 존재합니다.  

![[Screenshot_2023-11-01_at_2.14.57_PM.png]]

외부 E field가 0일 때, conductor 내부에서는 thermal energy에 의해서 전자가 움직이면서 충돌이 일어납니다.

$V_{th}$﻿는 thermal energy로 인한 전자의 이동속도, time between collisions는 충돌 간격입니다.

![[Screenshot_2023-11-01_at_2.17.08_PM.png]]

외부 E field가 존재할 때는 drift velocity가 존재하며, 이 속도는 $V_d$﻿로 나타납니다. $V_{th}$﻿에 비해서는 많이 낮습니다. 다만 무작위적인 움직임이 아닌 한 방향으로 모든 전하가 이동합니다.

여기서도 충돌이 존재하는데, 충돌이 존재하지 않는다면 전자는 무한히 가속할 것이고, 열 에너지로의 낭비도 이루어지지 않을 것입니다.

> [!important]  
> 그렇다면 충돌에 의해서 steady 하다고 생각할 수 있나요?  

## Relation between Vd and E

drift 속도인 $V_d$﻿와 $E$﻿와의 관계를 생각해봅시다. 유도과정은 다음과 같습니다.

![[Screenshot_2023-11-01_at_2.18.49_PM.png]]

여기에서 상수로 나타나는 term인 $q_et_c/m_e$﻿를 mobility로 정의하기로 했습니다.

그 외에도 속도에 영향을 주는 요인은 격자구조, 재질, 핵 간의 거리 등등이 있습니다.

## Relationship between J and E

이제는 전류의 정의를 이용해 $J$﻿와 $E$﻿의 관계를 알아봅시다.

단위 시간당 해당 지점을 통과하는 전하의 양을 알아내면 됩니다.

![[Screenshot_2023-11-01_at_2.21.37_PM.png]]

> [!important]  
> 근데 왜 저거 volume 쓰냐??  

아무튼 위에서 정리한 $V_d$﻿까지 사용하면 더 정확히 conductivity를 정의할 수 있습니다.

![[Screenshot_2023-11-01_at_2.23.38_PM.png]]

## Flow of current

![[Screenshot_2023-11-01_at_2.27.29_PM.png]]

수식은 복잡하지만, 말로 설명하면 다음과 같습니다.

voltage가 증가하면 E field가 증가하므로 current density 또한 증가합니다.

따라서 voltage과 current는 일정한 비율을 갖게 되며, 이를 Resistance라고 정의합니다.

## Resistance

다음과 같은 어떤 도선에서의 전류와 전압의 비를 구하면 다음과 같고, 이에 따른 Resistance는 다음과 같습니다.

![[Screenshot_2023-11-01_at_7.26.57_PM.png]]

좀 더 정확히는 $R=l/\sigma S$﻿ 입니다. 위의 경우에서는 길이가 1이네요.

### Real world ohm’s law

실제로는 온도에 대한 함수로 표현

![[Screenshot_2023-11-08_at_7.19.43_PM.png]]

## Electromotive Force and Kirchhoff’s Voltage Law

static E field와 current density의 정의($J =\sigma E$﻿) 에서 다음을 이끌어 낼 수 있습니다.

![[Screenshot_2023-11-08_at_7.07.57_PM.png]]

잘 생각해보면 외부적인 전압없이는 charge carrier가 이동할 수 없기 때문에 closed circuit 내부에서 current density의 합은 0이 됩니다. → another energy source가 필요.

![[Screenshot_2023-11-08_at_7.15.40_PM.png]]

전류가 흐를 수 있게 하는 전압차, charge carrier가 이동할 수 있게 하는 전압을 ==electromotive force== (emf) 라고 합니다.

계산은 다음과 같이 하며, $J$﻿에 대한 정의 또한 다시 합니다.

![[Screenshot_2023-11-08_at_7.14.35_PM.png]]

이는 옴의 법칙을 이용해 다음과 같이 표시할 수 있는데, 이를 다시 쓰면 ==KVL==이 됩니다.

![[Screenshot_2023-11-08_at_7.16.39_PM.png]]

## Equation of Continuity and Kirchhoff’s Current laws

principle of conservation of charge를 식으로 나타내기.

![[Screenshot_2023-11-08_at_7.18.59_PM.png]]

divergence theorem 사용.

![[Screenshot_2023-11-08_at_7.20.53_PM.png]]

![[Screenshot_2023-11-08_at_7.21.00_PM.png]]

요게 바로 equation of continuity, steady current에서는 시간에 따른 current density의 변화가 0이므로, $\partial \rho / \partial t = 0$﻿. $\nabla \cdot J =0$﻿.

divergence theorem의 역을 다시 사용하면..

![[Screenshot_2023-11-08_at_7.25.36_PM.png]]

KCL이 나오게 됩니다!

이것을 Ohm’s law에 적용시키면 다음과 같은 식이 튀어나옵니다.

![[Screenshot_2023-11-08_at_7.58.02_PM.png]]

![[Screenshot_2023-11-08_at_7.58.08_PM.png]]

![[Screenshot_2023-11-08_at_7.58.34_PM.png]]

여기서의 $\epsilon/\sigma$﻿을 relaxation time이라고 합니다.

> [!important]  
> 그러면 시간이 흐른뒤에 흩어진 차지는 어디로 가나요  

## Power dissipiation

하나의 charge carrier가 가지고 있는 power, energy를 계산하면 다음과 같습니다.

work = force x distance임을 이용, $\Delta w=qE\cdot\Delta l$﻿,

power 계산, $\lim_{\Delta t \rightarrow 0} \Delta w / \Delta t = qE\cdot v_d$﻿ ($v_d=$﻿ drift velocity)

totar power ⇒

![[Screenshot_2023-11-08_at_8.07.30_PM.png]]

Joule’s law

> $P=\int_VE\cdot J dv$﻿

그래서 $P=I^2R =VI$﻿이다.

## Boundary conditions

일단 current density의 특징을 정리하면 다음과 같습니다.

![[Screenshot_2023-11-08_at_8.44.43_PM.png]]

이를 normal, tangential component 로 정리하면 다음과 같습니다.

![[Screenshot_2023-11-08_at_8.45.55_PM.png]]

![[Screenshot_2023-11-08_at_8.46.00_PM.png]]

## Duality of J and D

![[Screenshot_2023-11-08_at_8.48.21_PM.png]]