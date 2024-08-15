---
Created: 2023-08-25T02:44
---
### 13.1 A Sequential Parity Checker

바이너리 데이터가 저장될 때, 예기치 않은 오류가 발생해 각각의 비트가 바뀔 수 있습니다. 이런 오류를 감지하기 위한 추가적인 비트를 `parity bit` 라고 합니다.

![[Media/Screenshot_2023-08-25_at_2.48.18_AM 2.png|Screenshot_2023-08-25_at_2.48.18_AM 2.png]]

전체 데이터를 8bit 라고 할 때, 앞의 일곱 개 비트는 데이터를 담고, 가장 뒤의 parity bit 는 오류를 체크하는 역할을 합니다. 가장 많이 사용하는 방법은 _비트 중에 1이 홀수/짝수 개만큼 있습니다. 아니라구요? 엥?_ 입니다.

Parity Checker 를 이용해 데이터를 통과시킨 후, 포함된 0/1의 개수에 따라 Parity bit인 Z를 내보냅니다. 사용자는 자신이 넣은 값과 결과값을 이용해 오류의 발생 여부를 알 수 있습니다.

State graph 를 이용해 디자인 해봅시다.

![[Media/Screenshot_2023-08-25_at_2.55.32_AM 2.png|Screenshot_2023-08-25_at_2.55.32_AM 2.png]]

위는 1/0의 개수에 따른 상태입니다. 인풋에 따라 상태가 달라짐을 알 수 있습니다.

### 13.2 Analysis by Signal Tracing and Timing Charts

sequential circuit을 디자인하기 위해서는 _어떤 상태에서, 어떤 입력값에 따라 어떤 결과가 나오는지_를 아는 것이 가장 중요합니다. 이를 쉽게 찾는 방법은 다음과 같습니다.

1. FF의 initial state를 추정해봅시다. 시작 값이 정해져 있지 않다면 모두 0으로 세팅합시다.
2. 입력값에 따른 다음 출력값과 FF 입력값을 정합니다.
3. 다음 상태에 대해서 반복합니다.
4. 모든 상태에 대해서 반복합니다.

그리고 출력값이 상태에만 의존하는 회로를 `Moore circuit` 이라고 하고, 출력값이 상태와 입력값에 의해 바뀌는 회로를 `Mealy circuit` 이라고 합니다. 아래의 회로는 Moore circuit 입니다. 출력값인 Z가 상태를 나타내는 AB에만 의해 결정됨을 알 수 있습니다.

![[Media/Screenshot_2023-08-25_at_3.56.35_PM 2.png|Screenshot_2023-08-25_at_3.56.35_PM 2.png]]

이제 timing chart를 작성해봅시다. 인풋의 변화에 따른 상태와 출력의 변화를 알기 위해 작성합니다. Moore circuit의 경우는 출력값이 _인풋값의 변화_에 의해 바뀝니다. 따라서, 처음 initial state는 _인풋값에 의한 출력이 아니므로_ 고려되지 않습니다. 아래의 차트에서 Z의 첫 0에 괄호가 쳐져있는 이유가 바로 이것입니다.

![[Media/Screenshot_2023-08-25_at_4.00.07_PM 2.png|Screenshot_2023-08-25_at_4.00.07_PM 2.png]]

반대로 Mealy circuit은 _인풋과 상태가 모두 결과에 영향을 미치기 때문에_ 출력값을 인풋, 상태 바로 아래에 적습니다. 하지만 _인풋이 상태에 미치는 영향_과 클락에 의해 상태가 변하는 타이밍이 맞지 않을 때 False output이 발생할 수 있습니다.

![[Media/Screenshot_2023-08-25_at_4.04.07_PM 2.png|Screenshot_2023-08-25_at_4.04.07_PM 2.png]]

### 13.3 State Tables and Graphs

State Table은 Transition table을 단순히 상태로 나타낸 것입니다. 만약 transition table의 상태가 $00, 01, 10, 11$﻿으로 나타났다면, 네 개의 상태를 $S_0,S_1, S_2, S_3$﻿ 으로 나타낼 수 있습니다.

![[Media/Screenshot_2023-08-25_at_4.10.27_PM 2.png|Screenshot_2023-08-25_at_4.10.27_PM 2.png]]

이를 그림으로 나타내면 State Graph가 됩니다. 아래와 같이 생겼습니다.

![[Media/Screenshot_2023-08-25_at_4.11.16_PM 2.png|Screenshot_2023-08-25_at_4.11.16_PM 2.png]]

위의 예시는 모두 Moore circuit입니다. Mealy circuit은 위에 더해 출력값까지 고려해야 합니다. 어떤 상태에서 어떤 인풋을 넣어야 어떤 결과가 나오는지 모두 알아야 하거든요!

![[Media/Screenshot_2023-08-25_at_4.13.02_PM 2.png|Screenshot_2023-08-25_at_4.13.02_PM 2.png]]

### 13.4 General Models for Sequential Circuits

sequential circuit은 FF가 데이터를 전달하는 부분과 해당 데이터를 이용해 결과를 출력하는 부분으로 나눌 수 있습니다. _결과를 출력하는 부분_은 ROM이 될 수도 있고, PLA가 올 수도 있습니다. Mealy circuit의 가장 기본적인 모델은 다음과 같습니다.

![[Media/Screenshot_2023-08-25_at_4.18.53_PM 2.png|Screenshot_2023-08-25_at_4.18.53_PM 2.png]]

그리고 next state를 나타내는 함수는 $\delta (S,X)$﻿로, output을 나타내는 함수는 $\lambda (S,X)$﻿로 나타냅니다. 다음 처럼 말이죠.

![[Media/Screenshot_2023-08-25_at_4.23.01_PM 2.png|Screenshot_2023-08-25_at_4.23.01_PM 2.png]]