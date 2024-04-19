# 집적 회로의 문제점
![](https://i.imgur.com/AEtinLD.png)

- PCB를 설계하면 저렇게 외부 GND와 연결될 수 밖에 없는데, 여기 있는 금속 wire가 inductor의 역할을 해 magnetic flux가 생기게 된다
- 이러면 noise가 발생해
![](https://i.imgur.com/UinTEP0.png)
- 또한 내부 회로에서 GND를 공유하면 서로의 noise가 타고 들어가 부작용이 커진다
- GND의 분리가 필요하다
- 이는 PCB의 공정으로 해결하거나 회로적으로 해결할 수 있다
- 회로적으로 해결하는 방법이 바로 Differential Amplifier
# Differential Signal

![](https://i.imgur.com/iDYUfxJ.png)
- 트랜스포머에 신호를 통과시키면 두 개의 위상이 다른 신호가 나오는데, 이를 **Differential signal**이라 한다. 
- 이 신호를 **Differential Amplifier**에 통과시키면 두 신호가 각각 증폭된다.
- 이걸 다시 transformer로 합쳐주면 큰 시그널 완성~
- 장점은 "시그널을 반만 들고 다녀도 된다" "증폭되는 과정에서 노이즈가 사라진다"

![](https://i.imgur.com/TGemteV.png)
- 하지만 노이즈가 생긴다면? (빨간색)
- 노이즈는 양쪽 differential signal에 동일한 형태로 타기 때문에 **common mode signal**이라고 불린다.
- 보면 알겠지만 amplifier를 통과하는 과정에서 common mode는 사라진다
- single end의 경우 노이즈 또한 증폭될 것
	- 또한 신호의 방사가 GND를 찾을 때까지 이루어지기 때문에 고통스럽다
# Passive vs Active
![](https://i.imgur.com/2wmzfEK.png)
- 위와 같이 transformer를 이용하는 방식이 **passive balun**이고,
- 위 그림과 같이 transistor를 이용하는 방식이 **active balun**이다.
	- 이게 더 작고 저렴이다 (성능은 몰라도)
# Differential Pair
![](https://i.imgur.com/le4Gqwz.png)
- differential amplifier는 이런 회로로 구성된다.
- 양단에 input voltage가 걸리는데, 이 비율에 따라 $I_{1}$과 $I_{2}$의 비율이 결정된다.
	- 각 입력 전압의 비와 동일하다
- 가장 좋은 지점은 두 input voltage가 동일할 때겠지
# Gain of Diff. amplifier
![](https://i.imgur.com/7g5pNEZ.png)
- 당연히 common mode의 gain은 낮고, differential signal의 gain이 높은 amplifier가 좋다
- 따라서 전체 gain은 둘의 비율로 정의
- 이를 common mode를 최대한 무시한다 해 **common mode rejection gain**이라 한다
	- 혹은 Common mode Rejection Ratio(**CMRR**)이라고도 한다
## Differential mode gain, $A_{diff}$
![](https://i.imgur.com/E4Z6LFo.png)
- 분자 부분, Differential signal의 gain을 구하는 법이다. 
- 수식으로는 $A_{diff} = {-(v_{o1}-v_{o2}) \over v_{s1} - v_{s2}}$이다. 아이디어는 다음과 같다.
	- SSM로 전환 
	- GND 공유를 이용해 회로를 반전 
	- KCL, KVL를 이용해 $v_{o1}-v_{o2}, v_{s1}- v_{s2}$값을 구한다.
- 일반 BJT 회로와 gain이 상당히 유사한 형태다
## Common mode gain, $A_{CM}$
### Common mode noise
![](https://i.imgur.com/3DgfHKC.png)
- common mode noise는 differential signal을 생성할 때 타는 노이즈를 의미, 두 시그널에 공통으로 들어간다
- 위상이 같은 noise
- 전원 자체에서 타거나, 아날로그-디지털 변환 도중 타기도 한다
- 절대값이 딱히 중요하지 않다
### Fully differential amplifier
![](https://i.imgur.com/57YCG6E.png)
- Common mode에서 noise는 두 input에서 같은 phase를 지니므로, Base를 묶어서 생각해도 상관없다
- 이 경우 $A_{CM}$은 병렬로 취급해서 저렇게 계산된다
- **Pseudo Differential Amplifier**는 아래에 $I_{EE}$가 없는 형태인데, 이러면 symmetry가 맞춰지지 않을 수 있어 위험하다
### New CMRR
![](https://i.imgur.com/KFVvyua.png)
- CMRR(Common mode rejection ratio)를 다시 정의하면 다음과 같다
	- ${A_{DM} \over A_{CM-DM}}$
- $A_{CM-DM}$은 저렇게 input 단을 연결시켰을 때 $A_{v1}-A_{v2}$로 정의된다.
- 여태껏 해왔던 것처럼 current loop를 돌리면 되지만, $I_{1}$과 $I_{2}$가 다를 수도 있기 때문에 이걸 맞춰줘야 한다.
	- 같은 양의 전류가 흐른다고 가정한 뒤, current divider로 맞춰주는 것이라 생각하면 된다
- 식을 통해 생각해보면, $A_{CM-DM}$을 줄이는 방법은...
	- $R_{EE}$를 높이거나
	- symmetry를 정확하게 맞춰주기 ($R_{1},R_{2}$와 ${1\over g_{m1}}, {1\over g_{m2}}$를 $맞춰준다$)
# etc.
![](https://i.imgur.com/N4y9X5o.png)
- Diff. amplifier 설계에는 **Symmetry**가 매우 중요하다. 이게 같지 않으면 noise가 상쇄되어 사라지지 않는다. 
![](https://i.imgur.com/6zIdXIl.png)
 - **virtual ground**는 실제로 GND는 아니지만, symmetry 같은 조건에 의해 gnd처럼 생각할 수 있는 것을 말한다. 
 - 'Symmetry' 조건을 만족한다면, 반으로 잘라서 Virtual GND를 붙인다고 생각하면 쉽다.
# Example
## 10.11

![](https://i.imgur.com/MfeiC66.png)
## 10.12

![](https://i.imgur.com/nBzzKk8.png)
## 10.13

![](https://i.imgur.com/iyEMVDH.png)
## 10.14

![](https://i.imgur.com/a7SxHL6.png)
- 저거랑 저거는 왜 등가회로일까?
![](https://i.imgur.com/lNw00al.png)
- 요런 과정을 거친다
## 10.27

![](https://i.imgur.com/B5Qk4tn.png)

## 10.34
## 10.70
## 10.71
### Current mirror

# 의문점
- 위처럼 current loop를 이용하는 방식이 간단하고 early effect나 channel length를 무시하는 회로면 괜찮은데, 조금이라도 복잡한 회로는 적용하기 어렵다
	- 그냥 **Transconductance**를 사용하기로 했다

 