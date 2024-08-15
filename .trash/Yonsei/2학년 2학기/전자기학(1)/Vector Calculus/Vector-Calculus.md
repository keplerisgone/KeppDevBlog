---
Created: 2023-09-20T18:09
Parent item:
  - "[[Vector Analysis]]"
---
Scalar field

Vector field

Vector Integral

Case 1: @import url('https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.css')$\int \vec{F}dv$﻿

Case 2: @import url('https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.css')$\int_C Vd\vec{l}$﻿

Case 3: @import url('https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.css')$\int_C \vec{F}d\vec{L}$﻿

Case 4: @import url('https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.css')$\int_S \vec{A}\cdot d\vec{S}$﻿

Gradient

Divergence of @import url('https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.css')$\vec{h}$﻿

Divergence Theorem

Curl of @import url('https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.css')$\vec{h}$﻿

Stokes’s Theorem

Identity

Helmholtz Theorem

## Scalar field

![[Untitled.jpeg]]

3차원, 혹은 그 이상의 차원에서 각 point마다 single scalar number가 존재.

## Vector field

![[Untitled 1.jpeg]]

위의 scalar field를 거대한 산으로 생각했을 때, 해당 값이 어디로 굴러내려갈지(해당 값의 변화량)를 나타냅니다.

heat flow $\vec{h}$﻿ 를 예시로 들면,

> $\vec{h}=h_x\vec{a_x}+h_y\vec{a_y}+h_z\vec{a_z}$﻿

> $(h_x, h_y, h_z)=({\partial \over \partial x}T, {\partial \over \partial y}T, {\partial \over \partial z } T)$﻿

이 성립합니다.

> [!important]  
> 그럼 편미분이 아닌 일반 미분과는 어떤 관계를 가질까요?  

또한 heat flow는 flux로, 단위 시간에 단위 면적당 해당 지점을 통과하는 에너지의 양을 말하는 것입니다. $\vec{h}$﻿ 는 x, y, z, t에 따른 함수니깐요.

## Vector Integral

Vector Integral을 이용하면 다음과 같은 것을 알 수 있습니다.

- 부피를 통과하는 벡터의 총량
- 어떤 면적을 통과하는 벡터의 총량
- 어떤 경로를 통과하는 벡터의 총량…

### Case 1: $\int \vec{F}dv$﻿

$dv$﻿는 volume differential이었다.

> $\int F_x dv\vec{a_x}+\int F_y dv\vec{a_y} +\int F_zdv \vec{a_z}$﻿ 와 같다고 한다

> [!important]  
> 이게 뭔 개소리노  

### Case 2: $\int_C Vd\vec{l}$﻿

이 경우는 스칼라장에서의 vector integral로, 아래와 같습니다.

> $\int _C V d\vec{l}=\int V(x,y,z)dx\vec{a_x}+\int V(x,y,z)dy \vec{a_y}+\int V(x,y,z)dz\vec{a_z}$﻿

그냥 적분해서 구합니다.

> [!important]  
> 근데 physical meaning을 모릅니다.  

### Case 3: $\int_C \vec{F}d\vec{L}$﻿

해당 경로에서의 벡터 크기 합에 가깝습니다. 일종의 dot production으로 계산되기 때문에, 결과는 항상 scalar입니다.

projection의 합.

> $d\vec{L} =dx\vec{a_x}+dy\vec{a_y}$﻿ 군요! 내적을 하니까 그렇게 나오지

폐경로에서 적분을 나타낼 때는 $\oint$﻿를 사용합니다. 원 경로에서의 적분이 대표적입니다.

원 경로에서는 Cartesian이 아닌 Circular coordinate를 쓰겠죠?

> $\oint_C \vec{A}\cdot d\vec{L} = \oint \vec{\omega}\cdot d\vec{l} = w\cdot2\pi r$﻿

자세한 계산법은 다음 두 가지를 사용할 수 있습니다.

> $\int \vec{F}(\vec{r}(t))\cdot \vec{r}'(t)dt$﻿ - contour가 $t$﻿에 대한 함수로 주어질 때

> $\int Pdx+Qdy+Rdz$﻿ - countour가 일종의 함수로 주어질 때

### Case 4: $\int_S \vec{A}\cdot d\vec{S}$﻿

