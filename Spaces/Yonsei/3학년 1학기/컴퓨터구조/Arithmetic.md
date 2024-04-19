# Adding Binary Numbers

![|450](https://i.imgur.com/aXP5tZQ.png)

유치원생이 덧셈하듯이 계산하면 된다. 1과 1을 더할 때는 1이 carry가 되어 올라간다. 나머지 계산은 알아서 수행하자. 다른 upper bit는 0가 된다.

# Subtracting Binary Numbers

![|450](https://i.imgur.com/Hip7z6U.png)

이것 또한 유치원생이 계산하듯 계산하면 된다. 0에서 1을 빼는 경우만 조심하면 된다.

![|450](https://i.imgur.com/F2UUPJs.png)

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

![|425](https://i.imgur.com/mEbLcLz.png)

위의 ALU size를 불필요하게 사용한다는 단점을 해결하기 위해 Product와 Multiplier를 128bit로 한군데 저장하고, 64bit ALU를 사용하는 방법을 고안했다. 128bit register의 lower half에는 multiplier가, 나머지에는 product가 저장된다. 위의 logic과 다른 점은
1. Multiplicand가 shift되지 않고 그대로 product자리에 add됨.
2. product가 multiplier자리에 나옴
3. carry를 위한 1bit가 따로 존재
 등등이 있다. 
굳이 Multiplicand를 shift하지 않는 이유는 위 register를 shift함으로써 product 자리까지 shift되기 때문에 결과가 똑같이 나오기 때문이다. 아래는 계산 예시이다.

![](https://i.imgur.com/zHJ6Sco.png)

## Multiplying Signed Numbers

부호가 다르면 계산 결과가 음수, 부호가 같으면 계산 결과가 양수가 됨을 이용한다. 연산은 음수를 two's complement를 이용해 계산한 후, sign bit를 정하는 방식으로 연산한다. multiplying을 이용하는 명령어는 다음과 같다.

- `mul`: 연산 결과의 lower 64bit를 반환.
- `mulh`: 연산 결과의 upper 64 bits를 반환.
- `mulhu`: 연산 결과의 unsigned upper 64bits를 반환.

## Avoiding Multiply Operations

하지만 곱셈 연산은 덧셈 연산을 여러 번한 것과 같은 효과이므로 효율이 매우 나쁘다. 다양한 프로세서는 덧셈과 뺄셈 연산[^2]에 더 최적화되어 있기 때문에, 이들은 하나의 clock cycle만 소모하지만 multiplication은 multiple clock cycle이 걸린다.
때문에 다양한 컴파일러는 multiplication 연산을 적당한 shift instruction으로 바꾸어 코드를 최적화한다.

# Dividing Binary Numbers

![|450](https://i.imgur.com/xhbmjmb.png)

division은 multiplication의 역연산으로, 나눔 당하는 수를 **Dividend**, 나누는 수를 **Divisor**, 결과를 **Quotient**라고 한다. 나머지는 **Remainder**. 연산은 dividend의 맨 앞자리부터 Divisor를 계속해서 빼는 방식으로 진행한다.

## Divider Logic

![400|375](https://i.imgur.com/PFegyO2.png)

Multiplication과 마찬가지로 사람이 연산하는 방식과 같이 logic이 이루어져 있다. 64bits의 Divisor와 Dividend가 128bits ALU에 옮겨져 연산을 진행한다. Quotient와 remainder는 잘 계산되겠지!

## Divider Algorithm

![|450](https://i.imgur.com/88T3i8f.png)

division의 알고리즘은 다음과 같다.
1. 일단 remainder를 diviend로 세팅한다
2. remainder에서 divisor를 빼본다
3. 결과의 부호를 확인, positive면 quotient를 left shift하고 LSB를 1로 설정, negative면 다시 remainder를 복구한 후(dividend 더하기) quotient를 left shift 한 후 LSB를 0으로 설정.
4. divisor를 right shift한다.
모두 사람이 하는 과정을 그대로 옮긴 것.

## Revised Divider Logic

![|375](https://i.imgur.com/0lHdtNU.png)

128bits의 ALU를 사용한다는 단점이 multiplier와 같이 남아있기 때문에 이를 해결해야 한다. 이는 Remainder와 quotient가 같은 register를 사용함으로써 해결한다. 이 register를 계속 left shift하며 연산을 진행한다. 아래는 연산의 예시이다.

![|650](https://i.imgur.com/rKfbuAl.png)

## Dividing Signed Numbers

multiplication과 마찬가지로 음수를 two's complement로 변환한 뒤, 연산을 진행한다. 이후 두 수의 부호를 비교해 연산 결과의 부호를 결정한다. dividsion 연산을 사용하는 명령어는 다음과 같다.
- `div`: division 연산을 수행.
- `divu`: unsigned division 연산을 수행
- `rem`: remainder를 구하는 연산을 수행
- `remu`: unsigned division의 remainder를 구하는 연산을 수행

# Real Numbers and Scientific Notation

컴퓨터는 1.24525, 3.1415와 같은 실수, real number를 나타낼 수 있다. **scientific notation**은 수를 single digit + decimal point로 나누어 표현하는 것으로, 12345를 $1.2345\times 10^{4}$로 나타내는 것과 같다. 저렇게 singel digit으로 나타나야만 **normalized**되었다고 표현한다. $12.345\times  10^{3}$은 잘못된 표현이라는 것. 그리고 이 방식은 컴퓨터가 floating point number를 나타내는데 기본이 되는 표현 방식이기도 하다.

# Binary Floating-Point Numbers

컴퓨터는 decimal이 아닌 Binary를 사용한다. 따라서 위의 scientific notaion을 binary로 개량한 방식을 사용한다. 따라서 (1과 가까운 적당한 수 x $2^{n}$)로 float를 표현한다. 이는 다시 $\pm 1.aaa\times 2^{\pm bbb}$로 나타낼 수 있는데, a는 **fraction**, b는 **exponent라고** 한다. 

## IEEE 754 Floating-Point Standard

![|600](https://i.imgur.com/xrzQi7s.png)

이는 1980년에 컴퓨터에서 floating point number를 표현하기 위해서 개발된 방법이다. 이는 **sign and magnitude** 방법이라고 불린다. 32bits를 이용해서 수를 표현하는데, 가장 처음 비트는 sign을 나타내고, 이후의 8bits는 exponent, 나머지는 Fraction을 나타낸다. 

### Fraction

$1.aaa$를 나타내는 방법을 알아보자. 우선 aaa 왼쪽의 수는 1로 고정이므로 생각하지 않도록 한다. fraction 부분은 차례대로 $2^{-1}, 2^{-2}, 2^{-3}...$를 나타내며, 최종적으로는 1로 표시된 부분의 값을 모두 더하는 것으로 끝난다. 다만 0은 *모든 비트를 0으로 설정하는 것*으로 특별하게 정의한다.

### Exponent

$2^{\pm bbb}$를 나타내는 방법을 알아보자. 이를 나타내는 데는 **bias notation**이 사용된다. bias notation은 127를 bias, 기준으로 삼는 notation으로, *0b01111111*을 0으로 삼는다. 따라서 1은 127+1 = 128. *0x10000000*이 된다. 

예를 들어, -0.75를 나타내려면
1. sign이 -이므로 첫 비트는 1
2. 0.5+0.25이므로 $2^{-1}+2^{-2}$ -> $2^{-1}(1+2^{-1})$로 정리.
3. exponent는 -1이므로 01111110 (127-1), fraction은 0.5이므로 1000....일 것.

### Standard Encoding

다음과 같은 경우는 특수 경우이다. 

![|500](https://i.imgur.com/iKUl5UP.png)

fraction이 0이 아니고 exponent가 0인 경우는 **denormalized number**로, 이 때는 0.aaa를 나타낸다. 

## Tradeoff Between Fraction and Exponent

물론 fraction의 수가 많아진다면 더 정확한 float를 나타낼 수 있고 더 넒은 범위의 수를 나타낼 수 있지만, register의 공간을 더 많이 차지할 수 있다는 단점이 있다. 

또 fraction와 exponent의 크기가 잘 균형을 이루어야 하는데, fraction의 크기는 정확도와 상관있고, exponent의 크기는 범위와 상관있다. 하지만 exponent가 크면 overflow가 일어나기 쉽고, fraction이 작으면 underflow가 일어나기 쉽다.

### Double Precision

그래서 이를 해결하기 위해서 double precesion을 사용하기도 하는데, 이는 11bits의 exponent와 52bits의 fraction을 사용한다. RISC-V는 다양한 float 연산에 single-precision와 double-precision 모드를 지원하는데, 명령어 뒤에 `.s`와 `.d`를 붙여 구분한다.

![|550](https://i.imgur.com/Rzj4kME.png)

### Exceptions and Traps

보통 컴퓨터는 overflow와 underflow가 일어났을 때 exceptino을 발생시켜 인터럽트를 일으키지만, RISC-V는 그냥 FCSR이라는 마크를 남겨 발생 여부를 표시한다. 종류는 다음과 같다.
- **NV**: invalid operation
- **DZ**: Divide by zero
- **OF**: overflow
- **UF**: underflow
- **NX**: inexact

## Adding Floating-point Numbers

일단 연산을 진행하기 전에 어떤 방식으로 이루어지는지부터 알아보자. 우선 모든 fraction은 세자리까지밖에 표현하지 못한다. 따라서 shift를 진행해야 하는데, 무조건 큰 수에 맞춰서 작은 수를 shifting 한다. 이는 연산에 생길 오차를 최소화 하기 위함이다. exponent를 맞춰 더한 뒤, add를 진행하고, normalization을 한 뒤 three digit에 맞춰 round하면 끝이다. Binary floating에서는 다음과 같이 이루어진다.
1. 두 float의 binary 표현을 구한다. 
2. 큰 수의 exponent에 작은 수를 맞춰 shift한다. 
3. 일단 fraction을 더한다.
4. 더한 결과를 normalization 한다. (이 때는 exponent도 고려)
5. over/underflow 여부 확인, round를 진행한다. 
	1. round를 진행하다가 overflow가 발생하면 (2.aaa가 되는 경우) 또 rounding을 해야 한다.

![|600](https://i.imgur.com/YDxNEDZ.png)

## Multiplying Floating-Point Numbers

1. 두 수의 binary 표현을 구한다. 
2. fraction 부분의 multiplying 진행.
3. exponent 부분을 더한다. 
	1. 이 때 bias를 고려해 127를 한 번 빼주어야 한다.
4. normalization
5. 결과의 overflow, underflow여부 확인, rounding 진행

## Accuracy of Floating-Point Numbers

사실 위와 같은 특성때문에 Floating-point는 정확할 수가 없다. float를 표현하는 모든 과정이 rounding과 approximation으로 이루어져있기 때문에 실제 수와 많이 차이가 날 수 있다. 이를 위해서 다양한 하드웨어에서 rounding 을 하기 위한 extra bit를 사용하기도 한다. IEEE 754 같은 경우는 **guard bit**와 **round bit**를 사용한다.
- **guard bit**: 
- **round bit**:

[^1]:: 연산을 진행할 때 *Multiplier 한 칸 왼쪽으로 옮겨서 계산하기*의 방식과 같다.
[^2]:: 뺄셈 연산도 사실 complement 과정이 들어간 덧셈 연산이긴 하다.