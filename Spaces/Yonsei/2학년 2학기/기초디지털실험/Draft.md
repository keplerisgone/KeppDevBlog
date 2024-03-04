---
Created: 2023-09-09T15:07
Parent item:
  - "[[Week 1]]"
---
이번 실험에서는 논리회로를 구현하기 위해 사용하는 프로그램인 Vivado의 사용방법과 기초적인 Verilog의 문법에 대해 알아보고, 모듈을 이용해 기초적인 회로를 구성해 실험을 진행한다.

이런이런 회로를 구현했다.

## Theory

<선택사항> 디지털논리회로의 기본 정보… 넣지말까?

### Create/Add sources

- 하나의 프로젝트에는 다양한 모듈/시뮬레이션/보드를 추가할 수 있다.
- 각각의 차이, 자세한 설명은 아래에서
- 추가하는 방법

### Module

- module이란?
    - 이러이런…
- module은 다음과 같은 방법을 이용해 생성할 수 있다.
- 하나의 모듈 내부에서는 gate, i/o port 정의, 값 할당 등의 행동이 가능하다.

### Simulation

- testbench에 대하여
- module Instantiation
    
    - 외부 모듈의 게이트를 불러오는 것 < 사진 자료 >
    - 문법 .
    
    ```Verilog
    <외부 모듈의 이름> <정의하는 이름>(
    	.<외부 포트 이름1>(<연결하고자 하는 포트 이름1>),
    	.<외부 포트 이름2>(<연결하고자 하는 포트 이름2>),
    ...
    )
    ```
    
    ```Mermaid
    flowchart TB
      subgraph m1 [Module1]
    		A(<외부 포트1>)
    		B(<외부 포트2>)
    	end
    	subgraph m2 [Module2]
    		C(<내부 포트1>)
    		D(<내부 포트2>)
    	end
    	A --> C
    	B --> D
    ```
    
- 변수 타입
    - reg, wire

### Constraint

- 각 모듈을 보드와 연결하기 위해 필요.
- .xdc 파일을 불러와 포트를 확인 가능 < 사진 >
- 이후 constraint를 추가한 뒤, 외부 모듈 - 보드의 포트를 연결할 수 있다. < 사진 >
    - Pin assignment - 포트를 불러오는 행위, 아래의 Module Instantiation와 연결해 모듈-포트의 연결이 가능
- testbench 와 다른

### Board

- 보드의 구성
- 연결

## Simulation

- AND 연산하는 거
    - waveform simulation
        - 모듈 생성 → testbench 에 연결 → 테스트
    - FPGA (안 씀)
        - 모듈 생성(위의 waveform에서 사용한 것) → topModule 작성, 연결 → 테스트(못함)
- 2-bit adder
    - waveform simulation
        - 모듈 생성 → testbench 에 연결 → 테스트
    - FPGA (안씀)
        - 바바바바

## Discussion

- 알게 된 것
- 질문사항
    - 비트 수 넘어가면
    

  

## Reference

- 모듈의 정의

[http://www.ktword.co.kr/test/view/view.php?m_temp1=6636&id=1556](http://www.ktword.co.kr/test/view/view.php?m_temp1=6636&id=1556)

- initial, testbench

[https://velog.io/@gju06051/Verilog기초11-Testbench](https://velog.io/@gju06051/Verilog%EA%B8%B0%EC%B4%8811-Testbench)

- module instantiation

[https://m.blog.naver.com/soi897/222905274744](https://m.blog.naver.com/soi897/222905274744)

[https://blog.naver.com/soi897/222893340837](https://blog.naver.com/soi897/222893340837)

- 그냥 문법 표

IEEE Standard Verilog® Hardware Description Language