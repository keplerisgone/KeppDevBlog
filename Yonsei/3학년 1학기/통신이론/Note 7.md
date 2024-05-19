사람이 접하는 signal은 모오두 아날로그, 이를 변환한 것이 Digital signal이다. 그러면 analog 신호를 얼마나 빠르게 보내야 사람이 사용할 수 있을까? 또한 단말 간의 신호는 어떻게 동기화될까?

# Digital Transmission in an AWGN Channel

![](https://i.imgur.com/HCc4Ymv.png)

단말이 실제로 받는 신호는 0과 1로 이루어진 pulse가 된다. 받은 신호를 pulse로 변환하는 것은 TX가 해준다. bandlimited일 경우 저런 신호로 변경, level을 판단해 신호를 변형한다.
기본적인 방법은 Analog와 같지만 장점이 더 많다. 우선 Error의 영향이 매우 적다. 0과 1로만 신호를 받기 때문에 level만 판단하면 된다. 또한 Error를 찾아 직접 수정할 수 있는 가장 큰 특징을 가진다. (**Error Correction**) block도 가능하긴 한데 지금 중요하지는 않다.

**Receiving filter**를 사용한다. 이를 Matched filtering이라고 한다. Optimum detection을 사용해 신호를 받는다. 또한 Digital에서는 *Non-coherent detection*을 사용하는 경우가 많다(performance는 구리다).

**AWGN**(Additive White Gaussian Noise) 만 고려한다. 매우 간단한 채널. 아날로그에서 자주 사용한다. 

modulation은 shift를 이용한다. 요런 shift는 방법에 따라 **Amplitude-shift, Phase-shift, Frequency-shift**로 나뉠 수 있다. shift는 pulse 신호의 level을 판단하는 식으로 이루어진다. 받은 signal을 bit로 표현, 이를 다른 amplitude로 shift하기 때문에 저런 이름이 붙여졌다. level을 결정하는 방법이 굉장히 중요하다.  Amplitude는 level이 미친듯이 많아서 복잡하지만, Phase-shift는 2$\pi$ 까지의 범위를 사용한다. Frequency-shift는 특정 범위 내의 주파수만을 사용한다. level이 올라가면 효율은 높아지지만(아래 question 참고) noise에는 취약해진다. 그래서 RX 단이 중요해진다.

> [!question]
> level을 높이면 하나의 signal이 담는 bits의 수가 늘어나 빨라진다.
> 그치만 detection 하는 속도는 느려지지 않나??
> $\to$ 기술의 발전이라고 합니다 결정하는 속도는 같다고 가정

# Bit Error Rate (BER)

$$
BER = \lim_\limits{N \to \infty}(\frac{n}{N})
$$

디지털 신호에서 매우 중요한 성능 지표이다. 전체 보낸 비트 수 중 에러가 난 비트의 개수의 비율을 의미한다. 
물론 그럼에도 SNR가 중요한 지표가 되기는 한다(보낸 신호의 측면에서). 그치만 nonlinear 하게 나타나기 때문에 잘 사용하지 않는다. 물론 SNR과 BER가 일정한 상관관계를 가지는 것도 아니다. (exponential이라고는 한다)
각 분야에서 허용되는 BER은 다음과 같다. (해당 값을 넘으면 사람들이 짜증을 낸다)
- **Vocoded speech**: $10^{-2}$ ~ $10^{-3}$ 
- **무선 데이터 통신**: $10^{-5}$ ~ $10^{-6}$
- **비디오 통신**: $10^{-7}$~$10^{-12}$
- **금융**: $10^{-11}$ 보다 작아야함

> [!note]
> 물론 통신 기술은 그걸 구현하는 소프트웨어가 있을 때 짱짱이 된다. 
> 모든 기술에 감사하십시오 휴먼

**SNR**은 bit energy와 noise spectral density의 비율로 정의된다.

$$
\text{SNR}^\text{digital}_\text{ref}= \frac{\text{Modulated energy per bit}}{\text{Noise spectral density}}= \frac{E_{b}}{N_{0}}
$$

time unlimited <-> band limited가 되기 때문에 우리는 무조건 time unlimited 신호를 보내야한다.. 라고 생각할 수 있지만, 이를 조정하는 방법이 있다. 이는 나중에 알아보도록 하자.

# Single Pulse Transmission in Noise

![|500](https://i.imgur.com/K7JvUlu.png)

신호가 pulse이므로 0일 때는 *신호가 없는 것*으로 생각해도 된다. 즉 다음과 같이 received signal을 생각할 수 있다.

$$
r(t) = 
\begin{cases}
s(t) + n(t) & \text{pulse present} \\
n(t) & \text{pulse absent}
\end{cases}
$$

노이즈를 잘 다루기 위해서는 당연이 signal이 존재할 때는 이 크기를 maximize하고, signal이 없을 때는 크기를 minimize 해야한다.

# Demodulation and Detection

![](https://i.imgur.com/VaUKvKX.png)

디지털에서는 **Demodulation**과 **detection**이 나누어져 있다. AM에서는 단순히 cos 함수를 곱하는 과정이었지만 digital에서는 받는 신호가 pulse이므로, 신호를 정제 + 이를 해석하는 과정이 필요하다.

**Demodulation**은 단순하게 주파수를 원래대로 옮기는 과정이다. AM에서와 동일하다.
**Receiving filter**는 Detection을 위해서 SNR을 최대로 증가시킨다. 다른 말로는 optimum receiving filter, Matched filter/Correlator라고도 부른다.
**Equlizing filter**는 여러 곳을 통과해 일그러진 신호를 보정하는 필터.
**Detector**는 받은 신호를 디지털적으로 해석하는 부분이다. 범위를 통해 symbol을 결정하나..?
우리는 receiving filter를 중점적으로 본다!

# Detection of a Single Pulse in Noise

$$
Y = \int^{T}_{0}g(T-t)r(t)dt \Rightarrow Y=\int^{T}_{0}g(T-t)s(t)dt + \int^{T}_{0}g(T-t)n(t)dt
$$
Y는 전체 received signal에 필터를 씌운 것. Noise term에만 집중해보자. ($g(t)$친구는 단위 필터로 power를 추가하거나 소모하지 않아 1이라고 가정) *filter를 통과시키는 건 convolution인 걸 잊지 않았겠지*
$$
E[n] = \int^{T}_{0}g(T-t)E[n(t)]dt = 0
$$
$$
\begin{align*}
Var(n) = E[n^{2}]=E[\int^{T}_{0}g(T-t)n(t)dt\int^{T}_{0}g(T-t)n(\tau)d \tau] \\ 
= \int^{T}_{0}\int^{T}_{0}g(T-t)g(T-t)E[n(t)n(\tau)]dtd \tau\\
= \int^{T}_{0}\int^{T}_{0}g(T-t)g(T-t)\frac{N_{0}}{2}\delta(t-\tau)dtd \tau\\
= \frac{N_{0}}{2}\int^{T}_{0}|g(T-t)|^{2}d \tau =\frac{N_{0}T}{2}
\end{align*}
$$

따라서 평균과 분산은 각각 0, $\frac{N_{0}T}{2}$를 가지므로 이는 Gaussian noise가 된다!

> [!note]
> Gaussian noise는 음... 뭐지

이제 신호 파트를 보자, receiving filter이므로 $g(t)$는 SNR을 maximize하는 친구일 것이다. 
그러면 부등식을 사용해서 최댓값을 찾으면 되겠구나! 이 때 하나의 신호는 다른 하나의 constant배, complex conjugated여야 한다. ($f_{1}(x) = kf_{2}^{*}(x)$)

![](https://i.imgur.com/mdPsUqw.png)

결론적으로 $g(t)$는 받은 신호와 같은 모양을 갖는다. (마지막의 $s(t)$ term)

![](https://i.imgur.com/FcgsVFS.png)

output은 input의 에너지와 noise의 psd와는 연관이 있지만, input의 모양과는 연관이 없다. 하지만 모양이 match되어야 max SNR을 얻을 수 있다!! -> **matched filter**라고 부르는 이유
모양만 상관있고, 크기는 상관없다. ($g(T-t) = cs(t)$, 상수배) Correlation receiver를 사용한다는 이야기는 matched filter를 쓰는 것과 동일한 말이다. 매우 중요!

![](https://i.imgur.com/0oJC5Di.png)

> [!note]
> 물론 convolution 기준이므로, 우리가 생으로 볼 때는 모양이 좌우로 뒤집힌 것처럼 보인다.

# Optimum Detection of Binary PAM in Noise

어쨌든 보낸 신호를 그대로 찾을 수 있다. 넴...
Matched filter를 통과한 Output은 다음과 같다. 이 때 matched filter는 $g(T-t)=cs^{*}(t)$이다.
$$
s(t) = A\sum_\limits{k=0}^{\infty}b_{k}h(t-kT)
$$
이는 $Ab_{k}T$로 간단히 할 수 있는데, 따라서 최종 output은 $Y = E + n=Ab_{k}T + n$이 된다.

# Binary Signal Transmission

Modulation process는 보통 carrier wave의 amplitude, phase, frequency를 1과 0사이의 값으로 변환시켜 symbol을 전달하는 방식이다. 따라서 무엇을 변환시키는지에 따라 band-pass process를 다음과 같이 세 가지로 나눌 수 있다.
- **Binary Amplitude shift-keying**(BASK)
- **Binary phase shift-keying**(BPSK)
- **Binary frequency-shift keying**(BFSK)

우리는 이 단원에서 **Receiver**를 중점으로 알아볼 것이기 때문에 나머지는 간단하게 알아보자.
- **Source Encoder** : Efficient하게 신호 압축 및 전달
- **Channel Encoder** : error correction/재전송 요청
- **Modulator** : 이전에 다 배운거
- **Pulse Shaping** : [[Note 6 Baseband Digital Data Transmission]]에서 배운거
- **Channel** : 이것도 이전에 배운거

**Receiver**는 **matched filter**와 **Detector**로 이루어져 있다. Binary signal transmission에서 signal은 0 아니면 1로 보내지는데, 그 형태는 방식에 따라 다음과 같이 나뉜다.

![|600](https://i.imgur.com/p7TLaB0.png)

## BPSK

Phase에 따라서 0과 1을 구분해보자. 이는 정의에 따라 달라지는데, 우선 $0 \to \pi$, $1 \to 0$로 정의하도록 하자. 이러면 다음과 같이 modulation - demodulation이 된다.

![|600](https://i.imgur.com/9D6zKHT.png)

## QPSK Signal Transmission

이번에는 quadrature phase-shift keying이다. 각도의 정의는 (x, y)로 하도록 한다. 각도 정보 하나에(symbol) 두 개의 bit 정보를 담고 있다.

![|600](https://i.imgur.com/sCt6Xmn.png)

Demodulation은 위와 같은 방식으로 $\cos$을 곱한다.

![](https://i.imgur.com/gomCueD.png)

이 때 위의 cos, sin은 각각 하나의 축으로 생각할 수 있다.

> [!note]
> bit와 symbol의 차이는 무엇일까요?
> bit는 말 그대로 0과 1을 의미하고, symbol은 bit가 표현하는 signal을 의미합니다. 예를 들어, 01을 이루는 0과 1은 bit, 01이 표현하는 1은 symbol입니다.

# Symbol and Bit Error Probabilities

**Symbol error rate**(SER)는 symbol이 오류가 생기는 경우, **Bit error rate**(BER)은 bit가 오류가 생기는 경우를 말한다. bit가 error날 경우와 symbol이 error나는 경우는 다르게 생각해야 한다. 예를 들어 2 $\to$ 1 error는 하나의 symbol error가 2 bit error가 되지만($10 \to 01$), 1 $\to$ 0 error는 하나의 symbol error가 1bit error가 된다. ($01 \to 00$) 따라서 무조건 BER이 SER과 같지는 않다.

![|600](https://i.imgur.com/LyJ171P.png)

# Likelihood Detection

우리가 가정하는 noise는 AWGN noise이기 때문에 