이는 해당 면적을 통과하는 벡터들의 합입니다.

$d\vec{S}$﻿는 magnitude인 $ds$﻿와 해당 면에 수직인 방향의 벡터인 $\vec{a_n}$﻿으로 분리해 나타낼 수 있습니다.

역시 closed surface라면 $\oint$﻿를 사용합니다.

이는 해당 closed surface에서의 에너지 방출량을 나타냅니다.

sub-divide가 가능합니다.

## Gradient

진짜 차라리 이 개념이 이해하기 더 쉬운거 같음

Cartesian 에서의 경우 vector gradient는 다음과 같이 나타납니다. 임의의 스칼라 함수 $f$﻿에 적용해봅시다.

> $\nabla f={\partial f \over \partial x }\vec{a_x}...$﻿

이를 연산자 del 만 떼어서 생각해보면 다음과 같습니다.

> $\nabla=\vec{a_x} {\partial \over \partial x}+\vec{a_y} {\partial \over \partial y}+\vec{a_z} {\partial \over \partial z}$﻿

각 방향으로 편미분한 것을 더하면 최종 변화값이 벡터로 나오게 됩니다.

다른 coordinate에서 계산할 때는 scale factor를 적용해야 합니다.

## Divergence of $\vec{h}$﻿

벡터에 gradient 연산과 dot product를 수행한 값을 Divergence라고 합니다. 왜 하필 이름이 분산이냐면, _작은 공간에서 벡터가 얼마나 퍼져나오는지 확인하는 값_이기 때문입니다.

![[Media/Untitled 37.png|Untitled 37.png]]

원래 정리는 이렇지만, 연산은 Del 연산자를 이용해서 수행합니다.

Del 연산자와 벡터를 dot product해봅시다.

![[Screenshot_2023-09-24_at_10.18.31_PM.png]]

> $\nabla\cdot \vec{h}=$﻿ x의 성분을 x 에 대해서 편미분 값 + y의 성분을 y 에 대해서 … +

결국 값은 스칼라가 나오게 됩니다.

해당 지점에서 순 벡터의 합이 어떻게 되는지 나타내는 값이라고 할 수 있습니다.

### Divergence Theorem

어떤 vector field의 divergence의 부피에 대한 적분은 그냥 vector에 대한 경계선의 적분과 같다.

![[Media/Untitled 1 29.png|Untitled 1 29.png]]

## Curl of $\vec{h}$﻿

이번에는 벡터에 del 연산자를 cross product 해봅시다.

> $\nabla \times \vec{h} = \begin{vmatrix} \vec{a_x} \vec{a_y} \vec{a_z} \\ {\partial \over \partial x} {\partial \over \partial y} {\partial \over \partial z} \\ h_x h_y h_z \end{vmatrix} $﻿

![[Media/Untitled 2 28.png|Untitled 2 28.png]]

의미는 어떤 작은 loop를 평가하는 값으로, 해당 국소 지점에서의 회전력의 여부를 평가합니다. (net circulation)

더 쉽게 표현하자면, 작은 물레방아를 해당 지점에 놓았을 때 얼만큼 돌아가는가? 를 의미합니다. 우와.

증명은 뭐…

### Stokes’s Theorem

Divergence theorem와 궤만 같습니다.

curl을 면적분 한 것과 일반 벡터필드를 선적분 한 값이 같대요.

![[Media/Untitled 3 27.png|Untitled 3 27.png]]

따라서 닫힌 폐곡면의 curl integral 값은 0이 되고, 이는 가우스 정리의 기본이 됩니다.

## Identity

- curl of gradient of any scalar is zero
    
    ![[Screenshot_2023-09-29_at_7.43.28_PM.png]]
    
- divergence of curl of any vector is zero
    
    ![[Screenshot_2023-09-29_at_7.43.38_PM.png]]
    

## Helmholtz Theorem

![[Screenshot_2023-09-29_at_7.46.33_PM.png]]

모든 vector field는 irrotational한 성분과 solenoidal한 성분으로 나눌 수 있다.

즉, divergence free한 성분과 curl free한 성분으로 나눌 수 있다.

즉, vector field의 ner circulation + divergence of particular point 의 합으로 나타낼 수 있다!