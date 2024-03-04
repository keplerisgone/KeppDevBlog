---
Created: 2023-08-22T16:04
---
## Ch. 4 Applications of Boolean Algebra / Minterm and Maxterm Expansions

### 4.1 Conversion of English Sentences to Boolean Equations

- 문장을 보고

1. output 이 뭔지 찾기
2. 다양한 조건들을 찾기
3. and, or 찾아서 연결하기
4. simplification

를 하면 문제상황을 Boolean으로 표현할 수 있습니다! 코딩할 때도 도움이 많이 되겠죠.

### 4.2 Combinational Logic Design Using a Truth Table

- Truth Table을 가지고 함수를 구현해낸다
    1. 일단 결과가 1이 나오는 표현식을 모두 OR 연산합니다.
    2. 여러가지 연산 법칙을 이용해 식을 간단히 합니다.

![[Media/Untitled 17.png|Untitled 17.png]]

- 수식으로 구현한 다음 간단히 한다
- $f’$﻿로 표현할 수도 있는데, 마지막에 꼭 드모르간을 해줘야 한다

### 4.3 Minterm and Maxterm Expansions

- Minterm : input을 product로 표현해서 1이 되는 친구를 표현합니다
- Maxterm : input을 sum으로 표현해서 0이 되는 친구를 표현합니다
    - 정확히는 0이 나오는 친구에 드모르간을 적용한 것과 같습니다.
- 기호는 아래를 참고

![[Media/Untitled 1 10.png|Untitled 1 10.png]]

![[Media/Untitled 2 10.png|Untitled 2 10.png]]

### 4.4 General Minterm and Maxterm Expansions

- $a_i$﻿ 에 0, 1을 넣어 $m_i, M_j$﻿이 있나없나 표현한다
- 아 몰라 귀찮아 표를 봐라

![[Media/Untitled 3 9.png|Untitled 3 9.png]]

### 4.5 Incompletely Specified Functions

- 만약 function이 두 개일 경우, 중간 output에서 도출하지 못하는 결과가 있을 수 있음
- 이런 것을 Don’t care term, values 라고 하는데, 여기다 0과 1의 모든 조합을 넣어서 가장 단순화가 잘 된것을 고른다
- 기호로는 이렇게 표현

![[Media/Untitled 4 7.png|Untitled 4 7.png]]

### 4.6 Examples of Truth Table Construction

- Binary Adder에 사용합니다
- 의외로 sum, carry를 다 생각해야 하는 작업이라구

### 4.7 Design of Binary Adders and Subtracters

일반적으로 바이너리를 더할 때는 입력값으로 받는 두 숫자(X, Y)와 직전 계산에서의 올림 여부(C_in) 를 인풋으로 받고, 계산 결과(Sum)와 계산에서의 올림 여부($C_{out}$﻿)을 결과로 내보냅니다.

그리고 받은 입력값에 대한 결과값을 truth table로 나타내면 다음과 같습니다.

![[Screenshot_2023-08-22_at_4.17.28_PM.png]]

이를 간단히 하면…

$Sum = X \oplus Y \oplus C_{in}$﻿

$C_{out} = YC_{in}+XC_{in}+XY$﻿

입니다.

![[Screenshot_2023-08-22_at_4.19.41_PM.png]]

따라서 위의 Full Adder 하나하나는 위 연산을 수행하는 디지털 회로로 구성되어 있겠죠?

이 4-but Parallel Adder 는 $A_1A_2A_3A_4$﻿와 $B_1B_2B_3B_4$﻿를 인풋으로 받아 더한 값을 $S_1S_2S_3S_4$﻿로 출력하는 회로입니다.

Subtracter로 같은 방식으로 디자인하면 됩니다.