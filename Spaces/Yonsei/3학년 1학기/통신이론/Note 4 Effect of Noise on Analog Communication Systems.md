# Effect of Noise in Communication Systems

신호에 생긴 노이즈가 어떤 영향을 끼치는지 알아보자. 주로 노이즈는 보내진 신호에 더해져 보내지며, 이를 **Additive white Gaussian Noise**라고 한다. 따라서 받는 신호의 수식은 다음과 같다.
$$
r(t) = s(t) + w(t) (=n(t))
$$
이 때 $r(t)$는 받는 전체 신호이고, $s(t)$는 보낸 신호, $n(t)$는 노이즈이다. 아날로그 통신 체계의 가장 주가 되는 문제가 바로 노이즈를 처리하는 것이다. 이를 얼마나 잘 처리하는지는 보낸 신호와 노이즈의 power 비로 나타낼 수 있으며, **Signal to Noise Ratio**(SNR)라고 한다. (${S\over N} = {E[s^{2}(t)]\over E[n^{2}(t)]}$)

AM같은 경우, Coherent detection를 사용하는 경우 Oscillator를 사용하고, 사용하지 않는 경우는 envelope detector(Diode-RC)를 사용한다. 이 때는 Performance panalty가 존재.

FM 같은 경우는 애초에 Nonlinear한 시스템이기 때문에 noise 또한 nonlinear한 형태가 된다. plat한 노이즈가 들어와도 결과적으로는 parabolic noise가 된다. Bandwidth가 높아질수록 noise에 대한 저항력이 커진다.

# Bandpass Signals

Bandpass Signal을 $x(t)= A\cos (2\pi f_{c}t+\theta)$ 라고 하면 신호는 사실 Phasor인 $Ae^{j \theta}$만 들고 다녀도 된다. 오일러 공식에 의해 real 성분만 뽑아낸다면 signal을 금방 복원해낼 수 있기 때문. 결국 signal은 다음과 같은 다양한 방식으로 표현할 수 있다.

