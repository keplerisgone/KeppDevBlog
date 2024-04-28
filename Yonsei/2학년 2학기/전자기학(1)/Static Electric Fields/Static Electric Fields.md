---
Created: 2023-10-04T20:32
---
static하다는 말은… 시간에 구애받지 않는다는 것입니다.

Electrostatics

Coulomb’s Law

Electric Field

Multiple Charges

Dipole

Electric Field by continuous charge dstribution

Gauss’s Law

Point form of Gauss’s Law

Electrostatic Potential Energy (W)

Electrostatic Potential

Electrostatic field and Potential

Electric dipole

Metalic Conductor

Dielectrics in Static electric field

Boundary Conditions for Electrostatic Fields

Capacitors and Capacitance

Electrostatic Energy and Force

## Electrostatics

- electric charge at rest
- Electric field가 시간에 따라 변하지 않는다!
    - Magnetic field는 E의 변화에 따라 발생하므로, 자기장도 발생하지 않습니다.
    - = magnetostatics

![[Screenshot_2023-10-04_at_8.39.32_PM.png]]

- 정전기 또한 electrostatics의 대표적인 현상 중 하나입니다.
    - friction에 의한 대전
    - conductor는 free charge의 이동, insulator의 경우는 polarization
- electroscope도 있습니다.

## Coulomb’s Law

![[Screenshot_2023-10-04_at_8.53.30_PM.png]]

두 전하를 가진 물체가 서로 주고받는 전기력의 크기는?

> $\vec{F}=k{q_1q_2 \over r^2}\hat{r}$﻿

$k$﻿는 permittivity로, 투과율을 의미합니다.

> [!important]  
> 전기력의 크기는 중력보다 무지하게 큽니다!  
  
> [!important]  
> 벡터의 형태로 정의할 수도 있습니다.  

## Electric Field

![[Screenshot_2023-10-04_at_8.54.09_PM.png]]

단위 전하가 받는 전기력의 크기!!!

> [!important]  
> 이를 Electric field intensity라고 합니다. 정확히는 단위 전하가 아닌 어마어마하게 작은 test charge가 E field 위에서 받는 힘을 말합니다.  

그래서 전기력에서 전하 하나만 나눠주면 됩니다.

> $\vec{E}={\vec{F} \over q}$﻿

Static electric field에서는 다음의 두 가지 법칙이 성립합니다.

- $\nabla\cdot E =\rho/\epsilon_0$﻿
- $\nabla\times E = 0$﻿

> [!important]  
> 각각 E field가 charge density에 관련이 있음을, 아래는 static electric field에서는 rotational 성분이 없음을 뜻합니다. 각각 Green 정리, Stokes 정리로 증명합니다.  

위의 두 식은 differential form, integral form으로 나타낼 수 있습니다. 역시 green 정리, stokes 정리로 증명합니다.

![[Screenshot_2023-10-20_at_8.41.53_PM.png]]

  

![[Screenshot_2023-10-04_at_10.27.57_PM.png]]

위의 경우를 생각해봅시다. 거리가 한없이 증가하면 거리의 영향보다는 전하의 영향이 증가하므로, +3의 전하와 -1의 전하의 오른쪽에는 반드시 전기력이 0인 구간이 존재할 수밖에 없습니다.

![[Screenshot_2023-10-04_at_10.37.21_PM.png]]

  

### Multiple Charges

Electric field에는 superposition이 성립하기 때문에, 한 지점에서 모든 전하에 대한 전기력을 더하면 Net electric field가 됩니다.

### Dipole

Dipole은 반대되는 전하가 polarization 되어있는 것으로 생각하면 됩니다.

역시나 superposition과 Coulomb’s law가 성립하므로, 계산하시면 됩니다.

- electric dipole moment
    
    $p =qd$﻿, p는 moment, q는 charge, d는 dipole 사이의 distance입니다.
    

![[Screenshot_2023-10-20_at_8.59.22_PM.png]]

뭐 결론적으로 dipole에 의한 E field는 다음과 같긴 합니다.

## Electric Field by continuous charge dstribution

![[Screenshot_2023-10-04_at_10.38.41_PM.png]]

charge가 고르게 분포해있다면, vector calculus를 이용합니다. charge들을 벡터에 맞게 나타내고, vector integral을 취하면 됩니다.

