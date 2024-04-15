## Function Call Transition - Example

![](https://i.imgur.com/AeEOISG.png)
- 위의 간단한 함수 호출 코드를 assembly로 변환하면 어떻게 될까?

![400x300](https://i.imgur.com/V2q0j05.png)

1. Stack pointer 의 값을 -3 bytes 만큼 옮긴다. - stack에서 사용해야 하기 때문
2. 원래 register 의 값을 저장
3. 계산 진행 & return value 저장
4. 원래 register 값 복원 (stack 이용)
5. x1 에 담긴 return address 로 jump

![](https://i.imgur.com/C97RsJm.png)

# Calling Convention

![](https://i.imgur.com/KeKc5iV.png)

* register 에 따라 정해져 있다
* temporary register: 자유롭게 이용가능
* x2(sp)가 내려가는데 공간이 부족할 경우 → x8 (fp) 를 이용, 처음 주소를 저장
* 함수의 caller, callee 가 쓰는 temporary register 가 다름
* <font color="#c00000">이거를 굳이 왜 나눌까?</font>
	* 레지스터의 상태를 관리하는 책임을 명확하게 하기 위함! 호출하는 레지스터의 종류에 따라 백업의 책임이 다르다
	* 만약 역할이 나누어져 있지 않다면 레지스터의 복원이 꼬여 값을 잃어버리거나 원래 값을 덮어쓸 수 있다

# Nested Function Calls

![](https://i.imgur.com/rURcqKJ.png)

recursive function (재귀함수)는 어떻게 컴파일될까?
-> 이는 x1(ra), x10(return value)를 스택에 계속 쌓아가며 이루어진다. 아래의 사진 및 코드를 참고하자. 가장 핵심이 되는 부분은 재귀를 if-else문으로 다시 구현한 점, x1과 x10의 값이 계속 업데이트 된다는 점이다.

![](https://i.imgur.com/bZunXzt.png)


![](https://i.imgur.com/dtY2T9y.png)

# Function Frame and Frame Pointer

![](https://i.imgur.com/GRJU77J.png)
- 함수를 이용하다 보면 커다란 변수들을 담는 경우가 많아질 것.
- 정확히는 중첩된 함수를 사용할 때 + 함수마다 지역 변수를 사용할 때 sp를 어디로 되돌려야 하는지 모름 -> **fp**가 북마크 역할
- 해당 변수들은 **스택**에 저장된다.
	- 변수의 종류마다 함께 쌓이게 되는데, 이들을 function frame이라고 한다.
	- **Frame pointer** 요런 frame들의 시작 부분을 담고, 스택에 저장된다.
	- **x8**이 FP의 역할을 함.
![](https://i.imgur.com/Q9G6aWW.png)

## Stack Pointer Vs Frame Pointer

![](https://i.imgur.com/BV38AkA.png)
- 근데 왜 굳이 둘을 분리해서 사용할까?
	- **stack pointer**는 그냥 현재 스택의 제일 밑부분을 가리키는 포인터
	- **frame pointer**는 일종의 북마크 같은 것
		- sp의 위치는 계속해서 바뀔 수 있으므로, 원하는 값에 접근하기 위해서는 많은 노력이 필요하다...

# Data in Heap Memory Region and Memory Leak

![](https://i.imgur.com/bqnTmuU.png)
- **heap**은 동적 메모리이고, C 같은 경우는 malloc() 함수로 동적 할당 가능
- 하지만 컴파일러가 이를 자동으로 해제해주지 않으므로, **free**를 이용해서 꼭 해제해주어야 함
- 안 그러면 메모리 누수가 일어남
	- 컴퓨터가 메모리 공간이 없다고 인식

# Arrays Vs Pointers

![](https://i.imgur.com/9FohH40.png)
- 배열에 직접 접근하기 vs 배열 포인터 사용하기
- 위는 **array index** 사용하기
	- x10에 \*array가 담겨 있고, x11에 n이 담겨있다
	- 직접 array를 저장한 다음에 옮겨주는 방식

![](https://i.imgur.com/d8waiTg.png)
- 이거는 array pointer를 이용하는 방식
	- x5에 주소를 저장, pointer의 연산은 바이트 단위로 이루어지므로..
- **얘가 더 빠름**

# Handling Character Data : Load/Store Byte

![](https://i.imgur.com/dG5D8aY.png)
- `char`는 1byte로 취급
- RISC-v에서는 바이트 단위로 데이터 처리 가능 (byte, halfword, word, double word)
- 물론 char를 다룰 때는 `lbu`(load byte unsigned), `sb`(store byte)를 사용해야 함

# Handling String Data: a Series of Characters

![](https://i.imgur.com/0YP9gWw.png)
- 여러 개의 char로 이루어져 있으므로, 글자 수에 비례
- 마지막에 **\0**이 추가되어 있음 -> 즉 용량은 (글자 수 * 8) + 1
- string의 복사는 어떻게 일어날까...?

![](https://i.imgur.com/KoQPFOO.png)
- 뾰로롱..

# Wide Immediate Operands

![](https://i.imgur.com/6vSlLJa.png)
- 원래 immediate는 instruction type에 따라 달라지지만, 아무튼 부족할 수도 있음
- `lui`(load upper immediate)를 사용하면 20bit를 불러오기 때문에 더 큰 수를 사용 가능
	- `lui`는 상위 20비트를 불러오고, `addi`는 하위 12비트를 설정할 수 있기 때문에 총 32비트 설정 가능
		- addi 로 쓰고, 12비트 shift 후 addi 쓰는 거랑 똑같음
	- 여기서 MSB가 1일 경우는 잘못된 결과가 나올 수 있다...
		- lui 계산할 때 1을 더해주면 해결

# U- Type

![](https://i.imgur.com/xMCe9TY.png)
- U (upper)
- 20비트의 immediate + destination을 이용
- 잘 안 씀

# SB-Type

![](https://i.imgur.com/yZYAsRx.png)
- SB-type은 12bit immediate와 rs 두개 이용
- 주로 instruction 이동에 사용 - immediate는 2byte 단위로 사용
	- 왜 4byte아님? - 개발자들이 그리 해놓음

# UJ-type

![](https://i.imgur.com/KX8dfax.png)
- 여기도 주소 이동할 때 사용, 20bit immediate

# PC-Relative Addressing

![](https://i.imgur.com/DQlLMu7.png)
- direct address를 사용하는 경우는 불편함이 많음
	- 주소 값이 너무 클 수도 있음
- 그래서 PC의 현재 위치에 따라 이동하는 방식을 이용

![](https://i.imgur.com/BIiKLA5.png)

![](https://i.imgur.com/l2UpNRU.png)

# Branching Far Away

![](https://i.imgur.com/Y5moGTD.png)

# RISC-V Addressing Modes

![](https://i.imgur.com/74Ga69D.png)

![](https://i.imgur.com/fqYp8Yw.png)

![](https://i.imgur.com/ZlXEyiD.png)

# Instruction Opcode Encoding

![](https://i.imgur.com/1zDgCqk.png)

# Summary

![](https://i.imgur.com/FGLXy5a.png)

# Pseudo-instructions

![](https://i.imgur.com/REDZVbB.png)
- 사람이 쓰기 편하라고 만들어 놓은 거
