---
Created: 2023-09-19T20:05
Parent item:
  - "[[Basic Physics of semiconductors]]"
---
## review) Dopant Compensation

![[Media/Untitled 41.png|Untitled 41.png]]

N-type과 P-type doping 을 했을 경우, 더 major한 carrier쪽이 효과를 갖습니다. 이에 따른 Mass active Law는 위 사진과 같습니다.

## Types of Charge in a Semoconductor

Negative charge를 담당하는 것은 conduction band의 electrons과 ionized acceptor atoms, Positive charge를 담당하는 것은 valence band의 hole과 ionized donor atoms입니다.

따라서 Net charge는 다음과 같이 표현할 수 있습니다.

> $\rho=q(p-n+N_D-N_A)$﻿ [C/cm3]

## Carrier Drift

![[Media/Untitled 1 31.png|Untitled 1 31.png]]

전하를 가진 particles가 electric field에 의해 움직이는 것을 Drift라고 하고, 이를 결정하는 것을 mobility ($\mu$﻿) 라고 합니다.

따라서, carrier의 velocity는 Electric field와 mobility의 곱으로 나타냅니다.

이 때 electron의 경우는 electric field와 방향이 반대이기 때문에, vector 방향의 반대를 의미하는 $-$﻿가 붙어있습니다.

## Velocity Saturation

![[Media/Untitled 2 30.png|Untitled 2 30.png]]

하지만 Electric field가 강해짐에 따라 carrier들의 속도는 특정 값으로 수렴하게 됩니다.

이는 여러 가지 이유가 있는데, impurity scattering, Lattice scattering이 바로 그것입니다. $\ce{Si}$﻿ 격자에서 진동이 발생하면 전자의 진동으로인해 collision이 발생하게 되고, 속도는 오히려 줄게 됩니다. 이것이 전기장에 의한 속도 증가와 상쇄되는 것입니다.

## Drift Current

Drift Current는 말 그대로 carrier의 drift로 인해 발생하는 전류입니다. 전류는 단위 시간당 단위 면적을 통과하는 전하량이 정의이므로, carrier velocity(단위 시간당 /전하량)과 carrier concentration (단위 부피당 농도) 를 곱한 값이 됩니다.

> $J_{p,drift}=q\ p \ v_h =q\ p \ \mu_p \ E$﻿  
>   
> $J_{n,drift}=-q\ n \ v_e = q \ n \ \mu_n \ E $﻿

## Conductivity and Resistivity

![[Media/Untitled 3 29.png|Untitled 3 29.png]]

위에서 $J_{tot,drift}$﻿ 를 구하면 $q(p\mu_p + n\mu_n)E$﻿ 이고, 가운데 term을 conductivity 라고합니다. conductivity의 역수를 resistivity 라고 합니다.

### Resistivity example

![[Media/Untitled 4 22.png|Untitled 4 22.png]]

## Elecrtical Resistane

![[Media/Untitled 5 18.png|Untitled 5 18.png]]

## Carrier Diffusion

만약 non-metalic 한 물질이라면, carrier가 물질에 걸쳐 균등하게 분포하지 않을 수도 있습니다. 이 농도에 따라서 carrier가 이동하는 것을 carrier diffusion이라고 하고, 이는 다음과 같이 표현할 수 있습니다. concentration gradient에 비례합니다.

> $J_{p,diff}=-qD_p\frac{dp}{dx}$﻿ 근데 교수님 이건 x 방향으로만이잖아요

$p$﻿는 hole concentration을 뜻합니다. $-$﻿가 왜 붙었는지 생각해봅시다. 양공은 _양공의 농도가 낮은 방향으로_ 이동합니다. 따라서 dp/dx의 값은 음수일 것입니다. 하지만 양공의 움직임은 곧 전류의 방향과 같기 때문에, 마이너스를 달아줘야 합니다.

> $J_{n,diff}=qD_n\frac{dn}{dx}$﻿

전자는 _전자의 농도가 감소하는 방향_으로 이동하고, _전자의 이동 방향과 전류의 방향은 반대이므로_ 음수가 붙지 않습니다. 어차피 gradient와 전류의 방향이 상쇄되기 때문입니다.

## Diffusion Current

![[Media/Untitled 6 16.png|Untitled 6 16.png]]

다 더해!

## Einstein Relation

![[Media/Untitled 7 14.png|Untitled 7 14.png]]