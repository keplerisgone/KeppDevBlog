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

![](https://i.imgur.com/yZgBrzM.png)
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

![](https://i.imgur.com/TSjq3LG.png)

PSD와 Autocorrelation function은 FT 관계를 갖는다. 왜 그런지는 모르겠다. 각 component의 PSD는 같은 형태를 가지며, Noise의 PSD는 이 둘을 합친 형태이다. 이 때 power는 다음과 같다.

![](https://i.imgur.com/xAnyLpy.png)

# Signal-to-Noise Ratios

노이즈를 얼마나 잘 걸렀는지 판단하는 변수는 **Figure of merit**로 불리기도 하는데, 이는 **Post-detection SNR**과 **Reference(Baseband) SNR**의 비율로 나타낸다. detection 이후의 power가 노이즈 detection을 하면서 얼마나 손해를 봤는가?를 보여주는 수라고 할 수 있다.
사용하는 SNR의 종류는 다음과 같다.

![](https://i.imgur.com/e4YpAXZ.png)

- **Pro-detection SNR** : demodulating 이전의 SNR
- **Post-detection SNR** : demodulation 이후의 SNR
- **Reference baseband SNR** : baseband transmission model의 SNR이라고 하면 내가 어찌앎..

**Signal-to-Noise ratio**(SNR)는 신호의 퀄리티를 측정할 수 있는 방법이다. signal의 power와 noise power의 비율을 나타내는 변수이다. 
$$
SNR = {E[s^{2}(t)] \over E[n^2(t)]}
$$
**Reference tranmission model**은 baseband에서 메세지 신호를 보내는 모델로, 다음과 같은 가정을 가진다. 
1. message의 power가 modulated signal power와 동일할 것. 즉 순수한 메세지를 보낼 때는 손실이 없다.
2. message bandwidth에서의 noise power...라고만 하면 제가 어떻게 알아요
### example

![](https://i.imgur.com/ZUy2h4n.png)


# Band-pass Communication System

![](https://i.imgur.com/BI4bkyM.png)

이는 Transmitter와 channel, Receiver 로 이루어져 있다. TX는 carrier frequency에 신호를 담는 역할을 하며, 중간 중간에 신호의 frequency를 IF, RF로 바꾸는 역할을 한다. RX는 Band-pass filter를 통해 신호를 복원하며, 신호를 IF로 변환하는 일도 한다. 

## Effect of Noise on DSB-SC AM

DSB-SC AM에서 noise 계산법을 알아보자. 보내는 신호는 $s(t) = A_{c}m(t)\cos (2\pi f_{c}t+\theta)$라고 가정한다. 모든 노이즈는 AWGN(Additive white Gaussian noise)라고 가정한다. additive가 아니라면 노이즈를 뽑아낼 수 없다. received signal은 $x(t) = s(t) + n(t)$

Pre - detector의 SNR을 구하면 다음과 같다. 
![](https://i.imgur.com/DsjAz2q.png)

Post-demodulation 신호의 SNR을 구하면 다음과 같다.
![](https://i.imgur.com/MU3Vj7q.png)

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
$$ 이고, $\eta$는 modulation efficiency라고 한다. 해당 값은 언제나 1보다 작기 때문에 baseband SNR보다 modulation이후의 SNR이 더 작은 값을 가진다.
	modulation index $k_{a}$는 0.8-0.9 값을 가진다. 
	뭐 아무튼 message는 dynamic range를 가진다....
위와 같은 loss가 발생하는 이유는 Carrier를 통해 옮겨지는 중 원하지 않는 signal이 추가되기 때문??

만약 Envelope detection을 이용한다면??
$$
y(t) = \sqrt{[A_{C}[1+k_{a}m_{n}(t)]+n_{I}(t)]^{2}+n_{Q}^{2}(t)}
$$ 가 되지만, $\sqrt{A^{2}+ B^{2}}$가 $A>>B$일 때 $A$에 가까워지므로, 다음과 같이 정리할 수 있다. $$
V_{r}(t) \approx A_{C}[1+k_{a}m_{n}(t)]+n_{I}(t), \\\\\\\\\\ y(t) = A_{c}k_{a}m_{n}(t) + n_{I}(t)
$$
