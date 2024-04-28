---
Created: 2023-10-04T19:15
Parent item:
  - "[[Bipolar transistors]]"
---
## Transistors

![[Screenshot_2023-10-04_at_7.29.59_PM.png]]

==Transistor==는 Transfer Resistor의 준말로, 저항의 값을 자유롭게 바꿀 수 있는 소자입니다. (Dynamic resistance)

또한 Current-controlled current source혹은 voltage-controlled current source이기도 합니다.

analog circuit에서는 amplifiers의 역할을 하고, digital circuit에서는 inverters의 역할을 합니다.

세 개의 터미널로 current flow를 조작하는 non-linear한 소자입니다.

### Functions of Transistors

- Switching for storing and moving Data
- Amplifications
- Miniaturization
- Efficiency = consuming a very little power
- Rugged = Widthstanding shock and vibration

## Voltage-Dependent Current Source

![[Screenshot_2023-10-04_at_7.48.17_PM.png]]

외부 전압 $V_{in}$﻿에 따라 전류를 공급하는 dependent current source를 연결하면, 저항 $R_L$﻿에 걸리는 전압 $V_{out}$﻿은 다음과 같이 계산할 수 있습니다.

> $V_{out} = -KV_{in}R_L$﻿

여기서 $V_{out}$﻿과 $V_{in}$﻿의 비율을 voltage gain이라고 하며, 다음과 같이 계산할 수 있습니다.

> $A_V= {V_{out}\over V_{in}}=-KR_L$﻿

결론적으로, 해당 dependent current source는 $K>1$﻿일 경우 voltage를 증폭시키는 역할을 수행합니다.

> [!important]  
> @import url('https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.css')KKK﻿는 transconductance라고 하는데, dynamic resistance의 역수 관계를 가지고 있습니다.