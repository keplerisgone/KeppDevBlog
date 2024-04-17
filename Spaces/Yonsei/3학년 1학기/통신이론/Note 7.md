
사람이 접하는 signal은 모오두 아날로그, 이를 변환한 것이 Digital signal이다. 그러면 analog 신호를 얼마나 빠르게 보내야 사람이 사용할 수 있을까? 또한 단말 간의 신호는 어떻게 동기화될까?

# Digital Transmission in an AWGN Channel

3p
단말이 실제로 받는 신호는 0과 1로 이루어진 pulse가 된다. 받은 신호를 pulse로 변환하는 것은 TX가 해준다. bandlimited일 경우 저런 신호로 변경, level을 판단해 신호를 변형한다.
기본적인 방법은 Analog와 같지만 장점이 더 많다. 우선 Error의 영향이 매우 적다. 0과 1로만 신호를 받기 때문에 level만 판단하면 된다. 또한 Error를 찾아 직접 수정할 수 있는 가장 큰 특징을 가진다. (**Error Correction**) block도 가능하긴 한데 지금 중요하지는 않다.

**Receiving filter**를 사용한다. 이를 Matched filtering이라고 한다. Optimum detection을 사용해 신호를 받는다. 또한 Digital에서는 *Non-coherent detection*을 사용하는 경우가 많다(performance는 구리다).

AWGN만 고려한다. 매우 간단한 채널.

modulation은 shift를 이용한다. 요런 shift는 방법에 따라 **amplitude-shift, Phase-shift, Frequency-shift**로 나뉠 수 있다. shift는 pulse 신호의 level을 판단하는 식으로 이루어진다. bit로 표현해서.. 이거를 amplitude를 shift한다 해서 shift... level을 결정하는 방법이 굉장히 중요하다.  Amplitude는 level이 미친듯이 많아서 복잡하지만, Phase-shift는 2$\pi$ 까지의 범위를 사용한다. Frequency-shift는 특정 범위 내의 주파수만을 사용한다. level이 올라가면 효율은 높아지지만(아래 question 참고) noise에는 취약해진다. 그래서 RX 단이 중요해진다.

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

$$

time unlimited <-> band limited가 되기 때문에 우리는 

# Single Pulse Transmission in Noise

신호가 pulse이므로 0일 때는 *신호가 없는 것*으로 생각해도 된다. 즉 다음과 같이 received signal을 생각할 수 있다.

$$

$$

노이즈는 최소화~ 메셎니느 최대화~

# Demodulation and Detection

디지털에서는 Demodulation과 detection이 나누어져 있다. AM에서는 단순히 cos 함수를 곱하는 과정이었지만 digital에서는 받는 신호가 pulse이므로, 신호를 정제 + 이를 해석하는 과정이 필요하다.

**Receiving filter**는 Detection을 위해서 SNR을 최대로 증가시킨다.
**Equlizing filter**는 여러 곳을 통과해 일그러진 신호를 보정하는 필터.
우리는 receiving filter를 중점적으로 본다!

# Detection of a Single Pulse in Noise

Y는 전체 received signal에 필터를 씌운 것. Noise term에만 집중해보자. ($g(t)$친구는 단위 필터로 power를 추가하거나 소모하지 않아 1이라고 가정)

> [!note]
> Gaussian noise는 음... 뭐지

이제 신호 파트를 보자, receiving filter이므로 $g(t)$는 SNR을 maximize하는 친구일 것이다. 
그러면 부등식을 사용해서 최댓값을 찾으면 되겠구나! 이 때 하나의 신호는 다른 하나의 constant배, complex conjugated여야 한다. ($f_{1}(x) = kf_{2}^{*}(x)$)
[TODO] - 수식
결론적으로 $g(t)$는 받은 신호와 같은 모양을 갖는다. 

[TODO] - 10p
output은 input의 에너지와 noise의 psd와는 연관이 있지만, input의 모양과는 연관이 없다. 하지만 모양이 match되어야 max SNR을 얻을 수 있다!! -> **matched filter**라고 부르는 이유
모양만 상관있고, 크기는 상관없다. ($g(T-t) = cs(t)$, 상수배) Correlation receiver를 사용한다는 이야기는 matched filter를 쓰는 것과 동일한 말이다. 매우 중요!

> [!note]
> 물론 convolution 기준이므로, 우리가 생으로 볼 때는 모양이 좌우로 뒤집힌 것처럼 보인다.

# Optimum Detection of Binary PAM in Noise

어쨌든 보낸 신호를 그대로 찾을 수 있다. 넴...

# Binary Signal Transmission

Modulation process는 

> [!note]
> bit와 symbol의 차이는 무엇일까요?
> bit는 말 그대로 0과 1을 의미하고, symbol은 bit가 표현하는 signal을 의미합니다. 예를 들어, 01을 이루는 0과 1은 bit, 01이 표현하는 1은 symbol입니다.

## Binary Phase- Shift Keying

와 이게 뭔소리람 16p~

# QPSK Signal Transmission

# Symbol and Bit Error Probabilities

bit가 error날 경우와 symbol이 error나는 경우는 다르게 생각해야 한다. 예를 들어 2 $\to$ 1 error는 하나의 symbol error가 2 bit error가 되지만($10 \to 01$), 1 $\to$ 0 error는 하나의 symbol error가 1bit error가 된다. ($01 \to 00$)

modulation 과정. 주루루룩

근데 이거 시험범위 아니잖아.