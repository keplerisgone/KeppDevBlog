# Instruction and Instruction Sets

컴퓨터가 사용하는 언어, 명령어를 **instruction**이라고 한다. 이를 사용하기 위한 문법은 **instruction set**이라고 하며, **instruction set architecture**라는 standard로 정해져 있다.

기기를 편리하게 관리, 사용하기 위해서 만들어진 것이다!

# Von Neumann Architecture

![|425](https://i.imgur.com/pj0Gq0W.png)

대부분 현대 컴퓨터 구조의 원형이 되는 것이 바로 **Von neumann architecture**이다. *stored-program concept*를 기반으로 만들어졌으며, 다음과 같은 특징을 지닌다.
- **메모리**에 컴퓨터 프로그램이 저장된다.
- *Processing unit* (CPU, ALU)와 같은 연산 장치들은 프로그램을 불러오고 실행하는 역할을 한다. 연산 결과는 다시 메모리에 저장된다.å
- *I/O device*가 존재한다.

# Instruction Sets of Modern Computers

![|600](https://i.imgur.com/EvdlieI.png)

세상에는 다양한 Computer instruction set이 존재하지만, 모두 비스무리~ 하다. 물론 다들 Von neumann 아키텍처를 사용하지만 세부적인 작동방식은 모두 다르다.

# CISC Vs RISC

![|600](https://i.imgur.com/5tjavdC.png)

사용하는 instruction set의 종류에 따라 CISC와 RISC로 나뉠 수 있다.

![|600](https://i.imgur.com/4vdYHvF.png)

**CISC**(Complex instruction set computers)는 assembly instruction을 사용할 때 *적은 수의 line을 사용하기*가 중점이 되는 instruction set이다. power consumption이 적으며, 사람이 알아먹기는 어렵지만 특정 기능을 수행하기는 쉽다. *x86, intel, AMD*에서 사용한다.

![|600](https://i.imgur.com/Ytm2fg0.png)

**RISC**(Reduced instruction set computer)는 *instruction 하나의 기능을 최대한 단순하게 하기*를 중점으로 하는 instruction set이다. 빠르고 간단한 여러 개의 operation이 존재하는 것이 특징이며, *ARM, RISC-v*에서 사용한다. 

# RISC-V Arithmetic Operation

모든 컴퓨터는 **arithmetic operation**을 할 수 있어야 한다. arithmetic operation은 누구나 할 수 있는 수학적 연산을 의미한다. arithmetic operation의 구조는 다음과 같다.

```cpp
add a, b, c
```

- `add` 은 *operation type*이다.
- `a, b, c`은 *operands*으로, 피연산자이다.
- 위는 b와 c를 더해 a에 저장하는 연산을 수행한다.
위와 같은 instruction는 한 번에 하나의 operation을 수행한다. 그리고 arithmetic operation의 경우 세 개의 operand를 가진다.

아래와 같은 C 코드를 RISC-v instruction으로 바꿔보자.

```cpp
f = (g + h) - (i + j);
```

```cpp
add x5, g, h
add x6, i, j
sub f, x5, x6
```

위에서 변수가 저장되는 `x5`, `x6`는 레지스터이다. 

# RISC-V Registers

기본적인 RISC-V는 64bit 사이즈의 레지스터를 가진다. 각 bit 수마다 이름이 있다.
- **doubleword**: 64bits
- **word**: 32bits
- **halfword**: 16bits
- **byte**: 8bits
RISC-V는 32개의 레지스터 `x0-x31`를 가지고 있다. 각각은 정해진 용도가 있다. 이보다 더 수를 늘리지 않는 이유는 속도 때문이다. 물론 레지스터가 많으면 값에 쉽게 접근이 가능한 장점이 있지만 어느정도 수가 늘어나면 접근하는데 오히려 오래걸리게 된다.

## Translation of An Equation Using Register

위의 코드를 register를 이용해 translating하면 다음과 같다. 

```cpp
f = (g + h) - (i + j);
```

```cpp
add x5, x19, x20
add x6, x21, x22
sub x7, x5, x6
```

레지스터를 설정하는 것은 컴파일러가 도맡아 한다.

# Memory Operands

간단한 프로그램은 적은 변수를 사용해 레지스터로 충분히 커버할 수 있지만, 복잡한 data structure를 사용하는 프로그램은 감당하지 못한다. 따라서 이런 경우는 **memory**에 데이터를 저장한다. 
하지만 RISC-V instruction은 레지스터에 저장된 데이터에만 접근할 수 있기 때문에 메모리에 저장된 데이터를 레지스터에 옮겨 사용한다. 이렇게 데이터를 옮기는 instruction을 **data transfer instruction**이라고 한다.

# Data Transfers from/to Memory

레지스터와 메모리 사이의 데이터 이동은 **memory address**를 이용한다. memory는 일종의 1-dimensional array라고 생각하면 된다. 각 메모리 주소 사이의 간격은 무조건 1byte이다. 또한 운영체제마다 다르지만 보통 64bit 운영체제를 사용하므로 하나의 메모리 주소에는 $2^{64}-1$ 종류의 데이터를 저장할 수 있다. 또한 역시 운영체제마다 다르지만 저장하는 data type 별로 사이즈가 다르다. 
char는 1byte, int/float는 4byte, long/double은 8byte.

레지스터에 쓰는 행위를 `load`, 메모리에 쓰는 행위를 `store`라고 한다. 

## Data Transfer Instructions

접근하고자 하는 데이터의 사이즈에 따라 사용하는 instrution이 다르다. 
- `ld, sd`: *load doubleword, store doubleword*로 64bits 데이터를 읽고 쓴다. 
- `lw, sw`: 이하 동문.
- `lh, sh`
- `lb, sb` 

![|575](https://i.imgur.com/nyH1Kbj.png)

위는 doubleword만큼 건너야 하니까 $8*8$ 만큼 offset에서 뛰어넘고 명령어도 `ld`를 쓴다

![|600](https://i.imgur.com/nEGNbFO.png)

store의 경우도 마찬가지인데, 데이터의 크기마다 사용하는 명령어가 다르고, 뛰어넘는 바이트 수도 다르다.
또한 RISC-V는 *alignment restriction*이 없기 때문에, 굳이 word나 doubleword의 주소값이 4, 8의 배수가 될 필요는 없다.

# Big Endian and Little Endian

![|425](https://i.imgur.com/9vujRVU.png)

위 사진은 0x1234567을 저장하는 모습.
**Big endian**과 **little endian**은 multi-byte data를 저장하는 두 가지의 방법이다. 물론 이거 두 개만ㄹ고도 더 있다.

**Big endian**은 가장 큰 바이트부터 낮은 레지스터에 저장하는 방식이고, **Little endian**은 가장 작은 바이트부터 낮은 레지스터에 저장하는 방식이다. Big endian은 *IBM*이, Little endian은 *intel, ARM, RISC-V* 등 대부분 아키텍쳐가 사용한다.

> [!note]
> multi-byte data에서 *가장 큰 바이트*는 가장 왼쪽 바이트(MSB)를 말하고, *가장 작은 바이트*는 가장 오른쪽 바이트(LSB)를 말한다.

# Register Vs Memory Operands

속도와 성능을 향상시키기 위해 *CPU에서 자주 사용하는 것은 레지스터로, 자주 사용하지 않는 것은 메모리로 이동*시키는 전략을 사용한다. 메모리로 데이터가 이동하는 과정은 특별히 **Spilling**이라고 불린다. 레지스터는 좀 작긴 하지만 메모리보다 200배 빠르고 10000배 power efficient하다. data transfer distance가 더 작기 때문.

# Constant (or Immediate) Operands

![|425](https://i.imgur.com/xtM66UI.png)

프로그램은 상수(**Constant or Immediate, 여기서는 Immediate를 더 자주 사용**)를 사용할 수 있는데, 이는 일반적으로 레지스터나 메모리에 접근하는 것보다 훨씬 빠르고 에너지도 적게 소모한다. 0은 특별히 자주 쓰이는 친구이기 때문에 `x0` 레지스터에 저장해 놓았다. 여기에 store하는 것은 모두 무시된다. 
Immediate를 쓰는 instruction도 따로 정의되어 있다. 주로 (arithmetic instruction + i)로 표현되는 편.

# Extension from 32-bit to 64-bit Machines

![|575](https://i.imgur.com/6oWtI4R.png)

별 중요하진 않고 메모리 넓어지면 좋은 거지~
그리고 운영체제 마다 사용하는 데이터 타입의 사이즈가 다르므로 `int64, int32`를 사용해 혼선이 없도록 하자. (아래쪽 표)

# Binary Number

이진수를 표현해보자. 이진수의 single digit은 *bit*이나 *binary digit*으로 불린다. 각 자리는 $2^{i}$를 의미한다.
예를 들어, 11은 다음과 같이 표현 가능하다.

$$
11_{10} = (1\times 2^{3}) + (0\times2^{2})+(1\times2^{1})+(1\times 2^{0}) = 1011_{2}
$$

제일 오른쪽이 **LSB**, 제일 왼쪽이 **MSB**.

n bit의 이진수는 $2^{n}-1$ 범위의 integer를 표시할 수 있다. 이보다 범위를 넘어가면 **overflow**가 발생한다. floating-point number의 경우는 fraction이 표현할 수 있는 범위보다 내려가면 **underflow**가 발생한다. 

![|550](https://i.imgur.com/F1R8BZ4.png)

또 하나 재밌는 점은 사람들이 MB, GB 등의 단위를 셀 때는 10진수로 세는 반면 컴퓨터는 이진수로 인식한다는 것이다. 어쨌든 4GB의 메모리를 감당하기 위해서는 12bits가 필요할 것이다.

# Signed Numbers

부호가 있는 수는 이진수로 어떻게 표현할까? 딱 두가지 방법만 알아놓자.

**One's complement**는 $2^{n}$에서 해당 수를 뺀 후 1을 더 뺀다. 즉 모든 bit를 shift하면 된다.
**Two's complement**는 $2^{n}$에서 해당 수를 빼면 된다. 즉 *one's complement를 하고 1을 더하자*.
둘 모두 MSB가 sign bit이다. 둘 중에서는 two's complement가 더 자주 쓰인다. one's 쪽은 0이 두개라 연산이 불편하다.

![|189](https://i.imgur.com/7Pn3YNu.png)

추가적으로 **Biased Notation**이 있는데, 어느 특정한 수를 기준으로 삼아 0으로 만든 뒤, 거기서 빼고 더하면 양수와 음수를 나타낼 수 있다. 예를 들어, bias를 3으로 잡으면 011이 0이 되고, 010은 -1, 100은 1이 된다. 또한 모든 비트를 뒤집은 뒤 1을 빼면 부호를 반전시킬 수 있다. 나중에 float에서만 부분적으로 사용한다. 

> [!note]
> **Two's complement**는 무조건 **shift 후 1 더하기**로 기억하자.

## Signed and Unsigned Loads

RISC-V에서는 signed number를 어떻게 저장하고 불러올까?
만약 우리가 integer를 레지스터에 저장한다고 가정하자. integer는 4byte를 차지하므로 레지스터의 절반만 차지할 것이다. 그렇다면 남은 절반을 어떻게 채울것인가? sign은 MSB를 이용해 판단하는데, 판단 기준이 사라져버리는 것 아닌가?

![|425](https://i.imgur.com/5rXUGDL.png)

이를 **sign extension**으로 해결한다. unsigned의 경우 남는 bit를 모두 0으로 채우고, sign의 경우 남는 bit를 모두 sign bit로 채운다. 이를 구분하기 위해서 명령어를 다르게 사용한다. (`lwu, ldu, lhu, lbu`)

또한 넒디 넒은 unsigned를 냅두고 signed만 쓰는 것은 멍청이기 때문에 반드시 타입을 구분해서 사용해야 한다. 멍청도의 수준은 `int` > `unsigned int` > `size_t` 순이다. 특히 array나 memory address는 모두 양수 값을 가지므로 `int` 타입을 사용할 일이 없다. pointer는 언제나 64bit임에 유의.

# Instruction Representation in Computers

컴퓨터는 instruction을 어떻게 구분하는 것일까?
각종 Instruction은 **operation type**과 **operands**로 구성되어 있는데, 컴퓨터는 요 친구들을 binary number로 변환한 다음 일렬로 붙여서 하나의 instruction을 구현한다. 
	이 과정에서 레지스터는 고유의 숫자($\text{x0}\to \text{0}$)으로 표현되고, operation type은 미리 정해진대로 변환된다.
이렇게 붙여진 코드를 **machine code**라고 하며, 각각의 instruction은 type마다 다른 format layout을 지닌다.

예를 들어, 다음과 같은 instruction을 변환해보자.

```cpp
add x9, x20, x21
```

RISC-V의 instruction은 무조건! 32bits(4bytes) 크기를 가지고 있으며, type마다 다르지만 주로 6개의 segment를 가지고 있다. 각 segment는 용도, 의미에 따라 opcode, operand 등으로 나뉜다.

![|500](https://i.imgur.com/8Har4ay.png)

segment는 오른쪽부터 읽는다.
- 제일 오른쪽부터 첫번째, 세번째, 마지막 칸은 operation type을 담는다. 위에서는 `add`에 해당
- 두번째는 operand 중 **destination** 역할을 하는 친구를 말한다. 위에서는 `x9`.
- 네번째, 다섯번째는 연산에 사용되는 **source operand**를 말한다. `x20, x21`.

## R-Type

![|575](https://i.imgur.com/zXFjD2j.png)

**R-type**은 일반적인 arithmetic operation이라고 생각하면 된다. 레지스터에 존재하는 값을 이용해 연산을 진행, 다른 레지스터에 결과를 저장한다. 한 개의 `rd`와 두 개의 `rs`, operation type을 나타내는 `opcode, funct3, funct7`으로 구성된다. funct의 이름 뒤 숫자는 차지하는 비트 수를 나타낸다.
- `add`, `sub`, `mul`...

## I-Type

![|525](https://i.imgur.com/G7xvDDm.png)

**I-Type**은 일반적인 연산과 같지만, **Immediate**를 사용한다. 즉 하나의 `rs`, 하나의 `rd`와 immediate를 사용하는 것! 위 R-type에서 쓸모없어진 rs2와 funct7를 immediate로 만들어 사용한다. 12bit가 됏어요!
- `addi`, `subi`, `ld`

## S-type

![](https://i.imgur.com/5Qcd3FD.png)

**S-type**은 하나의 immediate, 두개의 `rs`를 사용하는 타입이다. 이쪽은 I-type에서 쓸모없어진 `rd`를 immediate에 붙였다. 하긴 위치를 바꾸는 것보다 저게 더 효율적일 거 같긴 하다. 미적으로는 불쾌하지만 효율을 잡은 공대생들을 위하여~
- `sd`

> [!question]
> **왜 저건 두 개의 `rs`인가요??**: CPU의 입장에서 생각하면 쉬운데, *내가 연산 결과를 갖다줘야하는* 친구들이 아니라 *값을 가져와야 하는 친구들*이라고 분류하면 편하다. 

아래는 종합 컴파일 예시.

![](https://i.imgur.com/yDk2tV0.png)

## Logical Operations

![](https://i.imgur.com/5stHjW5.png)

이 친구들은 비트 연산자(**bit operator**)라고도 불린다. 모든 binary digit에 대해 연산을 수행한다. 자리 기준은 메모리에 저장된 기준이겠지 (64bit)
- **AND** `&`: 우리가 아는 and 연산자.
	- 원하는 비트만 남기는 **masking**에 사용된다. 
- **OR** `|`: 우리가 아는 or 연산자.
- **XOR** `^`: 우리가 아는 xor 연산자. 
	- not을 구현할 때 사용할 수 있다.

![](https://i.imgur.com/jQmyOCK.png)

요 친구들은 시프트 연산자(**Shift operator**)라고도 불린다. 비트를 왼쪽 오른쪽으로 옮겨준다. 왼쪽 시프트는 무조건 0으로 채워버리지만, 오른쪽 시프트는 원래 MSB에 따라 다르게 채우는 것과 그냥 0으로 미는 것으로 나뉜다.
- `sll, srl`: logical operation, 0으로 민다
- `slli, srli`: immediate 버-전
	- 요 친구들은 **I-type** operation인데, 레지스터의 크기는 64bits이므로 64bits 이상 shift는 의미가 없다. 따라서 12개의 immediate bit 중 6개는 *funct6*로 사용된다.
- `sra, srai`: arithmetic 버전, sign을 존중해준다.
또한 시프트 연산은 2로 나누거나 2를 곱하는 것과 효과가 동일하다.

## Conditional Branch Operations

이 쪽은 조건에 따라 특정 코드로 점프~하는 instruction이다. 길을 선택한다고 해서 **branch**라는 이름이 붙었다.

```cpp
beq x21, x22, L1
bne x21, x22, L1
blt x21, x22, L1
bge x21, x22, L1
```

`beq`의 경우는 두 값이 같을 때 해당 branch로, `bne`의 경우는 두 값이 다를 때 branch로 점프한다. 
`blt`는 *less than*, `bge`는 *greater than or equal*의 뜻을 가진다. 두 가지 종류밖에 없는 이유는 그냥 순서를 바꾸면 되니까 그렇다(실제 컴파일러도 그렇게 구현함). 둘은 unsigned 버전도 있는데(`bltu, bgeu`), 절대값을 취하는 게 아니라 sign bit를 무시하는 효과를 갖는다.

이제 각 조건문을 위 branch operation을 이용해 구현해보자. 참고로 반복문도 조건문의 일종이다.

### If- Else

![|525](https://i.imgur.com/B3SD5do.png)

### Loop

![|525](https://i.imgur.com/bJgOr18.png)

### Switch-case

이 경우는 **branch table**을 사용할 수 있다. 이는 각 경우의 수에 따라 점프할 branch를 64-bit array에 담아놓는 것으로, 나중에 `jalr` 같은 걸로 이용한다. 

# Compilation and Execution of Branch Instructions

![|231](https://i.imgur.com/WOmR7GD.png)

컴파일러는 이런 branch의 이동을 어떻게 구현할까? 우선 컴파일러는 branch의 흐름을 *basic block*으로 정리해본다. basic block은 실행하고자 하는 code의 모임으로, 컴파일러는 이를 최적화하기 위해 노력한다. 
다만 하나의 branch가 모두 끝날 때까지 기다려야(**stall**) 한다는 단점이 존재한다.

# Jump to/from Functions

이제 함수를 다루는 법을 배워보자.

**function**은 특정한 기능을 수행하는 명령어의 집합이다. 따라서, function을 실행시키기 위해서는 함수에 전달할 인자, 함수로 점프~할 명령어 등이 필요하다.
- `x10-x17` 레지스터는 함수의 인자를 담는 곳이다.
- `x1`은 함수의 리턴 값을 담는다.

```cpp
jal x1, FUNC
jalr x0, 0(x1)
```

`jal`(jump and link)는 다음 실행할 instruction의 return address를 저장하고, 해당하는 라벨로 점프한다. 20bit를 넘는 친구는 한 번에 못간다. 
`jalr`(jump and link register)는 다음 실행좌표를 레지스터에 담긴 값으로 지정한다. 위는 return address에 담긴 곳으로 점프하라는 뜻. x0에 저장하는 것은 무시된다.

각종 함수를 실행시키다보면 레지스터가 부족해질 수 있는데, 넘치는 함수 데이터는 메모리에 저장된다. 이 때 실행되는 함수, 사용하는 지역변수는 모두 **stack**에 저장되며, **LIFO**(Last In, First Out)의 원칙을 따른다. 
이 때 각종 친구들이 저장되는 곳을 **Function Call Stack**이라고 한다. 여기는 사용하던 지역변수, return address, FP 등등이 저장된다. **Stack Pointer**는 이 stack의 가장 밑바닥을 가리킨다. stack은 *높은 메모리 주소에서부터 아래로 자라나며 동적으로 저장*되므로 pointer가 필요한 것이다.

![|215](https://i.imgur.com/i75FmlT.png)

## Program Counter (PC)

**Program counter, PC**는 *현재 프로그램이 어디를 실행중인지*를 나타내는 포인터이다. 모든 instruction은 메모리에 저장되기 때문에 사용 가능한 아이디어이다. 
보통 instruction이 실행되면 (PC + 4)로 다음을 가리키며, 이는 하나의 instruction이 4byte를 차지하기 때문에 그렇다. 또한 `jal`이 실행되면 `x1`에는 (PC + 4)가 저장된다. 이것이 바로 다음 실행 위치이기 때문이다.

## Function Call Transition - Example

![](https://i.imgur.com/Hu5zUgN.png)

- 위의 간단한 함수 호출 코드를 assembly로 변환하면 어떻게 될까?


![|575](https://i.imgur.com/gzzW1lT.png)

1. Stack pointer 의 값을 -3 bytes 만큼 옮긴다. - stack에서 사용해야 하기 때문
2. `sd`로 원래 register 의 값을 저장
3. 계산 진행 & `x10`에 return value 저장
4. 원래 register 값 복원 (stack 이용)
5. x1 에 담긴 return address 로 jump

![|600](https://i.imgur.com/C97RsJm.png)

# Calling Convention

![|625](https://i.imgur.com/RdfnHCJ.png)

* register 에 따라 정해져 있다
* temporary register: 자유롭게 이용가능
* x2(sp)가 내려가는데 공간이 부족할 경우 → x8 (fp) 를 이용, 처음 주소를 저장
* 함수의 caller, callee 가 쓰는 temporary register 가 다름
	* `x5-x7, x10-x17, x28-x31`은 caller function이 관리한다.
	* `x8-x9, x18-x27`은 callee function이 관리한다.
* <font color="#c00000">이거를 굳이 왜 나눌까?</font>
	* 레지스터의 상태를 관리하는 책임을 명확하게 하기 위함! 호출하는 레지스터의 종류에 따라 백업의 책임이 다르다
	* 만약 역할이 나누어져 있지 않다면 레지스터의 복원이 꼬여 값을 잃어버리거나 원래 값을 덮어쓸 수 있다

# Nested Function Calls

![|575](https://i.imgur.com/j2xBoDt.png)

recursive function (재귀함수)는 어떻게 컴파일될까?
-> 이는 x1(ra), x10(return value)를 스택에 계속 쌓아가며 이루어진다. 아래의 사진 및 코드를 참고하자. 가장 핵심이 되는 부분은 재귀를 if-else문으로 다시 구현한 점, x1과 x10의 값이 계속 업데이트 된다는 점이다.

![](https://i.imgur.com/bZunXzt.png)

![|625](https://i.imgur.com/JjI1KGQ.png)

# Function Frame and Frame Pointer

![|575](https://i.imgur.com/1E1Ey5n.png)

- 함수를 이용하다 보면 커다란 변수들을 담는 경우가 많아질 것.
- 정확히는 중첩된 함수를 사용할 때 + 함수마다 지역 변수를 사용할 때 sp를 어디로 되돌려야 하는지 모름 -> **fp**가 북마크 역할
- 해당 변수들은 **스택**에 저장된다.
	- 변수의 종류마다 함께 쌓이게 되는데, 이들을 function frame이라고 한다.
	- **Frame pointer** 요런 frame들의 시작 부분을 담고, 스택에 저장된다.
	- **x8**이 FP의 역할을 함.
![|525](https://i.imgur.com/Q9G6aWW.png)

## Stack Pointer Vs Frame Pointer

![|575](https://i.imgur.com/y4YTGBf.png)

- 근데 왜 굳이 둘을 분리해서 사용할까?
	- **stack pointer**는 그냥 현재 스택의 제일 밑부분을 가리키는 포인터로, 함수를 실행하면서 위치가 계속 달라질 수 있다.
	- **frame pointer**는 일종의 북마크 같은 것
- If the stack pointer varies, it isn't easy to locate function frame elements using immediate offsets since the offset values must also vary. 가 뭘까용

# Data in Heap Memory Region and Memory Leak

- **heap**은 동적 메모리이고, C 같은 경우는 `malloc()` 함수로 동적 할당 가능
- 하지만 컴파일러가 이를 자동으로 해제해주지 않으므로, `free()` 를 이용해서 꼭 해제해주어야 함
- 안 그러면 메모리 누수가 일어남
	- 컴퓨터가 메모리 공간이 없다고 인식

# Arrays Vs Pointers

![|500](https://i.imgur.com/Pvzpl85.png)

- 배열에 직접 접근하기 vs 배열 포인터 사용하기
- 위는 **array index** 사용하기
	- x10에 \*array가 담겨 있고, x11에 n이 담겨있다
	- 직접 array를 저장한 다음에 옮겨주는 방식

![|500](https://i.imgur.com/5JRGKf5.png)

- 이거는 array pointer를 이용하는 방식
	- x5에 주소를 저장, pointer의 연산은 바이트 단위로 이루어지므로..
- **얘가 더 빠름**

# Handling Character Data: Load/Store Byte

```cpp
lbu x12, 0(x10)
sb x12, 0(x10)
```

- `char`는 1byte로 취급
- RISC-v에서는 바이트 단위로 데이터 처리 가능 (byte, halfword, word, double word)
- 물론 char를 다룰 때는 `lbu`(load byte unsigned), `sb`(store byte)를 사용해야 함
	- 레지스터는 64-bit의 데이터를 저장하기 때문에, 레지스터의 가장 작은 byte부터 읽고 쓴다.

# Handling String Data: a Series of Characters

- 여러 개의 char로 이루어져 있으므로, 글자 수에 비례
- 마지막에 **\0**이 추가되어 있음 -> 즉 용량은 (글자 수 + 1)bytes
- string의 복사는 어떻게 일어날까...?

![](https://i.imgur.com/JdYD5CA.png)

![](https://i.imgur.com/Dvlnc9e.png)

- 뾰로롱..

# Wide Immediate Operands

![](https://i.imgur.com/fONxxOQ.png)

- 원래 immediate는 instruction type에 따라 달라지지만, 크기가 부족할 수도 있음
- `lui`(load upper immediate)를 사용하면 20bit 레지스터의 상위 [31:12] bit를 불러오기 때문에 더 큰 수를 사용 가능
	- `lui`는 상위 20비트를 불러오고, `addi`는 하위 12비트를 설정할 수 있기 때문에 총 32비트 설정 가능
		- addi 로 쓰고, 12비트 shift 후 addi 쓰는 거랑 똑같음
	- 여기서 MSB가 1일 경우는 잘못된 결과가 나올 수 있다...
		- lui 계산할 때 1을 더해주면 해결 (수학적으로 그렇다)

# U- Type

![](https://i.imgur.com/phcQfqX.png)

- U(upper)-type은 20bit의 immediate를 사용하는 연산 타입이다. 레지스터의 32:12 bit에 해당 immediate를 저장하며, 나머지 왼쪽 비트에는 sign bit를 저장한다. lowest 12bit에는 0을 저장한다. `addi`와 조합해 32bit 수를 표현하는데 쓰인다.
- 잘 안 씀

# SB-Type

![](https://i.imgur.com/jaFgsaj.png)

- SB-type은 12bit immediate와 rs 두개 이용
특정 condition을 만족하면 해당 branch로 이동한다. branch는 메모리 주소로 나타나며, immediate로 표현된다. 

> [!question]
4byte 명령.... 머시기 먼소리야

# UJ-type

![](https://i.imgur.com/bEAOS2u.png)

- 여기도 주소 이동할 때 사용, 20bit immediate사용, `jal`
20bit를 사용하기 때문에 주소는 $\pm2^{20}$까지의 주소를 표시할 수 있다. 따라서 한번에 접근 가능한 범위는 2MB이므로, 프로그램의 용량은 이를 넘어서는 안된다.

> [!question]
> 이게 먼소리냐

# PC-Relative Addressing

![](https://i.imgur.com/FwK9nbI.png)

- direct address를 사용하는 경우는 불편함이 많음
	- 주소 값이 너무 클 수도 있음
- 그래서 PC의 현재 위치에 따라 이동하는 방식을 이용

아래는 array에 모두 1을 더하는 함수를 구현한 것이다.

![|575](https://i.imgur.com/QrVuDZP.png)

![|575](https://i.imgur.com/L8oF9jB.png)

# Branching Far Away

만약 뛰어넘고자 하는 주소가 너무 먼경우 `lui`와 `jalr`를 적절히 조합하여 사용할 수 있다.
우선 `lui`를 이용해 현재 레지스터의 20-bit를 설정한 뒤, `jalr`을 이용해 lower 12-bit를 설정하 점프한다.

> [!question]
> upper 32bit는 PC에서 복사된다고??

# RISC-V Addressing Modes

RISC-V는 다음과 같은 Addressing mode를 지원한다. 

![](https://i.imgur.com/OS2u3dG.png)

1. **Immediate addressing**: instruction의 imm 부분에 있는 데이터 불러오기

![](https://i.imgur.com/2tler23.png)

1. **rs** (source register)에 저장된 데이터 불러오기
1. Base Addressing: 레지스터에 저장된 memory address에 저장된 데이터 불러오기
4. PC-relative addressing: PC를 기준으로 해 데이터에 접근, PC에 immediate offset을 더해 불러온다. (*halfword*만 불러옴)

# Instruction Opcode Encoding

![|550](https://i.imgur.com/KPldVWM.png)

# Summary

![|475](https://i.imgur.com/s5Jw5wp.png)

# Pseudo-instructions

![|525](https://i.imgur.com/3auTnVR.png)

- 사람이 쓰기 편하라고 만들어 놓은 거
