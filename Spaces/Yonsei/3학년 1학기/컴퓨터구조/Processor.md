# A Basic RISC-V Processor Implementation

RISC-V의 프로세서를 이해하기 위해서, 다음과 같은 7가지의 간단한 instruction만을 수행할 수 있는 프로세서를 생각해보자.
- *Memory Instructions* : `ld`, `sd`
- *Arithmetic-logical instructions* : `add`, `sub`, `and`, `or`
- *Conditional branch instruction* : `beq`
간단해보이지만 프로세서의 중요 특징들을 알아보기에는 충분하다. 
# Processor Execution procedure

프로세서의 실행은 다음과 같이 이루어진다.
#### step 1
프로세서는 PC(program counter)가 가리키는 값을 instruction memory에게 주고, instruction corresponding을 PC에게 가져다 준다. 이는  instruction의 종류를 판단하는데 사용한다.
#### step 2
instruction의 종류와 이에 사용할 operand fields를 결정하고, 해당 레지스터의 값을 읽는다. 예를 들어, `ls` 같은 경우는 rs1이 필요할 것이다.
#### step 3
**ALU**가 연산을 수행한다. ALU가 하는 행동은 instruction의 종류마다 다르다.
- `add`, `sub`, `and`, `or`의 경우 평범한 arithmetic operation을 진행한다.
- `ld`, `sd`와 같은 메모리 연산의 경우는 메모리 주소를 계산하는 연산을 진행한다. 이는 add와 본질적으로 동일하긴 하다.
- `beq`와 같은 branch instruction은 testing을 진행한다. 이는 내부적으로 sub을 진행한 뒤 0인지 아닌지를 비교하는 방식으로 이루어진다. 
	- `blt` 와 같은 다른 branch instruction도 똑같다, 이 때는 sign 부호로 비교한다
#### step 4
ALU의 연산 이후 행동을 수행한다. 이 또한 instruction의 type 별로 다르다. 
- arithmetic-logical의 경우 `rd`에 결과를 저장한다.
- memory instruction의 경우 data memory에 접근, 데이터를 저장하거나 불러온다.
- branch의 경우는 PC의 위치를 바꾼다. branch가 따로 정해지지 않았을 경우, 다음 PC를 부른다. (PC + 4)
# Basic Implementation of RISC-V Processor

![](https://i.imgur.com/Ud1L7p2.png)

뭔가 회로가 복잡하지만 자세히는 보지 않고 대략적으로 어떤 부분이 어떤 기능을 하는지만 알아보자. **instruction memory**는 실행하고자 하는 program code를 담아놓는 곳이고, **Register**는 x0~x31의 레지스터가 존재하는 공간이다. **Data memory**는 레지스터에 저장되지 못하는 데이터가 따로 저장되는 메모리이다. 
실제 프로세서에서는 두 메모리가 아닌 두 개의 **cache**가 존재하는데, 이는 L1, L2, L3 캐시로 다시 나뉜다. 캐시가 뭔지는 좀 뒤에서 다시 배우자.
## 