## Gauss’s Law

![[Screenshot_2023-10-04_at_10.43.53_PM.png]]

Gauss’s Law는 어떤 폐면적을 통과하는 flux가 내부의 전하량의 총합이라는 정리입니다. 이 때 정의하는 면적을 Gaussian surface라고 합니다.

대강 한 spherical에 대해서 계산하면 위 사진과 같습니다.

여기서 더 일반화 시키면, 다음과 같습니다.

![[Screenshot_2023-10-04_at_10.45.08_PM.png]]

### Point form of Gauss’s Law

![[Screenshot_2023-10-11_at_3.55.18_PM.png]]

Gauss’s Law를 점전하를 사용하는 식으로 표시해봅시다.

_우선 Divergence Theorem을 이용해 Gauss’s Law를 Divergence operator를 이용해 나타냅니다. 그 뒤 해당 부피 내부의 전체 전하를 점전하의 적분으로 표현한 뒤, 양 변을 미분하면 최종적으로 다음과 같은 식이 얻어집니다._

따라서, Electric field는 Divergence 성분과 Curl 성분으로 나뉠 수 있고, Divergence 성분은 Charge에, Curl 성분은 자기장의 변화로 나타납니다.

하지만 Static Electric field에서는 자기장의 변화가 0이므로, Curl 성분이 0임을 알 수 있습니다.

## Electrostatic Potential Energy (W)

![[Screenshot_2023-10-11_at_4.01.34_PM.png]]

Electrostatic Potentisl Energy의 정의는 해당 전하를 그 곳에 위치시키기 위해 **내가 한 일**입니다.

일단 쉬운 것부터 시작합시다.

> $E=-\nabla V$﻿

즉 전기장이 한 일과 크기는 같지만 방향이 반대이므로, 계산식은 다음과 같게 됩니다.

> $W_e=\int^\infty_R \vec{F_{el}}\cdot d\vec{r}={Q_1Q_2 \over 4\pi \epsilon_0 R}$﻿ [J]

또한 Elecrostatic field는 conservative field이므로, 한 일이 경로 의존성을 가지지 않습니다. 따라서 거리로만 계산해도 됩니다!

## Electrostatic Potential

![[Screenshot_2023-10-11_at_4.11.26_PM.png]]

이는 단위 전하를 위치시키기 위해서 해야하는 일로, 역시나 전기장이 한 일과 크기는 같고 방향이 반대입니다. 따라서 계산식은 다음과 같습니다.

> $V={W\over q}=-\int^R_\infty\vec{E}\cdot d\vec{r}$﻿

물론 이는 어떤 지점을 reference로 잡냐에 따라 다른데, point a에서 point b까지 이동시킬 때의 포텐셜은 다음과 같습니다.

![[Screenshot_2023-10-11_at_4.13.31_PM.png]]

Electrostatic field는 conservative field이므로, 폐곡선에 대한 적분값이 0입니다. 따라서 Stokes’ Thm이 성립하고, curl 성분이 0이 됩니다.

![[Screenshot_2023-10-11_at_4.20.34_PM.png]]

중요한 것은 Electric field는 potential의 gradient로 표시될 수 있다는 점입니다.

### Electrostatic field and Potential

![[Screenshot_2023-10-11_at_4.27.17_PM.png]]

수직!!!

또한 potential이 같은 지점은 equipotential 하다고 합니다.

## Electric dipole

아주 작은 거리를 사이에 두고 존재하는 극성이 반대인 두 전하입니다. 다른 지점에서 dipole에 의한 potential은 근사(binomal expansion)을 이용해 구할 수 있습니다.

![[Screenshot_2023-10-11_at_4.33.05_PM.png]]

## Metalic Conductor

물질에는 conductor, semiconductor, insulator(dielectrics) 가 있습니다. conductor에 대해서 알아봅시다.

conductor는 전자가 매우 흐물렁하게 존재합니다.

![[Screenshot_2023-10-20_at_10.43.25_PM.png]]

![[Screenshot_2023-10-20_at_10.14.13_PM.png]]

conductor에 의한 eletric field는 늘 표면에 수직입니다. tangentional field는 언제나 0입니다.

