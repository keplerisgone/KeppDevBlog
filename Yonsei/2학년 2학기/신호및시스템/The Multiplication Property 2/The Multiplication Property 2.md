---
Created: 2023-10-30T18:25
Parent item:
  - "[[The Continuous-tIme Fourer Transform]]"
---
time-domain과 frequncy-domain 사이에는 convolution과 multiplication로 전환이 가능한 점을 기억해둡시다.

마찬가지로 time-domain에서의 곱을 frequncy-domain에서의 convolution으로 정의할 수 있고, 식은 다음과 같습니다.

![[Screenshot_2023-10-30_at_6.28.10_PM.png]]

이를 ==Modulation==이라고 합니다.

Modulation은 신호를 특정 주파수 대역으로 보내는데 이용됩니다.

역으로 Demodulation을 사용하기도 하는데, 이는 다시 원래 주파수 대역으로 보낸 뒤 LPF를 이용해 원래 신호를 복원하는 것을 말합니다.

![[Screenshot_2023-10-30_at_6.30.10_PM.png]]

## Frequency selective filtering with variable freq.

신호의 특정 부분을 자르는 필터입니다.

![[Screenshot_2023-10-30_at_6.34.26_PM.png]]

shift property를 이용해 신호를 자르고 싶은 곳에 위치시킨 뒤rectangular signal에 통과시킨 뒤에 shift property를 이용해 다시 원래 자리로 움직입니다.

> [!important]  
> 그렇다면 잘려져 있는 cos 신호를 FT로 나타내면? ![[Screenshot_2023-10-30_at_6.40.51_PM.png]]