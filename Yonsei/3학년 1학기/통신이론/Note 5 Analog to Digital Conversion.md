> [!note]
> 시험은 다음주에 보고.. 
> 범위는 Note 5 까지s
ㅐ

# Analog to Digital Conversion

Digital data의 장점은 무엇인가
- **noise immunity**: 특정 level로 나눠지므로 세세한 값이 필요없음 -> noise에 강함
- **flexibility in the BW-power trade-off**: 동일한 BW여도 더 많은 데이터를 전송가능.
- **Possibility of applying cryptographic and antijamming techniques**: 디지털 데이터의 symbol에 적용 가능
- **Ease of implementation**: 다양한 chip에 적용 가능 -> device 개발에 이득
이러한 장점을 이용하기 위해서 Analog 신호를 Digital 신호로 변환하고자 한다. 목적은 변환 과정에서 signal distortion을 없애는 것이다.

![](https://i.imgur.com/b9Q0x0S.png)

AD conversion은 다음과 같은 세 가지 단계로 나뉜다.
1. **Sampling**: discrete-time continuous-valued signal로 변환하는 과정
2. **Quantization**: 변환한 신호를 특정 symbol로 변환
3. **Encoding**: 신호를 binary data로 변환, n개의 bit로는 $2^n$가지의 데이터를 표현 가능하다.

## Sampling

Analog signal을 특정 시간 간격으로 나누어 discrete-time이지만 continuous-value를 가지는 analog signal을 만든다. 이 시간 간격을 **sampling time**이라고 한다. 이 역수를 **sampling rate**라고도 부른다.

![|325](https://i.imgur.com/BL1xcYq.png)

### Samping Theorem

signal $x_{c}(t)$을 sampling time $T_{S}$로 sampling해보자. 수식으로는 다음과 같이 표현할 수 있다.

$$x_{p}(t) = \sum_\limits{-\infty}^{\infty}x_c(nT_{S})\delta(t-nT_{S})$$

이를 FT하면..

$$X_{p(f)}= \frac{1}{T_{S}}\sum_\limits{-\infty}^{\infty}X_{C}(f-\frac{n}{T_{S}})$$

그래프로는 다음과 같이 나타낼 수 있다.

![|600](https://i.imgur.com/ejMDTfq.png)

이 때, $f_{s}> 2W$여야 LPF를 통과시킬 때 overlap이 생기지 않는다.

![](https://i.imgur.com/eFCnJiq.png)

aliasing이 일어나게 하지 않는 최소한의 sampling rate를 **Nyquist sampling rate**라고 하며, 이 값은 $f_{s} = 2W$이다. 

실제로는 Nyquist sampling rate보다 큰 rate를 사용하며, 남는 rate를 **guard band**라고 부른다. 

![](https://i.imgur.com/7mSq4Wi.png)

## Quantization

Sampling 이후의 signal 값을 특정 값으로 round하는 과정이다. Discrete-time, discrete-amplitude signal이 된다. 

![|320](https://i.imgur.com/ei1qhee.png)

### Scalar Quantization

sampling된 신호의 amplitude를 finite number of levels로 바꾸는 과정이다. 각 sampling을 가장 가까운 value로 rounding 한다. 
이 때 finite number if levels를 **Quantization region** $R_k$ 라고하며, 각각의 값을 **Quantization level**이라고 한다. 변환된 값은 **Quantization version** $\hat{x}_k$라고 한다. 이를 binary로 바꾸는 과정을 **Encoding step**이라고 한다. 

![|400](https://i.imgur.com/XuMEUNi.png)

당연히 Quantization을 진행하면 원래 값과 quantization된 값이 차이가 나게 되는데, 이 차이를 **squared error distortion** $(x-\hat{x})^2$로 나타낼 수 있다. 

$$(x - Q(x))^{2}= \tilde{x}^2$$

이를 Energy(Power) 측면에서 보면 **Average distortion**이 된다.

$$D = E[d(x, \hat{x})] = E(x-Q(x))^2$$

요것과 원래 signal symbol energy의 비는 **SQNR**(Signal to quantization noise ratio)이라고 하며, 이는 디지털 변환의 성능 지표가 된다.

![|600](https://i.imgur.com/ONg0xNy.png)

## Encoding

만들어낸 signal을 이용해 Digital data를 뽑아낸다. 

사용하는 bit의 개수는 $v = \log_2{N}$이다. 여기서 N은 총 level의 개수. 
sampling rate가 $f_s$일 때 **Bit rate**는 $R = vf_s$이다.
Encoding 방식은 다양하게 나눌 수 있다.
- **Natural binary coding**: 우리가 익숙하게 사용하는 방법이다. 
- **Gray Coding**: 수가 1 증가할 때 하나의 bit만 바뀌도록 하는 방법. 아래 표를 참고하자.

![|368](https://i.imgur.com/BqCx8HT.png)

# Waveform Coding

이제 modulation을 진행한 signal을 어떻게 바꿀 것인가? 일반적으로 Digital에서 little distortion은 허용된다. 

## Pulse Code Modulation

![](https://i.imgur.com/afVbVLS.png)

가장 간단한 waveform coding 방식으로, Sampler + Quantizer + Encoder의 section으로 나뉜다.
다음과 같은 가정을 사용한다.
- **Bandlimited waveform with a maximum frequency of W**: 따라서 sampling theorem에 따라 sampling rate는 2W보다 커야 한다.
- **Finite amplitude signal**: finite가 아니면 quantization을 진행할 수 없다.
- **Quantization with a large number of quantization levels N**: 2의 제곱수이므로 큰 값을 가진다.

## Uniform PCM

- Quantizer로 Uniform quantizer를 사용한다. quantization 간격이 동일. ($R_{2}-R_{1} =R_{3}-R_{2}$)
- input samples의 범위는 $[-x_{max},+x_{max}]$, Number if quantization levels는 N
- 각 quantization region은 $\Delta = \frac{2x_{max}}{N}$이다. 
	- 때문에 error의 범위도 $(\frac{-\Delta}{2}, + \frac{\Delta}{2})$이다.

## Nonuniform PCM

![](https://i.imgur.com/hrSVUmq.png)

- quantization region의 크기가 단계마다 다르다. 
- 사람의 목소리같은 경우는 대부분이 낮은 주파수 영역이기에 높은 주파수 영역에서 세세하게 level을 나눌 필요가 없다.
	- 따라서 lower amplitude에서 많은 quantization regions을 가지고, larger amplitudes에서는 quantization region이 상대적으로 적다.

### Companding Technique

nouniform quantization을 하는 방법
1. compressing 사용: 작은 값은 증폭, 큰 값은 줄인다. 
2. 이후 Uniform quantization을 사용 -> 최종적으로는 nonuniform이 됨
3. receiving할 때는 반대의 과정을 진행해 원래 signal을 복원한다

**$\mu$-law**는 북아메리카에서 사용하는 방법이다. 신호를 압축하기 위해 로그를 사용한다. 가장 자주 사용하는 $\mu$ 값은 255.

![|210](https://i.imgur.com/v8UYRdq.png)

![|475](https://i.imgur.com/C9OQEjZ.png)

**A-law**는 유럽에서 사용하는 방법으로, 분절적 선형 함수를 사용한다. $A=87.6$을 가장 자주 사용한다.

![|191](https://i.imgur.com/PLyJsSc.png)

![|230](https://i.imgur.com/VS81Wzo.png)

## Differential Pulse Code Modulation

![](https://i.imgur.com/F3lYEAT.png)

- 신호를 PCM과 다르게 현재 sample과 이전 sample의 차이를 이용하여 modulation을 진행
	- *previous samples give some information about the next sample*
- 이전 정보를 이용해서 정확도를 향상시킬 수 있다.
- 낮은 비트율로도 높은 정확도를 얻을 수 있다.
- decoder에서는 차이 신호를 더해 sample을 복원한다.

## Delta Modulation

![](https://i.imgur.com/VuO3Hce.png)

- 가장 심플한 DPCM 방식 
- 0에서 시작, sample보다 작으면 Delta를 더하고 크면 Delta를 뺀다.

![|292](https://i.imgur.com/TjIsdNR.png)
- **Large $\Delta$** : 신호가 변할 때는 잘 잡아내지만, 신호가 일정할 때는 varying이 너무 심하다 -> **Granular noise**
- **Small $\Delta$** : 신호가 일정할 때는 괜찮지만, 신호가 변할 때는 변화를 잡아내기가 힘듦 -> **Slope overload distortion**
- **Adaptive $\Delta$** : 그래서 input의 차이를 이용해 $\Delta$를 adjust한다.