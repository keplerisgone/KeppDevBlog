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
Y는 전체 received signal에 필터를 씌운 것. (이 필터는 impulse response로, sampling filter라고도 한다.) Noise term에만 집중해보자. ($g(t)$친구는 단위 필터로 power를 추가하거나 소모하지 않아 1이라고 가정) *filter를 통과시키는 건 convolution인 걸 잊지 않았겠지*
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
$$
\begin{align*}
g(T-t) &= h(t)\\
g_{k}(T-t) &= h(t-kT) & nth \ symbol\\
E &= \int_{(k-1)T}^{kT}h(t-kT)A\sum_\limits{k=0}^{\infty}b_{k}h(t-kT)dt\\
&=Ab_{k}T
\end{align*}
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

우리가 가정하는 noise는 AWGN noise이기 때문에 signal이 최종적으로 Gaussian의 형태를 자나게 된다.

![](https://i.imgur.com/alkUraJ.png)

이 때 신호의 detection은 가장 가능성이 높은 경우로 이루어진다.

## Maximum Likelihood

![](https://i.imgur.com/ErOMaEH.png)

위의 $P(d=i|r)$ (**A posterior probability**)은 어떤 결과 r이 관측되었을 때, 데이터 d가 i를 가질 확률을 의미한다.
- $p(r|d=i)$ : 데이터 d가 특정 값 i일 때 결과가 r일 확률
- $p(d=i)$ : 데이터 d가 특정 값 i를 가질 확률
- $p(r)$ : 결과 r이 관찰될 확률

![](https://i.imgur.com/SpPMBAH.png)

따라서, 결과 r이 관측되었을 때 확률에 따라 symbol을 결정한다. 이를 **Ratio test**라고 한다. 

![|600](https://i.imgur.com/ZLMsRbf.png)

위는 실제 test 과정이다. 이를 $\log$를 씌워 LLR을 진행해 linear로 대수비교를 하는 것이 일반적이다. 아래는 Gaussian 함수를 이용해 test를 적용한 예시이다.

![|575](https://i.imgur.com/6V3rSig.png)

![](https://i.imgur.com/KRqPYy2.png)

위와 같이 결과는 가장 높은 확률을 기준으로 결과를 선택한다. 따라서 error가 나타날 확률은 Gaussian 분포의 바깥 부분이다.

# SER & BER

우선 BPSK의 BEP (Bit Error Probability)는 다음과 같이 계산할 수 있다.

![|575](https://i.imgur.com/pJBsdKf.png)
위는 각각의 확률을 구한 것

![|575](https://i.imgur.com/d5bwIgO.png)
따라서 BER은 **Q function**으로 나타낼 수 있다!

# Gaussian Random Variables

$$
f_{X}(x) = \frac{1}{\sqrt{2\pi}\sigma_{X}}\text{exp}\{- \frac{(x-\mu_{X})^{2}}{2\sigma_{X}^{2}}\}
$$
위에서 주구장창 본 **Gaussian random variables**는 위와 같은 식으로 나타낼 수 있다. 이는 다음과 같은 특징을 지닌다. $\mu_{X}$는 평균, $\sigma_X$는 분산.

1. **Mean**과 **Variance**로 특징을 설명 가능
2. 정규분포 형태를 가진다.
3. **중심극한정리** : 여러 개의 gaussian random variable을 더하면 하나의 gaussian random variable로 수렴한다.
4. 임의의 상수가 곱해지거나 더해져도 여전히 gaussian random variable이 된다.
5. **uncorrelated** 가 뭐지

# Q-function

normalized gaussian distribution function을 정리한 것이다.

![](https://i.imgur.com/GWbG4nr.png)

![](https://i.imgur.com/3WMElWF.png)

따라서 PBE를 Q-function으로 나타낼 수 있다! 각종 분산과 SNR 정리를 이용하면 Q-function임을 증명할 수 있다.
Q-function은 다른 말로 **Complementary error function**이라고도 한다. error function과는 다음과 같은 관계를 가진다.
$$
Q(x) = \frac{1}{2}\text{erfc}(\frac{x}{\sqrt{2}})
$$

> [!note]
> $E_d$로 나타낼 때와 $E_b$로 나타낼 때 값이 다르다.

# Antipodal Signals for Binary Signal Transmission

![](https://i.imgur.com/h8CaxQm.png)

이제 Binary signal transmission에서 Q-function을 이용해 error를 찾는 과정까지 합해보자.
**Antipodal**의 의미는 Binary signal에서 두 개의 symbol을 나타낼 때 파형의 전체적인 모습과 상관없이 symbol을 나타내는 두 signal의 파형이 반대이기만 하면 된다는 뜻이다.

# Decision Theory


![](https://i.imgur.com/O13104x.png)

앞서 배웠던 내용을 종합하면 다음과 같다. *signal source*는 Digital signal을 일정 level로 mapping시킨 신호로, channel까지 통과했다고 생각하면 된다.
noise로는 *AWGN*가 추가되며, 이는 *gaussian process*로 잡아낸다. 사용하는 filter는 *Matched filter*.
다음은 *Decision rule*에 의해 symbol을 결정한다. 이는 *Maximum likelihood*를 기준으로 결정된다. error가 발생할 확률은 *Q-function*으로 계산할 수 있다.

# ML : Vector View

![](https://i.imgur.com/OuMuQny.png)

Likelihood ratio test를 잘 뜯어보면, 이는 결국 *가장 가까운 symbol로 결정됨을 알 수 있다*.
굳이 확률이 아닌 거리로 결정해도 된다는 뜻! 이는 **Maximum correlation**, 또는 **Minimum distance**로 불린다.

# Optimizing Error Performance

![](https://i.imgur.com/jBB0xwX.png)

아무래도 상식적으로 생각해보면 각 symbol이 멀리 떨어져 있을수록 error의 확률이 낮다. 이를 **Time cross-correlation coeff.**, $\rho$ 로 나타낼 수 있다. 이는 두 symbol이 벡터 공간에서 이루는 각으로 표현된다.

따라서 Q-function을 다음과 같이 다르게 표현할 수 있다. Energy difference를 사용함에 유의!

![](https://i.imgur.com/S82qBbP.png)

$\rho$ 의 값에 따른 error의 변화는 다음과 같다.

![](https://i.imgur.com/LVEDIAF.png)

$\rho$ = 1일 때는 error가 0이긴 하지만 현실적으로는 불가능하다. symbol이 하나밖에 없어서 사용할 일이 없다. 의외로 $\rho$ = 0일 때 error 확률이 낮다. orthogonal한 신호를 만드는 것이 목적?

# On-Off Signals for Binary Signal Transmission

![](https://i.imgur.com/UGkBOZp.png)

이는 binary에서 0과 1을 s(t)의 유무로 결정하는 방식이다. 없으면 0, 있으면 1이다. 0인 경우에는 noise만 존재하게 된다.
따라서 0을 받으면 n만 받게 되고, 1을 받으면 E + n을 받게 된다.
noise는 AWGN이므로, PDF는 다음과 같이 나타난다.

![](https://i.imgur.com/rrJQAg8.png)
error는 다음과 같이 계산할 수 있다.

![](https://i.imgur.com/uAnyk4v.png)
이게 만나는 부분이 $\frac{E}{2}$니깐... 절반을 기준으로 할 수 있는거구나

![](https://i.imgur.com/qgeJC2B.png)

Monte Carlo simulation을 통해 performance를 계산한 결과는 위와 같이 된다고 한다.

# Signal Constellation Diagrams for Binary Signals

Binary signal의 경우 다음과 같이 다양한 방법으로 나타낼 수 있다.

![|254](https://i.imgur.com/N77C8rz.png)

- **Antipodal** : one-dimensional로 나타내고, 위상이 반대인 energy가 하나의 축에 나타난다. 각 signal은 E 에너지를 갖는다.
- **On-off** : 0 아니면 E이다.
- **Binary orthogonal** : 수직인 두 신호이다. Two-dimensional이다.

![](https://i.imgur.com/uqlXaII.png)
 어째 error 확률이 다 다르다.
# Binary Transmission

![](https://i.imgur.com/YHmSfwC.png)

당연히 분산에 따라서 달라지겠지요... (사진은 orthogonal 기준)

# Multiamplitude Signal Transmission

![](https://i.imgur.com/DTh83Lx.png)

이번에는 Binary가 아닌 여러 개의 level이 존재하는 Transmission을 알아보자. 그중에서도 amplitude modulation을 사용한 경우이다.
이 때 중요한 것은 각 신호 사이의 거리이다. 거리가 같아야 error 확률이 같아진다.

![](https://i.imgur.com/ShUAybi.png)

이후 **Power normalization**을 진행한다. power의 평균이 1이 되도록 만들면 된다.
power normalization을 진행하는 이유는 위 그래프에서처럼 각 symbol마다 다른 진폭 level을 가지는 상황을 방지하기 위해서이다.

![](https://i.imgur.com/NTR7bW6.png)

Receive는 Minimum distance 원리를 적용해 symbol을 찾아내면 된다.

![](https://i.imgur.com/VOE3TdH.png)

Error의 경우는 왜 저렇게 구하는지 모르겠다...
notation이 휘릭휘릭 바뀌면 어쩌자는거

![](https://i.imgur.com/nQcZQmr.png)

요거는 SER 구하는 예시이다 어차피 위를 이해못하면 이것도 이해 못한다

## Signal Waveforms with Multiple Amplitude Levels

![](https://i.imgur.com/GahpPwI.png)

level이 여러 개 있을 때 signal은 어떻게 분석할까?

# Multidimensional Signals

![](https://i.imgur.com/f2wN0qh.png)

왜 써요 이거