> [!important]  
> 만약 표면에 수직이 아니라면 표면에 평행한 E 성분이 존재하고, 표면의 전하가 움직여 static이라는 조건에 어긋납니다.이는 conductor에서는 언제나 성립합니다.  

Conductor의 성질을 나타내는 값이 conductivity라고 하는데, 이는 챕5에서 배웁니다.

![[Screenshot_2023-10-20_at_5.55.42_PM.png]]

일반적인 conductor는 내부에 E field를 가지지 않습니다. 내부에 E field 를 가진다면 charge가 계속해서 움직일 것이고, 그러면 energy conservation law를 어기기 때문입니다!

> [!important]  
> 아니 이거 치우쳐진 포인트에 대해서는 E가 0이 될 수 없지 않나?물론 가우스 법칙으로 내부 전하가 아에 0인 건 알겠는데 대체 왜 그런지는 모르겠단 말이지  
  
> [!important]  
> 이게 뭔소리람?? 왜 내부에 E field가 형성되어서 charge가 움직이면 conservation하지 않죠???  

Hollow conductor의 경우에는 역시 내부적인 E가 field가 0이므로, 내부의 전하는 0입니다. 따라서 어떤 cage의 내부에 conductor를 넣더라도 대전이 되지 않습니다!

![[Screenshot_2023-10-20_at_6.06.05_PM.png]]

하지만 내부에 점전하가 존재하는 경우는 좀 다른데, 이 경우에도 내부의 charge는 0이 되어야 하므로 내부에 전하가 대전되기는 합니다.

표면에 생기는 potential은 항상 등위입니다. ==즉 conductor의 표면에서는 늘 equipotential==입니다.

물론 charge가 nonuniform인 경우, charge density가 맛이 간 경우, normal E field가 각 표면마다 다른 경우는 equipotential이 아닙니다.

## Dielectrics in Static electric field

![[Screenshot_2023-10-20_at_11.04.50_PM.png]]

- Dielectric은 conductor와 다르게 내부에 free charge가 존재하지 않습니다. 따라서 전하의 움직임보다는 일정한 방향으로의 ==============================배열이 일어나고,============================== 이를 ========================bound charge========================라고 합니다. _나는 polarization이라고 해야징_
- field에 의해서 dielectric이 polarization이 되면 내부적으로도 작은 electric field가 생깁니다. 따라서 내부의 E는 외부의 E보다 작습니다.

> [!important]  
> 아니 conductor는 내부 E가 0인데 아예 가정이 다른건가외부 자기장의 차이였답니다~  

- polarization vector
    
    ![[Screenshot_2023-10-20_at_11.21.54_PM.png]]
    
    그래서 저 친구들이 얼마나 극성을 지니는 지를 표현하는 벡터를 정의했습니다.
    
    정확히는, ============================================================단위 부피당 electric dipole의 합============================================================을 말하는 것입니다.
    
    > [!important]  
    > 근데 왜 밀도를 벡터로 표현해요  
    
    쌍극자가 만드는 퍼텐셜 공식을 polarization vector로 나타내면 외부 표면의 쌍극자가 만드는 퍼텐셜과 내부 쌍극자들이 만드는 퍼텐셜로 나눠집니다.
    
    ![[Screenshot_2023-10-20_at_11.33.35_PM.png]]
    
    공식 유도는 니가 하십시오
    
    여기서 형광펜 쳐놓은 것들을 새롭게 정의합니다. 이름은 equivalent polarization surface charge density, quivalent polarization volume charge density입니다. 왜 굳이 저게 charge density냐면…
    
- Gauss’s law with polarization
    
    극성에 의해 E의 크기는 줄어듭니다. 이를 수식으로 표현하면 다음과 같습니다.
    
    ![[Screenshot_2023-10-20_at_11.46.15_PM.png]]
    
    이걸 여차저차 정리해서 polarization에 의한 영향까지 고려한 E field 친구를 ==electric flux density==라고 정의합니다. 이 친구는 그냥 E와는 다르게 permitivity에 대한 정보를 가지고 있습니다.
    
    ![[Screenshot_2023-10-20_at_11.50.41_PM.png]]
    
- $\vec{P}$﻿도 다르게 정의해볼까요? ‘얼마나 E를 감쇄시키는지’ 를 상수를 이용해 정의하면 D를 더 쉽게 나타낼 수 있습니다.
    
    ![[Screenshot_2023-10-20_at_11.52.58_PM.png]]
    
    물론 물질마다 다른 값을 가지긴 합니다.
    
