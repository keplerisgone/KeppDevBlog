---
Created: 2023-09-13T20:24
Parent item:
  - "[[Signals and Systems]]"
---
DT unit impulse and unit step sequences

CT unit step and unit impulse functions

scaled impulse

Running integral

## DT unit impulse and unit step sequences

![[Screenshot_2023-09-13_at_8.32.44_PM.png]]

- impulse 는 n=0 에서만 1 신호를 가지는 signal
- unit step function은 특정 n 이상에서만 1 신호를 가지는 signal
- 다양한 시그널은 unit impulse로 표현이 가능, 특히나 $n=k$﻿ 에서의 신호는 한 신호와 unit impulse의 곱으로 표현가능
- unit step function은 특정 n 이상의 unit impulse의 합들임
    
    ![[Screenshot_2023-09-13_at_8.36.20_PM.png]]
    
    즉, $u[n]=\sum^n_{k=-\infty}\delta [k]$﻿ 로 표현이 가능. 이는 일반적인 신호도 마찬가지
    
- unit impulse, unit step function 모두 어떠한 signal을 표현하기 위해 사용하는 도구임에 유의할 것!

## CT unit step and unit impulse functions

![[Screenshot_2023-09-13_at_8.45.04_PM.png]]

CT 에서의 impulse, unit step function은 다음과 같이 나타납니다. unit step functiond은 현실적으로는 아래처럼 생겼고, unit impulse는 이를 미분한 signal 입니다. 저 $\Delta$﻿ 값을 0으로 보낸 것이 이론적인 step, impulse function입니다. 그렇다면 반대로 impulse 를 적분한 것이 step function이 되겠지요?

### scaled impulse

![[Screenshot_2023-09-13_at_8.50.28_PM.png]]

말 그대로 정수배가 된 impulse입니다. voltage의 변화를 더 상세하게 나타냅니다.

### Running integral

![[Screenshot_2023-09-13_at_8.56.09_PM.png]]

위의서의 DT unit step function과 unit impulse function의 관계를 생각해봅시다. unit step function은 특정 시점 $n$﻿ 이후의 unit impulse function을 모두 더한 것입니다.

Running integral 도 원리가 같습니다. CT 에서의 unit step function은 실행한 특정 시점(Running) 까지의 unit impulse function의 적분값 = 변화를 모두 더한 결과 (integral) 을 뜻합니다.

![[Screenshot_2023-09-13_at_8.56.31_PM.png]]