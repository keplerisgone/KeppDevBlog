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



## Encoding

만들어낸 signal을 이용해 Digital data를 뽑아낸다. 


