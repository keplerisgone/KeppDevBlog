---
Created: 2023-10-31T21:30
---
## Emitter Degeneration

Emitter에 저항을 달아 emitter current를 degrade 시키는 방식입니다.

> [!important]  
> 정확한 의미는 @import url('https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.css')VXV_XVX​﻿에서 발생할 수 있는 error (@import url('https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.css')R1,R2,VCCR_1, R_2, V_{CC}R1​,R2​,VCC​﻿에 의한)를 @import url('https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.css')RER_ERE​﻿가 흡수하는 방식입니다.  

gain은 줄어들지만 input impedance를 증가시킨다던가, linearity를 만든다던가 하는 장점이 있습니다.

그리고 가장 중요한 것으로 temperature에 대한 sensitivity를 줄입니다. ($V_{BE}$﻿)

![[Screenshot_2023-10-31_at_9.35.34_PM.png]]

> [!important]  
> 왜 저항을 달아주는 것만으로도 저런 이점을 가질 수 있나요?![[Screenshot_2023-10-31_at_10.56.03_PM.png]]이렇다는데요.원래 @import url('https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.css')RER_ERE​﻿가 0일 경우는… Base voltage가 증가하면 @import url('https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.css')VBEV_{BE}VBE​﻿도 같이 증가해서 collector current도 같이 증가하지만, @import url('https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.css')RER_ERE​﻿가 있을 경우는 그것보단 적게 증가하기 때문에 변화에 덜 민감해집니다.  

## Voltage Amplifier

이렇게 degenerated된 amplifier는 gain이 다음과 같이 계산됩니다.

![[Screenshot_2023-10-31_at_9.38.10_PM.png]]

$R_{in}$﻿에 $R_E(1+\beta)$﻿ term이 더 추가된 것을 볼 수 있습니다. input impedance가 정말 커진거죠!

output impedance의 변화는 없습니다. 여전히 $R_C$﻿입니다.

voltage gain은 $-R_C/(1/g_m+R_E)$﻿로 변화합니다. 좀 줄지 않았어요??

그리고 해당 모델에서는 외부에 연결된 transistor를 하나의 저항으로 취급할 수 있습니다.

> [!important]  
> 저항으로 취급할 수 있는 근거는?그냥 input/output이 저기 트랜지스터에 붙어있기 때문에 simplify를 위해서 바꾼거래요  
  
> [!important]  
> 저거 결과값이 적당한 approximation에 의한 것임을 잊지 맙시다실제로는 @import url('https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.css')1/rπ1/r_\pi1/rπ​﻿ term이 붙어있음  

## Degenerated CE Stage as a Black Box

$A_v$﻿은 Transistor에만 해당하는 voltage gain입니다.

모든 circuit에 대해 통용되는 gain인 $G_m$﻿을 생각해봅시다. $G_m$﻿은 다음과 같이 구할 수 있습니다.

> $G_m=i_{out}/v_{in}$﻿

따라서 Degenerated CE stage의 $G_m$﻿은 $g_m/1+(1/r_\pi+g_m)R_E$﻿ 가 됩니다.

![[Screenshot_2023-10-31_at_9.57.58_PM.png]]

> [!important]  
> 여기서는 approximation이 안됐습니다. 교재에서는 @import url('https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.css')rπr_\pirπ​﻿를 없애더라구요.  
  
> [!important]  
> 왜 굳이 @import url('https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.css')GmG_mGm​﻿이냐면 transconductnace에서 유래된거라 그렇습니다.  

## Degenerated CE Stage with Base Resistance

외부 기기를 input으로 연결하면 무조건 Base Resistance가 생길 수밖에 없습니다. 이 때의 voltage gain을 계산하면 다음과 같습니다. $R_B$﻿가 직렬로 연결된 것을 고려해 원래 $R_B$﻿가 없었을 때의 값을 이용해 계산합니다.

![[Screenshot_2023-10-31_at_10.20.54_PM.png]]

분모에 들어가 있는 $R_B/\beta+1$﻿이 gain을 조금 낮춥니다. 하지만 어쩔 수 없죠.

> [!important]  
> @import url('https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.css')β+1\beta+1β+1﻿이랑 @import url('https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.css')β\betaβ﻿랑 같다고 취급… 했네요  

I/O impedance를 측정하면 다음과 같습니다.

![[Screenshot_2023-10-31_at_10.23.40_PM.png]]

$R_E$﻿로 degenerating의 효과를 냈지만, 어쩔 수 없는 $R_B$﻿ 또한 gain을 감소시키는 효과를 내고 있습니다. 하지만 $R_B$﻿의 크기는 대개 작기 때문에 신경 쓸만한 정도는 아닙니다.

> [!important]  
> capacitor는 DC일 때 open, AC일 때 short의 역할을 합니다. 그래서 Bypass capacitor라고 부릅니다. ![[Screenshot_2023-10-31_at_10.25.49_PM.png]]  

## Output Impedance of Degenerated CE Stage with Early Effect

Early Effect를 고려할 경우 $r_O$﻿를 동시에 고려해야 합니다. 따라서 KVL, KCL을 이용해 Output impedance 부터 구해봅시다.

![[Screenshot_2023-10-31_at_10.30.16_PM.png]]

> [!important]  
> 아래에 저거 뭔소리냐output-impedance를 높이면 gain이 높아져요…라고 자랑하는 문장  

## Two Special Cases

![[Screenshot_2023-10-31_at_10.32.20_PM.png]]

> [!important]  
> @import url('https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.css')RoutR_{out}Rout​﻿이 저거인건 이해하겠는데 굳이 왜 저렇게 그려서 봐야하나  

## Analysis by Inspection

![[Screenshot_2023-10-31_at_10.42.04_PM.png]]

Capacitor가 달려있어 복잡해 보이는 회로는 SSM을 만들어 AC circuit을 만든 뒤, capacitor를 short 시켜버립시다.

그 뒤로는 알고 있는 topology를 이용해 I/O impedance를 계산하고, voltage gain을 계산합니다.

## Degeneration by Another BJT

다른 BJT에 의해 Degeneration을 할 수 있습니다. 이를 cascode라고 합니다.

이는 Resistor보다 transistor가 훨씬 공간을 적게 차지하기 때문에 장점을 가집니다.

![[Screenshot_2023-10-31_at_10.43.33_PM.png]]