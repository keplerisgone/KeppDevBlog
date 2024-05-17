
이전에 배운 것
- Carrier modulation: carrier의 성분을 이용해 message를 전송
	- **Amplitude**
	- **Frequency**
	- **Phase**
- Demodulation: carrier-modulated signal에서 message 성분만 빼낸다. carrier signal과 convolution으로 이루어짐
- **Signal-to-Noise Ratio**: noise를 얼마나 잘 잡아내는지 성능 지표

![](https://i.imgur.com/gxmlYtk.png)

Digital modulation은 **Shift Keying**으로 나뉘어진다.

# Digital Transmission in an AWGN Channel

**BER**(Bit error rate)는 디지털에서 SNR보다 자주 사용하는 성능 지표이다.
가장 널리 사용되는 정의는 **Average bit error rate**이다. 전체 길이 N에서 error가 난 bit의 수 n의 비율로 정해진다.

$$\text{BER} = \lim_\limits{N\to \infty} (\frac{n}{N})$$

**Packet error rate**(PER)는 각 분야에서 인정되는 최소의 BER이다. 굳이 이것보다 좋을 필요는 없다.

![](https://i.imgur.com/WnkqFZn.png)

# Baseband Digital Data Transmission

Digital data를 전송하는데 다음과 같은 물리적 한계가 있다.
1. **Intersymbol interference** (ISI)
	- Bandlimited: Bandlimited한 system은 time unlimited인 signal이 된다. 하지만 이는 현실에서 불가능하므로 오차가 생기게 된다.
2. **Channel noise**
	- Channel 자체에서 생기는 noise
- **ISI problem**이 뭔지, 이를 해결하는 방법이 뭔지
- **Baseband pulse-shaping**은 무엇인가
- **eye pattern**: performance 확인 방법

![|575](https://i.imgur.com/TY8t2jJ.png)

# Channel Effects

**Ideal channel**은 다음과 같은 특징을 지닌다.
- 일정한 $k$ 상수 왜곡이 존재한다.
- 모든 신호에 대해 $t_0$ 지연이 존재한다.

![|500](https://i.imgur.com/wMCmCNp.png)

따라서 channel을 통과할 때 **Allpass filter**와 **Linear phase**를 통과하는 것과 같은 효과가 나타난다.

![|400](https://i.imgur.com/YAmk8th.png)

하지만 **Practical channel**은 Bandlimited channel이기 때문에 이를 통과한 신호는 Time-unlimited signal이 된다. 따라서 신호의 symbol에 영향을 주게 되고, 이를 **ISI**라고 한다.

# Eye Pattern

Bandlimited에 의해 신호가 어떻게 변하는지를 나타낸 그래프로, 해당 채널의 성능을 나타낸다.

![|575](https://i.imgur.com/dUttdli.png)

# Baseband Binary Data Transmission

Input binary data $b_k$를 받으면 이를 **line encoder**를 통해 level encoding을 진행한다.
-> $a_k$
받은 signal은 $s(t) = a_k * g(t) =  \sum_\limits{k=-\infty}^{\infty}a_{k}g(t-kT_{b})$로 나타낼 수 있다. $T_b$는 **Bit duration**이다. 

![](https://i.imgur.com/pOZEiRd.png)

이 다음에 **Transmit-filter**, **Channel**, **Receive-filter**를 통과하는데, 이를 합쳐서 $p(t), P(f)$로 정의한다.

![|600](https://i.imgur.com/QZ7Tjhn.png)

# Intersymbol Interference Problem

받은 signal $y(t)$는 이렇게 받는다. (convolution 정의 이용)

$$\begin{matrix}
 y(t) = \sum_\limits{k=-\infty}^{\infty}a_kp(t-kT_{b})\\ y(iT_{b})=\sum_\limits{k=-\infty}^{\infty}a_kp[(i-k)T_b] \\ 
y_{i}=\sum_\limits{k=-\infty}^{\infty}a_{k}p_{i-k} 
\end{matrix} $$
sampling과 simplify를 진행한 값이다. 이 때 가장 중요한 값은 $i=k$일 때이다. 
$$\begin{matrix}
y_{i}=\sum_\limits{k=-\infty}^{\infty}a_{k}p_{i-k} \\ 
y_{i}=\sqrt{E}a_{i}+\sum_\limits{k=-\infty, k\ne i}^{\infty}a_{k}p_{i-k}
\end{matrix}$$
따라서 뒤의 term이 **ISI**가 된다! 이를 zero로 만드는 것이 성능 향상의 목적이다.
pulse spectrum($P(f)$)와 receive-filter는 다음과 같은 조건을 만족시켜야 한다.
1. ISI이 zero가 될 것
2. Transmission bandwidth이 보존된다.

## Pulse Shaping

