# Frequency

![|550](https://i.imgur.com/qIZYlcA.png)

회로를 분석할 때 Frequency로 분석하는 이유는 일반 time 축에서 볼 때는 복잡한 주기 신호인 것을 단순하게 표현할 수 있다. 

![|425](https://i.imgur.com/WwTaGfT.png)

또한 미분 방정식으로 나타나는 RLC 회로를 linear한 Impedance로 나타낼 수 있다. 이게 가장 큰 이유일듯

# Frequency Response

![|600](https://i.imgur.com/uglRgJh.png)

Frequency response를 분석할 때 gain은 일반적인 KCL이나 KVL로 구할 수 있다. 이 때 voltage gain이 -3dB를 가지는 곳을 **cutoff frequency**라고 하는데, 이 때 이후로 20dB/dec를 가지면 **zero**, -20dB/dec를 가지면 **pole**이라고 한다. 간단하게 분모에서 나타나면 pole, 분자에서 나타나면 zero가 된다.
근데 교수님은 또 저 때 $R = \frac{1}{sC}$가 될 때가 pole이라고 설명하셨네

![|302](https://i.imgur.com/Umgq7Ej.png)

![|400](https://i.imgur.com/jlYXnre.png)

**Bode plot**은 이런 gain을 $\omega$에 따른 그래프로 나타낸 것이다. (물론 dB scale) 실제 gain그래프는 보기 복잡하니까 그냥 zero와 pole에 따라 approximation해서 그린다.

## Total Frequency Response

![|600](https://i.imgur.com/IapLxtv.png)

**Total Frequency response**는 일반 DC gain (lower frequency gain이라고 하신 것 같음)과 zero, pole만 구하면 간단하게 위 수식을 이용해 구할 수 있다. 

![|575](https://i.imgur.com/bMvQ106.png)

![|348](https://i.imgur.com/37vuP3p.png)

또한 경험적으로 R-C의 병렬연결은 $\frac{1}{RC}$의 pole이 생김을 알 수 있다.

# Floating Capacitor

![|600](https://i.imgur.com/8ivBTwt.png)

하지만 위와 같은 회로에서 Capacitor가 ground에 연결되어 있지 않다면 곤란해진다. 이를 붕 떠있는 capacitor라 해서 **floating capacitor**라고 한다. 이는 Ground Capacitor로 approximation해서 회로를 분석할 수 있다. 사용할 수 있는 방법은 다음과 같다.
- **KCL & KVL을 푼다**: 가장 원초적인 방법이다. 이는 **dominant pole approximation**을 이용해 다시 한 번 간단히 할 수 있다. 
- **Miller Approximation**: Miller capacitance를 없애는 방법으로, MOSFET에 구성된 capacitor를 grounded capacitor로 바꾼다. 오차가 제일 크다.
- **MATLAB**으로 푼다: 원초적인 방법. 하지만 배우는 게 없다.

![|625](https://i.imgur.com/bbdRATS.png)

가장 유명한 Floating capacitor는 MOSFET에 달려있는 **gate-source capacitance**($C_{gs}$)이다. 이는 회로의 Bandwidth를 낮추는데, 이를 **Miller effect**라고 한다.

# Miller Theorem

![|425](https://i.imgur.com/THy8jXj.png)

![|450](https://i.imgur.com/qF2HDaf.png)

**Miller theorem**은 위의 floating capacitor를 위와 같이 grounded capacitor로 바꾸는 정리이다. 이를 증명하기 위해서는  모두 일정한 gain을 가진다는 approximation이 필요하다. 

![|625](https://i.imgur.com/oPiZ6Xw.png)

따라서 Grounded cap으로 전환된 친구들은 다음과 같이 계산이 가능하다. 

![|550](https://i.imgur.com/X1XWmN7.png)

위 수식을 통해서 Miller theorem을 사용했을 경우 $C_1$이 gain만큼 증가해 pole ($\frac{1}{RC}$)이 감소하게 되어 bandwidth가 줄어드는 것을 알 수 있다. 대충 Miller theorem이 나쁜 이유.

![|600](https://i.imgur.com/ulwzGUv.png)

왜 그래야하는 걸까... DC blocking capacitor는 MOSFET의 saturation을 막기 위해서라는데...
작은 capacitor는 고주파 영역으로 갈수록 존재감을 드러낸다. 저주파에서는 impedance가 무한대라 open로 봐도 되잖아. 하지만 고주파수 영역에서는 회로를 short시킨다. 아래 그래프로 확인.

![|450](https://i.imgur.com/JRzfXbc.png)

이를 direct analysis로 풀어보자.

![|575](https://i.imgur.com/ClYsvj2.png)

![|600](https://i.imgur.com/EpKLS6r.png)

하지만 계산된 pole이 너무 더럽다!
## Parasitic capacitance

![|500](https://i.imgur.com/oCqaK2h.png)

기생.. 하는 capacitance를 의미한다. 회로 사이에 무조건적으로 존재하게 되는 capacitance를 말한다. MOSFET에서는 각 gate, source, channel 사이에 있는 간극 때문에 capacitance가 존재할 수밖에 없다. 

# Dominant approximation 

![|600](https://i.imgur.com/UqwopRv.png)
 
KCL로 만들어진 무자비한 수식을 간단하게 표현하는 방식이다. 꼭 오른쪽과 같이 pole의 차이가 심각하다는 가정을 해야 한다. 하지만 두 개의 pole과 하나의 zero를 찾는 만큼 한계가 존재하는 편.

![](https://i.imgur.com/QIlqptE.png)

더 높은 order도 표현할 수 있다는데 교재에 안나와있어서 잘 몰?루

## CB & CG Stage

![|450](https://i.imgur.com/LL9PRC5.png)

별 다를 거 없다.
## Source follower

![|275](https://i.imgur.com/QSbAN6q.png)

![|575](https://i.imgur.com/aVDPkKm.png)

잘 계산하라는 말밖에는 해줄말이 없다
Source follower는 원래 gain이 1에 가깝지만 output impedance를 줄이는 buffer의 역할을 했다. 이는 아래처럼 input impedance를 측정함으로써 얻을 수 있다. 아무튼 bandwidth의 영향을 덜 받는다. C가 줄어드니깐...

![|575](https://i.imgur.com/HIEx4lL.png)

output impedance도?

![](https://i.imgur.com/xgCsTuI.png)

저주파에서는 죽고 고주파수에서는 사는게 완전 inductor이다. 따라서 이 회로를 **active inductor**라고도 한다. 참고로 위에서 output impedance를 구하는 방법은 일반적인 MOSFET과 같이 *끌어내리는* 방법을 쓴다. 이해했지?

## Cascode Frequency response

![](https://i.imgur.com/Jkf45ZJ.png)

cascode는 impedance를 높이기 위해서도 쓰지만, Miller cap을 해결하기 위해서도 사용한다. 
계산은 복잡하니까 알아서 해라.
# Example

## 11.1

![|600](https://i.imgur.com/cXHJuob.png)

## 11.6

![|425](https://i.imgur.com/W7bepYn.png)

## 11.9

![|600](https://i.imgur.com/Qi3cehv.png)

## 11.14

![|600](https://i.imgur.com/Emids0a.png)

## 11.16

![|600](https://i.imgur.com/k8yGvw0.png)

## 11.18

![|600](https://i.imgur.com/P47BJtQ.png)

## 11.19

![|525](https://i.imgur.com/fmCmr3r.png)

## 몇인지 몰라

![|425](https://i.imgur.com/IsYmxwy.png)

![|450](https://i.imgur.com/g15Qu0j.png)

![|450](https://i.imgur.com/gf32JnS.png)

![](https://i.imgur.com/1y9gFPC.png)

![](https://i.imgur.com/nmctRje.png)
