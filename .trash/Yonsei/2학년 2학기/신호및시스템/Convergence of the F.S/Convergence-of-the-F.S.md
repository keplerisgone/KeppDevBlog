---
Created: 2023-10-04T22:51
Parent item:
  - "[[Fourier Series Representation of Periodic Signals]]"
---
## Validity of F.S.

FS는 정말 해당 신호를 잘 나타낼까요?

이를 알아보기 위해서는 우선 FS의 Finite Sum을 나타낸 뒤, Error size를 integral을 통해 나타내 확인해봅시다.

![[Screenshot_2023-10-04_at_10.55.34_PM.png]]

이 때 Error size를 minimize하는 것이 바로 FS의 coefficient인 것을 확인할 수 있습니다.

## Convergence of *

이제 위의 *이 항상 converge인지 생각해봅시다.

### Dirichlet conditions

1. $x(t)$﻿가 integrable할 것
2. $x(t)$﻿가 bounded variation에 있을 것> [!important]  
    > 유계변동함수가 뭘까요…That is, there are no more than a finite number of maxima and minima suting any single period of the signal이라는데  
    
3. $x(t)$﻿의 불연속점이 유한개일 것