---
Created: 2023-08-22T16:50
---
## Ch.6 QUINNE-McCLUSKEY Method

### 6.1 Determination of Prime Implicants

- Prime Implicants : a minimum term of minterms represented by using the law $XY+XY’=X$﻿.
- follow next :
    
    ![[Media/Untitled 27.png|Untitled 27.png]]
    
    1. minterms를! 1의 개수를! 기준으로 group을 나눕니다.
    
    ![[Media/Untitled 1 19.png|Untitled 1 19.png]]
    
    2. 1의 개수가 1씩 차이나는 것들끼리 합친다  
    group 1 - group 2 / group 2 - group 3….  
    끝까지 가면 체크가 안 된 것들을 합친다  
    → 이것들은 prime implicants에요  
    
    ![[Media/Untitled 2 18.png|Untitled 2 18.png]]
    
    3. 위에서 합친 것들을 consensus theorem를! 이용해서 간단하게 만들어주면 이게 minimum form이다
    

### 6.2 The Prime Implicant Chart

위에서 발견한 PI 들을 표로 정리해봅시다. 가로는 존재하는 minterm을 나열한 것이고, 세로 축은 PI들을 나열한 것입니다. 해당 PI가 해당 minterm을 포함하는지 여부를 교차하는 곳에 표시합니다.

![[Media/Untitled 3 17.png|Untitled 3 17.png]]

하나만 있는 x → essential PI  
find remaining cover → minimum sum of products  

![[Media/Untitled 4 12.png|Untitled 4 12.png]]

EPI 가 없을 수도 → 그냥 PI들로 minimum solution을 찾는다  
Tip) Again starting with the other prime implicant that covers column 0.  

### 6.3 Petrick’s Method

위에서 Essential PI가 없을 때, minimum SOP를 구하는 방법입니다.

만약 하나의 minterm에 대해서 여러개의 PI가 존재할 경우, 그 중 하나만 1이어도 OR 연산시에 1이 됨을 이용합니다.

또한 함수는 모든 minterm에 대해 1이 나와야합니다. 여기서 논리함수 $P$﻿를 생각해봅시다. 해당 논리함수는 모든 minterm이 포함됐을 경우에만 1을 반환합니다. 따라서 중복된 PI 들을 OR 연산으로 묶어주고, 이들을 다시 AND 연산으로 묶어주면, 이 함수는 무조건 1이 될 수 밖에 없습니다.

그리고 이를 정리해 나온 식들 중 가장 길이가 짧은 식을 이용합니다.

![[Media/Untitled 5 10.png|Untitled 5 10.png]]

(0에 대한 minterm)(1에 대한 minterm)… = 1

![[Media/Untitled 6 9.png|Untitled 6 9.png]]

using distributive law  
→ 선택하는 기준이 뭐지 → 아 일단 제일 적은 거를 고른 담에 minimum solution을 구하는 거구나  

### 6.4 Simplification of Incompletely Specified Functions

1. Treat Don’t care terms as required minterms

![[Media/Untitled 7 8.png|Untitled 7 8.png]]

1. Forming PI chart, omit don’t care terms.

![[Media/Untitled 8 7.png|Untitled 8 7.png]]

그리고 결과를 통해 빠진 don’t care term 들에 대한 결과를 예측할 수 있습니다.

### 6.5 Simplification Using Map-Entered Variables

카르노맵을 이용해 가장 간단한 형태를 구할 수도 있습니다.

만약 함수의 형태가 (4변수의 minterm) + (2개 이상의 추가 변수) 일 경우에 사용가능합니다.

만약 함수의 형태가 이럴 경우…

![[Media/Screenshot_2023-08-22_at_11.33.36_PM 2.png|Screenshot_2023-08-22_at_11.33.36_PM 2.png]]

카르노맵은 이렇게 작성합니다.

![[Media/Screenshot_2023-08-22_at_11.33.56_PM 2.png|Screenshot_2023-08-22_at_11.33.56_PM 2.png]]

맵을 작성한 이후에, 추가적인 변수들에 0과 1을 대입해 각 상황에서의 가장 간단한 형태를 구합니다. 근데 왜 $E=1, F=1$﻿은 대입을 안 할까요…?