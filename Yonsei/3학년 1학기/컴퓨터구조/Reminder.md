## Data size

| 1 bit | 1 byte | 1 halfword | 1 word | 1 doubleword |
| ----- | ------ | ---------- | ------ | ------------ |
| 1 bit | 8 bit  | 16 bit     | 32 bit | 64 bit       |
| -     | 1 byte | 2 byte     | 4 byte | 8 byte       |

| 1KB | $2^{10}$byte | $2^{13}$bit |
| --- | ------------ | ----------- |
| 1MB | $2^{20}$byte | $2^{23}$bit |
| 1GB | $2^{30}$byte | $2^{33}$bit |
| 1TB | $2^{40}$byte | $2^{43}$bit |
| 1PB | $2^{50}$byte | $2^{53}$bit |
| 1EB | $2^{60}$byte | $2^{63}$bit |

## CPI

컴퓨터의 효율, performance는 *execution time이 짧은 정도*로 정의된다. execution time이 짧을 수록 server는 같은 시간에 더 많은 작업을 처리할 수 있다.
$$

\text{Performance} = \frac{1}{\text{Execution time}}

$$
그렇다면 두 컴퓨터의 performance는 어떻게 비교할 수 있을까? performance는 execution time의 역수로 정의되므로 이를 이용한다. **컴퓨터 X는 컴퓨터 Y보다 n배 빠르다**에서 n은 다음과 같이 계산할 수 있다.
$$

n = \frac{\text{Performance}_{X}}{\text{Performance}_{Y}}= \frac{\text{Execution time}_{Y}}{\text{Execution time}_{X}}

$$
$$

\text{Execution time} = \text{clock cycles}\times \text{clock period} = \frac{\text{Clock cycles}}{\text{Clock frequency(or clock rate)}}

$$
$$

\text{Clock cycles}=\text{number of instructions}\times \text{average clock cycles per instructions}

$$
$$

\text{Execution time} = \frac{\text{Instructions}}{\text{Program}}\times \frac{\text{Cycles}}{\text{Instruction}}\times\frac{\text{Seconds}}{\text{Cycle}}

$$
![|525](https://i.imgur.com/kJ2LVUq.png)
![|550](https://i.imgur.com/vw2G9x3.png)

![|550](https://i.imgur.com/tjhVKBd.png)

우선 CMOS에 Capacitor가 달려있다고 가정하자. 그렇다면 위와 같은 회로에서 에너지는 이렇게 계산할 수 있다. 
$$

E = \int^{\infty}_{0}i_{L}V_{o}dt = \int^{\infty}_{0}C_{L}\frac{dV_{0}}{dt}dt=C_{L}\int^{V_{dd}}_{0}V_{o}dV_{o}=\frac{1}{2}C_{L}V_{dd}^{2}

$$
따라서 power는 $\alpha$ (Switching probability), Capacitance, supply voltage의 제곱, clock frequency에 비례한다.

이거는 **Arithmetic Mean**,
$$

A = \frac{1}{n}\sum\limits_{i=1}^{n}a_{i} = \frac{a_{1}+a_{2}+...+a_{n}}{n}

$$
이거는 **Geometric Mean**이다.
$$

(\prod_{i=1}^{n}a_{i})^{\frac{1}{n}}=\sqrt[n]{a_{1}a_{2}...a_{n}}

$$

![|600](https://i.imgur.com/kRXHjnU.png)
$$

\text{speedup} = \frac{1}{(1-f)+\frac{f}{s}}

$$
- instruction code
- branch immediate