Outputstage는 주로 오디오 시스템을 구성하는데 사용된다. 

![](https://i.imgur.com/DjJC6Wk.png)
 
**outputstage**는 출력 단계로, 증폭된 신호를 load impedance에 전달하는 역할을 한다.
결국 가장 중요한 것은 *Amplifier*와 *Load impedance* 단계이다. 

예를 들어 다음과 같은 회로를 생각해보자. (CE amplifier + load resistance)

![|400](https://i.imgur.com/50ARtAW.png)

본래 CE stage의 gain은 output impedance에 의해 결정된다. load resistance를 output에 연결할 경우, output impedance가 획기적으로 낮아지기 때문에 gain 또한 획기적으로 낮아지게 된다. 

이를 해결하는 방법은 **Buffer**를 연결하는 것이다. 주로 CC stage를 Buffer로 사용한다. 연결한 모습은 다음과 같다.

![](https://i.imgur.com/3kjmZIk.png)

여기서 1W의 소리를 내고싶다면 $V_p$의 값이 4V가 되어야 한다. 즉 output voltage가 4V가 되어야 한다.
gain을 구할 때는 무조건 $\frac{1}{g_{m}} < \frac{R_{L}}{10} = 0.8$이어야만 $A_{v} \approx 1$이 성립한다. 이러면 $I_{C}$가 32.5mA이어야겠죠! 따라서 output voltage는 $I_{C}\times R_{L} = 260mV$가 된다. 

![|500](https://i.imgur.com/trly7Yt.png)

*input voltage*로 sin 신호를 넣는다고 가정한다 -> positive의 경우는 0.8V가 가감, negative의 경우는 -260mV까지 떨어짐 (왜 여기까지인가 -> $I_{C}\times R_{L}$ 범위)

![|325](https://i.imgur.com/aYEUDyj.png)

위와 같이 발생하는 신호의 왜곡을 **Distortion**이라고 한다. 이를 표현하는 지표는 **THD**(Total harmonic distortion)이다. distortion은 harmonic의 개수와 크기로 표현된다. 이를 제거하는데는 feddback이 관여한다. 

# Push-Pull Outputstage

하지만 output voltage가 4V가 되어야 하는데, 위 회로에서는 턱없이 부족하다. 
그러면 current source의 출력을 0.5A로 늘리면 되지 않을까?
하지만 이는 *heat dissipation*이 커져 출력하려는 전압보다 소모하는 전압이 커진다. 
이를 해결하기 위해서는 **cascade**를 이용한 **push-pull outputstage**를 활용한다. 

![|500](https://i.imgur.com/XS4vkOt.png)

다만 이러면 출력이 다음과 같이 변하는데, 중간에 발생하는 zero crossing을 **cross-over distortion**이라고 한다.

![|425](https://i.imgur.com/ic2nSdb.png)

이를 없애기 위해서 DC 전압원을 달아 그래프를 움직임으로써 dead zone을 없앨 수 있다. 다음과 같은 세 가지 방법이 있다.

![|400](https://i.imgur.com/wcPvUdw.png)

하지만 실제로는 DC battery를 달 수 없으므로, diode를 연결한 뒤 전류를 공급한다. current source는 current mirror로 대체한다. 

![|350](https://i.imgur.com/a4ZTAQc.png)

## Gain of Push-pull Stage

1. 일단 diode를 short 시킨다. 
2. 두 개의 BJT가 있는 부분을 다음과 같이 생각하자.

![|500](https://i.imgur.com/fZ6VaRm.png)

그러면..

$$g_{m}^{*}=g_{m2}+g_{m3}$$

$$r_{\pi}^{*}=r_{\pi2} / / r_{\pi3}$$

인 BJT로 생각할 수 있다.

3. gain을 계산한다. (평소 gain 구하듯이 하면 된다.)

![|500](https://i.imgur.com/kyyEa9o.png)

*output impedance*는 다음과 같다.

$$R_{out}=\frac{r_{o2}//r_{o4}}{\beta_{*}}+ \frac{1}{g_{m}^{*}}$$

다음은 최종 정리!

![](https://i.imgur.com/8ANZwwV.png)

하지만 위는 ideal한 경우로, 실제로는 small signal이 불가능하다. 따라서 회색 circuit처럼 feedback을 걸어 linearity를 증가시키기도 한다.

# Harmonics

우리는 sin 신호를 보내고 싶지만 실제로는 pulse 신호와 유사한 것을 보내게 된다. 그러면 해당 신호는 frequency domain에서 다음과 같이 표현할 수 있다.

![](https://i.imgur.com/6WS2QFm.png)

pulse 신호는 위 domain과 마찬가지로 여러 frequency에서 신호가 보이게 되는데[](), 이 모임을 **harmonics**라고 한다.
이는 신호를 왜곡시키는ㅔ 요인이며, spectral analyzer로 측정할 수 있다.
이를 줄이기 위해서는 **loop gain**을 낮추는 방밥을 사용할 수 있는데, 이는 Ak를 높임으로써 해결할 수 있다.

![](https://i.imgur.com/FoDIFal.png)

이러면 전체적인 gain도 떨어지지만, harmonics가 줄어드는 속도가 더 커서 괜찮다.

# Power Rating

transistor가 소모하는 power는 다음과 같이 계산할 수 있다. ($P_{av}$의 definiation)

$$
P_{av}= \frac{1}{T}\int_{0}^{T}I_{C}V_{CE}dt
$$

$$I_{C} = I_{1} + \frac{v_{out}}{R_{L}}, \ v_{out} = V_{p}\sin \omega t$$

$$I_{C}= I_{1}+ \frac{V_{p}\sin\omega{t}}{{R_{L}}}$$

아오 귀찮아서 사진으로 찍습니다

![](https://i.imgur.com/QvtopbC.png)

- max의 경우: 모든 power가 transistor에서 소모될 경우 
- min의 경우: 소리에서 절반, transistor에서 절반 소모

### Push-pull Stage Power Rating

![](https://i.imgur.com/hKvlWYQ.png)

하나의 transistor가 소모하는 전압을 측정하기 위해 계산하는 과정, transistor가 두 개이기 때문에 $\frac{T}{2}$를 사용하는 것이다. 편미분을 이용해 max 값을 구한다.

# Efficiency

$$
\mu = \frac{P_{out}}{P_{out}+P_{ckt}}
$$

따라서 circuit에서 1W를 소모하고 1W를 출력하면 efficiency는 1/2이다. 

![](https://i.imgur.com/QvXvu2h.png)

$P_{out}$은 rms로 구한다!

## Push-pull Stage Efficiency

Push-pull stage에서 efficiency는 다음과 같이 구할 수 있다.

![](https://i.imgur.com/rOgCOrL.png)

transistor가 두 개이기 때문에 $2P_{av}$로 구하는 것이다. 