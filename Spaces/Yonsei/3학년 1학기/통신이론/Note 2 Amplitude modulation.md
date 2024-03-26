# Amplitude Modulation

![](https://i.imgur.com/wpReNih.png)
- **analog signal** - continuous한 신호를 보냄
    그렇다고 digital이 non continuous인 건 아님  (애초에 현실에서 완벽한 non-continuous를 만들 수 있나?)
    digital은 그냥 level이 존재함 - digital도 analog 신호가 일정 레벨을 가지도록 변형된 것
- bandwidth를 유지하는 것이 중요하기 때문에 따로 변형을 가하지 x
- 보내는 정보에 따라 bandwidth가 다름
	- 말하는 것은 4kHz까지, 음악과 같은 경우는 20kHz
	- 티비에서 송수신하는 비디오의 경우는 6MHz 정도의 BW를 가짐

![](https://i.imgur.com/zMYEyEd.png)
- analog signal은 carrier modulation에 의해 전달됨
- analog를 전해주는 신호 = carrier wave
- 왜 사인함수인가 : 진동을 보기 좋아서
	-> rectangular 함수를 써도 됨
- 뭐든 지 level을 적당히 정해야 효율적임
    예를 들어 phase는 360도까지만 존재하므로, 이상의 값이 필요없음 -> 자원 낭비다
- carrier에는 정보가 담기는데...
	이 정보는 A, P, F 중에 하나에 담김
	각 종류마다 modulation이 있음
	이중 Amplitude를 사용하는 modulation이 바로 AM이다
- 이런 modulation을 진행하는 게 바로 modem 부품
+ demodulation도 진행
# Introduction to Modulation
![](https://i.imgur.com/6zkWZXu.png)
- m(t)
    메세지를 담은 signal
    analog
    baseband = 중심이 0이라는 뜻
    bandwidth가 W **가장 중요한 것은 BW는 양수 부분만 한정이라는 것이다!!**
    modulating (당하는)
- c(t)
    그냥 코사인 함수
    carrier
- u(t)
    Passband = 밴드의 중심이 $f_c$
    Modulated (당한)
    transmitted = 전달되는

![](https://i.imgur.com/V1gUnhZ.png)
- 왼쪽 위와 같은 message signal $m(t)$를 AM 시켜보자
- 단순히 carrier signal과 곱해버리면 된다
- 이를 이용하면 phase 정보로 봤을 때 $f_c$ 부분에서 생긴 것을 알 수 있음
	- 이 때 원본 message의 BW는 0~W이고, AM 진행 후에는 $f_{c}- W \~ f_{c}+ W$로  두배가 되었음을 알 수 있다

![](https://i.imgur.com/fhsUc6O.png)
- 여기도 마찬가지...

![](https://i.imgur.com/Zyk3is7.png)
- sinc 함수를 Modulation하면 다음과 같이 된다
- 역시나 BW가 두배로 늘어난 모습
- sinc 함수를 FT했을 때 왜 rect이 안나오고 저런 모양이 나오냐면 Gibbs Phenomenan때문이다
# Objectives of Modulation

![](https://i.imgur.com/7qGoUpR.png)

- AM을 왜 하는가?
**1. 채널의 주파수 대역을 맞추기 위해서**
**2. transmitter를 맞추기 위해서**
    - 안테나의 크기는 신호의 반파장이어야 하는데,
    - 주파수를 크게 하면 파장이 줄어든다 -> 안테나 만드는 값 아끼기

![](https://i.imgur.com/wJ01s7J.png)
**3. Frequency-division**
- 주파수가 높을 수록 더 많이 frequency-division이 가능
- 더 많은 사람들이 이용할 수 있게 한다

**4. 노이즈에 강해진다**
	근데 AM만 이게 해당이 안 됨 - AM은 애초에 BW에 따라 power가 달라지거나 하지 않음
	PM,FM의 경우는 bandwidth를 5배로 늘리는 경우만 해당
아무튼 takeoff가 있다~
## example

![](https://i.imgur.com/KGjQHdI.png)
# Amplitude Modulation (AM)

![](https://i.imgur.com/AjSFKQj.png)
- AM의 종류는 다음과 같다.
- 물론 AM을 시행하는 방법, 즉 스펙트럼이 어떻게 되가냐의 차이지 analog, digital의 차이는 아니다.
- DSB-SC AM (double sideband - Suppressed-Carrier AM)
	- 원래 y축에 의해서 쪼개져 있던게 나와서 bandwidth가 두배가 됨
	- cos이 사라져요.. (물론 주파수 대역에서)
- DSB-LC AM
	- carrier(cos)이 살아있어요
	- 간섭을 억제할 수 있음

SSB AM
- 신호의 절반만 보내요

VSB AM
- SSB가 현실적인 건 아니니까
신호의 60%만 보내요

위 모두 analog, digital 상관없이 스펙트럼에 관한 이야기
# Demodulation of SSB-AM Signals
![](https://i.imgur.com/KUB95Kh.png)

↳ LSB 만 있어도 가능
쓰기가 너무 어렵다 - 완벽한 LSB를 만들기도 어렵고 이를 복원하는 것도 쉽지 않음
애초에 가장 큰 문제는 완벽한 필터를 만들 수가 없다는 것임!!

# Vestigial-Sideband AM (VSB-AM)

![](https://i.imgur.com/RF4CvLD.png)

추가적으로 절반에서 조금 신호를 더 보낸다, BW가 조금 더 늘어난다.
low-freq 에서 효과적인 방법. ⇒ TV 방송에서 주로 쓰인다
완벽한 BPF를 완화시켜 적당히 걸러내는 방법

![](https://i.imgur.com/1Pjr7ow.png)
![](https://i.imgur.com/FkDQo7P.png)
![](https://i.imgur.com/zlcupys.png)
![](https://i.imgur.com/5gabT8J.png)

실제로는 위와 같이 곡선이 아닌 선형으로 필터를 설계하는 편. 다만 감쇄되는 부분이 0 부근(DC 성분)에서 상쇄되도록 해야함.
핵심은 가운데를 flat 하게 만든 완화된 필터 → 필터가 감쇄된 만큼 신호가 더해진다

## VSB - AM : example
![](https://i.imgur.com/xQ1klFT.png)

# Signal Multiplexing

![](https://i.imgur.com/KLeRcvL.png)

동시에 여러 사용자에게 신호를 전달
**Frequency**-**Division** **Multiplexing** : 받은 신호를 여러 주파수로 변환, 핵심은 적절한 BW를 사용해 효율적으로 이용하는것, 간섭이 없어야 함
정확히는 여러 개의 신호를 주파수를 달리 한 뒤 뭉쳐서 한 번에 보내는 것
	더더 정확히는 다음 그림처럼 기지국마다 할당된 주파수대로 신호를 보내는데, 이를 통째로 변환시켜 보내고자하는 채널로 변환시키는 것
![400](https://i.imgur.com/f7cy8GT.png)

![](https://i.imgur.com/OiBoF65.png)

**Time-division multiplexing** : 위와 같이 frequency가 아닌 time을 기준으로 나누는 경우도 존재. 이는 매우 작은 시간 간격마다 신호를 바꾸어 여러 개의 신호를 동시에 보내는 것

# AM-Radio Broadcasting
![](https://i.imgur.com/dd4P1YI.png)

그냥 읽어보자.

# Summary

![](https://i.imgur.com/AnX20JY.png)

→ DSB-SC → DSB- LC → SSB-AM → VSB AM
* 각각의 signal 에 무슨 문제가 있었는가?
* 앞의 두 개는 신호에 관련, 뒤의 두 개는 BW에 관련된 것
* 직교 신호는 서로에게 간섭을 주지 않는다 → 두 신호를 완전히 동시에 보내는 게 가능
	* 결국 통신 속도의 발전은 직교 축의 발견이 된다 (Quadrature-Carrier)