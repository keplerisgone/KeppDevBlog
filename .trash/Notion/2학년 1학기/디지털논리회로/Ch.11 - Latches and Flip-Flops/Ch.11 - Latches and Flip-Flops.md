---
Created: 2023-08-24T15:37
---
### 11.2 Set-Reset Latch

![[Media/Untitled 16.png|Untitled 16.png]]

![[Media/Untitled 1 9.png|Untitled 1 9.png]]

- S와 R의 값에 따라 Q의 값이 연속해서 변하는 Latch를 말합니다.
- 위와 같이 다양한 형태로 나타낼 수 있습니다.
- table은 니가 알아서 작성하십시오. 다만 S=R=1 인 경우는 제한되어 있습니다.
- S, R이 입력될 때 Debouncing이 일어날 수도 있습니다.
- NAND 를 사용하는 S-R latch도 있습니다.
- reset/set-dominant latch도 있습니다. 이때는 S=R=1일 때 정의된 값으로 Q가 변합니다.
- $Q^+=S+R'Q$﻿

### 11.3 Gated D Latch

![[Media/Untitled 2 9.png|Untitled 2 9.png]]

- G가 열려있을 때(1일때), 다음 Q값은 D의 값으로 변하는 Latch입니다.
- 위와 같이 다양한 형태가 있습니다. FF에서는 G가 EN으로 표현됩니다.
- 별개로 D gate는 어느 Latch에나 달 수 있는데, 이 때는 D=1 일 때만 해당 Latch가 동작한다고 보시면 됩니다. Gated S-R latch도 있어요.

### 11.4 Edge-Triggered D Flip-Flop

![[Media/Untitled 3 8.png|Untitled 3 8.png]]

- Edge-trggered 이면 clock을 사용하는 FF를 뜻합니다.
- CLK에 연결돼있는 버블의 유무에 따라 rising-edge triggered / falling-edge triggered로 나뉩니다.
- 올라갈 때 작동하냐/내려갈 때 작동되냐의 차이가 있습니다.
- 그냥 CLK이 있는 D 처럼 작동합니다.

![[Media/Untitled 4 6.png|Untitled 4 6.png]]

- setup time - FF가 작동하기 전에 준비하는 시간을 말합니다.
- hold time - propagation delay 동안 이전 input이 유지되는 시간을 말합니다. 대개 propagation delay와 값이 같습니다.
- minimum Clk period는 setup time + (hold time) + propagation delay입니다.
- minimum clk time은 이걸 모두 더한다? propagation + setup 이면 충분

### 11.5 S-R Flip-Flop

![[Media/Untitled 5 5.png|Untitled 5 5.png]]

- S-R처럼 동작하지만 Clk에 의해서 동작하는 FF를 말합니다.

### 11.6 J-K Flip-Flop

![[Media/Untitled 6 5.png|Untitled 6 5.png]]

- J는 set, K는 reset 처럼 동작하지만 J=K=1 일 때 Q가 switch 되는 FF입니다.
- S-R FF 두개를 이용해 Master-Slave J-K FF를 만들 수 있습니다.
    
    ![[Screenshot_2023-08-25_at_1.55.27_AM.png]]
    
- $Q^+=JQ'+K'Q$﻿

### 11.7 T Flip-Flop

![[Media/Untitled 7 4.png|Untitled 7 4.png]]

- T가 1이면 Q가 switching되는 FF입니다.
- $Q^+=T'Q+TQ'=T \oplus Q$﻿

### 11.8 Flip-Flops with Additional Inputs

![[Media/Untitled 8 3.png|Untitled 8 3.png]]

- ClrN은 Clear N으로, 0일 때 _Clock과 다른 input에 관계없이_ Q를 0으로 만듭니다.
- PreN은 Preset N으로, 0일 때 Q를 1로 만듭니다.
- 위처럼 다양한 방식으로 표현될 수 있습니다.

### 11.9 Asynchronous Sequential Circuits

비동기는 언제나 인풋의 변화를 기다리는 것을 뜻합니다. 이러한 특성 때문에 항상 몇가지 제약 사항을 두고 디자인 되어야 합니다.

비동기 회로는 값을 받는 즉시 연산을 처리합니다. 딜레이는 어떻게 처리하냐구요? 하자드는 어떻게 해결하냐구요? 사실 각종 게이트에 딜레이가 존재하는 한 문제를 완벽하게 해결할 방법은 없습니다.

동기회로는 위에서 배운 클락을 사용하는 회로로, _원하는 타이밍에 값이 바뀌게 함으로서_ 나타날 수 있는 오류를 해결하는 회로입니다. 클락의 값이 변하는 타이밍을 우리가 설정할 수 있으니, 딜레이도 계산해서 해결할 수 있죠. 현대 대부분의 기계는 동기 회로를 사용합니다.