---
Created: 2023-11-29T17:59
---
Review

Need for Faraday’s law

Faraday’s discovery

Faraday’s experiment

Two Source of E

Lenz’s Law

Example

Inductance

Use of Inductance

Eddy Current

Magnetic Levitation

Maxwell’s Equation

Physical nature of Je, Jd

Capacitor

Maxwell’s Equation

Boundary condition

Potential functions

From classical physics to relativity

Waves

EM Wave propagation

EM Wave

Linearity & Phasor

Phasor

Linearity & Phasor cont.

## Review

![[Screenshot_2023-11-29_at_6.09.45_PM.png]]

![[Screenshot_2023-12-18_at_9.01.46_PM.png]]

- D는 polarization을 고려한 electric field density
    - $\vec{D}=\epsilon E+P$﻿
- H는 Magnetization? 을 고려한 값
- divergence들에 대해서는 time varying field에서도 변하지 않는다
- $\epsilon_0$﻿와 $\mu_0$﻿의 관계성
    - 둘이 곱해서 역수 취한 담에 루트 때리면 빛의 속도 나옴
- curl에 대한 표현은 각각 패러데이의 법칙, displacement current로 대체될 것

## Need for Faraday’s law

![[Screenshot_2023-11-29_at_6.17.18_PM.png]]

- 코일을 움직이는 경우
    - 코일의 charge가 움직여 (F 발생,) 전류가 흐름 → EMF 발생
- 자석을 움직이는 경우
    - move charge가 0인데 힘은 같아야 하잖아 → F는 어디서 오는 것인가?

## Faraday’s discovery

![[Screenshot_2023-11-29_at_6.19.23_PM.png]]

- 전류는 자기장을 형성하는데 역도 성립하는가?
    - steady 에서는 성립하지 않음
    - 하지만 switching되는 순간에는 성립
    - → 즉 자기장의 변화는 전류를 만들어 낸다
    - 방향은 렌츠의 법칙

## Faraday’s experiment

![[Screenshot_2023-11-29_at_6.21.33_PM.png]]

- 유도 전류의 세기는…
    - 자기장의 변화, 자기장이 통과하는 면적에 비례
- 패러데이 법칙 : $\nabla \times \vec{E}=-{\partial\vec{B} \over \partial t}$﻿

## Two Source of E

![[Screenshot_2023-11-29_at_6.24.10_PM.png]]

- 하나는 electrostatic (charge) → conservative
- 다른 하나는 inductive (자기장의 변화) → non-conservative
- induced의 특징
    - wire에 유도되기도 하지만, free space에 유도되기도 함

> [!important]  
> 그러면 계속 자기장이 전류를 발생시키면 전류는 자기장을 발생시키고…. 계속 그럴 수 있는거?  

## Lenz’s Law

![[Screenshot_2023-11-29_at_6.25.46_PM.png]]

- 전류의 방향은 자기장의 변화를 방해하는 쪽으로

![[Screenshot_2023-11-29_at_6.26.29_PM.png]]

- 에너지 보존의 측면에서 살펴보면…
- Inductive coupling
    - 관성 때문에 step function처럼 전류가 증가하지는 않음
    - $I_1$﻿의 변화량 = 자기장의 변화량 = $I_2$﻿에 유도되는 전류
    - 방향은 렌츠의 법칙으로 알아서

![[Screenshot_2023-11-29_at_6.31.22_PM.png]]

- 아래에서는 왜 KVL이 성립이 안 될까

![[Screenshot_2023-11-29_at_6.39.17_PM.png]]

- flux를 이용한 power generator

## Example

![[Screenshot_2023-11-29_at_6.41.06_PM.png]]

![[Screenshot_2023-11-29_at_6.41.40_PM.png]]

## Inductance

![[Screenshot_2023-11-29_at_6.42.04_PM.png]]

- capacitance와 다르게 magnetic energy를 저장할 수 있는 정도를 나타낸다
- 어떻게 사용하나요
    - 주로 coupling시켜서 사용합니다.

![[Screenshot_2023-11-29_at_6.44.46_PM.png]]

- 플럭스의 링크된 양
- self inductance
- mutual inductance

