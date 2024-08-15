---
Created: 2023-09-11T21:38
Parent item:
  - "[[Signals and Systems]]"
---
1.1 Continuous-time and Discrete-time signals

Signals Energy and Power

Three classes of signals

## 1.1 Continuous-time and Discrete-time signals

![[Screenshot_2023-09-06_at_7.58.24_PM.png]]

- signal : 정보를 담고 있는 일종의 함수
    
    - 우리는 시간에 대한 함수로 배운다
    - Countinuous-time(CT): 시간, amplitude 면에서 연속적, Analog로 불리는 것
        
        ![[Screenshot_2023-09-06_at_7.58.56_PM.png]]
        
    - Discrete-time(DT) : 시간에 대해서 불연속, amplitude 면에서는 연속. CT를 샘플링하여 얻어집니다.
        
        - Sampling Interval Time($T_s)$﻿ : 불연속 처리하는 시간 간격. DT에서는 Index가 됩니다만, 이는 위치 정보(순서) + 시간의 정보를 모두 담고 있습니다.
        - x축이 시간이 아니야! 인덱스입니다.
        
        ![[Screenshot_2023-09-06_at_7.59.57_PM.png]]
        
    - Digital: 시간, amplitude 면에서 모두 불연속, DT를 Quantization 하여 얻어집니다.
    
    > [!important]  
    > 근데 왜 변형하나요?담고 있는 정보의 전체적인 내용을 변하게 하지 않으면서 용량을 줄이고, 오류의 감지를 쉽게 합니다.5.1 → 5, 3.7 → 3 이 훨씬 쉽잖아요  
    

### Signals Energy and Power

- 에너지는 “각 시간/인덱스의 함수를 제곱해서 적분한 것”, 평균적인 파워는 이를 시간/인덱스의 간격으로 나눈 것입니다.
- 수학적인 의미는 나중에 배웁니다.

![[Screenshot_2023-09-06_at_8.06.21_PM.png]]

### Three classes of signals

- Finite total energy: $E_\infty<\infty$﻿ → average power가 0입니다.
- Finite average power: $P_\infty<\infty$﻿
- Nonfinite average power and energy: $x(t)=t$﻿ 같은 경우

$E_\infty$﻿

![[Screenshot_2023-10-10_at_1.09.14_AM.png]]

![[Screenshot_2023-10-10_at_1.09.25_AM.png]]

$P_\infty$﻿

![[Screenshot_2023-10-10_at_1.10.33_AM.png]]

  

---