---
Created: 2023-10-03T15:24
Parent item:
  - "[[Applications of Diode]]"
---
## Half-Wave Rectifier

![[Screenshot_2023-10-03_at_3.00.50_PM.png]]

diode의 특성을 이용해 AC Wave의 한쪽은 날려버릴 수 있지만, constant한 output을 만들어 낼 수는 없습니다. 좋은 방법이 있을까요?

## Diode-Capacitor Circuit: CV Model

![[Screenshot_2023-10-03_at_3.06.28_PM.png]]

위의 회로에서 저항을 ==capacitor==로 바꾼다면, constant output을 만들 수 있습니다!

capacitor는 전압이 연결되면 전류가 흐름에 따라 전기 에너지를 저장하는 특성을 가지고 있습니다.

$V_{in}>V_{D,on}$﻿일 때는 capacitor가 충전되다가, $V_p$﻿(peek voltage)에 도달하면 충전이 모두 끝나 fully charged 상태가 됩니다.

전압이 $V_{D,on}$﻿아래로 떨어져도 Diode가 off 되었을 때 회로는 open 상태가 되므로, capacitor에 저장된 전기 에너지가 사용되지는 않습니다. 따라서 ==output voltage가 constant 상태==가 됩니다!

하지만 이 charger에 다른 기기를 연결하면 문제가 발생합니다.

바로 그 기기가 ==Load Resistor==가 되기 때문입니다!

## Diode-Capacitor With Load Resistor

![[Screenshot_2023-10-03_at_3.08.38_PM.png]]

실제 회로에서는 저항(Load Resistor)이 fully charged 된 capacitor의 전기 에너지를 뽑아먹습니다. 따라서 그래프의 모습이 위와 같이 변합니다.

이렇게 저항에 낭비된 전압을 ==Ripple==이라고 합니다.

## Peak to Peak amplitude of Ripple

직접 Ripple의 값을 계산해봅시다.

$V_{out}$﻿의 값은 peak voltage에서 decaying합니다.

> $V_{out}(t)=(V_p-V_{D,on})\exp{-t \over R_LC_1}$﻿

Linear approximation을 위해 Taylor Series를 사용합니다. $t$﻿가 매우 작다고 가정합시다.

> $V_{out}(t)\approx(V_p-V_{D,on})(1-{t \over R_LC_1}) \approx (V_p-V_{D,on}) - {V_p-V_{D,on} \over R_L}{t \over C_1}$﻿

뒤의 term이 바로 시간 $t$﻿에 따른 output voltage loss, Ripple입니다. 대충 주기를 기준으로 decay한다고 가정해봅시다.

> $V_R\approx {V_p-V_{D,on} \over R_L}\cdot {T_{in}\over C_1}\approx {V_p-V_{D,on} \over R_L C_1 f_{in}} $﻿

그럼 Ripple을 줄일 수 있는 방법이 좀 명확해졌죠?

## Different Capacitor Values or…

모두 위의 Ripple 식에서 기인합니다.

1. Use high capacitance
2. Use high input Frequency
3. Use Large Load Resistance
4. or Use Fully wave rectifier! = Use Half Period