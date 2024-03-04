---
Created: 2023-09-14T22:09
Parent item:
  - "[[Fourier Analysis]]"
---
[[Linear Algebra Lecture 5 - (2) 벡터 공간(Vector Spaces), 부분 공간(Sub Spaces) -- Learn Again! 러너게인]]

벡터 공간(Vector space)

2-dimensional vector space

3-dimensional vector space

부분 공간(subspace)

Function space

## 벡터 공간(Vector space)

### 2-dimensional vector space

What is the Vector Space? It is a set of vectors, and the Linear combination is possible between each vector.

벡터 공간은 특정 vector들의 set으로, 벡터 간의 Linear Combination(선형 결합)이 가능한 벡터들의 집합입니다.

어떤 2-dimensional plane을 생각해봅시다. 또한 그 plane 위의 모든 vector를 포함하는 2-dimensional vector space $\mathbb{R}^2$﻿ 를 생각해봅시다.

![[Screenshot_2023-09-14_at_10.31.55_PM.png]]

  

> [!important]  
> 평면 상의 모든 벡터를 포함하는 벡터 공간이 평면인 걸까요 아님 모든 벡터를 모아봤더니 평면이 되는걸까요물론 같은 말 반복이긴 한데 뭐가 먼저인지 궁금함  

The most inportant thing is that Vector space of every dimension must contain 0 vector, Because any vectors in vector space can be made by Linear combination of other vectors in vector space. If there is no 0 vector, it can’t be performed.

### 3-dimensional vector space

Let’s expand our theory to 3 dimension and n-dimension.

3-dimensional vector space is vector space that contains vectors $<x, y, z>$﻿, and so $n$﻿-dimensional vector space contains vectors with $n$﻿ components, $<x,y,z,...,n>$﻿

> [!important]  
> 이렇게 addition, scalar multiplication 을 수행해도 한 vector space 안에서 모든 결과가 나오는 것을 closed under addition/multiplication (연산에 대해 닫혀있다) 라고 표현합니다.  

## 부분 공간(subspace)

하나의 벡터 공간에서 벡터 공간의 조건을 만족하는 작은 벡터 공간을 말합니다. 이 말인 즉슨, 해당 subspace 내부에서도 모든 벡터가 다른 벡터들의 Linear combination 들로 표현할 수 있어야 합니다.

예를 들어 1사분면을 생각해봅시다. 1사분면에서는 scalar multiplication 을 벡터에 적용했을 때, 1사분면의 벡터 공간을 벗어나는 벡터가 존재합니다. 따라서, 1사분면은 벡터공간이 될 수 없습니다.

![[Screenshot_2023-09-14_at_10.50.19_PM.png]]

여기서 잘 생각해보면, **벡터 공간은 반드시 zero vector를 포함해야 하므로,** subspace 또한 zero vector를 항상 포함해야 한다는 것을 알 수 있습니다. 따라서 원점을 지나는 직선, 평면, 그리고 무려 **영벡터 그 자체 또한 vector space가 될 수 있습니다.**

## Function space

이제 우리가 배운 vector space를 함수로 확장해봅시다.