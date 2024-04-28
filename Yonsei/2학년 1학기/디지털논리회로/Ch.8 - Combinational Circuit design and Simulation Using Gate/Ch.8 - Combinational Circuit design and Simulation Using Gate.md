---
Created: 2023-08-24T14:54
---
### 8.1 Review of Combinational Circuit design

특정 회로를 디자인하는 방법은 다음과 같습니다.

1. 변수가 무엇인지, 몇 개인지 정한다.
2. 변수에 따른 결과를 진리표로 정리한다.
3. 진리표의 결과를 Quine를 쓰던지 카르노맵을 쓰던지 해서 간단히 한다
4. 회로를 구성한다!

### 8.2 Design of dirduits with Limited Gate Fan-in

- 회로를 디자인 하되, limited input, gate에 유의할 것

회로를 디자인할 때, 사용하는 게이트의 종류에 따라 인풋의 개수가 제한되어 있을 수도 있습니다.

만약 세 가지의 함수를 하나의 회로로 표현한다고 했을 때, 간단한 회로를 만드는 가장 좋은 방법은 공통된 인수를 찾는 것입니다. 다음과 같은 예시를 생각해봅시다.

![[Media/Screenshot_2023-08-24_at_3.05.02_PM 2.png|Screenshot_2023-08-24_at_3.05.02_PM 2.png]]

two-input NAND gate만을 이용해 회로를 구성한다고 생각해봅시다. 표현식을 간단히 해 공통된 인풋을 찾아봅시다.

![[Media/Screenshot_2023-08-24_at_3.06.20_PM 2.png|Screenshot_2023-08-24_at_3.06.20_PM 2.png]]

이를 묶어서 넣은 뒤, 마지막으로 OR-AND-OR 게이트를 NAND로 변환해줍니다.

### 8.3 gate delays and Timing Diagrams

- Propagation delay : 게이트를 통과할 때 값이 변하는 시간

모든 게이트들이 값을 넣은대로 바로 결과를 출력하는 것은 아닙니다. 내부에서 연산할 시간이 필요합니다. 이러한 딜레이를 `Propagation delay` 라고 합니다. 다음은 인버터에서의 딜레이입니다.

![[Media/Screenshot_2023-08-24_at_3.08.32_PM 2.png|Screenshot_2023-08-24_at_3.08.32_PM 2.png]]

이 때문에 원하는 시간에 원하는 결과가 나오지 않을 수도 있습니다. 이를 방지하기 위해서는 딜레이를 계산해 회로를 설계해야합니다. 주로 `Timing Diagram` 을 그려 계산하는 편입니다.

![[Media/Screenshot_2023-08-24_at_3.09.49_PM 2.png|Screenshot_2023-08-24_at_3.09.49_PM 2.png]]

### 8.4 Hazards in Combinational Logic

- 갑자기 원하지 않는 결과가 나옵니다
    - static 1-hazard = 갑자기 0
    - static 0-hazard = 갑자기 1
    - dynamic hazard
- Propagation delay 때문
- 중간에 combination을 하나 더 연결해주면 해결
    - 연결시킬 수 있는 건 전부 연결
- prime implicant에서 연결되지 않은 0과 1이 hazard를 일으킨다

딜레이로 인해 회로에서 원하는 결과가 나오지 않을 수도 있습니다. 이를 `Hazard` 라고 합니다. 결과가 나오는 모양에 따라 다음과 같은 네 가지로 나뉩니다.

![[Media/Screenshot_2023-08-24_at_3.11.37_PM 2.png|Screenshot_2023-08-24_at_3.11.37_PM 2.png]]

카르노맵을 이용해 존재하는 하자드를 찾을 수 있습니다. 카르노맵 상에서 연결되지 않은 항은 하자드를 일으킵니다. 이 때 해당 하자드를 연결해주는 항을 추가한다면 하자드 발생을 막을 수 있습니다.

![[Media/Screenshot_2023-08-24_at_3.24.09_PM 2.png|Screenshot_2023-08-24_at_3.24.09_PM 2.png]]

### 8.5 Simulation and Testing Logic Circuits

이제 디자인한 회로를 점검해봅시다. 시뮬레이션은 다음과 같이 진행합니다.

1. 입력값에 따른 결과가 진리표와 맞는지 확인합시다.
2. 끝!