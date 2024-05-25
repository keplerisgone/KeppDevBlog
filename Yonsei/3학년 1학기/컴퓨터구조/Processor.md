# A Basic RISC-V Processor Implementation

RISC-V의 프로세서를 이해하기 위해서, 다음과 같은 7가지의 간단한 instruction만을 수행할 수 있는 프로세서를 생각해보자.
- *Memory Instructions*: `ld`, `sd`
- *Arithmetic-logical instructions*: `add`, `sub`, `and`, `or`
- *Conditional branch instruction*: `beq`
간단해보이지만 프로세서의 중요 특징들을 알아보기에는 충분하다. 

# Processor Execution Procedure

프로세서의 실행은 다음과 같이 이루어진다.

#### Step 1

프로세서는 PC(program counter)가 가리키는 값을 instruction memory에게 주고, instruction corresponding을 PC에게 가져다 준다. 이는  instruction의 종류를 판단하는데 사용한다.

#### Step 2

instruction의 종류와 이에 사용할 operand fields를 결정하고, 해당 레지스터의 값을 읽는다. 예를 들어, `ls` 같은 경우는 rs1이 필요할 것이다.

#### Step 3

**ALU**가 연산을 수행한다. ALU가 하는 행동은 instruction의 종류마다 다르다.
- `add`, `sub`, `and`, `or`의 경우 평범한 arithmetic operation을 진행한다.
- `ld`, `sd`와 같은 메모리 연산의 경우는 메모리 주소를 계산하는 연산을 진행한다. 이는 add와 본질적으로 동일하긴 하다.
- `beq`와 같은 branch instruction은 testing을 진행한다. 이는 내부적으로 sub을 진행한 뒤 0인지 아닌지를 비교하는 방식으로 이루어진다. 
	- `blt` 와 같은 다른 branch instruction도 똑같다, 이 때는 sign 부호로 비교한다

#### Step 4

ALU의 연산 이후 행동을 수행한다. 이 또한 instruction의 type 별로 다르다. 
- arithmetic-logical의 경우 `rd`에 결과를 저장한다.
- memory instruction의 경우 data memory에 접근, 데이터를 저장하거나 불러온다.
- branch의 경우는 PC의 위치를 바꾼다. branch가 따로 정해지지 않았을 경우, 다음 PC를 부른다. (PC + 4)

# Basic Implementation of RISC-V Processor