- D를 이용하면 continuous한 E field graph를 그릴 수 있습니다. polarization을 고려한 E field는 내부에 감쇄가 존재해 다음과 같은 그래프를 가집니다.
    
    ![[Screenshot_2023-10-21_at_12.11.10_AM.png]]
    
    > [!important]  
    > conductor는 0인데 dielectric은 굳이 E를 가지는 이유가?전하가 움직이지 않으니까.  
    

## Boundary Conditions for Electrostatic Fields

다양한 물질들 표면에서의 condition을 알아봅시다.

- normal condition
    
    ![[Screenshot_2023-10-21_at_12.19.22_AM.png]]
    
    어떤 물질 사이의 tangentional 한 E field vector는 연속적입니다!
    
    물론 static에서만요. (폐곡선은 성립해야 하니까)
    
    ![[Screenshot_2023-10-21_at_12.19.59_AM.png]]
    
    D field로 표현하면 다음과 같습니다.
    
- Tangentional condition
    
    ![[Screenshot_2023-10-21_at_12.31.04_AM.png]]
    
    대충 가우스 법칙을 적용한 것입니다. 정말 작은 곡면에 대해서 적용시킨 것입니다. 따라서 다음이 성립합니다.
    
    ![[Screenshot_2023-10-21_at_12.32.43_AM.png]]
    
- Boundary condition!
    
    ![[Screenshot_2023-10-21_at_12.33.01_AM.png]]
    

## Capacitors and Capacitance

- capacitance
    
    어떤 물체의 potential이 증가하면, 그만큼 total charge도 증가합니다. 해당 비율을 $C$﻿라고 정의하고, 이를 capacitance라고 부릅니다.
    
    정확히는 단위 일당 저장할 수 있는 전하의 수를 의미합니다.
    
    > [!important]  
    > 왜 역은 성립이 안 하는지?아니지 역도 성립하는게 맞지  
    
- capacitor
    
    $Q+$﻿ 전하를 가진 어떤 물체와 $-Q$﻿ 전하를 가진 물체 사이에는 꽤 일정한 E field가 생기고, 이에 따른 potential이 생깁니다. 따라서 capacitor는 다음과 같이 구할 수 있습니다.
    
    ![[Screenshot_2023-10-21_at_7.06.22_AM.png]]
    
- series and parallel connections of capacitors
    
    ![[Screenshot_2023-10-21_at_7.15.37_AM.png]]
    
    series 로 연결했을 때는 역수로 더하고, parallel로 연결했을 때는 직렬 저항 더하듯이 더하면 됩니다.
    
    series는 total potential을 이용하는 것이고, parallel은 total charge를 이용합니다.
    

## Electrostatic Energy and Force

- Energy
    
    ![[Screenshot_2023-10-21_at_7.41.23_AM.png]]
    
    potential이 단위 전하에 해주는 일인 만큼, 전체 에너지는 potential에 전하를 곱해준 값이 됩니다.
    
    빈 공간에 계속해서 전하를 가져오는 행위를 반복해봅시다. 계속 식을 정리하다보면… 다음과 같은 식이 나옵니다.
    
    ![[Screenshot_2023-10-21_at_7.45.06_AM.png]]
    
- electrostatic static energy with field quantities
    
    ![[Screenshot_2023-10-21_at_7.48.38_AM.png]]
    
    이것도 한 번 해보십시오…
    
- Capacitor and energy
    
    위의 공식을 증명하면 어쨌든 capacitor에서의 에너지도 구할 수 있겠죠?
    
    ![[Screenshot_2023-10-21_at_7.48.24_AM.png]]
    
- Electostatic force
    
    ![[Screenshot_2023-10-21_at_8.00.24_AM.png]]
    
    정말 단순하게 생각하면 일이 힘을 선적분한 값이기 때문에, gradient를 일에다가 씌우면 되지 않을까요??
    
    위는 Charge가 고정되어 있을 때,
    
    ![[Screenshot_2023-10-21_at_8.00.50_AM.png]]
    
    위는 Potential이 고정되어 있을 때 (Conductor겠죠 그럼)