![[Note 2 Amplitude modulation 2024-03-13 22.10.18.excalidraw|100]]

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