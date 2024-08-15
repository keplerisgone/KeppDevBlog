---
Created: 2023-10-03T15:35
Parent item:
  - "[[Applications of Diode]]"
---
## Limiting Circuits

![[Screenshot_2023-10-03_at_3.36.47_PM.png]]

이를 사용하는 이유는 과하게 큰 신호에 의한 기기의 손상을 방지하기 위함입니다!

![[Screenshot_2023-10-03_at_3.37.31_PM.png]]

input voltage를 clipping 하는 기능을 가지고 있습니다.

우선 한 쪽으로만 clipping을 하는 회로를 살펴봅시다.

![[Screenshot_2023-10-03_at_7.37.02_PM.png]]

diode가 on인 경우에 $V_{out}=V_{D,on}$﻿이 되고, diode가 off인 경우에는 $V_{out} = V_{in}$﻿이 되는 것이 핵심입니다. 이는 positive과 negative 둘에서 모두 성립합니다.

![[Screenshot_2023-10-03_at_7.42.26_PM.png]]

방향이 다른 두 다이오드를 병렬로 연결하면 두 곳에서 모두 clipping이 일어나는 회로가 됩니다. 이를 ==combination clipper==라고 합니다.

다음과 같은 방법을 통해 $V_p$﻿의 크기를 늘릴 수 있습니다.

1. $V_{D,on}$﻿이 높은 다른 물질 사용하기
2. 다이오드를 여러 개 연결하기 → 개수만큼 $V_{D,on}$﻿이 오릅니다.
3. 배터리를 연결하기 → 배터리의 전압만큼 오릅니다.