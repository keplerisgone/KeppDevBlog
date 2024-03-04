---
Created: 2023-08-25T02:11
---
## Ch. 12 Registers and Counters

### 12.1 Registers and Register Transfers

![[Media/Untitled 19.png|Untitled 19.png]]

- FF 여러 개를 이어붙여서 데이터를 저장하기 위해 만든 것을 Register라고 합니다.
- ClrN, load, Clk, input, output으로 구성되어 있습니다.
- load가 1일 경우 저장되어 있는 데이터를 로드합니다.
- 가장 중요한 기능 중 하나는 레지스터 간의 정보 교환입니다.
- 위와 같이 다양한 형태로 표현할 수 있으며, 데이터를 선택하기 위해 여러개의 register를 연결해 사용하기도 합니다.

![[Media/Untitled 1 12.png|Untitled 1 12.png]]

- Parallel Adder with Accumulator
- 여기서는 Ad가 load 역할을 합니다.

### 12.2 Shift Registers

![[Media/Untitled 2 12.png|Untitled 2 12.png]]

- Shift input의 값에 따라 output의 shift가 이루어지는 register입니다.
- D FF와 S-R FF등 다양한 FF로 나타낼 수 있지만, D가 제일 편하긴 합니다
- Sh, L를 input으로 받을 수도 있는데, Sh=1 일 경우 shift가 일어나고, L=1 일 경우 load가 일어나 D값으로 바뀝니다.
    
    ![[Screenshot_2023-08-25_at_2.20.07_AM.png]]
    
- 첫번째 register에 마지막 output의 complement가 연결된 카운터를 Johnson counter라고 합니다.

### 12.3 Design of Binary Counters

![[Media/Untitled 3 11.png|Untitled 3 11.png]]

- 그냥… truth table 쓰고… 이것저것… 다해서…
    
    카운터 결과의 배열을 한 번 봅시다. 이를 보고, truth table을 적습니다. 보통 _현재 상태 → 다음 상태 | 다음 상태가 되기 위해서 필요한 플립플랍 인풋값_ 으로 나타냅니다.
    
    이 때 _필요한 플립플랍 인풋_을 카르노맵 등을 이용해서 가장 간단한 형태로 나타냅시다.
    
- Up-down counter는 유의해주세요
- 다양한 예시는 강의안을 참고해주세요

### 11.4 Counters for Other Sequences

다양한 배열에 대한 카운터를 디자인하려면, 다음 방식을 따릅시다. 물론 T FF 기준입니다! TFF 가 가장 만들기 쉽습니다. T=1 이기만 하면 결과값이 변하거든요.

1. tansition table 을 작성합니다. 입력 결과에 따른 다음 상태를 나타낸 truth table입니다.
2. next-state map을 작성합니다. 위의 transition table에 따라 그린 카르노맵입니다.
3. 이 때, 항상 $Q^+ \ne Q$﻿ 일 경우, $T_Q$﻿ 는 항상 1입니다.
4. 가장 간단한 표현식으로 나타낸 뒤, 회로로 나타냅니다.

이후 교재에는 다양한 플립플랍(S-R, D, J-K)를 이용해서 카운터를 만드는 방법이 나와있습니다.