---
Created: 2023-08-31T22:28
Sub-item:
  - "[[Yonsei/2학년 2학기/기초디지털실험/Draft]]"
  - "[[Verilog 기초 문법]]"
  - "[[Vivado 사용법]]"
---
### 개요

<일단 처음에 소개>

I. Theory

II.

III. Discussion

IIII. Reference

  

### 목적)

- 기본적인 디지털논리회로에 알아보고 실험환경을 구성한다.
- 베릴로그 HDL을 이용, 디지털 논리 회로의 Gates를 구현한다.
- digital design process를 이해한다.

위는 정말 표면적인 목적이고, 우리가 정말 알아야하는 것은…

- Vivado 프로그램의 사용방법 알기
    
    - 아니 근데 보드가 없는데 어케 작성함 → 이후의 실험을 위해서 조사만 했다고 하자
        - 보드 연결 관련 theory
    
      
    

### 실험 진행)

- 두 개의 인풋(SW0, SW1)을 받아 아웃풋을 나타내는 회로를 만들기, 아웃풋 시그널은 LEDR0.
- 다양한 logic gate를 회로에 넣어보기
- 테스트, 특정
    
    - waveform
    - 보드 - 근데 현재 실험환경에서 보드가 없으므로 waveform만 결과를 측정해본다.
    
      
    

1. 모듈 정의
    1. create module (무슨 의미를 가질까)
        1. Add Sources → Add or Create design source → Create file
    2. I/O port Definition (현재 실험에서는 사용하지 않지만 이후의 실험을 위해) 찾아보기 안쓰나?
    3. Design Source → 만들어진 logic_gate
        
        ![[%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7_2023-09-09_133651.png]]
        
        ![[Media/Untitled 49.png|Untitled 49.png]]
        
        위와 같은 내용 작성 → 저장.
        
2. Waveform Simulation
    
    Add Sources → Add or create simulation sources → create file
    
    이를 testbench라고 하는데.. 이게 뭐징
    
    ![[Media/Untitled 1 37.png|Untitled 1 37.png]]
    
    여기서는 Module Instantiation 이 일어나는데, 이게 뭐징 아무튼 module의 이름 → 불러올 이름으로 하면 된다고 한다
    
    ![[Media/Untitled 2 36.png|Untitled 2 36.png]]
    
    이게 뭐시당가
    
    reg, wire는 변수 타입인 거 같고, . + (모듈의 포트 이름) + ( 와이어나 레지스터) 는 해당 모듈의 게이트를 연결해주는 과정인 것 같다.
    
    ![[Media/Untitled 3 35.png|Untitled 3 35.png]]
    
    ![[Media/Untitled 4 26.png|Untitled 4 26.png]]
    
    레지스터로 정의된 변수를 초기화한다. 중간에 10ns는 왜 넣어주는 겁니까? → 시간에 따른 변화 관찰, 만약 보드를 이용해 테스트를 진행했다면 직접 인풋을 변화시켜 아웃풋의 변화를 볼 수 있지만, waveform에서는 불가능하기 때문에 시간에 따라 인풋을 변화시키고, 이에 따른 아웃풋의 변화를 확인할 수 있다. 여기서는 output인 result가 input_a & input_b 로 연산되기 때문에, 10ns 이후 a가 0으로 바뀌었을때 r 또한 0으로 바뀌는 것을 볼 수 있다.
    
    ![[Media/Untitled 5 22.png|Untitled 5 22.png]]
    
3. 사실 있어야 하는 Configure Pin Assignments
    
    1. 보드 연결, FPGA의 아무 input/output signal을 연결한다.
    2. Add Sources → Add or create constraints
    3. 가지고 있는 xdc 파일을 프로젝트 경로에 추가한 뒤, 이후의 Add file을 통해 constraint에 추가.
    
    > [!important]  
    > 뭘 담고 있는 파일인가요?열어보면 알겠지만, input - output pin에 관한 정보를 담고 있는 파일입니다. 포트에 대한 정보가 담겨있다고 볼 수 있습니다.  
    
4. Evaluation on FPGA
    1. topModule을 위의 logic_gate와 같은 방식으로 추가한뒤, logic_gate 를 instantiation 합니다.
        
        ![[Media/Untitled 6 18.png|Untitled 6 18.png]]
        
    2. 포트 연결, 앞의 xdc 파일을 보고 LED 부분을 찾아 module() 안에 선언합니다.
        
        ![[Media/Untitled 7 16.png|Untitled 7 16.png]]
        
        ![[Media/Untitled 8 13.png|Untitled 8 13.png]]
        
        ![[Media/Untitled 9 4.png|Untitled 9 4.png]]
        
        아마도 sw의 1~0 포트, led의 0~3 포트를 불러오고 assign 을 통해 포트를 연결시켜주는 과정인 것 같다.
        
        > [!important]  
        > 여기서 wire로 input을 선언하는 이유는 무엇인가요 위의 testbench에서는 reg로 선언하지 않았습니  
        
        사실 아니고 비트 수를 선언하는 거였습니다.
        
    3. 시뮬레이션은 Run bitstream을 이용한다.
5. 2-bit Adder 만들기
    1. 2-bit input signal → 4-bit output signal (3 output signals)
    2. 2bit 인풋을 받아서 111을 더한 값을 출력하기 (즉,
        
        ![[Media/Untitled 10 3.png|Untitled 10 3.png]]
        
        ![[Media/Untitled 11 3.png|Untitled 11 3.png]]
        
        logic_gate - definition of gates
        
        ![[Media/Untitled 12 3.png|Untitled 12 3.png]]
        
        topModule - 사용하지는 않지만, 각 포트에 인풋-아웃풋 할당, logic-gate를 instantiation하는 것도 잊지 말기
        
        ![[Media/Untitled 13 3.png|Untitled 13 3.png]]
        
        ![[Media/Untitled 14 3.png|Untitled 14 3.png]]
        
        waveform를 위한 testbench, 10ns 마다 2bit 인풋인 a 를 1씩 증가시켜 결과를 살펴본다.
        
        ![[Media/Untitled 15 3.png|Untitled 15 3.png]]
        
        ![[Media/Untitled 16 3.png|Untitled 16 3.png]]
        
        결과 출력 잘됨!
        

  

### 이제 할일)

- 코드 주석 달아서 스크린샷 다시 찍기
- 정의 관련해서 초안 작성, 레퍼런스 찾아서 풍부하게 하기
- 필요하면 사진 자료 만들기 (mermaid 사용)