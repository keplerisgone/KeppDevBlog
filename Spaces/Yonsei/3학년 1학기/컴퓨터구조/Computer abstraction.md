---
annotation-target: PDFs/컴퓨터구조/1_computer_abstraction.pdf
---
# Introduction

![[1_computer_abstraction.pdf]]
#### computer architecture (p4)

컴퓨터는 어떻게 만들어지나요
재료 - 소자 - 회로 - (기능을 하는) 논리 회로 - microarchitecture? (메모리 관리, CPU 구조 등등)
컴퓨터는 복잡한 계산기이다 <- 사실 처음부터 계산기로 시작함

#### traditional classes of computing systems (p6)
##### personal computers (p6)
- good performance for single users (personal!!!)
	- server computers? for anyone
##### Servers (p7)
- large system <- many small computers - enable to run parallel, sizable workloads, many jobs (good)
	 - security
	 - reliability <- slow running speed
##### Supercomputers (p8)
- extremely large... servers
	PB 단위 살면서 처음본당
	- <span style="background:#affad1">flash memory</span>
##### Embedded system (p9)
- wide range
	- automobile! - navigation
#### Post-PC era (p10)
##### PMDs (p10)
- 작은 mobile device - 이제는 컴퓨터보다 빠르다
- 그래서 블루스택 돌리는게 그렇게 부담이었니
##### SoC (p11)
- 여러 기능을 수행하는 모듈을 하나의 칩에 몰아넣은 것
- 의외로 CPU와 GPU가 절반도 차지하지 않는다
#### New computing devices (p12)
- 
Important concepts in computer achitecture

1.asfd
2.fu
3.ashfassddfj
	잘 짜여진 싱글스레드는 멀티스레드를 이긴다
4.fdshafg
5.drt
6.ghgh
7.ghjfj

translating 

under the hood: processor components

#### Comparing Code Segments (p32)

- instruction의 횟수, 각 Instruction의 CPI의 조합에 따라 성능이 달라짐
- Average CPI를 따질 것인가? 총 코드의 길이(instruction)을 따질 것인가?
#### Basic Elements of Performance Evaluation
- 프로그램의 execution time = Algorithms and compliers + Computer architecture + Circuit design
	- 각각 프로그램의 instruction 수
	- CPI
	- Cycle period
- 모두를 종합적으로 생각해야함
#### Measurement of Performance Elements (p35)
- 어떻게 해당 elements를 측정할 것인가
	- 다양하게 측정
	- Clock cycle time = period같은 경우는 하드웨어로 측정이 가능하나, 나머지는 시뮬레이션 필요
#### Technology Scaling Trends (p36)
- Moore's Law continues (조금 느려졌지만)
- Single-thread performance is bounded (왜 멈췄을까?)
- base clock frequency doesn't increase (왜 멈췄을까?)
- chip power is limited (clock speed와 안좋은 관계 => 어느 순간에 머무를수밖에 없음)
#### Single-Thread Performance Scaling (p37)
- 싱글코어의 퍼포먼스는 더이상 늘지 않는다 - 한계가 존재
- 실제로 멈추기 시작한 부분과 멀티코어가 등장한 부분이 일치
#### The Power wall
- clock frequency와 power consumption은 둘 중 하나를 포기해야하는 구조
- thermal limitation (air cooling)의 한계와 일치
#### End of Dennard Scaling
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
#### Arithmetic Mean vs Geometric Mean
- 일반적인 평균은 중간값보다 못하다
- Geometric mean은 모두 곱한뒤에 제곱근을 씌우는것
#### Amdahl's law

![](https://i.imgur.com/kRXHjnU.png)

- 어떤 application이 몇 퍼를 차지하고 있는데, 이게 이만큼 빨라지면 전체는 몇퍼가 빨라질까?
- 중학교 수준의 수학임
- 1960년도에 태어났으면 님들 뛰어난 공학자가 될 수 있었는데
- 특정 부분의 속도만 증가시키기 때문에 전체 speedup에는 한계가 존재
	- speedup을 변수로 하는 방정식을 풀면 됨
#### Optimization and performance speedup
- python - 느리다. 프레임워크를 사용하거나 프로토타입 코드를 작성하는데 사용
- C, C++ - 빠르다. 서버 쪽에서와 같이 속도가 중요하면 무조건 이거 쓴다
- **Data lever parallelism** : 반복적인 작업을 여러 개의 프로세스로 나누어 처리하는 것, CPU와 GPU에서 처리한다. 반복적인 연산 작업 (벡터 연산, 곱셈 등)을 처리할 때 사용한다.
- **Instruction-level parallelism** : 여러 개의 instruction을 한 번에 처리
- **Memory hiearchy optimization** : 메모리의 접근을 용이하게 하기 위한 정렬
- **Thread-level parallelism** : CPU -> GPU 같은거?
