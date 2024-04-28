---
Created: 2023-08-22T15:39
---
## Ch.1 Introduction Number Systems and Conversion

- 무엇을 배우나요?
    - analog 와 Digital 의 차이점
    - Combinational 과 Sequential Circuits 의 차이점
    - Binary number & conversion
    - Binary 연산
    - Negative binary number 를 위한 1’s & 2’s Complement
    - BCD code, 6-3-1-1 code, excess-3 code (Conversion 을 위한 것들)

### 1.1 Digital Systems and Switching Circuits

- Digital system : Digital data를 이용하는 시스템입니다. 계산, 제어, 처리, 측정, 통신에 편리해 많은 기계가 사용하고 있습니다.
    - 현재는 반도체, 휴대폰 등에서 많이 사용중입니다.
- Analog (Continuous)
    - 연속적이기 때문에, 더 많은 데이터를 가지고 있습니다.
        - 따라서 Digital 보다 처리, 제어가 어렵습니다.
    - 보통 자연의 현상에서 아날로그가 많이 나타납니다. (압력, 온도, 속도 등)
- Digital (Discrete)
    - Discrete 하기 때문에 더 적은 데이터를 가지고 있습니다.
        - 그래서 다루기가 편리합니다.
    - 보통 아날로그 데이터를 받아 디지털로 변환하여 사용합니다.
        - 푸리에 변환을 통해 더 자세한 디지털 데이터로 변환이 가능한데, 이러한 특징에 따라 아날로그 데이터를 명확히 구현할 수 있다는 것을 알 수 있습니다.
        - 디지털로 변환된 데이터를 다시 아날로그로 사용합니다.
- Binary Digit
    - Binary는 0과 1로만 수를 다루는 방식입니다. 따라서 사칙연산만으로 미적분을 구현하는 등의 편리한 일이 가능합니다.
- Switching Circuit
    - Discrete 한 데이터가 input, Discrete 한 데이터가 output으로 나오는 서킷을 말합니다.
    - Combinational Circuit
        - output 이 오로지 input 에만 의존합니다. 과거의 input 에 영향을 받지 않습니다.
        - 이쪽이 더 간단합니다.
    - Sequential Circuit
        - output 이 과거의 input에 영향을 받습니다.
        - 따라서 memory 가 반드시 필요합니다.

---

### 1.2 Number Systems and Conversion

![[Media/Untitled 30.png|Untitled 30.png]]

- Radix (Base) : N진수라고 할 때 N을 말합니다. R로 줄여쓰고, 밑으로 씁니다.

![[Media/Untitled 1 22.png|Untitled 1 22.png]]

![[Media/Untitled 2 21.png|Untitled 2 21.png]]

![[Media/Untitled 3 20.png|Untitled 3 20.png]]

- 곱셈, 나눗셈의 원리를 진수를 바꾸는 데 사용합니다. 관건은 $a_n$﻿을 알아내는 것입니다.
- 소수점을 표현하는 것에 조심하세요!
    - ==역으로 변환하는건 어케할까 진짜==
- n진수 ↔ a진수 변환을 잘해야 한다
    - 주로 n진수 → 10진수 → a진수 를 씁니다.
    - n승 관계인 경우는 n 자리씩 끊어서 변환합니다.
        - 이 이유를 설명할 수 있나요?
            - 알긴 아는데 말로는 설명을 못할 듯
            - 16으로 나눈 나머지는 2로 4번 나눈 나머지를 나열한 것을 16진법으로 변환한 것과 같기 때문…?

### 1.3 Binary Arithmetic

- Addition
    - 0 + 0 = 0 / 0 + 1 = 1 / 1 + 1 = 0 (1을 다음 계산에 추가합니다.)
- Subtraction
    - 0 - 0 = 0 / 0 - 1 = 1 (1을 다음 계산에서 뺍니다.) / 1 - 0 = 1 / 1 - 1 = 0
- Multiplication
    - 일반적인 곱셈과 같습니다.
- Division
    - 일반적인 나눗셈과 같지만, 1과 0 밖에 없어서 계산이 좀더 편리할 수도 있습니다.

### 1.4 Representation of Negative Numbers

- Signed number
    - n bits 로 수를 표현할 때, 제일 앞의 bit에 1을 붙여 표현합니다.
    - 비효율적입니다.
- 2’s Complement
    - n bits 로 수를 표현할 때, $N^* = 2^n - N$﻿ 으로 표현합니다.
    - 10…0 - $N_2$﻿ 이라고 생각하면 편합니다.
    - 각종 연산시에 bit 를 넘는 수는 버립니다.
    - $-2^{n-1} ~ +2^{n-1}-1$﻿ 까지 표현됩니다.
- 1’s Complement
    - n bits 로 수를 표현할 때, $\bar{N}=2^n-N-1$﻿ 로 표현합니다.
    - 11…11 - $N$﻿ 이라고 생각하면 편합니다.
    - 각종 연산시에 bit 를 넘는 수는 1로 추가합니다.
        
        - Case 를 보고 이해합시다. 이해한 나 칭찬해
        
        ![[Media/Untitled 4 15.png|Untitled 4 15.png]]
        
    - $-2^{n-1}-1 ~~~~~~~ +2^{n-1}-1$﻿ 까지 표현됩니다.

### 1.5 Binary Code

- 8-4-2-1 Code
    - 가장 일반적인 바이너리 코드입니다.
- 6-3-1-1 Code
    - 4 bit 코드로, 순서대로 6-3-1-1 인데… 왜 쓰지?
- Excees-3 Code
- 2-out-of-5 code
- Gray Code
- ASCII Code
    - 2진법으로 각종 문자들을 표현합니다. 7bit 코드입니다.