![|575](https://i.imgur.com/yZgBrzM.png)
핵심은 Phasor 정보를 잘 저장하는 것.
# Properties of  the Thermal Noise

narrowband noise process를 통해서 noise를 In-phase component와 Quadrature component로 나눌 수 있다. 
$$
N(t) = N_{I}(t)\cos (2\pi f_{c}t)- N_{Q}(t)t\sin 
(2\pi f_{c}t)
$$
앞 쪽이 in-phase, 뒤 쪽이 quadrature이다. 특징은 다음과 같다.
- 둘다 zero mean을 가짐
- noise가 gaussian이면 둘 다 gaussian
- noise가 stationary면 둘 다 stationary
-  둘은 같은 PSD(power spectral density)를 가짐, 이는 다음과 같이 정의 가능
	- $S_{N_{I}}(f) = S_{N_{Q}}=S_{N}(f-f_{c})+ S_{N}(f+f_{c}), (-B\le f\le B)$
- Same varience를 가진다.
# Narrowband Noise

![|600](https://i.imgur.com/TSjq3LG.png)

PSD와 Autocorrelation function은 FT 관계를 갖는다. 왜 그런지는 모르겠다. 각 component의 PSD는 같은 형태를 가지며, Noise의 PSD는 이 둘을 합친 형태이다. 이 때 power는 다음과 같다.

![|425](https://i.imgur.com/xAnyLpy.png)

# Signal-to-Noise Ratios

노이즈를 얼마나 잘 걸렀는지 판단하는 변수는 **Figure of merit**로 불리기도 하는데, 이는 **Post-detection SNR**과 **Reference(Baseband) SNR**의 비율로 나타낸다. detection 이후의 power가 노이즈 detection을 하면서 얼마나 손해를 봤는가?를 보여주는 수라고 할 수 있다.
사용하는 SNR의 종류는 다음과 같다.

![|550](https://i.imgur.com/e4YpAXZ.png)

- **Pre-detection SNR** : demodulating 이전의 SNR
- **Post-detection SNR** : demodulation 이후의 SNR
- **Reference baseband SNR** : baseband transmission model의 SNR이라고 하면 내가 어찌앎..

**Signal-to-Noise ratio**(SNR)는 신호의 퀄리티를 측정할 수 있는 방법이다. signal의 power와 noise power의 비율을 나타내는 변수이다. 
$$
SNR = {E[s^{2}(t)] \over E[n^2(t)]}
$$
**Reference tranmission model**은 baseband에서 메세지 신호를 보내는 모델로, 다음과 같은 가정을 가진다. 
1. message의 power가 modulated signal power와 동일할 것. 즉 순수한 메세지를 보낼 때는 손실이 없다. 즉 Pre-detection과 baseband가 같다.??
2. message bandwidth에서의 noise power...라고만 하면 제가 어떻게 알아요
### example

![](https://i.imgur.com/ZUy2h4n.png)


# Band-pass Communication System

![|625](https://i.imgur.com/BI4bkyM.png)

이는 Transmitter와 channel, Receiver 로 이루어져 있다. TX는 carrier frequency에 신호를 담는 역할을 하며, 중간 중간에 신호의 frequency를 IF, RF로 바꾸는 역할을 한다. RX는 Band-pass filter를 통해 신호를 복원하며, 신호를 IF로 변환하는 일도 한다. 

## Effect of Noise on DSB-SC AM

DSB-SC AM에서 noise 계산법을 알아보자. 보내는 신호는 $s(t) = A_{c}m(t)\cos (2\pi f_{c}t+\theta)$라고 가정한다. 모든 노이즈는 AWGN(Additive white Gaussian noise)라고 가정한다. additive가 아니라면 노이즈를 뽑아낼 수 없다. received signal은 $x(t) = s(t) + n(t)$

Pre - detector의 SNR을 구하면 다음과 같다. 
![|525](https://i.imgur.com/DsjAz2q.png)

Post-demodulation 신호의 SNR을 구하면 다음과 같다.
![|600](https://i.imgur.com/MU3Vj7q.png)

Baseband SNR을 구하면 다음과 같다. $({S \over N})_{b} = {P_{R}\over N_{0}W}= {A_{c}^{2}P_{m}\over 2N_{o}W}$

따라서 DSB-SC AM의 Figure of merit는 Post-demodulation SNR = Baseband SNR이므로 1의 값을 가진다. 따라서 DSB-SC AM은 딱히 SNR의 improvement도 없고 그렇다.

## Effect of Noise on SSB AM

SSB AM의 modulated signal은 $s(t) = {A_{c}\over c}m(t) \cos(2\pi f_{c}t)\mp {A_{c}\over 2}\hat{m}(t)\sin(2\pi f_{c}t)$ 이므로, **Pre-Detect SNR**을 구할 때는 위의 DSB-SC 와 비교해서 $E[s^{2}(t)]$의 값은 같지만, $E[n^{2}(t)]$는 single band이기 때문에 절반의 값을 가진다. 따라서 SNR은 ${A_{C}^{2}P_{m}\over 4N_{0}W}$이긴 한데 어차피 구하는 방식이 같으니까 Figure of merit가 1이 되겠지? 하고 넘어가는 거다

## Effect of Noise on Conventional AM

이 때는 modulated signal이 $$
s(t) = A_{C}[1+ k_{a}m(t)]\cos (2\pi f_{c}t)
$$ 이기 때문에 SNR을 다음과 같이 계산할 수 있다.

우선 Pre-Detection SNR.
$$
E[s^{2}(t)] = {A_{C}^{2}\over 2}E[(1 + k_{a}m(t))^{2}]={A_{C}^{2}\over 2}E[1 + 2k_{a}m(t)+k_{a}^{2}m^{2}(t)] \\ 
$$
$$
=> E[s^{2}(t)] = {A_{c}^{2}\over 2}\{1 + k_{a}^{2}P_{m}\}
$$
Noise power는 DSB-SC와 파형이 같으므로 그대로 $2N_{0}W$이다. 
Pre-detector SNR의 값은 ${A_{C}^{2}\{1+ k_{a}^{2}P_{m}\}\over 4N_{0}W}$이다. 이렇게 얻어낸 신호를 envelope detector를 이용해 demodulation한다.

Post-demodulation SNR이다. 이 경우는 envelope detection을 하지않고 정직하게 carrier를 곱해 detection한다고 가정한다.
$$
v(t) = [s(t) + n(t)]\cos(2\pi f_{c}t)
$$
여기서 LPF를 통과시켜 low frequency만 남기면
$$
y_{l}(t) = {1\over 2}A_{C}[1+k_{a}m_{n}(t)] + {1\over 2}n_{I}(t)
$$
DC 신호를 없애면.. $$
y(t) ={1\over 2}A_{C}k_{a}m_{n}(t) + {1\over 2}n_{I}(t)
$$
Signal power, $$
{1\over 4}A_{C}^{2}k_{a}^{2}P_{m_{n}} 
$$ Noise power는 $$
{1\over 4}P_{n_{I}}={1\over 2}N_{0}W
$$ 따라서 post-demodulation SNR은 $$
{A_{C}^{2}k_{a}^{2}P_{m_{n}}\over 2 N_{0}W}
$$ 이다.

Baseband SNR은 $$
({S\over N})_{b}={P_{R}\over N_{0}W} = {A_{C}^{2}\over 2}{[1+k_{a}^{2}P_{m_{n}}]\over N_{0}W}
$$ 이다.

따라서 전체 Figure of merit는 $$
{k_{a}^{2}P_{m_{n}}\over [1+k_{a}^{2}P_{m_{n}}]}({S\over N})_{b} = \eta({S\over N})_{b}
$$ 이고, $\eta$는 modulation efficiency라고 한다. 해당 값은 언제나 1보다 작기 때문에 baseband SNR보다 modulation이후의 SNR이 더 작은 값을 가진다. 따라서 power 측면에서는 좀 그렇지만 방송 쪽에서 많이 사용했었다.
	modulation index $k_{a}$는 0.8-0.9 값을 가진다. 
	뭐 아무튼 message는 dynamic range를 가진다....
위와 같은 loss가 발생하는 이유는 Carrier를 통해 옮겨지는 중 원하지 않는 signal이 추가되기 때문??

만약 Envelope detection을 이용한다면??
$$
y(t) = \sqrt{[A_{C}[1+k_{a}m_{n}(t)]+n_{I}(t)]^{2}+n_{Q}^{2}(t)}
$$ 가 되지만, $\sqrt{A^{2}+ B^{2}}$가 $A>>B$일 때 $A$에 가까워지므로, 다음과 같이 정리할 수 있다. $$
V_{r}(t) \approx A_{C}[1+k_{a}m_{n}(t)]+n_{I}(t), \\\\\\\\\\ y(t) = A_{c}k_{a}m_{n}(t) + n_{I}(t)
$$
근데 만약 아니라면??? noise가 additive가 아니기 때문에 SNR을 분석할 수가 없다.

### examples..

![](https://i.imgur.com/72l9oUD.png)


![](https://i.imgur.com/vFD9cEU.png)

![](https://i.imgur.com/3Gbp1mo.png)

![](https://i.imgur.com/18euQXA.png)
# Effect of Noise on Angle Modulation

**Amplitude modulation**에서는 노이즈가 신호에 바로 추가되지만, **Angle modulation**에서는 조금 다르다.
**Frequency modulation**에서는 노이즈가 크기에 더해지긴 하지만, frequency term에 메세지가 포함되어 있으므로 노이즈가 바로 눈에 보이지는 않는다. 다만 신호의 주파수가 달라지게 되는데, 이는 *zero crossing*에 영향을 주게 된다. 

![|325](https://i.imgur.com/9NqtmLW.png)

두 경우에서 모두 노이즈가 발생했지만, Power가 높은 아래 신호에서 노이즈의 영향이 덜한 것을 볼 수 있다. power가 작은 신호일 수록 노이즈에 의한 zero crossing이 더 자주 발생.

# Detection of Angle Modulation

**Angle modulated signal**은 다음과 같이 표현 가능하다.
$$
u(t) = A_{c}\cos{(2\pi f_{c}t + \phi(t))}
\begin{cases}
A_{C}(2\pi f_{c}t + 2\pi k_{f}\int^{t}_{-\infty}m(\tau)d\tau) & FM \\
A_{c}\cos(2\pi f_{c}t + k_{p}m(t)) & PM \\
\end{cases}
$$
**Pre-Detection SNR**을 구하면 다음과 같다. 이는 Baseband와 동일.
$$
x(t)=u(t) + n(t) = u(t) + n_{c}(t)\cos(2\pi f_{c}t) -n_{s}(t)\sin(2\pi f_{c}t)
$$
$$
\begin{matrix}
E[u^{2}(t)] = E[(A_{c}\cos(2\pi f_{c}t + \phi(t)))^{2}] = \frac{A_{c}^{2}}{{2}} \\ 
E[n^{2}(t)] = \frac{N_{0}}{2}2B_{T}=\frac{N_{0}}{2}2(2W) = N_{0}B_{T}= 2N_{0}W \\ 
SNR_{pre} = \frac{A_{c}^{2}}{2N_{0}B_{T}}=\frac{A_{c}^{2}}{4B_{0}W}
\end{matrix}
$$
**Post-Demodulation SNR**을 구하면 다음과 같다.
$$
\begin{matrix}
n(t) = n_{I}(t)\cos(2\pi f_{c}t)- n_{Q}(t)\sin(2\pi f_{c}t) \\ 
= r(t)\cos[2\pi f_{c}t]
\end{matrix}
$$
$$
\begin{matrix}
r(t) = [n_{I}^{2}(t) + n_{Q}^{2}(t)]^{\frac{1}{2}} \\ 
\phi_{n}(t) = \tan^{-1}\frac{n_{Q}(t)}{n_{I}(t)} \\ 
{Phase diff.}, \psi_{n}= \phi_{n(t)}- \phi(t) \\ 
\theta(t) = \phi(t) + \tan^{-1}\{\frac{r(t)\sin(\psi_{n}(t)}{A_{c}+r(t)\cos(\psi_{n}(t))}\} \\ 
\theta(t) = \phi(t) + \frac{r(t)\sin(\psi_{n}(t)}{A_{c}} = \phi(t) + n_{Q}(t)/A_{c}
\end{matrix}
$$

위상 차이는 $0$가 될 것이고,  중간에 신호의 크기가 크다는 가정이 중요하다. $\tan^{-1}$의 경우는 들어가는 값이 매우 작으면 일차 함수처럼 작용한다고 볼 수 있기 때문. 또한 신호의 크기가 클수록 = power가 강할 수록 노이즈 영향이 적어진다는 것을 표현하는 것이기도 하다. 

![](https://i.imgur.com/TPQMH3I.png)

demodulated의 phase 표현 방식, 마지막에 Discreminator에 통과시킨다는 사실에 주목하자. 마지막 Phase term에서 메세지가 적분 형태로 나타나므로, 이를 끄집어내기 위해서 통과시키는 것이다. 굳이 통과시키는 이유는 당연히 메세지 signal을 얻기 위해서...

하지만 이를 통과시키면서 *노이즈의 형태도 변한다는 것이 중요하다.*


![](https://i.imgur.com/TLcJ1z2.png)

Carson's rule도 사용한다. Baseband의 bandwidth가 얼마인지 몰라도 된다고...?가 아니라 Bandwidth가 늘어나는 정도에 제곱해 SNR이 향상된다.

## Example - Multiplexed Channels

![|600](https://i.imgur.com/EB0B4XP.png)

소리가 왼쪽 오른쪽 나뉠 때 노이즈가 들어가면 어떻게 될까?
우선 왼쪽과 오른쪽 시그널의 frequency를 shift해서 나누어 생각해보자. 이를 baseband signal로 생각한다. 왼쪽과 시발 뭔소리세요???
# Effect of Noise on angle modulation

![|575](https://i.imgur.com/RajEBIM.png)

**FM**일 경우 노이즈가 주파수의 제곱에 비례하기 때문에 저주파수에서는 괜찮지만 **고주파수로 갈수록 노이즈에 고통받는다**. 이는 노이즈의 스펙트럼이 parabolic으로 나타나는 것에서 볼 수 있다.
근데 PM은 노이즈가 상수라고?? Flat noise spectrum을 가진단다.
- [ ] -> PM 수식을 유도하는 것은 숙제라고 합니다 중간고사 전까지 제출!!!

## example

![](https://i.imgur.com/9fT91WL.png)

# Threshold Effect in angle modulation

demodulator에 들어가는 신호의 SNR이 매우 좋다(=높다) 고 가정, 또한 노이즈가 linear하게 더해진다고 가정.
=> nonlinear할 경우에는 계산이 거의 불가능, 신호로부터 잡음을 분리할 수 없어 SNR을 계산할 수 없다.
결론적으로 이를 계산하기 위해서는 어느 정도의 SNR이 보장되어야 한다. (=**Threshold SNR**)
BW를 높이는 것이 Power를 높이는 방법이 될 수 있지만, FM의 경우는 주파수의 제곱에 noise power가 비례하므로 적절하게 BW를 선택해야한다. *=> tradeoff*

![|325](https://i.imgur.com/O9M1bBv.png)

위 그래프는 어느정도의 SNR이 확보되어야 SNR이 뻥튀기되는지를 나타내는 것이다. 이는 $\beta$에 비례한다. $$({S \over N})_{b,th} = 20
(\beta+1)$$
기본적으로 우리는 baseband SNR을 계산할 수 있고, received power인 $P_{R}$도 계산할 수 있으므로, 알아서 잘 $\beta$값을 계산해보자. BW이 주어져도 마찬가지이다. Carson's rule을 사용하면 될 일.
정리하면, Threshold를 고려해 적당히 큰 $\beta$를 선택하되 사용하는 BW에 맞는지도 고려해야 한다.

![|600](https://i.imgur.com/j2e60pQ.png)

실제로 예시 signal을 가져와 Threshold effect를 살펴본 것이다. 사실 수식을 보면 알겠지만 수식 유도 한 번만 해보면 모든게 이해가 가는 것을 알 수 있다. 한 번 위에서 유도한 공식을 계속해서 우려먹기 때문. 위 수식을 보는 법은 (얻게 되는 db scale gain + baseband SNR) & (Threshold SNR) 이다.
따라서 $\beta = 5$일 때는 원래 15.7dB의 gain을 추가적으로 얻어야 하지만 20dB일 경우 Threshold인 20.8dB를 넘지 못해 나가리가 되는 것.

그리고 가장 중요한 것은 모든 게 다 **dB scale이라는 것이다!!!** 잊지 말자.


![|600](https://i.imgur.com/ZsYfURl.png)

짜잔 PM일 때는 output baseband SNR은 어떻게 될까요~
위 수식은 SNR에 Threshold SNR을 넣어버린 것

## Example

![](https://i.imgur.com/NZ5BzxH.png)

![](https://i.imgur.com/x3Wdui2.png)

# Preemphasis and Deemphasis Filtering


![|625](https://i.imgur.com/bkXs8oD.png)

이전에 보았듯이 PM에서 noise의 power는 flat한 형태를 지니고, FM에서는 parabolic한 형태를 가진다. 즉 FM는 저주파에서, PM는 고주파에서 좋다. 그러면 저주파수는 FM modulation, 고주파수는 PM modulation을 쓰는게 좋지 않을까? 물론 실제로는 불가능하다. 
이 아이디어에서 출발한 것이 바로 **Preemphasis, Deemphasis Filtering**이다.


![|350](https://i.imgur.com/M3Xrazs.png)

FM에서는 고주파 부분에서 noise가 확 뛰기 때문에 이를 조절하는 것이 가장 중요하다. 이를 위해 다음과 같은 방법을 사용한다.
1. low frequency는 감쇄, high frequency는 증폭시키자. (noise를 flat한 것처럼 속이는 방법)
2. demodulation을 진행한 후 다시 원래대로 high는 감쇄, low는 증폭시킨다. 
3. Net effect로 Flat한 response를 얻을 수 있다!

# Comparison of Analog-Modulation Systems

AM은 Linear, FM와 PM은 nonlinear이다. 이 친구들을 세 가지 측면에서 비교할 수 있다.
1. **Bandwidth 효율**
2. **Power 효율**
3. **설계 난이도** : 예를 들어 Conventional AM의 경우 envelope detector는 만들기가 매우 쉽다. 

## Bandwidth Efficiency

**SSB-SC**의 경우는 Bandwidth의 측면에서 가장 우월함을 보인다. 보내는 신호의 bandwidth와 받는 신호의 bandwidth가 동일하며, bandwidth가 중요한 분야(통화 등)에서 자주 사용한다. 하지만 DC 전송 효율이 매우 떨어지므로 이미지 전송 분야에서는 사용하지 않는다.

**VSB**의 경우는 DC 전송이 매우 잘 되지만 Bandwidth는 SSB-SC보다 살짝 높아 효율이 떨어진다. 이미지 전송, TV 방송 분야에서 사용.

**PM, FM**은 Bandwidth에서 효율이 매~우 구리지만 noise immunity가 그만큼 높다.

## Power Efficiency

이는 적은 power로 얼마나 많은 신호를 보낼 수 있냐를 나타내는 것

**angle, 특히 FM**의 경우는 굉장한 Power efficiency를 보인다. point-to-point 통신, 라디오 방송에서 쓰인다. SSB와 섞이면 통화에서도 쓰인다.

**AM** 친구들의 경우는 Angle 친구들보다 효율은 덜하지만 구현이 쉽다..!

## Ease of Implementation

![](https://i.imgur.com/YTiRcKI.png)

# Summary

![](https://i.imgur.com/TN4LWHl.png)

# Gaussian

**Gaussian**은 신호 체계에서 중요한 역할을 한다. 어디로 튈 지 모르는 노이즈에서 다른 사전 정보를 이용해 예측을 가능케 하는 것이 바로 **Gaussian process**이다. 

우리가 사용하는 노이즈는 **white noise**인데, 사실 white process는 무한한 주파수 영역대를 갖지만, 실제 thermal noise는 그렇지 않다. 하지만 적절한 범위에서$\frac{kT}{2}$인 **PSD**(Power spectrum densuty)를 가지므로 이를 $\frac{N_{0}}{2}$로 정의하기로 하자.

![|450](https://i.imgur.com/Sjh3w3W.png)
