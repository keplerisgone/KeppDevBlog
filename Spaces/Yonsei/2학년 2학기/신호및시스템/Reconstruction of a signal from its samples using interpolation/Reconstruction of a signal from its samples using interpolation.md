---
Created: 2023-11-13T17:37
Parent item:
  - "[[Sampling]]"
---
## Interpolation

CT signal의 각 지점을 특정 차수의 함수로 연결해 approximation하는 방법입니다.

일차함수로 진행하는 경우는 linear interpolation (first-order hold) 라고합니다.

![[Screenshot_2023-11-13_at_5.48.00_PM.png]]

## Band-limited Interpolation

band-limited로 interpolation한 함수를 reconstruction하기 위해서는 LPF에 통과시켜야 합니다. 이를 식으로 표현하면 다음과 같습니다.

![[Screenshot_2023-11-13_at_5.56.59_PM.png]]

impulse의 FT는 sinc모양으로 나타나므로, 실제 신호는 이 sinc들의 무한 sum으로 나타납니다.

## Approximation

> [!important]  
> 뭔가 교수님이 반복해서 approximation해가지고 ideal 이랑 비슷하게 만든다고 하셨던 거 같은데  

![[Screenshot_2023-11-13_at_6.11.01_PM.png]]

참고로 오른쪽 맨 아래에 있는 건 zero-order hold의 전달 함수와 ideal LPF을 비교하는 사진입니다.