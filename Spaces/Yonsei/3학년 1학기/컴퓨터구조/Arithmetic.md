# Adding Binary Numbers

![](https://i.imgur.com/aXP5tZQ.png)

유치원생이 덧셈하듯이 계산하면 된다. 1과 1을 더할 때는 1이 carry가 되어 올라간다. 나머지 계산은 알아서 수행하자. 다른 upper bit는 0가 된다.

# Subtracting Binary Numbers

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
# Multiplying Binary Numbers

![400](https://i.imgur.com/kHZOQCD.png)

binary number에서 곱셈하는 법을 알아보자. 초등학생이 두자리수 곱셈을 하듯이 계산하면 된다. 여기서 곱함 당하는(...) 숫자를 **Multiplicand**, 곱하고자 하는 수를 **Multiplier**라고 한다. multiplier의 LSB부터 시작하며, LSB가 0일 경우 0을 내리고, 1일 경우 multiplicand를 그대로 내리면 된다. 이렇게 구한 결과는 **product**라고 하며, product는 $(m + n)$bit의 크기를 가진다.
## Multiplier Algorithm

Multiplying의 알고리즘은 다음과 같다. 중요한 아이디어는 *Multiplier의 LSB부터 계산한 뒤 덧셈 연산을 수행하는 것*이다.
1. Multiplicand와 Multiplier LSB와의 연산을 수행한다. 
2. LSB가 0이면 아무것도 수행하지 않고, LSB가 1이면 Product에 Multiplicand를 더한다.
3. Multiplicand는 **Left shift**, Multiplier는 **Right shift**를 진행한다.[^1]
4. 1~3을 반복한다.
## Multiplier Logic

![400](https://i.imgur.com/zukFkJX.png)

**Multiplier**는 64bit의 Multiplicand와 Multiplier 를 받아 128bit를 수용하는 ALU(연산 장치)로 Product를 계산하는 구조로 이루어져 있다.
여기서 가장 큰 문제는 굳이 ALU가 128bit를 사용할 필요가 없다는 것이다! 그리고 128bit ALU를 만드는 난이도도 굉장히 어렵다. ALU는 디지털 논리 회로의 FF(flip-flop)를 여러 개 붙여서 만드는데, 수용 bit 수가 올라갈 수록 사용해야 하는 FF의 수가 기하급수적으로 늘어나기 때문.
## Revised Multiplier Logic

![](https://i.imgur.com/mEbLcLz.png)

위의 ALU size를 불필요하게 사용한다는 단점을 해결하기 위해 Product와 Multiplier를 128bit로 한군데 저장하고, 64bit ALU를 사용하는 방법을 고안했다. 128bit register의 lower half에는 multiplier가, 나머지에는 product가 저장된다. 위의 logic과 다른 점은
1. Multiplicand가 shift되지 않고 그대로 product자리에 add됨.
2. product가 multiplier자리에 나옴
3. carry를 위한 1bit가 따로 존재
 등등이 있다. 
굳이 Multiplicand를 shift하지 않는 이유는 위 register를 shift함으로써 product 자리까지 shift되기 때문에 결과가 똑같이 나오기 때문이다. 아래는 계산 예시이다.

![](https://i.imgur.com/zHJ6Sco.png)
## Multiplying Signed Numbers

부호가 다르면 계산 결과가 음수, 부호가 같으면 계산 결과가 양수가 됨을 이용한다. 연산은 음수를 two's complement를 이용해 계산한 후, sign bit를 정하는 방식으로 연산한다. 

[^1]: : 연산을 진행할 때 *Multiplier 한 칸 왼쪽으로 옮겨서 계산하기*의 방식과 같다.