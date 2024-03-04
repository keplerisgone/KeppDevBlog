---
Created: 2023-09-11T21:40
Parent item:
  - "[[Signals and Systems]]"
---
## 1.3 Exponential and Sinusoidal Signals

### Complex number

![[Screenshot_2023-09-06_at_8.41.28_PM.png]]

$z=x+jy$﻿ 로 구성됩니다. ($x=Re\{z\},\ y=Im\{z\}$﻿)

Euler’s relation을 이용해 $e^{j\theta}=\cos\theta+j\sin\theta$﻿ 로 표현할 수 있습니다.

> [!important]  
> 근데 굳이 angular function 안 쓰고 복소평면 쓰는 이유가 뭐에요  

### CT complex Exponential and Sinusoidal Signals

Complex number를 이용한 CT는 다음과 같이 표현합니다.

> $x(t) = Ce^{at}$﻿

> [!important]  
> 여기서 중요한 점은 C 또한 complex number라는 것입니다. @import url('https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.css')C=∣C∣ejθC=|C|e^{j\theta}C=∣C∣ejθ﻿ 로 표현됩니다.  

a의 값에 따라 함수의 형태가 달라집니다.

여기서 a가 pure imaginary하다고 가정해봅시다. ($a=jw_0$﻿)

시그널은 주기함수임을 이용하면 다음을 이끌어 낼 수 있습니다.

$e^{jw_0t}=e^{jw_0(t+T)}=e^{jw_0t}e^{jw_0T},\ w_0T=2\pi$﻿ 이고, 이 때 $w_0$﻿를 fundamental frequency 라고 합니다.

> [!important]  
> 복소평면을 생각하는 이유는 exponential을 periodic으로 바꾸기 위해서? (정보가 적어지니깐? periodic은 주기 + 진폭 + 합 의 관계만 생각하면 됨)  

Periodic sinusoidal signals는 다음과 같은 식으로 표현됩니다.

> $x(t) = A\cos(\omega_0t+\phi)$﻿

여기서 t는 시간, $\phi$﻿는 phase, $\omega_0$﻿은 fundamental frequency입니다.

### Harmonically related complex exponentials

![[Screenshot_2023-09-11_at_9.54.15_PM.png]]

fundamental freqeuncy의 정수배를 가지는 signals의 모임을 Harmonic set of signals라고 합니다.

Harmonic set of signals에 속하는 signal들은 간단히 하나로 합칠 수 있습니다.

### General complex exponential signals

> $C=|C|e^{j\theta},\ a=r+j\omega_0$﻿ 일 경우에
> 
> ![[Screenshot_2023-09-11_at_10.03.19_PM.png]]

이후 r 값에 따라 signal의 Growing/decaying 여부가 달라집니다.

### DT complex exponential and sinusoidal signals

CT signal과 마찬가지로 $x[n]=C\alpha^n$﻿으로 나타납니다. $C,\alpha$﻿는 모두 complex number입니다.

- 모두 real number인 경우
    
    ![[Screenshot_2023-09-11_at_10.07.00_PM.png]]
    
- purely imaginary한 경우
    
    ![[Screenshot_2023-09-11_at_10.09.14_PM.png]]
    
- 모두 complex number (General)
    
    ![[Screenshot_2023-09-11_at_10.10.00_PM.png]]
    

### Difference between CT and DT signals

![[Screenshot_2023-10-10_at_1.28.04_AM.png]]

![[Screenshot_2023-09-11_at_10.33.51_PM.png]]

우선 주파수를 봅시다. CT에서는 주파수가 높아질 수록 oscillation이 빠르게 일어나지만, DT에서는 $2\pi$﻿ 범위 밖의 주파수는 의미가 없습니다.

![[Screenshot_2023-09-11_at_10.36.21_PM.png]]

또한 모든 경우에서 주기성이 성립하는 CT와 달리, DT에서는 $\frac{\omega_0}{2\pi}$﻿가 유리수여야만 주기성이 성립합니다.

  

> [!important]  
> Example 1.5