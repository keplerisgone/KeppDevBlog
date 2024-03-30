# 집적 회로의 문제점
![](https://i.imgur.com/AEtinLD.png)

- PCB를 설계하면 저렇게 외부 GND와 연결될 수 밖에 없는데, 여기 있는 금속 wire가 inductor의 역할을 해 magnetic flux가 생기게 된다
- 이러면 noise가 발생해
![](https://i.imgur.com/UinTEP0.png)
- 또한 내부 회로에서 GND를 공유하면 서로의 noise가 타고 들어가 부작용이 커진다
- GND의 분리가 필요하다
- 이는 PCB의 공정으로 해결하거나 회로적으로 해결할 수 있다
- 회로적으로 해결하는 방법이 바로 Differential Amplifier
# Differential Signal

![](https://i.imgur.com/iDYUfxJ.png)
- 트랜스포머에 신호를 통과시키면 두 개의 위상이 다른 신호가 나오는데, 이를 **Differential signal**이라 한다. 
- 이 신호를 **Differential Amplifier**에 통과시키면 두 신호가 각각 증폭된다.
- 이걸 다시 transformer로 합쳐주면 큰 시그널 완성~
- 장점은 "시그널을 반만 들고 다녀도 된다" "증폭되는 과정에서 노이즈가 사라진다"

![](https://i.imgur.com/TGemteV.png)
- 하지만 노이즈가 생긴다면? (빨간색)
- 노이즈는 양쪽 differential signal에 동일한 형태로 타기 때문에 **common mode signal**이라고 불린다.
- 보면 알겠지만 amplifier를 통과하는 과정에서 common mode는 사라진다
- single end의 경우 노이즈 또한 증폭될 것
	- 또한 신호의 방사가 GND를 찾을 때까지 이루어지기 때문에 고통스럽다
