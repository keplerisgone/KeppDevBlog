---
Created: 2023-09-13T16:47
Parent item:
  - "[[Vector Analysis]]"
Sub-item:
  - "[[Metric coefficient and transformation]]"
---
Vector notation

Dot product

Cross Product

(Orthogonal) Coordinate Systems

Cartesian Coordinate system

Cylindrical Coordinate system

Transformation

Spherical Coordinate system

Transition

Scalar field & Vector field

## Vector notation

![[Screenshot_2023-09-13_at_4.54.21_PM.png]]

Vector의 notation은 다음과 같습니다.

> $\vec{A}=A\vec{a_k}$﻿, $\vec{a_k}=\vec{a_x}+\vec{a_y}+\vec{a_z}$﻿

## Dot product

![[Screenshot_2023-09-13_at_5.01.04_PM.png]]

Dot product는 벡터의 스칼라적인 연산으로, 결과가 벡터가 아닌 스칼라로 나옵니다. 내적의 기하학적인 의미는 projection입니다.

![[Screenshot_2023-09-13_at_5.04.44_PM.png]]

projection은 공학에서 중요한 의미를 지니는데…

> [!important]  
> 뭔 중요한 의미라는 거에요![[Screenshot_2023-09-13_at_5.11.52_PM.png]]대표적으로는 푸리에 변환입니다. 푸리에 변환은 해당 함수에 해당 성분(삼각함수들이겠죠?) 이 얼마나 포함되어있는지를 나타냅니다.![[Screenshot_2023-09-13_at_5.14.28_PM.png]]다음은 signal에서의 error detection입니다. error detection은 projection을 이용해 근사값을 취합니다.  

## Cross Product

외적은 두 벡터에 수직인 벡터를 구하는 연산입니다. 기하학적으로는 두 벡터를 두 변으로 하는 평행사변형의 넓이만큼의 크기를 지니는 수직인 벡터(오른손 방향)을 뜻합니다.

![[Screenshot_2023-09-13_at_5.17.11_PM.png]]

> [!important]  
> 근데 이거 왜 써요?  

다음과 같은 연산 법칙을 지닙니다.

![[Screenshot_2023-09-13_at_5.17.43_PM.png]]

또한 세 벡터의 Cross product - Dot product는 세 벡터를 각각 모서리로 하는 평행사변기둥? 의 부피를 뜻합니다. 증명은……. 니가 하세요!

![[Screenshot_2023-09-13_at_5.19.17_PM.png]]

BACK-CAP 공식도 알아둬서 나쁠건 없습니다!

## (Orthogonal) Coordinate Systems

![[Screenshot_2023-09-13_at_5.27.20_PM.png]]

Coordinate system에는 세 가지의 종류가 있는데, Cartesian, Cylindrical, Spherical 입니다.

세 가지 모두 EM을 표시하는데 쓰이며, 이 셋 사이의 변환은 정보 자체를 변환하는 것이 아닌 표시 방식만 변환하는 것입니다.

각자의 표현 방식마다 장점이 있고, 잘 표현할 수 있는 EM의 종류 또한 다릅니다.

> [!important]  
> 그렇다면 orthogonal의 뜻은 무엇일까요?이는 세 가지 표현 방식이 모두 perpendicular 한 세 평면위에 표시되는 방식이기 때문입니다.![[Screenshot_2023-09-13_at_5.32.03_PM.png]]위는 cartesian의 예시이지만, 다른 좌표계들도 xyz 평면을 사용합니다.물론 다른 Coordinate들도 많습니다.  

## Cartesian Coordinate system

![[Screenshot_2023-09-13_at_5.34.12_PM.png]]

가장 전통적인, xyz 좌표로 point를 표시하는 좌표계입니다.

각종 product는 다음과 같은 방법으로 계산합니다.

> [!important]  
> determinant는 정확히 어떤 것을 표현하는 값일까요?  

![[Screenshot_2023-09-13_at_5.36.26_PM.png]]

길이, 너비, 부피에 대한 변화는 다음과 같이 계산합니다. 증명은 또 다음과 같습니다.

> [!important]  
> 길이의 변화는 알겠습니다만, 너비와 부피에 대한 변화는 어떤 변화를 말하는 것일까요? 아니다 이게 @import url('https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.css')SxS_xSx​﻿ 가 뭔지를 몰라서 그런거였나요  

## Cylindrical Coordinate system

![[Screenshot_2023-09-13_at_5.37.54_PM.png]]

x,y 좌표는 벡터의 크기와 xy 평면에 대한 각도($\phi$﻿)로 표현하고, 나머지를 z평면에 대한 벡터 크기로 서술하는 좌표계입니다. Cartesian coordinate와 달리 point의 위치에 따라 벡터의 방향이 달라집니다. xyz 좌표계는 각 unit vector의 방향이 정해져 있습니다.

![[Screenshot_2023-09-13_at_5.40.22_PM.png]]

좌표, 너비, 부피에 대한 변화는 다음과 같이 서술합니다.

## Transformation

![[Screenshot_2023-09-13_at_8.08.18_PM.png]]

내적이 projection임을 이용해 x, y, z 좌표를 나타냅니다.

## Spherical Coordinate system

![[Screenshot_2023-09-13_at_8.11.40_PM.png]]

x, y, z 좌표를 모두 각도로 나타내는 좌표계입니다. 역시나 위의 Cylinderical coordinate 처럼 각 위치마다 unit vector가 표시하는 방향이 달라집니다. 모두 _구를 생각했을 때 접선의 방향_입니다.

![[Screenshot_2023-09-13_at_8.11.58_PM.png]]

spherical coordinate 에서 길이, 넓이, 부피의 변화를 표현하면 다음과 같습니다. 증명은 또 다음과 같긴합니다.

## Transition

![[Screenshot_2023-09-13_at_8.16.52_PM.png]]

사실 잘 기하학적으로 생각해서 변환하면 되긴합니다.

## Scalar field & Vector field

![[Screenshot_2023-09-13_at_8.19.35_PM.png]]

![[Screenshot_2023-09-13_at_8.19.42_PM.png]]

Scalar field는 해당 지점에서의 정도를 수로 나타낸 것, Vector field는 그 지수가 어떻게 변화하는 지 나타내는 필드입니다.

결국 Vector field는 Scalar field의 _변화_를 나타내므로, Scalar field의 각 편미분 값은 Vector field의 각 축의 벡터값일지도 모릅니다.

> [!important]  
> 일반적인 미분들은 어떤 관련이 있을까요?