---
Created: 2023-11-13T16:46
Parent item:
  - "[[Sampling]]"
---
## Sampling Theorem

sampling을 진행하기 위한 규칙입니다.

우선 CT를 DT로 sampling 하기 위해서는 다음의 두 가지 조건을 만족해야 합니다.

![[Screenshot_2023-11-13_at_4.50.04_PM.png]]

- freq. domain에서 limited band를 가질 것
- sampling freq는 최대한 높은 값을 가질 것

여기서 sampling freq가 가지는 의미를 더 자세히 알아봅시다.

## Impulse train sampling

어떤 CT를 sampling하기 위해서는 일정한 sampling period를 가진 train pulse를 convolution하면 됩니다.

![[Screenshot_2023-11-13_at_5.02.05_PM.png]]

이 때 sampling freqeuncy 를 적당히 높게 잡거나 낮게 잡는 경우는 다음과 같이 sampling이 됩니다.

![[Screenshot_2023-11-13_at_5.03.54_PM.png]]

freqeuncy가 높으면 정상적으로 convolution이 살아있지만, freqeuncy가 낮으면 신호의 일부가 손실되는 것을 알 수 있습니다.

따라서 위의 경우에는 원래 신호를 찾을 수 있지만, 아래의 경우에는 원래 신호를 찾을 수 없어 올바른 sampling이라고 할 수 없습니다.

![[Screenshot_2023-11-13_at_5.12.41_PM.png]]

이 때 ideal LPF를 사용해 원래 신호를 찾을 수 있습니다.

## Sampling Theorem (cont.)

![[Screenshot_2023-11-13_at_5.15.28_PM.png]]

이 때 위의 sampling freq의 조건은 band width의 두 배보다 클 것 입니다.

> [!important]  
> 아래의 조건은… 좀 더 생각해볼게요  

## Zero-order hold

하지만 저렇게 생으로 sampling된 함수 (impulse train의 형태)를 그대로 사용할 수는 없으므로, zero-order hold를 이용해봅시다.

![[Screenshot_2023-11-13_at_5.20.56_PM.png]]

특정 신호 함수 $h_0(t)$﻿ (모양은 위의 사진 참고) 와 convolution을 진행해 비연속적인 constant들로 이루어진 신호를 만들어냅니다.

하지만 이러한 함수의 모양은 현실적으로 만들기 굉장히 어렵기 때문에 나중에 approximation을 사용하는 편입니다.

## Reconstruction filter

근데 zero-order hold 를 진행한 후 reconstruction을 진행하는 경우를 생각해봅시다.

![[Screenshot_2023-11-13_at_5.37.23_PM.png]]

위와 같이 filter의 모양이 괴상하게 생긴 것을 알 수 있습니다.

해당 필터는 현실적으로 만들기 어렵기 때문에 interpolation 을 이용해 신호를 만듭니다.