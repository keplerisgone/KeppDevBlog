---
Created: 2023-08-22T15:51
---
### 2.1 Introduction

- Boolean algebra : logic design 중 하나로, 0과 1의 두 상태를 다룬다.
    - what is different from binary?
        - It represents not numeric value, but two different states.

### 2.2 Basic Operations

- NOT (Inverter)
    
    - $0’ = 1, \ \ 1’=0$﻿
    
    ![[Screenshot_2023-03-13_at_8.34.56_PM.png]]
    
- AND
    
    - $0\cdot 0 =0, \ 0\cdot 1 = 0, \ 1\cdot 0 =0, \ 1\cdot 1 = 1$﻿
    
    ![[Media/Untitled 14.png|Untitled 14.png]]
    
- OR
    
    - $0+0=0, \ \ 0+1=1, \ \ 1+0=1, \ \ 1+1=1$﻿
    
    ![[Media/Untitled 1 7.png|Untitled 1 7.png]]
    
- Apply Basic Operations to Switch
    
    ![[Media/Untitled 2 7.png|Untitled 2 7.png]]
    

### 2.3 Boolean Expressions and Truth Tables

- Logic Expression : 수식.
- Circuit of logic gates : 잘 회로로 표현하기
- Truth tables : n개의 variables가 있을 때, $2^n$﻿ 개의 rows가 존재한다
    - 신기하게 00001111, 00110011, 01010101 같이 쓰면 모든 경우의 수를 쓸 수 있다. (세로로)

### 2.4 Basic Theorems

아몰랑

![[Media/Untitled 3 6.png|Untitled 3 6.png]]

모르겠다 싶으면 서킷을 그리면 된다

### 2.5 Commutative, Associative, and Distributive Laws

- Commutative Laws, Associative Laws
    
    ![[Media/Untitled 4 4.png|Untitled 4 4.png]]
    
- Distributive Laws
    
    OR 연산도 분배법칙이 유효함에 유의합시다.
    
    ![[Media/Untitled 5 4.png|Untitled 5 4.png]]
    

### 2.6 Simplification Theorems

사실 교환법칙, 분배법칙, 결합법칙만 잘 적용하면 유도가 가능합니다.

![[Media/Untitled 6 4.png|Untitled 6 4.png]]

### 2.7 Multiplying Out and Factoring

- sum of product = $()+()+()$﻿ 의 모습을 말한다. → 구현이 쉽다, 줄여서 SOP라고 합니다.
- Multiplying : 아무튼 전개해서 sum of product 형태로 만드는 것을 말한다.
- product of sum = $()()()$﻿ 의 형태를 말한다. 줄여서 POS라고 합니다.

### 2.8 DeMorgan’s laws

- $(X+Y)’=X’Y’$﻿
- $(XY)’=X’+Y’$﻿
- Dual : AND → OR, OR → AND, 0 → 1, 1 → 0