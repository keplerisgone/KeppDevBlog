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
- amplitude는 1(E?)를 맞추기 위해 