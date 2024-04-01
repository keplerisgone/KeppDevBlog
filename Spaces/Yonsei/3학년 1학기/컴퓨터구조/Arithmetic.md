## Adding Binary Numbers

![](https://i.imgur.com/aXP5tZQ.png)

유치원생이 덧셈하듯이 계산하면 된다. 1과 1을 더할 때는 1이 carry가 되어 올라간다. 나머지 계산은 알아서 수행하자. 다른 upper bit는 0가 된다.

## Subtracting Binary Numbers

![](https://i.imgur.com/Hip7z6U.png)

이것 또한 유치원생이 계산하듯 계산하면 된다. 0에서 1을 빼는 경우만 조심하면 된다.

![](https://i.imgur.com/F2UUPJs.png)

그대로 뺄셈을 수행하지 않고 two's / one's complement 적용 후 덧셈을 하는 방식도 있다.
## Overflow Conditions
만약 사용하고 있는 bit의 수가 연산 결과를 표시할 수 없다면, **overflow**가 발생하게 된다. overflow는 다음과 같은 상황에서 발생할 수 있다.

1. 덧셈의 경우, 두 수의 sign이 같을 때
2. 뺄셈의 경우, 두 수의 sign이 다를 때

위의 경우는 연산 결과가 표현 범위를 벗어나 overflow가 발생할 수 있다. overflow로 인한 연산 결과는 본래의 결과와 부호가 다른 경우가 대부분이다.

다만 다음과 같은 상황에서는 절대 overflow가 발생하지 않는다.

1. 덧셈의 경우, 두 수의 sign이 다를 때
2. 뺄셈의 경우, 두 수의 sign이 같을 때

위의 경우는 연산 결과가 무조건 범위 안에 있을 수밖에 없으므로, overflow가 발생하지 않는다. overflow가 발생하는 경우를 표로 정리하면 다음과 같다.

![](https://i.imgur.com/E3VO3VL.png)
## Adder Logic
Adder의 구성은 **ripple-carry adder**와 **carry-lookhead adder**로 나뉠 수 있다. [TODO] - 뭔지 찾아보기
## Multiplying Binary Numbers
binary number에서 곱셈하는 법을 알아보자. 초등학생이 두자리수 곱셈을 하듯이 계산하면 된다. 여기서 곱함 당하는(...) 숫자를 **Multiplicand**, 곱하고자 하는 수를 **Multiplier**라고 한다. multiplier의 LSB부터 시작하며, LSB가 0일 경우 0을 내리고, 1일 경우 multiplicand를 그대로 내리면 된다. 이렇게 구한 결과는 **product**라고 하며, product는 $(m + n)$bit의 크기를 가진다.