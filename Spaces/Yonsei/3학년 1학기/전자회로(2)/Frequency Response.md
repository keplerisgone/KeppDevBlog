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

## total frequency response

![|600](https://i.imgur.com/IapLxtv.png)

**Total Frequency response**는 일반 DC gain (lower frequency gain이라고 하신 것 같음)과 zero, pole만 구하면 간단하게 위 수식을 이용해 구할 수 있다. 

![|575](https://i.imgur.com/bMvQ106.png)

![|348](https://i.imgur.com/37vuP3p.png)

또한 경험적으로 R-C의 병렬연결은 $\frac{1}{RC}$의 pole이 생김을 알 수 있다.

# F
# Example

## 11.1

![|600](https://i.imgur.com/cXHJuob.png)

## 11.6

![|425](https://i.imgur.com/W7bepYn.png)

## 몇인지 몰라

![|425](https://i.imgur.com/IsYmxwy.png)

![|450](https://i.imgur.com/g15Qu0j.png)

![|450](https://i.imgur.com/gf32JnS.png)
