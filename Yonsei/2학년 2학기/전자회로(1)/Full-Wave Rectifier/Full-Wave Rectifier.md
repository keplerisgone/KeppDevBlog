---
Created: 2023-10-03T15:24
Parent item:
  - "[[Applications of Diode]]"
---
## Full-Wave Rectifier

![[Screenshot_2023-10-03_at_3.27.29_PM.png]]

==AC wave를 한쪽으로 모두 몰아주는 회로==입니다.

Period를 절반으로 줄여 Ripple을 절반으로 줄이는 효과가 있습니다. 물론 Full-wave rectifier의 output을 또 CV model에 연결시켜야 합니다.

## Bridge Rectifier

![[Screenshot_2023-10-03_at_3.29.41_PM.png]]

가장 단순한 모델은 다음과 같습니다. 전압의 전위에 따라 전류의 방향을 바꿔 $V_{out}$﻿를 만듭니다. 다이오드의 성질을 이용합니다.

## Complete Full-Wave Rectifier

![[Screenshot_2023-10-03_at_3.35.26_PM.png]]

Diode-capacitor 회로에 연결하면 Ripple이 생기지만, Full-wave rectifier에 의해 주기가 절반으로 줄어드므로 Ripple또한 절반으로 줄어듭니다! 다만 $V_{out}$﻿이 $V_{in}-2V_{D,on}$﻿으로 바뀐 것에 유의합시다.