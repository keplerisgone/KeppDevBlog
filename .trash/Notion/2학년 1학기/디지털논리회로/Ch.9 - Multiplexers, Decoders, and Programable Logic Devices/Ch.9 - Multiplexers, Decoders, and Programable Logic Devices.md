---
Created: 2023-08-24T15:28
---
## Ch.9 Multiplexers, Decoders, and Programable Logic Devices

### 9.1 Introduction

앞서 설명한 많은 게이트들로 이루어진 하나의 회로를 `integrated circuits` 라고 합니다. 주로 하나의 소자로서 사용됩니다.

IC의 종류에는 `small-scale intergration(SSI), medium-scale integration(MSI), large-scale integration(LSI), very-large-scale integration(VLSI)` 이 있습니다. 모두 규모, 크기에 따라 나눠집니다.

- IC, SSI, MSI, LSI, VLSI
    - 전부 다 규모와 크기만 다른 집적회로이다
- Mulriplexer, Decoder, Encoder, Three-State Buffer
    - 아래에서 더 자세히 설명
- ROMs
    - 역시 아래에서 더 자세히 설명
- PLD
- PLA
- CPLD
- FPGA

### 9.2 Multiplexers

![[Media/Untitled 13.png|Untitled 13.png]]

- input selection을 담당하는 소자입니다.
- $2^n$﻿ bits의 input을 n 개의 selection input으로 선택합니다. 어떻게 보면 minterm 이랑 비슷할 수도
    - 그래서 진짜 minterm 같이 AND-OR gate로 표현할 수 있습니다
    - $2^n$﻿ to n multiplexer는 여러 개의 2-to-1 MUX로 나타낼 수 있습니다.
    - 또한 여러 개의 4bits 의 input 중 선택하는 MUX는 Bus inputs으로 간편하게 나타낼 수 있습니다.

- active-high/low output? deactive high?low enable????

### 9.3 Three-state Buffers

![[Media/Untitled 1 6.png|Untitled 1 6.png]]

- 특정 input(output)을 쓰고 싶을 때만 쓰게 해주기 때문에, 회로가 원하는 대로 작동할 수 있도록 도와줍니다.
- input, control input, output으로 나누어집니다. control input에 따라 회로의 open, close가 달라집니다.
- data selection에도 쓰일 수 있기에, MUX를 대체할 수 있습니다.

![[Media/Untitled 2 6.png|Untitled 2 6.png]]

- 두 개의 buffer를 쓸 경우, X, Z에 유의합시다.
- 이를 이용해서 4-bit adder를 만들 수 있습니다.
- 쌍방향 input/output의 방향을 조절하는 데도 사용할 수 있습니다.

### 9.4 Decoders and Encoders

- Decoders
    
    ![[Media/Untitled 3 5.png|Untitled 3 5.png]]
    
    - 특정 input을 특정 output으로 바꿔줍니다.
    - 주로 이진수를 10진수로 바꾸어 출력하는 데 사용합니다. 예시로는 8x8x8의 값을 지닌 RGB가 있습니다.
    - input bit가 정해진 범위를 초과할 경우, output에는 영향을 주지 않습니다.
    - minterm으로 이루어진 함수를 구현하는 데도 사용합니다.
- Priority Encoder
    - Encoder는 Decoder의 반대 작용을 합니다.
    - 주로 함수 구현에 쓰입니다.
    - priority encoder는 가장 뒤의 1에 priority를 줍니다. 앞의 bits는 don’t care term으로 작동합니다.
    - 가장 뒤에 encode되는 term에 주의합시다. 처음 0말고는 다 1입니다

### 9.5 Read-Only Memories

![[Media/Untitled 4 3.png|Untitled 4 3.png]]

- 특정값을 저장하는 소자입니다.
- N words X n bits로 나타내며, n개의 비트로 N가지 경우를 나타냅니다.
- decoder - memory array 형태, 혹은 통짜 회로로 이루어져 있습니다.
    - 근데 programmable이 중요한거면 decoder - memory array가 낫겠지??
    - memory array는 PLA으로 보면 쉽습니다.

### 9.6 Programmable Logic Devices

- PLA (Programmable Logic Array)
    
    ![[Media/Untitled 5 3.png|Untitled 5 3.png]]
    
    - 왼쪽은 input에 대한 AND array, 오른쪽은 output에 대한 OR array으로 이루어져있는 저장장치입니다. 사용자 함수를 구현할 때 편합니다.
    
    ![[Media/Untitled 6 3.png|Untitled 6 3.png]]
    
    - 위처럼 화살표로 표시하거나 진짜 gate들로 표시하거나 크로스로 표시하거나 점으로 표시하거나 하는데, 점이나 크로스가 제일 편한 거 같습니다.
- PAL (Programmable Array logic)
    
    ![[Media/Untitled 7 3.png|Untitled 7 3.png]]
    
    - 이것도 input을 잘 연결해서 output으로 나타내는 건데, output의 gate를 마음대로 조작할 수 있다는 점이 다른 거 같습니다.

### 9.7 Complex Programmable Logic Devices

- 몇가지 예시만 소개합니다.
- 으에에에ㅔㄹㄱ 그아아아앍
- Xilinx XCRR3064XL CPLD
    
    ![[Screenshot_2023-08-24_at_3.34.48_PM.png]]
    
- CPLD function block and Macrocell
    
    ![[Screenshot_2023-08-24_at_3.35.01_PM.png]]
    

### 9.8 Field Programmable Gate Arrays

여러 개의 로직 블럭들이 필드에 나열된 것을 말합니다. 가장자리에는 입력/출력을 담당하는 블럭들, 중간에는 연산을 담당하는 Configurable Logic Block이 존재합니다. 이렇게 생겼습니다.

![[Screenshot_2023-08-24_at_3.36.38_PM.png]]

- 뭔가 넓은 것들….
- CLB (Simplified Configurable Logic block)
- LUT (LookUp Table)
    - 요건 좀 쓸만 합니다 out값을 알 때의 MUX와 같은 편
- Decomposition
    - 하나의 term을 골라서 묶어버립니다.
    - 카르노맵을 이용하면 더 쉽게 할 수 있습니다.
    - 이 때 사용하는 걸 Shannon’s expansion theorem 이라고 합니다.

![[Screenshot_2023-05-06_at_4.16.47_PM.png]]