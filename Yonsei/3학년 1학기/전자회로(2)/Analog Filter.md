송수신 시스템에서는 송신 - 수신 신호의 크기와 세기가 많이 차이가 난다. 
그럼 내 작은 신호는 어떻게 찾을 수 있지??? -> filter를 이용한다.

# Filter Characteristics

![](https://i.imgur.com/ppZRexj.png)

- **Passband**: plat한 부분을 말한다. 이 주파수 대역은 잘 통과한다.
- **Stopband**: gain이 0인 부분을 말한다. 신호가 잘 통과하지 않는다.
- **Transition band**: Pass와 stop 사이를 말한다. 여기가 sharp하면 좋다.
- **ripple**: response가 흔들리는 부분을 말한다. 나중에 나오겠지만, ripple을 줄이면 sharpness가 안 좋아지고 ripple을 포기하면 sharpness가 좋아진다.

# Classification of Filters

![](https://i.imgur.com/7ZBLuGB.png)

- **LPF**: Low-Pass Filter로 저주파수 대역의 신호를 통과시킨다.
- **BPF**: Band-Pass Filter로 특정 주파수 대역의 신호를 통과시킨다.
- **HPF**: High-Pass Filter로 고주파수 대역의 신호를 통과시킨다.
- **Band-Reject Filter**: 특정 주파수 빼고 다 통과시킨다.

# Filter Transfer Function

- 우리가 배우는 filter들은 또 RLC 회로이기 때문에, Transfer function으로 특징을 알 수 있다. 
- 기본적인 Transfer function의 형태는 다음과 같다.

$$
H(s) = \alpha \frac{(s-z_{1})(s-z_{2})...}{(s-p_{1})(s-p_{2})...}
$$

- $z_{k}$과 $p_{k}$는 일반적으로 $\sigma+j\omega$로 나타낸다.

## Example: 15.4

![|600](https://i.imgur.com/2CbAdw0.png)

위 회로들의 pole, zero를 분석하면 다음과 같이 된다. 계산은 직접 해보자..

![|575](https://i.imgur.com/GatfHyG.png)

세번째 회로는 imaginary term을 가진다.
- 축 위의 zero와 pole은 real, 축 밖의 zero와 pole은 imaginary다.

![](https://i.imgur.com/UxrwTt9.png)

- 이 때 $\sigma$ 의 위치에 따라 response가 달라진다.
	- $\sigma$ > 0일 경우, positive oscillation
	- $\sigma$ = 0일 경우, oscillation x
	- $\sigma$ < 0일 경우, negative oscillation -> stable
- 이게 이렇게 되는 이유는 transfer function을 Laplace transform해보면 나온다.
- transfer function을 L로 time domain에서 나타내면 zero와 pole이 exponential로 나타나는데, 이 때 $\sigma$ 의 부호가 exponential의 모양을 결정하기 때문.

# First-Order Filter

$$
H(s) = \alpha \frac{s+z_{1}}{s+p_{1}}
$$

- 위 수식으로 나타낸다.

![|575](https://i.imgur.com/BsoYjoZ.png)

- 이렇게 된다고 한다.

![](https://i.imgur.com/5RDy6Z6.png)

- 이것도 한 번 분석해보자.
- $R_{1}C_{1}$과 $R_{2}C_{2}$의 값에 따라 response가 달라지는 게 신기하다.

# Second-Order Filter

$$
H(s)= \frac{\alpha^{2}+\beta s+\gamma}{s^{2}+\frac{\omega_{n}}{Q}s+\omega_{n}^{2}}
$$

- 수식으로는 위와 같이 나타낸다.
- $\omega_n$과 $Q$는 계산된 수식에서 끌어내릴 수 있으며, 회로의 특징을 결정짓는 중요한 값이다.
	- $\omega_n$은 값의 범위를, **Q**(quality factor)는 zero와 pole의 imaginary 정도를 결정한다.

![|186](https://i.imgur.com/RRvmCmh.png)

- 위 response에서 pole은 다음과 같다.

$$s_{12}=- \frac{\omega_{n}}{2Q}\pm j\omega_{n}\sqrt{q- \frac{1}{4Q^{2}}}$$

- 따라서 *Q가 작으면 real*이 되고, 크면 imaginary 성분이 강해진다. 

![|375](https://i.imgur.com/Bler1tl.png)

- Q가 $\frac{\sqrt{2}}{2}$보다 크면 oscillation, 작으면 그냥 쳐진다.
	- oscillation이 살아있을 경우 peak는 $\omega_{n}\sqrt{1- \frac{1}{2Q^{2}}}$에서 이루어진다.
	- peak magnitude는 $\frac{Q}{\sqrt{1-(4Q^{2})^{-1}}}$가 곱해진다고 한다.
	- 물론 대부분의 경우에서 $4Q^{2}$가 크기 때문에 무시하고 $\omega_{n}$, $Q$로 생각한다.
	- 이는 HPF에서도 동일, BPF에서는 좀 다르다.


![|475](https://i.imgur.com/kTNjWFb.png)

- 식에 따라서 계산해보면... 저렇게 나온다고 한다.

> [!question]
> 그러면 BPF에서는 Quality factor가 무슨 역할을 하는 것인가요

![|250](https://i.imgur.com/isJ7hYP.png)

- $\alpha=\beta=0$일 경우: LPF
- $\alpha= \gamma = 0$일 경우: BPF
- $\beta = \gamma=0$일 경우: HPF

## RLC Realizations

![](https://i.imgur.com/toE5YSi.png)

- RLC 회로를 통해 이를 알아보도록 하자

![](https://i.imgur.com/evZEEc8.png)
 - 이것도 귀찮으면 어떡하려고.

### LPF

![|237](https://i.imgur.com/lTccj8Q.png)

$$H(s) = \frac{R}{s^{2}RLC+sL+R}$$

### HPF

![|239](https://i.imgur.com/VQz3wee.png)

$$
H(s) = \frac{s^{2}RLC}{s^{2}RLC+sL+R}
$$

### BPF

![|251](https://i.imgur.com/EwYMez7.png)

$$
H(s) = \frac{sL}{s^{2}RLC+sL+R}
$$

# Active Filter

- 하지만 RLC 소자를 이용하는 것은 공간을 너무 많이 차지하므로 Op-amp를 이용한 Active filter를 주로 사용한다.