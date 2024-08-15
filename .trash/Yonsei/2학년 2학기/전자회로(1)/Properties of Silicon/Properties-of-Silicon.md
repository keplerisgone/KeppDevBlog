---
Created: 2023-09-15T15:33
Parent item:
  - "[[Basic Physics of semiconductors]]"
---
Properties of silicon

Silicon Crystal

How can we convert silicon into semiconductor?

Carrier Concentrations in Intrinsic Si

Doping

Dope - N type

Dope - P type

## Properties of silicon

![[Screenshot_2023-09-15_at_11.59.37_PM.png]]

- atomic density 는 $5\times 10^{22}$﻿ atoms/cm^3 이다.
- $\ce{Si}$﻿ has four valence eletrons that can form covalent bonds.
- 온도가 오르면 Si 내부의 전자들이 자유전자가 될 수 있다.
    - Valence band의 전자들이 에너지를 얻어 더 위의 에너지 밴드인 Conduction band로 이동할 수 있다.
    - 상온에서 $10^{10}$﻿/cm3 정도 → 상온에서는 conductor일 수밖에 없음
    - ==Free electron== 이 생기면 빈 공간에 + 전하의 양공(==hole==)이 생긴다. → EHP(eletron hole pair!)
        
        ![[Screenshot_2023-09-16_at_2.18.25_AM.png]]
        
        - hole에 다른 free electron이 결합하는 과정에서 hole은 lattice 사이를 이동하게 됩니다.
- 지구에서 두 번째로 많은 원소 ($\ce{O - Si - Al - Fe - K - Ca}$﻿)
    - 따라서 만드는 데 값이 적게 듭니다
- Silicon Microprocessor를 만들 수 있습니다.
    
    ![[Screenshot_2023-09-16_at_1.47.12_AM.png]]
    
    - 아래에 잘려있는 부분이 있는데, 이는 실리콘의 방향을 배열해주기 위한 것입니다.

## Silicon Crystal

silicon은 crystal structure을 형성할 수 있습니다. 모습은 다음과 같이 생겼습니다.

![[Screenshot_2023-09-16_at_1.48.36_AM.png]]

하나의 결정 단위를 unit cell 또는 unit lattice이라고 합니다. 모서리의 원자는 1/8 개의 원자이고, 면의 원자는 1/2개의 원자와 같습니다.

하나의 unit cell에 모서리 원자 8개, 면의 원자 6개, 내부 원자 4개가 존재하므로, 총 8개의 원자가 존재합니다. 그리고 각 unit lattice의 크기는 5.43A 이므로, 이를 통해 Silicon crystal의 atom density를 계산할 수 있습니다.

## How can we convert silicon into semiconductor?

1. doping (adding special atoms)
2. applying an electric field
3. changing the temperature (increasing free electron)
4. irradiation → solar cell

## Carrier Concentrations in Intrinsic Si

앞서 말했듯이, valance band와 conductor band 사이의 에너지 차이를 band-gap energy라고 하고, 각 밴드에 electron이 들어가는 자리를 state라고 합니다. 밴드의 사이에는 state가 존재하지 않아 전자가 존재할 수 없습니다. 에너지의 양자화?

Intrinsic (without doping) 상태의 electron concentration $n_i$﻿은 다음과 같이 계산할 수 있습니다.

![[Screenshot_2023-09-16_at_2.30.42_AM.png]]

이는 동시에 ==Intrinsic carrier concentration (====$n_i$==﻿==)==이라고 부릅니다. 단어를 천천히 분석해보자면,  
  
Intrinsic - 내재적이라는 뜻으로, 도핑을 하지 않은 기본적인 상태를 뜻합니다.  
  
carrier - hole과 free electron은 전하를 가진 입자들로, 전류의 기원이 됩니다. 따라서 이 입자들의 쌍을 Electron-Hole Pair(EHP) 라고 부릅니다. EHP의 농도를 말하는 것입니다!

> [!important]  
> 사실 hole은 전자의 움직임으로 생기는, 우리가 간편하게 생각하기 위해서 만든 가상의 입자입니다. 잘 생각해보면 사실상 전자의 움직임과 같습니다.  
  
> [!important]  
> 진짜 electron concentration이 뭔가요?말 그대로 전자의 농도입니다만, 주로 고체 내부에서 기본적인 열 에너지로 인해 자유 전자가 되는 친구들의 농도를 뜻합니다.  

## Doping

### Dope - N type

![[Screenshot_2023-09-16_at_2.44.35_AM.png]]

valance electron이 4개인 Si에 valance electron이 5개 존재하는 $\ce{P}$﻿ (phosphorus) 를 집어넣으면, free electron이 하나 늘어나 electron concentration이 늘어나게 됩니다.

이것은 Conduction band에 state 하나를 추가해주는 것과 동일한 효과를 지닙니다. 해당 state에 추가된 전자는 conduction band로 이동하기 편해지게 되고(band-gap energy가 몹시 낮기 때문입니다), conduction band에 존재하는 전자의 수가 많아지므로 electron concentration이 높아지게 됩니다.

만들어지는 state는 전자를 보내주는 역할을 하기에, ==donor== 라고도 부릅니다.

좀 더 복잡하게 여러가지 수들을 추가해봅시다.

$N_d$﻿ = 추가한 donor의 농도

$N_d^+$﻿ = 이온화된 donor 원자의 농도

$n$﻿ (or $n_0$﻿) = 도핑 상태의 전자 농도 (conduction electron concentration) 라고 하면,

$n=N_d+n_i\approx N_d\approx N_d^+$﻿ 이 성립합니다. $n_i$﻿는 값이 매우 작기 때문에, 생략 가능하다고 하겠습니다.

이렇게 도핑을 하게 되면 상온에서보다 concentration이 $10^{18}$﻿ /cm3 정도로 높아집니다.

> [!important]  
> @import url('https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.css')Nd+N_d^+Nd+​﻿에 대해서 처음엔 잘 이해 못했는데, donor 원자는 자유전자 하나를 빼앗기기 때문에 (+) 전하로 ionized된다 라고 생각하니 쉬워졌습니다.  
  
> [!important]  
> 굳이 Phosphorus의 남는 전자가 자유전자가 되는 이유가 뭔가요?원자는 valance electron을 8개로 만들고 싶어하는 성질이 있는데, (Octet rule) 이를 실현하는 가장 빠른 방법이기 때문입니다.  

### Dope - P type

![[Screenshot_2023-09-16_at_3.02.52_AM.png]]

N type과 비교하여 생각해봅시다.

P type에서는 valance eletron이 3개인 원소를 첨가해 hole를 추가해주는 과정입니다. 예시에서는 $\ce{B}$﻿ (boron)을 추가했네요. hole의 수가 늘어나면 hole concentraion ($p$﻿)이 증가하게 되고, 전류가 잘 통하게 됩니다.

이는 valance band 바로 위에 state를 추가해주는 것과 같습니다. 해당 state로 전자가 이동하면 valance band에는 hole이 다량 추가됩니다.

이 state들은 valance band로부터 전자를 받는다 하여 ==Acceptor==라고도 부릅니다.

이번에도 여러가지 수들을 추가해봅시다.

$N_a$﻿ = 추가된 acceptor의 농도

$N_a^-$﻿ = ionized 된 acceptor 원자의 농도 (역시나 위와 같은 방식으로 생각하면, 전자를 받기 때문에 (-) 전하로 ionized됩니다.)

$p$﻿ (or $p_0$﻿) = 도핑 상태의 hole concentration 라고 하면,

$p = n_i+N_a\approx N_a\approx N_a^-$﻿ 이 성립합니다.