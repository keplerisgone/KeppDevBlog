# Feedback

회로를 설계할 때는 다양한 amplifier를 사용하지만, amplifier는 active device이기 때문에 non-linear하다. 이를 해결하는 것이 바로 **Feedback circuit**이다.

![|550](https://i.imgur.com/3LL1y0N.png)

회로를 linear하게 만드는 방법은 다음과 같다. Feedback 회로의 gain은 다음과 같다.

$$ Y = \frac{A}{1+Ak}X \approx \frac{1}{k}X$$

대부분 amplifier는 gain이 굉장히 높기 때문에 gain이 저렇게 수렴한다.

## Properties of Feedback

Feedback circuit은 다음과 같은 특징을 지닌다.

- **Gain desensitization** : 회로의 gain에 대해 영향을 잘 받지 않는다.

![|450](https://i.imgur.com/nevgQ7T.png)

- **Bandwidth extension** : 다음과 같은 원리로 gain은 좀 줄어들지만 bandwidth는 늘어난다. 굳이 쓰는 이유는 linearity가 늘어나기 때문

![|600](https://i.imgur.com/4hOf1dB.png)

- **Impedance modification** : 회로의 구성에 따라 input / output impedance가 크거나 작아진다.

![](https://i.imgur.com/qDb5mPi.png)

- **Linearity** : 회로의 선형성이 증가한다. 이 부분은 대학원가서 배워용


## Sense, Return (Add)

Feedback 회로는 신호를 **sensing**하는 부분과 이를 다시 입력 부분에 **return**하는 부분으로 나뉜다.

![|625](https://i.imgur.com/rFwN2uK.png)

# Example

## 12.1

![](https://i.imgur.com/F1cpbMl.png)

## 12.7 

![](https://i.imgur.com/1IipWo0.png)
