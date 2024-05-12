# Feedback

회로를 설계할 때는 다양한 amplifier를 사용하지만, amplifier는 active device이기 때문에 non-linear하다. 이를 해결하는 것이 바로 **Feedback circuit**이다.

![|550](https://i.imgur.com/3LL1y0N.png)

회로를 linear하게 만드는 방법은 다음과 같다. Feedback 회로의 gain은 다음과 같다.

$$ Y = \frac{A}{1+Ak}X \approx \frac{1}{k}X$$

대부분 amplifier는 gain이 굉장히 높기 때문에 gain이 저렇게 수렴한다.

## Properties of Feedback

Feedback circuit은 다음과 같은 특징을 지닌다.

- **Gain desensitization**: 회로의 gain에 대해 영향을 잘 받지 않는다.

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
- **V/I** : resistance amplifier
- **I/I** : current amplifier

### 원리?

![|550](https://i.imgur.com/ItRyf4Z.png)



sensing의 경우는 **Multimeter**를 생각하면 쉽다. voltage의 경우 *parallel*로, current의 경우 *series*로 측정하기 때문!
return의 경우는 **source**를 생각하면 쉽다. voltage의 경우 *series*로 연결하고, current의 경우 *parallel*로 연결하기 때문!

## Impedance of Feedback Circuit

![|325](https://i.imgur.com/U0GuEK9.png)

- **voltage**는 input impedance가 낮고, output impedance가 높아야 한다. output에서 신호를 더 sensing해야 하기 때문이다.
- **current**는 input impedance가 크고, output impedance가 높아야 한다. 전류가 output 단으로 많이 흘러 들어가야 하기 때문이다.
-> 물론 input/output 기준은 모두 loop 기준이다!

# Example

## 12.1

![](https://i.imgur.com/F1cpbMl.png)

## 12.7

![](https://i.imgur.com/1IipWo0.png)
