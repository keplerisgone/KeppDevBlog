
비범하게도 한국어로 "발진기"라고 한다.
회로에서 주파수를 맞추거나 MC(micro controller)에 신호를 인가할 때 사용한다. 

![|575](https://i.imgur.com/7y9datN.png)

oscillation은 다음과 같은 **Bark Hausen criteria oscillation condition**을 만족해야 한다.

![|525](https://i.imgur.com/JbYA93H.png)

- $|H(S)| = 1$일 것, 즉 gain의 크기가 1이여야 한다.
- phase shift가 180도로 일어날 것.
	- 정확하는 우리가 배운 feedback 회로는 subtractor로 동작하기 때문에, 기본적인 amplifier는 -180° shift가 일어난다. feedback 부분에서 -180°로 추가적인 shift가 일어나 총 360° shift가 일어나야 한다.
위 조건을 만족하면 oscillation이 일어난다.

# Various Oscillator

![|575](https://i.imgur.com/gWpczuJ.png)

oscillator는 다음과 같은 종류가 있다.
- **Ring oscillator**: R + transistor + parastic C 로 이루어진 oscillator이다. 
- **LC oscilltor**: I + C + transistor로 이루어진 oscillator이다.
- **Colpitts oscillator**: I + C로 이루어진 oscillator이다.
- **Crystal oscillator**: 크리스탈을 깎아만든 oscillator이다. reference로 사용한다. (매우 정확) 

## Ring Oscillator

![|450](https://i.imgur.com/gszR4SC.png)

- 단순히 CS stage + Capacitor를 세 개 연결해서 만든 oscillator이다. 
	- 세 개를 연결하는 이유는 phase를 -180 shift 하기 위해서다.
	- 두 개를 연결하면 phase shift는 최대 -180까지 할 수 있으나, gain이 사라진다.
우선 gain과 phase는 다음과 같이 계산할 수 있으며, 다음 조건을 만족해야 한다.

$$
A_{v}^{3}= (\frac{g_{m}R_{D}}{1+\frac{j\omega}{\omega_{p}}})^{3}, \ \measuredangle(\frac{g_{m}R_{D}}{1+\frac{j\omega}{\omega_{p}}})^{3} = -180\degree
$$

이 때 다음과 같은 정리를 통해 oscillation이 일어나는 frequency의 값, low-frequency gain을 구할 수 있다.

$$
\measuredangle(a+jb) = \tan^{-1}(\frac{b}{a}),\ \measuredangle(\frac{1}{a+jb})=-\tan^{-1}(\frac{b}{a}),\ \measuredangle(\frac{1}{a+jb})^{3}=-3\tan^{-1}(\frac{b}{a})
$$

$$
\frac{\omega}{\omega_{p}} = \sqrt{3},\ g_{m}R_{D}=2
$$

## LC-oscillator

![|575](https://i.imgur.com/YioXxUY.png)

- 왼쪽과 같은 회로에서 LC만 존재할 경우는 에너지를 저장하는 **LC tank**가 된다.
	- 이 때 impedance와 phase는 각각 무한대로 가거나 딱 떨어지는 모양이 된다.
- 하지만 resistor가 눈치없이 끼어들면 오른쪽과 같이 impedance는 제한되고, phase도 동글해진다.

$$
Z_{in1}(s) = sL \frac{1}{sC} = \frac{sL}{s^{2}LC+1} 
$$
$$Z_{in2}(s) = \frac{sRL}{s^{2}RLC+sL+R}$$
- resistance가 존재하면 에너지를 계속 잡아먹기 때문에 신호가 줄어든다. 

![](https://i.imgur.com/m5tZHgL.png)

## Cross-coupled Oscillator

![](https://i.imgur.com/iRVnEFI.png)

- 위에서 만든 RLC tank를 CS stage의 output단에 연결한 oscillator이다.
- 다만 CS stage + RLC tank를 모두 합쳐도 phse shift가 -270도 밖에 안된다.

![](https://i.imgur.com/3ko9rQY.png)

- phase 360도를 맞추기 위해 CS stage를 하나 더 추가했다.
- 요거를 다르게 그리면 아래와 같이 된다. Cross-coupled라고 불리는 이유다.

![|525](https://i.imgur.com/IwIRc9v.png)

- 여기다 current source를 달지 않고 capacitor를 추가할 수도 있는데, 이는 공간을 많이 차지해 쓰이지 않는다.

## Colpitts Oscillator

![](https://i.imgur.com/qiCT81t.png)

- Transistor를 하나만 사용해 만들 수 있는 oscillator이다. (BJT를 사용한다)
- collector에 inductor와 resistance를, capacitor로 feedback 회로를 만든다.
- 회로의 전체 frequency response는 $I_{ret}$와 $I_{test}$의 비로 구한다.

![](https://i.imgur.com/J33W0ux.png)

![|182](https://i.imgur.com/jHYUJDV.png)

![|475](https://i.imgur.com/kpgyoY5.png)

![|475](https://i.imgur.com/Ay6ZUpq.png)

- 다 긁어왔다

교재를 보면 뒷부분이 더 중요한 내용 같은데 안 하셨다. 
따로 해볼까?
회로 공부하다보면 느끼는건데
라자비 한 권만 먹어서 야비하게 강해지면 소원이 없겠다