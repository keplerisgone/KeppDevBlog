
![](https://i.imgur.com/WdpNbjs.png)

- 통신은 "의미있는 정보"를 어떤 방식으로든 넘기는 것
- CD도 통신이고 팩스도 통신이고 트랜지스터도 통신임
- 유선과 무선의 방식이 있는데, 무슨 경우든 RX와 TX 사이의 모든 것을 "채널"이라고 함!!!!
* 채널의 기원이 그렇다
    방송국에서 '특정 주파수를 쏴주는 것'에서 
    특정 주파수를 채널이라고 하는 것

![](https://i.imgur.com/kKWe4qs.png)
- 1G : 이 때는 무식하게 다 크던 시절
- 2G : 
    유럽은 GSM,
    미국은 USDC - 계속 쓸거임
    우리나라는 독자적인 IS-95 쓰던 시절
    디지털화 되던 시절
    우리나라는 산지가 너무 많아서 통신이 안될거라 했는데
    여차저차 잘 됐다
- 4G : 
    유럽이랑 일본이랑 합작해서 단일화 시키려고 하던때
    사실 데이터 통신의 시작은 화상통화였다
    Upload Link(UL)과 Download Link(DL) 존재
    당연히 DL은 짱짱 세요 (나눠져서 세야함)

![](https://i.imgur.com/wl3Qk6w.png)


![](https://i.imgur.com/lZf2HMl.png)

![](https://i.imgur.com/ScXLqHf.png)
- 사실 뭘 통신하던지 "전용 통신망" 이 빠르고 좋다
- 정보의 흐름은 
	info - transmitter - channel - receiver - output이 되는데
	우리는 info -> TX의 과정을 배운다
	- 데이터가 캐리어에 담기는 과정

![](https://i.imgur.com/XbjcAtY.png)

![](https://i.imgur.com/2hRssjs.png)


![](https://i.imgur.com/LIe5zB4.png)
- Modulation : tranmitter가 신호의 주파수를 맞추는 과정
    대부분 '주파수를 맞추는 과정'
    신호를 2.1GHz 같이 맞춘다
- 이를 이용해 여러 사용자에게 신호를 보낼 수 있음

![](https://i.imgur.com/dVwCllz.png)
- Receiver의 주 역할은 "받은 신호를 표현하는 것"
- Carrier demodulation을 진행
- 노이즈를 줄이는 역할도 수행

![](https://i.imgur.com/ZVJZJUk.png)
- 아날로그와 디지털의 차이점
- 결국 내가 무슨 신호를 보내는지에 따라 결정됨
	- 디지털도 따지고 보면 아날로그 신호를 인코딩해서 보내는 거임

![](https://i.imgur.com/5oDxvQe.png)
- 채널은 TX와 RX 사이에 존재하는 모든 것을 의미함. 무선 통신같은 경우는 공기가 된다
- 채널은 다양한 환경 조건에 의해서 노이즈가 발생한다.
- 통신 기술의 발달은 바로 *채널을 어떻게 잘 이용했는가*가 중점이 된다

![](https://i.imgur.com/QUFYFdQ.png)
- **잡음과 간섭의 차이**는 무엇인가?
- **잡음** : 어쩔 수 없이 발생,
    그냥 존재... - *signal distortion*
- **간섭** : 어디서 발생하는 지 예상 가능, - *thermal noise*
    경우에 따라 없앨 수 있음
    네 가지 종류 존재
    man-made : 자동차
    atmosphere : 자연에 의한 대기이상
    interference : 다른 이용자
    multipath : 다른 곳에서 반사된 신호

![](https://i.imgur.com/b9vE5oq.png)
- 물리적 채널은 다양한 종류가 존재

![](https://i.imgur.com/KNxjt5L.png)
- 채널의 성능을 결정하는 핵심적인 요소는 바로 **Power**와 **Bandwidth**
	- **Power** : 신호의 세기를 결정, 이게 높으면 노이즈의 영향을 잘 안 받기도 함. 다만 다양한 곳에서 power가 제한되는 경우가 많음...
	- **Bandwidth** : 신호를 보내기 위해서 사용하는 주파수 대역의 제한..? 이게 넓을 수록 한번에 더 많은 데이터를 보낼 수 있다 (modulation을 통해 여러 대역의 주파수로 동시에 보내면 되기 때문)
- 둘 모두 국제적인 제약이 존재

![](https://i.imgur.com/Uzcr61O.png)
- 통신 시스템을 설계할 때는 Bandwidth를 높게하면 노이즈를 줄일 수 있지만, 이걸 높이면 다른 통신과의 간섭이 발생하거나 유지 보수 비용이 높게 들거나 오히려 통신을 복잡하게 할 수 있기 때문에 둘 사이에서 잘 조절해야 한다.