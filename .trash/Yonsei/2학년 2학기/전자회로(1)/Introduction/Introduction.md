---
Created: 2023-09-08T16:24
Parent item:
  - "[[Introduction & Review of Basic Circuit theory]]"
---
Introduction

What is eletronics?

Cellular Phone

Transmitter (TX)

Receiver (RX)

Digital Camera

Electronics vs Microelectronics

History of IC devices

## Introduction

### What is eletronics?

electronics는 전자의 움직임(Directing Electrons)과 이를 사용하는 소자들에 대한 학문입니다.

- Directing electrons
    
    전자의 포텐셜 에너지 → Voltage ($V$﻿)
    
    전자의 흐름 → Current ($I$﻿)
    
    이들을 이용하는 소자 → Resistor, Conductor, Inductor, Diode, Transistors
    
    앞의 세 개는 Passive device로 BCT에서 배웠고, 뒤의 두 개는 Active device로서 이번에 배웁니다.
    
- Perform useful works
    
    위의 요소들은 전자기기에서 이용됩니다. (회로, 시스템)
    

## Cellular Phone

우리가 사용하는 휴대전화는 아래와 같은 구조로 이루어져 있습니다.

![[Screenshot_2023-09-08_at_7.35.24_PM.png]]

신호를 만들어내는 DSP(Digital Signal Processor), 컴퓨터의 CPU, 우리의 뇌와 같은 역할을 하는 Microprocessor & Control Logic, 소리와 관련된 역할을 하는 Audio D/A & A/D(Digital to Analog convertor, vicebersa), 저장 장치인 Memory, 전원 장치인 RF and Power, 가장 중요한, 신호를 증폭시키는 RF TX & RX (Transmitter, receiver) 로 이루어져 있습니다. TX와 RX에 대해 자세히 살펴봅시다.

![[Screenshot_2023-09-08_at_7.39.33_PM.png]]

### Transmitter (TX)

![[Screenshot_2023-09-08_at_8.00.38_PM.png]]

트랜스미터는 신호를 받아 전달하는 소자입니다.

microphone → Audio amp → Modulator & oscillator → Power amp → Antena 의 경로로 신호가 이동합니다.

사람의 목소리는 2Hz ~ 2kHz의 주파수를 갖고 있습니다. 이는 Audio amp 를 통과해 커집니다. oscillator는 1GHz ~ 2GHz 의 주파수를 가진 파동 함수로 목소리를 바꿔주는 역할을 합니다.

이는 안테나와 연관되어 있습니다. 안테나는 wavelength와 연관있습니다. 파동의 wavelength는 다음과 같이 구할 수 있습니다. ($c=\lambda f$﻿) 여기서 파동의 주파수가 낮을 수록 wavelength 가 길어지는데, 이러면 파동을 받아들이는 안테나의 크기 또한 천문학적으로 커질 수밖에 없게됩니다.

### Receiver (RX)

리시버는 신호를 받는 장치입니다. Antena 를 이용해 신호를 받아들인 뒤, 스피커로 소리를 내보냅니다.

Antena → Lownoise amp → Signal processor(Demodulator) → amp → Speaker 로 신호가 전달됩니다.

Lownoise amp 는 장거리를 이동하며 주파수가 낮아진 신호를 증폭시키는 역할을 하고, demodulator는 원래 목소리의 주파수로 돌려놓는 역할을 합니다.

## Digital Camera

빛 신호를 전기 신호로 바꾸는 예시입니다.

![[Screenshot_2023-09-08_at_8.12.50_PM.png]]

빛 신호는 photoeletric conversion (image sensor 에서 일어남) 통해 photon → elecrical signal로 변환되고, analog eletronics 에서는 eletrical charge → voltage 정보로 변환됩니다. 마지막으로는 voltage → digital value로 바뀝니다.

이 모든 과정은 하나하나의 픽셀에서 일어납니다. 카메라는 5천만개의 image diodes로 이루어져 있는데, 하나하나의 크기는 10um 이기 때문에, 각 신호를 증폭시키는 amp가 중요해집니다.

### Electronics vs Microelectronics

회로의 가장 큰 기능은 신호를 증폭하는 것입니다. 하지만 일반적인 전기회로의 amplifier는 굉장히 큰 크기를 가지고, 많은 에너지를 잡아먹기 때문에, microelecronics의 발달이 필요합니다. 이는 매우 작은 크기를 자랑하기 때문에 기능적으로도 우수합니다.

많은 회로의 기본은 실리콘으로 이루어져 있습니다.

### History of IC devices

1940년도에는 진공 튜브를 이용한 증폭을 시도했습니다. 물로 크기가 크고 에너지를 굉장히 많이 잡아먹었습니다.

이후 1956년에는 트랜지스터가 최초로 개발되었고, 이후에 BJT가 개발됩니다.

또한 트랜지스터가 모인 집적회로(IC)는 1958년에 개발됩니다.

또한 매년 IC에 포함되는 칩의 개수가 두 배가된다는 Moore’s Law는 아직까지도 적용되고 있습니다.

칩의 개수를 늘리는 법은 새로운 재료의 발견, 새로운 디자인이 있습니다.