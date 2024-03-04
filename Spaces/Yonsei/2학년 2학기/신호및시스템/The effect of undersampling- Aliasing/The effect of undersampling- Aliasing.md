---
Created: 2023-11-13T18:05
Parent item:
  - "[[Sampling]]"
---
만약 sampling freq가 sampling theorem을 만족하지 못한다면 신호가 다시 돌아올 수 없게 되는데 (=손실이 일어나는데) 이를 aliasing이라고 합니다.

![[Screenshot_2023-11-14_at_12.01.18_AM.png]]

> [!important]  
> 이거 위치가 뒤바뀐게 아니라 FT cos signal이 벌어져서 위치 바뀐거처럼 보이는 거임  

sin wave의 경우는 다음과 같이 aliasing이 일어난다

![[Screenshot_2023-11-14_at_12.02.53_AM.png]]

- nyquist freq는 $f_s=2f_n$﻿ 일 때, 물론 이게 충분하지 않은 경우도 많기에 $w_s>2w_0$﻿ 으로 표기하는 것
    - cos 같은 경우는 0이 되어버린다

![[Screenshot_2023-11-14_at_12.04.20_AM.png]]