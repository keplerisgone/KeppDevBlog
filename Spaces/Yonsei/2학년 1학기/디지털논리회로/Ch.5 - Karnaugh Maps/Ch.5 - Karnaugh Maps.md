---
Created: 2023-08-22T16:22
---
## Ch.5 Karnaugh Maps

5.5 까지 이해를 잘 하면 된단다~

### 5.1 Minimum Forms of Switching Functions

1. combine terms by using $XY’+XY=X$﻿  
    이를 이용해서 가능한 만큼 많은 terms를 지운다  
    
    +) $(X+Y)(X+Y’) = X$﻿
    
2. Consensus Theorems를 이용해서 필요없는 친구들을 지운다
    
    중요한 점은 _가장 많은 term을 지우는 경우를 찾는 것_입니다!
    
    ![[Media/Untitled 35.png|Untitled 35.png]]
    
    Example) minimum sum-of-products  
    위에서 왜 중복으로 씀????  
    
    ![[Media/Untitled 1 27.png|Untitled 1 27.png]]
    
    Example) minimum product-of-sums
    

### 5.2 Two-and Three-Variable Karnaugh Maps

- 카르노맵 : 간단한 형태의 truth table????
    
    ![[Media/Untitled 2 26.png|Untitled 2 26.png]]
    
    2-variable Karnaugh map
    
    - 같은 줄이 같은 값일 경우 묶어줄 수 있다
    - 대각선으로는 묶지 못해요
- Three-variable 은 어떻게 표현하나요 → 00 01 10 11과 같이 표기를 합니다
    
    ![[Media/Untitled 3 25.png|Untitled 3 25.png]]
    
    Trurh table and Karnaugh map - 근데 세번째 칸은 왜 불편하게 11이냐  
    01 → 10 은 두 개의 값이 변해버려서 묶기에 불편하다  
    참고로 두 개가 다르다 이런  
    
- 카르노맵은 왜 쓸까요?
    - 좀 더 쉽게 minimum solution을 구하기 위해서 사용합니다  
        솔직히 말해서 Truth table 보다는 낫잖아요  
        
    - 그러기 위해서 아래의 방법을 사용합니다
- Karnaugh map for product terms
    - 대충 일렬로 나와있는 결과들을 묶어버리면 된다
        
        ![[Media/Untitled 4 19.png|Untitled 4 19.png]]
        
    - 더 정확히 말하면 그냥 일렬로 묶는다기 보다 공통되는 term을 찾아서 묶어버리는 것에 가깝다
    - 거꾸로도 할 줄 알아야 한다
    - 강의안에서 다양한 예제를 살펴보세요
    - 겹치는 건 consensus term같다
    - 닥터 마리오 하는 거 같다

### 5.3 Four-Variable Karnaugh Maps

- 이제는 variable이 4개에요
- 00 01 11 10
    
    ![[Media/Untitled 5 15.png|Untitled 5 15.png]]
    
    Location of Minterms on Four-Variable Karnaugh Map
    
    ![[Media/Untitled 6 14.png|Untitled 6 14.png]]
    
    acd를 세 개로 묶어버리면 안 되는 걸까  
    이게 진짜 되네  
    
    - 팁) 나는 진짜 못 묶어먹겠고 algebra form이 더 편하다하면 그냥 대충 묶어놓고 equation에서 묶어주면 된다
- Don’t care term이 포함된 경우: don’t care term을 포함해서 가장 간단하게 묶으면 된다.
    
    ![[Media/Untitled 7 12.png|Untitled 7 12.png]]
    
    don’t care term 포함해서 묶어버리면 된다
    
- Maxterm (product-of-sums form) 이 더 편리할 거 같은 경우
    
    ![[Media/Untitled 8 10.png|Untitled 8 10.png]]
    
    그냥 도출해내는 건 어려우니까 invert 하라구~
    

### 5.4 Dtermination of Minimum Expressions Using Essential Prime Implicants

- Implicants of F : single ‘1’ or can be combined together on a Map
    - 그냥 존재할 수 있는 모든 묶인 것들의 집합입니다.
- Prime Implicants : product term that can not be combined with other terms
    
    - 간단히 말해서, 각 1에 대해서 가장 크게 묶인 것들의 집합을 의미합니다.
    - essential : 크다
        - Implicants of F 중에서 반드시 포함되어야 하는 것들을 말합니다. _얘가 없으면 모든 1을 넣을 수 없다_에 가깝습니다.
    
    [[🔗 LINK]](https://blastic.tistory.com/195) — [Karnaugh Map] Essential Prime Implicants
    
    - 이거 설명 맛집이다

### 5.5 Five-variable Karnauph Maps

- 차원을 하나 더 늘려서 생각합시다. 4 변수 카르노맵이 두 개가 겹쳐있다고 생각하면 편합니다.
- 여기에서도 마찬가지로 인접한 건 묶을 수 있습니다. 다만, 직육면체처럼 생각해서 묶어주세요.
- 그 외 다른 특징들, 즉 Essential Prime implicants들을 구해 Minimum SOP 를 구하는 방식 같은 건 다른 카르노맵과 동일합니다.

### 5.6 Other Uses of Karnauph Maps

그 외에도 _두 식이 같은 함수를 나타내는가?_를 증명할 때도 쓰입니다.

두 식에 대한 카르노맵을 작성한 뒤, 같은 카르노맵을 나타낸다면 같은 함수를 나타내는 거겠죠!

### 5.7 Other Forms of Karnauph Maps

Veitch Diagram 이라는 다른 형태의 카르노맵이 존재합니다. 0과 1로 표현하는 카르노맵과 달리 해당 인자의 참 여부를 표시하는 방식으로 사용하는 다이어그램입니다만, 설명이 복잡해서 그렇지 사실 카르노맵과 완벽하게 일치합니다.

![[Media/Screenshot_2023-08-22_at_4.47.34_PM 2.png|Screenshot_2023-08-22_at_4.47.34_PM 2.png]]

그래도 카르노맵과 달리 이점이 있다면, 5변수 카르노맵을 다이어그램 두 개를 나란히 대칭으로 붙임으로써 간단히 나타낼 수 있다는 점입니다. 묶는게 복잡해지긴 하지만, 그래도 5변수 카르노맵에서 더럽게 묶는 것보다는 백배천배 낫습니다.

![[Media/Screenshot_2023-08-22_at_4.48.54_PM 2.png|Screenshot_2023-08-22_at_4.48.54_PM 2.png]]