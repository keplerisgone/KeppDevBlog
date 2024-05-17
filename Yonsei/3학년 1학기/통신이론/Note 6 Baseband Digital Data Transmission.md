
이전에 배운 것
- Carrier modulation : carrier의 성분을 이용해 message를 전송
	- **Amplitude**
	- **Frequency**
	- **Phase**
- Demodulation : carrier-modulated signal에서 message 성분만 빼낸다. carrier signal과 convolution으로 이루어짐
- **Signal-to-Noise Ratio** : noise를 얼마나 잘 잡아내는지 성능 지표

![](https://i.imgur.com/gxmlYtk.png)

Digital modulation은 **Shift Keying**으로 나뉘어진다.

# Digital Transmission in an AWGN Channel

**BER**(Bit error rate)는 디지털에서 SNR보다 자주 사용하는 성능 지표이다.
가장 널리 사용되는 정의는 **Average bit error rate**이다. 전체 길이 N에서 error가 난 bit의 수 n의 비율로 정해진다.
$$\text{BER} = \lim_\limits{N\to \infty} (\frac{n}{N})$$
**Packet error rate**(PER)는 각 분야에서 인정되는 최소의 BER이다. 굳이 이것보다 좋을 필요는 없다.

![](https://i.imgur.com/WnkqFZn.png)

# Baseband Digital Data Transmission

Digital data를 전송하는데 다음과 같은 물리적 한계가 있다.
1. **Intersymbol interference** (ISI)
	- Bandlimited : Bandlimited한 system은 time unlimited인 signal이 된다. 하지만 이는 현실에서 불가능하므로 오차가 생기게 된다.
2. **Channel noise**
	- Channel 자체에서 생기는 noise

- **ISI problem**이 뭔지, 이를 해결하는 방법이 뭔지
- **Baseband pulse-shaping**은 무엇인가
- **eye pattern** : performance 확인 방법

![|575](https://i.imgur.com/TY8t2jJ.png)

# Channel Effects

**Ideal channel**은 