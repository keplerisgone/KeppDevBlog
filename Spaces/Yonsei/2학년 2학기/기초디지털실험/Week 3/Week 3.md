---
Created: 2023-09-19T10:28
---
## Theory

### Theoretical backgrounds of PYNQ GPIO, DEMUX, Decoder

combinational logic

```Mermaid
flowchart LR
  A[Combinational Logic] --> B[Arithmetic function]
	A --> C[Data transmission]
	A --> D[Code converters]
	C --> E[MUX/DEMUX, Decoder/Encoder]
```

MUX and DEMUX - MUX : Multiplexing, multiple input 중 하나를 골라주는 회로

![[Media/Untitled 47.png|Untitled 47.png]]

DEMUX - 하나만 골라주는

Decode - input에 따른 output, DEMUX가 다른점? - [https://ko.spot-the-difference.info/difference-between-demultiplexer](https://ko.spot-the-difference.info/difference-between-demultiplexer)

Encoder - Decoder 반

Verilog HDL - Blocking, Non-blocking, If, Case

PYNQ GPIO

## Verilog code

### Verilog code with comments on operation

examples 를 이용하세요.

DEMUX는 알아서 구현하고

RGB Decoder는 비트를 out에 전부 할당해서 구현하는 것으로 하자 - 나는 멍청이인가?

## Waveform simulation results

### PYNQ LED experiment: verify the output value according to the input/control signal

### PYNQ RGB experiment : verify the output value according to the input signal

### Result analysis

## FPGA results

### PYNQ LED experiment: show the change of LED according to the input/control signal on FPGA board

### PYNQ RGB experiment: show the change of Tri-Color LEDs according to the input on FPGA board

### Result analysis

## Discussion

## Reference

- Combinational Logic

[https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=lagrange0115&logNo=220709564562](https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=lagrange0115&logNo=220709564562)

- 혜ㅑㅒ

[https://talkingaboutme.tistory.com/entry/Linux-GPIO-interface](https://talkingaboutme.tistory.com/entry/Linux-GPIO-interface)