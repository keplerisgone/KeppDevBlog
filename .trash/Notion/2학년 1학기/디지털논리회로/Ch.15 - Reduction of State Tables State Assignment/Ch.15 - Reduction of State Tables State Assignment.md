---
Created: 2023-08-25T20:24
---
### 15.1 Elimination of Redundant States

State table을 작성하다보면, _겉은 다른데 사실 같은 상태를 표현하는 것들_이 있을 때가 있습니다. 다음과 같은 예시를 봅시다.

![[Screenshot_2023-08-25_at_8.27.29_PM.png]]

위는 0101, 1001을 골라내는 detector입니다. A를 리셋 상태로 설정해놓은 상태입니다.

중복되는 상태는

1. Next State가 같은가?
2. Output이 동일한가?

를 기준으로 결정합니다. 위의 table을 기준으로 하면 $H\equiv I \equiv K \equiv M \equiv N \equiv P$﻿… 처럼 계속 지워나가면 됩니다.

### 15.2 Equivalent States

완전히 동일한 상태, Equivalent state의 정확한 정의는 다음과 같습니다.

상태 $p,q$﻿에서 어떠한 인풋 시퀀스 $X$﻿를 넣었을 때 둘 모두에서 동일한 결과 시퀀스 $Z$﻿가 나온다면 두 상태는 동일합니다. 수식으로 표현하면 다음과 같습니다.

$\lambda(p,X) = \lambda(q,X), \ \delta(p,X)\equiv \delta(q,X)$﻿ 이면 $p\equiv q$﻿ 이다.

### 15.3 Determination of State Equivalence Using an Implication Table

위처럼 귀찮게 비교하는 것 말고도, Implication Table을 이용해 Equivalent state인지 확인할 수 있는 방법이 있습니다. 일종의 귀류법입니다.

1. 우선 output이 같은 것끼리 next state를 짝짓습니다.
2. _이건 같을 수가 없다_ 하는 것을 지워줍시다.
3. 1~2를 끝까지 반복합니다.
4. 남은 것이 equivalent state입니다.

![[Screenshot_2023-08-25_at_8.40.16_PM.png]]

### 15.4 Equivalent Sequential Circuits

state 말고도 circuit 또한 완벽하게 같은 것이 존재할 수 있습니다.

equivalent sequential circuit일 조건은 한 순차회로 $N_1$﻿의 모든 state에 대해 equivalent한 state가 $N_2$﻿에 있으면, 두 회로는 같습니다. 이 때도 Implication table을 작성하듯이 각각의 equivalent state를 구할 수 있습니다.

![[Screenshot_2023-08-25_at_8.44.56_PM.png]]

### 15.5 Reducing Incompletely Specified State Tables

Incompletely specified state tables에서는 같은 상태를 어떻게 찾아낼 수 있을까요?

1. don’t care 에 0과 1을 모두 집어넣어보고 가장 간단한 것으로 결정한다 ← 귀찮습니다
2. don’t care를 두 개로 분할한다
3. 그냥 뭐든지 될 수 있다고 생각해서 Implication table에 집어넣는다
4. 통짜로 reduced table 작성하기. ← 상태를 _연달아서_ 생각하는 방식입니다.

아래는 각각 방법의 예시입니다.

![[Screenshot_2023-08-25_at_8.48.49_PM.png]]

![[Screenshot_2023-08-25_at_8.48.55_PM.png]]

![[Screenshot_2023-08-25_at_8.49.21_PM.png]]

### 15.6 Derivation of Flip-Flop Input Equations

1. reduced table을 이용해 지난 챕터에서 했던 것처럼 각 상태에 FF 값 할당하기 ($S_0 = 00$﻿ 처럼)
2. 할당한 값을 이용해 Trasition table 작성
3. 카르노맵 이용, 간단한 형태 찾기
4. 회로를 그리렴!

### 15.7 Equivalent State Assignments

사실 각 상태에 순서대로 $00, 01, 10, 11$﻿… 을 할당하는 것보다 더 효율적으로 회로를 만들기 위해서, 다양한 경우의 수를 시도해봐야 합니다.

일단 _위치가 바뀌거나_($01=10)$﻿ _상태끼리 바꿀 수 있을 경우_($S_0=00,S_1=01$﻿과 $S_0=01,S_1=00$﻿) 는 같은 것으로 취급합니다. 이러한 규칙에 따라 모든 경우의 수를 찾아봅시다.

### 15.8 Guidelines for State Assignment

해당 가이드라인을 따라 할당하면 웬만하면 잘 됩니다.

1. 한 인풋에 대한 같은 next state를 가지고 있는 state의 경우는 연속적인 값을 할당받습니다.
2. 모든 인풋에 대해 같은 next state를 가지고 있는 state의 경우는 연속적인 값을 할당받습니다.
3. 같은 결과값을 같는 경우도 될 수 있으면 연속적인 값을 할당합니다.

![[Screenshot_2023-08-25_at_9.05.53_PM.png]]

### 15.9 Using a One-Hot State Assignment

One-Hot state assignment는 상태의 개수만큼 FF를 사용해 상태를 나타내는 방법입니다. 예를 들어, $S_0$﻿인 경우 $0001$﻿을, $S_1$﻿인 경우 $0010$﻿을 사용합니다.

상태를 할당하는 과정이 복잡하지만, 이후 인풋에 따른 상태와 아웃풋의 표현식을 나타내는 과정이 훨씬 간단해집니다.

이런게 있다~ 정도만 알아놓으면 좋습니다.