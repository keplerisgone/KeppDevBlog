---
Created: 2023-09-12T13:58
Parent item:
  - "[[Week 2]]"
---
▶About Theory

–NAND

–Adder

–2’s complement

–Subtractor

▶About Verilog HDL

–About HDL

–Designing methodology

–Modules and ports

–Coding with Verilog

▶Debugging methods

▶HW in assignment folder debugging steps

▶Implement 4-bit Full Adder using NAND

▶Discussion

## ▶About Theory

### –NAND

![[Media/Untitled 48.png|Untitled 48.png]]

NAND 게이트의 진리표는 다음과 같다.

|a|b|r|
|---|---|---|
|0|0|1|
|0|1|1|
|1|0|1|
|1|1|0|

Not AND gate의 준말로, AND 게이트와 완전히 반대의 연산을 한다.

다른 논리 게이트들은 기초적인 논리 연산을 통해 NAND 게이트의 형태로 표현할 수 있는데, 각각의 식과 gate를 표현하면 다음과 같다.

![[Media/Untitled 1 36.png|Untitled 1 36.png]]

![[Media/Untitled 2 35.png|Untitled 2 35.png]]

![[Media/Untitled 3 34.png|Untitled 3 34.png]]

![[Media/Untitled 4 25.png|Untitled 4 25.png]]

### –Adder

Adder는 두 개의 binary digits를 받아 둘을 더하는 간단한 논리회로로, half adder와 full adder의 두 종류가 있다.

half adder는 단순히 A와 B를 받아 합의 결과인 Sum, 올림 결과인 Carry_out을 내보내는 adder로, 진리표와 회로는 다음과 같다.

|   |   |   |   |
|---|---|---|---|
|A|B|sum|carry_out|
|0|0|0|0|
|0|1|1|0|
|1|0|1|0|
|1|1|0|1|

![[Media/Untitled 5 21.png|Untitled 5 21.png]]

sum은 A와 B의 XOR 연산, carry_out은 A와 B의 AND 연산과 같은 것을 볼 수 있다.

full adder는 위의 half adder에 carry_in 인풋을 추가한 것으로, 이전 계산 결과의 올림 결과를 반영할 수 있다는 차이점이 있다. 따라서 한 자릿수 연산만 수행할 ㅜㅅ 있는 half adder와는 다르게 full adder를 여러 개 연결하여 여러 자리수의 연산을 수행할 ㅜㅅ 있다는 차이점이 있다.

full adder의 진리표와 회로도

|   |   |   |   |   |
|---|---|---|---|---|
|A|B|in|sum|out|
|0|0|0|0|0|
|0|0|1|1|0|
|0|1|0|1|0|
|0|1|1|0|1|
|1|0|0|1|0|
|1|0|1|0|1|
|1|1|0|0|1|
|1|1|1|1|1|

![[Media/Untitled 6 17.png|Untitled 6 17.png]]

sum 은 A와 B의 XOR 연산 후 Cin과의 XOR 연산,

full adder를 두 개 연달아 붙여놓은 2bit 연산과 4개 연달아 붙여놓은 4-bit 연산

![[Media/Untitled 7 15.png|Untitled 7 15.png]]

### –2’s complement

2’s complement 는 이진수에서 음수를 표시하기 위한 방법중 하나로, 연산 방법은 비트를 반전시킨 후 1을 더하는 것이다.

1을 더하지 않으면 1의 보수법이 된다

범위는 각각 이렇게 까지 표시할 수 있다

예시) -3을 3bit의 이진수로 표현해보자

$3 = 011$﻿ → 비트의 반전 → $100$﻿

$100 + 1 = 101 \ (-3)$﻿

$-2^{n-1}$﻿

예시 연산.

### –Subtractor

뺄셈 연산을 ‘음수를 더한다’는 개념으로 생각해보자. 즉, 3 - 5의 연산을 3 + (-5) 로 생각해보자. 위의 4-bit full adder에 B_n에 1과의 XOR 연산을 수행하면 B의 비트가 반전된다. 이때 최초 Cin에 1을 넣으면 B가 2의 보수법의 방식으로 음수로 전환된다.

![[Media/Untitled 8 12.png|Untitled 8 12.png]]

반대로 0과의 연산을 수행 후 cin에 0을 넣으면 원래대로 addition이 수행된다.

> [!important]  
> 이거 왜그런거임??  

## ▶About Verilog HDL

### –About HDL

what is HDL?

### –Designing methodology

top-down vs bottom-up

장점

위의 half adder를 간단하게 예시로 들어보자 - 회로 설계에서는 그래도 topdown 방식이 낫지 않을까?ㅔ

### –Modules and ports

module

structural modeling

Behavioral modeling

RTL modeling

ports

types - input, output, inout

port connection rules

### –Coding with Verilog

type - Nets, Register, (Integer, Numbers, real, array), function

## ▶Debugging methods

- syntax error and logical error

–With given example code! - ==_basic_demo - 2-bit adder였나_==

1. example sources 추가하기
2. syntax error - error message 확인, 고치기
3. logical error확인 - breakpoint 설정, 위의 source 확인, 값이 어딘가 달라진 것이 있나 확인
    1. 여기에는 회로 사진 들고와
4. 문제점 고치기
5. 다시 시뮬레이션 - 정상확인

## ▶HW in assignment folder debugging steps

역시나 위와 같이… 4-bit adder

1. assignmen sources 추가하기
2. syntax error - message 확인, 고치기
3. logical error 확인 - adder 사진 들고와, 회로 연결확인, 값 할당 확인, source 확인
4. 문제점 고치기
5. 다시 시뮬레이션

## ▶Implement 4-bit Full Adder using NAND

위 4-bit full adder 다시 회로도 가져와

그리고 NAND 게이트로 다른 게이트 표현하는 거 어디갔냐 그러고 다른 걸로 고쳐놔라

1. NAND 게이트 구현 (nand_gate source 만들기)
2. bit_0,1,2,3 adder 만들기 (full_adder 디자인 )
3. adder_4bit 구현
4. 시뮬레이션
5. 잘못되면 디버깅하는 과정까지 포함 (일부러 틀Con릴까?)

## ▶Discussion

질문 사항은 딱히 없는데 bottom-up 디자인 방법은 딱히 쓰는 데가 없는걸까?

subtractor에서 carry가 동작하는 방식 생각하기

  

![[Media/Untitled 9 3.png|Untitled 9 3.png]]

왜 |임??

  

NOR → XOR

1’b1 → 1’b0

carry_in 으로 바꾸기

- topdown vs bottomup

[https://ggodong.tistory.com/211](https://ggodong.tistory.com/211)

- HDL

[http://www.ktword.co.kr/test/view/view.php?m_temp1=4558](http://www.ktword.co.kr/test/view/view.php?m_temp1=4558)