![|525](https://i.imgur.com/Ud1L7p2.png)

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

![400|325](https://i.imgur.com/T1civJC.png)

processor fetch의 첫 번째 단계는 **Instruction Fetch**이다. 이는 총 세 가지로 나뉜다.
- *instruction memory*: program code를 담는 곳이다. 이는 read-only acess mode.
	- 그러면 처음에 프로그램 코드를 넣는 것은 누구인가? -> 그건 hardware가 직접 한다.
- *program counter(PC*): current instruction의 address이다. 매 clock cycle마다 업데이트 된다.
- *adder*: adder는 PC를 4씩 증가시키는 장치이다. 딱히 branch가 이동하는게 아니라면, 다음 instruction을 가리키는 주소는 (현재 PC + 4)이므로(every instruction occupies 4 bytes), 이를 계속 업데이트 한다.

## Register File

RISC-v에 존재하는 32개의 레지스터는 **register file**라는 데이터 구조에 저장된다. register number는 instruction format에 따라 이름이 붙여진다. (rs1, rs2, rd) 이는 어떤 레지스터에 데이터를 저장하고 읽을지 결정한다. 또한 source operand, destination operand에 접근할 수 있다. 
레지스터 파일은 multi-ported이기 때문에, 하나의 사이클에 multiple register가 접근할 수 있다. 

### Multi-Ported Register File

![|600](https://i.imgur.com/TnsWBOw.png)
(저따구로 생겨서 한 번에 두 개의 source operand를 뽑아낼 수 있다~)

## ALU Execution

![|575](https://i.imgur.com/JoHtyNF.png)

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

![|525](https://i.imgur.com/3zSWZKG.png)

## ALU Control Signals

위에서 받은 opcode는 ALU control signal로 번역되어 ALU에 들어간다. 아주 많은 instruction들은 네 가지의 종류(add, sub, and, or)로 바뀌어 들어간다.

![|600](https://i.imgur.com/UvGTXOu.png)

2bit ALUop는 ALU가 어떤 operation을 수행할지 결정하는 역할을 한다. 
- 00: add for load and store
- 01: subtract and test for branch
- 10: operation type to be determined by funct3 and funct7 (알아서 하겠다는 뜻, 위 말고 나머지)

# Main Control Unit

프로세서가 실행되기 위해서는 6개의 비트가 필요하다. 이 친구들은 무슨 동작을 하는 지 결정하는 역할을 한다. 제대로 실행되기 위해서는 각각의 control bit 6개와 ALUop 2bit가 필요!

![|600](https://i.imgur.com/OwTjkAO.png)

# Procedure of Instruction Execution

## R-Type

1. The instruction is fetched from the *instruction memory*, and the PC is incremented by 4.
2. Two source registers are located by `rs1` and `rs2` fields, and their values are read from the register file.
3. The main control unit generates necessary control signals based on the *instruction opcode*. => [[#Main Control Unit]].
4. The *ALU* operates on the data according to the geneated *ALU contol signals*.
5. The ALU output is written to the register file. The destination register is identified by the `rd` field.

## Load Instruction

1. The instruction is fetched from the *instruction memory*, and the PC is incremented by 4.
2. Two source registers are located by `rs1` field and its values are read from the register file.
3. The 12-bit immediate value is *sign-extended*.
4. The main control unit generates necessary control signals based on the *instruction opcode*. => [[#Main Control Unit]].
5. The ALU calculates the memory address by adding the sign-extended immediate to the source register. (ex, `8(x2)`)
6. The data memory is accessed to read the data stored at the memory address.
7. The ALU output is written to the register file. The destination register is identified by the `rd` field.

## `beq` Instruction

1. The instruction is fetched from the *instruction memory*, and the PC is incremented by 4.
2. The `rs1` and `rs2` fields locate two source registers, whose values are read from the register file.
3. The immediate field is shifted left by 1 (= multiplcation by 2), sign-extended, and added to the PC to calculate the branch target => *calculating branch address*
4. The main control unit generates necessary control signals based on the instruction opcode.
5. The ALU subtracts a register value from the other and tests if the result is zero. => *compare *rs1 == *rs2*
6. If the branch is taken, the branch target that was previously calculated is overwritten to the PC. If not. PC = PC + 4

# Single-Cycle Execution

**Single-cycle exection model** is the simplest execution model that the processor can execute *only one instruction at a time*. Each instruction accesses to all processor resources, and *no processor elements are used more than once per instruction execution.*

**The longest instruction** determines the *processor's clock speed*. Thus Single-cycle execution model can be fine with the *simple processor design and instructions*, but with more complicated instructions, such as `fmul` and `fdiv`, they will constrain the maximum clock speed.

# Pipelining Concept

The **pipelining concept** is processor design where the executions of multiple instructions are overlapped, like a factory.
	In the **single-cycle model**, datapath elements work on only a one instruction at a time, except for the one handling the instruction. => *related to instruction memory*
	"**Having other elements work on other instructions can save overall execution time**" is the main idea of Pipelining.


![|550](https://i.imgur.com/su82i58.png)

An (Pretty ugly) example of pipelining, it achives a *16/7* speedup, not 4.

# Single-cycle Vs Pipelined Executions

**Single-cycle model**'s clock period is determined by its the slowest instruction, but the slowest **stage** determines the clock period with **Pipelining execution**. The 'stage' doesn't means *instruction*, but *the datapath elements in processor*. Thus the pipelining execution typically results in a *longer execution time per instruction* than the single-cycle execution. 

The Single-cycle model can improve its performance by reducing its **latency**, and Piplining execution can improve its performance by increasing **throughput**. **Latency** is related to *the execution time of an instruction*, **Throughput** is related to *the amount of data transfered per time*. like capacitance?

만약 instruction의 개수가 충분히 크다면, single-cycle에 대한 pipelining의 actual speedup은 다음과 같이 계산할 수 있다.

$$ \text{Time between insructions}_\text{pipelined} = \frac{\text{Time between instructions}_\text{single-cycle}}{\text{Number of pipline stages}}$$

## Example

![|600](https://i.imgur.com/Khany3H.png)

**Single-cycle** - Total times of instructions are important, and the clock period has to be long enough to cover its the *slowest instruction*, which is `800ps` in the above example.
**Pipelining** - The execution time of each stage(element) is important, and the clock period has to be long enough to cover its the *slowest stage*, which is `200ps` in the above example.

![|600](https://i.imgur.com/ocM8dwp.png)

In the above table, Actual speedup for three loads is **12/7**, not 4.
If instructions are repeated many times, the overall speedup approaches to **a ratio of gap between their first and last load instructions**.

# Traditional 5-stage Pipeline Model

![](https://i.imgur.com/v4LSYXs.png)

가장 자주 사용되는 **Pipeline model**에는 총 다섯 개의 stage가 존재한다.
- **Instruction fetch (IF)**: instruction을 instruction memory에서 가져온다.
	- PC = PC + 4도 수행.
- **Instruction decode (ID)**: instruction information (opcode, operands)를 decoding 한다.
- **Execution (EX)**: ALU가 insturction을 수행한다.
	- 위의 Adder는 branch address를 계산하고 PC로 보내는데 사용한다.
- **Memory (MEM)**: 필요한 경우 data memory에 접근한다.
- **Write Back (WB)**: 필요한 경우 register file에 insturction result를 적는다. (**sd**)

## Pipelined Datapath

traditional pipeline model에는 총 다섯 가지의 stage가 존재하므로, 총 다섯 개까지의 instruction만이 overlapped되어 실행될 수 있다. 
위 표를 보면 insturction의 흐름은 left-to-right로 진행되지만, 몇몇 경우에서 backward로 진행된다.
	마지막 WB stage에서 data를 register로 보내는 경우.
	EX stage에서 branch address를 PC로 보내는 경우.

## Abstract Representation of 5-stage Pipeline

5-stage pipeline은 다음과 같은 diagram으로 나타낼 수 있다.

![|575](https://i.imgur.com/pG7Lsuw.png)

shading이 된 부분은 해당 instruction이 접근하는 부분을 나타낸 것이다.
- **left-shading**: stage에서 wrting을 진행
- **right-shading**: stage에서 reading을 진행
점선으로 이루어진 부분은 절대 접근하지 않는다는 뜻이다.

## Illustration of Pipeline Execution

![|475](https://i.imgur.com/wJJuo2l.png)

- Pipeline execution은 instruction 단위로 표시된다.
- 각각의 stage는 하나의 instruction 밖에 처리하지 못한다.
- 기본적으로 *1cycle - 1stage*를 처리한다.
- datapath를 나누지 않기 때문에 각 stage elements는 insturction 사이에 공유된다.

## Pipeline Registers (FF)

![|600](https://i.imgur.com/51OAPlV.png)

- **Pipeline Registers**는 각 stage를 연결하는 레지스터로, 각 cycle이 지날 때마다 insturction이 통과하는 곳이다. 
- pipeline 단계 간 동기화, 데이터 의존성 관리, 딜레이 조절에 관여한다.
- 이름은 끼어있는 두 스테이지를 붙여 쓴다. (*IF/ID*)

## IF (Instruction Fetch) Stage

![|173](https://i.imgur.com/F5qGG5x.png)

- instruction이 instruction memory에서 읽힌다.
- (PC + 4)로 증가, `beq`를 이용한 경우 PC를 저장한다.

## ID (Instruction Decode) Stage

![|212](https://i.imgur.com/fWGOiuq.png)

- 두 개의 source register를 register file에서 읽고, 12-bit immediate field에서 immediate도 불러온다. 
- instruction type을 고려하지 않고 불러오며, 좀 낭비같지만 간단한 방식이다.

## EX (Exexution) Stage

![|153](https://i.imgur.com/Txl9DHa.png)

- instruction type에 의해 ALU의 할 일이 정해지면 instruction이 실행된다. 
- MUX가 type에 맞게 operand를 가져온다. output은 EX/MEM으로 보내진다.

## MEM (Memory) Stage

![|166](https://i.imgur.com/Fu97bbB.png)

- `store` 명령의 경우 연산 결과를 메모리에 저장한다. 
- 저장된 메모리는 ID/EX나 EX/MEM을 통해 보내진다.
- `load` 명령의 경우 EX stage에서 계산된 주소에서 data를 읽어온다. 
- 읽은 data는 MEM/WB로 가 register에 쓰인다.

## WB (Writeback) Stage

![|425](https://i.imgur.com/ddaG1AA.png)

- MEM/WB으로 전해진 data는 register file로 전달되어 register에 저장된다. 
- 전달되는 data는 ALU의 연산 결과 혹은 data memory이며, MUX는 type에 맞게 이를 선택한다.
- data가 register에 쓰여야하는 경우, destination register (`rd`)가 정의되어야 한다.
	- 하지만 5-Stage 구조에서 하나의 data element는 한 번만 사용되기에 IF/ID register에 접근해 `rd`를 다시 찾아올 수 없다.
	- 따라서 `rd`는 처음부터 pipeline을 따라 이동한다.

## Exercise of Datapath Elements

![|550](https://i.imgur.com/VuXvMcM.png)

- 위 그림은 `ld` 명령의 datapath를 정리한 것이다.
- right-shading은 read만 한다는 

## Single-Cycle Pipeline Diagram

![|650](https://i.imgur.com/y2A7OWK.png)

- **single-cycle pipeline diagram**은 datapath를 하나의 cycle에서 어떤 stage에서 어떤 instruction을 처리하고 있는지를 나타낸 것이다.
- 따라서 execution의 순서는 오른쪽부터 왼쪽이 된다.

## Graphical Multi-Cycle Pipeline Diagram

![](https://i.imgur.com/JlQXW96.png)

- *multi-cycle diagram*은 각 cycle에서 어떤 instruction의 어떤 stage가 처리되고 있는지를 나타낸 것이다.

## Pipeline Control Signals

- **control signal**은 pipelined stage가 적절한 타이밍에 이루어질 수 있도록 돕는 역할을 한다.
- 각 control signal은 docode logic에 의해 생성되며, pipeline resgister를 통과하며 하나씩 사용된다.
- **IF** : 매 clock마다 PC, instruction을 읽기 때문에 control signal이 사용되지는 않는다.
- **ID** : Decoder를 이용해 control signal이 생성된다.
- **EX** : control signal과 instruction 정보(`funct3`, `rd`)가 pipeline register를 통해 전달된다. control signal은 **ALUOp**이다. ALU의 계산을 결정한다.
- **MEM** : 메모리에서 data를 쓰거나 읽는지 파악한다(`MEMWrite`,`MEMRead`). 또한 branch가 선택됐을 경우 이를 IF 단계의 MUX로 보낸다(`PCSrc`).  
- **WB** : 메모리의 data를 register로 보내거나(`MEMtoReg`) 연산 결과를 register로 보낸다(`RegWrite`).

# Pipeline Hazards

- **Pipeline Hazards**는 모종의 이유로 인해 위와 같은 pipeline 구조에서 intruction이 지연되는 현상을 말한다. 이를 *stalled*되었다고 한다.
- stalled된 상태들 **bubble**이라고 한다.
- pipeline hazard는 요인에 따라 **structural, data, control hazard**로 나뉠 수 있다.

## Structural Hazards

- **Structural Hazards**는 하드웨어적인 이유로 발생하는 hazard로, 하나의 element에 여러 개의 stage가 접근해야하는 경우에 발생한다. (간단하게 생각하면 줄이 밀렸어요)
- memory를 multi-port로 만들거나, 여러 개의 ALU를 사용함으로써 해결할 수 있다.
- 하드웨어적인 문제이기 때문에 자세히 다루지는 않도록 한다.

## Data Hazards

![|625](https://i.imgur.com/t1nlkIR.png)

- **Data Hazard**는 데이터에 접근해야 하지만 해당 데이터가 준비되지 않았을 경우로, 데이터가 필요한 instruction이 stalled된다.
- 이는 instruction의 dependent 관계에 의해 결정된다.
- 아래는 위 코드를 pipeline으로 나타낸 것이다. ALU의 계산 결과는 *WB stage*에서 memory나 register에 저장된다. 따라서 *x2* 데이터가 필요한 `and`, `or`, `add`, `sd`는 `sub`의 WB stage가 올 때까지 실행되지 못한다.

![](https://i.imgur.com/9patlpc.png)

### Detecting Data Dependency Between Instructions

이런 instruction 사이의 dependency는 어떻게 판단할까? 
- *ID/EX.rs1*, *ID/EX.rs2*는 각각 