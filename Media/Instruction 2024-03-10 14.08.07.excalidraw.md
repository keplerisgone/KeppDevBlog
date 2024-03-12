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
			"version": 18,
			"versionNonce": 1489231606,
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
			"updated": 1710132693757,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 1831220074,
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
			"updated": 1710132693757,
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
			"version": 18,
			"versionNonce": 102273078,
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
			"updated": 1710132693757,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 1906325034,
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
			"updated": 1710132693757,
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
			"version": 18,
			"versionNonce": 541399414,
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
			"updated": 1710132693757,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 1162600682,
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
			"updated": 1710132693757,
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
			"version": 18,
			"versionNonce": 1854831286,
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
			"updated": 1710132693757,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 1672754090,
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
			"updated": 1710132693757,
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
			"version": 18,
			"versionNonce": 127513590,
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
			"updated": 1710132693757,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 520367722,
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
			"updated": 1710132693757,
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
			"version": 18,
			"versionNonce": 1701561654,
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
			"updated": 1710132693757,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 1275515178,
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
			"updated": 1710132693757,
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
			"version": 18,
			"versionNonce": 2036969078,
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
			"updated": 1710132693757,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 1848056810,
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
			"updated": 1710132693757,
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
			"version": 18,
			"versionNonce": 1079537590,
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
			"updated": 1710132693757,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 1668288170,
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
			"updated": 1710132693757,
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
			"version": 18,
			"versionNonce": 1448937718,
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
			"updated": 1710132693757,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 277653866,
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
			"updated": 1710132693757,
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
			"version": 18,
			"versionNonce": 184318518,
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
			"updated": 1710132693757,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 214428714,
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
			"updated": 1710132693757,
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
			"version": 18,
			"versionNonce": 1964753782,
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
			"updated": 1710132693757,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 1309464298,
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
			"updated": 1710132693757,
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
			"version": 18,
			"versionNonce": 117433526,
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
			"updated": 1710132693757,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 1424386474,
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
			"updated": 1710132693757,
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
			"version": 18,
			"versionNonce": 575528438,
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
			"updated": 1710132693757,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 1484760170,
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
			"updated": 1710132693757,
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
			"version": 18,
			"versionNonce": 738897718,
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
			"updated": 1710132693757,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 1923319594,
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
			"updated": 1710132693757,
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
			"version": 18,
			"versionNonce": 547051638,
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
			"updated": 1710132693757,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 1270682090,
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
			"updated": 1710132693757,
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
			"version": 18,
			"versionNonce": 667212214,
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
			"updated": 1710132693757,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 1188512938,
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
			"updated": 1710132693757,
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
			"version": 18,
			"versionNonce": 682373878,
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
			"updated": 1710132693757,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 765271914,
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
			"updated": 1710132693757,
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
			"version": 18,
			"versionNonce": 1574331446,
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
			"updated": 1710132693757,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 1549378090,
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
			"updated": 1710132693757,
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
			"version": 18,
			"versionNonce": 1764257142,
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
			"updated": 1710132693758,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 1844956394,
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
			"updated": 1710132693758,
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
			"version": 18,
			"versionNonce": 1743212214,
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
			"updated": 1710132693758,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 1745002410,
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
			"updated": 1710132693758,
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
			"version": 18,
			"versionNonce": 112723958,
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
			"updated": 1710132693758,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 1722096234,
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
			"updated": 1710132693758,
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
			"version": 18,
			"versionNonce": 362780982,
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
			"updated": 1710132693758,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 1219116330,
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
			"updated": 1710132693758,
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
			"version": 18,
			"versionNonce": 469959286,
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
			"updated": 1710132693758,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 1534920682,
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
			"updated": 1710132693758,
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
			"version": 18,
			"versionNonce": 1822901174,
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
			"updated": 1710132693758,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 120093354,
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
			"updated": 1710132693758,
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
			"version": 18,
			"versionNonce": 967924982,
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
			"updated": 1710132693758,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 2052560234,
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
			"updated": 1710132693758,
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
			"version": 18,
			"versionNonce": 681987638,
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
			"updated": 1710132693758,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 1448433706,
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
			"updated": 1710132693758,
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
			"version": 18,
			"versionNonce": 1718294390,
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
			"updated": 1710132693758,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 1527562986,
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
			"updated": 1710132693758,
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
			"version": 18,
			"versionNonce": 994359478,
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
			"updated": 1710132693758,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 319346090,
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
			"updated": 1710132693758,
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
			"version": 18,
			"versionNonce": 517485046,
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
			"updated": 1710132693758,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 2138345578,
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
			"updated": 1710132693758,
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
			"version": 18,
			"versionNonce": 1277854518,
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
			"updated": 1710132693758,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 1142616874,
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
			"updated": 1710132693758,
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
			"version": 18,
			"versionNonce": 1436593270,
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
			"updated": 1710132693758,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 1399258602,
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
			"updated": 1710132693758,
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
			"version": 18,
			"versionNonce": 956280246,
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
			"updated": 1710132693758,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 442740906,
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
			"updated": 1710132693758,
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
			"version": 18,
			"versionNonce": 1936492278,
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
			"updated": 1710132693758,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 750521194,
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
			"updated": 1710132693758,
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
			"version": 18,
			"versionNonce": 359413814,
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
			"updated": 1710132693758,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 1891307050,
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
			"updated": 1710132693758,
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
			"version": 18,
			"versionNonce": 1457766774,
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
			"updated": 1710132693758,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 1263253738,
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
			"updated": 1710132693758,
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
			"version": 18,
			"versionNonce": 723002038,
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
			"updated": 1710132693758,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 1274612650,
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
			"updated": 1710132693758,
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
			"version": 18,
			"versionNonce": 1420712950,
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
			"updated": 1710132693758,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 1491994218,
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
			"updated": 1710132693758,
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
			"version": 18,
			"versionNonce": 2041277750,
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
			"updated": 1710132693758,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 1526049066,
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
			"updated": 1710132693758,
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
			"version": 18,
			"versionNonce": 930371190,
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
			"updated": 1710132693758,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 1769665514,
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
			"updated": 1710132693758,
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
			"version": 18,
			"versionNonce": 919476150,
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
			"updated": 1710132693758,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 1988683434,
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
			"updated": 1710132693758,
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
			"version": 18,
			"versionNonce": 1071493366,
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
			"updated": 1710132693758,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 2060091754,
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
			"updated": 1710132693758,
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
			"version": 18,
			"versionNonce": 1311253046,
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
			"updated": 1710132693758,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 562742314,
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
			"updated": 1710132693758,
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
			"version": 18,
			"versionNonce": 613575542,
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
			"updated": 1710132693758,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 1957998314,
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
			"updated": 1710132693759,
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
			"version": 18,
			"versionNonce": 1633782966,
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
			"updated": 1710132693759,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 148062634,
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
			"updated": 1710132693759,
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
			"version": 18,
			"versionNonce": 305825270,
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
			"updated": 1710132693759,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 689011818,
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
			"updated": 1710132693759,
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
			"version": 18,
			"versionNonce": 1210210102,
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
			"updated": 1710132693759,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 54157098,
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
			"updated": 1710132693759,
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
			"version": 18,
			"versionNonce": 729677942,
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
			"updated": 1710132693759,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 1404627434,
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
			"updated": 1710132693759,
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
			"version": 18,
			"versionNonce": 269648310,
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
			"updated": 1710132693759,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 295181482,
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
			"updated": 1710132693759,
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
			"version": 18,
			"versionNonce": 151313142,
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
			"updated": 1710132693759,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 444790634,
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
			"updated": 1710132693759,
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
			"version": 18,
			"versionNonce": 2094664758,
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
			"updated": 1710132693759,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 1589934634,
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
			"updated": 1710132693759,
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
			"version": 18,
			"versionNonce": 964105590,
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
			"updated": 1710132693759,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 222799082,
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
			"updated": 1710132693759,
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
			"version": 18,
			"versionNonce": 136378038,
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
			"updated": 1710132693759,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 1066891178,
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
			"updated": 1710132693759,
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
			"version": 18,
			"versionNonce": 1098690550,
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
			"updated": 1710132693759,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 635368042,
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
			"updated": 1710132693759,
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
			"version": 18,
			"versionNonce": 1636778294,
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
			"updated": 1710132693759,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 854136106,
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
			"updated": 1710132693759,
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
			"version": 18,
			"versionNonce": 465414774,
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
			"updated": 1710132693759,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 1210114026,
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
			"updated": 1710132693759,
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
			"version": 18,
			"versionNonce": 1858923446,
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
			"updated": 1710132693759,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 1636913834,
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
			"updated": 1710132693759,
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
			"version": 18,
			"versionNonce": 954336502,
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
			"updated": 1710132693759,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 1105554794,
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
			"updated": 1710132693759,
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
			"version": 18,
			"versionNonce": 1266808374,
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
			"updated": 1710132693759,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 510144554,
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
			"updated": 1710132693759,
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
			"version": 18,
			"versionNonce": 2140258166,
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
			"updated": 1710132693759,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 1258593002,
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
			"updated": 1710132693759,
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
			"version": 18,
			"versionNonce": 1230397622,
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
			"updated": 1710132693759,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 1715842474,
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
			"updated": 1710132693759,
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
			"version": 18,
			"versionNonce": 1282726390,
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
			"updated": 1710132693759,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 89548906,
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
			"updated": 1710132693759,
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
			"version": 18,
			"versionNonce": 1878141750,
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
			"updated": 1710132693759,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 1610730282,
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
			"updated": 1710132693759,
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
			"version": 18,
			"versionNonce": 1915966582,
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
			"updated": 1710132693759,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 2092094954,
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
			"updated": 1710132693759,
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
			"version": 18,
			"versionNonce": 2096977334,
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
			"updated": 1710132693759,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 1551141034,
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
			"updated": 1710132693759,
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
			"version": 18,
			"versionNonce": 963981046,
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
			"updated": 1710132693759,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 653386602,
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
			"updated": 1710132693760,
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
			"version": 18,
			"versionNonce": 1679810614,
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
			"updated": 1710132693760,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 1450567210,
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
			"updated": 1710132693760,
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
			"version": 18,
			"versionNonce": 1625450870,
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
			"updated": 1710132693760,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 1676382442,
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
			"updated": 1710132693760,
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
			"version": 18,
			"versionNonce": 1325517494,
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
			"updated": 1710132693760,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 1927144362,
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
			"updated": 1710132693760,
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
			"version": 18,
			"versionNonce": 488834038,
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
			"updated": 1710132693760,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 2105007722,
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
			"updated": 1710132693760,
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
			"version": 18,
			"versionNonce": 491459894,
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
			"updated": 1710132693760,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 8683818,
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
			"updated": 1710132693760,
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
			"version": 18,
			"versionNonce": 417267318,
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
			"updated": 1710132693760,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 661572586,
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
			"updated": 1710132693760,
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
			"version": 18,
			"versionNonce": 1688453046,
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
			"updated": 1710132693760,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 2017574570,
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
			"updated": 1710132693760,
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
			"version": 18,
			"versionNonce": 1958631670,
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
			"updated": 1710132693760,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 2141739370,
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
			"updated": 1710132693760,
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
			"version": 18,
			"versionNonce": 1890830902,
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
			"updated": 1710132693760,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 2095946794,
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
			"updated": 1710132693760,
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
			"version": 18,
			"versionNonce": 1198068598,
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
			"updated": 1710132693760,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 234653418,
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
			"updated": 1710132693760,
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
			"version": 18,
			"versionNonce": 1126380726,
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
			"updated": 1710132693760,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 1533024682,
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
			"updated": 1710132693760,
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
			"version": 18,
			"versionNonce": 495398390,
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
			"updated": 1710132693760,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 1145263210,
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
			"updated": 1710132693760,
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
			"version": 18,
			"versionNonce": 328859446,
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
			"updated": 1710132693760,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 175191850,
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
			"updated": 1710132693760,
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
			"version": 18,
			"versionNonce": 2042669174,
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
			"updated": 1710132693760,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 2119483882,
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
			"updated": 1710132693760,
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
			"version": 18,
			"versionNonce": 1337993654,
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
			"updated": 1710132693760,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 18,
			"versionNonce": 720958634,
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
			"updated": 1710132693760,
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
			"id": "t8Mqz3BhEb4Y13vINrpWz",
			"type": "rectangle",
			"x": -981.9474352952545,
			"y": -8621.397328325436,
			"width": 362.7341252758317,
			"height": 177.92082375244883,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"seed": 1178919734,
			"version": 339,
			"versionNonce": 1421705974,
			"isDeleted": false,
			"boundElements": [
				{
					"type": "text",
					"id": "T9BBns1U"
				}
			],
			"updated": 1710132693760,
			"link": null,
			"locked": false
		},
		{
			"id": "T9BBns1U",
			"type": "text",
			"x": -976.9474352952545,
			"y": -8616.397328325436,
			"width": 346.75177001953125,
			"height": 120,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1086259190,
			"version": 531,
			"versionNonce": 34131818,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132693760,
			"link": null,
			"locked": false,
			"text": "Instruction - 컴퓨터가 사용하는 언어\nISA - instruction set들의 짜임 -> standard가\n정해짐\n\n=> 결국 이를 사용하는 이유는 편리하게 기기를\n관리하기 위해서!",
			"rawText": "Instruction - 컴퓨터가 사용하는 언어\nISA - instruction set들의 짜임 -> standard가 정해짐\n\n=> 결국 이를 사용하는 이유는 편리하게 기기를 관리하기 위해서!",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 114,
			"containerId": "t8Mqz3BhEb4Y13vINrpWz",
			"originalText": "Instruction - 컴퓨터가 사용하는 언어\nISA - instruction set들의 짜임 -> standard가 정해짐\n\n=> 결국 이를 사용하는 이유는 편리하게 기기를 관리하기 위해서!",
			"lineHeight": 1.25
		},
		{
			"id": "TSaQ8a8W",
			"type": "text",
			"x": 601.2487079958565,
			"y": -8731.43585427145,
			"width": 368.86383056640625,
			"height": 40,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 840191542,
			"version": 134,
			"versionNonce": 457028662,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132693760,
			"link": null,
			"locked": false,
			"text": "모든 컴퓨터 아키텍쳐의 기반이 됨 = stored-program\n",
			"rawText": "모든 컴퓨터 아키텍쳐의 기반이 됨 = stored-program\n",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 34,
			"containerId": null,
			"originalText": "모든 컴퓨터 아키텍쳐의 기반이 됨 = stored-program\n",
			"lineHeight": 1.25
		},
		{
			"id": "B5z6U6E9Cm61UbO1R5P_q",
			"type": "rectangle",
			"x": 634.5746998343027,
			"y": -8680.23542618939,
			"width": 193.5936809859486,
			"height": 117.75618810082415,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"seed": 1151234538,
			"version": 99,
			"versionNonce": 131027498,
			"isDeleted": false,
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
			"updated": 1710132693760,
			"link": null,
			"locked": false
		},
		{
			"id": "CAz9W5LZ",
			"type": "text",
			"x": 661.2755625440739,
			"y": -8631.357332138978,
			"width": 140.19195556640625,
			"height": 20,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 253381098,
			"version": 100,
			"versionNonce": 489012598,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132693760,
			"link": null,
			"locked": false,
			"text": "메모리 <=> 프로세서",
			"rawText": "메모리 <=> 프로세서",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "center",
			"verticalAlign": "middle",
			"baseline": 14,
			"containerId": "B5z6U6E9Cm61UbO1R5P_q",
			"originalText": "메모리 <=> 프로세서",
			"lineHeight": 1.25
		},
		{
			"id": "Lmt4uWzEAL-LiBON4wn_n",
			"type": "rectangle",
			"x": 913.8808940504575,
			"y": -8652.761423547912,
			"width": 82.33292435484816,
			"height": 61.0486553465289,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"seed": 2077179574,
			"version": 159,
			"versionNonce": 2134342890,
			"isDeleted": false,
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
			"updated": 1710132693760,
			"link": null,
			"locked": false
		},
		{
			"id": "oX0Db6O3",
			"type": "text",
			"x": 940.8793645896981,
			"y": -8632.237095874647,
			"width": 28.335983276367188,
			"height": 20,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 729602998,
			"version": 132,
			"versionNonce": 1337630390,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132693760,
			"link": null,
			"locked": false,
			"text": "I/O",
			"rawText": "I/O",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "center",
			"verticalAlign": "middle",
			"baseline": 14,
			"containerId": "Lmt4uWzEAL-LiBON4wn_n",
			"originalText": "I/O",
			"lineHeight": 1.25
		},
		{
			"id": "ajdLtQr6MXH5okIgbOgop",
			"type": "arrow",
			"x": 837.5776170053151,
			"y": -8627.471639363826,
			"width": 67.99209489339933,
			"height": 4.887993481312151,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 592014070,
			"version": 255,
			"versionNonce": 365711274,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132693760,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					67.99209489339933,
					4.887993481312151
				]
			],
			"lastCommittedPoint": null,
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
			"startArrowhead": "arrow",
			"endArrowhead": "arrow"
		},
		{
			"id": "d1bvRq3p",
			"type": "text",
			"x": 725.2814289414068,
			"y": -8600.207837034255,
			"width": 91.03997802734375,
			"height": 40,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1367591658,
			"version": 107,
			"versionNonce": 933320694,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132693761,
			"link": null,
			"locked": false,
			"text": "프로그램 실행\n",
			"rawText": "프로그램 실행\n",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 34,
			"containerId": null,
			"originalText": "프로그램 실행\n",
			"lineHeight": 1.25
		},
		{
			"id": "UotxPxiC",
			"type": "text",
			"x": -521.4661347417822,
			"y": -7968.190180952794,
			"width": 283.7439270019531,
			"height": 40,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 2095757930,
			"version": 193,
			"versionNonce": 263768682,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132693761,
			"link": null,
			"locked": false,
			"text": "Von neumann 아키텍처를 사용하긴 하는데\n세부적인 작동방식은 모두 다름",
			"rawText": "Von neumann 아키텍처를 사용하긴 하는데\n세부적인 작동방식은 모두 다름",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 34,
			"containerId": null,
			"originalText": "Von neumann 아키텍처를 사용하긴 하는데\n세부적인 작동방식은 모두 다름",
			"lineHeight": 1.25
		},
		{
			"id": "X__5oLzTFEKzCsFJuyqSc",
			"type": "rectangle",
			"x": 605.6112138146932,
			"y": -8286.110465383563,
			"width": 136.46775002968707,
			"height": 48.55049463544492,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"seed": 1524322934,
			"version": 73,
			"versionNonce": 2094983478,
			"isDeleted": false,
			"boundElements": [
				{
					"type": "text",
					"id": "XqXOQw5O"
				}
			],
			"updated": 1710132693761,
			"link": null,
			"locked": false
		},
		{
			"id": "XqXOQw5O",
			"type": "text",
			"x": 654.3171118397906,
			"y": -8271.83521806584,
			"width": 39.05595397949219,
			"height": 20,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1807395830,
			"version": 70,
			"versionNonce": 1942482218,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132693761,
			"link": null,
			"locked": false,
			"text": "CISC",
			"rawText": "CISC",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "center",
			"verticalAlign": "middle",
			"baseline": 14,
			"containerId": "X__5oLzTFEKzCsFJuyqSc",
			"originalText": "CISC",
			"lineHeight": 1.25
		},
		{
			"id": "MQ6G7UKK",
			"type": "text",
			"x": 610.8842094598102,
			"y": -8224.339770945237,
			"width": 257.1038818359375,
			"height": 60,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1732507894,
			"version": 186,
			"versionNonce": 2128106102,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132693761,
			"link": null,
			"locked": false,
			"text": "- 가능한 적은 수의 instruction 사용.\n- lower power consumption\n- x86, intel, AMD 에서 사용",
			"rawText": "- 가능한 적은 수의 instruction 사용.\n- lower power consumption\n- x86, intel, AMD 에서 사용",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 54,
			"containerId": null,
			"originalText": "- 가능한 적은 수의 instruction 사용.\n- lower power consumption\n- x86, intel, AMD 에서 사용",
			"lineHeight": 1.25
		},
		{
			"id": "tX8myfQJrr5rOBibd3YnM",
			"type": "rectangle",
			"x": 611.9018140209395,
			"y": -8145.357942944344,
			"width": 136.4322486527542,
			"height": 45.49125616782021,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"seed": 1829405994,
			"version": 99,
			"versionNonce": 929347562,
			"isDeleted": false,
			"boundElements": [
				{
					"type": "text",
					"id": "6BCixxbK"
				}
			],
			"updated": 1710132693761,
			"link": null,
			"locked": false
		},
		{
			"id": "6BCixxbK",
			"type": "text",
			"x": 660.3179581837423,
			"y": -8132.612314860434,
			"width": 39.59996032714844,
			"height": 20,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 860385962,
			"version": 43,
			"versionNonce": 1750242230,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132693761,
			"link": null,
			"locked": false,
			"text": "RISC",
			"rawText": "RISC",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "center",
			"verticalAlign": "middle",
			"baseline": 14,
			"containerId": "tX8myfQJrr5rOBibd3YnM",
			"originalText": "RISC",
			"lineHeight": 1.25
		},
		{
			"id": "iEhLxw13",
			"type": "text",
			"x": 614.9106445964248,
			"y": -8080.315331904046,
			"width": 280.39990234375,
			"height": 60,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 552766454,
			"version": 152,
			"versionNonce": 1788488362,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132693761,
			"link": null,
			"locked": false,
			"text": "- 최대한 instruction을 간결하게 짜는 쪽\n- fast, simple, more operations\n- ARM, RISC-V 에서 사용",
			"rawText": "- 최대한 instruction을 간결하게 짜는 쪽\n- fast, simple, more operations\n- ARM, RISC-V 에서 사용",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 54,
			"containerId": null,
			"originalText": "- 최대한 instruction을 간결하게 짜는 쪽\n- fast, simple, more operations\n- ARM, RISC-V 에서 사용",
			"lineHeight": 1.25
		},
		{
			"id": "vipUEY6ER4KWDYVb97JwU",
			"type": "freedraw",
			"x": -350.2420034122119,
			"y": -7691.828157358241,
			"width": 76.9265065105854,
			"height": 28.77660859983189,
			"angle": 0,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1991992438,
			"version": 57,
			"versionNonce": 1131588854,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132693761,
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
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				0.8278575736877656,
				5.171951311200246
			]
		},
		{
			"id": "WhPAVaZMfpji3fUxbweER",
			"type": "freedraw",
			"x": -150.6989214335158,
			"y": -7701.329372074957,
			"width": 77.2025436831616,
			"height": 27.18615707099434,
			"angle": 0,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 652185450,
			"version": 51,
			"versionNonce": 1678984554,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132693761,
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
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				3.1424051410557468,
				-8.797942089548087
			]
		},
		{
			"id": "lNV_zjpCL3r8g8Qd3vKSi",
			"type": "freedraw",
			"x": -391.96780273436144,
			"y": -7584.819439749786,
			"width": 40.102690589639565,
			"height": 2.163146130118548,
			"angle": 0,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1966195370,
			"version": 29,
			"versionNonce": 230530614,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132693761,
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
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				40.102690589639565,
				2.163146130118548
			]
		},
		{
			"id": "yb45C9AuIpFLe4m7eDdGp",
			"type": "freedraw",
			"x": -197.45123831457965,
			"y": -7582.994547082291,
			"width": 30.574760959808373,
			"height": 0.47774492434928106,
			"angle": 0,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 2061158762,
			"version": 27,
			"versionNonce": 1830488106,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132693761,
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
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				30.574760959808373,
				-0.47774492434928106
			]
		},
		{
			"id": "jmVIlVzq5Z7ae-m1oERyr",
			"type": "freedraw",
			"x": -391.76007650881644,
			"y": -7546.8739529997065,
			"width": 50.479250415712954,
			"height": 0,
			"angle": 0,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 813341354,
			"version": 23,
			"versionNonce": 1276667766,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132693761,
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
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				50.479250415712954,
				0
			]
		},
		{
			"id": "5q8tVZKnqaq3WYizQV2YR",
			"type": "freedraw",
			"x": -395.644252193658,
			"y": -7514.367490508755,
			"width": 70.30654088315089,
			"height": 0,
			"angle": 0,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1882314986,
			"version": 23,
			"versionNonce": 1838969578,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132693761,
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
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				70.30654088315089,
				0
			]
		},
		{
			"id": "f-Ja1UtBKLm2PNSii9dYw",
			"type": "freedraw",
			"x": -204.47771756286056,
			"y": -7552.016243646916,
			"width": 39.117489288142906,
			"height": 0.16912673131173506,
			"angle": 0,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 137658154,
			"version": 25,
			"versionNonce": 516425910,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132693761,
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
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				39.117489288142906,
				-0.16912673131173506
			]
		},
		{
			"id": "YZB_ddI-fQvstsuUFtlrH",
			"type": "freedraw",
			"x": -213.13919012477072,
			"y": -7514.189475736007,
			"width": 47.18554541502442,
			"height": 0.27298984408480464,
			"angle": 0,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 797620970,
			"version": 24,
			"versionNonce": 404915626,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132693761,
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
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				47.18554541502442,
				-0.27298984408480464
			]
		},
		{
			"id": "gjWWYZvm",
			"type": "text",
			"x": 596.0188585816577,
			"y": -7823.279941203918,
			"width": 283.2799377441406,
			"height": 40,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 594255606,
			"version": 150,
			"versionNonce": 1433502198,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132693761,
			"link": null,
			"locked": false,
			"text": "컴퓨터라면 누구나 할 수 있는 수학적 연산\n- operation / operand",
			"rawText": "컴퓨터라면 누구나 할 수 있는 수학적 연산\n- operation / operand",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 34,
			"containerId": null,
			"originalText": "컴퓨터라면 누구나 할 수 있는 수학적 연산\n- operation / operand",
			"lineHeight": 1.25
		},
		{
			"id": "XgQQWP0B",
			"type": "text",
			"x": -797.701401223195,
			"y": -7365.914374469314,
			"width": 194.7678985595703,
			"height": 60,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 607799146,
			"version": 146,
			"versionNonce": 366493802,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132693761,
			"link": null,
			"locked": false,
			"text": "add - operator, 연산 시행\ng, h - operand, 연산자\nx5, x6 - register!",
			"rawText": "add - operator, 연산 시행\ng, h - operand, 연산자\nx5, x6 - register!",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 54,
			"containerId": null,
			"originalText": "add - operator, 연산 시행\ng, h - operand, 연산자\nx5, x6 - register!",
			"lineHeight": 1.25
		},
		{
			"id": "5KeRyN42",
			"type": "text",
			"x": -831.5594446068492,
			"y": -7280.271106266116,
			"width": 231.64788818359375,
			"height": 40,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 404313078,
			"version": 145,
			"versionNonce": 52024118,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132693761,
			"link": null,
			"locked": false,
			"text": "register는 CPU의 임시 저장공간,\n다양한 종류가 있음",
			"rawText": "register는 CPU의 임시 저장공간,\n다양한 종류가 있음",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 34,
			"containerId": null,
			"originalText": "register는 CPU의 임시 저장공간,\n다양한 종류가 있음",
			"lineHeight": 1.25
		},
		{
			"id": "KqjndcrP",
			"type": "text",
			"x": 607.6769519467957,
			"y": -7379.603151368213,
			"width": 155.15187072753906,
			"height": 80,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1325744758,
			"version": 126,
			"versionNonce": 847815466,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132693761,
			"link": null,
			"locked": false,
			"text": "byte - 8bits\nhalfword - 16bits\nword - 32bits\ndoubleword - 64bits",
			"rawText": "byte - 8bits\nhalfword - 16bits\nword - 32bits\ndoubleword - 64bits",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 74,
			"containerId": null,
			"originalText": "byte - 8bits\nhalfword - 16bits\nword - 32bits\ndoubleword - 64bits",
			"lineHeight": 1.25
		},
		{
			"id": "H8Qj4rR9",
			"type": "text",
			"x": 603.0835969332894,
			"y": -7251.104113852202,
			"width": 374.22381591796875,
			"height": 40,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1476465398,
			"version": 216,
			"versionNonce": 304479350,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132693761,
			"link": null,
			"locked": false,
			"text": "RISC-V 같은 경우는 총 32개의 64-bit 레지스터 존재\n더 수를 늘리지 않는 이유는 속도 때문",
			"rawText": "RISC-V 같은 경우는 총 32개의 64-bit 레지스터 존재\n더 수를 늘리지 않는 이유는 속도 때문",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 34,
			"containerId": null,
			"originalText": "RISC-V 같은 경우는 총 32개의 64-bit 레지스터 존재\n더 수를 늘리지 않는 이유는 속도 때문",
			"lineHeight": 1.25
		},
		{
			"id": "SzCUpCqL",
			"type": "text",
			"x": -757.1022837924777,
			"y": -6794.687259294081,
			"width": 168.23995971679688,
			"height": 40,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 2064178230,
			"version": 105,
			"versionNonce": 144616938,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132693761,
			"link": null,
			"locked": false,
			"text": "변수를 레지스터에 넣는건\n<컴파일러>가 담당",
			"rawText": "변수를 레지스터에 넣는건\n<컴파일러>가 담당",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 34,
			"containerId": null,
			"originalText": "변수를 레지스터에 넣는건\n<컴파일러>가 담당",
			"lineHeight": 1.25
		},
		{
			"id": "IaoXUppA",
			"type": "text",
			"x": 610.970435994524,
			"y": -6882.569919406659,
			"width": 368.60791015625,
			"height": 120,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 265742378,
			"version": 292,
			"versionNonce": 1482358198,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132693761,
			"link": null,
			"locked": false,
			"text": "하지만 array 등의 이용으로 레지스터가 부족하다면?\n -> memory의 이용\n\nCPU 레지스터에 저장된 데이터 -> 메모리로 이동\n > 하지만 매우 느리다 (캐시까지 다 거쳐서 오기 때문)\n > memory hierarchy",
			"rawText": "하지만 array 등의 이용으로 레지스터가 부족하다면?\n -> memory의 이용\n\nCPU 레지스터에 저장된 데이터 -> 메모리로 이동\n > 하지만 매우 느리다 (캐시까지 다 거쳐서 오기 때문)\n > memory hierarchy",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 114,
			"containerId": null,
			"originalText": "하지만 array 등의 이용으로 레지스터가 부족하다면?\n -> memory의 이용\n\nCPU 레지스터에 저장된 데이터 -> 메모리로 이동\n > 하지만 매우 느리다 (캐시까지 다 거쳐서 오기 때문)\n > memory hierarchy",
			"lineHeight": 1.25
		},
		{
			"id": "Af9-UIN41V18KnBSGVdFU",
			"type": "freedraw",
			"x": 171.6293858631286,
			"y": -6576.861707237859,
			"width": 230.80322073265998,
			"height": 0.7875111301145807,
			"angle": 0,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1662880246,
			"version": 51,
			"versionNonce": 757424298,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132693761,
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
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				230.80322073265998,
				-0.7875111301145807
			]
		},
		{
			"id": "dA191UfA",
			"type": "text",
			"x": -861.3732680965674,
			"y": -6482.172515195531,
			"width": 284.8798828125,
			"height": 260,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 445650870,
			"version": 497,
			"versionNonce": 719181558,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132693761,
			"link": null,
			"locked": false,
			"text": "레지스터와 메모리 사이의 데이터 이동은 \n<memory address>를 이용\n\n주소 사이의 간격은 무조건 1byte\n\n보통 64bit이므로 2^64 - 1만큼 저장가능\n\n운영체제마다 다르지만, 대개\nchar - 1byte, int/float - 4bytes, \nlong/double - 8bytes만큼 저장\n\n레지스터에 쓰는 행위를 load,\nmemory에 저장하는 행위를 store",
			"rawText": "레지스터와 메모리 사이의 데이터 이동은 \n<memory address>를 이용\n\n주소 사이의 간격은 무조건 1byte\n\n보통 64bit이므로 2^64 - 1만큼 저장가능\n\n운영체제마다 다르지만, 대개\nchar - 1byte, int/float - 4bytes, \nlong/double - 8bytes만큼 저장\n\n레지스터에 쓰는 행위를 load,\nmemory에 저장하는 행위를 store",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 254,
			"containerId": null,
			"originalText": "레지스터와 메모리 사이의 데이터 이동은 \n<memory address>를 이용\n\n주소 사이의 간격은 무조건 1byte\n\n보통 64bit이므로 2^64 - 1만큼 저장가능\n\n운영체제마다 다르지만, 대개\nchar - 1byte, int/float - 4bytes, \nlong/double - 8bytes만큼 저장\n\n레지스터에 쓰는 행위를 load,\nmemory에 저장하는 행위를 store",
			"lineHeight": 1.25
		},
		{
			"id": "SOnc6PT3-08uvgw-gbqMJ",
			"type": "rectangle",
			"x": -1049.8163765806335,
			"y": -6442.8641677764945,
			"width": 151.02781258420532,
			"height": 37.18883338316573,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [
				"Sa4UO2A-icw4ijMTyuKTY"
			],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"seed": 759955050,
			"version": 82,
			"versionNonce": 584105514,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132693761,
			"link": null,
			"locked": false
		},
		{
			"type": "rectangle",
			"version": 133,
			"versionNonce": 1044451702,
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
			"updated": 1710132693761,
			"link": null,
			"locked": false
		},
		{
			"id": "MlfzEXr4",
			"type": "text",
			"x": -982.017609627765,
			"y": -6393.794942604482,
			"width": 13.151962280273438,
			"height": 20,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [
				"Sa4UO2A-icw4ijMTyuKTY"
			],
			"frameId": null,
			"roundness": null,
			"seed": 210832438,
			"version": 14,
			"versionNonce": 254503146,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132693761,
			"link": null,
			"locked": false,
			"text": "...",
			"rawText": "...",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "center",
			"verticalAlign": "middle",
			"baseline": 14,
			"containerId": "UJFwZ2W9SfaMuBFqDUrqS",
			"originalText": "...",
			"lineHeight": 1.25
		},
		{
			"type": "rectangle",
			"version": 128,
			"versionNonce": 1514894006,
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
			"updated": 1710132693761,
			"link": null,
			"locked": false
		},
		{
			"id": "87uFiNXv",
			"type": "text",
			"x": -1013.3870764581737,
			"y": -6354.651234894422,
			"width": 76.0479736328125,
			"height": 20,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [
				"Sa4UO2A-icw4ijMTyuKTY"
			],
			"frameId": null,
			"roundness": null,
			"seed": 160261174,
			"version": 20,
			"versionNonce": 1482865578,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132693761,
			"link": null,
			"locked": false,
			"text": "0010 1010",
			"rawText": "0010 1010",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "center",
			"verticalAlign": "middle",
			"baseline": 14,
			"containerId": "kO9Ks88i2gHQAOdawIke0",
			"originalText": "0010 1010",
			"lineHeight": 1.25
		},
		{
			"type": "rectangle",
			"version": 126,
			"versionNonce": 1626844150,
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
			"updated": 1710132693761,
			"link": null,
			"locked": false
		},
		{
			"id": "U7KXNfZ4",
			"type": "text",
			"x": -1012.012381321677,
			"y": -6315.187826321599,
			"width": 76.0479736328125,
			"height": 20,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [
				"Sa4UO2A-icw4ijMTyuKTY"
			],
			"frameId": null,
			"roundness": null,
			"seed": 1638942570,
			"version": 20,
			"versionNonce": 211924586,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132693762,
			"link": null,
			"locked": false,
			"text": "0000 1011",
			"rawText": "0000 1011",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "center",
			"verticalAlign": "middle",
			"baseline": 14,
			"containerId": "ZSICSDk-Jt2MLZnxwa0Y4",
			"originalText": "0000 1011",
			"lineHeight": 1.25
		},
		{
			"id": "Kx2dHAWs",
			"type": "text",
			"x": -1067.8332939545976,
			"y": -6311.221307820888,
			"width": 11.00799560546875,
			"height": 20,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [
				"Sa4UO2A-icw4ijMTyuKTY"
			],
			"frameId": null,
			"roundness": null,
			"seed": 650540778,
			"version": 44,
			"versionNonce": 1347075382,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132693762,
			"link": null,
			"locked": false,
			"text": "0",
			"rawText": "0",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 14,
			"containerId": null,
			"originalText": "0",
			"lineHeight": 1.25
		},
		{
			"id": "0NRLXXpV",
			"type": "text",
			"x": -1065.983226533494,
			"y": -6353.088854145645,
			"width": 4.33599853515625,
			"height": 20,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [
				"Sa4UO2A-icw4ijMTyuKTY"
			],
			"frameId": null,
			"roundness": null,
			"seed": 1477824554,
			"version": 36,
			"versionNonce": 1018386730,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132693762,
			"link": null,
			"locked": false,
			"text": "1",
			"rawText": "1",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 14,
			"containerId": null,
			"originalText": "1",
			"lineHeight": 1.25
		},
		{
			"id": "3Y2j5Fdn",
			"type": "text",
			"x": -1035.9548805543222,
			"y": -6468.900405447293,
			"width": 126.89593505859375,
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
			"seed": 1018524394,
			"version": 114,
			"versionNonce": 671261674,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132693762,
			"link": null,
			"locked": false,
			"text": "RAM = 1D array",
			"rawText": "RAM = 1D array",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 14,
			"containerId": null,
			"originalText": "RAM = 1D array",
			"lineHeight": 1.25
		},
		{
			"id": "VLA2kOtYAsNVYtkc99E_p",
			"type": "freedraw",
			"x": 318.8623659223992,
			"y": -6421.815040684256,
			"width": 103.59852196980341,
			"height": 0.9146060867597043,
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
			"seed": 221761322,
			"version": 62,
			"versionNonce": 1962868982,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132693762,
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
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				103.59852196980341,
				0.9146060867597043
			]
		},
		{
			"id": "z_5bJ7AmclbBU5nNp-M6y",
			"type": "freedraw",
			"x": 164.25360650125901,
			"y": -6265.222061002594,
			"width": 30.55092117147609,
			"height": 24.24791345723588,
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
			"seed": 1302364406,
			"version": 147,
			"versionNonce": 1923052086,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132693762,
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
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				1.9501513827877375,
				-4.346700584074824
			]
		},
		{
			"id": "fFc86EPy",
			"type": "text",
			"x": 608.283956398401,
			"y": -6472.519029703522,
			"width": 332.3358154296875,
			"height": 300,
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
			"seed": 1992337642,
			"version": 438,
			"versionNonce": 1570749302,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132693762,
			"link": null,
			"locked": false,
			"text": "a[8]에 어떻게 접근할 것인가\n\n1. doubleword array -> 한 칸당 8bytes 차지.\n2. [8] -> 8th element\n3. base register -> x22\n4. 결론은 x22에서 8 * 8 = 64bytes 이동\n5. 64(x22)\n\n앞의 operator마다 다름\nlb - load byte\nlh - load halfword\nlw - load word\nld - load doubleword\n뛰어넘는 간격은 모두 byte 단위지만, \n읽는 범위가 다름",
			"rawText": "a[8]에 어떻게 접근할 것인가\n\n1. doubleword array -> 한 칸당 8bytes 차지.\n2. [8] -> 8th element\n3. base register -> x22\n4. 결론은 x22에서 8 * 8 = 64bytes 이동\n5. 64(x22)\n\n앞의 operator마다 다름\nlb - load byte\nlh - load halfword\nlw - load word\nld - load doubleword\n뛰어넘는 간격은 모두 byte 단위지만, \n읽는 범위가 다름",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 294,
			"containerId": null,
			"originalText": "a[8]에 어떻게 접근할 것인가\n\n1. doubleword array -> 한 칸당 8bytes 차지.\n2. [8] -> 8th element\n3. base register -> x22\n4. 결론은 x22에서 8 * 8 = 64bytes 이동\n5. 64(x22)\n\n앞의 operator마다 다름\nlb - load byte\nlh - load halfword\nlw - load word\nld - load doubleword\n뛰어넘는 간격은 모두 byte 단위지만, \n읽는 범위가 다름",
			"lineHeight": 1.25
		},
		{
			"id": "5jGvaqGl",
			"type": "text",
			"x": -922.2795327932897,
			"y": -5949.575792692519,
			"width": 422.559814453125,
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
			"seed": 1353561066,
			"version": 429,
			"versionNonce": 434396906,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132693762,
			"link": null,
			"locked": false,
			"text": "store의 경우도 load와 비슷함\n\n아래의 예시는 x9를 중복 사용해 레지스터를 아낌\n\na[12]는 96(x22)\n\nRISC-V 같은 경우는 alignment restriction,\n즉 word나 double word의 길이가 4나 8의 배수가 될 필요 x",
			"rawText": "store의 경우도 load와 비슷함\n\n아래의 예시는 x9를 중복 사용해 레지스터를 아낌\n\na[12]는 96(x22)\n\nRISC-V 같은 경우는 alignment restriction,\n즉 word나 double word의 길이가 4나 8의 배수가 될 필요 x",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 154,
			"containerId": null,
			"originalText": "store의 경우도 load와 비슷함\n\n아래의 예시는 x9를 중복 사용해 레지스터를 아낌\n\na[12]는 96(x22)\n\nRISC-V 같은 경우는 alignment restriction,\n즉 word나 double word의 길이가 4나 8의 배수가 될 필요 x",
			"lineHeight": 1.25
		},
		{
			"id": "D1tOryiO",
			"type": "text",
			"x": 599.3832498239328,
			"y": -5989.519866962028,
			"width": 303.6959228515625,
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
			"seed": 1149705334,
			"version": 281,
			"versionNonce": 742710454,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132693762,
			"link": null,
			"locked": false,
			"text": "빅 엔디안\n- 가장 큰 바이트부터 낮은 레지스터에 저장\n- IBM만 사용\n\n리틀 엔디안\n- 가장 작은 바이트부터 낮은 레지스터에 저장\n- intel, ARM, RISC-V 등 대부분이 사용 ",
			"rawText": "빅 엔디안\n- 가장 큰 바이트부터 낮은 레지스터에 저장\n- IBM만 사용\n\n리틀 엔디안\n- 가장 작은 바이트부터 낮은 레지스터에 저장\n- intel, ARM, RISC-V 등 대부분이 사용 ",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 134,
			"containerId": null,
			"originalText": "빅 엔디안\n- 가장 큰 바이트부터 낮은 레지스터에 저장\n- IBM만 사용\n\n리틀 엔디안\n- 가장 작은 바이트부터 낮은 레지스터에 저장\n- intel, ARM, RISC-V 등 대부분이 사용 ",
			"lineHeight": 1.25
		},
		{
			"id": "3SZQIimTlmLzlaDUHLVJ0",
			"type": "freedraw",
			"x": -394.5678734360104,
			"y": -5544.630830105707,
			"width": 79.28554863079393,
			"height": 2.7996179875926828,
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
			"seed": 1933772214,
			"version": 43,
			"versionNonce": 1284305322,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132693762,
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
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				79.28554863079393,
				2.7996179875926828
			]
		},
		{
			"id": "KiBTVOE5WB-SVeQrzhsKu",
			"type": "freedraw",
			"x": -316.16907082841124,
			"y": -5544.240178947733,
			"width": 9.23600907282622,
			"height": 7.577273954932025,
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
			"seed": 183458806,
			"version": 22,
			"versionNonce": 1144247798,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132693762,
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
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				-4.200979184930418,
				7.577273954932025
			]
		},
		{
			"id": "8Nl1AZi3CzENDhW1GuIAD",
			"type": "freedraw",
			"x": -305.47590083093485,
			"y": -5514.0612824917325,
			"width": 86.22100632136176,
			"height": 3.0507565605885247,
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
			"seed": 841871978,
			"version": 44,
			"versionNonce": 706030698,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132693762,
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
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				-86.22100632136176,
				3.0507565605885247
			]
		},
		{
			"id": "a08uVVmgqjsnI85NCX7QY",
			"type": "freedraw",
			"x": -385.06525682156064,
			"y": -5517.6297851669415,
			"width": 15.76226876310352,
			"height": 20.36936807463553,
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
			"seed": 917205738,
			"version": 27,
			"versionNonce": 242329398,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132693762,
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
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				7.130849603039621,
				20.36936807463553
			]
		},
		{
			"id": "GCZ2zAT2EDMPZnrCC4JIf",
			"type": "freedraw",
			"x": -188.6884247692882,
			"y": -5460.018914922305,
			"width": 171.5026243660871,
			"height": 3.903354105870676,
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
			"seed": 409382838,
			"version": 40,
			"versionNonce": 191058038,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132693762,
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
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				-171.5026243660871,
				-2.2880541537442696
			]
		},
		{
			"id": "iz-KqrrSU7KggQmtR7-QM",
			"type": "freedraw",
			"x": -351.3984661409342,
			"y": -5467.8318054148185,
			"width": 17.61313218602305,
			"height": 18.36965231209524,
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
			"seed": 189311862,
			"version": 30,
			"versionNonce": 1267767786,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132693762,
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
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				8.433002440690814,
				18.192913375515673
			]
		},
		{
			"id": "Qt7pHywm1yrMGg3ABTb4k",
			"type": "freedraw",
			"x": -378.57619694949153,
			"y": -5329.279808895364,
			"width": 189.30796445731733,
			"height": 0.3255647428068187,
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
			"seed": 78881706,
			"version": 50,
			"versionNonce": 1724764598,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132693762,
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
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				189.30796445731733,
				-0.3255647428068187
			]
		},
		{
			"id": "Ldjb3br9K4zeQFwizJCIg",
			"type": "freedraw",
			"x": -191.22146174865105,
			"y": -5334.255881582078,
			"width": 3.720406355124794,
			"height": 9.744388899409387,
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
			"seed": 1202481002,
			"version": 23,
			"versionNonce": 318360746,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132693762,
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
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				-1.4075434781099148,
				9.744388899409387
			]
		},
		{
			"id": "pVT7JCbw",
			"type": "text",
			"x": 646.5169584306034,
			"y": -5555.008624183627,
			"width": 311.6959228515625,
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
			"seed": 6116266,
			"version": 250,
			"versionNonce": 198585078,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132693762,
			"link": null,
			"locked": false,
			"text": "CPU에서 자주 사용하는 것은 레지스터에 저장,\n자주 사용하지 않는 것은 메모리로 이동\n\nSpilling - 메모리로 데이터가 이동하는 것\n\n메모리로 이동하면 매우 느려짐",
			"rawText": "CPU에서 자주 사용하는 것은 레지스터에 저장,\n자주 사용하지 않는 것은 메모리로 이동\n\nSpilling - 메모리로 데이터가 이동하는 것\n\n메모리로 이동하면 매우 느려짐",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 114,
			"containerId": null,
			"originalText": "CPU에서 자주 사용하는 것은 레지스터에 저장,\n자주 사용하지 않는 것은 메모리로 이동\n\nSpilling - 메모리로 데이터가 이동하는 것\n\n메모리로 이동하면 매우 느려짐",
			"lineHeight": 1.25
		},
		{
			"id": "8E70EYq_MlvI4Mq_YgkRo",
			"type": "freedraw",
			"x": 97.29794026892262,
			"y": -5332.378909299592,
			"width": 235.98391895291184,
			"height": 2.960834888757745,
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
			"seed": 509087338,
			"version": 91,
			"versionNonce": 1680779114,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132693762,
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
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				235.98391895291184,
				-2.960834888757745
			]
		},
		{
			"id": "MsJVgRRoIuquuCC29o3Ak",
			"type": "freedraw",
			"x": 102.54067356404667,
			"y": -5300.888546784692,
			"width": 414.5553578471663,
			"height": 0,
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
			"seed": 1103647466,
			"version": 109,
			"versionNonce": 956390454,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132693762,
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
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				414.5553578471663,
				0
			]
		},
		{
			"id": "If5ukpSg",
			"type": "text",
			"x": -736.8926998157369,
			"y": -4903.280823805154,
			"width": 213.90391540527344,
			"height": 60,
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
			"seed": 1208034218,
			"version": 173,
			"versionNonce": 1467623978,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132693762,
			"link": null,
			"locked": false,
			"text": "Constant 사용시\nload, store 과정이 없어지므로\n굉장히 빨라짐",
			"rawText": "Constant 사용시\nload, store 과정이 없어지므로\n굉장히 빨라짐",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 54,
			"containerId": null,
			"originalText": "Constant 사용시\nload, store 과정이 없어지므로\n굉장히 빨라짐",
			"lineHeight": 1.25
		},
		{
			"id": "it1Vi1Lz",
			"type": "text",
			"x": -532.3518608698457,
			"y": -4775.498506324406,
			"width": 427.1678771972656,
			"height": 40,
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
			"seed": 1149448170,
			"version": 130,
			"versionNonce": 338978166,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132693762,
			"link": null,
			"locked": false,
			"text": "0은 매우 자주 사용하기 때문에 x0 레지스터에 따로 저장해놓음\n쓰기는 무시됨",
			"rawText": "0은 매우 자주 사용하기 때문에 x0 레지스터에 따로 저장해놓음\n쓰기는 무시됨",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 34,
			"containerId": null,
			"originalText": "0은 매우 자주 사용하기 때문에 x0 레지스터에 따로 저장해놓음\n쓰기는 무시됨",
			"lineHeight": 1.25
		},
		{
			"id": "3mrlKz47",
			"type": "text",
			"x": 557.2011501148254,
			"y": -4986.439969340592,
			"width": 344.47991943359375,
			"height": 60,
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
			"seed": 477054518,
			"version": 203,
			"versionNonce": 1137136874,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132693762,
			"link": null,
			"locked": false,
			"text": "운영체제마다 데이터 타입이 차지하는 바이트가 다름\n\n그래서 혹시 모르니까 int64, int32같은 걸 쓴다",
			"rawText": "운영체제마다 데이터 타입이 차지하는 바이트가 다름\n\n그래서 혹시 모르니까 int64, int32같은 걸 쓴다",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 54,
			"containerId": null,
			"originalText": "운영체제마다 데이터 타입이 차지하는 바이트가 다름\n\n그래서 혹시 모르니까 int64, int32같은 걸 쓴다",
			"lineHeight": 1.25
		},
		{
			"id": "mod03kf9W95nlGiB-bK_6",
			"type": "freedraw",
			"x": -191.47267992182913,
			"y": -4564.429072749579,
			"width": 143.605573249666,
			"height": 0.45576410653575294,
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
			"seed": 119313450,
			"version": 47,
			"versionNonce": 1788946346,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132693762,
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
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				143.605573249666,
				0.45576410653575294
			]
		},
		{
			"id": "qPe1ZN0aVW7sQGPKksb-O",
			"type": "freedraw",
			"x": -526.131743478061,
			"y": -4431.556973722681,
			"width": 141.05088502090376,
			"height": 0.6045899127620942,
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
			"seed": 76365610,
			"version": 82,
			"versionNonce": 607298154,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132693762,
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
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				141.05088502090376,
				0.6045899127620942
			]
		},
		{
			"id": "4Vtnu8ggX-lw9LhtGnE-x",
			"type": "freedraw",
			"x": -135.8769944083599,
			"y": -4453.340094089592,
			"width": 35.908384861701734,
			"height": 1.667995272355256,
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
			"seed": 1248393322,
			"version": 40,
			"versionNonce": 1737396534,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132693762,
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
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				35.908384861701734,
				-1.667995272355256
			]
		},
		{
			"id": "2oM6KgZAbR_gfmuIc8jZr",
			"type": "freedraw",
			"x": -493.0167943231798,
			"y": -4410.871354126488,
			"width": 192.06420034592963,
			"height": 1.8199254856644984,
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
			"seed": 1141460522,
			"version": 162,
			"versionNonce": 189187370,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132693762,
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
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				192.06420034592963,
				-1.8199254856644984
			]
		},
		{
			"id": "gCgT3eXjvtS8RL0ifRbf_",
			"type": "freedraw",
			"x": 502.3476566947377,
			"y": -4621.903561349715,
			"width": 113.83897920103959,
			"height": 26.12674307729594,
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
			"seed": 1025475434,
			"version": 54,
			"versionNonce": 1163065974,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132693763,
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
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				12.175113112002691,
				4.166883773805239
			]
		},
		{
			"id": "gVHmbxhHN6PP8q3PAkVDM",
			"type": "freedraw",
			"x": 143.60189658243473,
			"y": -4505.249415592275,
			"width": 83.88951700184884,
			"height": 28.328006499686126,
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
			"seed": 443729834,
			"version": 59,
			"versionNonce": 692621290,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132693763,
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
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				2.8213488371735593,
				8.5507841760882
			]
		},
		{
			"id": "QrWLZRW9_J8LCuruXL9G7",
			"type": "freedraw",
			"x": 182.06189179920955,
			"y": -4393.977489181541,
			"width": 103.2202619067674,
			"height": 35.554906988541916,
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
			"seed": 1631076778,
			"version": 61,
			"versionNonce": 1496857526,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132693763,
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
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				13.61364759415494,
				-5.878261145140641
			]
		},
		{
			"id": "du0c5PB0TuLLmMIoV2su2",
			"type": "freedraw",
			"x": 377.22333521179144,
			"y": -4392.563736889266,
			"width": 111.61914240293913,
			"height": 0,
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
			"seed": 215505194,
			"version": 54,
			"versionNonce": 574816938,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132693763,
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
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				111.61914240293913,
				0
			]
		},
		{
			"id": "ndRNtoCU",
			"type": "text",
			"x": 285.4702754685278,
			"y": -4349.75507761727,
			"width": 264.55987548828125,
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
			"seed": 1980086314,
			"version": 46,
			"versionNonce": 1499682038,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132693763,
			"link": null,
			"locked": false,
			"text": "0.00000000000000000001 같은",
			"rawText": "0.00000000000000000001 같은",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 14,
			"containerId": null,
			"originalText": "0.00000000000000000001 같은",
			"lineHeight": 1.25
		},
		{
			"id": "1X7M9Inz",
			"type": "text",
			"x": -222.8977172210175,
			"y": -4002.485859423113,
			"width": 207.31195068359375,
			"height": 60,
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
			"seed": 1180564522,
			"version": 178,
			"versionNonce": 1625365866,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132693763,
			"link": null,
			"locked": false,
			"text": "컴퓨터는 2진수로 받아들이는데\n사람은 10진수 단위로 개발함\n-> 제조사는 소비자를 속이나요",
			"rawText": "컴퓨터는 2진수로 받아들이는데\n사람은 10진수 단위로 개발함\n-> 제조사는 소비자를 속이나요",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 54,
			"containerId": null,
			"originalText": "컴퓨터는 2진수로 받아들이는데\n사람은 10진수 단위로 개발함\n-> 제조사는 소비자를 속이나요",
			"lineHeight": 1.25
		},
		{
			"id": "4VOgBlziCOWhXNDWegpv4",
			"type": "freedraw",
			"x": 279.4161509888043,
			"y": -4198.741659399241,
			"width": 91.60012126098667,
			"height": 52.08915157964748,
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
			"seed": 192082422,
			"version": 146,
			"versionNonce": 1275006838,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132693763,
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
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				19.922917189348823,
				-20.102733999618067
			]
		},
		{
			"id": "1IxjYvaP89jR6jBMiIL8a",
			"type": "freedraw",
			"x": 129.99429860208198,
			"y": -3983.1302261947444,
			"width": 391.6839437972105,
			"height": 7.688873409556891,
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
			"seed": 681532842,
			"version": 115,
			"versionNonce": 1401964342,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132696483,
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
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				391.6839437972105,
				-1.0603009525102607
			]
		},
		{
			"id": "SGHShFMe",
			"type": "text",
			"x": 250.31395312272713,
			"y": -3917.712594671579,
			"width": 253.5519256591797,
			"height": 40,
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
			"seed": 1161637034,
			"version": 140,
			"versionNonce": 1807899318,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710132716234,
			"link": null,
			"locked": false,
			"text": "무엇보다 연산이 몹시 힘들어짐\n-> 아하 컴퓨터는 연산하는 기계구나~",
			"rawText": "무엇보다 연산이 몹시 힘들어짐\n-> 아하 컴퓨터는 연산하는 기계구나~",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 34,
			"containerId": null,
			"originalText": "무엇보다 연산이 몹시 힘들어짐\n-> 아하 컴퓨터는 연산하는 기계구나~",
			"lineHeight": 1.25
		},
		{
			"id": "qUHj4Lip",
			"type": "text",
			"x": -979.3630896417675,
			"y": -6354.651234894422,
			"width": 8,
			"height": 20,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 2128424554,
			"version": 11,
			"versionNonce": 1539816298,
			"isDeleted": true,
			"boundElements": null,
			"updated": 1710132693761,
			"link": null,
			"locked": false,
			"text": "",
			"rawText": "",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "center",
			"verticalAlign": "middle",
			"baseline": 14,
			"containerId": "kO9Ks88i2gHQAOdawIke0",
			"originalText": "",
			"lineHeight": 1.25
		},
		{
			"id": "O77IIQiy",
			"type": "text",
			"x": -977.9883945052708,
			"y": -6315.187826321599,
			"width": 8,
			"height": 20,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 273142122,
			"version": 11,
			"versionNonce": 1915979830,
			"isDeleted": true,
			"boundElements": null,
			"updated": 1710132693761,
			"link": null,
			"locked": false,
			"text": "",
			"rawText": "",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "center",
			"verticalAlign": "middle",
			"baseline": 14,
			"containerId": "ZSICSDk-Jt2MLZnxwa0Y4",
			"originalText": "",
			"lineHeight": 1.25
		},
		{
			"id": "82T97rym",
			"type": "text",
			"x": -1019.1722170630923,
			"y": -6300.031167356192,
			"width": 8,
			"height": 20,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 705836790,
			"version": 11,
			"versionNonce": 497657462,
			"isDeleted": true,
			"boundElements": null,
			"updated": 1710132693762,
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
		},
		{
			"id": "P87k2KyQ",
			"type": "text",
			"x": 626.7270531447332,
			"y": -6434.749566062263,
			"width": 8,
			"height": 20,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 573661110,
			"version": 10,
			"versionNonce": 1238984630,
			"isDeleted": true,
			"boundElements": null,
			"updated": 1710132693762,
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
		},
		{
			"id": "1g4pJe8HfR4gamq6PJwWK",
			"type": "freedraw",
			"x": 321.9037827283453,
			"y": -6419.964124194548,
			"width": 94.65713970252943,
			"height": 2.3097584699326035,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 754056234,
			"version": 67,
			"versionNonce": 1754961578,
			"isDeleted": true,
			"boundElements": null,
			"updated": 1710132693762,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.35034693268295314,
					-0.3534513397662522
				],
				[
					3.2802173507920998,
					-0.3534513397662522
				],
				[
					4.904803990773132,
					-0.3534513397662522
				],
				[
					8.01133374528058,
					-0.3534513397662522
				],
				[
					9.493329926594697,
					-0.6386853238882395
				],
				[
					10.194023791960547,
					-0.6386853238882395
				],
				[
					11.006317111951091,
					-0.6386853238882395
				],
				[
					12.05730484321208,
					-0.8153977270740143
				],
				[
					14.32060334047452,
					-0.8153977270740143
				],
				[
					16.090911379599333,
					-1.029309948467926
				],
				[
					17.368228960586578,
					-1.029309948467926
				],
				[
					19.138536999711448,
					-1.3145439325899133
				],
				[
					20.127542722887995,
					-1.5284826873776183
				],
				[
					21.17858352093674,
					-1.7051950905643025
				],
				[
					22.45595416871174,
					-1.7051950905643025
				],
				[
					24.226262207836555,
					-1.7051950905643025
				],
				[
					25.215267931013102,
					-1.8819074937500773
				],
				[
					28.117172151981435,
					-2.3097584699326035
				],
				[
					28.641153614161226,
					-2.3097584699326035
				],
				[
					29.91847119514847,
					-2.3097584699326035
				],
				[
					31.68877923427334,
					-2.3097584699326035
				],
				[
					34.09779913067956,
					-2.3097584699326035
				],
				[
					36.36104456115419,
					-2.3097584699326035
				],
				[
					38.13135260027906,
					-2.3097584699326035
				],
				[
					39.90166063940387,
					-2.3097584699326035
				],
				[
					42.33854059937545,
					-2.3097584699326035
				],
				[
					44.313474172039435,
					-2.3097584699326035
				],
				[
					46.08378221116425,
					-2.3097584699326035
				],
				[
					47.565725325690664,
					-2.3097584699326035
				],
				[
					49.33603336481548,
					-2.3097584699326035
				],
				[
					50.03672723018133,
					-2.3097584699326035
				],
				[
					52.157382201989094,
					-2.3097584699326035
				],
				[
					53.92769024111391,
					-2.3097584699326035
				],
				[
					57.17686352107603,
					-2.3097584699326035
				],
				[
					58.94717156020084,
					-2.3097584699326035
				],
				[
					60.28652421606034,
					-2.3097584699326035
				],
				[
					62.05683225518516,
					-2.3097584699326035
				],
				[
					63.33420290296016,
					-2.3097584699326035
				],
				[
					65.59744833343484,
					-2.3097584699326035
				],
				[
					66.87476591442208,
					-2.3097584699326035
				],
				[
					69.77672320217812,
					-2.3097584699326035
				],
				[
					70.76572892535467,
					-2.3097584699326035
				],
				[
					71.46642279072051,
					-2.3097584699326035
				],
				[
					74.22265867933277,
					-2.3097584699326035
				],
				[
					78.11049074978848,
					-2.3097584699326035
				],
				[
					81.3596640297506,
					-2.3097584699326035
				],
				[
					85.59476515920011,
					-2.3097584699326035
				],
				[
					87.36507319832498,
					-2.3097584699326035
				],
				[
					89.5136413004858,
					-2.3097584699326035
				],
				[
					89.86085729269189,
					-2.3097584699326035
				],
				[
					90.56155115805768,
					-2.3097584699326035
				],
				[
					91.83886873904498,
					-2.3097584699326035
				],
				[
					93.3208649203591,
					-2.3097584699326035
				],
				[
					94.30987064353565,
					-2.3097584699326035
				],
				[
					94.65713970252943,
					-2.3097584699326035
				],
				[
					94.65713970252943,
					-2.3097584699326035
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				94.65713970252943,
				-2.3097584699326035
			]
		},
		{
			"id": "1QBxPEjM0tWk7IJUx1HMH",
			"type": "freedraw",
			"x": 162.95145366360777,
			"y": -6266.090154049897,
			"width": 26.27246447644012,
			"height": 16.89076053786357,
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
			"seed": 384576426,
			"version": 99,
			"versionNonce": 522596714,
			"isDeleted": true,
			"boundElements": null,
			"updated": 1710132693762,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.17363452949689417,
					0.17360799610287359
				],
				[
					-0.17984334366286703,
					0.6975894582819819
				],
				[
					-0.356555746848926,
					0.871197454385765
				],
				[
					-0.8866929564069892,
					1.2184399799853054
				],
				[
					-1.8819074937495088,
					1.392047976088179
				],
				[
					-2.588810173281331,
					1.5656825055857553
				],
				[
					-3.5840247106239076,
					2.1268372525792074
				],
				[
					-4.867551105777125,
					2.3376716002849207
				],
				[
					-5.686053239933642,
					2.5485059479897245
				],
				[
					-6.569668322651523,
					2.5485059479897245
				],
				[
					-7.0998055322095865,
					2.722113944092598
				],
				[
					-8.095020069552106,
					2.722113944092598
				],
				[
					-9.443712480054444,
					2.722113944092598
				],
				[
					-9.973849689612507,
					2.8957219401954717
				],
				[
					-10.150562092798566,
					2.8957219401954717
				],
				[
					-10.327274495984568,
					2.8957219401954717
				],
				[
					-10.68075236914433,
					2.8957219401954717
				],
				[
					-12.029391712858967,
					2.8957219401954717
				],
				[
					-13.024606250201487,
					2.8957219401954717
				],
				[
					-13.731508929733309,
					2.8957219401954717
				],
				[
					-15.861450589396213,
					2.8957219401954717
				],
				[
					-16.856665126738733,
					2.719009537009697
				],
				[
					-18.351025869597095,
					1.8664119917275457
				],
				[
					-19.057928549128974,
					1.689699588541771
				],
				[
					-19.588065758687037,
					1.512960651962203
				],
				[
					-19.94149056505904,
					1.3362482487764282
				],
				[
					-20.29496843821886,
					1.159535845589744
				],
				[
					-20.64839324459092,
					0.8060845058244013
				],
				[
					-21.677729726452526,
					-0.22322544264352473
				],
				[
					-22.031154532824587,
					-0.7533891855955517
				],
				[
					-22.20786693601059,
					-0.9301015887813264
				],
				[
					-22.5985446273786,
					-1.9253161261240166
				],
				[
					-22.77525703056466,
					-2.4554798690760435
				],
				[
					-22.77525703056466,
					-2.8089312088422957
				],
				[
					-22.77525703056466,
					-3.804145746184986
				],
				[
					-22.77525703056466,
					-4.511021892322788
				],
				[
					-22.77525703056466,
					-5.3295240264787935
				],
				[
					-22.77525703056466,
					-5.8596877694308205
				],
				[
					-22.77525703056466,
					-6.389851512382847
				],
				[
					-22.217153623865727,
					-7.561778452911312
				],
				[
					-21.578494833372076,
					-8.631392626670277
				],
				[
					-20.98011373477584,
					-9.449894760827192
				],
				[
					-20.381785702967306,
					-10.445109298169882
				],
				[
					-20.034516643973518,
					-10.975273041121
				],
				[
					-19.222223323982973,
					-11.403124017303526
				],
				[
					-18.698294928590883,
					-11.756575357069778
				],
				[
					-18.174313466411093,
					-12.110000163442237
				],
				[
					-17.188385616923654,
					-12.500651321415717
				],
				[
					-16.841169624717622,
					-12.677363724602401
				],
				[
					-16.20245776743627,
					-12.891302479390106
				],
				[
					-14.720514652909856,
					-13.176536463512093
				],
				[
					-14.081855862416262,
					-13.390448684906005
				],
				[
					-13.207527467553518,
					-13.390448684906005
				],
				[
					-12.683546005373671,
					-13.390448684906005
				],
				[
					-12.509964542664534,
					-13.567187621485573
				],
				[
					-11.985983080484743,
					-13.567187621485573
				],
				[
					-10.823342827811302,
					-13.995038597668099
				],
				[
					-10.47299589512835,
					-13.995038597668099
				],
				[
					-9.660702575137861,
					-13.995038597668099
				],
				[
					-9.136774179745771,
					-13.995038597668099
				],
				[
					-8.789505120751983,
					-13.995038597668099
				],
				[
					-8.150846330258332,
					-13.995038597668099
				],
				[
					-7.977211800761438,
					-13.995038597668099
				],
				[
					-7.164918480770893,
					-13.995038597668099
				],
				[
					-6.175912757594347,
					-13.610596253860422
				],
				[
					-4.343622710385091,
					-12.699068040788916
				],
				[
					-3.9188761412856934,
					-12.060409250295379
				],
				[
					-3.218182275919844,
					-11.713166724695839
				],
				[
					-2.5174884105539945,
					-11.012472859330046
				],
				[
					-1.9191073119577595,
					-10.200179539338933
				],
				[
					0.2294077234153633,
					-9.204965001996243
				],
				[
					1.041701043405908,
					-8.820522658188565
				],
				[
					1.4664476125053056,
					-8.181863867695029
				],
				[
					1.6400821420021998,
					-8.008229338198362
				],
				[
					2.5516103550731373,
					-6.1759127575951425
				],
				[
					2.7252448845700314,
					-5.651957828808918
				],
				[
					2.8988263472791687,
					-5.304715303208468
				],
				[
					3.3235729163785663,
					-4.31570958003249
				],
				[
					3.4972074458754605,
					-4.142075050535823
				],
				[
					3.4972074458754605,
					-3.9684670544320397
				],
				[
					3.3204950426894584,
					-3.6212245288324993
				],
				[
					2.9298173513214465,
					-2.9825392049451693
				],
				[
					1.757890410792868,
					-2.6352966793447195
				],
				[
					0.9393882766363504,
					-2.424488865033709
				],
				[
					0.23253866389222821,
					-2.424488865033709
				],
				[
					-1.255666331587861,
					-1.968724758497956
				],
				[
					-2.2508808689304374,
					-1.5842824146902785
				],
				[
					-2.4275932721164395,
					-1.2339354820069275
				],
				[
					-2.4275932721164395,
					-1.2339354820069275
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				-2.4275932721164395,
				-1.2339354820069275
			]
		},
		{
			"id": "76_jDDRR_sFR4DJeHCn2G",
			"type": "freedraw",
			"x": 700.5972422198732,
			"y": -6424.509254764691,
			"width": 0.0001,
			"height": 0.0001,
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
			"seed": 190455798,
			"version": 10,
			"versionNonce": 519074858,
			"isDeleted": true,
			"boundElements": null,
			"updated": 1710132693762,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.0001,
					0.0001
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				0.0001,
				0.0001
			]
		},
		{
			"id": "Y1Z45Q9jC1Fz3cizURmVX",
			"type": "freedraw",
			"x": -370.5896453940872,
			"y": -5457.795947183728,
			"width": 167.26439229616074,
			"height": 0.9269971816984253,
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
			"seed": 346606762,
			"version": 47,
			"versionNonce": 138940202,
			"isDeleted": true,
			"boundElements": null,
			"updated": 1710132693762,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.9748805058762287,
					0
				],
				[
					4.731116394488481,
					0.604563379368301
				],
				[
					7.980289674450546,
					0.9269971816984253
				],
				[
					12.361112203043888,
					0.9269971816984253
				],
				[
					15.11734809165614,
					0.9269971816984253
				],
				[
					18.859458762968075,
					0.9269971816984253
				],
				[
					21.122704193442758,
					0.9269971816984253
				],
				[
					26.982391962873294,
					0.9269971816984253
				],
				[
					31.710430483672667,
					0.9269971816984253
				],
				[
					36.93145946260961,
					0.9269971816984253
				],
				[
					42.15248844154655,
					0.9269971816984253
				],
				[
					47.37346435369574,
					0.9269971816984253
				],
				[
					55.20500782210115,
					0.9269971816984253
				],
				[
					59.4400558847629,
					0.9269971816984253
				],
				[
					62.68922916472502,
					0.9269971816984253
				],
				[
					65.93845551147484,
					0.9269971816984253
				],
				[
					70.812215431418,
					0.9269971816984253
				],
				[
					74.06138871138012,
					0.9269971816984253
				],
				[
					77.80349938269205,
					0.9269971816984253
				],
				[
					82.03860051214156,
					0.9269971816984253
				],
				[
					86.27370164159106,
					0.9269971816984253
				],
				[
					94.10519204320872,
					0.9269971816984253
				],
				[
					99.32622102214566,
					0.9269971816984253
				],
				[
					104.05425954294503,
					0.9269971816984253
				],
				[
					109.27528852188198,
					0.9269971816984253
				],
				[
					117.10677892349963,
					0.9269971816984253
				],
				[
					122.82074529378639,
					0.9269971816984253
				],
				[
					129.027649055423,
					0.9269971816984253
				],
				[
					135.23455281705964,
					0.9269971816984253
				],
				[
					144.5449615263023,
					0.9269971816984253
				],
				[
					149.76599050523924,
					0.9269971816984253
				],
				[
					154.49402902603862,
					0.9269971816984253
				],
				[
					158.72913015548812,
					0.9269971816984253
				],
				[
					163.60289007543128,
					0.9269971816984253
				],
				[
					165.5778236480952,
					0.9269971816984253
				],
				[
					166.56682937127175,
					0.9269971816984253
				],
				[
					166.91404536347784,
					0.9269971816984253
				],
				[
					167.26439229616074,
					0.9269971816984253
				],
				[
					167.26439229616074,
					0.9269971816984253
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				167.26439229616074,
				0.9269971816984253
			]
		},
		{
			"id": "nTMN-tLt-CUK38RmKftTF",
			"type": "freedraw",
			"x": -189.59692817545783,
			"y": -4562.559556350767,
			"width": 141.7515788862695,
			"height": 1.804403450250902,
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
			"seed": 307396266,
			"version": 50,
			"versionNonce": 1052001974,
			"isDeleted": true,
			"boundElements": null,
			"updated": 1710132693762,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.4819431145263025,
					-0.17671240318668424
				],
				[
					3.1065297545073918,
					-0.5022506125997097
				],
				[
					8.473280132588116,
					-0.8277888220118257
				],
				[
					12.361112203043831,
					-1.1533270314248512
				],
				[
					13.843108384357947,
					-1.1533270314248512
				],
				[
					16.106353814832687,
					-1.4788652408378766
				],
				[
					19.355527094794752,
					-1.804403450250902
				],
				[
					22.111762983406948,
					-1.804403450250902
				],
				[
					26.985522903350102,
					-1.804403450250902
				],
				[
					30.727633574662036,
					-1.804403450250902
				],
				[
					33.976806854624215,
					-1.804403450250902
				],
				[
					37.71897059272385,
					-1.804403450250902
				],
				[
					40.968143872685914,
					-1.804403450250902
				],
				[
					44.363038551791874,
					-1.804403450250902
				],
				[
					47.61221183175394,
					-1.804403450250902
				],
				[
					51.84731296120344,
					-1.804403450250902
				],
				[
					56.082361023865246,
					-1.804403450250902
				],
				[
					60.9561209438084,
					-1.804403450250902
				],
				[
					65.1912751400456,
					-1.804403450250902
				],
				[
					69.42632320270741,
					-1.804403450250902
				],
				[
					73.66147739894461,
					-1.804403450250902
				],
				[
					75.92466976263154,
					-1.804403450250902
				],
				[
					80.79842968257469,
					-1.804403450250902
				],
				[
					84.04760296253687,
					-1.804403450250902
				],
				[
					86.80389191793688,
					-1.804403450250902
				],
				[
					90.05306519789895,
					-1.804403450250902
				],
				[
					93.30223847786101,
					-1.804403450250902
				],
				[
					97.6830079396666,
					-1.804403450250902
				],
				[
					100.93218121962866,
					-1.804403450250902
				],
				[
					104.18135449959084,
					-1.804403450250902
				],
				[
					107.4305277795529,
					-1.804403450250902
				],
				[
					112.30428769949606,
					-1.804403450250902
				],
				[
					115.55346097945812,
					-1.804403450250902
				],
				[
					118.80263425942019,
					-1.804403450250902
				],
				[
					123.0377884556575,
					-1.804403450250902
				],
				[
					126.28696173561957,
					-1.804403450250902
				],
				[
					131.16072165556272,
					-1.804403450250902
				],
				[
					134.4098949355248,
					-1.1595358455906535
				],
				[
					137.65906821548697,
					-1.1595358455906535
				],
				[
					140.76559796999436,
					-0.6634675137638624
				],
				[
					141.5779443567726,
					-0.6634675137638624
				],
				[
					141.7515788862695,
					-0.6634675137638624
				],
				[
					141.7515788862695,
					-0.6634675137638624
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				141.7515788862695,
				-0.6634675137638624
			]
		},
		{
			"id": "fh1EyHN_f-cZdvt8nGo3n",
			"type": "freedraw",
			"x": -522.873230443456,
			"y": -4427.9574535100355,
			"width": 164.061705522262,
			"height": 6.123217437364474,
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
			"seed": 1523358314,
			"version": 40,
			"versionNonce": 1764098038,
			"isDeleted": true,
			"boundElements": null,
			"updated": 1710132693762,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.1315961818435198,
					0
				],
				[
					6.991283951273999,
					0
				],
				[
					10.733447689373747,
					0
				],
				[
					12.996693119848373,
					0
				],
				[
					16.738803791160308,
					0
				],
				[
					24.57034725956572,
					0.7441024977397319
				],
				[
					29.791323171714907,
					1.4881784620865801
				],
				[
					35.50528954200166,
					1.8757252129771587
				],
				[
					42.20518376177586,
					2.2632719638686467
				],
				[
					48.90507798155005,
					2.6508187147592253
				],
				[
					57.722496232655146,
					3.4259122165422013
				],
				[
					62.94347214480433,
					3.4259122165422013
				],
				[
					68.16450112374127,
					3.797936932018274
				],
				[
					73.38547703589046,
					3.797936932018274
				],
				[
					82.20289528699556,
					4.573030433800341
				],
				[
					88.40985211541994,
					5.348123935582407
				],
				[
					95.60268372654394,
					5.348123935582407
				],
				[
					101.80958748818057,
					5.735670686473895
				],
				[
					108.01654431660495,
					6.123217437364474
				],
				[
					113.23752022875414,
					6.123217437364474
				],
				[
					122.05493847985923,
					6.123217437364474
				],
				[
					127.27596745879617,
					6.123217437364474
				],
				[
					132.0040059795955,
					6.123217437364474
				],
				[
					136.23910710904505,
					6.123217437364474
				],
				[
					141.60580442033802,
					6.123217437364474
				],
				[
					144.85497770030008,
					6.123217437364474
				],
				[
					148.1041509802622,
					6.123217437364474
				],
				[
					151.35337732701203,
					6.123217437364474
				],
				[
					155.09548799832396,
					6.123217437364474
				],
				[
					159.96924791826711,
					6.123217437364474
				],
				[
					162.2324933487418,
					6.123217437364474
				],
				[
					163.7144895300559,
					5.946505034178699
				],
				[
					164.061705522262,
					5.946505034178699
				],
				[
					164.061705522262,
					5.946505034178699
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				164.061705522262,
				5.946505034178699
			]
		},
		{
			"id": "Z1rbuXY3oJrexfibjnFIG",
			"type": "freedraw",
			"x": 280.50439160506136,
			"y": -4196.608600065799,
			"width": 114.8156734294596,
			"height": 49.84759719866361,
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
			"seed": 616509098,
			"version": 89,
			"versionNonce": 1868121654,
			"isDeleted": true,
			"boundElements": null,
			"updated": 1710132693763,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.35342480637211793,
					0.3503336659859997
				],
				[
					-0.9580147191343258,
					1.1626269859771128
				],
				[
					-3.869258694745554,
					2.232254426432519
				],
				[
					-7.1246407888736485,
					3.2181690092229474
				],
				[
					-12.351825515188807,
					3.956049426100435
				],
				[
					-21.5195906989768,
					4.362196086095537
				],
				[
					-37.73138822105591,
					4.362196086095537
				],
				[
					-49.85380601282935,
					3.9281495624445597
				],
				[
					-60.9902959551153,
					1.3548481578809515
				],
				[
					-69.66507068076572,
					-1.5346782348460692
				],
				[
					-76.06731328808632,
					-5.521745198382632
				],
				[
					-80.32411873372297,
					-10.783051869216251
				],
				[
					-81.30075989535527,
					-14.038433963344687
				],
				[
					-81.65418470172733,
					-17.78676671551966
				],
				[
					-81.33175089939749,
					-21.042148809647188
				],
				[
					-80.11949320018385,
					-23.804566979031733
				],
				[
					-76.40837353291414,
					-28.473714632133124
				],
				[
					-71.06645841149742,
					-31.13382003474817
				],
				[
					-63.87362680037336,
					-32.33366010562986
				],
				[
					-55.20500782210121,
					-32.74291117270786
				],
				[
					-40.48141529550219,
					-32.74291117270786
				],
				[
					-30.337008950081895,
					-31.899613581977974
				],
				[
					-19.206727821961863,
					-29.332507724883726
				],
				[
					-8.076446693841945,
					-25.909713182121777
				],
				[
					2.1330195333520123,
					-22.080771979364727
				],
				[
					12.21539080390005,
					-16.09397598659143
				],
				[
					15.052235143094777,
					-12.931606704680235
				],
				[
					15.938928099501709,
					-10.17538408276505
				],
				[
					15.585503293129705,
					-5.940296220012897
				],
				[
					11.142698756451978,
					0.279025169956185
				],
				[
					4.256805445636587,
					4.2970964042315245
				],
				[
					-6.458068868026885,
					8.141533109010197
				],
				[
					-20.05935190063758,
					9.89324123903043
				],
				[
					-36.12229708309599,
					10.33658771723367
				],
				[
					-59.72842080936141,
					8.110542104967863
				],
				[
					-73.32970384197205,
					4.160674959639437
				],
				[
					-83.06485912031411,
					-0.06511294856045424
				],
				[
					-88.58040877122778,
					-4.387018076062304
				],
				[
					-90.78167219361796,
					-8.749227428854283
				],
				[
					-89.62210981463363,
					-17.08299497646476
				],
				[
					-84.29569019523802,
					-23.615450214210796
				],
				[
					-74.92950829207689,
					-29.571241936245315
				],
				[
					-61.334434073632224,
					-33.51490026740703
				],
				[
					-34.789153241402516,
					-37.117511620437654
				],
				[
					-16.763639047824313,
					-37.570171319890505
				],
				[
					-0.7069026795318223,
					-34.90075269602676
				],
				[
					11.468210432470869,
					-30.123109995383857
				],
				[
					18.90286739534224,
					-24.762581698166287
				],
				[
					23.646454484950482,
					-15.653720648773742
				],
				[
					24.03400123584163,
					-8.953839695695933
				],
				[
					20.75999269921556,
					-1.1843445688600696
				],
				[
					9.921154369383203,
					7.967925112906414
				],
				[
					-1.215335572902859,
					10.953568724934485
				],
				[
					-16.29548384635075,
					12.277425878773101
				],
				[
					-34.327206854094925,
					10.919460047111897
				],
				[
					-51.86593940370153,
					7.3199398344668225
				],
				[
					-70.28207822185999,
					-1.416869966055856
				],
				[
					-75.4968983866309,
					-7.000623705916041
				],
				[
					-77.06258089221666,
					-13.70670020646321
				],
				[
					-75.50305413400918,
					-20.41277670700947
				],
				[
					-65.07033593077819,
					-29.558837574610152
				],
				[
					-52.4611895618209,
					-33.47459604211599
				],
				[
					-35.41852534404103,
					-35.26969953781372
				],
				[
					-17.393011150462826,
					-35.72235923726657
				],
				[
					-1.3362747821703351,
					-33.496300358302506
				],
				[
					13.61370066094264,
					-25.86321340936138
				],
				[
					17.56043686579369,
					-19.96322141463952
				],
				[
					18.335530367575984,
					-13.756304386305601
				],
				[
					14.680183894224683,
					-6.479759917516276
				],
				[
					1.0665363000698562,
					1.984220260519578
				],
				[
					-13.027737190678408,
					5.059785544378428
				],
				[
					-30.569547613974123,
					6.402242607320659
				],
				[
					-49.58714540441798,
					5.493832068030315
				],
				[
					-72.69725386564443,
					0.17360799610378308
				],
				[
					-81.03723022742082,
					-3.9684670544320397
				],
				[
					-84.71115007648228,
					-10.56913964782234
				],
				[
					-83.54850982380884,
					-16.78225222362471
				],
				[
					-81.61077606935311,
					-19.501275027331758
				],
				[
					-47.34868216381955,
					-32.29955142780727
				],
				[
					-30.799008404177243,
					-33.642008490749504
				],
				[
					-22.769048216398687,
					-33.642008490749504
				],
				[
					-6.7091809076293885,
					-31.862400497072485
				],
				[
					12.943997799618955,
					-27.943550889181097
				],
				[
					20.136829410743076,
					-25.57797942523939
				],
				[
					20.136829410743076,
					-25.57797942523939
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				20.136829410743076,
				-25.57797942523939
			]
		},
		{
			"id": "y1I2iQKWfSDliJeZ0jzyg",
			"type": "freedraw",
			"x": 277.74815571644905,
			"y": -4197.26588529879,
			"width": 88.23006183854483,
			"height": 48.52684445190789,
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
			"seed": 520298038,
			"version": 75,
			"versionNonce": 1114497066,
			"isDeleted": true,
			"boundElements": null,
			"updated": 1710132693763,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					2.2632719638686467
				],
				[
					0,
					3.887858603849054
				],
				[
					-1.698986276397477,
					6.7835938107427864
				],
				[
					-4.610230252008705,
					8.178746193913867
				],
				[
					-8.358549737486555,
					9.177065138339458
				],
				[
					-11.61393183161465,
					9.527412071022809
				],
				[
					-17.827044407417304,
					9.527412071022809
				],
				[
					-31.08418932151102,
					9.108861049392544
				],
				[
					-40.741814022959716,
					7.0037148463025005
				],
				[
					-49.9065013330586,
					4.498630797384067
				],
				[
					-57.598479149698505,
					1.6710996794381572
				],
				[
					-61.23827705424088,
					-1.3703569265990154
				],
				[
					-61.84907578116912,
					-4.132775095983561
				],
				[
					-61.84907578116912,
					-7.388157190111087
				],
				[
					-61.84907578116912,
					-9.657624701449095
				],
				[
					-61.84907578116912,
					-13.405957453624069
				],
				[
					-61.56691967073664,
					-16.317188162537605
				],
				[
					-60.56862725970501,
					-20.06552091471258
				],
				[
					-57.66666997194898,
					-24.074292194436566
				],
				[
					-55.118190557352705,
					-28.436501547228545
				],
				[
					-50.19173531718019,
					-32.69329372616812
				],
				[
					-47.928436819917806,
					-33.23275742367241
				],
				[
					-42.707460907768564,
					-33.9768466547157
				],
				[
					-35.51462929664456,
					-34.37678450054409
				],
				[
					-26.846010318372407,
					-34.37678450054409
				],
				[
					-10.643499484148379,
					-34.37678450054409
				],
				[
					0.48678164397165347,
					-34.37678450054409
				],
				[
					11.124125380741702,
					-34.37678450054409
				],
				[
					20.28568175036378,
					-34.37678450054409
				],
				[
					23.84487120432368,
					-33.07154052250735
				],
				[
					25.46637997061555,
					-29.822353975848273
				],
				[
					25.46637997061555,
					-27.559095278676978
				],
				[
					25.46637997061555,
					-25.295836581504773
				],
				[
					25.46637997061555,
					-20.56778479400873
				],
				[
					22.38771027967357,
					-12.137913293794554
				],
				[
					19.3400315927737,
					-7.183531656572086
				],
				[
					14.289559269644542,
					-2.9174395230802475
				],
				[
					7.490483223577598,
					0.675885142095467
				],
				[
					0.29144279828756225,
					3.069356469693048
				],
				[
					-11.982905206795635,
					4.687747562205004
				],
				[
					-20.167820414785297,
					5.093894222200106
				],
				[
					-26.873923448725463,
					5.093894222200106
				],
				[
					-34.71470053819826,
					4.740456149131205
				],
				[
					-38.46307309046392,
					3.056952108057885
				],
				[
					-41.644002481387815,
					-0.12401708295692515
				],
				[
					-44.55216858330988,
					-4.132775095983561
				],
				[
					-47.128561128259264,
					-11.480628060802701
				],
				[
					-48.29741019509868,
					-17.693753903302422
				],
				[
					-48.68803481967893,
					-23.906879745802144
				],
				[
					-48.68803481967893,
					-29.627041663557975
				],
				[
					-48.68803481967893,
					-34.36128899852338
				],
				[
					-47.3641776658406,
					-37.64457095630769
				],
				[
					-44.607994844016105,
					-38.25534314984179
				],
				[
					-41.35876849726628,
					-38.60878122291069
				],
				[
					-36.13779258511704,
					-38.99943238088508
				],
				[
					-27.46917360684489,
					-38.99943238088508
				],
				[
					-10.773725381271106,
					-38.99943238088508
				],
				[
					0.356555746848926,
					-38.571581404702556
				],
				[
					9.025174725121133,
					-36.925290448534724
				],
				[
					15.337469127216423,
					-34.1783677811718
				],
				[
					19.814395608413292,
					-30.823777327356765
				],
				[
					24.421547986732776,
					-22.781439311336726
				],
				[
					25.99343930648456,
					-16.081558358259826
				],
				[
					26.380986057375708,
					-10.367605254669797
				],
				[
					26.380986057375708,
					-5.146589542429865
				],
				[
					24.322313093652383,
					1.206048885047494
				],
				[
					21.718007418349885,
					3.8041457461840764
				],
				[
					18.95561578235936,
					5.341928388113047
				],
				[
					17.467463853667027,
					5.90618754219031
				],
				[
					17.11398598050721,
					5.90618754219031
				],
				[
					17.11398598050721,
					5.90618754219031
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				17.11398598050721,
				5.90618754219031
			]
		},
		{
			"id": "QLl91YN7s60vFwEQMn-jK",
			"type": "freedraw",
			"x": 133.9193835575337,
			"y": -3977.282929520252,
			"width": 377.47186203767143,
			"height": 6.017800263512527,
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
			"seed": 1946400566,
			"version": 84,
			"versionNonce": 1121209066,
			"isDeleted": true,
			"boundElements": null,
			"updated": 1710132693763,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.0509877312609888,
					-0.3534513397662522
				],
				[
					3.807223619873298,
					-0.6386853238877848
				],
				[
					5.577531658998112,
					-0.9239193080093173
				],
				[
					8.333767547610364,
					-0.9239193080093173
				],
				[
					10.104075586735178,
					-0.9239193080093173
				],
				[
					11.874383625860048,
					-0.9239193080093173
				],
				[
					14.776287846828325,
					-0.9239193080093173
				],
				[
					16.258284028142498,
					-0.9239193080093173
				],
				[
					19.507457308104563,
					-0.9239193080093173
				],
				[
					23.888279836697905,
					-0.9239193080093173
				],
				[
					26.6444626585224,
					-0.9239193080093173
				],
				[
					30.38662639662209,
					-0.9239193080093173
				],
				[
					34.128737067934026,
					-0.9239193080093173
				],
				[
					36.88497295654628,
					-0.9239193080093173
				],
				[
					41.75873287648943,
					-0.25113857299675146
				],
				[
					43.529040915614246,
					-0.25113857299675146
				],
				[
					46.2852768042265,
					0.35342480637200424
				],
				[
					49.53445008418862,
					0.9983189444251366
				],
				[
					53.276560755500554,
					1.3486393437142397
				],
				[
					59.13624852493109,
					1.698986276397136
				],
				[
					62.878359196243025,
					2.0493332090800322
				],
				[
					67.11346032569253,
					2.3996801417629285
				],
				[
					70.85562406379222,
					2.7500005410520316
				],
				[
					76.71531183322281,
					3.7762326158308497
				],
				[
					79.96448511318488,
					3.7762326158308497
				],
				[
					83.70659578449681,
					3.7762326158308497
				],
				[
					86.95576906445893,
					4.421100220490189
				],
				[
					92.32251944253966,
					4.421100220490189
				],
				[
					96.06463011385159,
					4.77144715317354
				],
				[
					99.31380339381371,
					5.093880955503209
				],
				[
					103.05596713191335,
					5.093880955503209
				],
				[
					107.43673659371893,
					5.093880955503209
				],
				[
					111.17890033181862,
					5.093880955503209
				],
				[
					114.92101100313056,
					5.093880955503209
				],
				[
					117.18430950039294,
					5.093880955503209
				],
				[
					121.41935756305475,
					5.093880955503209
				],
				[
					129.25090103146016,
					5.093880955503209
				],
				[
					134.96486740174697,
					5.093880955503209
				],
				[
					140.1858433138961,
					5.093880955503209
				],
				[
					146.39280014232048,
					5.093880955503209
				],
				[
					152.59970390395705,
					5.093880955503209
				],
				[
					162.40305000454958,
					5.093880955503209
				],
				[
					168.60995376618627,
					5.093880955503209
				],
				[
					174.81685752782283,
					5.093880955503209
				],
				[
					180.53082389810965,
					5.093880955503209
				],
				[
					186.24479026839634,
					5.093880955503209
				],
				[
					194.07633373680181,
					5.093880955503209
				],
				[
					198.31143486625132,
					5.093880955503209
				],
				[
					203.0394733870507,
					5.093880955503209
				],
				[
					207.2745745165002,
					5.093880955503209
				],
				[
					213.62719967728054,
					5.093880955503209
				],
				[
					218.8481755894298,
					5.093880955503209
				],
				[
					225.05513241785417,
					5.093880955503209
				],
				[
					231.7549735708406,
					5.093880955503209
				],
				[
					242.0513101295707,
					5.093880955503209
				],
				[
					250.23001652339434,
					5.093880955503209
				],
				[
					258.4087759840059,
					5.093880955503209
				],
				[
					266.58753544461734,
					5.093880955503209
				],
				[
					274.7662949052288,
					5.093880955503209
				],
				[
					287.03438102935826,
					5.093880955503209
				],
				[
					294.72025616540753,
					5.093880955503209
				],
				[
					300.9271599270442,
					5.093880955503209
				],
				[
					306.6410732305432,
					5.093880955503209
				],
				[
					314.47256363216087,
					5.093880955503209
				],
				[
					319.20060215296024,
					5.093880955503209
				],
				[
					319.72458361514003,
					5.093880955503209
				],
				[
					320.5369300019183,
					5.093880955503209
				],
				[
					323.2931128237428,
					5.093880955503209
				],
				[
					328.6598632018236,
					4.10177082524342
				],
				[
					332.8949112644853,
					3.7266151692906533
				],
				[
					340.5806802669592,
					3.317390635605989
				],
				[
					349.73915876289203,
					2.8988263472788276
				],
				[
					358.40783080795205,
					2.4895752802008246
				],
				[
					369.1970516912442,
					1.289735209319133
				],
				[
					374.41808067018115,
					0.9146060867597043
				],
				[
					375.90002378470746,
					0.7378671501801364
				],
				[
					376.42400524688736,
					0.5611547469939069
				],
				[
					376.77435217957026,
					0.5611547469939069
				],
				[
					376.94798670906715,
					0.5611547469939069
				],
				[
					377.47186203767143,
					0.3844423438076774
				],
				[
					377.47186203767143,
					0.3844423438076774
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				377.47186203767143,
				0.3844423438076774
			]
		}
	],
	"appState": {
		"theme": "light",
		"viewBackgroundColor": "#ffffff",
		"currentItemStrokeColor": "#1971c2",
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
		"scrollX": 585.159496955451,
		"scrollY": 4085.1488437598464,
		"zoom": {
			"value": 1.1501573553869047
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