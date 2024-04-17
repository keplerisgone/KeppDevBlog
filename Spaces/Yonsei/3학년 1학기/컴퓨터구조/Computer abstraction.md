# Introduction

![|600](https://i.imgur.com/NAYcQlx.png)

1940년도 electronic computing이 발명된 수, computer는 현대 사회에서 빠질 수 없는 물건이 되고 말았다. 컴퓨터가 우리 일상 여기저기에 침투해 삶을 발전시켰다는 것에 부정할 사람은 없을 것이다. 전세계의 수많은 컴퓨터 회사들은 경제에도 거대한 영향을 끼치고 있다. 근데... 컴퓨터는 어떻게 생긴거지??

# What is Computer Architecture?

![|575](https://i.imgur.com/ytFCA6z.png)

컴퓨터 구조는 무엇을 말하는 것일까? 컴퓨터의 어디부터 어디까지를 '컴퓨터 구조'라고 부를 수 있을까? 
위 그림을 보면 알 수 있듯이 컴퓨터 구조라는 단어는 컴퓨터의 내부적인 소프트웨어부터 우리 눈에 보이는 몸체(하드웨어)까지 칭하는 포괄적인 단어이다. 해당 과목에서 다루는 내용은 가운데의 *컴파일러, OS(운영체제), 명령어 처리 구조, 마이크로아키텍쳐, 논리회로*이다. 
위 구조는 각종 재료(*Materials*)들이 모여서 소자(*device*)가 된 뒤, 이것들로 회로(*Circuit*)를 구성한 뒤 또 회로로 특정 기능을 수행하는 논리 회로(*Logic* *Circuit*)를 만드는 방식으로 꼬리에 꼬리를 무는 방식으로 이루어져 있다.
근데 사실 저렇게 복잡하게 모여서 하는 일은 커다란 계산 뿐이다. *컴퓨터는 커다란 계산기다*라는 말도 틀리진 않는다.

이 강의에서는 이런 부분을 배울 수 있다.
- *컴퓨터는 우리가 쓰는 언어를 어떻게 hardware language로 바꾸는 거지?*
- *컴퓨터는 어떻게 코드를 실행하는거지?*
- *프로그램의 performance를 결정하는 요인은 뭐지?*
- *performance를 증가시킬 수 있는 방법은?*

# Traditional Classes of Computing Systems (p6)

## Personal Computers (p6)

*good performance, low cost*에 초점을 맞춘 기기로, single user가 사용하기 좋다. 

## Servers (p7)

서버는 여러 대의 슈퍼컴퓨터가 연결된 거대한 시스템으로, *sizable workloads*나 *many jobs*를 수행하기에 알맞다.
일반적인 PC와 하는 일은 같지만 그 규모가 아예 다르다. 더 큰 용량, power, I/O를 가진다.
서버는 반드시 **reliability**를 갖도록 설계하는데, 이는 crash가 발생했을 경우 손해가 일반 PC보다 막심하기 때문이다.

## Supercomputers (p8)

![|600](https://i.imgur.com/Chm2clH.png)

일반적인 서버보다 훨씬 큰 서버들의 모임이다. 수천 개의 프로세서와 페타바이트(PB) 단위의 메모리를 가지고 있다. 좀 더 진화된 버전은 flash memory를 쓴다고는 하는데... 잘 몰루겠다

## Embedded System (p9)

임베디드 시스템(Embedded system)은 자동차, 비행 시스템 등에서 작동되는 넓은 범위의 무언가를 의미한다. 사실 이것도 컴퓨터의 일종이다. 임베디드 시스템은 특정 하드웨어에서 특정 소프트웨어만을 실행시키도록 설계된 것이 특징이다. 매우 작고 효율적인 구조를 지닌다.

# Post-PC Era (p10)

## PMDs (p10)

![|600](https://i.imgur.com/KIt2cbn.png)

PMD(Personal mobile devices)는 우리가 들고다닐 수 있는 휴대용 기기를 뜻한다. 이미 PC의 성능을 뛰어넘은지는 좀 됐다. 배터리를 전력으로 사용하며, 무선 통신을 사용한다는 점이 특징이다. 

# SoC (p11)

![|625](https://i.imgur.com/wyU5Roo.png)

여러 기능을 수행하는 모듈을 하나의 칩에 몰아넣은 것이다.  의외로 CPU와 GPU가 절반도 차지하지 않는다. CPU와 GPU이외에도 audio module, display 등등 다양한 기능의 unit들이 있다.
neural accelerators, display engines, wireless modems, audio/video DSPs, camera IPU, security modules, sensors (e.g., proximity, gyroscope), GPS, etc.

# New Computing Devices (p12)

아주 다양한 processing unit들이 존재한다.
- **Central Processing unit (CPU)**
- **Graphics processing unit (GPU)**
- **Field-programmable gate arrays (FPGA)**
- **ASIC, accelerators**
- **Quantum processor**

# Important Concepts in Computer Architecture

1. **Use abstraction to simplify a design**: 시스템을 개발하기 위해서 abstraction을 적극적으로 사용한다. 즉 lower-level의 디테일을 숨긴다는 뜻.
2. **Make the common cases faster**: 한 번 쓰이는 연산을 80% 빠르게 하는 것보다 자주 쓰이는 연산을 10% 빠르게 하는 것이 훨씬 낫다.
3. **Performance scaling via parallelism**: parallelism을 이용해 성능 향상을 이룬다. 하지만 과도한 parallelism은 오히려 성능을 낮추는 경우가 있다. 이 때는 차라리 single thread가 낫다.
4. **Performance scaling via pipelining**: 각 연산 과정을 쪼개고 쪼개서 pipelining 시킨다. 자동차 공장이라고 생각하면 쉽다.
5. **Performance scaling via prediction**: 컴퓨터 프로그램은 같은 과정을 반복하는 경우가 많다. 그래서 대충 이렇겠군~하고 찍는게 때에 따라서는 효율적일 수 있다. 물론 틀렸을 경우의 risk보다 이득이 커야하겠지만...
6. **Memory hierarchy**: 무조건 빠르고 큰 메모리가 좋을 것 같지만, 둘 사이에는 tradeoff가 존재한다. 따라서 memory에 계층을 두어 빠르고 작은 - 크고 느린 메모리를 적절하게 사용하도록 한다.
![|525](https://i.imgur.com/S6uS3kV.png)
1. **Reliability via redundancy**: 무조건 시스템은 reliable해야 한다. 특히 비행, 운송 관련 분야에서는 더 중요하다. 가장 간단한 방법은 redundancy를 키우는 것. (backup)

# Translating High-Level Language to Machine Code

![|300](https://i.imgur.com/Ehjnnl9.png)

1. **Compiler**는 우리가 쓴 High-level language code를 assembly code로 바꾼다. 
2. **assembler**는 assembly code를 binary code로 바꾼다. 
3. **Operating system**(OS)는 binary code를 실행한다.

# Under the Hood: Processor Components

![|575](https://i.imgur.com/v6Z5RMa.png)

# Integration Technology for Building Processors

![|600](https://i.imgur.com/Aiid8CX.png)

**Moore**라는 똑똑한 사람이 "칩에 들어가는 트랜지스터의 밀도는 매년마다 두 배로 증가한다" (**Moore's Law**)라고 했지만, 현대에 맞는 법칙은 아니다.

![|575](https://i.imgur.com/xF768hF.png)

**DRAM** 또한 용량의 상승세가 줄어드는 중. DRAM은 각 cell에 bit를 얼마나 쑤셔넣느냐가 중요한데, 이 DRAM cell의 크기를 줄이는데 한계에 봉착했기 때문이다.

## Defects and Wafer Dicing

![](https://i.imgur.com/5CnXAdm.png)

칩을 만드는 공정은 저러하다. 공정 상에서 "완벽한 wafer"를 만드는 것은 불가능에 가까우므로, 각 wafer마다 자잘자잘한 defect가 생기게 된다. 결국 최종 목표는 defect를 줄이는 것이 된다. 
wafer를 잘라 만든 조각을 **Dies**라고 하며, 이를 이용해 칩을 만든다. defect를 줄인다는 말은 defected Dies의 비율을 줄인다는 말과 같다.

## Die Yield

하나의 wafer에 존재하는 dies의 개수를 비율로 나타낼 수 있다. 역시 뭐든 효율을 나타낼 때는 비율이 최고인 것 같다. 

$$
\text{Cost per die} = \frac{\text{Cost per wafer}}{\text{Dies per wafer}\times \text{Yield}} \\ 

$$

$$\text{Dies per wafer} \approx \frac{\text{Wafer area}}{\text{Die area}}$$$$
\text{Yield} = \frac{1}{(1 + (\text{Defects per area}\times\text{Die area}))^{N}}

$$
첫번째 수식은 die 하나의 비용이 얼마나 되는지를 wafer의 전체 cost와 yield를 고려해 계산한 것이고, 두번째 수식은 wafer 하나에 die가 얼마나 나오는지를 계산한 것이다. 세번째는 Yield를 계산하는 식인데, N은 공정 step 수를 의미한다.

# Performance Difinition

컴퓨터의 효율, performance는 *execution time이 짧은 정도*로 정의된다. execution time이 짧을 수록 server는 같은 시간에 더 많은 작업을 처리할 수 있다.
$$

\text{Performance} = \frac{1}{\text{Execution time}}

$$
그렇다면 두 컴퓨터의 performance는 어떻게 비교할 수 있을까? performance는 execution time의 역수로 정의되므로 이를 이용한다. **컴퓨터 X는 컴퓨터 Y보다 n배 빠르다**에서 n은 다음과 같이 계산할 수 있다.
$$

n = \frac{\text{Performance}_{X}}{\text{Performance}_{Y}}= \frac{\text{Execution time}_{Y}}{\text{Execution time}_{X}}

$$
## Performance Evaluation in Clock Cycles

![|600](https://i.imgur.com/me4Ss7k.png)

Clock Cycle을 이용해 performance를 정의할 수도 있다. 이는 processor마다 다른데, clock period (1/Clock Frequency = rate)가 다르기 때문이다. Execution time을 Clock Cycle을 이용해 나타낼 수 있다.
$$

\text{Execution time} = \text{clock cycles}\times \text{clock period} = \frac{\text{Clock cycles}}{\text{Clock frequency(or clock rate)}}

$$
예를 들어, 2GHz clock rate를 가진 컴퓨터가 어떤 프로그램을 실행할 때 10초가 걸린다 하자. 다른 컴퓨터는 해당 프로그램을 실행하는데 6초가 걸리지만 1.2배의 clock cycle을 갖는다고 한다. 그러면 다른 컴퓨터의 clock rate는 4GHz가 된다!
## Performance Evaluation in CPI

어떤 program의 코드는 여러 개의 instruction이 모여 만들어진다. 사용하는 clock cycles를 나타내는 또 다른 방법은 instruction을 이용해 나타낼 수 있다. 이 때 사용하는 것이 바로 **CPI**(**clock cycles per instruction**) 인데, 이는 모든 instruction이 가지는 평균 clock cycle로 구해진다.
$$
\text{Clock cycles}=\text{number of instructions}\times \text{average clock cycles per instructions}
$$

![|475](https://i.imgur.com/O400ZTR.png)
위와 같은 문제에서, *같은 프로그램을 실행시켰을 때* 비교하는 것이 중요하다. N개의 instruction을 가지는 프로그램을 실행시켰다고 가정할 때, clock rate는 두 배 차이나고 CPI는 0.6배 차이나므로 1.2배의 성능차이가 나는 것은 맞는데, 뭐가 더 빠를까? (답은 A)
# Comparing Code Segments (p32)

![|475](https://i.imgur.com/u0ULwQY.png)

![|475](https://i.imgur.com/fqW8UZS.png)

위 두가지 type의 instruction set이 있을 때, 어떤 것을 선택해야 잘 골랐다고 소문이 날까?
- **number of instructions**를 따지는 경우
	- *Code1*의 경우 $2 + 1 + 2 = 5$
	- *Code 2*의 경우 $4 + 1 + 1 = 6$
- **CPI**를 따지는 경우
	- *Code1*의 경우 $\frac{2\times 1 + 1\times 2 + 2\times 3}{5}=2$
	- *Code2*의 경우 $\frac{(4\times 1)+(1\times 2)+(1\times 3)}{6}=1.5$
Average CPI를 따질 것인가? 총 코드의 길이(instruction)을 따질 것인가? 알아서 잘 고르자.

# Basic Elements of Performance Evaluation

프로그램의 execution time에는 다양한 parameter가 관여한다.
$$
\text{Execution time} = \frac{\text{Instructions}}{\text{Program}}\times \frac{\text{Cycles}}{\text{Instruction}}\times\frac{\text{Seconds}}{\text{Cycle}}
$$
여기서 첫번째 term은 알고리즘과 컴파일러의 영역, 두번째 term은 컴퓨터 구조의 영역, 마지막 term은 회로 디자인의 영역이다.

![|525](https://i.imgur.com/kJ2LVUq.png)

따라서 위와 같은 모든 영역의 변수를 고려해 performance를 결정해야 한다.
## Measurement of Performance Elements (p35)

Performance를 측정하는데 필요한 요소들은 어떻게 측정할까?
- *Clock cycle time* : product specifications를 본다 => 메뉴얼을 읽는다는 뜻
- *Instruction count* : 소프트웨어의 Hardware counters를 이용한다.
- *CPI* : hardware simulators나 hardware counters를 이용한다. 이는 프로세서나 하드웨어에 따라 달라지기 때문에 여러 번 측정해야 한다.
# Technology Scaling Trends (p36)

![|550](https://i.imgur.com/1SaHsMa.png)

- Moore's Law continues (조금 느려졌지만)
- Single-thread performance is bounded (왜 멈췄을까?)
- base clock frequency doesn't increase (왜 멈췄을까?)
- chip power is limited (clock speed와 tradeoff => 어느 순간에 머무를수밖에 없음)

## Single-Thread Performance Scaling (p37)

![|550](https://i.imgur.com/IFngJdJ.png)

single thread의 퍼포먼스는 한계가 존재해 더이상 늘지 않는다. 실제로 멈추기 시작한 부분과 멀티코어가 등장한 부분이 일치한다.

## The Power Wall

![|500](https://i.imgur.com/0fCDVLj.png)

clock frequency가 증가하면 성능이 향상되지만, power consumption 또한 증가하게 된다. 따라서 둘은 **thermal limitation**에 의해 묶이게 되었다.

## End of Dennard Scaling

**Dennard Scaling**이란 
- 트랜지스터의 크기가 작아져 밀도가 두배가 되면 소모 전력도 두배가 될 것 같지만, 크기만큼 소모전력도 줄기 때문에 엄청 이득이라는 말
- 근데 현실에서는 아니기 시작함 - 균형이 깨짐

#### Consequences of Increasing Power Density

- 이제는 속도 증가보다는 power density를 줄이는데 노력 - 속도에 신경쓰면 따땃해지기 때문

#### Multicore Processors

- 놀랍게도 문제에 직면한 때 = 멀티코어가 상용화되었을 때

#### Energy and Power

![](https://i.imgur.com/CFZ4ZtT.png)

- Power는 다음에 비례함

#### Performance, Power, Energy, Voltage, Frequency

- 각 관계를 보여줌

#### Arithmetic Mean Vs Geometric Mean

- 일반적인 평균은 중간값보다 못하다
- Geometric mean은 모두 곱한뒤에 제곱근을 씌우는것

#### Amdahl's Law

![](https://i.imgur.com/kRXHjnU.png)

- 어떤 application이 몇 퍼를 차지하고 있는데, 이게 이만큼 빨라지면 전체는 몇퍼가 빨라질까?
- 중학교 수준의 수학임
- 1960년도에 태어났으면 님들 뛰어난 공학자가 될 수 있었는데
- 특정 부분의 속도만 증가시키기 때문에 전체 speedup에는 한계가 존재
	- speedup을 변수로 하는 방정식을 풀면 됨

#### Optimization and Performance Speedup

- python - 느리다. 프레임워크를 사용하거나 프로토타입 코드를 작성하는데 사용
- C, C++ - 빠르다. 서버 쪽에서와 같이 속도가 중요하면 무조건 이거 쓴다
- **Data lever parallelism**: 반복적인 작업을 여러 개의 프로세스로 나누어 처리하는 것, CPU와 GPU에서 처리한다. 반복적인 연산 작업 (벡터 연산, 곱셈 등)을 처리할 때 사용한다.
- **Instruction-level parallelism**: 여러 개의 instruction을 한 번에 처리
- **Memory hiearchy optimization**: 메모리의 접근을 용이하게 하기 위한 정렬
- **Thread-level parallelism**: CPU -> GPU 같은거?