![[Screenshot_2023-11-29_at_6.50.03_PM.png]]

![[Screenshot_2023-11-29_at_6.50.47_PM.png]]

![[Screenshot_2023-11-29_at_6.50.53_PM.png]]

## Use of Inductance

![[Screenshot_2023-11-29_at_6.51.19_PM.png]]

![[Screenshot_2023-11-29_at_6.51.29_PM.png]]

![[Screenshot_2023-11-29_at_6.51.36_PM.png]]

## Eddy Current

![[Screenshot_2023-11-29_at_6.51.49_PM.png]]

## Magnetic Levitation

![[Screenshot_2023-11-29_at_6.52.02_PM.png]]

## Maxwell’s Equation

![[Screenshot_2023-12-19_at_12.04.03_AM.png]]

- 전하 보존의 법칙에 부합하게 수식을 수정
- 남의 방정식 정리해서 업적을 탈취함
- displacement current

  

- 그래서 divergence를 취해보았더니 ampere’s law에서 뭔가 이상…
- 그래서 우변에 term을 하나 넣음

  

- 저기에 자기장이 유도 → E field의 발생 (Capacitor)
- electric flux term을 고려

  

## Physical nature of Je, Jd

- 고정된 charge들이 electris field를 맞아 rotation
    - 이게 시간에 따라 일어남 → displacement로 볼 수도 있음

## Capacitor

- displacement current만 쓰는 경우
- 사이에 물질이 있는 경우
    - conduct current? displacement current?
    - 둘다 있다!
    - 크기의 차이는 때에 따라 다르다
- displacement current는 phase가 존재

## Maxwell’s Equation

- 정리

## Boundary condition

- EM field의 분포를 알아낼 수 있다.

## Potential functions

## From classical physics to relativity

- 대체 왜 똑같이 전류가 흐르는 도선 사이에 힘이 작용하는가?
- 두 도선이 있을 때 전류가 흐르면 각각의 전하의 입장에서는...
- 전자는 다른 전자가 가만히 있고 +가 움직이는 것처럼 보임
- 공간의 축소?? 시간의 절대성은 없다
- 전하가 공간의 축소에 의해서 몰려서 힘이 작용하는 거임

## Waves

- 맥스웰 방정식의 해
- wave는 sin 함수로 많이 나타낸다
- wavelength, direction, speed(=velocity) 정보를 담고 있다
- 따라서 frequency, period를 추가로 계산가능

## EM Wave propagation

- $\nabla^2\vec{E}-{1\over v^2}{\partial^2\vec{E}\over \partial t^2}=0$﻿ : wave equation
- Likewise, E → H
- 방정식을 구하는 법은 paraday law에 curl을 취해서 얻는다
- 해를 구하는 법은 일단 공간에 대한 미분($\nabla^2$﻿)을 x에 대한 2차 편미분으로 생각한다.
- 속도는… 빛의 속도다.
- 해의 형태는 $f(x-vt)$﻿, 뭐든지 될 수 있다!

## EM Wave

- 일단 대표적인 cos 함수를 집어넣어 보자
    - plane wave → 가장 단순한 보편적인 wave
- condition은 위 슬라이드를 참고.
- 모든 맥스웰 방정식을 만족한다. 증명은 슬라이드로…

## Linearity & Phasor

- 맥스웰 방정식은 선형 방정식이다
- 선형 방정식에서 사용할 수 있는 도구 phasor

## Phasor

- 대표적인 eigenfunction : $e^t$﻿ → 확장된 : $e^{jwt}$﻿
- 푸리에 변환으로 주파수를… 뜯어서… $e^{jwt}$﻿로 머시기 머시기…
- phasor는 교류를 직류처럼 해석할 수 있게 해주는 해석 기법
    - 실제로 미방에서는 페이저를 이용하면 그냥 방정식 풀듯이 풀 수 있다
- 리니어에서만 사용가능한 이유 → eigenfunction이라?

## Linearity & Phasor cont.

- 헬름홀츠 방정식 → H 식의 양변에 curl을 취함
    - 사실 wave eq. 의 페이즈 버전
- H나 E를 구하는 법
- 예시) Aircraft VHF communication