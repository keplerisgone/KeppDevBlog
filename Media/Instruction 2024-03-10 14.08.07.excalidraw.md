---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠==


# Text Elements
Instruction - 컴퓨터가 사용하는 언어
ISA - instruction set들의 짜임 -> standard가 정해짐

=> 결국 이를 사용하는 이유는 편리하게 기기를 관리하기 위해서! ^T9BBns1U

모든 컴퓨터 아키텍쳐의 기반이 됨 = stored-program
 ^TSaQ8a8W

메모리 <=> 프로세서 ^CAz9W5LZ

I/O ^oX0Db6O3

프로그램 실행
 ^d1bvRq3p

Von neumann 아키텍처를 사용하긴 하는데
세부적인 작동방식은 모두 다름 ^UotxPxiC

CISC ^XqXOQw5O

- 가능한 적은 수의 instruction 사용.
- lower power consumption
- x86, intel, AMD 에서 사용 ^MQ6G7UKK

RISC ^6BCixxbK

- 최대한 instruction을 간결하게 짜는 쪽
- fast, simple, more operations
- ARM, RISC-V 에서 사용 ^iEhLxw13

컴퓨터라면 누구나 할 수 있는 수학적 연산
- operation / operand ^gjWWYZvm

add - operator, 연산 시행
g, h - operand, 연산자
x5, x6 - register! ^XgQQWP0B

register는 CPU의 임시 저장공간,
다양한 종류가 있음 ^5KeRyN42

byte - 8bits
halfword - 16bits
word - 32bits
doubleword - 64bits ^KqjndcrP

RISC-V 같은 경우는 총 32개의 64-bit 레지스터 존재
더 수를 늘리지 않는 이유는 속도 때문 ^H8Qj4rR9

변수를 레지스터에 넣는건
<컴파일러>가 담당 ^SzCUpCqL

하지만 array 등의 이용으로 레지스터가 부족하다면?
 -> memory의 이용

CPU 레지스터에 저장된 데이터 -> 메모리로 이동
 > 하지만 매우 느리다 (캐시까지 다 거쳐서 오기 때문)
 > memory hierarchy ^IaoXUppA

레지스터와 메모리 사이의 데이터 이동은 
<memory address>를 이용

주소 사이의 간격은 무조건 1byte

보통 64bit이므로 2^64 - 1만큼 저장가능

운영체제마다 다르지만, 대개
char - 1byte, int/float - 4bytes, 
long/double - 8bytes만큼 저장

레지스터에 쓰는 행위를 load,
memory에 저장하는 행위를 store ^dA191UfA

0 ^Kx2dHAWs

1 ^0NRLXXpV

0000 1011 ^U7KXNfZ4

0010 1010 ^87uFiNXv

... ^MlfzEXr4

RAM = 1D array ^3Y2j5Fdn

a[8]에 어떻게 접근할 것인가

1. doubleword array -> 한 칸당 8bytes 차지.
2. [8] -> 8th element
3. base register -> x22
4. 결론은 x22에서 8 * 8 = 64bytes 이동
5. 64(x22)

앞의 operator마다 다름
lb - load byte
lh - load halfword
lw - load word
ld - load doubleword
뛰어넘는 간격은 모두 byte 단위지만, 
읽는 범위가 다름 ^fFc86EPy

store의 경우도 load와 비슷함

아래의 예시는 x9를 중복 사용해 레지스터를 아낌

a[12]는 96(x22)

RISC-V 같은 경우는 alignment restriction,
즉 word나 double word의 길이가 4나 8의 배수가 될 필요 x ^5jGvaqGl

빅 엔디안
- 가장 큰 바이트부터 낮은 레지스터에 저장
- IBM만 사용

리틀 엔디안
- 가장 작은 바이트부터 낮은 레지스터에 저장
- intel, ARM, RISC-V 등 대부분이 사용  ^D1tOryiO

CPU에서 자주 사용하는 것은 레지스터에 저장,
자주 사용하지 않는 것은 메모리로 이동

Spilling - 메모리로 데이터가 이동하는 것

메모리로 이동하면 매우 느려짐 ^pVT7JCbw

Constant 사용시
load, store 과정이 없어지므로
굉장히 빨라짐 ^If5ukpSg

0은 매우 자주 사용하기 때문에 x0 레지스터에 따로 저장해놓음
쓰기는 무시됨 ^it1Vi1Lz

운영체제마다 데이터 타입이 차지하는 바이트가 다름

그래서 혹시 모르니까 int64, int32같은 걸 쓴다 ^3mrlKz47

0.00000000000000000001 같은 ^ndRNtoCU

컴퓨터는 2진수로 받아들이는데
사람은 10진수 단위로 개발함
-> 제조사는 소비자를 속이나요 ^1X7M9Inz

무엇보다 연산이 몹시 힘들어짐
-> 아하 컴퓨터는 연산하는 기계구나~ ^SGHShFMe

- Two's complement

- 1으로 시작하면 음수
- 11...11111은 -1
- MSB = sign bit
 ^Er39qOlA

MSB가 제일 큰 음수구나~ ^UE31vryE

- One's complement

- 2^n - x -1
- 물론 two's complement가 더 자주 쓰임 ^X8brBnxo

- Biased notation

- 000...000 = most negative number
- 111...111 = most positive number
- 0111...111 = 0
- negative sign 변환은 flip -> 1 빼기

- 예를 들어, bias = 3일 때...
- 000 -> -3...
- 011 -> 0...

- two's complement가 주로 사용
- 이거는 float가 부분적으로 사용
 ^W77egtbv

RISC-V에서 sign/unsigned 를 저장하는 방법

1. 만약 int x = 2;라면 4bytes 로 저장을 할 것임
2. register의 용량은 64bit (8B) 이므로 절반이 남을 것임
3. 그럼 남은 절반을 어떻게 채울 것인가?

- unsigned의 경우 무조건 0으로 채움 = zero extension
- signed의 경우 sign bit로 채움 = sign extension

그래서 이를 구분하기 위해
ldu, lwu, lhu, lbu를 쓴다 ^MXOBIaej

예시 ^NvxFHYHu

sign/unsigned를 어떻게 구분할 것이냐??

array, memory address를 표현할 때는 모두 양수
-> int 쓰면 바보
-> unsigned int는 더 좋음
-> size_t가 제일 좋음

- pointer는 언제나 64-bit
 ^njt4Npv4

- 컴퓨터는 operator, oparand를 어떻게 구분할까

1. 각 레지스터(x0-x31) - 5bits 사용해서 specify
2. operator들은 mapping해서 인코딩
3. 여러개를 붙이면 instruction! ^rpjPEYk5

- RISC는 고정된 instruction length를 가진다
    - 32bit, 6segments (보통)

- 오른쪽부터 읽어요
- operator (7bits)
- operand (5bits)
- 그 외 등등 ^uxXYNNGq

R-Type은 두 개의 source register를 가진 instruction

- opcode
- rd
- funct3
- rs1
- rs2
- funct7 ^yWInQKAg

I-Type - constant, one resource register를 가지는

- opcode
- rd 
- funct3
- rs1
- immediate
    - 원래는 5bits였지만, 이러면 표현할 수 있는 수가 적어짐
    - 위의 funct7과 rs2를 통합시켜 10bit로 사용 ^F6KJKQB3

 addi ^3pBll8lH


