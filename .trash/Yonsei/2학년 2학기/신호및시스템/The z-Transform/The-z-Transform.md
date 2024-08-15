---
Created: 2023-08-31T21:57
---
![[Screenshot_2023-11-20_at_4.56.06_PM.png]]

Z transform은 DTFT의 확장판입니다.

DTFT는 다음과 같이 표현됩니다.

> $z=e^{j\omega}$﻿, $X(e^{j\omega})=\sum^\infty_{n=-\infty}x[n]e^{-j\omega n}$﻿

이제 z를 complex exponential로 생각하고 $z=re^{j\omega}$﻿로 판단합니다.

![[Screenshot_2023-11-20_at_4.56.22_PM.png]]

따라서 ZT 수식으로 표현하면 다음과 같습니다.

> $X(z)=\sum^\infty_{n=-\infty}x[n]z^{-n}$﻿

ZT에서 ROC는 $x[n]r^{-n}$﻿가 converge한 범위를 말합니다. 여기서 $z$﻿의 coordinate가 angular로 나타나므로, 범위는 원 모양으로 나타납니다.

## ROC

ROC는 원 모양으로 나타납니다. pole과 zero는 위의 LT와 같습니다.

- right sided signal은 pole의 오른쪽, left sided signal은 pole의 왼쪽으로 나타납니다.
- ROC에 unit circle이 포함되지 않으면 DTFT가 존재하지 않습니다.

> Property 1: The ROC of X(z) consists of a ring in the z-plane centered about the origin.

- ROC는 늘 중심이 원점

> Property 2: The ROC dose not contain any poles

- ROC가 pole을 포함한다면 infinity로 갑니다.

> Property 3: IF x[n] is of finite duration, then the ROC is the entire z-plane, except possibly z=0 and/or z=infty

- 그러면 $x[n]r^{-1}$﻿이 무조건 converge하므로 z=0이거나 z=\infty가 아닌 이상 무조건 성립합니다.

> Property 4: If x[n] is right/left/two sided, 원의 모양이 어쩌구… 저쩌구…

![[Screenshot_2023-11-20_at_5.18.37_PM.png]]

## Inverse Z Transform

![[Screenshot_2023-11-20_at_5.22.32_PM.png]]

이것도 라플라스와 마찬가지로 내가 아는 형태로 바꾼 뒤 변환하는 게 중요

그리고 ROC의 범위도 잘 생각해서 변환해야 합니다.

![[Screenshot_2023-12-14_at_12.19.43_AM.png]]

## Properties of the z-transform

![[Screenshot_2023-11-29_at_6.55.11_PM.png]]

- ROC를 조심하자

![[Screenshot_2023-11-29_at_6.55.31_PM.png]]

![[Screenshot_2023-11-29_at_6.55.43_PM.png]]

![[Screenshot_2023-11-29_at_6.56.02_PM.png]]

## Example

![[Screenshot_2023-11-29_at_6.56.16_PM.png]]

![[Screenshot_2023-11-29_at_6.56.25_PM.png]]

## Analyis and characterization of LTI systems using ZT

![[Screenshot_2023-11-29_at_6.56.54_PM.png]]

![[Screenshot_2023-11-29_at_6.58.04_PM.png]]

![[Screenshot_2023-11-29_at_6.58.12_PM.png]]

![[Screenshot_2023-11-29_at_7.00.32_PM.png]]

### example 10.29

![[Screenshot_2023-11-29_at_7.00.43_PM.png]]

- 시스템을 여러개로 나눠서 생각하기
- 전달함수 시스템 설계하기

### example 10.30

![[Screenshot_2023-11-29_at_7.02.05_PM.png]]

## Unilateral z-tranform

![[Screenshot_2023-11-29_at_7.02.33_PM.png]]

- 일반 z-transform과 달리 0부터 무한까지 더하는 것

![[Screenshot_2023-11-29_at_7.03.54_PM.png]]