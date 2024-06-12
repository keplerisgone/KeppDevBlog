# Digital Transmission Via Carrier Modulation

![](https://i.imgur.com/GCgwntk.png)

- 아날로그 신호를 보내듯이 디지털도 carrier를 통해서 보낸다.
- 여기서도 carrier는 $\cos$이다.
# Amplitude Shift keying

![](https://i.imgur.com/aP1GKoL.png)
- 보내는 signal $s_{m}(t)$는 amplitude와 transmitted signal을 곱한 것이다. 
- amplitude의 값에 따라 value가 달라진다. 주로 distance로 나눈다.
- carrier로는 $\cos{2\pi f_{c}t}$를 곱한다. FT하면 오른쪽과 같은 파형이 만들어진다.
- $g_{T}(t)$는 amplitude로 $\sqrt{\frac{2}{T}}$를 가진다. 이는 마지막에 amplitude를 1로 만들기 위함이다. 
- 
![](https://i.imgur.com/ca6Jzgf.png)
- **bandpass**의 경우 mathced filter이므로 signal의 모양과 똑같은 파형을 집어넣는다.
- matched filter의 power는 저래 돼서 단위벡터가 된다. 
	- 이는 amplifier를 비교하는데 쓰인다.
- **Demodulation**은 analog와 마찬가지로 carrier를 곱해서 이루어진다.
	- amplitude와 noise가 남는데, 이 값을 이용해서 symbol을 결정한다.

![](https://i.imgur.com/gVOcuJG.png)

- noise를 생각하기 전에... Matched filter는 cos이 곱해져서 FT 형태가 저렇게 나온다.
- noise의 분산(=power density function 적분)은 저렇게 나온다.
- Error probability는 다음과 같이 구한다. 
	- 저거는 7장에서 증명했으니 패스.
- amplitude는 보통 하나의 축으로만 이루어져 있지만, 이를 두 개 겹치면 제곱으로 표현이 가능하다.
# Phase Shift Keying

![](https://i.imgur.com/6HFBdQT.png)

- phase는 $2\pi$를 자기네들끼리 나누어 가지는 방식이다.
- phase shift는 실제 time domain에서 밀리는 방식으로 이루어지기에 전의 orthogonal과 비슷하다고 볼 수 있다.

![](https://i.imgur.com/dSJqS4b.png)


![](https://i.imgur.com/4k5PB8m.png)

- modulation 진행시 cos 내부에 phase shift가 발생한다. 
- amplitude는 1(E?)를 맞추기 위해 저렇게 설정되었다.
- $g_{T}(t)$는 위에서 정했으니까..
- 위 signal을 풀면 저래 되는데 $\cos$, $\sin$을 각각 하나의 축으로 생각하면 phase를 결정할 수 있다.

![](https://i.imgur.com/KjwUfR2.png)

- **Demodultaion**을 생각하기 전에 noise를 생각하자.
- addtive noise의 두 component를 다시 생각해보자. 걍 외울까?

# Quadrature Phase Shift Keying (QPSK)

![](https://i.imgur.com/qT1kLQi.png)

- 요것은 4개의 level로 나눈 PSK입니다.

![](https://i.imgur.com/NJgoEiv.png)

- 다시 말하지만 phase shift가 일어나는 건 time domain에서 delay가 일어나는 것으로 바뀐다.

![](https://i.imgur.com/TveaPOL.png)

- transmitter와 receiver는 다음과 같이 표현할 수 있다. level이 몇 개여도 cos, sin 축 두개의 decision만 필요하다.

![](https://i.imgur.com/MzdgaK1.png)

- Error를 판단하는 방법은.. 
- 두 개의 축이기 때문에 signal도 두개도 나뉘어요
- 두 개의 receiver는 각각의 축을 받는다. Energy의 총합은 같기 때문에 BPSK에서 E인 것이 여기서는 E/2이다.

![](https://i.imgur.com/tvC2mG0.png)

- Error probability! : 두 개의 path를 지니므로 average를 계산해야 한다. 외울까?
- 식은 제공해주신다고 한다.

![](https://i.imgur.com/lwMQXP8.png)

- path가 두 개이므로 확률은 두 배, bit가 두 개이므로 bit energy는 2배이다.

![](https://i.imgur.com/atyUUcx.png)
- **detector**의 핵심은 받은 signal의 phase를 tan 역함수로 알아내는 것. 위에서는 두 개의 receive를 쓸 수도 있지만...
- symbol이 늘 수록 error 확률은 올라간다. 같은 공간을 나눠먹는 것이기 때문!

![](https://i.imgur.com/j93BUdj.png)

- 요고는 example이다.

# Quadrature Amplitude Modulation

![](https://i.imgur.com/TlPwEor.png)

- 두 개의 carrier (cos, sin)을 이용해 두 개의 축을 만든 ASK이다. 
- 정확히는 크기(amplitude), 위상 (phase)를 동시에 이용하는 것이다. 

![](https://i.imgur.com/kZrsZDa.png)

- rectangular를 이용하거나 circular 모양을 이용한다.

![](https://i.imgur.com/LMDVxA0.png)

- 요것도 똑같다. received signal은 noise도 받고 두 개로 나뉘어진다.

![](https://i.imgur.com/65DJ5rA.png)

- error probability. M-ary의 경우와 같다. 수식에 때려넣은 것과 같다.

![](https://i.imgur.com/nXnH0V8.png)

- 두 개의 축을(orthogonal한) 이용하는 것이기 때문에 4-PAM, 16-QAM은 error 확률이 같다.

# Frequency Shift keying

![](https://i.imgur.com/dQq8wVZ.png)

- OFDM의 기초가 되어서 알아보는 것이지, 시험에는 좀?
- 