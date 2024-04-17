---
annotation-target: PDFs/컴퓨터구조/1_computer_abstraction.pdf
---

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

![](https://i.imgur.com/Chm2clH.png)

일반적인 서버보다 훨씬 큰 서버들의 모임이다. 수천 개의 프로세서와 페타바이트(PB) 단위의 메모리를 가지고 있다. 좀 더 진화된 버전은 flash memory를 쓴다고는 하는데... 잘 몰루겠다

## Embedded System (p9)


- wide range
	- automobile! - navigation

#### Post-PC Era (p10)

##### PMDs (p10)

- 작은 mobile device - 이제는 컴퓨터보다 빠르다
- 그래서 블루스택 돌리는게 그렇게 부담이었니

##### SoC (p11)

- 여러 기능을 수행하는 모듈을 하나의 칩에 몰아넣은 것
- 의외로 CPU와 GPU가 절반도 차지하지 않는다

#### New Computing Devices (p12)

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

#### The Power Wall

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
