---
Created: 2023-08-22T23:48
---
## Ch.7 Multi-level Gate Circuits / NAND and NOR Gates

### 7.1 Multi-level Gate Circuits

여러 개의 게이트가 포함된 회로의 경우, 다음과 같은 속성을 가지고 있습니다.

- Number of gates : 말 그대로 게이트의 개수입니다.
- Number of Inputs : 말 그대로 인풋의 개수입니다.
- level : 게이트의 층수를 말합니다. 층수를 세는 기준은 연산의 횟수입니다.

![[Media/Untitled 33.png|Untitled 33.png]]

# of gate : 6  
# of input : 13  
level : 4  

- Terminology : AND-OR, OR-AND, OR-AND-OR, AND and OR
    - all OR/AND gates → next all OR/AND gates → next…

![[Media/Untitled 1 25.png|Untitled 1 25.png]]

# of gate : 6  
# of input : 19  
level : 3  

- level 을 줄이는 법 : using distributive law → multiplying out
- minimum sum-of-product form’s level is always 2
    - by using distributive law, we can reduce it
    - no change in # of gates

### 7.2 NAND and NOR Gates

- NAND : Not AND
    
    - (not+not)NAND ⇒ OR
    
    ![[Media/Screenshot_2023-08-22_at_11.59.56_PM 2.png|Screenshot_2023-08-22_at_11.59.56_PM 2.png]]
    
- NOR : Not OR
    
    - (not+not)NOR ⇒ AND
    
    ![[Media/Screenshot_2023-08-23_at_12.00.05_AM 2.png|Screenshot_2023-08-23_at_12.00.05_AM 2.png]]
    

### 7.3 Design of Two-level Circuits Using NAND and NOR Gates

conversion은 모든 곳에 버블을 붙여서 이루어집니다.

버블을 붙이는 행위는 드모르간의 법칙을 적용하는 것과 같습니다.

- AND-OR → conversion → NAND-NAND / OR-NAND / NOR-OR
- OR-AND → conversion → NOR-NOR / AND-NOR / NAND-AND

![[Media/Untitled 2 24.png|Untitled 2 24.png]]

- what form of circuit is most simple
- NAND-NOR 가 안되는 이유 - 어차피 AND gate 하나면 해결가능 - level이 하나로 줄어듦

### 7.4 Design of Multi-lavel NAND-and NOR-Gates Circuits

- How to convert to Multi level NAND gates
- 근데 사실 아래의 짝수 레벨 홀수 레벨 따지는 거는 오류가 많이 발생합니다. 홀수 짝수를 따지기보다는 버블을 붙이는 방식으로 구분하는 걸 추천합니다.

![[Media/Untitled 3 23.png|Untitled 3 23.png]]

![[Media/Untitled 4 18.png|Untitled 4 18.png]]

### 7.5 Circuits Conversion Using Alternative Gate Symbols

![[Media/Untitled 5 14.png|Untitled 5 14.png]]

- 왜 씀

![[Media/Untitled 6 13.png|Untitled 6 13.png]]

- 위의 NOR gates inverting algorythm을 사용

![[Media/Untitled 7 11.png|Untitled 7 11.png]]

- AND-AND-OR-OR gates 같이 레벨이 안 맞는 경우는 inverter를 이용해서 맞춰준다

### 7.6 Design of Two-level, Multiple-Output Circuits

![[Media/Untitled 8 9.png|Untitled 8 9.png]]

- 공통적으로 사용되는 input을 고려할 것