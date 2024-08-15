---
Created: 2023-08-22T15:54
---
## Ch.3 Boolean Algebra (continued)

### 3.1 Multiplying Out and Factoring Expressions

- sum-of-product form으로 나타내기 위함.
- Theorem for factoring
    
    아래의 (X + Y)(X’ + Z) 에서, 결과가 X가 0일 때는 Y를 따르고, X가 1일 때는 Z를 따라간다는 점을 이용합니다. 이를 SOP 형식으로 나타내면 X’Y + XZ가 되니깐요!
    

![[Media/Untitled 36.png|Untitled 36.png]]

### 3.2 Exclusive-OR and Equivalence Operations

- Exclusive-OR : $A\oplus B$﻿, 같은 것은 0, 다른 것은 1로 출력. 줄여서 XOR이라고 합니다.
    
    ![[Media/Untitled 1 28.png|Untitled 1 28.png]]
    
    - 매우 중요 XOR의 역 - truth table로 표현, 0이 나오는 결과를 더한 뒤 식을 단순화하면 얻을 수 있습니다.
        
        ![[Media/Untitled 2 27.png|Untitled 2 27.png]]
        
- Equivalence Operation = Exclusive-NOR : $A\equiv B$﻿, 같으면 1, 다르면 0 출력. 줄여서 XNOR라고 합니다.
    
    ![[Media/Untitled 3 26.png|Untitled 3 26.png]]
    
    - $X \equiv Y = (X \oplus Y)’ = (XY’+X’Y)’ = XY+X’Y’$﻿

### 3.3 The Consensus Theorem

- $X’Y + XZ + YZ = X’Y + XZ$﻿ : 대충 X 랑 X’랑 붙어있는 거끼리 곱해진 것은 지워도 된다는 뜻
    - 증명은 $YZ$﻿에 $(X+X’)$﻿를 곱해서 합니다 (1 이므로)
- Dual form of Consensus theorem : $(X+Y)(X’+Z)(Y+Z) = (X+Y)(X’+Z)$﻿

### 3.4 Algebric Simplification of Switching Expressions

사진으로 대체

![[Media/Untitled 4 20.png|Untitled 4 20.png]]

![[Media/Untitled 5 16.png|Untitled 5 16.png]]

### 3.5 Proving Validity of an Equation

해당 방정식이 성립함을 증명하는 방법은 다음과 같습니다.

1. Truth Table로 모든 0과 1에 대해서 성립함을 보인다
2. 양 쪽을 각종 theorem으로 정리해 동일함을 보인다
3. 양 쪽을 줄여서 비교하는 방법 (simplifying)
4. 양 쪽에 같은 operation을 진행