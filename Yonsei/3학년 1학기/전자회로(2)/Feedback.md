# Feedback

회로를 설계할 때는 다양한 amplifier를 사용하지만, amplifier는 active device이기 때문에 non-linear하다. 이를 해결하는 것이 바로 **Feedback circuit**이다.

![|550](https://i.imgur.com/3LL1y0N.png)

회로를 linear하게 만드는 방법은 다음과 같다. Feedback 회로의 gain은 다음과 같다.

$$ Y = \frac{A}{1+Ak}X \approx \frac{1}{k}X$$

이를 **closed-loop gain**이라고 하며, $Ak = T$는 따로 **Loop gain**이라고 부른다.
대부분 amplifier는 gain이 굉장히 높기 때문에 gain이 저렇게 수렴한다.

loop gain은 loop를 끊어 계산할 수 있다.

## Properties of Feedback

Feedback circuit은 다음과 같은 특징을 지닌다.

- **Gain desensitization**: 회로의 gain($A$)에 대해 영향을 잘 받지 않는다.
	- 그 외에도 신호의 frequency, load resistance, signal amplitude의 영향을 크게 받지 않는다.

![|450](https://i.imgur.com/nevgQ7T.png)

- **Bandwidth extension**: 다음과 같은 원리로 gain은 좀 줄어들지만 bandwidth는 늘어난다. 굳이 쓰는 이유는 linearity가 늘어나기 때문

![|600](https://i.imgur.com/4hOf1dB.png)

- **Impedance modification**: 회로의 구성에 따라 input / output impedance가 크거나 작아진다.

![](https://i.imgur.com/qDb5mPi.png)

- **Linearity**: 회로의 선형성이 증가한다. 이 부분은 대학원가서 배워용

## Sense, Return (Add)

Feedback 회로는 신호를 **sensing**하는 부분과 이를 다시 입력 부분에 **return**하는 부분으로 나뉜다. 이는 Loop 관점에서의 sense/return이다. 회로 전체 기준이 아니다!

![|625](https://i.imgur.com/rFwN2uK.png)

이 때 voltage/current 중 무엇을 sensing/return하느냐에 따라 회로의 구성이나 특징이 달라진다. 
- **V/V** : voltage amplifier
- **I/V** : transconductance amplifier
- **V/I** : resistance amplifier (transimpedance)
- **I/I** : current amplifier

### 원리?

![|550](https://i.imgur.com/ItRyf4Z.png)



sensing의 경우는 **Multimeter**를 생각하면 쉽다. voltage의 경우 *parallel*로, current의 경우 *series*로 측정하기 때문!
return의 경우는 **source**를 생각하면 쉽다. voltage의 경우 *series*로 연결하고, current의 경우 *parallel*로 연결하기 때문!

> [!note] 
> voltage를 parallel로 연결한 경우 더 낮은 쪽에 맞춰질 때까지 발열 + 방전,
> current를 series로 연결한 경우 회로 작동이 X

## Impedance of Feedback Circuit

![|350](https://i.imgur.com/U0GuEK9.png)

- **voltage**는 input impedance가 낮고, output impedance가 높아야 한다. output에서 신호를 더 sensing해야 하기 때문이다.
- **current**는 input impedance가 크고, output impedance가 높아야 한다. 전류가 output 단으로 많이 흘러 들어가야 하기 때문이다.
-> 물론 input/output 기준은 모두 loop 기준이다!

- **V/V** : input은 작고, output은 커야 한다. -> CE + source follower
- **V/I** : input과 output이 모두 커야 한다. -> CE stage
- **I/V** : input과 output이 모두 작아야 한다. -> source follower + source follower
- **I/I** : input은 크고, output은 작아야 한다. -> common gate

이 때 
- **impedance가 커짐** : $Z_{f} = Z_{o}(1+Ak)$
- **impedance가 작아짐** : $Z_{f} = \frac{Z_{o}}{1+Ak}$
f는 feedback 회로에서의 impedance, o는 open-loop impedance. open-loop impedance와 gain은 모두 feedback loop가 없었을 때를 기준으로 한다.

## Feedback Network

![|450](https://i.imgur.com/9mMFwQP.png)

넵. I/I는 알아서 생각해

## Polarity of Feedback

![|625](https://i.imgur.com/KzdpIZo.png)
(그림이 이상한 것 같다)

Feedback 회로에서 return되는 신호의 polarity에 따라서 기능이 달라진다.
- **Positive** : return된 신호가 입력 신호를 강화 -> 계속 커져요..?
- **Negative** : return된 신호가 입력 신호를 방해 
참고로 전부 **subtractor**를 이용하기 때문에 저런 결과가 나온다.

> [!note]
> - 둘의 차이를 출력!!!
> - 

## Effect of Nonideal I/O Impedance

회로를 분석하기 위해서는 Loop gain $k$와 open gain A를 알아야 한다.
1. impedance를 고려하여 회로를 자른다.
	1. Large의 경우 open, small의 경우 GND에 연결
2. sense/return에 따라 비율을 계산
3. Gain $\frac{A}{1+Ak}$를 계산

> [!note]
> current return의 경우는 회로로 들어가는 방향으로 계산

## Stability in Feedback

Bode plot을 이용해 Phase 정보도 살펴볼 수 있다.

![|625](https://i.imgur.com/g7DdR8D.png)

왜 phase 정보로 stability를 알아낼 수 있는걸까??
-> negative feedback이 phase shift로 인해 positive feedback이 되어 oscillation이 일어날 수 있기 때문!
그래서 phase가 180도 이상이 되는 주파수를 알아내 조심해야 함.
- 하나의 pole에 의해서는 $-90\degree$의 phase shift를 갖는다.
- 정확히 **zero/pole**에서는 $\pm 45 \degree$를 가진다.
- **one-tenth zero/pole**에서는 phase의 변화가 시작
- **ten times zero/pole**에서는 $\pm 90\degree$를 가진다.

![|600](https://i.imgur.com/NTan7QM.png)

요런 느낌
- stable 하기 위해서는 oscillation하지 않는다는 것이므로, phase shift가 180도 이상되는 곳에서 gain이 1 이하여야 한다.
	- 다만 $|KH|$의 phase와 gain으로 계산한다. Feedback 기준이라는 뜻.
- 이를 높은 gain에서 이루기 위해서는 frequency compensation이 필요한데, 이는 pole을 옮겨서 bandwidth를 포기하는 대신 -180 shift에서 gain이 빠르게 감소하도록 하는 것이다.

# 푸는 법

1. 우선 feedback loop를 끊는다. I/O impedance 가 변화하는 정도에 따라 open, short를 정함에 유의한다. 
	1. 만약 문제에서 저항이 높다던가 낮다던가 하는 조건이 주어지면 무시해도 된다.
2. 이렇게 끊은 회로에서 구한 gain이 $A_{0, open}$이다. 
3. $k$는 따로 feedback loop 부분만 뜯어서 구한다.
4. $\frac{A_{0}}{1+A_{0}k}$를 구하면 closed-loop gain이 된다.

## 종류에 따른 gain 구하는 법

k는 회로가 작아서 구하기 쉬우니까 A에 대해서만 서술.

- **V/V** : 평소에 구하듯이...
- **I/V** :  transimpedance를 구해야 하는데, output 저항이 곧 transimpedance임을 생각하면 괜찮다. 이걸로 한 단에서  voltage output 으로 바꾼 뒤 V/V를 쓰자.
- **V/I** : transconductance의 정의를 이용하자.
-  **I/I** : 같은 current라 좀 쉽다. 다만 feedback current가 output 쪽으로 들어가는 방향이다.

> [!note]
> - current divider는 다음과 같이 구할 수 있다.
> - $\frac{\text{갈라지는데 남겨진 저항}}{\text{갈라지는 저항의 총합}}$
> - current의 경우는 output impedance를 특이하게 구한다. series로 구해버리는 것이 특징.
# Example

## 12.1

![](https://i.imgur.com/F1cpbMl.png)

## 12.7

![](https://i.imgur.com/1IipWo0.png)

## 12.26

## 12.27

## 12.28

## 12.29

## 12.30

## 12.31

## 12.32

## 12.33