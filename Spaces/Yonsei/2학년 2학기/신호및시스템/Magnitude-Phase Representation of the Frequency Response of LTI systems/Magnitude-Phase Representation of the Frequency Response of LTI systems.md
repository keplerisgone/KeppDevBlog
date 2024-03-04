---
Created: 2023-11-08T21:20
Parent item:
  - "[[Time and Frequency Characterization of Signals and Systems]]"
---
FT의 convolution 성질에 의해 LTI system을 다음과 같이 정의할 수 있습니다.

![[Screenshot_2023-11-08_at_9.21.04_PM.png]]

frequency response의 magnitude는 system의 gain을, phase는 phase shift를 나타냅니다.

### Linear and Nonlinear Phase

- Linear Phase shift
    
    CT의 경우는 정말 linear phase이기만 하면 그대로 shift되고,
    
    DT의 경우는 phase의 slope가 integer이기만 하면 됩니다.
    
    ![[Screenshot_2023-11-08_at_9.33.57_PM.png]]
    
- Non—linear phase shift
    
    신호가 망가짐.
    

![[Screenshot_2023-11-08_at_9.35.07_PM.png]]

DT도 마찬가지

## Group delay

Group delay는 다양한 주파수 성분으로 이루어져 있는 신호에서 각각의 주파수 성분마다 shift 되는 정도가 달라지기 때문에 발생합니다. (Linear phase여도)

![[Screenshot_2023-11-09_at_9.02.49_AM.png]]

## Log Magnitude and Bode Plots

FT에서는 log를 쓰는 게 더 편리할 수 있습니다.

![[Screenshot_2023-11-09_at_9.03.41_AM.png]]

DT 신호에서는 안 쓴다고 하네요

데시벨은 $20\log_{10}$﻿ 으로 정의됩니다.

![[Screenshot_2023-11-09_at_9.04.29_AM.png]]

Bode Plot은 주파수 도메인에서의 값을 log로 나타내거나 phase로 나타내는 방법입니다. 그래프로 두 방법을 표시하면 다음과 같습니다.

![[Screenshot_2023-11-09_at_9.07.01_AM.png]]

다시 말하지만, DT 신호에서는 굳이 쓸 일이 없습니다.