# Embedded files
d4b3407cb6d313443577ed57d3a38a3c6de91ef2: [[2_instructions.pdf#page=1]]
770ee617fc7dd06b9d4d3078794425af6655287f: [[2_instructions.pdf#page=2]]
b077caa7d4790193c00b524e632fd07578363b18: [[2_instructions.pdf#page=3]]
48001aadd9d2ca0e352c205e9321f3df7c404222: [[2_instructions.pdf#page=4]]
9a0092484a0d0e3fc0222d0b07204f9026ce0ba0: [[2_instructions.pdf#page=5]]
2dec1b93adc546fddfed17cae62777503dafe198: [[2_instructions.pdf#page=6]]
feb94b6d9b441cc6d5bb1b0e4dae0fb228bc1ed3: [[2_instructions.pdf#page=7]]
a253764f2b78aff915f8120dd81a8f085efe83ba: [[2_instructions.pdf#page=8]]
327dc2c966d581f5c8633d0e196d266374233bf5: [[2_instructions.pdf#page=9]]
e23d2c3e56af3fe57fab94a9d0eab036932c6f7e: [[2_instructions.pdf#page=10]]
d603462cc6b7d3c9ce7c4be08a37b6998ee1d179: [[2_instructions.pdf#page=11]]
8964a02494650097d34fbd57b5b291c88c5f9eb7: [[2_instructions.pdf#page=12]]
5b02659be381bb41c532200ee6b9fd62f0b30b51: [[2_instructions.pdf#page=13]]
bd06deab7d00adb8d2f549267bbccc18043b3e4d: [[2_instructions.pdf#page=14]]
15ce083b8cdcdd1f965ff9124bdd59d26d42cebe: [[2_instructions.pdf#page=15]]
a7780c1d52b390f2cb822e13200569ec3485fd3f: [[2_instructions.pdf#page=16]]
fd5eec783e5f0fc564d786771f5c889d6de281b8: [[2_instructions.pdf#page=17]]
86f31d93b13f9a383d4c7c4f8d02adca9d1aeee6: [[2_instructions.pdf#page=18]]
894653b32892d711e5a7c1dacba040c785a8bcde: [[2_instructions.pdf#page=19]]
378a6ed6eaed39c13fa9fa1bb864400ce37b11fe: [[2_instructions.pdf#page=20]]
caf8dcb5999e0100531cd57ddb4dcf24552528a2: [[2_instructions.pdf#page=21]]
cc8ad6c0b52360b69464d8532a18eba168040fc6: [[2_instructions.pdf#page=22]]
cf1c62445a7fd06c71c047bb938d65b410b30a7f: [[2_instructions.pdf#page=23]]
81fdb680795df746ef7bbe48709a9ee1b9dcd015: [[2_instructions.pdf#page=24]]
824123857f5405e1e271ff5f9f0948aea314bd35: [[2_instructions.pdf#page=25]]
0326e5059ecc3b216ede849a0621f2a78deabd24: [[2_instructions.pdf#page=26]]
e9763ec4eab43eb1653305376265e1e2364e3c4a: [[2_instructions.pdf#page=27]]
875e1c2cfd04f1d395e32d1c381cb7bc746908bf: [[2_instructions.pdf#page=28]]
57ae8976b720f7dc82b9109107fe57efb2e5a6bb: [[2_instructions.pdf#page=29]]
17a1c02d19355805d3805b43d317ef28465ba063: [[2_instructions.pdf#page=30]]
196225a28fc8a1edaf6cbe0a43b501b427e3445e: [[2_instructions.pdf#page=31]]
8e5b4b8f770afa89e6edbdec2f5fd65c2b1a0f46: [[2_instructions.pdf#page=32]]
21234b69e2937d644c751a4556acb32fc1298e38: [[2_instructions.pdf#page=33]]
6a1d4be6cf2306f1622d6ff28fec2970a3187162: [[2_instructions.pdf#page=34]]
0e532fc653b75d07c4c276185601f89935ada26d: [[2_instructions.pdf#page=35]]
15f9ab2c53185cc1df16c71a4cf2a6f768f31f3b: [[2_instructions.pdf#page=36]]
4e9b17583be7cfac8963b394bd64e34d295bef5a: [[2_instructions.pdf#page=37]]
04d258dd8b84c1e28b6f8f8edb2c46ddab5f1229: [[2_instructions.pdf#page=38]]
f725d153435b844bb8cf464b496632ba3330a609: [[2_instructions.pdf#page=39]]
b11b14d0f44fc7c88852a41c8bb1701af8e70b28: [[2_instructions.pdf#page=40]]
e813b441d2831c374c07032345ec896d6c35ebd1: [[2_instructions.pdf#page=41]]
75f033ca395d7ca99d615175ac63d526d56328a6: [[2_instructions.pdf#page=42]]
62c482ee90767cdd586958e00a1af52562c7f3bf: [[2_instructions.pdf#page=43]]
c4a8247be6facfba84d3f9c24f2709e693afee7a: [[2_instructions.pdf#page=44]]
3a138cb1d48a9dccaee2e5ea2509f7dbed739314: [[2_instructions.pdf#page=45]]
fb3495785ac4e6ded56d6924a1bf14b7ca6f9f9e: [[2_instructions.pdf#page=46]]
ce8f647da8edd5f67a224ec886f283cc55447aa8: [[2_instructions.pdf#page=47]]
1586d06bfee3b478386ad0d18506973be205fb17: [[2_instructions.pdf#page=48]]
f473a9ce1be649e7d81ed2d9100158cb49dac565: [[2_instructions.pdf#page=49]]
ad83bc806e649501a772f48f17e36e6a5df9d86d: [[2_instructions.pdf#page=50]]
b47fe2331d6945decfb2026af331d665ad7b7cb6: [[2_instructions.pdf#page=51]]
8a12417ccff5ee807ef1675aafb82c36327b3348: [[2_instructions.pdf#page=52]]
d6ee983437a18f62fb612df1e2e225f2a314a0fa: [[2_instructions.pdf#page=53]]
cc72e2c90d4a16fa479f97875a2c8858d33456dc: [[2_instructions.pdf#page=54]]
02e1875075786c71f1b1485e05f7bc0c13f0bd21: [[2_instructions.pdf#page=55]]
038a79601c721183bcc2175cd91f531aa49fb94b: [[2_instructions.pdf#page=56]]
ec8af1c8551c31a4ec788a516389c83f41e2fcca: [[2_instructions.pdf#page=57]]
87bdffecae2feae111dff84b2ea922116cb2b20d: [[2_instructions.pdf#page=58]]
1e889aa1fba5e9abe912d7b24df1b8d1a7485b9f: [[2_instructions.pdf#page=59]]
749c53274d34629ed56d3535ee7c60cb156d42dc: [[2_instructions.pdf#page=60]]
2b9a642e2e6f641e7241fed15076a8572b95199b: [[2_instructions.pdf#page=61]]
b681ef128ac37a8cda38c3db639b491b700f3848: [[2_instructions.pdf#page=62]]
d2a54f1dcd40d87f2c256b2ca6d759acf2ec2190: [[2_instructions.pdf#page=63]]
2a6add797b8456f50f6dd764be78c90070fe5eef: [[2_instructions.pdf#page=64]]
2033e3f7bbdc14317445116bbdcaba1bd1b701ce: [[2_instructions.pdf#page=65]]
23903330023eb830c00ae8ede7c2494eba4c9359: [[2_instructions.pdf#page=66]]
b5e659765928bd977eaa7584127139a5cbc02924: [[2_instructions.pdf#page=67]]
51d332beedb0e7f0f8b741fb704fdf9d7568dec1: [[2_instructions.pdf#page=68]]
dedcc9f3a65967631cd65cae68c7caec9ed2609f: [[2_instructions.pdf#page=69]]
913c6099abd1943c8cf47b519e55b666b2ec6ae9: [[2_instructions.pdf#page=70]]
75e1f368298d8325f7cb0b8f7c549e93f1a2db9b: [[2_instructions.pdf#page=71]]
9fae32434da00259d79cf4d7e70f347c987769da: [[2_instructions.pdf#page=72]]
08ae1cdcd5e4df32548064176b777a4ce1cda65a: [[2_instructions.pdf#page=73]]
9f95871b3d6df1334f97a8d28482e593dc18ba3f: [[2_instructions.pdf#page=74]]
d5ba19a1fc410b3298496012c419bb9b7e8bead1: [[2_instructions.pdf#page=75]]
950168b9fdbe7add4e8cdc73e074050ff6e1a6b9: [[2_instructions.pdf#page=76]]
acf042e9e7cf7e1b1acb3ee1c39387f90448fffb: [[2_instructions.pdf#page=77]]
18afb4721893a799b0f0aa644046c00c48199b64: [[2_instructions.pdf#page=78]]
fcbcd41cc230506e6c455c3737b9cffda42da420: [[2_instructions.pdf#page=79]]
a8de8babb0c1b9743e797fbc86672d2f9671258d: [[2_instructions.pdf#page=80]]

%%
# Drawing
```json
{
	"type": "excalidraw",
	"version": 2,
	"source": "https://github.com/zsviczian/obsidian-excalidraw-plugin/releases/tag/2.0.20",
	"elements": [
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1314682866,
			"isDeleted": false,
			"id": "fmXCjay0",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -9204.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 29475,
			"groupIds": [
				"Wd54WPOV"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670714,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 767342638,
			"isDeleted": false,
			"id": "YS4BEsqL",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -9204.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 56623,
			"groupIds": [
				"Wd54WPOV"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670714,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "d4b3407cb6d313443577ed57d3a38a3c6de91ef2",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 598518194,
			"isDeleted": false,
			"id": "xaQ5U4hN",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -9204.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 22843,
			"groupIds": [
				"klGHAN4Q"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670714,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 974226030,
			"isDeleted": false,
			"id": "6Axs4S4l",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -9204.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 55792,
			"groupIds": [
				"klGHAN4Q"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670714,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "770ee617fc7dd06b9d4d3078794425af6655287f",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1267770226,
			"isDeleted": false,
			"id": "hT3SNXoa",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -8752.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 91263,
			"groupIds": [
				"4aPH3Zhf"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670714,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 1842545838,
			"isDeleted": false,
			"id": "o9cXDpIR",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -8752.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 31374,
			"groupIds": [
				"4aPH3Zhf"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670714,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "b077caa7d4790193c00b524e632fd07578363b18",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1347380530,
			"isDeleted": false,
			"id": "MYdtyGEH",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -8752.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 99072,
			"groupIds": [
				"KifnikkX"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670714,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 715800302,
			"isDeleted": false,
			"id": "qoNvxT8h",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -8752.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 70692,
			"groupIds": [
				"KifnikkX"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670714,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "48001aadd9d2ca0e352c205e9321f3df7c404222",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1531965170,
			"isDeleted": false,
			"id": "XTZ7IZgp",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -8300.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 39792,
			"groupIds": [
				"YdkQuK26"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670714,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 891302190,
			"isDeleted": false,
			"id": "4u0jY2mm",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -8300.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 90710,
			"groupIds": [
				"YdkQuK26"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670714,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "9a0092484a0d0e3fc0222d0b07204f9026ce0ba0",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1360609458,
			"isDeleted": false,
			"id": "S8zzgPCZ",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -8300.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 89720,
			"groupIds": [
				"M1acQQeB"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670714,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 1486740334,
			"isDeleted": false,
			"id": "M199vO19",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -8300.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 6,
			"groupIds": [
				"M1acQQeB"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670714,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "2dec1b93adc546fddfed17cae62777503dafe198",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1834113650,
			"isDeleted": false,
			"id": "lNRZIKie",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -7848.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 5796,
			"groupIds": [
				"kfTIoHYg"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670714,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 191643054,
			"isDeleted": false,
			"id": "AU3i3Uwa",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -7848.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 29772,
			"groupIds": [
				"kfTIoHYg"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670714,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "feb94b6d9b441cc6d5bb1b0e4dae0fb228bc1ed3",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1589787698,
			"isDeleted": false,
			"id": "lxhIXcoH",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -7848.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 63644,
			"groupIds": [
				"0cuFCCQq"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670714,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 313808878,
			"isDeleted": false,
			"id": "oEXXYAiw",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -7848.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 18880,
			"groupIds": [
				"0cuFCCQq"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670714,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "a253764f2b78aff915f8120dd81a8f085efe83ba",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1666180594,
			"isDeleted": false,
			"id": "PWThHX7y",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -7396.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 48466,
			"groupIds": [
				"AeKB9o6Z"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670714,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 645868078,
			"isDeleted": false,
			"id": "PK1nolCz",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -7396.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 53700,
			"groupIds": [
				"AeKB9o6Z"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670714,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "327dc2c966d581f5c8633d0e196d266374233bf5",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1677875122,
			"isDeleted": false,
			"id": "dD5zFvqb",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -7396.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 81226,
			"groupIds": [
				"wZUc6etc"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670714,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 364229742,
			"isDeleted": false,
			"id": "dCS9A4De",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -7396.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 83524,
			"groupIds": [
				"wZUc6etc"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670714,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "e23d2c3e56af3fe57fab94a9d0eab036932c6f7e",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 285249906,
			"isDeleted": false,
			"id": "dalqRS56",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -6944.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 47929,
			"groupIds": [
				"dDNH0Nau"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670714,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 1780545198,
			"isDeleted": false,
			"id": "PPxC4kf1",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -6944.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 31233,
			"groupIds": [
				"dDNH0Nau"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670714,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "d603462cc6b7d3c9ce7c4be08a37b6998ee1d179",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 2106692402,
			"isDeleted": false,
			"id": "hRvUA7cS",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -6944.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 45822,
			"groupIds": [
				"CleN6P0W"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670714,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 208269550,
			"isDeleted": false,
			"id": "fxqXOXHO",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -6944.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 21229,
			"groupIds": [
				"CleN6P0W"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670714,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "8964a02494650097d34fbd57b5b291c88c5f9eb7",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1008491762,
			"isDeleted": false,
			"id": "JTFPPD5F",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -6492.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 88278,
			"groupIds": [
				"51qalm5s"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670714,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 1746510638,
			"isDeleted": false,
			"id": "C1n7i9o7",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -6492.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 81481,
			"groupIds": [
				"51qalm5s"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670714,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "5b02659be381bb41c532200ee6b9fd62f0b30b51",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 2049437362,
			"isDeleted": false,
			"id": "ezAQCoIJ",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -6492.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 73820,
			"groupIds": [
				"OGnoFAhV"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670714,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 261688686,
			"isDeleted": false,
			"id": "Qf5KSQZI",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -6492.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 55647,
			"groupIds": [
				"OGnoFAhV"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670714,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "bd06deab7d00adb8d2f549267bbccc18043b3e4d",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 475744370,
			"isDeleted": false,
			"id": "gbL8aWjF",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -6040.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 93444,
			"groupIds": [
				"u0dbjHsB"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670714,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 1613836206,
			"isDeleted": false,
			"id": "mC84tM9K",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -6040.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 18430,
			"groupIds": [
				"u0dbjHsB"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670714,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "15ce083b8cdcdd1f965ff9124bdd59d26d42cebe",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1518168626,
			"isDeleted": false,
			"id": "LyeMKJIO",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -6040.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 35328,
			"groupIds": [
				"TakcHM2a"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670714,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 638257646,
			"isDeleted": false,
			"id": "llMf15A6",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -6040.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 67376,
			"groupIds": [
				"TakcHM2a"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670714,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "a7780c1d52b390f2cb822e13200569ec3485fd3f",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1534415858,
			"isDeleted": false,
			"id": "W1dvwB0t",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -5588.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 49508,
			"groupIds": [
				"PETItXLl"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670714,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 1076861998,
			"isDeleted": false,
			"id": "fAAG1tvt",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -5588.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 8437,
			"groupIds": [
				"PETItXLl"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670714,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "fd5eec783e5f0fc564d786771f5c889d6de281b8",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1363805618,
			"isDeleted": false,
			"id": "90f8wd8Q",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -5588.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 97099,
			"groupIds": [
				"hjElzomS"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670714,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 1149757038,
			"isDeleted": false,
			"id": "vZVOQpre",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -5588.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 74927,
			"groupIds": [
				"hjElzomS"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670714,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "86f31d93b13f9a383d4c7c4f8d02adca9d1aeee6",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 354582386,
			"isDeleted": false,
			"id": "xqhJAb7U",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -5136.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 98350,
			"groupIds": [
				"s3bOx4GV"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670714,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 601680046,
			"isDeleted": false,
			"id": "b6NIeUUV",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -5136.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 75511,
			"groupIds": [
				"s3bOx4GV"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670714,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "894653b32892d711e5a7c1dacba040c785a8bcde",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1128644914,
			"isDeleted": false,
			"id": "nK5xlfgn",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -5136.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 24720,
			"groupIds": [
				"dY7qDJRl"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670714,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 1305977582,
			"isDeleted": false,
			"id": "goFz8rFm",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -5136.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 63614,
			"groupIds": [
				"dY7qDJRl"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670714,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "378a6ed6eaed39c13fa9fa1bb864400ce37b11fe",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1461373682,
			"isDeleted": false,
			"id": "UWbIStf4",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -4684.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 88061,
			"groupIds": [
				"dmKd1YLK"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670714,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 1426134318,
			"isDeleted": false,
			"id": "vhcoImFR",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -4684.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 62277,
			"groupIds": [
				"dmKd1YLK"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670714,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "caf8dcb5999e0100531cd57ddb4dcf24552528a2",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1193843890,
			"isDeleted": false,
			"id": "c4esPcjs",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -4684.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 55922,
			"groupIds": [
				"YowG3LU9"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670714,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 314720110,
			"isDeleted": false,
			"id": "OmDCTCFL",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -4684.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 13291,
			"groupIds": [
				"YowG3LU9"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670714,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "cc8ad6c0b52360b69464d8532a18eba168040fc6",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 555103858,
			"isDeleted": false,
			"id": "L9bn5dZG",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -4232.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 27820,
			"groupIds": [
				"xLR5KGx1"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670714,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 1264853422,
			"isDeleted": false,
			"id": "c4wgKc4m",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -4232.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 75399,
			"groupIds": [
				"xLR5KGx1"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670714,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "cf1c62445a7fd06c71c047bb938d65b410b30a7f",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 631937074,
			"isDeleted": false,
			"id": "Vgr71jM3",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -4232.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 32575,
			"groupIds": [
				"zFbR7fqh"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670714,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 1376762862,
			"isDeleted": false,
			"id": "w3WDzDok",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -4232.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 21077,
			"groupIds": [
				"zFbR7fqh"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670714,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "81fdb680795df746ef7bbe48709a9ee1b9dcd015",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1691140594,
			"isDeleted": false,
			"id": "sb5aYARi",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -3780.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 59301,
			"groupIds": [
				"ElXfJpSl"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670714,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 751701550,
			"isDeleted": false,
			"id": "Adp0eiUd",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -3780.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 88176,
			"groupIds": [
				"ElXfJpSl"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670714,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "824123857f5405e1e271ff5f9f0948aea314bd35",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1501803442,
			"isDeleted": false,
			"id": "CFuAS8BC",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -3780.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 19370,
			"groupIds": [
				"5NynKEXz"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670714,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 948443246,
			"isDeleted": false,
			"id": "kyrVugXn",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -3780.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 36363,
			"groupIds": [
				"5NynKEXz"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670714,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "0326e5059ecc3b216ede849a0621f2a78deabd24",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 100035954,
			"isDeleted": false,
			"id": "V4WbWb81",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -3328.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 2647,
			"groupIds": [
				"A6W2X4sn"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670714,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 1292294830,
			"isDeleted": false,
			"id": "JFtxR7CU",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -3328.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 79942,
			"groupIds": [
				"A6W2X4sn"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670714,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "e9763ec4eab43eb1653305376265e1e2364e3c4a",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 258731826,
			"isDeleted": false,
			"id": "j119Lsxr",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -3328.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 66247,
			"groupIds": [
				"UoKbFRLT"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 1626559726,
			"isDeleted": false,
			"id": "Ko2lCmWm",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -3328.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 18682,
			"groupIds": [
				"UoKbFRLT"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "875e1c2cfd04f1d395e32d1c381cb7bc746908bf",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1514879218,
			"isDeleted": false,
			"id": "3QZIaTIv",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -2876.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 26177,
			"groupIds": [
				"MkkrUJai"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 769034030,
			"isDeleted": false,
			"id": "OcLQb7B3",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -2876.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 38310,
			"groupIds": [
				"MkkrUJai"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "57ae8976b720f7dc82b9109107fe57efb2e5a6bb",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 639322802,
			"isDeleted": false,
			"id": "JAOETtf5",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -2876.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 76052,
			"groupIds": [
				"fX0WkN86"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 1410953582,
			"isDeleted": false,
			"id": "BMDRTv0M",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -2876.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 94124,
			"groupIds": [
				"fX0WkN86"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "17a1c02d19355805d3805b43d317ef28465ba063",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 696460402,
			"isDeleted": false,
			"id": "GdwKUtHL",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -2424.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 23297,
			"groupIds": [
				"zZkRdAjX"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 2131039150,
			"isDeleted": false,
			"id": "LvniaEfp",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -2424.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 75058,
			"groupIds": [
				"zZkRdAjX"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "196225a28fc8a1edaf6cbe0a43b501b427e3445e",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 776586802,
			"isDeleted": false,
			"id": "eTQnlwOY",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -2424.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 39331,
			"groupIds": [
				"vSCxlFnZ"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 146959854,
			"isDeleted": false,
			"id": "gjW5uxVo",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -2424.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 90773,
			"groupIds": [
				"vSCxlFnZ"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "8e5b4b8f770afa89e6edbdec2f5fd65c2b1a0f46",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 760623090,
			"isDeleted": false,
			"id": "Lv6rXr0M",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -1972.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 17723,
			"groupIds": [
				"4DasTi7D"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 509247534,
			"isDeleted": false,
			"id": "4A6VitJm",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -1972.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 74216,
			"groupIds": [
				"4DasTi7D"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "21234b69e2937d644c751a4556acb32fc1298e38",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1789878706,
			"isDeleted": false,
			"id": "pwE7gXMg",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -1972.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 84338,
			"groupIds": [
				"jfkaGK5B"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 1672890990,
			"isDeleted": false,
			"id": "PGGm1IVP",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -1972.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 2394,
			"groupIds": [
				"jfkaGK5B"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "6a1d4be6cf2306f1622d6ff28fec2970a3187162",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 293362546,
			"isDeleted": false,
			"id": "7mQQoGO2",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -1520.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 26398,
			"groupIds": [
				"T1fRIlS0"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 396283054,
			"isDeleted": false,
			"id": "N0cXxnYI",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -1520.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 84181,
			"groupIds": [
				"T1fRIlS0"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "0e532fc653b75d07c4c276185601f89935ada26d",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1342446898,
			"isDeleted": false,
			"id": "Z99e0GSh",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -1520.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 97845,
			"groupIds": [
				"35DmKogV"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 935134958,
			"isDeleted": false,
			"id": "LSfo4Ob5",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -1520.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 68607,
			"groupIds": [
				"35DmKogV"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "15f9ab2c53185cc1df16c71a4cf2a6f768f31f3b",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1940760306,
			"isDeleted": false,
			"id": "HoKrsjQi",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -1068.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 59929,
			"groupIds": [
				"9iGOhIgq"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 614070574,
			"isDeleted": false,
			"id": "DM0oguOx",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -1068.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 52550,
			"groupIds": [
				"9iGOhIgq"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "4e9b17583be7cfac8963b394bd64e34d295bef5a",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 83884210,
			"isDeleted": false,
			"id": "8qvtb1Vs",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -1068.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 94445,
			"groupIds": [
				"DjyHimkn"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 1168024430,
			"isDeleted": false,
			"id": "wimIwP2W",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -1068.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 38729,
			"groupIds": [
				"DjyHimkn"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "04d258dd8b84c1e28b6f8f8edb2c46ddab5f1229",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1671565938,
			"isDeleted": false,
			"id": "MLm04Fgr",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -616.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 51320,
			"groupIds": [
				"AwGKWCMa"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 756286894,
			"isDeleted": false,
			"id": "XEwZjV78",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -616.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 90689,
			"groupIds": [
				"AwGKWCMa"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "f725d153435b844bb8cf464b496632ba3330a609",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1650127922,
			"isDeleted": false,
			"id": "9UXqMuM8",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -616.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 36418,
			"groupIds": [
				"GXxvFISQ"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 1008934894,
			"isDeleted": false,
			"id": "vL1Zlk6V",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -616.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 53909,
			"groupIds": [
				"GXxvFISQ"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "b11b14d0f44fc7c88852a41c8bb1701af8e70b28",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1662098930,
			"isDeleted": false,
			"id": "0vrDS4NR",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -164.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 4075,
			"groupIds": [
				"aOeskCme"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 1188360750,
			"isDeleted": false,
			"id": "HgEvM5KW",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -164.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 74610,
			"groupIds": [
				"aOeskCme"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "e813b441d2831c374c07032345ec896d6c35ebd1",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1926041522,
			"isDeleted": false,
			"id": "ZTxKOicl",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -164.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 45117,
			"groupIds": [
				"Z49mNCOO"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 940735598,
			"isDeleted": false,
			"id": "hbhqUrVx",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -164.698486328125,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 47613,
			"groupIds": [
				"Z49mNCOO"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "75f033ca395d7ca99d615175ac63d526d56328a6",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1706314098,
			"isDeleted": false,
			"id": "6xvOPCj2",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": 287.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 79933,
			"groupIds": [
				"spRA4ma4"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 899989166,
			"isDeleted": false,
			"id": "AfwXpccG",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": 287.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 73506,
			"groupIds": [
				"spRA4ma4"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "62c482ee90767cdd586958e00a1af52562c7f3bf",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1930316594,
			"isDeleted": false,
			"id": "ZgZEeuJN",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": 287.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 92440,
			"groupIds": [
				"5jZ29J5a"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 1144305902,
			"isDeleted": false,
			"id": "dFVWG4y5",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": 287.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 80533,
			"groupIds": [
				"5jZ29J5a"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "c4a8247be6facfba84d3f9c24f2709e693afee7a",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1363285234,
			"isDeleted": false,
			"id": "wDk2jwzr",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": 739.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 9638,
			"groupIds": [
				"Fhg38xSd"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 1800104750,
			"isDeleted": false,
			"id": "rGAZpwCd",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": 739.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 99052,
			"groupIds": [
				"Fhg38xSd"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "3a138cb1d48a9dccaee2e5ea2509f7dbed739314",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1373021874,
			"isDeleted": false,
			"id": "pykeuWUv",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": 739.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 78904,
			"groupIds": [
				"VKBluetF"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 1498535278,
			"isDeleted": false,
			"id": "6HPc9Pia",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": 739.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 73458,
			"groupIds": [
				"VKBluetF"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "fb3495785ac4e6ded56d6924a1bf14b7ca6f9f9e",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 2104688754,
			"isDeleted": false,
			"id": "8MyyBSLf",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": 1191.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 33462,
			"groupIds": [
				"TO46TAdq"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 126941102,
			"isDeleted": false,
			"id": "rh6nYSbN",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": 1191.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 88585,
			"groupIds": [
				"TO46TAdq"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "ce8f647da8edd5f67a224ec886f283cc55447aa8",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 803086898,
			"isDeleted": false,
			"id": "wXA4Lgog",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": 1191.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 17844,
			"groupIds": [
				"eYQUj5qA"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 1580323310,
			"isDeleted": false,
			"id": "5pHL3ynb",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": 1191.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 75580,
			"groupIds": [
				"eYQUj5qA"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "1586d06bfee3b478386ad0d18506973be205fb17",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 872352754,
			"isDeleted": false,
			"id": "G4jim2MH",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": 1643.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 79956,
			"groupIds": [
				"CpZC0Kce"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 1480418350,
			"isDeleted": false,
			"id": "jdmHNxwp",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": 1643.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 97413,
			"groupIds": [
				"CpZC0Kce"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "f473a9ce1be649e7d81ed2d9100158cb49dac565",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1608302002,
			"isDeleted": false,
			"id": "lI2pX7Lx",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": 1643.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 74583,
			"groupIds": [
				"dSd94kfq"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 664579694,
			"isDeleted": false,
			"id": "5tzzFI5b",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": 1643.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 60455,
			"groupIds": [
				"dSd94kfq"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "ad83bc806e649501a772f48f17e36e6a5df9d86d",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 815675250,
			"isDeleted": false,
			"id": "KbbQBTsQ",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": 2095.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 24654,
			"groupIds": [
				"Nvko9eim"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 1494790318,
			"isDeleted": false,
			"id": "UXIU64w7",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": 2095.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 2152,
			"groupIds": [
				"Nvko9eim"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "b47fe2331d6945decfb2026af331d665ad7b7cb6",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1720351026,
			"isDeleted": false,
			"id": "M6QDtVeM",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": 2095.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 64673,
			"groupIds": [
				"SIaX80cd"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 2019191534,
			"isDeleted": false,
			"id": "IH9YeVWY",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": 2095.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 18701,
			"groupIds": [
				"SIaX80cd"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "8a12417ccff5ee807ef1675aafb82c36327b3348",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 554205938,
			"isDeleted": false,
			"id": "kTAXXMAl",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": 2547.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 97594,
			"groupIds": [
				"Ibl7Mga4"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 871030062,
			"isDeleted": false,
			"id": "JWTgTX0R",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": 2547.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 71316,
			"groupIds": [
				"Ibl7Mga4"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "d6ee983437a18f62fb612df1e2e225f2a314a0fa",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 2057262258,
			"isDeleted": false,
			"id": "Hv8vClR9",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": 2547.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 80756,
			"groupIds": [
				"AVKl230x"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 20121454,
			"isDeleted": false,
			"id": "ms91zmTZ",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": 2547.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 32064,
			"groupIds": [
				"AVKl230x"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "cc72e2c90d4a16fa479f97875a2c8858d33456dc",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 620097138,
			"isDeleted": false,
			"id": "FP6dKmVR",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": 2999.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 84586,
			"groupIds": [
				"nGbRKx9A"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 1081862574,
			"isDeleted": false,
			"id": "xxjMPGfB",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": 2999.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 88246,
			"groupIds": [
				"nGbRKx9A"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "02e1875075786c71f1b1485e05f7bc0c13f0bd21",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 80957490,
			"isDeleted": false,
			"id": "U1ZMTQin",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": 2999.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 44884,
			"groupIds": [
				"bhFi3Gn3"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 1626244078,
			"isDeleted": false,
			"id": "gh53O06N",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": 2999.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 21952,
			"groupIds": [
				"bhFi3Gn3"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "038a79601c721183bcc2175cd91f531aa49fb94b",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1310620146,
			"isDeleted": false,
			"id": "maXpeZJg",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": 3451.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 87361,
			"groupIds": [
				"iiOApWFE"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 76797486,
			"isDeleted": false,
			"id": "Lv5vJLwU",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": 3451.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 51566,
			"groupIds": [
				"iiOApWFE"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "ec8af1c8551c31a4ec788a516389c83f41e2fcca",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 534670258,
			"isDeleted": false,
			"id": "yAOLmXx5",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": 3451.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 230,
			"groupIds": [
				"RcUzuELx"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 609542254,
			"isDeleted": false,
			"id": "AT1Zx3jo",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": 3451.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 81118,
			"groupIds": [
				"RcUzuELx"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "87bdffecae2feae111dff84b2ea922116cb2b20d",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 540681586,
			"isDeleted": false,
			"id": "UWPNyw0F",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": 3903.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 37123,
			"groupIds": [
				"3Mi3sZfn"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 872063662,
			"isDeleted": false,
			"id": "DSVwQtmR",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": 3903.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 78250,
			"groupIds": [
				"3Mi3sZfn"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "1e889aa1fba5e9abe912d7b24df1b8d1a7485b9f",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 410560306,
			"isDeleted": false,
			"id": "crTzwtx0",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": 3903.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 40061,
			"groupIds": [
				"8clE6gAd"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 1177427182,
			"isDeleted": false,
			"id": "9qdHNysG",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": 3903.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 45567,
			"groupIds": [
				"8clE6gAd"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "749c53274d34629ed56d3535ee7c60cb156d42dc",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 285274354,
			"isDeleted": false,
			"id": "WByIiszo",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": 4355.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 38161,
			"groupIds": [
				"yxlE0pBA"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 813190958,
			"isDeleted": false,
			"id": "1uAgc8iP",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": 4355.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 34287,
			"groupIds": [
				"yxlE0pBA"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "2b9a642e2e6f641e7241fed15076a8572b95199b",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1834615474,
			"isDeleted": false,
			"id": "vSeumPOE",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": 4355.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 19909,
			"groupIds": [
				"RMl72BvJ"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 792869230,
			"isDeleted": false,
			"id": "HB1LY5wO",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": 4355.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 55338,
			"groupIds": [
				"RMl72BvJ"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "b681ef128ac37a8cda38c3db639b491b700f3848",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 137026674,
			"isDeleted": false,
			"id": "AjKe3yLC",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": 4807.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 86382,
			"groupIds": [
				"GT98Bkwf"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 164944814,
			"isDeleted": false,
			"id": "GnpPyYq9",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": 4807.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 93320,
			"groupIds": [
				"GT98Bkwf"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "d2a54f1dcd40d87f2c256b2ca6d759acf2ec2190",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1329233458,
			"isDeleted": false,
			"id": "agkfeGwA",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": 4807.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 3802,
			"groupIds": [
				"vsfmR2QR"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 911816174,
			"isDeleted": false,
			"id": "k0YSSyoG",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": 4807.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 61682,
			"groupIds": [
				"vsfmR2QR"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "2a6add797b8456f50f6dd764be78c90070fe5eef",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1601169394,
			"isDeleted": false,
			"id": "OpyfIsEq",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": 5259.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 40300,
			"groupIds": [
				"9ubn2vx9"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 2111326254,
			"isDeleted": false,
			"id": "ah9QCz40",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": 5259.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 20972,
			"groupIds": [
				"9ubn2vx9"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "2033e3f7bbdc14317445116bbdcaba1bd1b701ce",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 550640050,
			"isDeleted": false,
			"id": "iFLbm6VU",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": 5259.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 63730,
			"groupIds": [
				"17MHEatw"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 540742254,
			"isDeleted": false,
			"id": "YVSyEXVK",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": 5259.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 26974,
			"groupIds": [
				"17MHEatw"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "23903330023eb830c00ae8ede7c2494eba4c9359",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1653085042,
			"isDeleted": false,
			"id": "bV0i3tsJ",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": 5711.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 16743,
			"groupIds": [
				"HjdvByPe"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 2018153646,
			"isDeleted": false,
			"id": "ROoc6I2r",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": 5711.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 18832,
			"groupIds": [
				"HjdvByPe"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "b5e659765928bd977eaa7584127139a5cbc02924",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1993921842,
			"isDeleted": false,
			"id": "NA0ILnZC",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": 5711.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 74056,
			"groupIds": [
				"PeMggLvq"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 531615470,
			"isDeleted": false,
			"id": "S3R8wkwf",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": 5711.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 63720,
			"groupIds": [
				"PeMggLvq"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "51d332beedb0e7f0f8b741fb704fdf9d7568dec1",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1328242418,
			"isDeleted": false,
			"id": "I9F3tpBK",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": 6163.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 66827,
			"groupIds": [
				"ax5DYkYr"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 317964590,
			"isDeleted": false,
			"id": "lVBGLjEK",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": 6163.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 17881,
			"groupIds": [
				"ax5DYkYr"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "dedcc9f3a65967631cd65cae68c7caec9ed2609f",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 403091634,
			"isDeleted": false,
			"id": "FuZeN9Db",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": 6163.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 15036,
			"groupIds": [
				"Tim3s1rE"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 1434413934,
			"isDeleted": false,
			"id": "gfufC9IH",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": 6163.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 18862,
			"groupIds": [
				"Tim3s1rE"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670715,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "913c6099abd1943c8cf47b519e55b666b2ec6ae9",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1427229298,
			"isDeleted": false,
			"id": "h7t3ZV4k",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": 6615.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 89144,
			"groupIds": [
				"ZDPmjmZA"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670716,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 362532270,
			"isDeleted": false,
			"id": "209D9xNH",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": 6615.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 3190,
			"groupIds": [
				"ZDPmjmZA"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670716,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "75e1f368298d8325f7cb0b8f7c549e93f1a2db9b",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 2098441266,
			"isDeleted": false,
			"id": "hmgxHQXE",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": 6615.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 74257,
			"groupIds": [
				"YcyLzrgu"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670716,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 1349642222,
			"isDeleted": false,
			"id": "vSFpWDni",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": 6615.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 18706,
			"groupIds": [
				"YcyLzrgu"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670716,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "9fae32434da00259d79cf4d7e70f347c987769da",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 368268786,
			"isDeleted": false,
			"id": "u7XKjm0U",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": 7067.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 76278,
			"groupIds": [
				"cbcnqMkz"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670716,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 1980414510,
			"isDeleted": false,
			"id": "XsRlaFHj",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": 7067.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 76433,
			"groupIds": [
				"cbcnqMkz"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670716,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "08ae1cdcd5e4df32548064176b777a4ce1cda65a",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1354221490,
			"isDeleted": false,
			"id": "jM10BSnq",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": 7067.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 68038,
			"groupIds": [
				"jegFT2xB"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670716,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 223298670,
			"isDeleted": false,
			"id": "LIg6OxA8",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": 7067.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 73103,
			"groupIds": [
				"jegFT2xB"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670716,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "9f95871b3d6df1334f97a8d28482e593dc18ba3f",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 629670258,
			"isDeleted": false,
			"id": "q81dj3fX",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": 7519.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 65182,
			"groupIds": [
				"WZWv7dPJ"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670716,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 1476953774,
			"isDeleted": false,
			"id": "Z7OBkM78",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": 7519.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 66276,
			"groupIds": [
				"WZWv7dPJ"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670716,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "d5ba19a1fc410b3298496012c419bb9b7e8bead1",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1873478450,
			"isDeleted": false,
			"id": "I0SngxNe",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": 7519.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 35192,
			"groupIds": [
				"mbp5yxE4"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670716,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 1994359022,
			"isDeleted": false,
			"id": "IbZqFHdH",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": 7519.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 30183,
			"groupIds": [
				"mbp5yxE4"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670716,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "950168b9fdbe7add4e8cdc73e074050ff6e1a6b9",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 159894770,
			"isDeleted": false,
			"id": "OVQwxYfc",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": 7971.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 40123,
			"groupIds": [
				"cnrd5nCg"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670716,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 224211758,
			"isDeleted": false,
			"id": "OacsxJH5",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": 7971.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 34798,
			"groupIds": [
				"cnrd5nCg"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670716,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "acf042e9e7cf7e1b1acb3ee1c39387f90448fffb",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1755668146,
			"isDeleted": false,
			"id": "5dzmFbAY",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": 7971.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 95302,
			"groupIds": [
				"o4kbZTH5"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670716,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 1709874542,
			"isDeleted": false,
			"id": "oxKbOGxt",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": 7971.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 68551,
			"groupIds": [
				"o4kbZTH5"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670716,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "18afb4721893a799b0f0aa644046c00c48199b64",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 967489650,
			"isDeleted": false,
			"id": "ZgZuEgcV",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": 8423.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 58290,
			"groupIds": [
				"lJdrpUug"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670716,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 366002094,
			"isDeleted": false,
			"id": "pacqqr7k",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": 8423.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 11397,
			"groupIds": [
				"lJdrpUug"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670716,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "fcbcd41cc230506e6c455c3737b9cffda42da420",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 2086591026,
			"isDeleted": false,
			"id": "Sp1TwUOp",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": 8423.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 4184,
			"groupIds": [
				"rUgwzetQ"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670716,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 557357550,
			"isDeleted": false,
			"id": "k2Tn91Cu",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": 8423.301513671875,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 41840,
			"groupIds": [
				"rUgwzetQ"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670716,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "a8de8babb0c1b9743e797fbc86672d2f9671258d",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 341,
			"versionNonce": 531153906,
			"isDeleted": false,
			"id": "t8Mqz3BhEb4Y13vINrpWz",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -981.9474352952545,
			"y": -8621.397328325438,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 362.7341252758317,
			"height": 177.92082375244883,
			"seed": 1178919734,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "T9BBns1U"
				}
			],
			"updated": 1710299670716,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 533,
			"versionNonce": 522923054,
			"isDeleted": false,
			"id": "T9BBns1U",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -976.9474352952545,
			"y": -8616.397328325438,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 346.75177001953125,
			"height": 120,
			"seed": 1086259190,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670716,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 1,
			"text": "Instruction - 컴퓨터가 사용하는 언어\nISA - instruction set들의 짜임 -> standard가\n정해짐\n\n=> 결국 이를 사용하는 이유는 편리하게 기기를\n관리하기 위해서!",
			"rawText": "Instruction - 컴퓨터가 사용하는 언어\nISA - instruction set들의 짜임 -> standard가 정해짐\n\n=> 결국 이를 사용하는 이유는 편리하게 기기를 관리하기 위해서!",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": "t8Mqz3BhEb4Y13vINrpWz",
			"originalText": "Instruction - 컴퓨터가 사용하는 언어\nISA - instruction set들의 짜임 -> standard가 정해짐\n\n=> 결국 이를 사용하는 이유는 편리하게 기기를 관리하기 위해서!",
			"lineHeight": 1.25,
			"baseline": 114
		},
		{
			"type": "text",
			"version": 135,
			"versionNonce": 495941042,
			"isDeleted": false,
			"id": "TSaQ8a8W",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 601.2487079958565,
			"y": -8731.43585427145,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 368.86383056640625,
			"height": 40,
			"seed": 840191542,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670716,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 1,
			"text": "모든 컴퓨터 아키텍쳐의 기반이 됨 = stored-program\n",
			"rawText": "모든 컴퓨터 아키텍쳐의 기반이 됨 = stored-program\n",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "모든 컴퓨터 아키텍쳐의 기반이 됨 = stored-program\n",
			"lineHeight": 1.25,
			"baseline": 34
		},
		{
			"type": "rectangle",
			"version": 101,
			"versionNonce": 1569814126,
			"isDeleted": false,
			"id": "B5z6U6E9Cm61UbO1R5P_q",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 634.5746998343027,
			"y": -8680.235426189389,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 193.5936809859486,
			"height": 117.75618810082415,
			"seed": 1151234538,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "CAz9W5LZ"
				},
				{
					"id": "ajdLtQr6MXH5okIgbOgop",
					"type": "arrow"
				}
			],
			"updated": 1710299670716,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 101,
			"versionNonce": 389672818,
			"isDeleted": false,
			"id": "CAz9W5LZ",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 661.2755625440739,
			"y": -8631.357332138978,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 140.19195556640625,
			"height": 20,
			"seed": 253381098,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670716,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 1,
			"text": "메모리 <=> 프로세서",
			"rawText": "메모리 <=> 프로세서",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "B5z6U6E9Cm61UbO1R5P_q",
			"originalText": "메모리 <=> 프로세서",
			"lineHeight": 1.25,
			"baseline": 14
		},
		{
			"type": "rectangle",
			"version": 160,
			"versionNonce": 87324846,
			"isDeleted": false,
			"id": "Lmt4uWzEAL-LiBON4wn_n",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 913.8808940504575,
			"y": -8652.761423547912,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 82.33292435484816,
			"height": 61.0486553465289,
			"seed": 2077179574,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "oX0Db6O3"
				},
				{
					"id": "ajdLtQr6MXH5okIgbOgop",
					"type": "arrow"
				}
			],
			"updated": 1710299670716,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 133,
			"versionNonce": 1894723890,
			"isDeleted": false,
			"id": "oX0Db6O3",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 940.8793645896981,
			"y": -8632.237095874647,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 28.335983276367188,
			"height": 20,
			"seed": 729602998,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670716,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 1,
			"text": "I/O",
			"rawText": "I/O",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "Lmt4uWzEAL-LiBON4wn_n",
			"originalText": "I/O",
			"lineHeight": 1.25,
			"baseline": 14
		},
		{
			"type": "arrow",
			"version": 260,
			"versionNonce": 1035809518,
			"isDeleted": false,
			"id": "ajdLtQr6MXH5okIgbOgop",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 837.5776170053152,
			"y": -8627.526879798434,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 67.99209489339921,
			"height": 4.9210786081875995,
			"seed": 592014070,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1710299670716,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "B5z6U6E9Cm61UbO1R5P_q",
				"gap": 9.409236185063833,
				"focus": -0.21039353061793092
			},
			"endBinding": {
				"elementId": "Lmt4uWzEAL-LiBON4wn_n",
				"gap": 8.31118215174314,
				"focus": -0.09588001640065921
			},
			"lastCommittedPoint": null,
			"startArrowhead": "arrow",
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					67.99209489339921,
					4.9210786081875995
				]
			]
		},
		{
			"type": "text",
			"version": 108,
			"versionNonce": 1846950642,
			"isDeleted": false,
			"id": "d1bvRq3p",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 725.2814289414068,
			"y": -8600.207837034255,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 91.03997802734375,
			"height": 40,
			"seed": 1367591658,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670716,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 1,
			"text": "프로그램 실행\n",
			"rawText": "프로그램 실행\n",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "프로그램 실행\n",
			"lineHeight": 1.25,
			"baseline": 34
		},
		{
			"type": "text",
			"version": 194,
			"versionNonce": 1370793262,
			"isDeleted": false,
			"id": "UotxPxiC",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -521.4661347417822,
			"y": -7968.190180952794,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 283.7439270019531,
			"height": 40,
			"seed": 2095757930,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670716,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 1,
			"text": "Von neumann 아키텍처를 사용하긴 하는데\n세부적인 작동방식은 모두 다름",
			"rawText": "Von neumann 아키텍처를 사용하긴 하는데\n세부적인 작동방식은 모두 다름",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Von neumann 아키텍처를 사용하긴 하는데\n세부적인 작동방식은 모두 다름",
			"lineHeight": 1.25,
			"baseline": 34
		},
		{
			"type": "rectangle",
			"version": 74,
			"versionNonce": 1295387826,
			"isDeleted": false,
			"id": "X__5oLzTFEKzCsFJuyqSc",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 605.6112138146932,
			"y": -8286.110465383563,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 136.46775002968707,
			"height": 48.55049463544492,
			"seed": 1524322934,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "XqXOQw5O"
				}
			],
			"updated": 1710299670716,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 71,
			"versionNonce": 1384370030,
			"isDeleted": false,
			"id": "XqXOQw5O",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 654.3171118397906,
			"y": -8271.83521806584,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 39.05595397949219,
			"height": 20,
			"seed": 1807395830,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670716,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 1,
			"text": "CISC",
			"rawText": "CISC",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "X__5oLzTFEKzCsFJuyqSc",
			"originalText": "CISC",
			"lineHeight": 1.25,
			"baseline": 14
		},
		{
			"type": "text",
			"version": 187,
			"versionNonce": 1677043314,
			"isDeleted": false,
			"id": "MQ6G7UKK",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 610.8842094598102,
			"y": -8224.339770945237,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 257.1038818359375,
			"height": 60,
			"seed": 1732507894,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670716,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 1,
			"text": "- 가능한 적은 수의 instruction 사용.\n- lower power consumption\n- x86, intel, AMD 에서 사용",
			"rawText": "- 가능한 적은 수의 instruction 사용.\n- lower power consumption\n- x86, intel, AMD 에서 사용",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "- 가능한 적은 수의 instruction 사용.\n- lower power consumption\n- x86, intel, AMD 에서 사용",
			"lineHeight": 1.25,
			"baseline": 54
		},
		{
			"type": "rectangle",
			"version": 101,
			"versionNonce": 1014215086,
			"isDeleted": false,
			"id": "tX8myfQJrr5rOBibd3YnM",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 611.9018140209395,
			"y": -8145.357942944345,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 136.4322486527542,
			"height": 45.49125616782021,
			"seed": 1829405994,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "6BCixxbK"
				}
			],
			"updated": 1710299670716,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 45,
			"versionNonce": 991692850,
			"isDeleted": false,
			"id": "6BCixxbK",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 660.3179581837423,
			"y": -8132.612314860435,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 39.59996032714844,
			"height": 20,
			"seed": 860385962,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670716,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 1,
			"text": "RISC",
			"rawText": "RISC",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "tX8myfQJrr5rOBibd3YnM",
			"originalText": "RISC",
			"lineHeight": 1.25,
			"baseline": 14
		},
		{
			"type": "text",
			"version": 153,
			"versionNonce": 447564782,
			"isDeleted": false,
			"id": "iEhLxw13",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 614.9106445964248,
			"y": -8080.315331904046,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 280.39990234375,
			"height": 60,
			"seed": 552766454,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670716,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 1,
			"text": "- 최대한 instruction을 간결하게 짜는 쪽\n- fast, simple, more operations\n- ARM, RISC-V 에서 사용",
			"rawText": "- 최대한 instruction을 간결하게 짜는 쪽\n- fast, simple, more operations\n- ARM, RISC-V 에서 사용",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "- 최대한 instruction을 간결하게 짜는 쪽\n- fast, simple, more operations\n- ARM, RISC-V 에서 사용",
			"lineHeight": 1.25,
			"baseline": 54
		},
		{
			"type": "freedraw",
			"version": 58,
			"versionNonce": 714093042,
			"isDeleted": false,
			"id": "vipUEY6ER4KWDYVb97JwU",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -350.2420034122119,
			"y": -7691.828157358241,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 76.9265065105854,
			"height": 28.77660859983189,
			"seed": 1991992438,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670716,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.16912673131082556
				],
				[
					-1.5934480685201606,
					1.0415006953890042
				],
				[
					-2.528114505856138,
					2.5963492696755566
				],
				[
					-7.201599058960369,
					5.026568347722787
				],
				[
					-9.845410469899946,
					5.563634600051955
				],
				[
					-12.017444641453949,
					5.563634600051955
				],
				[
					-17.492071855131883,
					5.934545266349232
				],
				[
					-29.23952319218563,
					5.934545266349232
				],
				[
					-38.0107503686196,
					5.934545266349232
				],
				[
					-46.78202833386183,
					5.934545266349232
				],
				[
					-55.08442402178588,
					5.142290647210757
				],
				[
					-61.9744337424288,
					3.61413159163385
				],
				[
					-68.06330080249813,
					0.5904960785574076
				],
				[
					-68.40155426512143,
					-0.08606163549757184
				],
				[
					-68.40155426512143,
					-1.7862931732615834
				],
				[
					-68.40155426512143,
					-5.0443698249964655
				],
				[
					-66.30072600266624,
					-9.21931143679285
				],
				[
					-63.167310480662195,
					-12.696948106384298
				],
				[
					-60.86764403409734,
					-14.45952290621608
				],
				[
					-56.582897018968936,
					-17.319973978539565
				],
				[
					-52.39017932430198,
					-19.678936358680403
				],
				[
					-47.865048879954884,
					-21.408879349242852
				],
				[
					-42.86819198503042,
					-22.48301185390028
				],
				[
					-37.87128430129775,
					-22.842063333482656
				],
				[
					-32.402599378179445,
					-22.842063333482656
				],
				[
					-22.54830086684416,
					-21.699670670601336
				],
				[
					-14.720628169181396,
					-20.138879805755096
				],
				[
					-7.836560739098047,
					-17.848152189433677
				],
				[
					-1.4243213372085393,
					-15.207261134965847
				],
				[
					5.462742632558729,
					-10.889882310567373
				],
				[
					7.486422695355543,
					-9.204481104798106
				],
				[
					8.192641073400239,
					-7.955254183864781
				],
				[
					8.524952245463965,
					-7.284664154773964
				],
				[
					8.524952245463965,
					-5.895971166518393
				],
				[
					8.524952245463965,
					-4.00581488048465
				],
				[
					7.370675001463894,
					-2.8574799270436415
				],
				[
					4.459816036999712,
					-0.23738688953471865
				],
				[
					2.5904323735196613,
					2.8723102590392955
				],
				[
					0.8278575736877656,
					5.171951311200246
				],
				[
					0.8278575736877656,
					5.171951311200246
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 52,
			"versionNonce": 725196334,
			"isDeleted": false,
			"id": "WhPAVaZMfpji3fUxbweER",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -150.6989214335158,
			"y": -7701.329372074957,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 77.2025436831616,
			"height": 27.18615707099434,
			"seed": 652185450,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670716,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-5.145211003681652,
					2.563742854808879
				],
				[
					-8.26090123162328,
					3.777341426788553
				],
				[
					-11.376489881948487,
					4.720946694368649
				],
				[
					-16.851117095626364,
					6.174903301162885
				],
				[
					-27.657959704784616,
					8.480461249479049
				],
				[
					-35.49152390419874,
					9.25788553662278
				],
				[
					-44.26280186944098,
					9.655511116033267
				],
				[
					-53.505857074068786,
					9.655511116033267
				],
				[
					-61.336475522607316,
					9.655511116033267
				],
				[
					-68.84067430083337,
					9.655511116033267
				],
				[
					-69.51723201488824,
					9.317232259006232
				],
				[
					-70.02461220882333,
					8.640699939354818
				],
				[
					-70.60919139122484,
					5.6585842769836745
				],
				[
					-71.2857491052797,
					1.5993649646752601
				],
				[
					-72.22041554261568,
					-1.5162744744584415
				],
				[
					-72.53200488093307,
					-4.16011127980164
				],
				[
					-72.53200488093307,
					-6.803948085145748
				],
				[
					-71.60023340566465,
					-9.786063747516891
				],
				[
					-69.54394692800236,
					-11.848317910143123
				],
				[
					-67.2442804814375,
					-13.610867315570431
				],
				[
					-64.60641136105744,
					-14.545559147310087
				],
				[
					-59.47003761000292,
					-15.222091466961501
				],
				[
					-53.52957544749904,
					-15.963912799555146
				],
				[
					-45.70190274983622,
					-16.747279377258565
				],
				[
					-37.874230052173516,
					-17.530645954961074
				],
				[
					-30.046557354510696,
					-17.530645954961074
				],
				[
					-17.836216819506603,
					-17.530645954961074
				],
				[
					-10.480372150037624,
					-17.150821852825175
				],
				[
					-4.539909987533747,
					-16.038089853934252
				],
				[
					-0.01483033199485817,
					-14.652368010958526
				],
				[
					4.338176841356585,
					-12.168769895491096
				],
				[
					4.50435782179261,
					-12.002614309459204
				],
				[
					4.50435782179261,
					-11.836433329023748
				],
				[
					4.670538802228521,
					-11.059009041880017
				],
				[
					4.501412070916899,
					-10.557545744100935
				],
				[
					3.1424051410557468,
					-8.797942089548087
				],
				[
					3.1424051410557468,
					-8.797942089548087
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 30,
			"versionNonce": 1968776114,
			"isDeleted": false,
			"id": "lNV_zjpCL3r8g8Qd3vKSi",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -391.96780273436144,
			"y": -7584.819439749786,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 40.102690589639565,
			"height": 2.163146130118548,
			"seed": 1966195370,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670716,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.4183790466489654,
					0.5400627920125771
				],
				[
					4.528076195222809,
					0.5400627920125771
				],
				[
					7.637773343796653,
					0.5400627920125771
				],
				[
					11.21924773175607,
					0.5400627920125771
				],
				[
					11.830541827271759,
					0.5400627920125771
				],
				[
					17.106330856839975,
					0.8486555906456488
				],
				[
					20.68785603360766,
					1.15724838927963
				],
				[
					25.21293568914649,
					1.4925561010277306
				],
				[
					29.73801534468538,
					1.8278384183704475
				],
				[
					33.79131776083864,
					2.163146130118548
				],
				[
					37.23632262116013,
					2.163146130118548
				],
				[
					38.654650879000826,
					2.163146130118548
				],
				[
					39.32526630249612,
					2.163146130118548
				],
				[
					40.102690589639565,
					2.163146130118548
				],
				[
					40.102690589639565,
					2.163146130118548
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 28,
			"versionNonce": 50440302,
			"isDeleted": false,
			"id": "yb45C9AuIpFLe4m7eDdGp",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -197.45123831457965,
			"y": -7582.994547082291,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 30.574760959808373,
			"height": 0.47774492434928106,
			"seed": 2061158762,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670716,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.4183282578406988,
					0
				],
				[
					3.5844709276433377,
					0
				],
				[
					6.361806115345189,
					0
				],
				[
					8.999726024533516,
					0
				],
				[
					11.165817905527888,
					-0.2047550802653859
				],
				[
					14.275515054101675,
					-0.47774492434928106
				],
				[
					15.969829695710473,
					-0.47774492434928106
				],
				[
					20.162648967993846,
					-0.47774492434928106
				],
				[
					23.272346116567633,
					-0.47774492434928106
				],
				[
					26.85376971571884,
					-0.47774492434928106
				],
				[
					29.49174041371532,
					-0.47774492434928106
				],
				[
					30.574760959808373,
					-0.47774492434928106
				],
				[
					30.574760959808373,
					-0.47774492434928106
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 24,
			"versionNonce": 1704844658,
			"isDeleted": false,
			"id": "jmVIlVzq5Z7ae-m1oERyr",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -391.76007650881644,
			"y": -7546.8739529997065,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 50.479250415712954,
			"height": 0,
			"seed": 813341354,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670716,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.0830713349012626,
					0
				],
				[
					5.275789029568216,
					0
				],
				[
					8.38548617814206,
					0
				],
				[
					13.382393861874732,
					0
				],
				[
					20.26646129195808,
					0
				],
				[
					32.47680182696212,
					0
				],
				[
					41.71391474103035,
					0
				],
				[
					50.479250415712954,
					0
				],
				[
					50.479250415712954,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 24,
			"versionNonce": 835611310,
			"isDeleted": false,
			"id": "5q8tVZKnqaq3WYizQV2YR",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -395.644252193658,
			"y": -7514.367490508755,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 70.30654088315089,
			"height": 0,
			"seed": 1882314986,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670716,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.2492523153372304,
					0
				],
				[
					2.9435669569460288,
					0
				],
				[
					8.412251880064332,
					0
				],
				[
					22.50675562173518,
					0
				],
				[
					34.57468433854166,
					0
				],
				[
					48.05794477350497,
					0
				],
				[
					60.12582270150324,
					0
				],
				[
					70.30654088315089,
					0
				],
				[
					70.30654088315089,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 26,
			"versionNonce": 1755668274,
			"isDeleted": false,
			"id": "f-Ja1UtBKLm2PNSii9dYw",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -204.47771756286056,
			"y": -7552.016243646916,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 39.117489288142906,
			"height": 0.16912673131173506,
			"seed": 137658154,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670716,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.16912673131173506
				],
				[
					2.3055579483162774,
					-0.16912673131173506
				],
				[
					5.887032336275752,
					-0.16912673131173506
				],
				[
					8.053175006078277,
					-0.16912673131173506
				],
				[
					12.578254661617166,
					-0.16912673131173506
				],
				[
					18.04693958473547,
					-0.16912673131173506
				],
				[
					26.4858048002975,
					-0.16912673131173506
				],
				[
					30.53915800525897,
					-0.16912673131173506
				],
				[
					34.59240963260402,
					-0.16912673131173506
				],
				[
					39.117489288142906,
					-0.16912673131173506
				],
				[
					39.117489288142906,
					-0.16912673131173506
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 25,
			"versionNonce": 1716053230,
			"isDeleted": false,
			"id": "YZB_ddI-fQvstsuUFtlrH",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -213.13919012477072,
			"y": -7514.189475736007,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 47.18554541502442,
			"height": 0.27298984408480464,
			"seed": 797620970,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670716,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.4183282578408125,
					0
				],
				[
					3.584420138835185,
					-0.27298984408480464
				],
				[
					6.222340048023398,
					-0.27298984408480464
				],
				[
					8.86025995721161,
					-0.27298984408480464
				],
				[
					12.913562373364925,
					-0.27298984408480464
				],
				[
					18.854024535868803,
					-0.27298984408480464
				],
				[
					30.123756342977345,
					-0.27298984408480464
				],
				[
					38.42020974034176,
					-0.27298984408480464
				],
				[
					47.18554541502442,
					-0.27298984408480464
				],
				[
					47.18554541502442,
					-0.27298984408480464
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "text",
			"version": 151,
			"versionNonce": 718711026,
			"isDeleted": false,
			"id": "gjWWYZvm",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 596.0188585816577,
			"y": -7823.279941203918,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 283.2799377441406,
			"height": 40,
			"seed": 594255606,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670716,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 1,
			"text": "컴퓨터라면 누구나 할 수 있는 수학적 연산\n- operation / operand",
			"rawText": "컴퓨터라면 누구나 할 수 있는 수학적 연산\n- operation / operand",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "컴퓨터라면 누구나 할 수 있는 수학적 연산\n- operation / operand",
			"lineHeight": 1.25,
			"baseline": 34
		},
		{
			"type": "text",
			"version": 147,
			"versionNonce": 301602606,
			"isDeleted": false,
			"id": "XgQQWP0B",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -797.701401223195,
			"y": -7365.914374469314,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 194.7678985595703,
			"height": 60,
			"seed": 607799146,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670716,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 1,
			"text": "add - operator, 연산 시행\ng, h - operand, 연산자\nx5, x6 - register!",
			"rawText": "add - operator, 연산 시행\ng, h - operand, 연산자\nx5, x6 - register!",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "add - operator, 연산 시행\ng, h - operand, 연산자\nx5, x6 - register!",
			"lineHeight": 1.25,
			"baseline": 54
		},
		{
			"type": "text",
			"version": 146,
			"versionNonce": 867744434,
			"isDeleted": false,
			"id": "5KeRyN42",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -831.5594446068492,
			"y": -7280.271106266116,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 231.64788818359375,
			"height": 40,
			"seed": 404313078,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670716,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 1,
			"text": "register는 CPU의 임시 저장공간,\n다양한 종류가 있음",
			"rawText": "register는 CPU의 임시 저장공간,\n다양한 종류가 있음",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "register는 CPU의 임시 저장공간,\n다양한 종류가 있음",
			"lineHeight": 1.25,
			"baseline": 34
		},
		{
			"type": "text",
			"version": 127,
			"versionNonce": 223019374,
			"isDeleted": false,
			"id": "KqjndcrP",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 607.6769519467957,
			"y": -7379.603151368213,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 155.15187072753906,
			"height": 80,
			"seed": 1325744758,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670716,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 1,
			"text": "byte - 8bits\nhalfword - 16bits\nword - 32bits\ndoubleword - 64bits",
			"rawText": "byte - 8bits\nhalfword - 16bits\nword - 32bits\ndoubleword - 64bits",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "byte - 8bits\nhalfword - 16bits\nword - 32bits\ndoubleword - 64bits",
			"lineHeight": 1.25,
			"baseline": 74
		},
		{
			"type": "text",
			"version": 217,
			"versionNonce": 32674930,
			"isDeleted": false,
			"id": "H8Qj4rR9",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 603.0835969332894,
			"y": -7251.104113852202,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 374.22381591796875,
			"height": 40,
			"seed": 1476465398,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670716,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 1,
			"text": "RISC-V 같은 경우는 총 32개의 64-bit 레지스터 존재\n더 수를 늘리지 않는 이유는 속도 때문",
			"rawText": "RISC-V 같은 경우는 총 32개의 64-bit 레지스터 존재\n더 수를 늘리지 않는 이유는 속도 때문",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "RISC-V 같은 경우는 총 32개의 64-bit 레지스터 존재\n더 수를 늘리지 않는 이유는 속도 때문",
			"lineHeight": 1.25,
			"baseline": 34
		},
		{
			"type": "text",
			"version": 106,
			"versionNonce": 998548398,
			"isDeleted": false,
			"id": "SzCUpCqL",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -757.1022837924777,
			"y": -6794.687259294081,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 168.23995971679688,
			"height": 40,
			"seed": 2064178230,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670716,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 1,
			"text": "변수를 레지스터에 넣는건\n<컴파일러>가 담당",
			"rawText": "변수를 레지스터에 넣는건\n<컴파일러>가 담당",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "변수를 레지스터에 넣는건\n<컴파일러>가 담당",
			"lineHeight": 1.25,
			"baseline": 34
		},
		{
			"type": "text",
			"version": 293,
			"versionNonce": 659240498,
			"isDeleted": false,
			"id": "IaoXUppA",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 610.970435994524,
			"y": -6882.569919406659,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 368.60791015625,
			"height": 120,
			"seed": 265742378,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670716,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 1,
			"text": "하지만 array 등의 이용으로 레지스터가 부족하다면?\n -> memory의 이용\n\nCPU 레지스터에 저장된 데이터 -> 메모리로 이동\n > 하지만 매우 느리다 (캐시까지 다 거쳐서 오기 때문)\n > memory hierarchy",
			"rawText": "하지만 array 등의 이용으로 레지스터가 부족하다면?\n -> memory의 이용\n\nCPU 레지스터에 저장된 데이터 -> 메모리로 이동\n > 하지만 매우 느리다 (캐시까지 다 거쳐서 오기 때문)\n > memory hierarchy",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "하지만 array 등의 이용으로 레지스터가 부족하다면?\n -> memory의 이용\n\nCPU 레지스터에 저장된 데이터 -> 메모리로 이동\n > 하지만 매우 느리다 (캐시까지 다 거쳐서 오기 때문)\n > memory hierarchy",
			"lineHeight": 1.25,
			"baseline": 114
		},
		{
			"type": "freedraw",
			"version": 52,
			"versionNonce": 785382894,
			"isDeleted": false,
			"id": "Af9-UIN41V18KnBSGVdFU",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 171.6293858631286,
			"y": -6576.861707237859,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 230.80322073265998,
			"height": 0.7875111301145807,
			"seed": 1662880246,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670716,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5239814621798189,
					-0.17676546997427067
				],
				[
					3.630564283474996,
					-0.5022771459925934
				],
				[
					4.762160465318459,
					-0.7875111301145807
				],
				[
					10.621848234749024,
					-0.7875111301145807
				],
				[
					13.378084123361276,
					-0.7875111301145807
				],
				[
					18.744781434654243,
					-0.7875111301145807
				],
				[
					21.993954714616365,
					-0.7875111301145807
				],
				[
					26.22905584406587,
					-0.7875111301145807
				],
				[
					30.4641569735154,
					-0.7875111301145807
				],
				[
					37.80270998378319,
					-0.7875111301145807
				],
				[
					43.51667635407,
					-0.7875111301145807
				],
				[
					50.216570573844194,
					-0.7875111301145807
				],
				[
					57.4094021849682,
					-0.7875111301145807
				],
				[
					64.1092433379547,
					-0.7875111301145807
				],
				[
					73.91258943854717,
					-0.7875111301145807
				],
				[
					81.10542104967124,
					-0.7875111301145807
				],
				[
					87.31237787809553,
					-0.7875111301145807
				],
				[
					93.51928163973221,
					-0.7875111301145807
				],
				[
					98.74031061866916,
					-0.7875111301145807
				],
				[
					105.58587317079937,
					-0.7875111301145807
				],
				[
					109.32803690889901,
					-0.7875111301145807
				],
				[
					113.07014758021094,
					-0.7875111301145807
				],
				[
					117.30524870966056,
					-0.7875111301145807
				],
				[
					122.67194602095347,
					-0.7875111301145807
				],
				[
					126.41410975905322,
					-0.7875111301145807
				],
				[
					130.64921088850272,
					-0.7875111301145807
				],
				[
					135.87018680065185,
					-0.7875111301145807
				],
				[
					144.68760505175695,
					-0.7875111301145807
				],
				[
					151.88043666288095,
					-0.7875111301145807
				],
				[
					159.07332134079277,
					-0.7875111301145807
				],
				[
					166.26615295191678,
					-0.7875111301145807
				],
				[
					172.47305671355346,
					-0.7875111301145807
				],
				[
					178.67996047519003,
					-0.7875111301145807
				],
				[
					187.49737872629512,
					-0.7875111301145807
				],
				[
					203.01469119717436,
					-0.7875111301145807
				],
				[
					210.20752280829848,
					-0.7875111301145807
				],
				[
					226.21777267052758,
					-0.7875111301145807
				],
				[
					230.45287379997708,
					-0.7875111301145807
				],
				[
					230.80322073265998,
					-0.7875111301145807
				],
				[
					230.80322073265998,
					-0.7875111301145807
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "text",
			"version": 498,
			"versionNonce": 1688838130,
			"isDeleted": false,
			"id": "dA191UfA",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -861.3732680965674,
			"y": -6482.172515195531,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 284.8798828125,
			"height": 260,
			"seed": 445650870,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670716,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 1,
			"text": "레지스터와 메모리 사이의 데이터 이동은 \n<memory address>를 이용\n\n주소 사이의 간격은 무조건 1byte\n\n보통 64bit이므로 2^64 - 1만큼 저장가능\n\n운영체제마다 다르지만, 대개\nchar - 1byte, int/float - 4bytes, \nlong/double - 8bytes만큼 저장\n\n레지스터에 쓰는 행위를 load,\nmemory에 저장하는 행위를 store",
			"rawText": "레지스터와 메모리 사이의 데이터 이동은 \n<memory address>를 이용\n\n주소 사이의 간격은 무조건 1byte\n\n보통 64bit이므로 2^64 - 1만큼 저장가능\n\n운영체제마다 다르지만, 대개\nchar - 1byte, int/float - 4bytes, \nlong/double - 8bytes만큼 저장\n\n레지스터에 쓰는 행위를 load,\nmemory에 저장하는 행위를 store",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "레지스터와 메모리 사이의 데이터 이동은 \n<memory address>를 이용\n\n주소 사이의 간격은 무조건 1byte\n\n보통 64bit이므로 2^64 - 1만큼 저장가능\n\n운영체제마다 다르지만, 대개\nchar - 1byte, int/float - 4bytes, \nlong/double - 8bytes만큼 저장\n\n레지스터에 쓰는 행위를 load,\nmemory에 저장하는 행위를 store",
			"lineHeight": 1.25,
			"baseline": 254
		},
		{
			"type": "rectangle",
			"version": 83,
			"versionNonce": 1278611502,
			"isDeleted": false,
			"id": "SOnc6PT3-08uvgw-gbqMJ",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1049.8163765806335,
			"y": -6442.8641677764945,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 151.02781258420532,
			"height": 37.18883338316573,
			"seed": 759955050,
			"groupIds": [
				"Sa4UO2A-icw4ijMTyuKTY"
			],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [],
			"updated": 1710299670716,
			"link": null,
			"locked": false
		},
		{
			"type": "rectangle",
			"version": 134,
			"versionNonce": 1175769522,
			"isDeleted": false,
			"id": "UJFwZ2W9SfaMuBFqDUrqS",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1050.955534779731,
			"y": -6402.389359296065,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 151.02781258420532,
			"height": 37.18883338316573,
			"seed": 889173174,
			"groupIds": [
				"Sa4UO2A-icw4ijMTyuKTY"
			],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "MlfzEXr4"
				}
			],
			"updated": 1710299670716,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 15,
			"versionNonce": 1872747118,
			"isDeleted": false,
			"id": "MlfzEXr4",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -982.017609627765,
			"y": -6393.794942604482,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 13.151962280273438,
			"height": 20,
			"seed": 210832438,
			"groupIds": [
				"Sa4UO2A-icw4ijMTyuKTY"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670716,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 1,
			"text": "...",
			"rawText": "...",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "UJFwZ2W9SfaMuBFqDUrqS",
			"originalText": "...",
			"lineHeight": 1.25,
			"baseline": 14
		},
		{
			"type": "rectangle",
			"version": 129,
			"versionNonce": 1051970418,
			"isDeleted": false,
			"id": "kO9Ks88i2gHQAOdawIke0",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1050.8769959338701,
			"y": -6363.245651586005,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 151.02781258420532,
			"height": 37.18883338316573,
			"seed": 740737258,
			"groupIds": [
				"Sa4UO2A-icw4ijMTyuKTY"
			],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "87uFiNXv"
				}
			],
			"updated": 1710299670716,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 21,
			"versionNonce": 265706670,
			"isDeleted": false,
			"id": "87uFiNXv",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1013.3870764581737,
			"y": -6354.651234894422,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 76.0479736328125,
			"height": 20,
			"seed": 160261174,
			"groupIds": [
				"Sa4UO2A-icw4ijMTyuKTY"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670716,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 1,
			"text": "0010 1010",
			"rawText": "0010 1010",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "kO9Ks88i2gHQAOdawIke0",
			"originalText": "0010 1010",
			"lineHeight": 1.25,
			"baseline": 14
		},
		{
			"type": "rectangle",
			"version": 127,
			"versionNonce": 1154321714,
			"isDeleted": false,
			"id": "ZSICSDk-Jt2MLZnxwa0Y4",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1049.5023007973734,
			"y": -6323.782243013182,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 151.02781258420532,
			"height": 37.18883338316573,
			"seed": 1796524662,
			"groupIds": [
				"Sa4UO2A-icw4ijMTyuKTY"
			],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "U7KXNfZ4"
				}
			],
			"updated": 1710299670716,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 21,
			"versionNonce": 1652725486,
			"isDeleted": false,
			"id": "U7KXNfZ4",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1012.012381321677,
			"y": -6315.187826321599,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 76.0479736328125,
			"height": 20,
			"seed": 1638942570,
			"groupIds": [
				"Sa4UO2A-icw4ijMTyuKTY"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670716,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 1,
			"text": "0000 1011",
			"rawText": "0000 1011",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "ZSICSDk-Jt2MLZnxwa0Y4",
			"originalText": "0000 1011",
			"lineHeight": 1.25,
			"baseline": 14
		},
		{
			"type": "text",
			"version": 45,
			"versionNonce": 1841895154,
			"isDeleted": false,
			"id": "Kx2dHAWs",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1067.8332939545976,
			"y": -6311.221307820888,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 11.00799560546875,
			"height": 20,
			"seed": 650540778,
			"groupIds": [
				"Sa4UO2A-icw4ijMTyuKTY"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670716,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 1,
			"text": "0",
			"rawText": "0",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "0",
			"lineHeight": 1.25,
			"baseline": 14
		},
		{
			"type": "text",
			"version": 37,
			"versionNonce": 2984238,
			"isDeleted": false,
			"id": "0NRLXXpV",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1065.983226533494,
			"y": -6353.088854145645,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 4.33599853515625,
			"height": 20,
			"seed": 1477824554,
			"groupIds": [
				"Sa4UO2A-icw4ijMTyuKTY"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670716,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 1,
			"text": "1",
			"rawText": "1",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "1",
			"lineHeight": 1.25,
			"baseline": 14
		},
		{
			"type": "text",
			"version": 115,
			"versionNonce": 170748082,
			"isDeleted": false,
			"id": "3Y2j5Fdn",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1035.9548805543222,
			"y": -6468.900405447293,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 126.89593505859375,
			"height": 20,
			"seed": 1018524394,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670716,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 1,
			"text": "RAM = 1D array",
			"rawText": "RAM = 1D array",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "RAM = 1D array",
			"lineHeight": 1.25,
			"baseline": 14
		},
		{
			"type": "freedraw",
			"version": 63,
			"versionNonce": 138425198,
			"isDeleted": false,
			"id": "VLA2kOtYAsNVYtkc99E_p",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 318.8623659223992,
			"y": -6421.815040684256,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 103.59852196980341,
			"height": 0.9146060867597043,
			"seed": 221761322,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670716,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.1735814627091372,
					0
				],
				[
					3.56847614181504,
					0
				],
				[
					5.83177463907748,
					0
				],
				[
					8.587957460901976,
					0
				],
				[
					12.330121199001667,
					0
				],
				[
					15.579294478963732,
					0
				],
				[
					18.33553036757604,
					0
				],
				[
					19.38651809883703,
					0
				],
				[
					21.64981659609947,
					0
				],
				[
					23.13175971062583,
					0
				],
				[
					24.902067749750643,
					0
				],
				[
					25.88799559923808,
					0
				],
				[
					26.58868946460393,
					0
				],
				[
					27.289330263182023,
					0
				],
				[
					28.278389053146327,
					0
				],
				[
					29.906053566816468,
					0
				],
				[
					32.16929899729115,
					0
				],
				[
					34.9255348859034,
					0
				],
				[
					37.681770774515655,
					0
				],
				[
					40.438006663127965,
					0
				],
				[
					43.83290134223381,
					0
				],
				[
					44.82190706541036,
					0
				],
				[
					47.57808988723491,
					0
				],
				[
					48.85546053500991,
					0
				],
				[
					52.25035521411576,
					0
				],
				[
					53.73235139542987,
					0
				],
				[
					55.009668976417174,
					0
				],
				[
					55.99867469959372,
					0
				],
				[
					57.914704137862316,
					0
				],
				[
					61.16387741782444,
					0
				],
				[
					62.93418545694925,
					0
				],
				[
					66.18335873691137,
					0
				],
				[
					69.60616654637033,
					0.35034693268244155
				],
				[
					71.0881627276845,
					0.35034693268244155
				],
				[
					72.85847076680932,
					0.35034693268244155
				],
				[
					75.61465358863381,
					0.6324765097215277
				],
				[
					77.87795208589625,
					0.6324765097215277
				],
				[
					79.1552696668835,
					0.6324765097215277
				],
				[
					83.04315480412697,
					0.6324765097215277
				],
				[
					85.30640023460165,
					0.6324765097215277
				],
				[
					87.56964566507634,
					0.9146060867597043
				],
				[
					88.84701631285134,
					0.9146060867597043
				],
				[
					89.83602203602788,
					0.9146060867597043
				],
				[
					91.31796515055424,
					0.9146060867597043
				],
				[
					92.79996133186836,
					0.9146060867597043
				],
				[
					94.28195751318253,
					0.9146060867597043
				],
				[
					97.03814033500703,
					0.9146060867597043
				],
				[
					100.63766054765205,
					0.9146060867597043
				],
				[
					102.90095904491449,
					0.9146060867597043
				],
				[
					103.42488744030652,
					0.9146060867597043
				],
				[
					103.59852196980341,
					0.9146060867597043
				],
				[
					103.59852196980341,
					0.9146060867597043
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 148,
			"versionNonce": 1101103730,
			"isDeleted": false,
			"id": "z_5bJ7AmclbBU5nNp-M6y",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 164.25360650125901,
			"y": -6265.222061002594,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 30.55092117147609,
			"height": 24.24791345723588,
			"seed": 1302364406,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670716,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.17671240318600212,
					0
				],
				[
					-0.5301372095580632,
					0.35034693268244155
				],
				[
					-1.097527304112134,
					1.4819696479198683
				],
				[
					-1.9811423868299585,
					2.3562715093885345
				],
				[
					-4.250596631470614,
					3.2026867738986766
				],
				[
					-5.534123026623888,
					3.624328935914491
				],
				[
					-6.529337563966408,
					4.008771279723078
				],
				[
					-7.6640646862867925,
					4.2909008567612545
				],
				[
					-8.194254962632556,
					4.464535386257921
				],
				[
					-8.547679769004617,
					4.464535386257921
				],
				[
					-9.366181903161134,
					4.464535386257921
				],
				[
					-9.896372179506955,
					4.814855785547479
				],
				[
					-10.249796985879016,
					4.814855785547479
				],
				[
					-11.245011523221535,
					5.025690133252283
				],
				[
					-11.775148732779599,
					5.025690133252283
				],
				[
					-12.48205141231142,
					5.025690133252283
				],
				[
					-14.323681214163628,
					5.307819710291369
				],
				[
					-14.965417878346386,
					5.307819710291369
				],
				[
					-15.318895751506147,
					5.307819710291369
				],
				[
					-15.672320557878209,
					5.307819710291369
				],
				[
					-16.555935640596033,
					5.307819710291369
				],
				[
					-17.086072850154096,
					5.307819710291369
				],
				[
					-18.397512375660483,
					5.307819710291369
				],
				[
					-18.750990248820244,
					5.307819710291369
				],
				[
					-19.457839861564366,
					5.307819710291369
				],
				[
					-20.099629592534825,
					5.307819710291369
				],
				[
					-22.052858849011727,
					4.526517394342591
				],
				[
					-22.58299605856979,
					4.526517394342591
				],
				[
					-23.11318633491561,
					4.349804991156816
				],
				[
					-23.466611141287615,
					4.173092587971041
				],
				[
					-24.350226224005496,
					3.6429288450190143
				],
				[
					-25.168728358162014,
					3.4662164418332395
				],
				[
					-25.522153164534075,
					3.1127651020669873
				],
				[
					-25.698865567720077,
					2.9360526988812126
				],
				[
					-25.875577970906136,
					2.759313762300735
				],
				[
					-26.052343440879895,
					2.5826013591149604
				],
				[
					-26.4057682472519,
					2.2291765527425014
				],
				[
					-26.75919305362396,
					1.8757252129771587
				],
				[
					-26.935905456809962,
					0.9921101302588795
				],
				[
					-27.112670926783778,
					0.46194638730685256
				],
				[
					-27.28938332996978,
					-0.35652921345536015
				],
				[
					-27.28938332996978,
					-0.9983189444255913
				],
				[
					-27.64280813634184,
					-1.5284826873776183
				],
				[
					-27.64280813634184,
					-2.588783639887879
				],
				[
					-27.996232942713846,
					-3.118947382839906
				],
				[
					-27.996232942713846,
					-3.760737113810137
				],
				[
					-27.996232942713846,
					-4.290900856762164
				],
				[
					-27.996232942713846,
					-4.821064599714191
				],
				[
					-27.996232942713846,
					-5.992991540242656
				],
				[
					-27.996232942713846,
					-6.523155283194683
				],
				[
					-27.82265148000471,
					-7.2300314293324845
				],
				[
					-27.649016950507814,
					-7.7601951722845115
				],
				[
					-27.43818260280267,
					-8.932122112812976
				],
				[
					-27.264548073305775,
					-9.285573452579229
				],
				[
					-27.090966610596638,
					-9.815737195531256
				],
				[
					-27.090966610596638,
					-10.169188535296598
				],
				[
					-26.74369755160285,
					-10.87606468143531
				],
				[
					-26.005803868028806,
					-12.36424314352098
				],
				[
					-26.005803868028806,
					-12.540955546706755
				],
				[
					-25.655456935345853,
					-12.894380353079214
				],
				[
					-25.305163069450714,
					-13.42454409603124
				],
				[
					-24.33159978150752,
					-14.726696933682433
				],
				[
					-23.984383789301432,
					-15.25686067663446
				],
				[
					-23.6371677970954,
					-15.433599613214028
				],
				[
					-23.11318633491561,
					-15.963736822772262
				],
				[
					-22.300893014925066,
					-16.177675577560876
				],
				[
					-21.48859969493452,
					-16.568326735534356
				],
				[
					-20.499593971757974,
					-16.782238956929177
				],
				[
					-20.149247039075078,
					-16.958951360114952
				],
				[
					-19.16024131589853,
					-17.34960251808934
				],
				[
					-18.46262532422179,
					-17.703053857854684
				],
				[
					-17.938696928829756,
					-17.879766261041368
				],
				[
					-17.41471546664991,
					-18.23321760080671
				],
				[
					-17.067499474443878,
					-18.409930003992486
				],
				[
					-16.71715254176098,
					-18.409930003992486
				],
				[
					-16.36680560907803,
					-18.409930003992486
				],
				[
					-15.842824146898238,
					-18.409930003992486
				],
				[
					-15.318895751506147,
					-18.58664240717917
				],
				[
					-14.506602431515603,
					-18.58664240717917
				],
				[
					-13.632274036652916,
					-18.763381343758738
				],
				[
					-13.108345641260826,
					-18.940093746944513
				],
				[
					-12.761076582267037,
					-18.940093746944513
				],
				[
					-12.413860590061006,
					-18.940093746944513
				],
				[
					-11.889879127881159,
					-18.940093746944513
				],
				[
					-11.716244598384264,
					-18.940093746944513
				],
				[
					-11.369028606178233,
					-18.940093746944513
				],
				[
					-10.845047143998386,
					-18.940093746944513
				],
				[
					-10.49470021131549,
					-18.940093746944513
				],
				[
					-10.321118748606352,
					-18.940093746944513
				],
				[
					-10.147484219109458,
					-18.940093746944513
				],
				[
					-9.800215160115613,
					-18.940093746944513
				],
				[
					-9.16155636962202,
					-18.940093746944513
				],
				[
					-7.505978725598709,
					-18.76648575084164
				],
				[
					-6.867319935105115,
					-18.555651403136835
				],
				[
					-6.516973002422162,
					-18.555651403136835
				],
				[
					-6.169703943428374,
					-18.38201687364017
				],
				[
					-5.648853421725448,
					-18.03480088143351
				],
				[
					-5.298506489042552,
					-18.03480088143351
				],
				[
					-5.124871959545601,
					-17.68445394875107
				],
				[
					-4.4242311609675085,
					-17.33721142315062
				],
				[
					-4.250596631470614,
					-17.163576893653953
				],
				[
					-3.903327572476826,
					-16.98996889755108
				],
				[
					-3.3793991770847924,
					-16.64272637195063
				],
				[
					-2.7810180784885006,
					-16.0040410480633
				],
				[
					-1.968724758497956,
					-15.619598704255623
				],
				[
					-1.6215087662919245,
					-15.272356178655173
				],
				[
					-0.9238927746152399,
					-14.925140186449426
				],
				[
					-0.5766767824091517,
					-14.751505656952759
				],
				[
					-0.2294077234153633,
					-14.751505656952759
				],
				[
					0.11780826879066808,
					-14.401158724269408
				],
				[
					0.8185021341565175,
					-14.227550728166534
				],
				[
					0.9921366636534117,
					-14.053916198669867
				],
				[
					1.339352655859443,
					-13.706673673069417
				],
				[
					1.5129871853563372,
					-13.533065676966544
				],
				[
					1.5129871853563372,
					-13.35945768086367
				],
				[
					1.5129871853563372,
					-13.185823151367003
				],
				[
					1.5129871853563372,
					-12.835476218683652
				],
				[
					1.5129871853563372,
					-12.661868222580779
				],
				[
					1.5129871853563372,
					-12.488233693084112
				],
				[
					1.6866217148532314,
					-11.964278764297887
				],
				[
					2.0338377070593197,
					-11.617036238698347
				],
				[
					2.0338377070593197,
					-11.26671583940879
				],
				[
					2.0338377070593197,
					-10.919473313809249
				],
				[
					2.381053699265351,
					-10.572230788208799
				],
				[
					2.381053699265351,
					-10.04824932602969
				],
				[
					2.554688228762245,
					-9.350686401140592
				],
				[
					2.554688228762245,
					-9.003443875540142
				],
				[
					2.554688228762245,
					-8.829809346043476
				],
				[
					2.554688228762245,
					-8.129142014071476
				],
				[
					2.554688228762245,
					-7.605187085286161
				],
				[
					2.554688228762245,
					-7.25484015260281
				],
				[
					2.554688228762245,
					-6.90759762700327
				],
				[
					2.554688228762245,
					-6.383642698217045
				],
				[
					2.554688228762245,
					-6.210008168720378
				],
				[
					2.554688228762245,
					-5.686053239934154
				],
				[
					2.1268637859737396,
					-4.697047516757266
				],
				[
					1.9501513827877375,
					-4.346700584074824
				],
				[
					1.9501513827877375,
					-4.346700584074824
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "text",
			"version": 439,
			"versionNonce": 1157862830,
			"isDeleted": false,
			"id": "fFc86EPy",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 608.283956398401,
			"y": -6472.519029703522,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 332.3358154296875,
			"height": 300,
			"seed": 1992337642,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670716,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 1,
			"text": "a[8]에 어떻게 접근할 것인가\n\n1. doubleword array -> 한 칸당 8bytes 차지.\n2. [8] -> 8th element\n3. base register -> x22\n4. 결론은 x22에서 8 * 8 = 64bytes 이동\n5. 64(x22)\n\n앞의 operator마다 다름\nlb - load byte\nlh - load halfword\nlw - load word\nld - load doubleword\n뛰어넘는 간격은 모두 byte 단위지만, \n읽는 범위가 다름",
			"rawText": "a[8]에 어떻게 접근할 것인가\n\n1. doubleword array -> 한 칸당 8bytes 차지.\n2. [8] -> 8th element\n3. base register -> x22\n4. 결론은 x22에서 8 * 8 = 64bytes 이동\n5. 64(x22)\n\n앞의 operator마다 다름\nlb - load byte\nlh - load halfword\nlw - load word\nld - load doubleword\n뛰어넘는 간격은 모두 byte 단위지만, \n읽는 범위가 다름",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "a[8]에 어떻게 접근할 것인가\n\n1. doubleword array -> 한 칸당 8bytes 차지.\n2. [8] -> 8th element\n3. base register -> x22\n4. 결론은 x22에서 8 * 8 = 64bytes 이동\n5. 64(x22)\n\n앞의 operator마다 다름\nlb - load byte\nlh - load halfword\nlw - load word\nld - load doubleword\n뛰어넘는 간격은 모두 byte 단위지만, \n읽는 범위가 다름",
			"lineHeight": 1.25,
			"baseline": 294
		},
		{
			"type": "text",
			"version": 430,
			"versionNonce": 787244082,
			"isDeleted": false,
			"id": "5jGvaqGl",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -922.2795327932897,
			"y": -5949.575792692519,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 422.559814453125,
			"height": 160,
			"seed": 1353561066,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670716,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 1,
			"text": "store의 경우도 load와 비슷함\n\n아래의 예시는 x9를 중복 사용해 레지스터를 아낌\n\na[12]는 96(x22)\n\nRISC-V 같은 경우는 alignment restriction,\n즉 word나 double word의 길이가 4나 8의 배수가 될 필요 x",
			"rawText": "store의 경우도 load와 비슷함\n\n아래의 예시는 x9를 중복 사용해 레지스터를 아낌\n\na[12]는 96(x22)\n\nRISC-V 같은 경우는 alignment restriction,\n즉 word나 double word의 길이가 4나 8의 배수가 될 필요 x",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "store의 경우도 load와 비슷함\n\n아래의 예시는 x9를 중복 사용해 레지스터를 아낌\n\na[12]는 96(x22)\n\nRISC-V 같은 경우는 alignment restriction,\n즉 word나 double word의 길이가 4나 8의 배수가 될 필요 x",
			"lineHeight": 1.25,
			"baseline": 154
		},
		{
			"type": "text",
			"version": 282,
			"versionNonce": 1335930862,
			"isDeleted": false,
			"id": "D1tOryiO",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 599.3832498239328,
			"y": -5989.519866962028,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 303.6959228515625,
			"height": 140,
			"seed": 1149705334,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670716,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 1,
			"text": "빅 엔디안\n- 가장 큰 바이트부터 낮은 레지스터에 저장\n- IBM만 사용\n\n리틀 엔디안\n- 가장 작은 바이트부터 낮은 레지스터에 저장\n- intel, ARM, RISC-V 등 대부분이 사용 ",
			"rawText": "빅 엔디안\n- 가장 큰 바이트부터 낮은 레지스터에 저장\n- IBM만 사용\n\n리틀 엔디안\n- 가장 작은 바이트부터 낮은 레지스터에 저장\n- intel, ARM, RISC-V 등 대부분이 사용 ",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "빅 엔디안\n- 가장 큰 바이트부터 낮은 레지스터에 저장\n- IBM만 사용\n\n리틀 엔디안\n- 가장 작은 바이트부터 낮은 레지스터에 저장\n- intel, ARM, RISC-V 등 대부분이 사용 ",
			"lineHeight": 1.25,
			"baseline": 134
		},
		{
			"type": "freedraw",
			"version": 44,
			"versionNonce": 2079657458,
			"isDeleted": false,
			"id": "3SZQIimTlmLzlaDUHLVJ0",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -394.5678734360104,
			"y": -5544.630830105707,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 79.28554863079393,
			"height": 2.7996179875926828,
			"seed": 1933772214,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670716,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.3472690589938452,
					0
				],
				[
					0.5209035884907394,
					0
				],
				[
					1.5067783711903644,
					0
				],
				[
					2.495784094366911,
					0
				],
				[
					3.484842884331215,
					0
				],
				[
					5.748088314805898,
					0
				],
				[
					10.128910843399183,
					0
				],
				[
					13.871021514711117,
					0
				],
				[
					17.12019479467324,
					0
				],
				[
					19.87643068328549,
					0.28212957703908614
				],
				[
					24.750190603228646,
					0.5642591540772628
				],
				[
					28.49230127454058,
					0.5642591540772628
				],
				[
					31.248537163152832,
					0.8463887311163489
				],
				[
					34.4977104431149,
					0.8463887311163489
				],
				[
					37.25394633172721,
					0.8463887311163489
				],
				[
					41.63476886032049,
					0.8463887311163489
				],
				[
					43.898014290795174,
					0.8463887311163489
				],
				[
					46.30698112041364,
					1.1285183081545256
				],
				[
					47.93156776039467,
					1.450978643878443
				],
				[
					51.326462439500574,
					1.450978643878443
				],
				[
					54.082698328112826,
					1.7734124462085674
				],
				[
					56.83893421672508,
					1.7734124462085674
				],
				[
					60.0881074966872,
					2.477184185263468
				],
				[
					62.35135292716183,
					2.477184185263468
				],
				[
					66.2391849976176,
					2.7996179875926828
				],
				[
					67.22824378758185,
					2.7996179875926828
				],
				[
					69.20317736024583,
					2.7996179875926828
				],
				[
					69.90381815882392,
					2.7996179875926828
				],
				[
					72.02447313063169,
					2.7996179875926828
				],
				[
					73.5064693119458,
					2.7996179875926828
				],
				[
					76.75564259190793,
					2.7996179875926828
				],
				[
					78.23758570643429,
					2.7996179875926828
				],
				[
					78.93827957180014,
					2.7996179875926828
				],
				[
					79.28554863079393,
					2.7996179875926828
				],
				[
					79.28554863079393,
					2.7996179875926828
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 23,
			"versionNonce": 874545710,
			"isDeleted": false,
			"id": "KiBTVOE5WB-SVeQrzhsKu",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -316.16907082841124,
			"y": -5544.240178947733,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 9.23600907282622,
			"height": 7.577273954932025,
			"seed": 183458806,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670716,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.35034693268295314,
					0.17360799610287359
				],
				[
					1.0510407980488026,
					0.8743018614686662
				],
				[
					2.3562715093891597,
					1.330039434610626
				],
				[
					3.3793991770847924,
					2.179559106203669
				],
				[
					3.903380639264583,
					2.5298795054923175
				],
				[
					5.035029887895803,
					2.812009082530494
				],
				[
					4.216527753739285,
					3.373190362918649
				],
				[
					3.574738022768827,
					3.583998177230569
				],
				[
					-0.4433199448096161,
					6.064286769576029
				],
				[
					-3.2057646475878414,
					6.978892856335733
				],
				[
					-3.3824770507739004,
					6.978892856335733
				],
				[
					-4.024266781744359,
					7.403665958829151
				],
				[
					-4.200979184930418,
					7.577273954932025
				],
				[
					-4.200979184930418,
					7.577273954932025
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 45,
			"versionNonce": 2109898674,
			"isDeleted": false,
			"id": "8Nl1AZi3CzENDhW1GuIAD",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -305.47590083093485,
			"y": -5514.0612824917325,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 86.22100632136176,
			"height": 3.0507565605885247,
			"seed": 841871978,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670716,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.488204995480146,
					0
				],
				[
					-3.7576592401208018,
					0
				],
				[
					-7.013041334248896,
					0
				],
				[
					-10.268423428376991,
					0
				],
				[
					-11.90537462990227,
					0.1736345294966668
				],
				[
					-14.174828874542982,
					0.4960683318267911
				],
				[
					-16.937273577321207,
					0.8463887311154394
				],
				[
					-18.71379043061205,
					1.1285448415483188
				],
				[
					-20.983244675252706,
					1.1285448415483188
				],
				[
					-26.85221913253838,
					1.4788652408369671
				],
				[
					-30.107601226666475,
					1.8012990431670914
				],
				[
					-33.36298332079457,
					2.123759378891009
				],
				[
					-36.12542802357285,
					2.123759378891009
				],
				[
					-39.38075705091319,
					2.4461931812202238
				],
				[
					-42.636139145041284,
					2.768626983550348
				],
				[
					-46.533310970139894,
					3.0507565605885247
				],
				[
					-48.80276521478055,
					3.0507565605885247
				],
				[
					-51.072219459421206,
					3.0507565605885247
				],
				[
					-53.83466416219949,
					3.0507565605885247
				],
				[
					-58.22477337864791,
					3.0507565605885247
				],
				[
					-61.97309286412582,
					3.0507565605885247
				],
				[
					-65.22847495825391,
					3.0507565605885247
				],
				[
					-67.49792920289462,
					3.0507565605885247
				],
				[
					-71.39510102799318,
					3.0507565605885247
				],
				[
					-74.1575457307714,
					3.0507565605885247
				],
				[
					-76.42699997541212,
					3.0507565605885247
				],
				[
					-77.9151519041045,
					3.0507565605885247
				],
				[
					-78.91036644144702,
					3.0507565605885247
				],
				[
					-81.8216104170582,
					3.0507565605885247
				],
				[
					-82.81682495440077,
					3.0507565605885247
				],
				[
					-83.81203949174329,
					3.0507565605885247
				],
				[
					-84.80725402908581,
					3.0507565605885247
				],
				[
					-85.69086911180364,
					3.0507565605885247
				],
				[
					-86.04429391817575,
					3.0507565605885247
				],
				[
					-86.22100632136176,
					3.0507565605885247
				],
				[
					-86.22100632136176,
					3.0507565605885247
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 28,
			"versionNonce": 359402606,
			"isDeleted": false,
			"id": "a08uVVmgqjsnI85NCX7QY",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -385.06525682156064,
			"y": -5517.6297851669415,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 15.76226876310352,
			"height": 20.36936807463553,
			"seed": 917205738,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670716,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.35342480637200424,
					0.17360799610287359
				],
				[
					-0.8836150827178244,
					0.6975629248890982
				],
				[
					-1.9532292564767886,
					1.7609948178760533
				],
				[
					-2.948443793819365,
					2.53608831965812
				],
				[
					-4.2785097618236705,
					4.185483682909762
				],
				[
					-6.222399263657735,
					6.436338018445895
				],
				[
					-6.826989176419943,
					7.248631338436098
				],
				[
					-7.747804077346018,
					8.553888583171101
				],
				[
					-8.101228883718079,
					8.904235515853543
				],
				[
					-8.45465369009014,
					9.428190444639768
				],
				[
					-8.6314191600639,
					9.601798440742641
				],
				[
					-8.420584812358811,
					10.240483764629971
				],
				[
					-5.71083542980989,
					13.303631420157217
				],
				[
					-2.294236434516847,
					15.334364720133635
				],
				[
					1.7331082209166198,
					17.92938370758111
				],
				[
					4.9822815008787416,
					19.197414600713273
				],
				[
					6.95721507354267,
					20.01902114195218
				],
				[
					7.130849603039621,
					20.36936807463553
				],
				[
					7.130849603039621,
					20.36936807463553
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 41,
			"versionNonce": 1350285682,
			"isDeleted": false,
			"id": "GCZ2zAT2EDMPZnrCC4JIf",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -188.6884247692882,
			"y": -5460.018914922305,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 171.5026243660871,
			"height": 3.903354105870676,
			"seed": 409382838,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670716,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5301902763457633,
					0.3472425256004499
				],
				[
					-0.8836150827178244,
					0.5208770550971167
				],
				[
					-1.4138053590636446,
					0.5208770550971167
				],
				[
					-2.055542023246403,
					0.9456236241967417
				],
				[
					-2.7624447027782253,
					0.9456236241967417
				],
				[
					-5.031898947418881,
					0.9456236241967417
				],
				[
					-8.436080314379922,
					0.9456236241967417
				],
				[
					-16.128111197807527,
					0.9456236241967417
				],
				[
					-25.292745441118655,
					0.9456236241967417
				],
				[
					-34.45743275121754,
					0.9456236241967417
				],
				[
					-44.115057452666235,
					0.9456236241967417
				],
				[
					-60.326801907957645,
					0.9456236241967417
				],
				[
					-72.44921969973103,
					-0.35652921345445066
				],
				[
					-85.55756534099186,
					-1.667995272355256
				],
				[
					-97.18699267462767,
					-2.532983912574309
				],
				[
					-111.42698756451966,
					-2.9577304816739343
				],
				[
					-119.11896538115957,
					-2.9577304816739343
				],
				[
					-125.33207795696217,
					-2.9577304816739343
				],
				[
					-130.0663252919275,
					-2.9577304816739343
				],
				[
					-134.30763523554305,
					-2.9577304816739343
				],
				[
					-140.66954708417853,
					-2.9577304816739343
				],
				[
					-144.91085702779407,
					-2.9577304816739343
				],
				[
					-149.6451043627594,
					-2.9577304816739343
				],
				[
					-154.87228908907463,
					-2.9577304816739343
				],
				[
					-161.72719139584774,
					-2.9577304816739343
				],
				[
					-164.48963609862597,
					-2.6352966793447195
				],
				[
					-166.47077848545592,
					-2.6352966793447195
				],
				[
					-167.4659930227985,
					-2.4616886832409364
				],
				[
					-168.95414495149083,
					-2.4616886832409364
				],
				[
					-170.79577475334304,
					-2.2880541537442696
				],
				[
					-171.14919955971504,
					-2.2880541537442696
				],
				[
					-171.5026243660871,
					-2.2880541537442696
				],
				[
					-171.5026243660871,
					-2.2880541537442696
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 31,
			"versionNonce": 1363955374,
			"isDeleted": false,
			"id": "iz-KqrrSU7KggQmtR7-QM",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -351.3984661409342,
			"y": -5467.8318054148185,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 17.61313218602305,
			"height": 18.36965231209524,
			"seed": 189311862,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670716,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.3534248063720611,
					-0.17673893657956796
				],
				[
					-0.7068496127440653,
					-0.17673893657956796
				],
				[
					-1.2370398890898855,
					0.17360799610287359
				],
				[
					-1.5904646954619466,
					0.3472425256004499
				],
				[
					-2.762391635990525,
					0.9052928655110009
				],
				[
					-3.5808937701470427,
					1.2897352093195877
				],
				[
					-5.143498402043633,
					2.2105501102450944
				],
				[
					-7.412952646684289,
					2.5329839125752187
				],
				[
					-7.943089856242352,
					2.7066184420718855
				],
				[
					-8.826704938960177,
					3.4041813669609837
				],
				[
					-9.003417342146236,
					3.7545282996443348
				],
				[
					-9.180129745332238,
					3.9281362957472084
				],
				[
					-9.180129745332238,
					4.449013350844325
				],
				[
					-8.615870591255089,
					6.219321389969082
				],
				[
					-6.355703034469514,
					8.832913753126377
				],
				[
					-3.4320944973140968,
					10.779934195436908
				],
				[
					-0.34413811851692344,
					13.492761451675506
				],
				[
					3.3763213033956276,
					15.721911471025123
				],
				[
					4.7187518329442355,
					16.924855948989716
				],
				[
					6.489059872069106,
					17.699949450771783
				],
				[
					7.794343650197163,
					17.98207902780996
				],
				[
					8.433002440690814,
					18.192913375515673
				],
				[
					8.433002440690814,
					18.192913375515673
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 51,
			"versionNonce": 1936177970,
			"isDeleted": false,
			"id": "Qt7pHywm1yrMGg3ABTb4k",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -378.57619694949153,
			"y": -5329.279808895364,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 189.30796445731733,
			"height": 0.3255647428068187,
			"seed": 78881706,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670717,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.7703080391248704,
					0
				],
				[
					3.540616078249684,
					0
				],
				[
					6.2968519668619365,
					0
				],
				[
					10.03896263817387,
					0
				],
				[
					14.912722558117025,
					0
				],
				[
					20.62668892840378,
					0
				],
				[
					27.819520539527844,
					0
				],
				[
					35.01235215065185,
					0
				],
				[
					46.787553950219205,
					0
				],
				[
					53.48739510320564,
					0
				],
				[
					58.708424082142585,
					0
				],
				[
					61.318938571611056,
					0
				],
				[
					67.67156373239146,
					0
				],
				[
					73.53125150182206,
					0
				],
				[
					77.27336217313399,
					0
				],
				[
					81.5084633025835,
					0
				],
				[
					86.72949228152044,
					0
				],
				[
					94.56098268313809,
					0
				],
				[
					99.78201166207504,
					0
				],
				[
					105.00298757422422,
					0
				],
				[
					109.23808870367372,
					0
				],
				[
					112.98019937498566,
					0
				],
				[
					118.83988714441625,
					0
				],
				[
					122.08906042437837,
					0
				],
				[
					126.32416155382788,
					0
				],
				[
					131.0522000746272,
					0
				],
				[
					137.40487830219536,
					0
				],
				[
					141.1469889735073,
					0
				],
				[
					144.3961622534694,
					0
				],
				[
					147.64533553343148,
					0
				],
				[
					150.8945088133936,
					0
				],
				[
					155.76826873333675,
					0
				],
				[
					159.01744201329882,
					0
				],
				[
					162.26661529326094,
					0
				],
				[
					165.51584164001076,
					0
				],
				[
					170.88253895130373,
					0
				],
				[
					174.62470268940342,
					0
				],
				[
					178.85975075206522,
					0
				],
				[
					182.60191449016492,
					0
				],
				[
					185.85108777012698,
					0
				],
				[
					187.6833778173363,
					0
				],
				[
					189.30796445731733,
					-0.3255647428068187
				],
				[
					189.30796445731733,
					-0.3255647428068187
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 24,
			"versionNonce": 610945262,
			"isDeleted": false,
			"id": "Ldjb3br9K4zeQFwizJCIg",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -191.22146174865105,
			"y": -5334.255881582078,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 3.720406355124794,
			"height": 9.744388899409387,
			"seed": 1202481002,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670717,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.17671240318600212,
					0.35034693268335104
				],
				[
					0.45579063992937563,
					1.8322900472094261
				],
				[
					0.8061375726122719,
					2.182636979892777
				],
				[
					1.6184308926028166,
					2.781018078489069
				],
				[
					1.965646884808848,
					3.1313650111715106
				],
				[
					2.139281414305742,
					3.304946473880591
				],
				[
					2.3128628770148794,
					3.4785810033781672
				],
				[
					2.3128628770148794,
					4.002562465557276
				],
				[
					2.3128628770148794,
					4.349778457763932
				],
				[
					2.1361504738288772,
					5.050472323129725
				],
				[
					1.7827256674568162,
					5.751166188495517
				],
				[
					0.27594729626645176,
					7.574169547849124
				],
				[
					-0.7006407985780925,
					9.046825974521198
				],
				[
					-1.0541186717378537,
					9.394095033514532
				],
				[
					-1.4075434781099148,
					9.744388899409387
				],
				[
					-1.4075434781099148,
					9.744388899409387
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "text",
			"version": 251,
			"versionNonce": 1693287666,
			"isDeleted": false,
			"id": "pVT7JCbw",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 646.5169584306034,
			"y": -5555.008624183627,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 311.6959228515625,
			"height": 120,
			"seed": 6116266,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670717,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 1,
			"text": "CPU에서 자주 사용하는 것은 레지스터에 저장,\n자주 사용하지 않는 것은 메모리로 이동\n\nSpilling - 메모리로 데이터가 이동하는 것\n\n메모리로 이동하면 매우 느려짐",
			"rawText": "CPU에서 자주 사용하는 것은 레지스터에 저장,\n자주 사용하지 않는 것은 메모리로 이동\n\nSpilling - 메모리로 데이터가 이동하는 것\n\n메모리로 이동하면 매우 느려짐",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "CPU에서 자주 사용하는 것은 레지스터에 저장,\n자주 사용하지 않는 것은 메모리로 이동\n\nSpilling - 메모리로 데이터가 이동하는 것\n\n메모리로 이동하면 매우 느려짐",
			"lineHeight": 1.25,
			"baseline": 114
		},
		{
			"type": "freedraw",
			"version": 92,
			"versionNonce": 1313798958,
			"isDeleted": false,
			"id": "8E70EYq_MlvI4Mq_YgkRo",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 97.29794026892262,
			"y": -5332.378909299592,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 235.98391895291184,
			"height": 2.960834888757745,
			"seed": 509087338,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670717,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.624586639981061,
					0
				],
				[
					3.8878320704557154,
					0
				],
				[
					6.151130567718155,
					0
				],
				[
					9.400303847680249,
					0
				],
				[
					14.767001158973216,
					0
				],
				[
					18.016174438935337,
					0
				],
				[
					20.77241032754759,
					0
				],
				[
					24.660242398003305,
					0
				],
				[
					26.923540895265745,
					0
				],
				[
					29.186786325740428,
					0
				],
				[
					31.94302221435268,
					0
				],
				[
					35.192195494314745,
					0
				],
				[
					39.08002756477046,
					-0.32553820941302547
				],
				[
					41.83626345338271,
					-0.32553820941302547
				],
				[
					45.085436733344835,
					-0.32553820941302547
				],
				[
					47.84167262195709,
					-0.32553820941302547
				],
				[
					51.23656730106299,
					-0.32553820941302547
				],
				[
					53.992750122887486,
					-0.32553820941302547
				],
				[
					54.98180891285179,
					-0.5022506125988002
				],
				[
					57.737991734676285,
					-0.5022506125988002
				],
				[
					58.72699745785283,
					-0.5022506125988002
				],
				[
					61.13601735425905,
					-0.5022506125988002
				],
				[
					62.4133349352463,
					-0.5022506125988002
				],
				[
					63.11402880061215,
					-0.5022506125988002
				],
				[
					65.8702646892244,
					-0.5022506125988002
				],
				[
					69.75809675968011,
					-0.7874845967207875
				],
				[
					73.50020743099205,
					-0.7874845967207875
				],
				[
					77.73530856044161,
					-0.7874845967207875
				],
				[
					80.49154444905386,
					-0.7874845967207875
				],
				[
					83.24778033766611,
					-0.7874845967207875
				],
				[
					88.61447764895908,
					-1.4664741458991557
				],
				[
					92.35664138705877,
					-1.819925485665408
				],
				[
					96.0987520583707,
					-2.1733502920369574
				],
				[
					99.34792533833277,
					-2.1733502920369574
				],
				[
					102.5970986182949,
					-2.1733502920369574
				],
				[
					106.97792114688818,
					-2.78412248557197
				],
				[
					109.73415703550043,
					-2.78412248557197
				],
				[
					113.96925816494999,
					-2.78412248557197
				],
				[
					118.20430622761174,
					-2.78412248557197
				],
				[
					123.07806614755489,
					-2.78412248557197
				],
				[
					125.83430203616714,
					-2.78412248557197
				],
				[
					128.30217300018094,
					-2.78412248557197
				],
				[
					131.55139934693082,
					-2.78412248557197
				],
				[
					135.43923141738654,
					-2.78412248557197
				],
				[
					137.70247684786122,
					-2.78412248557197
				],
				[
					139.32706348784225,
					-2.78412248557197
				],
				[
					145.1867512572728,
					-2.78412248557197
				],
				[
					149.42185238672235,
					-2.78412248557197
				],
				[
					154.78854969801532,
					-2.78412248557197
				],
				[
					157.54478558662757,
					-2.78412248557197
				],
				[
					160.79395886658972,
					-2.78412248557197
				],
				[
					162.56426690571448,
					-2.78412248557197
				],
				[
					168.42395467514507,
					-2.78412248557197
				],
				[
					172.65905580459457,
					-2.78412248557197
				],
				[
					176.4011664759065,
					-2.78412248557197
				],
				[
					178.66446497316895,
					-2.78412248557197
				],
				[
					180.63939854583293,
					-2.78412248557197
				],
				[
					185.5131584657761,
					-2.78412248557197
				],
				[
					188.76233174573815,
					-2.78412248557197
				],
				[
					192.5044424170501,
					-2.78412248557197
				],
				[
					196.24660615514972,
					-2.78412248557197
				],
				[
					200.13443822560544,
					-2.78412248557197
				],
				[
					202.39768365608018,
					-2.78412248557197
				],
				[
					205.15391954469237,
					-2.78412248557197
				],
				[
					208.40309282465455,
					-2.78412248557197
				],
				[
					211.15932871326675,
					-2.78412248557197
				],
				[
					215.04716078372246,
					-2.78412248557197
				],
				[
					216.52915696503658,
					-2.78412248557197
				],
				[
					217.80647454602388,
					-2.78412248557197
				],
				[
					220.5627104346362,
					-2.78412248557197
				],
				[
					222.33301847376094,
					-2.78412248557197
				],
				[
					226.22085054421666,
					-2.78412248557197
				],
				[
					227.20990933418102,
					-2.78412248557197
				],
				[
					227.9105501327591,
					-2.78412248557197
				],
				[
					228.4345315949389,
					-2.960834888757745
				],
				[
					229.9133968357762,
					-2.960834888757745
				],
				[
					232.38126779978995,
					-2.960834888757745
				],
				[
					233.65863844756495,
					-2.960834888757745
				],
				[
					234.6476441707415,
					-2.960834888757745
				],
				[
					234.8212787002384,
					-2.960834888757745
				],
				[
					235.45993749073205,
					-2.960834888757745
				],
				[
					235.63357202022894,
					-2.960834888757745
				],
				[
					235.98391895291184,
					-2.960834888757745
				],
				[
					235.98391895291184,
					-2.960834888757745
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 110,
			"versionNonce": 1049892530,
			"isDeleted": false,
			"id": "MsJVgRRoIuquuCC29o3Ak",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 102.54067356404667,
			"y": -5300.888546784692,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 414.5553578471663,
			"height": 0,
			"seed": 1103647466,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670717,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.35029386589516776,
					0
				],
				[
					1.3393526558594715,
					0
				],
				[
					2.3283583790360183,
					0
				],
				[
					3.6056759600232624,
					0
				],
				[
					4.129657422203081,
					0
				],
				[
					5.180698220251827,
					0
				],
				[
					5.527914212457887,
					0
				],
				[
					6.340207532448403,
					0
				],
				[
					7.0409013978142525,
					0
				],
				[
					9.449868227432717,
					0
				],
				[
					11.22017626655753,
					0
				],
				[
					13.976412155169783,
					0
				],
				[
					17.225585435131904,
					0
				],
				[
					20.474758715094026,
					0
				],
				[
					25.841456026386993,
					0
				],
				[
					28.597691914999245,
					0
				],
				[
					33.81872089393619,
					0
				],
				[
					40.02562465557281,
					0
				],
				[
					49.33598029802772,
					0
				],
				[
					54.55700927696466,
					0
				],
				[
					59.778038255901606,
					0
				],
				[
					65.49200462618836,
					0
				],
				[
					70.22004314698773,
					0
				],
				[
					77.06560569911795,
					0
				],
				[
					81.30070682856751,
					0
				],
				[
					84.54988010852958,
					0
				],
				[
					87.7990533884917,
					0
				],
				[
					89.42364002847273,
					0
				],
				[
					96.41497704653449,
					0
				],
				[
					100.65007817598405,
					0
				],
				[
					104.88517930543355,
					0
				],
				[
					109.61321782623293,
					0
				],
				[
					116.95177083650071,
					0
				],
				[
					122.66573720678753,
					0
				],
				[
					128.37970357707428,
					0
				],
				[
					133.60067948922347,
					0
				],
				[
					141.43222295762888,
					0
				],
				[
					143.54974698895978,
					0
				],
				[
					150.88829999922757,
					0
				],
				[
					157.09520376086422,
					0
				],
				[
					163.3021605892886,
					0
				],
				[
					173.10545362309333,
					0
				],
				[
					178.32648260203027,
					0
				],
				[
					182.0685932733422,
					0
				],
				[
					185.31781962009208,
					0
				],
				[
					190.684516931385,
					0
				],
				[
					194.9196180608345,
					0
				],
				[
					199.64765658163387,
					0
				],
				[
					204.37569510243324,
					0
				],
				[
					207.6248683823953,
					0
				],
				[
					212.49862830233846,
					0
				],
				[
					214.47356187500245,
					0
				],
				[
					216.44849544766643,
					0
				],
				[
					219.20473133627874,
					0
				],
				[
					222.5996260153846,
					0
				],
				[
					224.8628714458592,
					0
				],
				[
					228.60503518395896,
					0
				],
				[
					232.3471458552709,
					0
				],
				[
					236.08930959337053,
					0
				],
				[
					239.97714166382625,
					0
				],
				[
					243.71925233513818,
					0
				],
				[
					247.95435346458768,
					0
				],
				[
					252.68239198538706,
					0
				],
				[
					258.0491423634678,
					0
				],
				[
					261.29831564343,
					0
				],
				[
					263.5615610739046,
					0
				],
				[
					267.30372481200425,
					0
				],
				[
					271.53882594145375,
					0
				],
				[
					278.87737895172165,
					0
				],
				[
					284.0983548638708,
					0
				],
				[
					289.3193838428077,
					0
				],
				[
					294.54035975495697,
					0
				],
				[
					301.87891276522475,
					0
				],
				[
					307.0999417441617,
					0
				],
				[
					312.32091765631094,
					0
				],
				[
					317.049009243898,
					0
				],
				[
					321.2840573065597,
					0
				],
				[
					325.02622104465945,
					0
				],
				[
					329.8999809646026,
					0
				],
				[
					333.14915424456467,
					0
				],
				[
					336.8913179826643,
					0
				],
				[
					343.73688053479464,
					0
				],
				[
					347.97198166424414,
					0
				],
				[
					352.20708279369364,
					0
				],
				[
					355.9491934650056,
					0
				],
				[
					359.6913572031052,
					0
				],
				[
					363.9264583325547,
					0
				],
				[
					370.2790834933352,
					0
				],
				[
					374.5141846227847,
					0
				],
				[
					376.98205558679854,
					0
				],
				[
					378.2593731677857,
					0
				],
				[
					383.62612354586645,
					0
				],
				[
					386.38235943447876,
					0
				],
				[
					390.1244701057907,
					0
				],
				[
					394.85250862659007,
					0
				],
				[
					399.08760975603957,
					0
				],
				[
					403.46843228463285,
					0
				],
				[
					406.22461510645735,
					0
				],
				[
					408.98090406185736,
					0
				],
				[
					412.2300773418194,
					0
				],
				[
					414.5553578471663,
					0
				],
				[
					414.5553578471663,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "text",
			"version": 174,
			"versionNonce": 895706478,
			"isDeleted": false,
			"id": "If5ukpSg",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -736.8926998157369,
			"y": -4903.280823805154,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 213.90391540527344,
			"height": 60,
			"seed": 1208034218,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670717,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 1,
			"text": "Constant 사용시\nload, store 과정이 없어지므로\n굉장히 빨라짐",
			"rawText": "Constant 사용시\nload, store 과정이 없어지므로\n굉장히 빨라짐",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Constant 사용시\nload, store 과정이 없어지므로\n굉장히 빨라짐",
			"lineHeight": 1.25,
			"baseline": 54
		},
		{
			"type": "text",
			"version": 131,
			"versionNonce": 1359114354,
			"isDeleted": false,
			"id": "it1Vi1Lz",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -532.3518608698457,
			"y": -4775.498506324406,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 427.1678771972656,
			"height": 40,
			"seed": 1149448170,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670717,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 1,
			"text": "0은 매우 자주 사용하기 때문에 x0 레지스터에 따로 저장해놓음\n쓰기는 무시됨",
			"rawText": "0은 매우 자주 사용하기 때문에 x0 레지스터에 따로 저장해놓음\n쓰기는 무시됨",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "0은 매우 자주 사용하기 때문에 x0 레지스터에 따로 저장해놓음\n쓰기는 무시됨",
			"lineHeight": 1.25,
			"baseline": 34
		},
		{
			"type": "text",
			"version": 204,
			"versionNonce": 183535534,
			"isDeleted": false,
			"id": "3mrlKz47",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 557.2011501148254,
			"y": -4986.439969340592,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 344.47991943359375,
			"height": 60,
			"seed": 477054518,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670717,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 1,
			"text": "운영체제마다 데이터 타입이 차지하는 바이트가 다름\n\n그래서 혹시 모르니까 int64, int32같은 걸 쓴다",
			"rawText": "운영체제마다 데이터 타입이 차지하는 바이트가 다름\n\n그래서 혹시 모르니까 int64, int32같은 걸 쓴다",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "운영체제마다 데이터 타입이 차지하는 바이트가 다름\n\n그래서 혹시 모르니까 int64, int32같은 걸 쓴다",
			"lineHeight": 1.25,
			"baseline": 54
		},
		{
			"type": "freedraw",
			"version": 48,
			"versionNonce": 1073713714,
			"isDeleted": false,
			"id": "mod03kf9W95nlGiB-bK_6",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -191.47267992182913,
			"y": -4564.429072749579,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 143.605573249666,
			"height": 0.45576410653575294,
			"seed": 119313450,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670717,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.17363452949689417,
					0
				],
				[
					2.6415054935106355,
					0.17360799610378308
				],
				[
					4.904803990773075,
					0.45576410653575294
				],
				[
					8.15397727073514,
					0.45576410653575294
				],
				[
					12.534746732540725,
					0.45576410653575294
				],
				[
					15.78392001250279,
					0.45576410653575294
				],
				[
					20.657732999233758,
					0.45576410653575294
				],
				[
					23.906906279195823,
					0.45576410653575294
				],
				[
					26.66308910102032,
					0.45576410653575294
				],
				[
					29.419324989632628,
					0.45576410653575294
				],
				[
					32.17556087824482,
					0.45576410653575294
				],
				[
					36.55638340683822,
					0.45576410653575294
				],
				[
					39.80555668680029,
					0.45576410653575294
				],
				[
					43.54766735811222,
					0.45576410653575294
				],
				[
					46.796840638074286,
					0.45576410653575294
				],
				[
					50.04601391803635,
					0.45576410653575294
				],
				[
					54.91982690476732,
					0.45576410653575294
				],
				[
					58.169000184729384,
					0.45576410653575294
				],
				[
					60.92518300655388,
					0.45576410653575294
				],
				[
					64.66734674465363,
					0.45576410653575294
				],
				[
					70.52698144729641,
					0.45576410653575294
				],
				[
					74.26914518539604,
					0.45576410653575294
				],
				[
					78.50419324805785,
					0.45576410653575294
				],
				[
					82.73934744429516,
					0.45576410653575294
				],
				[
					87.96037642323199,
					0.45576410653575294
				],
				[
					95.29887636671208,
					0.45576410653575294
				],
				[
					99.53392442937388,
					0.45576410653575294
				],
				[
					103.27608816747363,
					0.45576410653575294
				],
				[
					107.51124236371083,
					0.45576410653575294
				],
				[
					113.8638675244913,
					0.45576410653575294
				],
				[
					118.59190604529056,
					0.45576410653575294
				],
				[
					122.82695410795236,
					0.45576410653575294
				],
				[
					127.06210830418968,
					0.45576410653575294
				],
				[
					128.68669494417065,
					0.45576410653575294
				],
				[
					133.7061762632576,
					0.45576410653575294
				],
				[
					135.96936862694452,
					0.45576410653575294
				],
				[
					137.73967666606939,
					0.45576410653575294
				],
				[
					140.00297516333183,
					0.45576410653575294
				],
				[
					142.26627366059427,
					0.45576410653575294
				],
				[
					143.605573249666,
					0.45576410653575294
				],
				[
					143.605573249666,
					0.45576410653575294
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 83,
			"versionNonce": 1864327662,
			"isDeleted": false,
			"id": "qPe1ZN0aVW7sQGPKksb-O",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -526.131743478061,
			"y": -4431.556973722681,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 141.05088502090376,
			"height": 0.6045899127620942,
			"seed": 76365610,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670717,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.6386587904936505,
					0
				],
				[
					2.9019572877560904,
					0
				],
				[
					6.151130567718155,
					0
				],
				[
					7.921438606843026,
					0
				],
				[
					8.910444330019573,
					0
				],
				[
					10.249796985879016,
					0
				],
				[
					10.950490851244922,
					0
				],
				[
					11.939496574421355,
					0
				],
				[
					13.421492755735471,
					0
				],
				[
					14.122133554313677,
					0
				],
				[
					14.996461949176364,
					0
				],
				[
					15.520390344568455,
					0
				],
				[
					16.332683664558942,
					0
				],
				[
					18.45333863636671,
					0
				],
				[
					19.73070928414171,
					0
				],
				[
					21.035939995482067,
					0.28212957703817665
				],
				[
					22.024945718658614,
					0.28212957703817665
				],
				[
					22.375292651341567,
					0.28212957703817665
				],
				[
					25.627596871780497,
					0.28212957703817665
				],
				[
					26.616602594957044,
					0.28212957703817665
				],
				[
					28.879848025431727,
					0.28212957703817665
				],
				[
					31.143146522694167,
					0.28212957703817665
				],
				[
					34.04505074366244,
					0.28212957703817665
				],
				[
					36.30834924092488,
					0.28212957703817665
				],
				[
					39.06453206274938,
					0.28212957703817665
				],
				[
					41.32783056001182,
					0.28212957703817665
				],
				[
					43.9414229231694,
					0.28212957703817665
				],
				[
					44.29176985585235,
					0.28212957703817665
				],
				[
					47.89129006849737,
					0.28212957703817665
				],
				[
					49.8662236411613,
					0.28212957703817665
				],
				[
					51.348166755687714,
					0.28212957703817665
				],
				[
					53.11847479481253,
					0.28212957703817665
				],
				[
					54.107480517989075,
					0.28212957703817665
				],
				[
					56.721072881146654,
					0.28212957703817665
				],
				[
					58.491380920271524,
					0.28212957703817665
				],
				[
					61.74055420023359,
					0.28212957703817665
				],
				[
					65.13544887933949,
					0.6045899127620942
				],
				[
					67.89168476795174,
					0.6045899127620942
				],
				[
					68.88069049112829,
					0.6045899127620942
				],
				[
					71.14398898839073,
					0.6045899127620942
				],
				[
					73.40723441886541,
					0.6045899127620942
				],
				[
					76.30919170662145,
					0.6045899127620942
				],
				[
					79.55836498658351,
					0.6045899127620942
				],
				[
					82.31454780840807,
					0.6045899127620942
				],
				[
					84.08485584753288,
					0.6045899127620942
				],
				[
					85.85516388665775,
					0.6045899127620942
				],
				[
					88.46880931660309,
					0.6045899127620942
				],
				[
					90.44368982247931,
					0.6045899127620942
				],
				[
					91.43274861244356,
					0.6045899127620942
				],
				[
					94.0463409756012,
					0.6045899127620942
				],
				[
					96.30958640607582,
					0.6045899127620942
				],
				[
					98.5728318365505,
					0.6045899127620942
				],
				[
					100.83613033381295,
					0.6045899127620942
				],
				[
					104.23102501291885,
					0.6045899127620942
				],
				[
					106.49427044339353,
					0.6045899127620942
				],
				[
					109.25050633200578,
					0.6045899127620942
				],
				[
					111.0208143711306,
					0.6045899127620942
				],
				[
					113.28405980160528,
					0.6045899127620942
				],
				[
					115.40471477341305,
					0.6045899127620942
				],
				[
					116.53636402204427,
					0.6045899127620942
				],
				[
					119.93125870115011,
					0.6045899127620942
				],
				[
					122.68744152297467,
					0.6045899127620942
				],
				[
					125.79402434426981,
					0.6045899127620942
				],
				[
					127.7689579169338,
					0.6045899127620942
				],
				[
					129.5392659560586,
					0.6045899127620942
				],
				[
					131.8025113865333,
					0.6045899127620942
				],
				[
					133.0798820343083,
					0.6045899127620942
				],
				[
					135.3462053384721,
					0.6045899127620942
				],
				[
					135.69655227115504,
					0.6045899127620942
				],
				[
					136.6855579943316,
					0.6045899127620942
				],
				[
					137.67461678429584,
					0.6045899127620942
				],
				[
					138.66362250747238,
					0.6045899127620942
				],
				[
					139.82626276014582,
					0.6045899127620942
				],
				[
					140.52690355872397,
					0.6045899127620942
				],
				[
					140.87725049140687,
					0.6045899127620942
				],
				[
					141.05088502090376,
					0.6045899127620942
				],
				[
					141.05088502090376,
					0.6045899127620942
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 41,
			"versionNonce": 510819314,
			"isDeleted": false,
			"id": "4Vtnu8ggX-lw9LhtGnE-x",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -135.8769944083599,
			"y": -4453.340094089592,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 35.908384861701734,
			"height": 1.667995272355256,
			"seed": 1248393322,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670717,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.3502938658951962,
					0
				],
				[
					2.1206549718077667,
					-0.2852339841219873
				],
				[
					4.876837793632262,
					-0.2852339841219873
				],
				[
					5.577531658998055,
					-0.46194638730776205
				],
				[
					7.347839698122925,
					-0.46194638730776205
				],
				[
					8.048533563488832,
					-0.8153977270740143
				],
				[
					8.398880496171728,
					-0.8153977270740143
				],
				[
					8.922861958351518,
					-0.8153977270740143
				],
				[
					9.270024883769793,
					-0.8153977270740143
				],
				[
					9.617293942763581,
					-0.8153977270740143
				],
				[
					10.42964032954194,
					-0.8153977270740143
				],
				[
					11.418592985930673,
					-1.029309948467926
				],
				[
					13.53924795773844,
					-1.029309948467926
				],
				[
					15.021191072264855,
					-1.3145439325899133
				],
				[
					15.721884937630648,
					-1.4912828691694813
				],
				[
					16.24586639981044,
					-1.4912828691694813
				],
				[
					17.40845358569618,
					-1.4912828691694813
				],
				[
					18.220799972474424,
					-1.4912828691694813
				],
				[
					19.498117553461725,
					-1.4912828691694813
				],
				[
					21.761416050724165,
					-1.4912828691694813
				],
				[
					23.038733631711352,
					-1.4912828691694813
				],
				[
					24.027792421675713,
					-1.667995272355256
				],
				[
					25.860082468885025,
					-1.667995272355256
				],
				[
					28.12338096614735,
					-1.667995272355256
				],
				[
					29.400698547134652,
					-1.667995272355256
				],
				[
					31.375632119798638,
					-1.667995272355256
				],
				[
					32.18787237300137,
					-1.667995272355256
				],
				[
					32.82658423028272,
					-1.667995272355256
				],
				[
					33.17385328927651,
					-1.667995272355256
				],
				[
					33.347487818773516,
					-1.667995272355256
				],
				[
					34.22171008006069,
					-1.667995272355256
				],
				[
					34.922403945426595,
					-1.667995272355256
				],
				[
					35.26967300442038,
					-1.667995272355256
				],
				[
					35.908384861701734,
					-1.667995272355256
				],
				[
					35.908384861701734,
					-1.667995272355256
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 163,
			"versionNonce": 351859758,
			"isDeleted": false,
			"id": "2oM6KgZAbR_gfmuIc8jZr",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -493.0167943231798,
			"y": -4410.871354126488,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 192.06420034592963,
			"height": 1.8199254856644984,
			"seed": 1141460522,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670717,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.6386587904936505,
					0
				],
				[
					1.6277175804579542,
					0
				],
				[
					4.095588544471752,
					0
				],
				[
					6.5045553740902164,
					-0.21393875478770497
				],
				[
					8.27486341321503,
					-0.21393875478770497
				],
				[
					10.0451714523399,
					-0.21393875478770497
				],
				[
					11.034177175516447,
					-0.21393875478770497
				],
				[
					12.516173356830564,
					-0.21393875478770497
				],
				[
					14.841453862177445,
					-0.21393875478770497
				],
				[
					16.61176190130226,
					-0.21393875478770497
				],
				[
					19.86093518126438,
					-0.21393875478770497
				],
				[
					21.631243220389194,
					-0.21393875478770497
				],
				[
					24.24483558354683,
					-0.21393875478770497
				],
				[
					24.945529448912623,
					-0.21393875478770497
				],
				[
					25.29582331480782,
					-0.21393875478770497
				],
				[
					25.646170247490772,
					-0.21393875478770497
				],
				[
					26.346864112856565,
					-0.21393875478770497
				],
				[
					28.262893551125217,
					-0.21393875478770497
				],
				[
					30.03320159025003,
					-0.21393875478770497
				],
				[
					31.515144704776446,
					-0.21393875478770497
				],
				[
					32.215838570142296,
					-0.21393875478770497
				],
				[
					33.98614660926711,
					-0.21393875478770497
				],
				[
					36.59973897242469,
					-0.21393875478770497
				],
				[
					39.35597486103694,
					-0.21393875478770497
				],
				[
					42.11221074964919,
					-0.21393875478770497
				],
				[
					44.72580311280683,
					-0.21393875478770497
				],
				[
					46.20774622733319,
					-0.21393875478770497
				],
				[
					47.19680501729749,
					-0.21393875478770497
				],
				[
					48.18581074047404,
					-0.21393875478770497
				],
				[
					50.160744313138025,
					-0.21393875478770497
				],
				[
					54.54156684173131,
					-0.21393875478770497
				],
				[
					56.31182181406842,
					-0.21393875478770497
				],
				[
					57.589192461843425,
					-0.21393875478770497
				],
				[
					58.57819818501997,
					-0.21393875478770497
				],
				[
					59.45252657988266,
					-0.21393875478770497
				],
				[
					60.15316737846075,
					-0.21393875478770497
				],
				[
					61.635163559774924,
					-0.21393875478770497
				],
				[
					62.62416928295147,
					-0.21393875478770497
				],
				[
					64.39447732207628,
					-0.21393875478770497
				],
				[
					67.78937200118219,
					-0.21393875478770497
				],
				[
					69.559680040307,
					-0.21393875478770497
				],
				[
					71.32998807943187,
					-0.21393875478770497
				],
				[
					73.10029611855668,
					-0.21393875478770497
				],
				[
					74.37766676633169,
					-0.21393875478770497
				],
				[
					75.54025395221737,
					-0.21393875478770497
				],
				[
					76.52931274218167,
					-0.21393875478770497
				],
				[
					77.22995354075977,
					-0.21393875478770497
				],
				[
					79.00026157988464,
					-0.21393875478770497
				],
				[
					80.05130237793338,
					-0.21393875478770497
				],
				[
					82.80753826654563,
					-0.21393875478770497
				],
				[
					84.57784630567045,
					-0.21393875478770497
				],
				[
					85.566852028847,
					-0.21393875478770497
				],
				[
					87.2224296728703,
					-0.21393875478770497
				],
				[
					87.92312353823615,
					-0.21393875478770497
				],
				[
					88.44705193362819,
					-0.21393875478770497
				],
				[
					89.43611072359249,
					-0.21393875478770497
				],
				[
					90.13675152217058,
					-0.21393875478770497
				],
				[
					91.18779232021933,
					-0.21393875478770497
				],
				[
					92.17679804339588,
					-0.21393875478770497
				],
				[
					93.65879422471,
					-0.21393875478770497
				],
				[
					94.18272262010208,
					-0.21393875478770497
				],
				[
					95.52207527596158,
					-0.21393875478770497
				],
				[
					97.32029644543951,
					-0.21393875478770497
				],
				[
					98.62558022356762,
					-0.21393875478770497
				],
				[
					99.26423901406122,
					-0.21393875478770497
				],
				[
					99.78822047624107,
					-0.21393875478770497
				],
				[
					101.73210997807502,
					-0.21393875478770497
				],
				[
					102.72111570125156,
					-0.21393875478770497
				],
				[
					103.71017449121587,
					-0.21393875478770497
				],
				[
					104.34883328170952,
					-0.21393875478770497
				],
				[
					105.65406399304987,
					-0.21393875478770497
				],
				[
					106.70510479109862,
					-0.21393875478770497
				],
				[
					107.69411051427517,
					-0.21393875478770497
				],
				[
					108.39480437964102,
					-0.21393875478770497
				],
				[
					109.38381010281756,
					-0.21393875478770497
				],
				[
					110.08450396818341,
					-0.21393875478770497
				],
				[
					112.23301900355654,
					-0.21393875478770497
				],
				[
					112.93371286892233,
					-0.21393875478770497
				],
				[
					113.63440673428818,
					-0.21393875478770497
				],
				[
					115.60934030695216,
					-0.21393875478770497
				],
				[
					117.44163035416148,
					-0.21393875478770497
				],
				[
					118.14232421952732,
					-0.21393875478770497
				],
				[
					119.13132994270387,
					-0.21393875478770497
				],
				[
					119.83202380806966,
					-0.21393875478770497
				],
				[
					120.70629913614465,
					-0.21393875478770497
				],
				[
					121.98366978391965,
					-0.21393875478770497
				],
				[
					122.9726755070962,
					-0.21393875478770497
				],
				[
					123.96168123027275,
					-0.21393875478770497
				],
				[
					124.94760907976018,
					-0.21393875478770497
				],
				[
					125.64830294512603,
					-0.21393875478770497
				],
				[
					126.17228440730582,
					-0.21393875478770497
				],
				[
					127.16129013048237,
					-0.21393875478770497
				],
				[
					127.86193092906046,
					-0.21393875478770497
				],
				[
					130.18721143440735,
					-0.21393875478770497
				],
				[
					130.8879052997732,
					-0.21393875478770497
				],
				[
					131.41188676195304,
					-0.21393875478770497
				],
				[
					131.76223369463594,
					-0.21393875478770497
				],
				[
					132.92482088052162,
					-0.21393875478770497
				],
				[
					133.62551474588747,
					-0.21393875478770497
				],
				[
					134.14949620806732,
					-0.21393875478770497
				],
				[
					134.67342460345935,
					-0.21393875478770497
				],
				[
					135.1974060656392,
					-0.21393875478770497
				],
				[
					136.0096993856297,
					-0.21393875478770497
				],
				[
					136.71039325099554,
					-0.21393875478770497
				],
				[
					137.69939897417208,
					-0.21393875478770497
				],
				[
					138.68840469734863,
					-0.21393875478770497
				],
				[
					139.38909856271448,
					-0.21393875478770497
				],
				[
					139.7363145549205,
					-0.21393875478770497
				],
				[
					139.9099490844174,
					-0.21393875478770497
				],
				[
					140.0835836139143,
					-0.21393875478770497
				],
				[
					140.2572181434112,
					-0.21393875478770497
				],
				[
					141.7081702538954,
					-0.21393875478770497
				],
				[
					142.23209864928742,
					-0.21393875478770497
				],
				[
					142.75608011146727,
					-0.21393875478770497
				],
				[
					143.28006157364706,
					-0.21393875478770497
				],
				[
					143.80398996903915,
					-0.21393875478770497
				],
				[
					144.78991781852653,
					-0.21393875478770497
				],
				[
					145.31389928070638,
					-0.3906511579734797
				],
				[
					146.30290500388293,
					-0.3906511579734797
				],
				[
					147.58022258487017,
					-0.3906511579734797
				],
				[
					149.49625202313882,
					-0.3906511579734797
				],
				[
					150.48525774631537,
					-0.3906511579734797
				],
				[
					151.96725392762949,
					-0.675885142095467
				],
				[
					152.49123538980928,
					-0.675885142095467
				],
				[
					154.0041695083779,
					-0.675885142095467
				],
				[
					154.64288136565926,
					-0.675885142095467
				],
				[
					156.41318940478413,
					-0.675885142095467
				],
				[
					158.21448844795117,
					-0.675885142095467
				],
				[
					158.56483538063412,
					-0.675885142095467
				],
				[
					160.36613442380116,
					-0.675885142095467
				],
				[
					161.3551401469777,
					-0.675885142095467
				],
				[
					164.2570974347338,
					-0.675885142095467
				],
				[
					165.59645009059324,
					-0.675885142095467
				],
				[
					166.58545581376978,
					-0.675885142095467
				],
				[
					167.57446153694633,
					-0.675885142095467
				],
				[
					168.09844299912618,
					-0.675885142095467
				],
				[
					170.39267943364308,
					-0.675885142095467
				],
				[
					171.20497275363357,
					-0.675885142095467
				],
				[
					171.72895421581342,
					-0.675885142095467
				],
				[
					172.71795993898996,
					-0.675885142095467
				],
				[
					174.48826797811478,
					-0.675885142095467
				],
				[
					176.75151340858946,
					-0.675885142095467
				],
				[
					179.6534706963455,
					-0.675885142095467
				],
				[
					182.40970658495775,
					-1.0014233515084925
				],
				[
					183.5413027668012,
					-1.0014233515084925
				],
				[
					184.59234356485,
					-1.0014233515084925
				],
				[
					185.2310023553436,
					-1.4292743276910187
				],
				[
					186.22000807852015,
					-1.4292743276910187
				],
				[
					187.35165732715137,
					-1.4292743276910187
				],
				[
					188.69100998301082,
					-1.6059867308767934
				],
				[
					189.96838063078582,
					-1.8199254856644984
				],
				[
					190.3155966229919,
					-1.8199254856644984
				],
				[
					190.6659435556748,
					-1.8199254856644984
				],
				[
					191.18992501785465,
					-1.8199254856644984
				],
				[
					191.54027195053754,
					-1.8199254856644984
				],
				[
					192.06420034592963,
					-1.8199254856644984
				],
				[
					192.06420034592963,
					-1.8199254856644984
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 55,
			"versionNonce": 174206386,
			"isDeleted": false,
			"id": "gCgT3eXjvtS8RL0ifRbf_",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 502.3476566947377,
			"y": -4621.903561349715,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 113.83897920103959,
			"height": 26.12674307729594,
			"seed": 1025475434,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670717,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-2.0586729637233248,
					2.0493332090800322
				],
				[
					-3.57468495598107,
					3.661528754122628
				],
				[
					-4.904750923985375,
					5.1342117141884955
				],
				[
					-6.84869349260714,
					6.858006713855502
				],
				[
					-9.611138195385365,
					8.39577608908803
				],
				[
					-13.508256953696218,
					9.651415887282383
				],
				[
					-16.763585981036613,
					10.28389239700391
				],
				[
					-19.033146359252783,
					10.606326199334035
				],
				[
					-24.26033108556794,
					11.350428697073767
				],
				[
					-32.594045566390605,
					12.482051412311193
				],
				[
					-39.30020166711847,
					12.869598163201772
				],
				[
					-47.482039001419025,
					12.869598163201772
				],
				[
					-56.64667324473021,
					12.869598163201772
				],
				[
					-65.32150103716833,
					12.869598163201772
				],
				[
					-78.0887333668137,
					11.641844961967763
				],
				[
					-85.28777379210374,
					9.24216482020438
				],
				[
					-91.11339268380289,
					6.523155283193773
				],
				[
					-95.9530306592269,
					3.9095629200364783
				],
				[
					-97.93417304605691,
					2.579496952032059
				],
				[
					-98.11088544924291,
					2.4027845488462845
				],
				[
					-98.32479767063717,
					1.4075700115035943
				],
				[
					-98.32479767063717,
					0.7006938653657926
				],
				[
					-97.65201693562449,
					-1.2804485214646775
				],
				[
					-96.66301121244794,
					-3.0569388413614433
				],
				[
					-92.48681421739377,
					-6.06739117665893
				],
				[
					-90.22356878691903,
					-6.932406350272686
				],
				[
					-85.98846765746953,
					-8.005124931114551
				],
				[
					-79.28857343769528,
					-9.183260685809728
				],
				[
					-67.02048731356592,
					-11.229489487806859
				],
				[
					-59.33471831109205,
					-12.038704934107955
				],
				[
					-51.64884317504266,
					-12.847893847016167
				],
				[
					-39.38075705091319,
					-13.25714491409417
				],
				[
					-30.712191139428796,
					-13.25714491409417
				],
				[
					-22.04351909436889,
					-13.25714491409417
				],
				[
					-13.864759633757444,
					-13.25714491409417
				],
				[
					-6.178990631283568,
					-13.25714491409417
				],
				[
					4.117239793871022,
					-13.25714491409417
				],
				[
					8.845384448245909,
					-12.181321926169403
				],
				[
					12.587442052770143,
					-11.183002981743812
				],
				[
					13.610569720465719,
					-10.159875314047895
				],
				[
					14.525228874013578,
					-8.854618069313801
				],
				[
					15.191747728072528,
					-6.733989630899487
				],
				[
					15.191747728072528,
					-4.759056058235728
				],
				[
					15.514181530402425,
					-2.4957840943670817
				],
				[
					15.514181530402425,
					-1.0138144464472134
				],
				[
					15.12360997260987,
					-0.20152112645610032
				],
				[
					14.044656044207954,
					2.061750837411637
				],
				[
					12.175113112002691,
					4.166883773805239
				],
				[
					12.175113112002691,
					4.166883773805239
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 60,
			"versionNonce": 1717976686,
			"isDeleted": false,
			"id": "gVHmbxhHN6PP8q3PAkVDM",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 143.60189658243473,
			"y": -4505.249415592275,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 83.88951700184884,
			"height": 28.328006499686126,
			"seed": 443729834,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670717,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.8185021341565175,
					0.5611812803881548
				],
				[
					-4.073884228284612,
					1.857125303873545
				],
				[
					-6.343338472925268,
					2.7159316633214985
				],
				[
					-9.105730108915793,
					4.253701038554027
				],
				[
					-14.974704566201467,
					6.662667868172321
				],
				[
					-17.73714926897975,
					6.985128203896238
				],
				[
					-23.950261844782347,
					7.754012891512502
				],
				[
					-35.73475033220484,
					7.754012891512502
				],
				[
					-43.91966554019456,
					8.566306211502706
				],
				[
					-50.625768574134725,
					8.566306211502706
				],
				[
					-55.85295330044994,
					8.566306211502706
				],
				[
					-61.228990366385744,
					8.566306211502706
				],
				[
					-64.48437246051384,
					8.566306211502706
				],
				[
					-67.24681716329212,
					8.566306211502706
				],
				[
					-68.55825668879845,
					8.10433329080115
				],
				[
					-70.05261743165687,
					7.037823524125088
				],
				[
					-73.62114664025961,
					3.4414077185638234
				],
				[
					-75.60844477446784,
					2.0214466121215082
				],
				[
					-75.9619226476276,
					1.8447076755419403
				],
				[
					-79.36610401458864,
					0.4123554741618136
				],
				[
					-80.18460614874516,
					-0.19220790520648734
				],
				[
					-80.18460614874516,
					-0.5456592449727395
				],
				[
					-80.53803095511722,
					-0.8991105847389917
				],
				[
					-80.53803095511722,
					-1.6059867308767934
				],
				[
					-78.62200151684857,
					-5.131080773710892
				],
				[
					-75.2333156519087,
					-7.521474227619365
				],
				[
					-71.81671665661571,
					-9.204965001996243
				],
				[
					-69.87898290215998,
					-10.395491851628321
				],
				[
					-66.13687223084798,
					-11.753470949985967
				],
				[
					-60.77012185276726,
					-13.421466222341223
				],
				[
					-54.56321809113069,
					-14.977835506678275
				],
				[
					-48.35631432949407,
					-16.534204791014417
				],
				[
					-43.135285350557126,
					-18.0285920672668
				],
				[
					-36.78266018977672,
					-19.08271073900505
				],
				[
					-33.040549518464786,
					-19.76170028818342
				],
				[
					-29.791323171714964,
					-19.76170028818342
				],
				[
					-26.542149891752842,
					-19.76170028818342
				],
				[
					-20.189524730972437,
					-19.76170028818342
				],
				[
					-15.461486210173064,
					-19.76170028818342
				],
				[
					-11.22638508072356,
					-19.76170028818342
				],
				[
					-7.977211800761438,
					-19.116806150130287
				],
				[
					-4.728038520799373,
					-18.471938545470948
				],
				[
					-1.4788652408372513,
					-17.8270709408107
				],
				[
					0.3193559286406753,
					-17.17909892906846
				],
				[
					1.13164924863122,
					-16.580717830472167
				],
				[
					1.9780645131408505,
					-14.31744586660352
				],
				[
					2.32835837903599,
					-11.068272586641797
				],
				[
					3.0011391140487262,
					-6.687476591441737
				],
				[
					3.3514860467316225,
					-1.959411537248343
				],
				[
					3.3514860467316225,
					2.768626983550348
				],
				[
					3.3514860467316225,
					6.510764188256871
				],
				[
					3.1747736435456204,
					7.49976991143285
				],
				[
					2.8213488371735593,
					8.5507841760882
				],
				[
					2.8213488371735593,
					8.5507841760882
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 62,
			"versionNonce": 1224058738,
			"isDeleted": false,
			"id": "QrWLZRW9_J8LCuruXL9G7",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 182.06189179920955,
			"y": -4393.977489181541,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 103.2202619067674,
			"height": 35.554906988541916,
			"seed": 1631076778,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670717,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.5239814621800178
				],
				[
					0,
					0.6975629248890982
				],
				[
					-0.17671240318600212,
					0.871197454385765
				],
				[
					-2.9391571059642843,
					0.871197454385765
				],
				[
					-5.7016018087425095,
					0.871197454385765
				],
				[
					-11.421723926407537,
					0.871197454385765
				],
				[
					-19.606692201185012,
					1.6834907743759686
				],
				[
					-24.189009322840548,
					2.0989506556206834
				],
				[
					-41.0488053900562,
					4.142075050534913
				],
				[
					-48.74078320669605,
					5.754244062183716
				],
				[
					-54.95389578249865,
					6.5293375639657825
				],
				[
					-61.1670083583013,
					6.5293375639657825
				],
				[
					-66.39424615140422,
					6.5293375639657825
				],
				[
					-73.74208584952714,
					6.5293375639657825
				],
				[
					-77.49040533500511,
					6.5293375639657825
				],
				[
					-80.7457874291332,
					6.5293375639657825
				],
				[
					-82.72692981596316,
					6.352625160780008
				],
				[
					-85.34980886697588,
					5.31092411737427
				],
				[
					-86.1683110011324,
					4.920246426006088
				],
				[
					-86.3450234043184,
					4.743534022820313
				],
				[
					-86.94961331708066,
					3.9250318886633977
				],
				[
					-87.47975052663872,
					3.218182275919389
				],
				[
					-88.11846238392013,
					-0.037199818208137
				],
				[
					-88.40369636804166,
					-2.306654062848793
				],
				[
					-89.05477278686732,
					-5.5620361569772285
				],
				[
					-89.38028446288627,
					-7.543178543806789
				],
				[
					-89.38028446288627,
					-9.673120203469807
				],
				[
					-89.38028446288627,
					-10.026545009842266
				],
				[
					-89.60661431261246,
					-12.296052321270508
				],
				[
					-88.02235843131655,
					-14.41665422629012
				],
				[
					-84.95918424239557,
					-17.132612423005412
				],
				[
					-81.07135217193985,
					-19.188154446252156
				],
				[
					-78.80805367467747,
					-20.592566983885263
				],
				[
					-74.5729525452279,
					-22.366005963486714
				],
				[
					-68.36604878359128,
					-24.69744221621204
				],
				[
					-58.562702682998804,
					-27.05376679238907
				],
				[
					-51.86286153001237,
					-28.244267108627355
				],
				[
					-45.655904701587986,
					-29.025569424576133
				],
				[
					-39.44900093995136,
					-29.025569424576133
				],
				[
					-33.24209717831474,
					-29.025569424576133
				],
				[
					-22.45282322823482,
					-29.025569424576133
				],
				[
					-15.752929008460626,
					-28.638022673684645
				],
				[
					-9.546025246824001,
					-27.087835670119603
				],
				[
					-4.324996267887059,
					-25.599683741427725
				],
				[
					2.027628892893347,
					-23.488315457474528
				],
				[
					6.262730022342851,
					-21.727347172993177
				],
				[
					6.436311485051988,
					-21.20336571081316
				],
				[
					6.783580544045776,
					-20.67938424863314
				],
				[
					7.930725294698107,
					-18.881216145942744
				],
				[
					9.3072777687658,
					-16.974473395529458
				],
				[
					9.955223247114532,
					-14.21823750691783
				],
				[
					10.553604345710824,
					-13.229231783740943
				],
				[
					11.551949823530265,
					-11.254298211077185
				],
				[
					12.764154455956145,
					-7.366466140621014
				],
				[
					13.61364759415494,
					-5.878261145140641
				],
				[
					13.61364759415494,
					-5.878261145140641
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 55,
			"versionNonce": 674250926,
			"isDeleted": false,
			"id": "du0c5PB0TuLLmMIoV2su2",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 377.22333521179144,
			"y": -4392.563736889266,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 111.61914240293913,
			"height": 0,
			"seed": 215505194,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670717,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.3503469326828963,
					0
				],
				[
					2.613592363157636,
					0
				],
				[
					6.3557561012572705,
					0
				],
				[
					8.61900153173201,
					0
				],
				[
					12.361112203043945,
					0
				],
				[
					16.10327594114358,
					0
				],
				[
					20.977035861086733,
					0
				],
				[
					23.24028129156136,
					0
				],
				[
					24.51765193933636,
					0
				],
				[
					25.999595053862777,
					0
				],
				[
					28.613240483808113,
					0
				],
				[
					31.36942330563261,
					0
				],
				[
					33.63272180289505,
					0
				],
				[
					36.388904624719544,
					0
				],
				[
					38.652203121981984,
					0
				],
				[
					42.54008825922551,
					0
				],
				[
					44.80328062291244,
					0
				],
				[
					46.573588662037196,
					0
				],
				[
					48.05553177656361,
					0
				],
				[
					51.45042645566946,
					0
				],
				[
					54.20671541106947,
					0
				],
				[
					56.96289823289408,
					0
				],
				[
					60.21207151285614,
					0
				],
				[
					62.47537001011858,
					0
				],
				[
					65.37727423108686,
					0
				],
				[
					67.14758227021173,
					0
				],
				[
					68.91789030933649,
					0
				],
				[
					70.68819834846136,
					0
				],
				[
					75.06896781026694,
					0
				],
				[
					77.33226630752938,
					0
				],
				[
					80.08855526292939,
					0
				],
				[
					82.35174762661632,
					0
				],
				[
					84.61504612387864,
					0
				],
				[
					89.20044111922334,
					0
				],
				[
					91.95673007462335,
					0
				],
				[
					94.71291289644796,
					0
				],
				[
					96.97621139371029,
					0
				],
				[
					97.61481711741624,
					0
				],
				[
					100.86706827106741,
					0
				],
				[
					101.56776213643332,
					0
				],
				[
					102.55682092639756,
					0
				],
				[
					103.25751479176336,
					0
				],
				[
					103.78149625394326,
					0
				],
				[
					106.39503555031308,
					0
				],
				[
					108.65833404757552,
					0
				],
				[
					110.92163254483785,
					0
				],
				[
					111.44550787344224,
					0
				],
				[
					111.61914240293913,
					0
				],
				[
					111.61914240293913,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "text",
			"version": 47,
			"versionNonce": 1651763506,
			"isDeleted": false,
			"id": "ndRNtoCU",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 285.4702754685278,
			"y": -4349.75507761727,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 264.55987548828125,
			"height": 20,
			"seed": 1980086314,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670717,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 1,
			"text": "0.00000000000000000001 같은",
			"rawText": "0.00000000000000000001 같은",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "0.00000000000000000001 같은",
			"lineHeight": 1.25,
			"baseline": 14
		},
		{
			"type": "text",
			"version": 179,
			"versionNonce": 503315182,
			"isDeleted": false,
			"id": "1X7M9Inz",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -222.8977172210175,
			"y": -4002.485859423113,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 207.31195068359375,
			"height": 60,
			"seed": 1180564522,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670717,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 1,
			"text": "컴퓨터는 2진수로 받아들이는데\n사람은 10진수 단위로 개발함\n-> 제조사는 소비자를 속이나요",
			"rawText": "컴퓨터는 2진수로 받아들이는데\n사람은 10진수 단위로 개발함\n-> 제조사는 소비자를 속이나요",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "컴퓨터는 2진수로 받아들이는데\n사람은 10진수 단위로 개발함\n-> 제조사는 소비자를 속이나요",
			"lineHeight": 1.25,
			"baseline": 54
		},
		{
			"type": "freedraw",
			"version": 147,
			"versionNonce": 1044640498,
			"isDeleted": false,
			"id": "4VOgBlziCOWhXNDWegpv4",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 279.4161509888043,
			"y": -4198.741659399241,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 91.60012126098667,
			"height": 52.08915157964748,
			"seed": 192082422,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670717,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.35342480637200424,
					0.7006805986684412
				],
				[
					-2.632218805655498,
					2.9732525170893496
				],
				[
					-6.175912757594347,
					5.438032340717655
				],
				[
					-8.938304393584872,
					6.706089767243611
				],
				[
					-11.207811705013228,
					7.5648828599942135
				],
				[
					-18.555651403136267,
					10.485426790157362
				],
				[
					-22.796961346751743,
					11.892983534964515
				],
				[
					-27.03821822357952,
					13.300553546468109
				],
				[
					-31.279528167194997,
					14.354672218205451
				],
				[
					-35.52083811081053,
					15.055352816874802
				],
				[
					-41.389812568096204,
					15.405699749557243
				],
				[
					-44.15220420408673,
					15.405699749557243
				],
				[
					-46.914648906864954,
					15.405699749557243
				],
				[
					-50.66296839234292,
					15.405699749557243
				],
				[
					-59.489673331303095,
					13.086628058376846
				],
				[
					-62.5962561525983,
					11.92088339862039
				],
				[
					-70.15493019842637,
					7.753999624815151
				],
				[
					-70.68512047477219,
					7.047123478677349
				],
				[
					-71.0385452811442,
					6.516959735725322
				],
				[
					-71.32377926526578,
					5.205506943521868
				],
				[
					-71.67720407163785,
					1.8013123098644428
				],
				[
					-71.67720407163785,
					-0.961105859520103
				],
				[
					-71.02925859328911,
					-3.7235240289046487
				],
				[
					-69.16592447524982,
					-6.724676409650783
				],
				[
					-68.0187797245975,
					-9.84053265210423
				],
				[
					-67.48551157456257,
					-12.110000163441327
				],
				[
					-66.57090548780246,
					-13.598178625527908
				],
				[
					-64.74790212844829,
					-16.078467217873367
				],
				[
					-62.27382235026846,
					-18.013083298549645
				],
				[
					-61.284816627091914,
					-19.789586885142853
				],
				[
					-59.42148250905268,
					-22.226480111811725
				],
				[
					-57.93333058036029,
					-23.506928633275493
				],
				[
					-55.50265943455469,
					-24.768777245635647
				],
				[
					-51.1218369059614,
					-26.96383185386003
				],
				[
					-48.36560101734915,
					-28.098558976180357
				],
				[
					-45.11642773738703,
					-29.372811950175674
				],
				[
					-42.360191848774775,
					-30.30910908642545
				],
				[
					-40.58988380964996,
					-30.8082685586387
				],
				[
					-38.32663837917528,
					-30.8082685586387
				],
				[
					-33.94581585058194,
					-30.8082685586387
				],
				[
					-29.71076778792019,
					-30.8082685586387
				],
				[
					-25.822882650676718,
					-30.8082685586387
				],
				[
					-21.587781521227214,
					-30.8082685586387
				],
				[
					-16.859743000427898,
					-30.457934892652702
				],
				[
					-12.131704479628524,
					-29.382111904727026
				],
				[
					-8.389540741528776,
					-28.35589309664556
				],
				[
					-3.0228434302358664,
					-26.356150800711475
				],
				[
					0.2263298497263122,
					-25.060206777226085
				],
				[
					3.475503129688377,
					-23.764249487044253
				],
				[
					4.948159556359656,
					-22.617118003088763
				],
				[
					5.64577554803634,
					-22.269875477489222
				],
				[
					5.8194100775332345,
					-21.919541811503223
				],
				[
					5.9929915402424285,
					-21.395573616019647
				],
				[
					6.275147650674853,
					-19.13231491884835
				],
				[
					6.597581453004636,
					-15.24446958169574
				],
				[
					6.597581453004636,
					-12.488246959780554
				],
				[
					6.879684496649361,
					-10.224988262609259
				],
				[
					7.1618406070817855,
					-8.454680223484502
				],
				[
					6.985128203895783,
					-7.465661233610263
				],
				[
					4.979203627189577,
					-5.143498402043406
				],
				[
					3.773154742141969,
					-3.943658331161714
				],
				[
					0.7037717390550142,
					-1.2339354820069275
				],
				[
					-2.2260456122663754,
					0.713084960303604
				],
				[
					-7.602082678202237,
					3.7173417481326396
				],
				[
					-9.871536922842893,
					4.576134840883242
				],
				[
					-12.633981625621232,
					5.8441790007127565
				],
				[
					-14.903435870261887,
					6.408451421486461
				],
				[
					-18.158817964389982,
					7.378857235558826
				],
				[
					-24.52072981302547,
					8.429884766910618
				],
				[
					-28.762039756641002,
					8.429884766910618
				],
				[
					-32.51035924211891,
					8.429884766910618
				],
				[
					-35.765741336247004,
					8.429884766910618
				],
				[
					-36.76095587358958,
					8.039233608937138
				],
				[
					-36.93766827677558,
					8.039233608937138
				],
				[
					-37.291146149935344,
					7.685795535867328
				],
				[
					-39.445869999474496,
					5.856583362347919
				],
				[
					-42.06567117679805,
					3.5902202580928133
				],
				[
					-48.14240210809976,
					-2.839922212883721
				],
				[
					-49.98397884316421,
					-5.248902309199366
				],
				[
					-52.8115364945038,
					-8.783309573283077
				],
				[
					-54.43920100817394,
					-12.038691667410603
				],
				[
					-55.86229305509272,
					-14.45697171827851
				],
				[
					-56.71799500745749,
					-15.740524646825179
				],
				[
					-57.00322899157908,
					-18.009992158163186
				],
				[
					-57.00322899157908,
					-19.786495744757303
				],
				[
					-56.43896983750187,
					-22.05594998939796
				],
				[
					-53.192874431228915,
					-26.28794671176456
				],
				[
					-50.12970024230799,
					-28.678326898975683
				],
				[
					-46.24807698601825,
					-31.15240667715534
				],
				[
					-42.505913247918556,
					-32.863810581884536
				],
				[
					-38.61808117746284,
					-33.72881248880185
				],
				[
					-34.38298004801334,
					-34.43568863493965
				],
				[
					-30.147878918563833,
					-35.142578047774805
				],
				[
					-25.912777789114273,
					-35.496016120843706
				],
				[
					-18.57422477884643,
					-35.496016120843706
				],
				[
					-13.3532488666973,
					-35.496016120843706
				],
				[
					-9.118147737247796,
					-35.496016120843706
				],
				[
					-5.376037065935861,
					-35.496016120843706
				],
				[
					-3.605729026810991,
					-35.00306546279717
				],
				[
					-0.8525710118879033,
					-32.81731080912414
				],
				[
					0.20775647401603692,
					-31.329132347038467
				],
				[
					0.772015628093186,
					-29.06587364986717
				],
				[
					1.0944494304229693,
					-26.802601685998525
				],
				[
					1.7889344816228459,
					-22.567513823245463
				],
				[
					1.7889344816228459,
					-17.83946203574942
				],
				[
					1.7889344816228459,
					-11.486823608272061
				],
				[
					1.7889344816228459,
					-8.730614253053318
				],
				[
					0.5704679682431788,
					-5.974391631138133
				],
				[
					-1.7082729642526147,
					-3.3762815033051083
				],
				[
					-7.958638425051163,
					1.016918853529205
				],
				[
					-13.67876054271619,
					3.298790726502375
				],
				[
					-21.370791426143796,
					5.31092411737427
				],
				[
					-30.53542566945498,
					6.972710575563724
				],
				[
					-42.80977367453812,
					8.191150555549939
				],
				[
					-48.03695840085334,
					8.929044239123868
				],
				[
					-49.525163396333426,
					8.929044239123868
				],
				[
					-51.329540313189625,
					8.929044239123868
				],
				[
					-54.733721680150666,
					8.603506029710843
				],
				[
					-58.416981283854966,
					5.431836793248294
				],
				[
					-59.55170840617535,
					4.86447323208813
				],
				[
					-60.95617401059616,
					2.9205439301631486
				],
				[
					-63.42717591508682,
					-0.9487014978849402
				],
				[
					-67.53512902110276,
					-8.029933654384877
				],
				[
					-70.22312102067684,
					-15.033635233990935
				],
				[
					-70.54868576348349,
					-16.661326281055153
				],
				[
					-70.26652965305107,
					-19.42374445043879
				],
				[
					-67.99399753472125,
					-22.028050125741174
				],
				[
					-64.71998899809518,
					-25.661679016208836
				],
				[
					-61.191790548177494,
					-28.489196867457395
				],
				[
					-54.87944307929445,
					-31.64226619481633
				],
				[
					-46.21087716781,
					-34.12255478716179
				],
				[
					-30.501356791723595,
					-36.25250971352125
				],
				[
					-20.3569504463033,
					-36.683451830090235
				],
				[
					-12.181321926168721,
					-36.683451830090235
				],
				[
					-5.48142770639447,
					-36.683451830090235
				],
				[
					0.7254760552420976,
					-35.90835832830817
				],
				[
					8.184968274777475,
					-32.553781141190484
				],
				[
					11.713166724695157,
					-29.732445570713026
				],
				[
					15.439781893986037,
					-26.005817134725476
				],
				[
					18.037878755122506,
					-23.40770700689245
				],
				[
					19.57570119714285,
					-20.626688928403382
				],
				[
					19.922917189348823,
					-20.102733999618067
				],
				[
					19.922917189348823,
					-20.102733999618067
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 116,
			"versionNonce": 777940270,
			"isDeleted": false,
			"id": "1IxjYvaP89jR6jBMiIL8a",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 129.99429860208198,
			"y": -3983.1302261947444,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 391.6839437972105,
			"height": 7.688873409556891,
			"seed": 681532842,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670717,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.1736345294966668
				],
				[
					0,
					0.34724252559999513
				],
				[
					0,
					0.6975894582828914
				],
				[
					0,
					0.8712239877795582
				],
				[
					0.3472690589938452,
					1.0448319838828866
				],
				[
					1.336274782170392,
					1.0448319838828866
				],
				[
					3.1065828212952056,
					1.0448319838828866
				],
				[
					4.095588544471752,
					1.0448319838828866
				],
				[
					5.434941200331195,
					1.0448319838828866
				],
				[
					6.9169373816453685,
					1.0448319838828866
				],
				[
					8.194254962632613,
					1.0448319838828866
				],
				[
					10.457500393107296,
					1.0448319838828866
				],
				[
					14.345385530350768,
					1.0448319838828866
				],
				[
					16.608630960825394,
					1.0448319838828866
				],
				[
					18.378938999950265,
					1.2556663315876904
				],
				[
					21.62811227991233,
					1.5377959086263218
				],
				[
					23.891357710387013,
					1.8199254856649532
				],
				[
					27.286252389492915,
					2.1423592879946227
				],
				[
					28.563623037267917,
					2.3531936356998813
				],
				[
					29.087604499447707,
					2.3531936356998813
				],
				[
					30.569547613974123,
					2.3531936356998813
				],
				[
					31.55855333715067,
					2.3531936356998813
				],
				[
					34.95344801625657,
					2.917452789777144
				],
				[
					37.709683904868825,
					3.2398865921068136
				],
				[
					40.46591979348108,
					3.2398865921068136
				],
				[
					44.84674232207436,
					3.522016169145445
				],
				[
					48.095915602036484,
					3.8041457461840764
				],
				[
					51.34508888199855,
					4.154492678866973
				],
				[
					53.60833431247323,
					4.154492678866973
				],
				[
					58.9750316237662,
					4.504839611549869
				],
				[
					62.22425797051608,
					4.855186544232765
				],
				[
					63.50157555150332,
					4.855186544232765
				],
				[
					66.25781144011557,
					5.137316121271397
				],
				[
					69.5069847200777,
					5.459749923601066
				],
				[
					72.40894200783373,
					5.741879500639698
				],
				[
					74.67218743830841,
					6.024009077678329
				],
				[
					76.9354328687831,
					6.024009077678329
				],
				[
					79.19873136604548,
					6.3061386547169604
				],
				[
					83.57950082785106,
					6.62857245704663
				],
				[
					86.82867410781313,
					6.62857245704663
				],
				[
					89.58490999642544,
					6.62857245704663
				],
				[
					92.8340832763875,
					6.62857245704663
				],
				[
					96.08325655634962,
					6.62857245704663
				],
				[
					101.94294432578016,
					6.62857245704663
				],
				[
					105.68510806387985,
					6.62857245704663
				],
				[
					107.94835349435454,
					6.62857245704663
				],
				[
					111.69046416566647,
					6.62857245704663
				],
				[
					116.41850268646584,
					6.62857245704663
				],
				[
					124.2500461548712,
					6.62857245704663
				],
				[
					130.45694991650782,
					6.62857245704663
				],
				[
					136.6638536781445,
					6.62857245704663
				],
				[
					141.88488265708145,
					6.62857245704663
				],
				[
					149.22343566734924,
					6.62857245704663
				],
				[
					152.4726089473113,
					6.62857245704663
				],
				[
					155.72178222727337,
					6.62857245704663
				],
				[
					157.9850807245358,
					6.62857245704663
				],
				[
					161.0916104790433,
					6.62857245704663
				],
				[
					163.35485590951794,
					6.62857245704663
				],
				[
					165.61815440678038,
					6.62857245704663
				],
				[
					168.37433722860487,
					6.62857245704663
				],
				[
					170.34927080126886,
					6.62857245704663
				],
				[
					173.25122808902483,
					6.62857245704663
				],
				[
					176.500401368987,
					6.62857245704663
				],
				[
					180.24256510708665,
					6.62857245704663
				],
				[
					182.99874792891114,
					6.62857245704663
				],
				[
					188.85843569834174,
					6.62857245704663
				],
				[
					193.09353682779124,
					6.62857245704663
				],
				[
					196.3427101077533,
					5.977496038221034
				],
				[
					200.57781123720292,
					5.62407123184903
				],
				[
					206.4374990066334,
					5.270619892083232
				],
				[
					210.6725470692952,
					5.270619892083232
				],
				[
					215.40063865688228,
					5.270619892083232
				],
				[
					219.63573978633178,
					5.270619892083232
				],
				[
					223.8707878489936,
					5.270619892083232
				],
				[
					229.73047561842418,
					4.917168552317435
				],
				[
					233.96557674787368,
					4.917168552317435
				],
				[
					237.70768741918562,
					4.591630342904409
				],
				[
					241.94278854863512,
					4.591630342904409
				],
				[
					245.68495228673487,
					4.591630342904409
				],
				[
					252.03757744751522,
					4.591630342904409
				],
				[
					257.75154381780203,
					4.591630342904409
				],
				[
					262.972572796739,
					4.591630342904409
				],
				[
					267.20762085940066,
					4.591630342904409
				],
				[
					272.5743712374814,
					4.238205536532405
				],
				[
					274.8376697347438,
					4.238205536532405
				],
				[
					278.57972733926806,
					4.238205536532405
				],
				[
					283.800756318205,
					4.238205536532405
				],
				[
					289.02178529714195,
					4.238205536532405
				],
				[
					296.8532756987596,
					4.238205536532405
				],
				[
					300.59543943685924,
					4.238205536532405
				],
				[
					303.8446127168214,
					3.9126673271193795
				],
				[
					307.0937859967835,
					3.5871291177068088
				],
				[
					310.34295927674555,
					3.5871291177068088
				],
				[
					315.70970965482627,
					3.5871291177068088
				],
				[
					319.4517672593505,
					3.5871291177068088
				],
				[
					323.19393099745014,
					2.908139568527986
				],
				[
					326.9360947355499,
					2.582601359115415
				],
				[
					330.6782584736495,
					2.229176552742956
				],
				[
					337.03088363442987,
					1.8757252129771587
				],
				[
					341.75892215522924,
					1.5222738732113612
				],
				[
					346.4869606760286,
					1.5222738732113612
				],
				[
					351.70798965496556,
					1.1471447506523873
				],
				[
					359.04648959844565,
					0.7936934108861351
				],
				[
					364.2675185773826,
					0.4185642883271612
				],
				[
					369.48854755631953,
					-0.3317204901850346
				],
				[
					374.70947040168096,
					-0.3317204901850346
				],
				[
					379.43761505605585,
					-0.7068761461382564
				],
				[
					385.29724975869857,
					-1.0603009525102607
				],
				[
					388.54642303866075,
					-1.0603009525102607
				],
				[
					390.52135661132473,
					-1.0603009525102607
				],
				[
					391.510415401289,
					-1.0603009525102607
				],
				[
					391.6839437972105,
					-1.0603009525102607
				],
				[
					391.6839437972105,
					-1.0603009525102607
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "text",
			"version": 141,
			"versionNonce": 1055704242,
			"isDeleted": false,
			"id": "SGHShFMe",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 250.31395312272713,
			"y": -3917.712594671579,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 253.5519256591797,
			"height": 40,
			"seed": 1161637034,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710299670717,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 1,
			"text": "무엇보다 연산이 몹시 힘들어짐\n-> 아하 컴퓨터는 연산하는 기계구나~",
			"rawText": "무엇보다 연산이 몹시 힘들어짐\n-> 아하 컴퓨터는 연산하는 기계구나~",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "무엇보다 연산이 몹시 힘들어짐\n-> 아하 컴퓨터는 연산하는 기계구나~",
			"lineHeight": 1.25,
			"baseline": 34
		},
		{
			"id": "Er39qOlA",
			"type": "text",
			"x": -743.6660533906029,
			"y": -3656.824669787144,
			"width": 150.2559051513672,
			"height": 120,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 892124398,
			"version": 186,
			"versionNonce": 112498542,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710299670717,
			"link": null,
			"locked": false,
			"text": "- Two's complement\n\n- 1으로 시작하면 음수\n- 11...11111은 -1\n- MSB = sign bit\n",
			"rawText": "- Two's complement\n\n- 1으로 시작하면 음수\n- 11...11111은 -1\n- MSB = sign bit\n",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 114,
			"containerId": null,
			"originalText": "- Two's complement\n\n- 1으로 시작하면 음수\n- 11...11111은 -1\n- MSB = sign bit\n",
			"lineHeight": 1.25
		},
		{
			"id": "GQRat7-smmXtSPyCKOlHt",
			"type": "freedraw",
			"x": 168.9412171419603,
			"y": -3462.377516574363,
			"width": 68.87137178381573,
			"height": 34.37425512328218,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1216659506,
			"version": 98,
			"versionNonce": 778595310,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710299673694,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.6227228600407102,
					0.30593831802571003
				],
				[
					-2.6220746492675744,
					1.0516162172489203
				],
				[
					-3.7774780098566225,
					1.857369107098748
				],
				[
					-6.645369235557666,
					2.7122572616563048
				],
				[
					-8.644767775749983,
					3.7064632933097528
				],
				[
					-9.775533377537101,
					4.2663996067262815
				],
				[
					-12.34029134314028,
					5.63484711695537
				],
				[
					-13.905373414129997,
					6.0691168351927445
				],
				[
					-15.904725203356804,
					6.5662198510194685
				],
				[
					-17.494398282183,
					6.719189010032551
				],
				[
					-19.059433602207264,
					7.3419118700730905
				],
				[
					-22.058508037012984,
					8.336164652692332
				],
				[
					-23.189273638800103,
					8.52185948753322
				],
				[
					-25.188625428026967,
					9.278477112675773
				],
				[
					-26.499709503626207,
					9.527005245106466
				],
				[
					-28.630151000026785,
					9.775580128502497
				],
				[
					-31.063819258456135,
					9.775580128502497
				],
				[
					-33.49744076592009,
					9.775580128502497
				],
				[
					-35.49679255514695,
					9.775580128502497
				],
				[
					-38.061550520750075,
					9.775580128502497
				],
				[
					-42.797750579469664,
					9.775580128502497
				],
				[
					-44.23174294328567,
					9.775580128502497
				],
				[
					-46.231094732512474,
					9.775580128502497
				],
				[
					-52.2701506969089,
					9.775580128502497
				],
				[
					-54.13836602799648,
					9.464218698482
				],
				[
					-60.00537843946876,
					9.212932259088575
				],
				[
					-60.62810129950947,
					9.057251544078554
				],
				[
					-61.50486890590611,
					9.057251544078554
				],
				[
					-63.12731441152573,
					8.494556923699292
				],
				[
					-64.00408201792237,
					8.338876208689271
				],
				[
					-64.47112416295295,
					8.027514778668774
				],
				[
					-64.93821305894892,
					7.5604258826729165
				],
				[
					-66.65079442599188,
					6.511614723352068
				],
				[
					-67.18338142460925,
					5.790527831965392
				],
				[
					-67.65047032060528,
					5.323438935969534
				],
				[
					-68.15028489242923,
					4.446671329572837
				],
				[
					-68.87137178381573,
					3.75835686497976
				],
				[
					-68.87137178381573,
					1.3247353575156922
				],
				[
					-68.87137178381573,
					-0.5435267245370596
				],
				[
					-68.58731291762899,
					-2.9771482320011273
				],
				[
					-68.40157133182254,
					-4.97654677219316
				],
				[
					-67.84439332536869,
					-6.287584096827231
				],
				[
					-67.47019859775867,
					-8.164027597837503
				],
				[
					-67.28445701195221,
					-9.294839950589903
				],
				[
					-66.69445982773948,
					-11.916937975340261
				],
				[
					-66.17005424807905,
					-13.359088382630489
				],
				[
					-65.83134350325957,
					-14.235855989027186
				],
				[
					-65.3697712211889,
					-14.702921509540374
				],
				[
					-64.59679075813233,
					-16.882545021613623
				],
				[
					-63.21198040998922,
					-19.037600901333462
				],
				[
					-62.68481652336618,
					-19.91436850773016
				],
				[
					-61.96919949493946,
					-20.446978881830546
				],
				[
					-60.67181345222252,
					-21.905538878000243
				],
				[
					-60.363163578199305,
					-22.216923683502955
				],
				[
					-59.59294142210541,
					-22.68396582853393
				],
				[
					-59.131322389069226,
					-22.99535063403664
				],
				[
					-58.41570536064256,
					-23.37228029312655
				],
				[
					-57.26581861397881,
					-23.872118240433338
				],
				[
					-54.27497234909555,
					-24.34738855538626
				],
				[
					-52.281043671863074,
					-24.34738855538626
				],
				[
					-50.72143146383314,
					-24.598674994779685
				],
				[
					-48.29327981932903,
					-24.598674994779685
				],
				[
					-46.299351142096555,
					-24.598674994779685
				],
				[
					-43.308504877213295,
					-24.598674994779685
				],
				[
					-40.446036763506584,
					-24.598674994779685
				],
				[
					-38.01788511900247,
					-24.598674994779685
				],
				[
					-35.58968672353291,
					-24.598674994779685
				],
				[
					-30.86166808377027,
					-24.598674994779685
				],
				[
					-27.130613782623925,
					-24.29002512075658
				],
				[
					-23.399606232442977,
					-23.672725372710374
				],
				[
					-20.102821649533723,
					-23.080016632500246
				],
				[
					-17.240353535827012,
					-22.52281525056378
				],
				[
					-14.249507270943809,
					-22.27426374265042
				],
				[
					-13.686859401530114,
					-22.088545532326407
				],
				[
					-12.815561658093259,
					-21.749858162989767
				],
				[
					-11.75852232884995,
					-21.00144533228695
				],
				[
					-10.734255426400125,
					-20.66275796295031
				],
				[
					-10.116955678353747,
					-20.201162305396792
				],
				[
					-9.811064111293206,
					-19.739566647843276
				],
				[
					-9.34944507825702,
					-19.12226689979707
				],
				[
					-8.625646630873348,
					-17.38240634440308
				],
				[
					-7.869029005730795,
					-15.079851168630285
				],
				[
					-7.311850999276942,
					-13.77426033147367
				],
				[
					-7.126109413470488,
					-12.902962588036644
				],
				[
					-6.8775345300743425,
					-11.343350380006996
				],
				[
					-6.691839695233398,
					-9.475111673436459
				],
				[
					-6.538870536220372,
					-8.759494645009909
				],
				[
					-6.164675808610298,
					-7.888150150607544
				],
				[
					-5.79048108100028,
					-6.762854411780154
				],
				[
					-5.79048108100028,
					-6.301235378743968
				],
				[
					-5.79048108100028,
					-5.022970480903496
				],
				[
					-5.6375119219872545,
					-4.714320606880392
				],
				[
					-5.6375119219872545,
					-4.097020858834185
				],
				[
					-5.484542762974286,
					-3.6354485767633378
				],
				[
					-5.484542762974286,
					-3.326798702740234
				],
				[
					-5.484542762974286,
					-3.326798702740234
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				-5.484542762974286,
				-3.326798702740234
			]
		},
		{
			"id": "UE31vryE",
			"type": "text",
			"x": 154.53743168497036,
			"y": -3418.3696640047065,
			"width": 181.7919464111328,
			"height": 20,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 711769458,
			"version": 95,
			"versionNonce": 931421422,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710299686169,
			"link": null,
			"locked": false,
			"text": "MSB가 제일 큰 음수구나~",
			"rawText": "MSB가 제일 큰 음수구나~",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 14,
			"containerId": null,
			"originalText": "MSB가 제일 큰 음수구나~",
			"lineHeight": 1.25
		},
		{
			"id": "X8brBnxo",
			"type": "text",
			"x": -881.6440478164715,
			"y": -3276.280261110382,
			"width": 289.15185546875,
			"height": 80,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1307090034,
			"version": 241,
			"versionNonce": 1772714994,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710300128956,
			"link": null,
			"locked": false,
			"text": "- One's complement\n\n- 2^n - x -1\n- 물론 two's complement가 더 자주 쓰임",
			"rawText": "- One's complement\n\n- 2^n - x -1\n- 물론 two's complement가 더 자주 쓰임",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "right",
			"verticalAlign": "top",
			"baseline": 74,
			"containerId": null,
			"originalText": "- One's complement\n\n- 2^n - x -1\n- 물론 two's complement가 더 자주 쓰임",
			"lineHeight": 1.25
		},
		{
			"id": "Khf_nRHOaMrucf7pS9XjX",
			"type": "freedraw",
			"x": -419.2393648055821,
			"y": -2935.4352529031094,
			"width": 343.66316809345665,
			"height": 2.616651537272901,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1275091762,
			"version": 182,
			"versionNonce": 717884910,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710299747010,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.152922408047516,
					0
				],
				[
					0.614541441083702,
					0.30589156706082576
				],
				[
					1.076160474119888,
					0.7675106000970118
				],
				[
					1.5377327561906213,
					0.9204797591100942
				],
				[
					1.6907019152036469,
					1.0734021671573828
				],
				[
					2.714968817653471,
					1.2263713261704652
				],
				[
					3.1765410997242043,
					1.3793404851835476
				],
				[
					3.793840847770582,
					1.3793404851835476
				],
				[
					5.787722774037604,
					1.3793404851835476
				],
				[
					7.347334982067537,
					1.5650820709897744
				],
				[
					8.344299320683774,
					1.5650820709897744
				],
				[
					10.212561402736867,
					1.5650820709897744
				],
				[
					12.952121228226815,
					1.5650820709897744
				],
				[
					13.260771102249976,
					1.5650820709897744
				],
				[
					14.132068845686831,
					1.5650820709897744
				],
				[
					15.003366589123686,
					1.5650820709897744
				],
				[
					15.71898361755035,
					1.5650820709897744
				],
				[
					16.336283365596728,
					1.5650820709897744
				],
				[
					17.262232987666266,
					1.5650820709897744
				],
				[
					19.384493065109837,
					1.5650820709897744
				],
				[
					20.81572712196322,
					1.5650820709897744
				],
				[
					22.375339329993096,
					1.5650820709897744
				],
				[
					25.800455313113446,
					1.5650820709897744
				],
				[
					28.228653708583067,
					1.5650820709897744
				],
				[
					29.788265916612943,
					1.5650820709897744
				],
				[
					33.08776205551942,
					1.5650820709897744
				],
				[
					35.08164398178644,
					1.5650820709897744
				],
				[
					36.38725819442584,
					1.5650820709897744
				],
				[
					39.25243786412972,
					1.5650820709897744
				],
				[
					40.3777803539225,
					1.376582178220815
				],
				[
					41.683347815596505,
					1.376582178220815
				],
				[
					43.67727649282898,
					1.0898117560368519
				],
				[
					45.111222105679474,
					1.0898117560368519
				],
				[
					45.41987197970269,
					1.0898117560368519
				],
				[
					46.85110603655602,
					1.0898117560368519
				],
				[
					49.10174426517614,
					1.0898117560368519
				],
				[
					52.52686024829649,
					1.0898117560368519
				],
				[
					53.089554868675634,
					1.0898117560368519
				],
				[
					55.517706513179746,
					1.0898117560368519
				],
				[
					56.64304900297259,
					1.0898117560368519
				],
				[
					58.63693092923961,
					1.0898117560368519
				],
				[
					60.759237757648634,
					1.0898117560368519
				],
				[
					63.621705871355346,
					1.0898117560368519
				],
				[
					64.18435374076898,
					1.0898117560368519
				],
				[
					66.92120201026177,
					1.0898117560368519
				],
				[
					68.10114962772178,
					1.0898117560368519
				],
				[
					69.40671708939578,
					1.0898117560368519
				],
				[
					70.96632929742566,
					1.0898117560368519
				],
				[
					72.52594150545559,
					1.0898117560368519
				],
				[
					74.39420358750868,
					1.0898117560368519
				],
				[
					75.26550133094554,
					1.0898117560368519
				],
				[
					75.72712036398173,
					1.0898117560368519
				],
				[
					77.03268782565567,
					1.0898117560368519
				],
				[
					77.64998757370205,
					1.0898117560368519
				],
				[
					79.64386949996907,
					1.0898117560368519
				],
				[
					81.7661763283781,
					1.0898117560368519
				],
				[
					83.07174379005204,
					1.0898117560368519
				],
				[
					84.19708627984488,
					1.0898117560368519
				],
				[
					84.65594700591839,
					1.0898117560368519
				],
				[
					85.27324675396477,
					1.0898117560368519
				],
				[
					85.57913832102531,
					1.0898117560368519
				],
				[
					86.29475534945198,
					1.0898117560368519
				],
				[
					87.16605309288883,
					1.0898117560368519
				],
				[
					88.47166730552829,
					1.0898117560368519
				],
				[
					90.59392738297186,
					1.0898117560368519
				],
				[
					92.58780930923888,
					1.0898117560368519
				],
				[
					95.88459389214813,
					1.0898117560368519
				],
				[
					99.30970987526848,
					1.0898117560368519
				],
				[
					101.7379082707381,
					1.0898117560368519
				],
				[
					104.60037638444476,
					1.0898117560368519
				],
				[
					106.03161044129814,
					1.0898117560368519
				],
				[
					111.32227695047442,
					1.0898117560368519
				],
				[
					118.17255566768057,
					1.0898117560368519
				],
				[
					121.03502378138728,
					1.0898117560368519
				],
				[
					122.46625783824061,
					1.0898117560368519
				],
				[
					126.75996000880065,
					1.0898117560368519
				],
				[
					129.18811165330476,
					1.0898117560368519
				],
				[
					131.18204033053723,
					0.8385253166434268
				],
				[
					133.17592225680426,
					0.8385253166434268
				],
				[
					135.16980418307128,
					0.3359524378570313
				],
				[
					138.59496691715714,
					0.3359524378570313
				],
				[
					140.154579125187,
					0.3359524378570313
				],
				[
					141.71419133321695,
					0.08466599846360623
				],
				[
					143.27380354124682,
					0.08466599846360623
				],
				[
					145.83033333692754,
					0.08466599846360623
				],
				[
					147.82426201416,
					0.08466599846360623
				],
				[
					149.81814394042703,
					0.08466599846360623
				],
				[
					152.2463423358966,
					0.08466599846360623
				],
				[
					154.29482938983085,
					0.08466599846360623
				],
				[
					156.72302778530042,
					0.08466599846360623
				],
				[
					158.71690971156744,
					0.08466599846360623
				],
				[
					161.5794245762396,
					0.08466599846360623
				],
				[
					163.57330650250663,
					0.08466599846360623
				],
				[
					167.43273895482957,
					0.08466599846360623
				],
				[
					168.99235116285945,
					0.08466599846360623
				],
				[
					171.42050280736362,
					0.08466599846360623
				],
				[
					174.28297092107027,
					0.08466599846360623
				],
				[
					176.27689959830275,
					0.08466599846360623
				],
				[
					180.13628529966024,
					0.08466599846360623
				],
				[
					182.56448369512987,
					0.08466599846360623
				],
				[
					185.42695180883652,
					0.08466599846360623
				],
				[
					188.28941992254317,
					0.08466599846360623
				],
				[
					191.71458265662898,
					0.08466599846360623
				],
				[
					195.01132048857278,
					0.08466599846360623
				],
				[
					197.18547413768647,
					0.08466599846360623
				],
				[
					198.6167081945398,
					0.08466599846360623
				],
				[
					200.2009114104062,
					0.08466599846360623
				],
				[
					205.49157791958248,
					-0.20215117468569588
				],
				[
					207.4854598458495,
					-0.20215117468569588
				],
				[
					209.913658241319,
					-0.453437614079121
				],
				[
					212.77612635502578,
					-0.7647990440991634
				],
				[
					216.20124233814613,
					-1.0515694662831265
				],
				[
					218.62944073361564,
					-1.0515694662831265
				],
				[
					220.62332265988266,
					-1.0515694662831265
				],
				[
					222.18293486791265,
					-1.0515694662831265
				],
				[
					223.74254707594253,
					-1.0515694662831265
				],
				[
					225.86485390435155,
					-1.0515694662831265
				],
				[
					227.42446611238142,
					-1.0515694662831265
				],
				[
					228.42138370003227,
					-1.0515694662831265
				],
				[
					231.41222996491547,
					-1.0515694662831265
				],
				[
					234.14903148344285,
					-1.0515694662831265
				],
				[
					235.70864369147273,
					-1.0515694662831265
				],
				[
					237.7025723687052,
					-1.0515694662831265
				],
				[
					239.69650104593768,
					-1.0515694662831265
				],
				[
					245.54981542452765,
					-1.0515694662831265
				],
				[
					247.54365059982922,
					-1.0515694662831265
				],
				[
					250.40611871353588,
					-1.0515694662831265
				],
				[
					252.40004739076835,
					-1.0515694662831265
				],
				[
					255.39089365565155,
					-1.0515694662831265
				],
				[
					256.3878112433024,
					-1.0515694662831265
				],
				[
					258.6903897945581,
					-1.0515694662831265
				],
				[
					259.81568553338536,
					-1.0515694662831265
				],
				[
					260.6870300277877,
					-1.0515694662831265
				],
				[
					264.6747938803218,
					-1.0515694662831265
				],
				[
					265.2920936283681,
					-0.8986470582358379
				],
				[
					267.72024527287226,
					-0.8986470582358379
				],
				[
					271.17271057079165,
					-0.6145881920488137
				],
				[
					273.1666392480241,
					-0.6145881920488137
				],
				[
					274.2919349868515,
					-0.42884660624258686
				],
				[
					275.16327948125377,
					-0.42884660624258686
				],
				[
					277.03154156330686,
					-0.42884660624258686
				],
				[
					277.49316059634305,
					-0.42884660624258686
				],
				[
					278.798728058017,
					0.06825640958413715
				],
				[
					280.79256323331856,
					0.31683129298016866
				],
				[
					282.35217544134844,
					0.31683129298016866
				],
				[
					285.2147370569861,
					0.31683129298016866
				],
				[
					288.2055833218694,
					0.31683129298016866
				],
				[
					291.0680514355761,
					0.31683129298016866
				],
				[
					293.06188661087765,
					0.31683129298016866
				],
				[
					295.4901317573127,
					0.6008901591671929
				],
				[
					298.6612497450426,
					0.6008901591671929
				],
				[
					300.2208619530725,
					0.6008901591671929
				],
				[
					301.34615769189975,
					0.7866317449734197
				],
				[
					302.90576989992974,
					0.7866317449734197
				],
				[
					305.46229969561034,
					0.7866317449734197
				],
				[
					306.4592172832612,
					0.7866317449734197
				],
				[
					308.7617958345169,
					0.7866317449734197
				],
				[
					310.0673632961908,
					0.7866317449734197
				],
				[
					310.63005791656997,
					0.7866317449734197
				],
				[
					314.1835988018323,
					0.7866317449734197
				],
				[
					316.6117504463364,
					0.7866317449734197
				],
				[
					319.03990209084054,
					0.7866317449734197
				],
				[
					320.16529133159884,
					0.7866317449734197
				],
				[
					322.4677763809235,
					0.7866317449734197
				],
				[
					324.461705058156,
					1.0351598774041122
				],
				[
					326.021317266186,
					1.0351598774041122
				],
				[
					328.88378537989263,
					1.0351598774041122
				],
				[
					331.3119370243968,
					1.0351598774041122
				],
				[
					332.8715492324267,
					1.0351598774041122
				],
				[
					334.43116144045655,
					1.0351598774041122
				],
				[
					336.5534682688656,
					1.0351598774041122
				],
				[
					338.11308047689556,
					1.0351598774041122
				],
				[
					341.10392674177876,
					1.0351598774041122
				],
				[
					341.9751777342501,
					1.0351598774041122
				],
				[
					342.28111605227616,
					1.0351598774041122
				],
				[
					342.5870543703022,
					1.0351598774041122
				],
				[
					343.0486734033384,
					1.0351598774041122
				],
				[
					343.5101989344437,
					1.0351598774041122
				],
				[
					343.66316809345665,
					1.0351598774041122
				],
				[
					343.66316809345665,
					1.0351598774041122
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				343.66316809345665,
				1.0351598774041122
			]
		},
		{
			"id": "W77egtbv",
			"type": "text",
			"x": 599.7270066813859,
			"y": -3304.8169919936595,
			"width": 287.391845703125,
			"height": 280,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 673626994,
			"version": 372,
			"versionNonce": 105859694,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710300105073,
			"link": null,
			"locked": false,
			"text": "- Biased notation\n\n- 000...000 = most negative number\n- 111...111 = most positive number\n- 0111...111 = 0\n- negative sign 변환은 flip -> 1 빼기\n\n- 예를 들어, bias = 3일 때...\n- 000 -> -3...\n- 011 -> 0...\n\n- two's complement가 주로 사용\n- 이거는 float가 부분적으로 사용\n",
			"rawText": "- Biased notation\n\n- 000...000 = most negative number\n- 111...111 = most positive number\n- 0111...111 = 0\n- negative sign 변환은 flip -> 1 빼기\n\n- 예를 들어, bias = 3일 때...\n- 000 -> -3...\n- 011 -> 0...\n\n- two's complement가 주로 사용\n- 이거는 float가 부분적으로 사용\n",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 274,
			"containerId": null,
			"originalText": "- Biased notation\n\n- 000...000 = most negative number\n- 111...111 = most positive number\n- 0111...111 = 0\n- negative sign 변환은 flip -> 1 빼기\n\n- 예를 들어, bias = 3일 때...\n- 000 -> -3...\n- 011 -> 0...\n\n- two's complement가 주로 사용\n- 이거는 float가 부분적으로 사용\n",
			"lineHeight": 1.25
		},
		{
			"id": "MXOBIaej",
			"type": "text",
			"x": -1007.9092454582092,
			"y": -2862.941312433515,
			"width": 411.11981201171875,
			"height": 220,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 667141298,
			"version": 672,
			"versionNonce": 1848263662,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710300849602,
			"link": null,
			"locked": false,
			"text": "RISC-V에서 sign/unsigned 를 저장하는 방법\n\n1. 만약 int x = 2;라면 4bytes 로 저장을 할 것임\n2. register의 용량은 64bit (8B) 이므로 절반이 남을 것임\n3. 그럼 남은 절반을 어떻게 채울 것인가?\n\n- unsigned의 경우 무조건 0으로 채움 = zero extension\n- signed의 경우 sign bit로 채움 = sign extension\n\n그래서 이를 구분하기 위해\nldu, lwu, lhu, lbu를 쓴다",
			"rawText": "RISC-V에서 sign/unsigned 를 저장하는 방법\n\n1. 만약 int x = 2;라면 4bytes 로 저장을 할 것임\n2. register의 용량은 64bit (8B) 이므로 절반이 남을 것임\n3. 그럼 남은 절반을 어떻게 채울 것인가?\n\n- unsigned의 경우 무조건 0으로 채움 = zero extension\n- signed의 경우 sign bit로 채움 = sign extension\n\n그래서 이를 구분하기 위해\nldu, lwu, lhu, lbu를 쓴다",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "right",
			"verticalAlign": "top",
			"baseline": 214,
			"containerId": null,
			"originalText": "RISC-V에서 sign/unsigned 를 저장하는 방법\n\n1. 만약 int x = 2;라면 4bytes 로 저장을 할 것임\n2. register의 용량은 64bit (8B) 이므로 절반이 남을 것임\n3. 그럼 남은 절반을 어떻게 채울 것인가?\n\n- unsigned의 경우 무조건 0으로 채움 = zero extension\n- signed의 경우 sign bit로 채움 = sign extension\n\n그래서 이를 구분하기 위해\nldu, lwu, lhu, lbu를 쓴다",
			"lineHeight": 1.25
		},
		{
			"id": "NvxFHYHu",
			"type": "text",
			"x": 593.9830345130898,
			"y": -2862.011213663261,
			"width": 27.67999267578125,
			"height": 20,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 71381234,
			"version": 76,
			"versionNonce": 1242346290,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710300882220,
			"link": null,
			"locked": false,
			"text": "예시",
			"rawText": "예시",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 14,
			"containerId": null,
			"originalText": "예시",
			"lineHeight": 1.25
		},
		{
			"id": "njt4Npv4",
			"type": "text",
			"x": -937.772064296926,
			"y": -2396.857714135718,
			"width": 347.26385498046875,
			"height": 180,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1764386930,
			"version": 428,
			"versionNonce": 1166765102,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710301090657,
			"link": null,
			"locked": false,
			"text": "sign/unsigned를 어떻게 구분할 것이냐??\n\narray, memory address를 표현할 때는 모두 양수\n-> int 쓰면 바보\n-> unsigned int는 더 좋음\n-> size_t가 제일 좋음\n\n- pointer는 언제나 64-bit\n",
			"rawText": "sign/unsigned를 어떻게 구분할 것이냐??\n\narray, memory address를 표현할 때는 모두 양수\n-> int 쓰면 바보\n-> unsigned int는 더 좋음\n-> size_t가 제일 좋음\n\n- pointer는 언제나 64-bit\n",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "right",
			"verticalAlign": "top",
			"baseline": 174,
			"containerId": null,
			"originalText": "sign/unsigned를 어떻게 구분할 것이냐??\n\narray, memory address를 표현할 때는 모두 양수\n-> int 쓰면 바보\n-> unsigned int는 더 좋음\n-> size_t가 제일 좋음\n\n- pointer는 언제나 64-bit\n",
			"lineHeight": 1.25
		},
		{
			"id": "rpjPEYk5",
			"type": "text",
			"x": -942.0890667560882,
			"y": -1937.4779939067646,
			"width": 346.15985107421875,
			"height": 100,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 274818674,
			"version": 335,
			"versionNonce": 1357198642,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710301220276,
			"link": null,
			"locked": false,
			"text": "- 컴퓨터는 operator, oparand를 어떻게 구분할까\n\n1. 각 레지스터(x0-x31) - 5bits 사용해서 specify\n2. operator들은 mapping해서 인코딩\n3. 여러개를 붙이면 instruction!",
			"rawText": "- 컴퓨터는 operator, oparand를 어떻게 구분할까\n\n1. 각 레지스터(x0-x31) - 5bits 사용해서 specify\n2. operator들은 mapping해서 인코딩\n3. 여러개를 붙이면 instruction!",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "right",
			"verticalAlign": "top",
			"baseline": 94,
			"containerId": null,
			"originalText": "- 컴퓨터는 operator, oparand를 어떻게 구분할까\n\n1. 각 레지스터(x0-x31) - 5bits 사용해서 specify\n2. operator들은 mapping해서 인코딩\n3. 여러개를 붙이면 instruction!",
			"lineHeight": 1.25
		},
		{
			"id": "uxXYNNGq",
			"type": "text",
			"x": 610.4015611248818,
			"y": -1944.3003155466197,
			"width": 323.8718566894531,
			"height": 140,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 545662638,
			"version": 205,
			"versionNonce": 1885962674,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710301304844,
			"link": null,
			"locked": false,
			"text": "- RISC는 고정된 instruction length를 가진다\n    - 32bit, 6segments (보통)\n\n- 오른쪽부터 읽어요\n- operator (7bits)\n- operand (5bits)\n- 그 외 등등",
			"rawText": "- RISC는 고정된 instruction length를 가진다\n    - 32bit, 6segments (보통)\n\n- 오른쪽부터 읽어요\n- operator (7bits)\n- operand (5bits)\n- 그 외 등등",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 134,
			"containerId": null,
			"originalText": "- RISC는 고정된 instruction length를 가진다\n    - 32bit, 6segments (보통)\n\n- 오른쪽부터 읽어요\n- operator (7bits)\n- operand (5bits)\n- 그 외 등등",
			"lineHeight": 1.25
		},
		{
			"id": "yWInQKAg",
			"type": "text",
			"x": -989.243202360267,
			"y": -1507.4134548871025,
			"width": 391.7118225097656,
			"height": 160,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1847314162,
			"version": 222,
			"versionNonce": 650887982,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710301376637,
			"link": null,
			"locked": false,
			"text": "R-Type은 두 개의 source register를 가진 instruction\n\n- opcode\n- rd\n- funct3\n- rs1\n- rs2\n- funct7",
			"rawText": "R-Type은 두 개의 source register를 가진 instruction\n\n- opcode\n- rd\n- funct3\n- rs1\n- rs2\n- funct7",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "right",
			"verticalAlign": "top",
			"baseline": 154,
			"containerId": null,
			"originalText": "R-Type은 두 개의 source register를 가진 instruction\n\n- opcode\n- rd\n- funct3\n- rs1\n- rs2\n- funct7",
			"lineHeight": 1.25
		},
		{
			"id": "F6KJKQB3",
			"type": "text",
			"x": 596.5802988481751,
			"y": -1511.5847396545835,
			"width": 422.7358703613281,
			"height": 180,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 928638386,
			"version": 311,
			"versionNonce": 1304136750,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710301669585,
			"link": null,
			"locked": false,
			"text": "I-Type - constant, one resource register를 가지는\n\n- opcode\n- rd \n- funct3\n- rs1\n- immediate\n    - 원래는 5bits였지만, 이러면 표현할 수 있는 수가 적어짐\n    - 위의 funct7과 rs2를 통합시켜 10bit로 사용",
			"rawText": "I-Type - constant, one resource register를 가지는\n\n- opcode\n- rd \n- funct3\n- rs1\n- immediate\n    - 원래는 5bits였지만, 이러면 표현할 수 있는 수가 적어짐\n    - 위의 funct7과 rs2를 통합시켜 10bit로 사용",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 174,
			"containerId": null,
			"originalText": "I-Type - constant, one resource register를 가지는\n\n- opcode\n- rd \n- funct3\n- rs1\n- immediate\n    - 원래는 5bits였지만, 이러면 표현할 수 있는 수가 적어짐\n    - 위의 funct7과 rs2를 통합시켜 10bit로 사용",
			"lineHeight": 1.25
		},
		{
			"id": "3pBll8lH",
			"type": "text",
			"x": 105.76448695993327,
			"y": -1219.195096863919,
			"width": 40.38397216796875,
			"height": 20,
			"angle": 0,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 715886450,
			"version": 82,
			"versionNonce": 169224050,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710301704790,
			"link": null,
			"locked": false,
			"text": " addi",
			"rawText": " addi",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 14,
			"containerId": null,
			"originalText": " addi",
			"lineHeight": 1.25
		},
		{
			"id": "psGjtKc3RrKvwbF4c7WTP",
			"type": "freedraw",
			"x": 114.85722248680258,
			"y": -1228.2686644949458,
			"width": 41.70251571143859,
			"height": 4.73620005871976,
			"angle": 0,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1185831598,
			"version": 68,
			"versionNonce": 1546205874,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710301694936,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.8712977434368554,
					0
				],
				[
					2.430909951466788,
					0
				],
				[
					4.8591083469363525,
					0
				],
				[
					9.587080235733481,
					-0.8849724008364319
				],
				[
					12.449548349440192,
					-1.4585599961696971
				],
				[
					15.312016463146904,
					-1.7453537938363297
				],
				[
					17.30594514037938,
					-1.9966402332297548
				],
				[
					19.73409678488349,
					-2.24792667262318
				],
				[
					23.159259518969293,
					-2.24792667262318
				],
				[
					24.718871726999225,
					-2.24792667262318
				],
				[
					25.84416746582656,
					-2.24792667262318
				],
				[
					27.40377967385649,
					-2.24792667262318
				],
				[
					28.02107942190281,
					-2.24792667262318
				],
				[
					28.791301577996762,
					-2.24792667262318
				],
				[
					29.50696535738888,
					-2.24792667262318
				],
				[
					30.63226109621621,
					-2.24792667262318
				],
				[
					32.626143022483234,
					-2.24792667262318
				],
				[
					33.93175723512269,
					-2.24792667262318
				],
				[
					34.08472639413566,
					-2.24792667262318
				],
				[
					33.929045679125466,
					-2.24792667262318
				],
				[
					32.617961603526226,
					-1.5978544977833735
				],
				[
					30.18434009606233,
					-1.3137956315965766
				],
				[
					28.619258025072554,
					-0.8795025378767605
				],
				[
					26.619906235845747,
					-0.8795025378767605
				],
				[
					19.71226408400969,
					0.10378714334001415
				],
				[
					15.975739919903504,
					0.10378714334001415
				],
				[
					12.23926250676277,
					0.10378714334001415
				],
				[
					9.371324530096274,
					0.10378714334001415
				],
				[
					5.503710658816317,
					0.10378714334001415
				],
				[
					4.192626583217077,
					0.10378714334001415
				],
				[
					2.4473195403462,
					0.10378714334001415
				],
				[
					1.8245499293400371,
					0.10378714334001415
				],
				[
					0.6937843275528621,
					0.10378714334001415
				],
				[
					-0.6172997480463778,
					0.10378714334001415
				],
				[
					-0.7729804630565695,
					0.10378714334001415
				],
				[
					-0.7729804630565695,
					0.25675630235309654
				],
				[
					0.09831728038028587,
					0.44247451267665383
				],
				[
					2.5265156758499074,
					0.9395775285036052
				],
				[
					5.517361940733167,
					0.9395775285036052
				],
				[
					9.6826859601166,
					0.9395775285036052
				],
				[
					15.58518235437947,
					0.9395775285036052
				],
				[
					20.619092561202592,
					0.9395775285036052
				],
				[
					22.918866054530156,
					0.9395775285036052
				],
				[
					27.521218099113412,
					0.9395775285036052
				],
				[
					27.67418725812638,
					1.0925466875164602
				],
				[
					25.240565750662483,
					1.625157061616619
				],
				[
					22.806897492233077,
					1.625157061616619
				],
				[
					20.373275984769123,
					1.625157061616619
				],
				[
					16.202435351460338,
					1.625157061616619
				],
				[
					10.294515845203193,
					1.625157061616619
				],
				[
					-0.08742430542611146,
					1.625157061616619
				],
				[
					-5.1267576242436235,
					1.625157061616619
				],
				[
					-7.150700421306908,
					1.625157061616619
				],
				[
					-7.617789317302936,
					1.625157061616619
				],
				[
					-6.467902570639126,
					2.0266777285430635
				],
				[
					-2.608470118316177,
					2.0266777285430635
				],
				[
					0.2539979953904776,
					2.0266777285430635
				],
				[
					4.853638483976567,
					2.0266777285430635
				],
				[
					11.19040459647647,
					2.0266777285430635
				],
				[
					17.527170708976428,
					2.0266777285430635
				],
				[
					22.714050074812576,
					2.0266777285430635
				],
				[
					23.022699948835736,
					2.0266777285430635
				],
				[
					23.17562235688331,
					2.179623512073249
				],
				[
					23.792922104929687,
					2.48827338609658
				],
				[
					24.101571978952848,
					2.48827338609658
				],
				[
					24.101571978952848,
					2.48827338609658
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				24.101571978952848,
				2.48827338609658
			]
		},
		{
			"id": "DniIqO8YyQMrJJfjbsDwm",
			"type": "freedraw",
			"x": 100.40855610296398,
			"y": -3454.459258801994,
			"width": 86.07899964381477,
			"height": 41.81993076121262,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 885109426,
			"version": 132,
			"versionNonce": 1578458738,
			"isDeleted": true,
			"boundElements": null,
			"updated": 1710299670717,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.15292240804757284,
					-0.002758306962732604
				],
				[
					0.30589156706054155,
					0.15021085205034979
				],
				[
					1.1744777545002307,
					0.48892159686965897
				],
				[
					2.045775497937086,
					0.8275855907236291
				],
				[
					4.348307298227269,
					1.7371256239139257
				],
				[
					6.088191229103813,
					2.021184490100495
				],
				[
					7.647803437133746,
					2.2697593734965267
				],
				[
					10.204379983779859,
					2.553818239683551
				],
				[
					11.763992191809791,
					2.7395598254897777
				],
				[
					13.757874118076813,
					2.98808795792047
				],
				[
					15.317486326106689,
					2.98808795792047
				],
				[
					17.74568472157631,
					3.2366628413165017
				],
				[
					20.73653098645957,
					3.485190973747194
				],
				[
					23.164682630963682,
					3.485190973747194
				],
				[
					24.035980374400538,
					3.859432452322835
				],
				[
					26.029909051633012,
					3.859432452322835
				],
				[
					28.332440851923195,
					4.107960584753528
				],
				[
					30.326322778190217,
					4.107960584753528
				],
				[
					32.75452117365984,
					4.107960584753528
				],
				[
					35.61698928736649,
					4.107960584753528
				],
				[
					38.045187682836115,
					4.107960584753528
				],
				[
					40.601717478516775,
					4.107960584753528
				],
				[
					42.59564615574925,
					4.107960584753528
				],
				[
					45.45811426945596,
					4.107960584753528
				],
				[
					47.451996195722984,
					4.107960584753528
				],
				[
					49.88019459119255,
					4.107960584753528
				],
				[
					55.476752667429366,
					4.107960584753528
				],
				[
					58.33922078113608,
					4.107960584753528
				],
				[
					60.3331027074031,
					3.8566741453601026
				],
				[
					61.6387169200425,
					3.6053877059666775
				],
				[
					62.100335953078684,
					3.294026275946635
				],
				[
					62.87055810917258,
					2.6712566649403016
				],
				[
					63.487857857218955,
					2.204214519909783
				],
				[
					64.79342531889296,
					1.5486724821103053
				],
				[
					66.99492828280563,
					-0.661011900759604
				],
				[
					68.44799504053282,
					-1.8327780992626685
				],
				[
					69.31933953493512,
					-2.5210458128904065
				],
				[
					70.3299084045027,
					-3.823901718566958
				],
				[
					72.03701990858582,
					-5.061212770656766
				],
				[
					73.77961539545953,
					-7.811712322066342
				],
				[
					74.55806572147588,
					-10.433833722299369
				],
				[
					74.9322604490859,
					-11.154920613686045
				],
				[
					75.11800203489236,
					-12.87568339968584
				],
				[
					75.11800203489236,
					-14.186720724319457
				],
				[
					75.11800203489236,
					-16.06316422532973
				],
				[
					75.11800203489236,
					-16.374525655350226
				],
				[
					75.11800203489236,
					-17.68560973094918
				],
				[
					74.92954889308874,
					-20.561729126573027
				],
				[
					74.74109575128512,
					-21.127135302949227
				],
				[
					74.45427857813576,
					-22.872465721302888
				],
				[
					74.01453899693882,
					-24.437547792292662
				],
				[
					74.01453899693882,
					-24.748909222312705
				],
				[
					73.85885828192863,
					-26.215650637439467
				],
				[
					73.5474501009428,
					-26.527035442942633
				],
				[
					73.04763552911885,
					-27.526711337556208
				],
				[
					72.51500177953596,
					-28.24779822894243
				],
				[
					71.73659820448506,
					-28.870544464466093
				],
				[
					71.42519002349923,
					-29.026225179476114
				],
				[
					70.95814787846871,
					-29.493290699989302
				],
				[
					70.64673969748287,
					-29.648994790482448
				],
				[
					69.86833612243197,
					-30.116060310995636
				],
				[
					68.99156851603533,
					-30.460194167809277
				],
				[
					68.5244796200393,
					-30.615898258302423
				],
				[
					68.21311819001892,
					-30.771578973312444
				],
				[
					66.08262994265289,
					-30.960032115116064
				],
				[
					64.89450090623586,
					-31.30418934741283
				],
				[
					62.460879398771965,
					-32.238320388439206
				],
				[
					61.99379050277594,
					-32.238320388439206
				],
				[
					61.11702289637924,
					-32.238320388439206
				],
				[
					59.928893859962216,
					-32.58247762073552
				],
				[
					58.3638117889725,
					-32.58247762073552
				],
				[
					55.495873812306,
					-33.14512549014944
				],
				[
					52.19366611740236,
					-33.74330409331924
				],
				[
					50.19431432817555,
					-34.245876972105634
				],
				[
					45.45811426945596,
					-34.84405557527543
				],
				[
					42.155859823586866,
					-35.15541700529593
				],
				[
					38.41938241044613,
					-35.4668018107991
				],
				[
					35.11712796457704,
					-35.77816324081914
				],
				[
					32.24923673887599,
					-36.35175083615286
				],
				[
					27.94730639839355,
					-37.21213222915276
				],
				[
					24.210828985252817,
					-37.52351703465547
				],
				[
					21.77716072682341,
					-37.52351703465547
				],
				[
					20.212078655833693,
					-37.71197017645909
				],
				[
					18.769904873060682,
					-37.71197017645909
				],
				[
					17.458867548426895,
					-37.71197017645909
				],
				[
					15.459515759200087,
					-37.71197017645909
				],
				[
					13.714161965363758,
					-37.71197017645909
				],
				[
					11.14940399976058,
					-37.71197017645909
				],
				[
					9.150052210533772,
					-37.71197017645909
				],
				[
					7.584970139544055,
					-37.71197017645909
				],
				[
					5.151348632080101,
					-37.71197017645909
				],
				[
					3.1519968428532934,
					-37.71197017645909
				],
				[
					1.2755065908777397,
					-37.71197017645909
				],
				[
					0.8084644458471644,
					-37.71197017645909
				],
				[
					0.24305826947085052,
					-37.52625196613553
				],
				[
					-0.508042741746408,
					-36.777862510915384
				],
				[
					-1.6962185291288847,
					-36.13052526755564
				],
				[
					-2.843393719795529,
					-35.27287880603535
				],
				[
					-3.905856161033171,
					-34.062870317779016
				],
				[
					-4.471262337409485,
					-33.87715210745546
				],
				[
					-7.494881029086173,
					-29.84838765820541
				],
				[
					-8.355285797568854,
					-28.703924023536274
				],
				[
					-9.805640999298816,
					-25.71307775865307
				],
				[
					-10.461136286132955,
					-24.53313014119294
				],
				[
					-10.649636178902028,
					-23.97048227177902
				],
				[
					-10.960997608922412,
					-23.044556025192378
				],
				[
					-10.960997608922412,
					-22.735906151169274
				],
				[
					-10.960997608922412,
					-22.274310493615758
				],
				[
					-10.960997608922412,
					-20.66006978243604
				],
				[
					-10.469364456055416,
					-19.48012216497591
				],
				[
					-9.543414833985878,
					-18.554172542906144
				],
				[
					-7.784409758232698,
					-16.508373669486446
				],
				[
					-7.475759884209538,
					-16.199723795463342
				],
				[
					-6.331343000505569,
					-15.055306911759544
				],
				[
					-3.8430696144089325,
					-13.427391543179965
				],
				[
					-1.6688692143298454,
					-12.187368935092763
				],
				[
					-0.35783188969605817,
					-11.253237894066388
				],
				[
					1.2017803183338742,
					-10.381940150629362
				],
				[
					3.504312118624057,
					-9.316719402429044
				],
				[
					4.375609862060912,
					-8.633874800795638
				],
				[
					5.935222070090845,
					-7.9510301991626875
				],
				[
					6.396841103127031,
					-7.4894111661265015
				],
				[
					8.543692188407022,
					-6.743733266903291
				],
				[
					9.414989931843877,
					-6.2493885580393
				],
				[
					11.966096615530205,
					-4.5095046271626416
				],
				[
					12.274746489553422,
					-4.356535468150014
				],
				[
					14.607339160639867,
					-3.171117987730213
				],
				[
					15.0689114427106,
					-2.865226420669387
				],
				[
					15.0689114427106,
					-2.865226420669387
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				15.0689114427106,
				-2.865226420669387
			]
		},
		{
			"id": "eZ2z6HgD",
			"type": "text",
			"x": 638.4020485819866,
			"y": -1923.6191844542402,
			"width": 8,
			"height": 20,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1661012846,
			"version": 3,
			"versionNonce": 1011070450,
			"isDeleted": true,
			"boundElements": null,
			"updated": 1710301231287,
			"link": null,
			"locked": false,
			"text": "",
			"rawText": "",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 14,
			"containerId": null,
			"originalText": "",
			"lineHeight": 1.25
		}
	],
	"appState": {
		"theme": "light",
		"viewBackgroundColor": "#ffffff",
		"currentItemStrokeColor": "#e03131",
		"currentItemBackgroundColor": "transparent",
		"currentItemFillStyle": "solid",
		"currentItemStrokeWidth": 0.5,
		"currentItemStrokeStyle": "solid",
		"currentItemRoughness": 1,
		"currentItemOpacity": 100,
		"currentItemFontFamily": 1,
		"currentItemFontSize": 16,
		"currentItemTextAlign": "left",
		"currentItemStartArrowhead": "arrow",
		"currentItemEndArrowhead": "arrow",
		"scrollX": 197.29422872352674,
		"scrollY": 1333.3003652868035,
		"zoom": {
			"value": 1.3055378779523845
		},
		"currentItemRoundness": "round",
		"gridSize": null,
		"gridColor": {
			"Bold": "#C9C9C9FF",
			"Regular": "#EDEDEDFF"
		},
		"currentStrokeOptions": null,
		"previousGridSize": null,
		"frameRendering": {
			"enabled": true,
			"clip": true,
			"name": true,
			"outline": true
		}
	},
	"files": {}
}
```
%%