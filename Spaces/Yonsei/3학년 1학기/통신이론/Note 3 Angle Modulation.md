

![400](https://i.imgur.com/1GFyKge.png)

→ Modulation 의 분류
# Angle Modulation

![](https://i.imgur.com/krrvqKw.png)

* FM: $f_c$ 를 이용하는 시스템
* PM: $\phi$ 를 이용하는 시스템 , FM >> PM (음질이) WHY?: BW 이 다섯 배는 늘어나기 때문
* properties
* nonlinear 이기 때문에 근사 방법 이용
* BW 이 무한대면 좋겠지만 그럴 수 없으므로 Effective BW를 정의한다
* noise 에 강하다 ⇒ 음악 관련 방송에 사용한다
* envelope 은 일정하다
* carrier wave의 형태
![300](https://i.imgur.com/mMzRSFd.png)

## Basic Definition

![](https://i.imgur.com/t6zEmAQ.png)

- phase angle 이란 그냥 삼각함수에서의 위상 각도 $\theta$를 의미한다. Angular rate 는 시간에 따라 달라질 수 있는 값으로, 헤르츠 주파수의 평균값이 된다. 
☆ Frequency = Angle 의 미분
☆ phase - 주파수의 적분 ← 여기가 싹다 이해가 안가는

# Angle Modulation - conti.
![](https://i.imgur.com/an6cKhj.png)

* PM: Phase 부분에 message 를 넣는 것
* FM: frequency 부분에 message 를 넣는 것
	⇒ 모두 미분- 적분 관계로 정의된다. 이해가 안가면 위의 Basic을 다시 읽어보고 올 것

# Representation of FM and PM Signals
![](https://i.imgur.com/S7oSPFX.png)

- PM: 위상이 $m(t)$에 비례해서 변화한다 ⇒ $\phi(t) = k_{p}m(t)$
	- $m(t)$는 메세지 신호,
	- $k_{p}$는 phase deviation constant
- FM: 주파수가 메세지에 비례 (미분 관계여도 괜찮은 건가)
	- 메세지 신호가 phase에 숨겨져있다 왜그러지

![](https://i.imgur.com/Ez7aTip.png)

* 메세지 적분후 PM을 할 경우 FM
* 메세지 미분후 FM을 할 경우 PM

![](https://i.imgur.com/64MJB3X.png)

* FM: $m(t)$ 의 크기에 따라 주파수가 비례
* PM: $m(t)$ 의 미분값의 크기에 따라 주파수가 비례
	→ 헷갈릴 수 있지만 당연함. 주파수임.
	→ 오른쪽은 왜 위상이 바뀌는가

# Demodulation of FM and PM signals

![](https://i.imgur.com/VSocspZ.png)

* FM: Instantaneous freq 를 알아내는 것
	* 이를 알아내야 위의 $f_{i(t)}- f_{c} = k_{f}m(t)$를 알아낼 수 있음
* PM: phase 값을 알아내는 것
	* $\phi(t) = k_{p}m(t)$이므로...
	* 근데 사실 둘 다 말장난이긴 하다
* **Modulation index**: 전체 주파수의 최대 변화 비율 (Maximum frequency deviation)
	* $\beta_{f}= {k_{f}max[|m(t)|]\over W} = {\Delta f_{max} \over W}$
	* PM일 경우에는 잘 구해라
		↳ 좋은 정도를 결정하는 parameter → BW의 넓이를 결정하는 param이기 때문 -> 밑의 슬라이드 참고!
## example

![](https://i.imgur.com/oUHLK7i.png)

→ 예제에서의 message signal 은 미분/적분 시 형태가 유지되므로 PM/FM 구분이 어렵다

# Spectral Characteristics of Angle

![](https://i.imgur.com/9ypG1dF.png)

* nonlinear 하다 → 해석이 매우 힘들다
* sine signal 을 이용해 모두 approximation 한 뒤 일반화시켜 버린다

# Angle Modulation by a Sinusoidal signal

![](https://i.imgur.com/wHJYjTj.png)

![](https://i.imgur.com/XUHmkuN.png)

* 핵심은 일반적인 sinusoidal signal을 이용해 특징을 알아보는 것
* 오일러 공식을 이용해도 된다.
* 주기 함수이기 때문에 Fourier-series 로 나타낼 수 있다는 점이 핵심
	* 무한대로 더해지는 급수지만 이를 적당히 제한해야 함 => effective BW
* 결국 Bessel 함수로 표현되는구나 ~ ⇒ 근데 왜 Series 로 등가시키는겨 무한대로 가는데.. → β 로 제한가능
* 어쨌든 Bessel 을 대입시켜서 전개시켰더니 주파수 스펙트럼을 구할 수 있구나
* β 값에 따라 사용하는 BW의 길이가 달라질 수 있다

![](https://i.imgur.com/SFESTAT.png)

- 사용하는 $\beta$, n 값에 따라 정확도, BW가 달라짐
## Bessel function

![](https://i.imgur.com/93mOhL8.png)

* n 이 짝수일 경우 대칭
* n 이 홀수일 경우 원점 대칭

## example

![](https://i.imgur.com/TC307Fu.png)

![](https://i.imgur.com/zd7mbY6.png)

![](https://i.imgur.com/PgGqo0I.png)

## effective bandwidth
![](https://i.imgur.com/PH7A3sM.png)

- 98% 이상의 정확도를 보장하는 BW를 쓰려면 위의 공식을 이용
- PM, FM 마다 베타의 값이 다르므로 대입해서 쓰시길

![](https://i.imgur.com/hbUGXOB.png)

- message 의 크기가 증가한다면? → BW가 증가한다
* message 의 BW 자체가 증가한다면? → PM는 심각하게 증가, FM은 적절하게 증가
	⇒ PM이 BW를 더 많이 잡아먹는다

![](https://i.imgur.com/jjvntTb.png)

- a가 증가하면 harmonic 의 수가 증가
- $f_{m}$ 가 증가하면 PM은 고정, FM은 harmonic 의 수가 감소 ⇒ 모두 harmonic 사이의 간격이 늘어나는 것

[]

- PM signal의 주파수가 증가하면
	- BW가 증가
	- Harmonic의 수는 그대로

# Angle Modulation by an Arbitrary Message Signal

[]
- 위와 같은 특징을 일반화 (sinusoidal -> general)
- **Carson's Rule** : modulated signal의 BW는 $2(\beta + 1)W$이다.
	- $\beta$는 Modulation index
	- $W$는 message signal의 BW이다
- **Wideband FM** : $\beta$가 5이상이면...
- Angle modulated signal의 BW는 SSB, DSB에 따라 달라짐
	- SSB의 경우는 $B_{c} = (\beta + 1)W$일수도 있음
	- AM은 보통 Amplitude modulation을 의미하는것... angle이 아니다
## example
[]

# Demodulation of FM Signals
[]
- 수학적으로 개념만 이해해보자
- FM 신호를 미분하면 AM signal이 나온다
	- 왜 $j2\pi f$인가? -> FT에서 미분을 하면 $j\omega$가 곱해지기 때문
	- 아무튼 FT를 진행해 주파수 도메인에서 생각한 다음, BPF를 통해 AM만 빼낼 예정
	- 전달 함수...
- 이를 AM demodulation을 진행하면 됨