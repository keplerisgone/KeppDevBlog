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
## Logic Design Conventions

프로세서의 datapath는 *combinational elements*와 *state elements*로 나뉜다. 

**combinational elements**는 ALU와 같이 데이터로 실행되는 구성 요소이다. combonational logic으로 이루어져 있으며, output은 current input에 의해 결정된다.
**state elements**는 레지스터나 메모리와 같이 internal storage를 가지는 요소이다. output이 이전 상태에 의해 결정되기 때문에 sequential logic이라고도 불린다.
## Clocks

clock은 신호가 언제 쓰여질지, 데이터를 언제 읽을지 결정하는 방법이다. 이를 위해서는 *edge-triggered clocking* 방법을 사용한다. 이는 clock 신호가 low, high로 변할 때 데이터가 이동하는 방식이다.
- low -> high = positive, rising edge
- high -> low = negative, falling edge
**synchronous** 디지털 시스템에서는 sequential logic의 input이 들어갈 때는 active clock edge에 들어가기 전 stable value로 들어가야 한다. (timing violation, timing error을 피하기 위함)
edge-triggered clocking 방법을 사용할 경우는 하나의 clock cycle에 한 번의 state transition만이 허용된다. 
디지털 논리 회로의 물리적인 특성이 데이터에 영향을 끼칠 수 있지만, 이는 설계자들이 고려할 사항이지...
## Control Signals and Data Buses

**Control Signal**은 operation에 접근하거나 이를 선택하기 위한 정보가 담긴 신호이다. 
- 신호가 **asserted**일 때는 high, 1
- **de-asserted**는 low, 0
모든 signal은 multiple bits를 가지므로, 이를 전달하기 위해서는 group of wires가 필요하다. 이를 **bus**라고 한다.
bus는 평범하게 64비트 데이터를 옮기는 **data bus**, control signal을 옮기는 **control bus** 등등의 종류가 존재한다. 
## Instruction Fetch

![400](https://i.imgur.com/T1civJC.png)

processor fetch의 첫 번째 단계는 **Instruction Fetch**이다. 이는 총 세 가지로 나뉜다.
- *instruction memory* : program code를 담는 곳이다. 이는 read-only acess mode.
	- 그러면 처음에 프로그램 코드를 넣는 것은 누구인가? -> 그건 hardware가 직접 한다.
- *program counter(PC*) : current instruction의 address이다. 매 clock cycle마다 업데이트 된다.
- *adder* : adder는 PC를 4씩 증가시키는 장치이다. 딱히 branch가 이동하는게 아니라면, 다음 instruction을 가리키는 주소는 (현재 PC + 4)이므로(every instruction occupies 4 bytes), 이를 계속 업데이트 한다.
## Register File

RISC-v에 존재하는 32개의 레지스터는 **register file**라는 데이터 구조에 저장된다. register number는 instruction format에 따라 이름이 붙여진다. (rs1, rs2, rd) 이는 어떤 레지스터에 데이터를 저장하고 읽을지 결정한다. 또한 source operand, destination operand에 접근할 수 있다. 
레지스터 파일은 multi-ported이기 때문에, 하나의 사이클에 multiple register가 접근할 수 있다. 
### Multi-Ported Register File

![](https://i.imgur.com/TnsWBOw.png)
(저따구로 생겨서 한 번에 두 개의 source operand를 뽑아낼 수 있다~)
## ALU Execution

![](https://i.imgur.com/JoHtyNF.png)

R-type instruction에서는 두 개의 source operands를 register file에서 읽어오며, ALU가 요고들로 계산을 한다. 
I, S-type instruction에서는 12-bit immediate value는 sign-extended 64bits로 변하며, ALU로 전달된다. 
SB-type instruction에서는 우선 12-bit immediate value를 진행한 후, 2-byte offset 대로 left shift한 뒤, upper ALU에서 계산을 진행한다. lower ALU은 결과를 비교하는 역할을 한다. 0이랑 비교!!!
## Data Memory Access

ALU는 메모리에 어떻게 접근할까? 메모리 주소를 어떻게 계산해서 접근할까?
이는 base register value에 sign-extended immediate offset을 더해서 계산한다.
`ld`의 경우, data memory에서 value를 뽑아와 사용한다. ALU의 output은 곧 접근하고자 하는 memory address이며, data memory에서 이를 이용해 값을 뽑은 뒤 MUX로 보낸다. MUX로 보내진 데이터는 rd 레지스터에 저장되겠지?
`sd`의 경우는 source operand가 register에서 나온다. 요게 data memory로 들어가는 것.
# Instruction Decode

각 instruction type에 따른 opcode, funct3, funct7 등등은 다음과 같다.

![](https://i.imgur.com/3zSWZKG.png)
## ALU Control Signals

위에서 받은 opcode는 ALU control signal로 번역되어 ALU에 들어간다. 아주 많은 instruction들은 네 가지의 종류(add, sub, and, or)로 바뀌어 들어간다.

![](https://i.imgur.com/UvGTXOu.png)

2bit ALUop는 ALU가 어떤 operation을 수행할지 결정하는 역할을 한다. 
- 00 : add for load and store
- 01 : subtract and test for branch
- 10 : operation type to be determined by funct3 and funct7 (알아서 하겠다는 뜻, 위 말고 나머지)
# Main Control Unit

프로세서가 실행되기 위해서는 6개의 비트가 필요하다. 이 친구들은 무슨 동작을 하는 지 결정하는 역할을 한다. 제대로 실행되기 위해서는 각각의 control bit 6개와 ALUop 2bit가 필요!

![](https://i.imgur.com/OwTjkAO.png)

