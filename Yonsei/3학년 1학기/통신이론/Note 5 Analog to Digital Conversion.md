> [!note]
> 시험은 다음주에 보고.. 
> 범위는 Note 5 까지s
ㅐ
# Analog to Digital Conversion

Digital data의 장점은 무엇인가
- **noise immunity** : 특정 level로 나눠지므로 세세한 값이 필요없음 -> noise에 강함
- **flexibility in the BW-power trade-off** : 동일한 BW여도 더 많은 데이터를 전송가능.
- **Possibility of applying cryptographic and antijamming techniques** : 디지털 데이터의 symbol에 적용 가능
- **Ease of implementation** : 다양한 chip에 적용 가능 -> device 개발에 이득
이러한 장점을 이용하기 위해서 Analog 신호를 Digital 신호로 변환하고자 한다. 목적은 변환 과정에서 signal distortion을 없애는 것이다.

![](https://i.imgur.com/b9Q0x0S.png)

AD conversion은 다음과 같은 세 가지 단계로 나뉜다.
1. **Sampling** : discrete-time continuous-valued signal로 변환하는 과정
2. **Quantization** : 변환한 신호를 특정 symbol로 변환
3. **Encoding** : 신호를 binary data로 변환, n개의 bit로는 $2^n$가지의 데이터를 표현 가능하다.

## Sampling

Analog signal을 특정 시간 간격으로 나누어 discrete-time이지만 continuous-value를 가지는 analog signal을 만든다. 이 시간 간격을 **sampling time**이라고 한다. 이 역수를 **sampling rate**라고도 부른다.

![|325](https://i.imgur.com/BL1xcYq.png)

### Samping Theorem



## Quantization

Sampling 이후의 signal 값을 특정 값으로 round하는 과정이다. Discrete-time, discrete-amplitude signal이 된다. 

![|320](https://i.imgur.com/ei1qhee.png)

## Encoding

만들어낸 signal을 이용해 Digital data를 뽑아낸다. 


