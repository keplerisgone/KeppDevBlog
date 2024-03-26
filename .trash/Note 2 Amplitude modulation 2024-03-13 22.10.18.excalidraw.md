---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠==


# Text Elements
- analog signal - continuous한 신호를 보냄
    그렇다고 digital이 non continuous인 건 아님
    digital은 그냥 level이 존재함

- bandwidth를 유지하는 것이 중요하기 때문에 따로 변형을 가하지 x
- 보내는 정보에 따라 bandwidth가 다름 ^99BQVgc2

analog signal은 carrier modulation에 의해 전달됨

- analog를 전해주는 신호 = carrier wave

- 왜 사인함수인가 : 진동을 보기 좋아서
-> rectangular 함수를 써도 됨

- 뭐든 지 level을 적당히 정해야 효율적임
    예를 들어 phase는 360도까지만 존재

- carrier에는 정보가 담기는데...
이 정보는 A, P, F 중에 하나에 담김
각 종류마다 modulation이 있음

- 이런 modulation을 진행하는 게 바로 modem
+ demodulation도 진행 ^NZqpQiJX

- m(t)
    메세지를 담은 signal
    analog
    baseband = 중심이 0이라는 뜻
    bandwidth가 W
    modulating (당하는)

- c(t)
    그냥 코사인 함수
    carrier

- u(t)
    Passband = 밴드의 중심이 fc
    Modulated (당한)
    transmitted = 전달되는 ^dgFz7CDC

Gibbs ^zeCcV0Iy

왜 하는가?

1. 채널의 주파수 대역을 맞추기 위해서

2. transmitter를 맞추기 위해서
    - 안테나의 크기는 신호의 반파장이어야 하는데,
    - 주파수를 크게 하면 파장이 줄어든다

 ^gaHr29zo

3. Freauency-division
- 더 많은 사람들이 이용할 수 있게 한다

4. 노이즈에 강해진다
근데 AM만 이게 해당이 안 됨
PM,FM의 경우는 bandwidth를 5배로 늘리는 경우만 해당

아무튼 takeoff가 있다~ ^5xLJkgZS

angle modulation ^p6QpW7hZ

DSB-SC AM
- 원래 y축에 의해서 쪼개져 있던게 나와서 bandwidth가 두배가 됨
- cos이 사라져요..

DSB-LC AM
- carrier(cos)이 살아있어요
- 간섭을 억제할 수 있음

SSB AM
- 신호의 절반만 보내요

VSB AM
- SSB가 현실적인 건 아니니까
신호의 60%만 보내요

위 모두 analog, digital 상관없이 스펙트럼에 관한 이야기 ^dP6Pf2UT

가장 중요한 점은 bandwidth는 "양수" 부분이다 ^Jh0qgU65

- 전까지 열심히 한 예제들

- bandwidth가 2배가 됨 ⭐️

- LSB / USB가 나뉘는데, y축에 가까운 기준임 (대칭이 되므로)

- 진폭은 절반이 되는데, 통신에서 상수는 그리 중요하지 않다 ^W7YhoNii

Power는 어떻게 계산하나요?

- 결과적으로 u(t)의 power는 요렇게 나온다

- power 손실이 거의 없는 방법 ^sqFJaB0M

외워도 좋지만 계산도 해봐... ^KHu9pbTm

이상적인 채널이란?
- 크기가 상수
- 위상의 변화가 linear -> 노이즈 감지 때문

- u(t)를 받아서 다시 modulation을 하면 됨
    - 이게 왜 그러냐면 modulation을 다시 할 때
    - 원래 신호 성분이 0으로 가기 때문
    - 요걸 LPF 같은 걸로 빼내면 된다

- 하지만 time delay가 phase의 형태로 나타남
    다를 경우는 문제가 없지만, (상수임)
    phi = 90이라면 ? (cos phi = 0)
    요걸 phase-coherent라고 함 ^r6piIJBX

파워도 손실나네 ^KibxUpXJ

PLL
- pilot signal이 필요하지 않은 사인함수를 보내는 것

Pilot tone = pilot signal
- referene가 되는 시그널
- 노이즈를 잡기 위한 기준이 되는 시그널
- 송수신 측 모두 알고 있음 ^biOHXWpg

DSB-SC의 강점인 부분

Envelope detector
- 다이오드와 RC로 이루어진 회로를 이용해 신호를 detect
- 회로로 통과한 신호 (양수 부분만 존재)를 외곽선만 따옴
- 편지봉투 뜯는거 같다해서 envelope

- 다만 RC값 설정하는 게 귀찮음
    - 너무크면 신호를 못따라가고
    - 너무 작으면 신호가 뭔지 알 수가 없음 (왜곡) ^4xwsbrAu

DSB-SC의 단점
- 0을 사이로 왔다갔다하면 어딜 선택해야할지 모름

그래서 conventional AM (DSB-LC)는 신호를 모두 양으로 옮김
- 편리한 demodulation ^fO9vQ0Fk

- message가 1보다 작게 되도록

- modulation index : 안전하게 1보다 작게 하려고













- delta signal이 추가됨 > message의 noise를 추적가능
 ^Q1gNY2bl

- power를 구할때는 그냥 (1+m)을 적용하면 됨
   ^H8vSIrSg

상수 부분은 정보를 담지 않음
뒷 부분이 정보를 담는다 - power는 작음
=> power 관점에서는 비효율적임 ^XTCUHNDY

LC는 뭔가가 추가될까요 ^FpHbmbhy

- idea : ussb/lssb 둘 중 하나만 있어도 복구하는데 문제x ^q35eetPr

<- domain 변환 ^Nuw3xXQP

진짜 변환
 ^aGT0urr5

그냥 BPF를 사용해도 ㄱㅊ ^UUDABM9f

잡음에 의한 영향이 훨씬 큼
-> pilot tone이 무조건 필요 ^JHcRK4Sb

근데 어려움 ^WOaAx25o


# Embedded files
c8143be10dd752ac6c71a0de2c90b07ae4be65d7: [[Note 2 Amplitude Modulation.pdf#page=1]]
38fa7096d0eb6769bc9b4c62286468930e56320c: [[Note 2 Amplitude Modulation.pdf#page=2]]
0adc1e6c918799d18e5e8712a4ba73cc6d016bc2: [[Note 2 Amplitude Modulation.pdf#page=3]]
0185974c2ecf6782be3703c587c5046f7685fe39: [[Note 2 Amplitude Modulation.pdf#page=4]]
25c9405845a297744e4f97c947a874e5467073fa: [[Note 2 Amplitude Modulation.pdf#page=5]]
c80031f00036a80338f82f83199920873be2d0a6: [[Note 2 Amplitude Modulation.pdf#page=6]]
846e93bf80e2ffa100370e495a3ef370292ab4f3: [[Note 2 Amplitude Modulation.pdf#page=7]]
41e70176b43b7556764e531de0ef651d5862e525: [[Note 2 Amplitude Modulation.pdf#page=8]]
a591b905e161d8412a6374aea43891351f9adb1b: [[Note 2 Amplitude Modulation.pdf#page=9]]
495af923d4362a721436f433077a997258670fc9: [[Note 2 Amplitude Modulation.pdf#page=10]]
e2bb92e652772c5f674beee877a5fb5cb329dd89: [[Note 2 Amplitude Modulation.pdf#page=11]]
6255af5699b5bc0be8396ab6b7a63e402b0e6885: [[Note 2 Amplitude Modulation.pdf#page=12]]
81746609bf5d631cd888e02849280c938e5365f4: [[Note 2 Amplitude Modulation.pdf#page=13]]
36ec707a1e5e939563eb9ab66041c891020b2433: [[Note 2 Amplitude Modulation.pdf#page=14]]
69978018fc67e7ce22f7811bbd22feb910e390bd: [[Note 2 Amplitude Modulation.pdf#page=15]]
dddf3e7f079d2d5b21521977be3cde7abb9a5a2b: [[Note 2 Amplitude Modulation.pdf#page=16]]
d6bfd4875243cdf4cf2011b3b7bfcc64aefeb7e3: [[Note 2 Amplitude Modulation.pdf#page=17]]
a4baa5f0097f930ab0eb6bd31544188798131d5a: [[Note 2 Amplitude Modulation.pdf#page=18]]
511ed20f00514224c728af45ee02178b30a60d93: [[Note 2 Amplitude Modulation.pdf#page=19]]
3cd04620345b27632ba7bda18dea4e2f19cc8fb9: [[Note 2 Amplitude Modulation.pdf#page=20]]
a9832ca7805be222907c12b55cd2d9b66600924e: [[Note 2 Amplitude Modulation.pdf#page=21]]
f2d85a5fb8c902337ecbd42bc23de5629834b902: [[Note 2 Amplitude Modulation.pdf#page=22]]
1372f45c5cc07d1dfd5a1297e7dfda9e1257b074: [[Note 2 Amplitude Modulation.pdf#page=23]]
5f5a0593ce707c35da3086e8412c217d393466e0: [[Note 2 Amplitude Modulation.pdf#page=24]]
ccd2f77088abe20d3608d3c3faa52cc79b5d81ae: [[Note 2 Amplitude Modulation.pdf#page=25]]
c2f8a1bd07ded1447b5c0506be8f6fab710b5ae9: [[Note 2 Amplitude Modulation.pdf#page=26]]
33ebcc857c5b9d2c8a2a299107b3c4fa2fd21c16: [[Note 2 Amplitude Modulation.pdf#page=27]]
05afcbd6f2a04ed5c6b5025bb87ba9866fee2733: [[Note 2 Amplitude Modulation.pdf#page=28]]
9b043278a0b9536ab308153a57a6c4c7145140f7: [[Note 2 Amplitude Modulation.pdf#page=29]]
94ad7704c96c5fb47b339a02ea2bedd891d0e73e: [[Note 2 Amplitude Modulation.pdf#page=30]]
e7d97db1a80647822d48c0aabe63f722c37456ff: [[Note 2 Amplitude Modulation.pdf#page=31]]
b2fa8a3175283950bd3cce1d2ba903d450ba5537: [[Note 2 Amplitude Modulation.pdf#page=32]]
2a89013e575f12a015412e91f55a7f498fc906d0: [[Note 2 Amplitude Modulation.pdf#page=33]]
0401b4db5299b78b007de29d01e18c65dff95179: [[Note 2 Amplitude Modulation.pdf#page=34]]
dee5debd6d637d34747d3da459d3ef0158354014: [[Note 2 Amplitude Modulation.pdf#page=35]]
0987f3531b04de513d938268a15ed865d89da71c: [[Note 2 Amplitude Modulation.pdf#page=36]]
11ec3d2debd4fb166f801600fcccfe15df71e303: [[Note 2 Amplitude Modulation.pdf#page=37]]
06b7f45aa80805876495506e733671c7dccd756c: [[Note 2 Amplitude Modulation.pdf#page=38]]
f74f5cd2236f5d340baf110553a81538263dc40c: [[Note 2 Amplitude Modulation.pdf#page=39]]
84693ea10fa5030eef4bfcf3c6b34a27b4a85740: [[Note 2 Amplitude Modulation.pdf#page=40]]
84a654f5c5933ef409fe897d1f615feb7761ccf6: [[Note 2 Amplitude Modulation.pdf#page=41]]
289bfc82af242884ffccb8cfce180c68dd2c0c28: [[Note 2 Amplitude Modulation.pdf#page=42]]
795b9b2199d917d4fb7700d266012bce0d9263e1: [[Note 2 Amplitude Modulation.pdf#page=43]]
0c35a242921b7d9039820cbd544ba7cc252e7b6b: [[Note 2 Amplitude Modulation.pdf#page=44]]
8812d6a58850a3145be6c9908ec726b4fcbe5b89: [[Note 2 Amplitude Modulation.pdf#page=45]]
df108c60d82250f25f8106242cfe0934c530a12e: [[Note 2 Amplitude Modulation.pdf#page=46]]
c4e81917e0b8ccd8624e421fc9f58c01e5a0872f: [[Note 2 Amplitude Modulation.pdf#page=47]]
0967cf6ed30f1b3336a38fa0f776fb38645b7184: [[Note 2 Amplitude Modulation.pdf#page=48]]
ea2835ce33ea8f1f779959a6139504daa72c4ee7: [[Note 2 Amplitude Modulation.pdf#page=49]]
1f4a991e3f4ed24a957392205d8d707f66ab4303: [[Note 2 Amplitude Modulation.pdf#page=50]]
2e032788dd8bf79ae3e4b168fcd91ed5d91f1963: [[Note 2 Amplitude Modulation.pdf#page=51]]
40541578232a9ce4ab0a5aa9207df5f179a4f2e1: [[Note 2 Amplitude Modulation.pdf#page=52]]
52200c40b49aa35d208ec62a6737b2fa3aca8d34: [[Note 2 Amplitude Modulation.pdf#page=53]]
c75a137e204e7c6d08c0ef0115db14f74edd3bf5: [[Note 2 Amplitude Modulation.pdf#page=54]]
ae17d23aa6ed4f91a8beaba3865fb5bcb18588c6: [[Note 2 Amplitude Modulation.pdf#page=55]]

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
			"versionNonce": 424950263,
			"isDeleted": false,
			"id": "tNsqApMs",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -6318,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 93259,
			"groupIds": [
				"8j5T21DW",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914307,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 10339577,
			"isDeleted": false,
			"id": "KmMtoX1f",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -6318,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 58314,
			"groupIds": [
				"8j5T21DW",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914307,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "c8143be10dd752ac6c71a0de2c90b07ae4be65d7",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 885515031,
			"isDeleted": false,
			"id": "rzrEb5gM",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -6318,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 33835,
			"groupIds": [
				"lEBgn3YZ",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914307,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 1181531609,
			"isDeleted": false,
			"id": "0ZHQyce5",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -6318,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 2817,
			"groupIds": [
				"lEBgn3YZ",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914307,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "38fa7096d0eb6769bc9b4c62286468930e56320c",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 841574455,
			"isDeleted": false,
			"id": "fQNHP399",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -5866,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 59738,
			"groupIds": [
				"qceOSXW6",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914307,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 1839831737,
			"isDeleted": false,
			"id": "8A3nqszQ",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -5866,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 88058,
			"groupIds": [
				"qceOSXW6",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914307,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "0adc1e6c918799d18e5e8712a4ba73cc6d016bc2",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1331513687,
			"isDeleted": false,
			"id": "jusuZGNI",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -5866,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 27464,
			"groupIds": [
				"Wj3TSTpY",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914307,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 1459084185,
			"isDeleted": false,
			"id": "ngmFP5YF",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -5866,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 51583,
			"groupIds": [
				"Wj3TSTpY",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914307,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "0185974c2ecf6782be3703c587c5046f7685fe39",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 431490679,
			"isDeleted": false,
			"id": "CtHPeeY2",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -5414,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 71360,
			"groupIds": [
				"YmHpyV7t",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914307,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 42664057,
			"isDeleted": false,
			"id": "WfGM0Eh5",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -5414,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 64941,
			"groupIds": [
				"YmHpyV7t",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914307,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "25c9405845a297744e4f97c947a874e5467073fa",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 2147360663,
			"isDeleted": false,
			"id": "5U7cmL8J",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -5414,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 26288,
			"groupIds": [
				"nv8A6Mir",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914307,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 505842009,
			"isDeleted": false,
			"id": "oMaXsfzm",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -5414,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 20299,
			"groupIds": [
				"nv8A6Mir",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914307,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "c80031f00036a80338f82f83199920873be2d0a6",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 610538679,
			"isDeleted": false,
			"id": "rr1bsfJ0",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -4962,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 29039,
			"groupIds": [
				"TsTOGFpw",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914307,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 1394472505,
			"isDeleted": false,
			"id": "X4GCXuoD",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -4962,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 48427,
			"groupIds": [
				"TsTOGFpw",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914307,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "846e93bf80e2ffa100370e495a3ef370292ab4f3",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1854825943,
			"isDeleted": false,
			"id": "Yh0E4Mk9",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -4962,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 45644,
			"groupIds": [
				"fq7c65CH",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914307,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 1414842137,
			"isDeleted": false,
			"id": "Dn3Hf0eC",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -4962,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 83342,
			"groupIds": [
				"fq7c65CH",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914308,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "41e70176b43b7556764e531de0ef651d5862e525",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1569821431,
			"isDeleted": false,
			"id": "fx2LRgYF",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -4510,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 84718,
			"groupIds": [
				"ieqvFYRk",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914308,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 742292473,
			"isDeleted": false,
			"id": "cVbio7gZ",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -4510,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 94735,
			"groupIds": [
				"ieqvFYRk",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914308,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "a591b905e161d8412a6374aea43891351f9adb1b",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 435297303,
			"isDeleted": false,
			"id": "CMQFT53p",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -4510,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 94984,
			"groupIds": [
				"6NSQJmxP",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914308,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 1256101081,
			"isDeleted": false,
			"id": "XP8Zh2hU",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -4510,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 26780,
			"groupIds": [
				"6NSQJmxP",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914308,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "495af923d4362a721436f433077a997258670fc9",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1201963319,
			"isDeleted": false,
			"id": "3PxxQYVY",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -4058,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 60984,
			"groupIds": [
				"v4XbNS1Z",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914308,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 1405653433,
			"isDeleted": false,
			"id": "DLu8RXVU",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -4058,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 83171,
			"groupIds": [
				"v4XbNS1Z",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914308,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "e2bb92e652772c5f674beee877a5fb5cb329dd89",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 403522135,
			"isDeleted": false,
			"id": "uH7tx4Pn",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -4058,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 78559,
			"groupIds": [
				"lFGLNRsh",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914308,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 740291225,
			"isDeleted": false,
			"id": "PBlhBm5u",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -4058,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 65427,
			"groupIds": [
				"lFGLNRsh",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914308,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "6255af5699b5bc0be8396ab6b7a63e402b0e6885",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 469819255,
			"isDeleted": false,
			"id": "fYgS7PMi",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -3606,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 25025,
			"groupIds": [
				"x28NfCw9",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914308,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 1217935225,
			"isDeleted": false,
			"id": "ITBusvm0",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -3606,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 65169,
			"groupIds": [
				"x28NfCw9",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914308,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "81746609bf5d631cd888e02849280c938e5365f4",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1438898327,
			"isDeleted": false,
			"id": "a6JsXyEb",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -3606,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 49772,
			"groupIds": [
				"SGo95r3U",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914308,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 997515353,
			"isDeleted": false,
			"id": "G56Vh0KH",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -3606,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 8324,
			"groupIds": [
				"SGo95r3U",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914308,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "36ec707a1e5e939563eb9ab66041c891020b2433",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 185249207,
			"isDeleted": false,
			"id": "VnM1qcTB",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -3154,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 55628,
			"groupIds": [
				"C0ZbG0uq",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914308,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 42560825,
			"isDeleted": false,
			"id": "xpAkdX44",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -3154,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 96497,
			"groupIds": [
				"C0ZbG0uq",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914308,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "69978018fc67e7ce22f7811bbd22feb910e390bd",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1459216087,
			"isDeleted": false,
			"id": "W1W7xgDI",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -3154,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 87657,
			"groupIds": [
				"WJDKPyyY",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914308,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 356081177,
			"isDeleted": false,
			"id": "bDoTHHoK",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -3154,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 90397,
			"groupIds": [
				"WJDKPyyY",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914308,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "dddf3e7f079d2d5b21521977be3cde7abb9a5a2b",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 2082860023,
			"isDeleted": false,
			"id": "KSgxyPBJ",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -2702,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 19112,
			"groupIds": [
				"eMAOd3n2",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914308,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 846738169,
			"isDeleted": false,
			"id": "uZRprIPr",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -2702,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 2401,
			"groupIds": [
				"eMAOd3n2",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914308,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "d6bfd4875243cdf4cf2011b3b7bfcc64aefeb7e3",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1989367063,
			"isDeleted": false,
			"id": "Ffth1WIC",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -2702,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 51048,
			"groupIds": [
				"W0BiNzj4",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914308,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 1858694105,
			"isDeleted": false,
			"id": "stDCnlxH",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -2702,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 23235,
			"groupIds": [
				"W0BiNzj4",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914308,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "a4baa5f0097f930ab0eb6bd31544188798131d5a",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1303812663,
			"isDeleted": false,
			"id": "vE5wiRJj",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -2250,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 67465,
			"groupIds": [
				"LZYPx3oX",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914308,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 37783737,
			"isDeleted": false,
			"id": "A2NgeaHk",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -2250,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 45751,
			"groupIds": [
				"LZYPx3oX",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914308,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "511ed20f00514224c728af45ee02178b30a60d93",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 645151575,
			"isDeleted": false,
			"id": "9E3IFQTk",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -2250,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 17457,
			"groupIds": [
				"1idc7I9j",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914308,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 1451297177,
			"isDeleted": false,
			"id": "88Flto62",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -2250,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 57782,
			"groupIds": [
				"1idc7I9j",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914308,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "3cd04620345b27632ba7bda18dea4e2f19cc8fb9",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 354465911,
			"isDeleted": false,
			"id": "Uti6oQEK",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -1798,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 24165,
			"groupIds": [
				"HslYIqrs",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914308,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 1421766265,
			"isDeleted": false,
			"id": "Bkwiw8qY",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -1798,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 51738,
			"groupIds": [
				"HslYIqrs",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914308,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "a9832ca7805be222907c12b55cd2d9b66600924e",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 796955031,
			"isDeleted": false,
			"id": "FZCHi7qF",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -1798,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 1856,
			"groupIds": [
				"VYNx9GLy",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914308,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 1941714777,
			"isDeleted": false,
			"id": "iCXJnhw1",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -1798,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 75580,
			"groupIds": [
				"VYNx9GLy",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914308,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "f2d85a5fb8c902337ecbd42bc23de5629834b902",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1590183607,
			"isDeleted": false,
			"id": "9Tn2aYaw",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -1346,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 52671,
			"groupIds": [
				"WrErqAjB",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914308,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 97379385,
			"isDeleted": false,
			"id": "Lf2zYegQ",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -1346,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 44406,
			"groupIds": [
				"WrErqAjB",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914308,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "1372f45c5cc07d1dfd5a1297e7dfda9e1257b074",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1906071511,
			"isDeleted": false,
			"id": "H5JTgHaQ",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -1346,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 99669,
			"groupIds": [
				"MmhhS3Dw",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914308,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 1188492569,
			"isDeleted": false,
			"id": "BRHFo5p0",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -1346,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 26763,
			"groupIds": [
				"MmhhS3Dw",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914308,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "5f5a0593ce707c35da3086e8412c217d393466e0",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1846625527,
			"isDeleted": false,
			"id": "LwqpM0Lm",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -894,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 12796,
			"groupIds": [
				"ubH2jHvB",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914308,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 709552633,
			"isDeleted": false,
			"id": "IWypwjzu",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -894,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 67967,
			"groupIds": [
				"ubH2jHvB",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914308,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "ccd2f77088abe20d3608d3c3faa52cc79b5d81ae",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 598445591,
			"isDeleted": false,
			"id": "Xvq6OBAp",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -894,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 82584,
			"groupIds": [
				"Cu6oURz1",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914309,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 1764573913,
			"isDeleted": false,
			"id": "LqSsNNRG",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -894,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 55442,
			"groupIds": [
				"Cu6oURz1",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914309,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "c2f8a1bd07ded1447b5c0506be8f6fab710b5ae9",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 2103423799,
			"isDeleted": false,
			"id": "gGSQQBIj",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -442,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 46424,
			"groupIds": [
				"EP8xcjc9",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914309,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 1343324089,
			"isDeleted": false,
			"id": "qxBD3ikW",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": -442,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 58485,
			"groupIds": [
				"EP8xcjc9",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914309,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "33ebcc857c5b9d2c8a2a299107b3c4fa2fd21c16",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 328348759,
			"isDeleted": false,
			"id": "Op6PoENq",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -442,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 46027,
			"groupIds": [
				"eEFtP83W",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914309,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 1293623449,
			"isDeleted": false,
			"id": "3RuVMTX5",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": -442,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 38689,
			"groupIds": [
				"eEFtP83W",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914309,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "05afcbd6f2a04ed5c6b5025bb87ba9866fee2733",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 2115473783,
			"isDeleted": false,
			"id": "EsGIh76x",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": 10,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 46076,
			"groupIds": [
				"sabZyOnD",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914309,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 1040033145,
			"isDeleted": false,
			"id": "glRiVo1Z",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": 10,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 47839,
			"groupIds": [
				"sabZyOnD",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914309,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "9b043278a0b9536ab308153a57a6c4c7145140f7",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1714702999,
			"isDeleted": false,
			"id": "4768IEFk",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": 10,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 99932,
			"groupIds": [
				"qgDCCPQ3",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914309,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 2113703513,
			"isDeleted": false,
			"id": "fp03yQAe",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": 10,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 50046,
			"groupIds": [
				"qgDCCPQ3",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914309,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "94ad7704c96c5fb47b339a02ea2bedd891d0e73e",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1486675895,
			"isDeleted": false,
			"id": "d77b9Xp5",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": 462,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 13136,
			"groupIds": [
				"CWPBtd0V",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914309,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 871062329,
			"isDeleted": false,
			"id": "l7silYUU",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": 462,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 60855,
			"groupIds": [
				"CWPBtd0V",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914309,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "e7d97db1a80647822d48c0aabe63f722c37456ff",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1467338967,
			"isDeleted": false,
			"id": "pbx4qPvN",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": 462,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 87637,
			"groupIds": [
				"TOkQ2L0o",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914309,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 1613597721,
			"isDeleted": false,
			"id": "UonThhh2",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": 462,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 81900,
			"groupIds": [
				"TOkQ2L0o",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914309,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "b2fa8a3175283950bd3cce1d2ba903d450ba5537",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 743677431,
			"isDeleted": false,
			"id": "bdJQnapH",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": 914,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 78669,
			"groupIds": [
				"0AmLxuVG",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914309,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 716611833,
			"isDeleted": false,
			"id": "k8SZhnvy",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": 914,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 58880,
			"groupIds": [
				"0AmLxuVG",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914309,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "2a89013e575f12a015412e91f55a7f498fc906d0",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 2050672407,
			"isDeleted": false,
			"id": "DSv639FX",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": 914,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 75395,
			"groupIds": [
				"1xjdQam5",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914309,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 1896487385,
			"isDeleted": false,
			"id": "oa9COXqv",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": 914,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 62892,
			"groupIds": [
				"1xjdQam5",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914309,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "0401b4db5299b78b007de29d01e18c65dff95179",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 262130743,
			"isDeleted": false,
			"id": "TchGRyNN",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": 1366,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 54093,
			"groupIds": [
				"exw9XVLS",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914309,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 339441337,
			"isDeleted": false,
			"id": "Tg1ivTqf",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": 1366,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 42668,
			"groupIds": [
				"exw9XVLS",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914309,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "dee5debd6d637d34747d3da459d3ef0158354014",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 2020027735,
			"isDeleted": false,
			"id": "hd5l6lau",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": 1366,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 72912,
			"groupIds": [
				"iwyaswBD",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914309,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 116275097,
			"isDeleted": false,
			"id": "VLg31uNq",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": 1366,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 44823,
			"groupIds": [
				"iwyaswBD",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914309,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "0987f3531b04de513d938268a15ed865d89da71c",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1340435063,
			"isDeleted": false,
			"id": "AwGk890B",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": 1818,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 28380,
			"groupIds": [
				"kkEW5gkj",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914309,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 458611833,
			"isDeleted": false,
			"id": "iPcP5Mrp",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": 1818,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 61902,
			"groupIds": [
				"kkEW5gkj",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914309,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "11ec3d2debd4fb166f801600fcccfe15df71e303",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1390347159,
			"isDeleted": false,
			"id": "WmTMi4y1",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": 1818,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 60616,
			"groupIds": [
				"n7LgykUJ",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914309,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 288744793,
			"isDeleted": false,
			"id": "5YibnvgT",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": 1818,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 76110,
			"groupIds": [
				"n7LgykUJ",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914309,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "06b7f45aa80805876495506e733671c7dccd756c",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 831027383,
			"isDeleted": false,
			"id": "oe75oVn6",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": 2270,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 99201,
			"groupIds": [
				"Pg3O3OIQ",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914309,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 1675743801,
			"isDeleted": false,
			"id": "nhOsAx0f",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": 2270,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 47571,
			"groupIds": [
				"Pg3O3OIQ",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914309,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "f74f5cd2236f5d340baf110553a81538263dc40c",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 562448855,
			"isDeleted": false,
			"id": "YemtgOXN",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": 2270,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 11534,
			"groupIds": [
				"BXUreRI9",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914309,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 1480401689,
			"isDeleted": false,
			"id": "tRsCGaKy",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": 2270,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 18246,
			"groupIds": [
				"BXUreRI9",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914309,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "84693ea10fa5030eef4bfcf3c6b34a27b4a85740",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 804058871,
			"isDeleted": false,
			"id": "jOLrdYbi",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": 2722,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 84782,
			"groupIds": [
				"X7SDVjaI",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914309,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 1253791737,
			"isDeleted": false,
			"id": "Vwrx5p2O",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": 2722,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 25063,
			"groupIds": [
				"X7SDVjaI",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914309,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "84a654f5c5933ef409fe897d1f615feb7761ccf6",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1396768791,
			"isDeleted": false,
			"id": "rEEPLYfR",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": 2722,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 98655,
			"groupIds": [
				"NjO8CpmR",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914309,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 1029697753,
			"isDeleted": false,
			"id": "OHKVb1LT",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": 2722,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 15912,
			"groupIds": [
				"NjO8CpmR",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914309,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "289bfc82af242884ffccb8cfce180c68dd2c0c28",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1031202103,
			"isDeleted": false,
			"id": "hxCRWLNd",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": 3174,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 73901,
			"groupIds": [
				"6PpJ78V4",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914309,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 633236921,
			"isDeleted": false,
			"id": "FDj8zOhw",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": 3174,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 56161,
			"groupIds": [
				"6PpJ78V4",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914309,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "795b9b2199d917d4fb7700d266012bce0d9263e1",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1844651607,
			"isDeleted": false,
			"id": "GtL80LzO",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": 3174,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 92453,
			"groupIds": [
				"YDjVxX61",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914309,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 2063224473,
			"isDeleted": false,
			"id": "HPZqGi7l",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": 3174,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 29105,
			"groupIds": [
				"YDjVxX61",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914309,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "0c35a242921b7d9039820cbd544ba7cc252e7b6b",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 59392887,
			"isDeleted": false,
			"id": "u5Gh1k5r",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": 3626,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 19797,
			"groupIds": [
				"gnIpHmzW",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914309,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 63378297,
			"isDeleted": false,
			"id": "Idlodvaa",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": 3626,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 92690,
			"groupIds": [
				"gnIpHmzW",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914309,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "8812d6a58850a3145be6c9908ec726b4fcbe5b89",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1317059735,
			"isDeleted": false,
			"id": "nvNUl9tn",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": 3626,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 23191,
			"groupIds": [
				"4fbgcUTO",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914309,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 1684552793,
			"isDeleted": false,
			"id": "nWoamd5o",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": 3626,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 85683,
			"groupIds": [
				"4fbgcUTO",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914309,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "df108c60d82250f25f8106242cfe0934c530a12e",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 579539383,
			"isDeleted": false,
			"id": "HDTTjJVp",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": 4078,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 8156,
			"groupIds": [
				"som31EEo",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914309,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 1823557945,
			"isDeleted": false,
			"id": "M0KmmZFl",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": 4078,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 55879,
			"groupIds": [
				"som31EEo",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914309,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "c4e81917e0b8ccd8624e421fc9f58c01e5a0872f",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1758315223,
			"isDeleted": false,
			"id": "pB7vD8ag",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": 4078,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 15212,
			"groupIds": [
				"hb5MwbPz",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914309,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 637909529,
			"isDeleted": false,
			"id": "R4rtnz6Z",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": 4078,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 32286,
			"groupIds": [
				"hb5MwbPz",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914309,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "0967cf6ed30f1b3336a38fa0f776fb38645b7184",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1910329335,
			"isDeleted": false,
			"id": "z2h7wbKD",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": 4530,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 80197,
			"groupIds": [
				"ugQMKxE9",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914309,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 559484665,
			"isDeleted": false,
			"id": "OFkDbHyq",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": 4530,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 9172,
			"groupIds": [
				"ugQMKxE9",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914310,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "ea2835ce33ea8f1f779959a6139504daa72c4ee7",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 129906967,
			"isDeleted": false,
			"id": "F7jWz7ho",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": 4530,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 27464,
			"groupIds": [
				"LvO9MKAY",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914310,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 86951897,
			"isDeleted": false,
			"id": "7AKF8uFE",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": 4530,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 15019,
			"groupIds": [
				"LvO9MKAY",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914310,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "1f4a991e3f4ed24a957392205d8d707f66ab4303",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1071971895,
			"isDeleted": false,
			"id": "JPNaMcvD",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": 4982,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 11186,
			"groupIds": [
				"59WDdcNF",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914310,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 1536844985,
			"isDeleted": false,
			"id": "sWeEvDbS",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": 4982,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 36226,
			"groupIds": [
				"59WDdcNF",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914310,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "2e032788dd8bf79ae3e4b168fcd91ed5d91f1963",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 221650775,
			"isDeleted": false,
			"id": "qe4ohdGL",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": 4982,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 7578,
			"groupIds": [
				"za9y6lEm",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914310,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 541025689,
			"isDeleted": false,
			"id": "uykW2nUa",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": 4982,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 29673,
			"groupIds": [
				"za9y6lEm",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914310,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "40541578232a9ce4ab0a5aa9207df5f179a4f2e1",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 302390391,
			"isDeleted": false,
			"id": "gn2Mno2r",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": 5434,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 95784,
			"groupIds": [
				"VORnmjDl",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914310,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 240208505,
			"isDeleted": false,
			"id": "QAfppBsQ",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": 5434,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 38265,
			"groupIds": [
				"VORnmjDl",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914310,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "52200c40b49aa35d208ec62a6737b2fa3aca8d34",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 840529303,
			"isDeleted": false,
			"id": "41iMz6Qp",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": 5434,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 75646,
			"groupIds": [
				"gaTr7Y0K",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914310,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 781423449,
			"isDeleted": false,
			"id": "qXKXao2d",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 10,
			"y": 5434,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 29118,
			"groupIds": [
				"gaTr7Y0K",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914310,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "c75a137e204e7c6d08c0ef0115db14f74edd3bf5",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 19,
			"versionNonce": 1688513207,
			"isDeleted": false,
			"id": "4fQ0yFlM",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": 5886,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 38883,
			"groupIds": [
				"peDbH18s",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914310,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 19,
			"versionNonce": 626638905,
			"isDeleted": false,
			"id": "mdzESEZO",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -586,
			"y": 5886,
			"strokeColor": "#000000",
			"backgroundColor": "transparent",
			"width": 576,
			"height": 432,
			"seed": 83794,
			"groupIds": [
				"peDbH18s",
				"eqazT9lH"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914310,
			"link": null,
			"locked": true,
			"status": "pending",
			"fileId": "ae17d23aa6ed4f91a8beaba3865fb5bcb18588c6",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "text",
			"version": 335,
			"versionNonce": 1179401175,
			"isDeleted": false,
			"id": "99BQVgc2",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 592.8348307053371,
			"y": -6311.877664611609,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 466.7198486328125,
			"height": 120,
			"seed": 591648754,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914310,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 1,
			"text": "- analog signal - continuous한 신호를 보냄\n    그렇다고 digital이 non continuous인 건 아님\n    digital은 그냥 level이 존재함\n\n- bandwidth를 유지하는 것이 중요하기 때문에 따로 변형을 가하지 x\n- 보내는 정보에 따라 bandwidth가 다름",
			"rawText": "- analog signal - continuous한 신호를 보냄\n    그렇다고 digital이 non continuous인 건 아님\n    digital은 그냥 level이 존재함\n\n- bandwidth를 유지하는 것이 중요하기 때문에 따로 변형을 가하지 x\n- 보내는 정보에 따라 bandwidth가 다름",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "- analog signal - continuous한 신호를 보냄\n    그렇다고 digital이 non continuous인 건 아님\n    digital은 그냥 level이 존재함\n\n- bandwidth를 유지하는 것이 중요하기 때문에 따로 변형을 가하지 x\n- 보내는 정보에 따라 bandwidth가 다름",
			"lineHeight": 1.25,
			"baseline": 114
		},
		{
			"type": "text",
			"version": 628,
			"versionNonce": 1082609945,
			"isDeleted": false,
			"id": "NZqpQiJX",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -960.4043506536436,
			"y": -5857.998360384538,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 361.8878479003906,
			"height": 320,
			"seed": 27092654,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914310,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 1,
			"text": "analog signal은 carrier modulation에 의해 전달됨\n\n- analog를 전해주는 신호 = carrier wave\n\n- 왜 사인함수인가 : 진동을 보기 좋아서\n-> rectangular 함수를 써도 됨\n\n- 뭐든 지 level을 적당히 정해야 효율적임\n    예를 들어 phase는 360도까지만 존재\n\n- carrier에는 정보가 담기는데...\n이 정보는 A, P, F 중에 하나에 담김\n각 종류마다 modulation이 있음\n\n- 이런 modulation을 진행하는 게 바로 modem\n+ demodulation도 진행",
			"rawText": "analog signal은 carrier modulation에 의해 전달됨\n\n- analog를 전해주는 신호 = carrier wave\n\n- 왜 사인함수인가 : 진동을 보기 좋아서\n-> rectangular 함수를 써도 됨\n\n- 뭐든 지 level을 적당히 정해야 효율적임\n    예를 들어 phase는 360도까지만 존재\n\n- carrier에는 정보가 담기는데...\n이 정보는 A, P, F 중에 하나에 담김\n각 종류마다 modulation이 있음\n\n- 이런 modulation을 진행하는 게 바로 modem\n+ demodulation도 진행",
			"textAlign": "right",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "analog signal은 carrier modulation에 의해 전달됨\n\n- analog를 전해주는 신호 = carrier wave\n\n- 왜 사인함수인가 : 진동을 보기 좋아서\n-> rectangular 함수를 써도 됨\n\n- 뭐든 지 level을 적당히 정해야 효율적임\n    예를 들어 phase는 360도까지만 존재\n\n- carrier에는 정보가 담기는데...\n이 정보는 A, P, F 중에 하나에 담김\n각 종류마다 modulation이 있음\n\n- 이런 modulation을 진행하는 게 바로 modem\n+ demodulation도 진행",
			"lineHeight": 1.25,
			"baseline": 314
		},
		{
			"type": "text",
			"version": 372,
			"versionNonce": 1797564663,
			"isDeleted": false,
			"id": "dgFz7CDC",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 593.4410202439296,
			"y": -5852.822735372356,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 253.37591552734375,
			"height": 300,
			"seed": 368782386,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914310,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 1,
			"text": "- m(t)\n    메세지를 담은 signal\n    analog\n    baseband = 중심이 0이라는 뜻\n    bandwidth가 W\n    modulating (당하는)\n\n- c(t)\n    그냥 코사인 함수\n    carrier\n\n- u(t)\n    Passband = 밴드의 중심이 fc\n    Modulated (당한)\n    transmitted = 전달되는",
			"rawText": "- m(t)\n    메세지를 담은 signal\n    analog\n    baseband = 중심이 0이라는 뜻\n    bandwidth가 W\n    modulating (당하는)\n\n- c(t)\n    그냥 코사인 함수\n    carrier\n\n- u(t)\n    Passband = 밴드의 중심이 fc\n    Modulated (당한)\n    transmitted = 전달되는",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "- m(t)\n    메세지를 담은 signal\n    analog\n    baseband = 중심이 0이라는 뜻\n    bandwidth가 W\n    modulating (당하는)\n\n- c(t)\n    그냥 코사인 함수\n    carrier\n\n- u(t)\n    Passband = 밴드의 중심이 fc\n    Modulated (당한)\n    transmitted = 전달되는",
			"lineHeight": 1.25,
			"baseline": 294
		},
		{
			"type": "freedraw",
			"version": 24,
			"versionNonce": 1167050233,
			"isDeleted": false,
			"id": "SeJ3G_dxOvcqiA90syyMP",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -515.0706561758109,
			"y": -5106.533342482828,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 13.18527907044097,
			"height": 0,
			"seed": 1279235822,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914310,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.5057422976160524,
					0
				],
				[
					3.982999106473585,
					0
				],
				[
					7.698884319759884,
					0
				],
				[
					11.30370809154374,
					0
				],
				[
					13.18527907044097,
					0
				],
				[
					13.18527907044097,
					0
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 37,
			"versionNonce": 1890742807,
			"isDeleted": false,
			"id": "oNSn96fvjK7EzB-uOWrLt",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -427.6668796354779,
			"y": -5146.453194189305,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 31.577984352707176,
			"height": 21.43020536270342,
			"seed": 1093093614,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914310,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.13238361988931047,
					0
				],
				[
					0.5318811329660207,
					0.2647672397788483
				],
				[
					1.2292013312520567,
					1.3946403965728678
				],
				[
					3.221874211193324,
					3.1178527299171037
				],
				[
					7.769809896063748,
					7.665828874329236
				],
				[
					10.965668622052647,
					10.861687600318874
				],
				[
					14.161527348041545,
					14.343554825390129
				],
				[
					17.57485610975931,
					16.901164283727667
				],
				[
					20.539043500941943,
					18.709463032912026
				],
				[
					23.392169450622077,
					19.49191010657978
				],
				[
					25.49355711865701,
					19.95282520369983
				],
				[
					26.843287424129812,
					20.49178675643452
				],
				[
					28.19301772960256,
					20.867615437715358
				],
				[
					29.918617175897964,
					21.082738820035047
				],
				[
					31.048490332691472,
					21.43020536270342
				],
				[
					31.313257572470093,
					21.43020536270342
				],
				[
					31.445600732817866,
					21.43020536270342
				],
				[
					31.577984352707176,
					21.43020536270342
				],
				[
					31.577984352707176,
					21.43020536270342
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 31,
			"versionNonce": 2138480345,
			"isDeleted": false,
			"id": "o03IG-ohDHVPsw51ZupoO",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -395.9328832906274,
			"y": -5130.944283189199,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 1.1771703608432063,
			"height": 10.46688339405955,
			"seed": 907073582,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914310,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.13234316034868243
				],
				[
					0.5342277863747427,
					0.39711040012662124
				],
				[
					0.6666114062640531,
					0.5294940200165001
				],
				[
					0.9313381865011365,
					0.7942208002532425
				],
				[
					1.1771703608432063,
					2.1652328245709214
				],
				[
					1.1771703608432063,
					3.514963130043725
				],
				[
					1.1771703608432063,
					5.616350798079111
				],
				[
					1.1771703608432063,
					7.453052145418042
				],
				[
					0.9077098142470277,
					8.207096620931225
				],
				[
					0.27658142590564694,
					9.712838918547277
				],
				[
					0.27658142590564694,
					10.199769500872208
				],
				[
					0.27658142590564694,
					10.46688339405955
				],
				[
					0.27658142590564694,
					10.46688339405955
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 31,
			"versionNonce": 1340741431,
			"isDeleted": false,
			"id": "9UEg7K2gNlZiMsSw1dvQ7",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -276.49728772023445,
			"y": -5139.345221473604,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 11.480961342990895,
			"height": 6.989749935346481,
			"seed": 1780689390,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914310,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.8651059170149438,
					-0.13477073283956997
				],
				[
					-1.8934256245657934,
					-0.269501006137034
				],
				[
					-2.297616444460118,
					-0.269501006137034
				],
				[
					-2.5670769910562967,
					-0.269501006137034
				],
				[
					-3.566994100452348,
					-0.269501006137034
				],
				[
					-5.432017126863457,
					-0.269501006137034
				],
				[
					-7.169349840202813,
					1.4631788599263018
				],
				[
					-8.431687535968763,
					2.4725230424992333
				],
				[
					-9.750668589877932,
					3.949903201501911
				],
				[
					-10.317992281225088,
					5.079776358295021
				],
				[
					-11.076770523096684,
					6.320791875674331
				],
				[
					-11.480961342990895,
					6.720248929209447
				],
				[
					-11.480961342990895,
					6.720248929209447
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 26,
			"versionNonce": 214916025,
			"isDeleted": false,
			"id": "AfvEnGWz8NKdXNJpGEcJ8",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -287.71348182344684,
			"y": -5142.106140128135,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 15.097558841360296,
			"height": 13.01741243262859,
			"seed": 526463918,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914310,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.13238361988931047,
					0
				],
				[
					1.5860949470967398,
					2.2621334265368205
				],
				[
					5.42958955437166,
					6.105668493353733
				],
				[
					8.211830387289524,
					8.87132091424428
				],
				[
					9.937348914501854,
					9.93738937404305
				],
				[
					14.965175221470986,
					13.01741243262859
				],
				[
					15.097558841360296,
					13.01741243262859
				],
				[
					15.097558841360296,
					13.01741243262859
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 45,
			"versionNonce": 1865422935,
			"isDeleted": false,
			"id": "DW3OULcJ8OFC6U7x00_Zc",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -271.0108929695534,
			"y": -5131.06719927637,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 24.210018623128803,
			"height": 22.772814788866526,
			"seed": 680071726,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914310,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.2694605465961786,
					0.26472678023765184
				],
				[
					-1.0282387884677746,
					1.614457085709546
				],
				[
					-2.4228791850399602,
					3.252583003215477
				],
				[
					-4.4581559622132545,
					4.8765076216432135
				],
				[
					-7.911620589129711,
					6.758078600541012
				],
				[
					-10.39365162388799,
					6.758078600541012
				],
				[
					-13.251470880385682,
					6.758078600541012
				],
				[
					-18.704769726094355,
					5.5785615862887425
				],
				[
					-20.938541014018597,
					3.8411479538663116
				],
				[
					-23.21722239304222,
					0.42308542578939523
				],
				[
					-24.210018623128803,
					-3.299880207264323
				],
				[
					-24.210018623128803,
					-5.781870782481747
				],
				[
					-24.210018623128803,
					-9.01555917980204
				],
				[
					-24.210018623128803,
					-10.745851932914775
				],
				[
					-22.543571026551717,
					-13.844769597395498
				],
				[
					-20.562671873195995,
					-15.33396394252577
				],
				[
					-18.461284205161064,
					-16.014736188325514
				],
				[
					-16.359815618043058,
					-16.014736188325514
				],
				[
					-13.882558809185525,
					-16.014736188325514
				],
				[
					-11.405302000327993,
					-15.768904013983047
				],
				[
					-8.552256969730934,
					-14.468817565969402
				],
				[
					-4.978141989969117,
					-11.660642166929392
				],
				[
					-3.741941158032205,
					-9.183385358071973
				],
				[
					-2.668711359381973,
					-5.9544307271107755
				],
				[
					-2.1770470106978337,
					-3.4771739182533565
				],
				[
					-2.1770470106978337,
					-2.8105625119897013
				],
				[
					-2.1770470106978337,
					-2.8105625119897013
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 35,
			"versionNonce": 1841134745,
			"isDeleted": false,
			"id": "4kMKvnhF_UZOqF0l_irCi",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -203.12973532782155,
			"y": -5125.164799519667,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 31.42905278033163,
			"height": 19.111307199397743,
			"seed": 876579694,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914310,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.13234316034777294
				],
				[
					0.13238361988931047,
					0.26472678023674234
				],
				[
					0.8864685549433489,
					0.26472678023674234
				],
				[
					2.611987082155565,
					0.26472678023674234
				],
				[
					6.327872295441921,
					-0.33095904972378776
				],
				[
					10.013089176247718,
					-2.054171383068933
				],
				[
					14.154446928273615,
					-4.422672944290753
				],
				[
					18.295804680299398,
					-6.791214965054678
				],
				[
					23.311816801141617,
					-9.859423837513532
				],
				[
					25.895401285142498,
					-11.68188342623398
				],
				[
					27.53352720264786,
					-13.076523822805939
				],
				[
					29.51434543692062,
					-15.062116282979332
				],
				[
					30.788497318813484,
					-17.222655800732355
				],
				[
					31.1359638614814,
					-18.222532450587096
				],
				[
					31.29666916044232,
					-18.711850145862627
				],
				[
					31.42905278033163,
					-18.846580419161
				],
				[
					31.42905278033163,
					-18.846580419161
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 31,
			"versionNonce": 1951987063,
			"isDeleted": false,
			"id": "jCIb5e1ovLn2qFGk5G02W",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -179.72809834448128,
			"y": -5143.472418386094,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 11.722019291432389,
			"height": 11.790598214327474,
			"seed": 405650990,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914310,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.9738611646502022,
					0
				],
				[
					2.323591470123006,
					0
				],
				[
					4.424979138157937,
					0
				],
				[
					6.658750426082179,
					0
				],
				[
					7.278105087838071,
					-0.134730273297464
				],
				[
					7.545218981025414,
					-0.134730273297464
				],
				[
					7.812332874212871,
					-0.134730273297464
				],
				[
					8.218870347515917,
					1.590828713456176
				],
				[
					8.679866363719611,
					3.6922568410327585
				],
				[
					10.022475789882947,
					6.921211471993956
				],
				[
					11.589635671543078,
					11.388754047842667
				],
				[
					11.722019291432389,
					11.65586794103001
				],
				[
					11.722019291432389,
					11.65586794103001
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 37,
			"versionNonce": 1374978425,
			"isDeleted": false,
			"id": "KOduWe3iBVI-A2RP7ILvW",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -136.24606722299393,
			"y": -5017.075435018967,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 8.211830387289524,
			"height": 16.352735198275695,
			"seed": 1280888814,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914310,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.5601199214337385,
					-1.9785120404058034
				],
				[
					-3.2904126745468147,
					-2.6380025673606724
				],
				[
					-3.829333767739172,
					-2.90746311395651
				],
				[
					-4.233605506716458,
					-2.90746311395651
				],
				[
					-4.772526599908815,
					-2.90746311395651
				],
				[
					-5.041987146504994,
					-2.90746311395651
				],
				[
					-5.17671741980314,
					-2.90746311395651
				],
				[
					-5.694356794150167,
					-1.4017208163404575
				],
				[
					-6.233358806425599,
					0.6996668516949285
				],
				[
					-7.268718474202842,
					3.5527928013743804
				],
				[
					-7.268718474202842,
					6.405878291513545
				],
				[
					-7.268718474202842,
					8.507306419090128
				],
				[
					-7.268718474202842,
					11.84736295109542
				],
				[
					-7.268718474202842,
					12.112089731332162
				],
				[
					-7.268718474202842,
					12.244473351221131
				],
				[
					-7.672909294097167,
					12.778701137596727
				],
				[
					-7.942369840693345,
					13.178158191130933
				],
				[
					-8.211830387289524,
					13.445272084319186
				],
				[
					-8.211830387289524,
					13.445272084319186
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 26,
			"versionNonce": 1453928087,
			"isDeleted": false,
			"id": "MK7H03tIznms3_k3DSxde",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -148.10993766703382,
			"y": -5006.821287894278,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 7.613757444378734,
			"height": 0.6216608556233041,
			"seed": 1539309358,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914310,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.1323027008062354,
					0
				],
				[
					0.8863876358601601,
					0
				],
				[
					2.611987082155565,
					-0.21747003572909307
				],
				[
					3.9617173876283687,
					-0.21747003572909307
				],
				[
					6.814762418225428,
					-0.4869305823258401
				],
				[
					7.481373824489538,
					-0.4869305823258401
				],
				[
					7.613757444378734,
					-0.6216608556233041
				],
				[
					7.613757444378734,
					-0.6216608556233041
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 39,
			"versionNonce": 649587289,
			"isDeleted": false,
			"id": "uvcWbHVOuqEmGTNY7JjVq",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -132.8114567424309,
			"y": -5003.256680906776,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 6.105749412436921,
			"height": 4.66611800568262,
			"seed": 1543994798,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914310,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.2694605465961786,
					0
				],
				[
					-0.5390020122754322,
					-0.1347302732983735
				],
				[
					-2.049437616709156,
					-0.269460546596747
				],
				[
					-3.049354726105321,
					-0.702053964645529
				],
				[
					-3.5385915022976633,
					-0.8651463765572771
				],
				[
					-3.808132967976917,
					-0.8651463765572771
				],
				[
					-4.0775935145730955,
					-0.8651463765572771
				],
				[
					-4.566911209848513,
					-0.8651463765572771
				],
				[
					-5.10583230304087,
					-0.8651463765572771
				],
				[
					-5.566747400161489,
					-0.24583217434246762
				],
				[
					-5.970938220055814,
					0.2883956120322182
				],
				[
					-6.105749412436921,
					0.687852665567334
				],
				[
					-6.105749412436921,
					1.3071668677821435
				],
				[
					-6.105749412436921,
					2.0612518028356135
				],
				[
					-6.105749412436921,
					2.548182385160544
				],
				[
					-6.105749412436921,
					2.812909165398196
				],
				[
					-5.973365792547611,
					2.9452927852871653
				],
				[
					-4.95216696430623,
					3.668588009236373
				],
				[
					-3.5811549399882097,
					3.8009716291253426
				],
				[
					-3.314041046800753,
					3.8009716291253426
				],
				[
					-3.314041046800753,
					3.8009716291253426
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 60,
			"versionNonce": 819282871,
			"isDeleted": false,
			"id": "f5fpmUNp3zdoQ-KFGHpls",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -148.14076783768041,
			"y": -5120.035379303915,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 12.979663680380668,
			"height": 13.317662690329598,
			"seed": 828158318,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914310,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.995142883495646
				],
				[
					0,
					3.2076729121163225
				],
				[
					0.7422707489268987,
					4.685053071119
				],
				[
					0.7422707489268987,
					5.439097546631274
				],
				[
					0.9573536717055049,
					6.568970703425293
				],
				[
					1.0897372915948154,
					6.836084596612636
				],
				[
					1.2221209114841258,
					7.1008518363914845
				],
				[
					1.3545045313734363,
					7.3679252700367215
				],
				[
					1.3545045313734363,
					7.5003088899266
				],
				[
					1.4868881512627468,
					7.63269250981557
				],
				[
					1.6475934502236669,
					7.143374814540039
				],
				[
					2.2385455138248744,
					6.2498662993702965
				],
				[
					2.645082987127921,
					4.519573546257561
				],
				[
					2.912196880315264,
					3.0090974822824137
				],
				[
					3.6544676292422764,
					1.4986214183072661
				],
				[
					4.271394718506372,
					0.2505659407015628
				],
				[
					4.403778338395682,
					-0.018935065436380683
				],
				[
					4.403778338395682,
					-0.1536653387347542
				],
				[
					4.536161958284879,
					-0.4231258853305917
				],
				[
					4.536161958284879,
					-0.5578561586289652
				],
				[
					4.668545578174189,
					-0.5602432715786563
				],
				[
					5.635285863514923,
					1.5411848559970167
				],
				[
					6.3752099590331,
					4.018441664855345
				],
				[
					7.859670537803936,
					6.247519645961802
				],
				[
					8.895030205581179,
					7.991973238610626
				],
				[
					9.159716526276725,
					8.526201024985312
				],
				[
					9.159716526276725,
					8.925698538061624
				],
				[
					9.424483766055346,
					9.190425318299276
				],
				[
					9.424483766055346,
					9.322808938188246
				],
				[
					9.556867385944656,
					9.455192558077215
				],
				[
					9.689251005833967,
					9.455192558077215
				],
				[
					9.689251005833967,
					9.185691551940181
				],
				[
					10.925532756853954,
					6.214423740989332
				],
				[
					11.140615679632447,
					4.1082618470536545
				],
				[
					11.355698602411053,
					2.002140412660083
				],
				[
					12.06487344636571,
					-0.10402148127559485
				],
				[
					12.658172163375639,
					-2.4796439218080195
				],
				[
					12.818877462336673,
					-3.1036918903810147
				],
				[
					12.979663680380668,
					-3.5929691261153494
				],
				[
					12.979663680380668,
					-3.7277398589549193
				],
				[
					12.979663680380668,
					-3.8624701322523833
				],
				[
					12.979663680380668,
					-3.8624701322523833
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 50,
			"versionNonce": 1692088121,
			"isDeleted": false,
			"id": "Q7VatEu8ukYeh7IScACCb",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -474.8577560100252,
			"y": -4637.633979666198,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 28.935248018987977,
			"height": 15.468694215823234,
			"seed": 716342382,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914310,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.2978226852093826,
					0.7540444755122735
				],
				[
					-2.295229331509745,
					3.013831248641509
				],
				[
					-4.025522084622764,
					4.07989970844028
				],
				[
					-7.259210481943057,
					5.153089047548747
				],
				[
					-9.36533191633714,
					5.862223431961866
				],
				[
					-14.215864512317637,
					6.933025658120641
				],
				[
					-16.697855087534265,
					7.178857832462199
				],
				[
					-18.803976521928348,
					7.178857832462199
				],
				[
					-19.938623904622546,
					7.178857832462199
				],
				[
					-22.909891715573053,
					5.8598363190121745
				],
				[
					-23.53393968414656,
					5.562013633802053
				],
				[
					-23.803440690284276,
					5.292553087206215
				],
				[
					-23.803440690284276,
					4.888321807769898
				],
				[
					-23.803440690284276,
					2.7822003733763268
				],
				[
					-23.06116994135732,
					-0.31675775064559275
				],
				[
					-22.243320768850538,
					-2.0470505037592375
				],
				[
					-21.10159296638841,
					-3.9380890153743167
				],
				[
					-17.78047149981967,
					-5.616391257620307
				],
				[
					-14.816243649095497,
					-6.2664547113981826
				],
				[
					-11.211460336853236,
					-7.091384303672385
				],
				[
					-6.479150521226188,
					-7.687070133632915
				],
				[
					-1.3709715647765393,
					-8.289836383361035
				],
				[
					2.2338117474657224,
					-8.289836383361035
				],
				[
					4.006667938269288,
					-8.289836383361035
				],
				[
					4.406124991804404,
					-8.289836383361035
				],
				[
					4.538508611693715,
					-8.289836383361035
				],
				[
					4.670892231583025,
					-7.535791907848761
				],
				[
					4.885975154361574,
					-5.323261879228085
				],
				[
					5.131807328703701,
					-3.221874211193608
				],
				[
					5.131807328703701,
					-2.6876464248189222
				],
				[
					5.131807328703701,
					-2.5552628049290433
				],
				[
					5.131807328703701,
					-2.5552628049290433
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "text",
			"version": 46,
			"versionNonce": 1392620759,
			"isDeleted": false,
			"id": "zeCcV0Iy",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -469.58110352264066,
			"y": -4638.71623194261,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 41.07196044921875,
			"height": 20,
			"seed": 1172683186,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914310,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 1,
			"text": "Gibbs",
			"rawText": "Gibbs",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Gibbs",
			"lineHeight": 1.25,
			"baseline": 14
		},
		{
			"type": "text",
			"version": 287,
			"versionNonce": 516024345,
			"isDeleted": false,
			"id": "gaHr29zo",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 596.5779451900742,
			"y": -4947.68762473993,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 345.6479187011719,
			"height": 180,
			"seed": 1609638514,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914310,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 1,
			"text": "왜 하는가?\n\n1. 채널의 주파수 대역을 맞추기 위해서\n\n2. transmitter를 맞추기 위해서\n    - 안테나의 크기는 신호의 반파장이어야 하는데,\n    - 주파수를 크게 하면 파장이 줄어든다\n\n",
			"rawText": "왜 하는가?\n\n1. 채널의 주파수 대역을 맞추기 위해서\n\n2. transmitter를 맞추기 위해서\n    - 안테나의 크기는 신호의 반파장이어야 하는데,\n    - 주파수를 크게 하면 파장이 줄어든다\n\n",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "왜 하는가?\n\n1. 채널의 주파수 대역을 맞추기 위해서\n\n2. transmitter를 맞추기 위해서\n    - 안테나의 크기는 신호의 반파장이어야 하는데,\n    - 주파수를 크게 하면 파장이 줄어든다\n\n",
			"lineHeight": 1.25,
			"baseline": 174
		},
		{
			"type": "freedraw",
			"version": 67,
			"versionNonce": 348324343,
			"isDeleted": false,
			"id": "ITytvav6aOCvln2zUzNNV",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 325.94973622530665,
			"y": -4664.184178171473,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 216.8122445026919,
			"height": 0.3261848238225866,
			"seed": 830268274,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914310,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.1323027008062354,
					0
				],
				[
					0.9951428834954186,
					0
				],
				[
					2.7206614107077485,
					0
				],
				[
					5.197999138648356,
					0
				],
				[
					8.913884351934598,
					0
				],
				[
					12.629769565220954,
					0
				],
				[
					16.610341099202742,
					0
				],
				[
					27.578356374664168,
					0
				],
				[
					32.68653533111387,
					0
				],
				[
					36.667187784178736,
					0
				],
				[
					38.1729300817949,
					0
				],
				[
					38.92701501684883,
					-0.16309241191083856
				],
				[
					41.13950458592785,
					-0.3261848238225866
				],
				[
					43.240892253962784,
					-0.3261848238225866
				],
				[
					46.845675566205045,
					-0.3261848238225866
				],
				[
					52.32972366347724,
					-0.3261848238225866
				],
				[
					60.931584031125226,
					-0.3261848238225866
				],
				[
					65.66389384675222,
					-0.3261848238225866
				],
				[
					70.39620366237932,
					-0.3261848238225866
				],
				[
					75.12851347800631,
					-0.3261848238225866
				],
				[
					79.10916593107117,
					-0.3261848238225866
				],
				[
					85.08010415112699,
					-0.3261848238225866
				],
				[
					89.06075660419185,
					-0.3261848238225866
				],
				[
					93.04140905725683,
					-0.3261848238225866
				],
				[
					97.77371887288382,
					-0.3261848238225866
				],
				[
					104.49639537458484,
					-0.3261848238225866
				],
				[
					108.85283604938923,
					-0.3261848238225866
				],
				[
					112.4576193616316,
					-0.3261848238225866
				],
				[
					116.43827181469646,
					-0.3261848238225866
				],
				[
					120.04305512693873,
					-0.3261848238225866
				],
				[
					127.14151985037927,
					-0.3261848238225866
				],
				[
					131.87391058508933,
					-0.3261848238225866
				],
				[
					136.98200862245596,
					-0.3261848238225866
				],
				[
					141.71439935716603,
					-0.3261848238225866
				],
				[
					149.94039058399142,
					-0.3261848238225866
				],
				[
					155.42435776218053,
					-0.3261848238225866
				],
				[
					160.53253671863024,
					-0.3261848238225866
				],
				[
					164.5131891716951,
					-0.3261848238225866
				],
				[
					168.11797248393736,
					-0.3261848238225866
				],
				[
					172.58559597886892,
					-0.3261848238225866
				],
				[
					176.5661675128507,
					-0.3261848238225866
				],
				[
					181.6743464693003,
					-0.3261848238225866
				],
				[
					187.1583945665726,
					-0.3261848238225866
				],
				[
					195.00851665257528,
					-0.3261848238225866
				],
				[
					200.4925647498476,
					-0.3261848238225866
				],
				[
					205.60074370629718,
					-0.3261848238225866
				],
				[
					210.33305352192417,
					-0.3261848238225866
				],
				[
					214.68949419672867,
					-0.3261848238225866
				],
				[
					216.8122445026919,
					-0.3261848238225866
				],
				[
					216.8122445026919,
					-0.3261848238225866
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 37,
			"versionNonce": 1314880761,
			"isDeleted": false,
			"id": "n1V75BuxcD88E9JsjR_cy",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 398.65771717168184,
			"y": -4840.201997517955,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 141.05256217680267,
			"height": 7.375046149345508,
			"seed": 1363291762,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914310,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.725599446295405,
					-0.4963981150431209
				],
				[
					4.689827297019519,
					-0.4963981150431209
				],
				[
					6.415345824231849,
					-0.4963981150431209
				],
				[
					10.771867418119314,
					-0.7942410300229312
				],
				[
					16.255834596308546,
					-1.1062447845388306
				],
				[
					22.865062543556746,
					-1.7373934026509232
				],
				[
					35.21825068287205,
					-3.0445602704330668
				],
				[
					43.70431584265839,
					-3.701704143979441
				],
				[
					68.75111870373053,
					-6.155332580582581
				],
				[
					80.95776238362077,
					-6.750998180772513
				],
				[
					88.43209624788392,
					-6.750998180772513
				],
				[
					94.66780170771824,
					-6.750998180772513
				],
				[
					104.76828349367293,
					-6.750998180772513
				],
				[
					107.8860957640486,
					-6.750998180772513
				],
				[
					117.23969441334168,
					-7.375046149345508
				],
				[
					126.96673463096556,
					-7.375046149345508
				],
				[
					130.08454690134124,
					-7.375046149345508
				],
				[
					139.06227640981172,
					-7.375046149345508
				],
				[
					141.05256217680267,
					-7.375046149345508
				],
				[
					141.05256217680267,
					-7.375046149345508
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 54,
			"versionNonce": 1729997591,
			"isDeleted": false,
			"id": "cPNITFe_YwpDEMzlP_fUm",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 102.44556447247714,
			"y": -4821.747834192102,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 181.617622192074,
			"height": 1.0282387884681157,
			"seed": 1059327218,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914310,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.7255589867538674,
					0
				],
				[
					3.8269871143303362,
					0
				],
				[
					5.9283747823652675,
					0
				],
				[
					9.157329413326465,
					0
				],
				[
					14.265508369776114,
					0
				],
				[
					24.36603061527228,
					0
				],
				[
					28.23319405434279,
					0
				],
				[
					39.45885569027337,
					0
				],
				[
					46.817353887133436,
					0
				],
				[
					53.800023402712384,
					0
				],
				[
					63.527063620336264,
					0
				],
				[
					69.76276908017064,
					0
				],
				[
					75.62260539918242,
					0
				],
				[
					83.09693926344562,
					0
				],
				[
					85.08722503043646,
					0
				],
				[
					92.18568975387711,
					0
				],
				[
					97.6697378511493,
					0
				],
				[
					103.15378594842161,
					0
				],
				[
					112.50730367863162,
					0
				],
				[
					119.11645070679674,
					0
				],
				[
					125.35215616663118,
					0
				],
				[
					131.5878616264656,
					0
				],
				[
					140.9413793566756,
					0
				],
				[
					146.42542745394792,
					0
				],
				[
					151.1577372695749,
					0
				],
				[
					155.8900470852019,
					-0.29782268520921207
				],
				[
					160.622356900829,
					-0.8935085151697422
				],
				[
					168.09669076509215,
					-0.8935085151697422
				],
				[
					173.20486972154174,
					-0.8935085151697422
				],
				[
					177.56139131542932,
					-0.8935085151697422
				],
				[
					179.442921834785,
					-0.8935085151697422
				],
				[
					179.71003572797235,
					-1.0282387884681157
				],
				[
					179.84241934786166,
					-1.0282387884681157
				],
				[
					180.5965042829157,
					-1.0282387884681157
				],
				[
					181.35050829888667,
					-1.0282387884681157
				],
				[
					181.617622192074,
					-1.0282387884681157
				],
				[
					181.617622192074,
					-1.0282387884681157
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "text",
			"version": 283,
			"versionNonce": 1664579033,
			"isDeleted": false,
			"id": "5xLJkgZS",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1026.566559808847,
			"y": -4493.417542030982,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 388.5438232421875,
			"height": 160,
			"seed": 580924146,
			"groupIds": [
				"g94ixqIAcN-ZKggGAbYUq"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914310,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 1,
			"text": "3. Freauency-division\n- 더 많은 사람들이 이용할 수 있게 한다\n\n4. 노이즈에 강해진다\n근데 AM만 이게 해당이 안 됨\nPM,FM의 경우는 bandwidth를 5배로 늘리는 경우만 해당\n\n아무튼 takeoff가 있다~",
			"rawText": "3. Freauency-division\n- 더 많은 사람들이 이용할 수 있게 한다\n\n4. 노이즈에 강해진다\n근데 AM만 이게 해당이 안 됨\nPM,FM의 경우는 bandwidth를 5배로 늘리는 경우만 해당\n\n아무튼 takeoff가 있다~",
			"textAlign": "right",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "3. Freauency-division\n- 더 많은 사람들이 이용할 수 있게 한다\n\n4. 노이즈에 강해진다\n근데 AM만 이게 해당이 안 됨\nPM,FM의 경우는 bandwidth를 5배로 늘리는 경우만 해당\n\n아무튼 takeoff가 있다~",
			"lineHeight": 1.25,
			"baseline": 154
		},
		{
			"type": "freedraw",
			"version": 43,
			"versionNonce": 646328375,
			"isDeleted": false,
			"id": "x4RbemzLAEVsr6MXAJ1l0",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -975.4840347517368,
			"y": -4374.216227435825,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 78.62935622805571,
			"height": 36.021898556301494,
			"seed": 1212014126,
			"groupIds": [
				"g94ixqIAcN-ZKggGAbYUq"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914310,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.13473027329803244,
					0.2671138931873429
				],
				[
					-1.3686653709091843,
					1.4183092283674341
				],
				[
					-3.8506357163551,
					2.1699665909300165
				],
				[
					-12.457229850362182,
					3.9877328728325665
				],
				[
					-22.45136373140258,
					4.987609522687308
				],
				[
					-35.44988155813678,
					5.668381768487052
				],
				[
					-49.94942814589854,
					5.668381768487052
				],
				[
					-62.94794597263285,
					4.302143970069665
				],
				[
					-71.81455335028863,
					1.4088416956492438
				],
				[
					-71.81455335028863,
					-1.0731488795672703
				],
				[
					-71.27795868073417,
					-3.5551394547837845
				],
				[
					-67.53371132883467,
					-8.8547729617585
				],
				[
					-61.69040273253836,
					-14.698081558054582
				],
				[
					-49.812310759650245,
					-22.61916967990237
				],
				[
					-39.40451852599722,
					-26.644711994295903
				],
				[
					-27.911742996879298,
					-29.015600668468323
				],
				[
					-17.54647374137528,
					-30.022577967862162
				],
				[
					-8.684600130078707,
					-30.353516787814442
				],
				[
					-0.08512687538109276,
					-28.84777449019839
				],
				[
					2.697073497995234,
					-26.365783914981876
				],
				[
					4.687399724527722,
					-22.66881353736062
				],
				[
					5.885851804216259,
					-17.560634580911028
				],
				[
					6.814802877767079,
					-8.207096620930315
				],
				[
					6.814802877767079,
					-3.098917664480723
				],
				[
					6.814802877767079,
					-1.2173466855838342
				],
				[
					6.814802877767079,
					-0.9502327923964913
				],
				[
					6.814802877767079,
					-0.9502327923964913
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "text",
			"version": 71,
			"versionNonce": 274551481,
			"isDeleted": false,
			"id": "p6QpW7hZ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1105.6793170364472,
			"y": -4428.039980359646,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 128.06393432617188,
			"height": 20,
			"seed": 101363822,
			"groupIds": [
				"g94ixqIAcN-ZKggGAbYUq"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914310,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 1,
			"text": "angle modulation",
			"rawText": "angle modulation",
			"textAlign": "right",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "angle modulation",
			"lineHeight": 1.25,
			"baseline": 14
		},
		{
			"type": "text",
			"version": 526,
			"versionNonce": 752947543,
			"isDeleted": false,
			"id": "dP6Pf2UT",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1048.3344678332194,
			"y": -3603.5747422430777,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 451.391845703125,
			"height": 320,
			"seed": 746753970,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914310,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 1,
			"text": "DSB-SC AM\n- 원래 y축에 의해서 쪼개져 있던게 나와서 bandwidth가 두배가 됨\n- cos이 사라져요..\n\nDSB-LC AM\n- carrier(cos)이 살아있어요\n- 간섭을 억제할 수 있음\n\nSSB AM\n- 신호의 절반만 보내요\n\nVSB AM\n- SSB가 현실적인 건 아니니까\n신호의 60%만 보내요\n\n위 모두 analog, digital 상관없이 스펙트럼에 관한 이야기",
			"rawText": "DSB-SC AM\n- 원래 y축에 의해서 쪼개져 있던게 나와서 bandwidth가 두배가 됨\n- cos이 사라져요..\n\nDSB-LC AM\n- carrier(cos)이 살아있어요\n- 간섭을 억제할 수 있음\n\nSSB AM\n- 신호의 절반만 보내요\n\nVSB AM\n- SSB가 현실적인 건 아니니까\n신호의 60%만 보내요\n\n위 모두 analog, digital 상관없이 스펙트럼에 관한 이야기",
			"textAlign": "right",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "DSB-SC AM\n- 원래 y축에 의해서 쪼개져 있던게 나와서 bandwidth가 두배가 됨\n- cos이 사라져요..\n\nDSB-LC AM\n- carrier(cos)이 살아있어요\n- 간섭을 억제할 수 있음\n\nSSB AM\n- 신호의 절반만 보내요\n\nVSB AM\n- SSB가 현실적인 건 아니니까\n신호의 60%만 보내요\n\n위 모두 analog, digital 상관없이 스펙트럼에 관한 이야기",
			"lineHeight": 1.25,
			"baseline": 314
		},
		{
			"type": "freedraw",
			"version": 80,
			"versionNonce": 1517589401,
			"isDeleted": false,
			"id": "c1vX80zjc6gJMhMYRVxoG",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -483.19964359356567,
			"y": -3375.859217731373,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 18.699995500193722,
			"height": 96.05289365248927,
			"seed": 1307002926,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914310,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.1347302732980893,
					0
				],
				[
					-1.8721439057205203,
					1.980858693814298
				],
				[
					-2.694726844586455,
					3.706417680567938
				],
				[
					-4.904869760256588,
					7.13868150772214
				],
				[
					-7.2734117810204,
					11.575515291548982
				],
				[
					-10.4219733029596,
					17.555921044322986
				],
				[
					-13.598937423053542,
					23.905075058610237
				],
				[
					-16.485118818164494,
					30.942122198006473
				],
				[
					-18.387971515906997,
					41.04260398396127
				],
				[
					-18.699995500193722,
					47.27830944379548
				],
				[
					-18.699995500193722,
					53.88749693150248
				],
				[
					-18.699995500193722,
					60.12320239133669
				],
				[
					-17.78993903253786,
					68.34919361816173
				],
				[
					-16.296010921048776,
					73.45737257461178
				],
				[
					-14.556250635217566,
					77.8138537089576
				],
				[
					-13.21364120905423,
					81.04280833991879
				],
				[
					-11.235129168648825,
					84.75869355320538
				],
				[
					-10.24706670492128,
					87.2359503620628
				],
				[
					-8.762606126150388,
					89.71320717092021
				],
				[
					-7.278145547379552,
					91.94228515202667
				],
				[
					-6.041863796359564,
					94.17132267359193
				],
				[
					-5.212159978184218,
					95.43357945027492
				],
				[
					-5.051414219681703,
					96.05289365248927
				],
				[
					-4.91907105933393,
					95.78343310589298
				],
				[
					-4.91907105933393,
					94.05314035278025
				],
				[
					-5.188531605930109,
					90.70600340100691
				],
				[
					-6.646976699496577,
					86.34478850030155
				],
				[
					-8.497838886371824,
					80.48021841493073
				],
				[
					-10.369982792092344,
					74.23977918873743
				],
				[
					-11.930102713526082,
					64.87914057921807
				],
				[
					-12.573045287994546,
					57.5159086159988
				],
				[
					-12.892149692049202,
					54.0222272048004
				],
				[
					-13.863664203290625,
					42.413616008279405
				],
				[
					-13.863664203290625,
					35.426212726340964
				],
				[
					-13.863664203290625,
					22.198410677751326
				],
				[
					-13.863664203290625,
					13.589469890335295
				],
				[
					-13.863664203290625,
					5.618737911028802
				],
				[
					-13.863664203290625,
					4.377762853191143
				],
				[
					-13.731280583401315,
					3.8388013004573622
				],
				[
					-13.140328519800107,
					2.4843372286254635
				],
				[
					-12.60848784637568,
					2.0801464087312524
				],
				[
					-12.47610422648637,
					2.0801464087312524
				],
				[
					-12.343761066138597,
					2.0801464087312524
				],
				[
					-12.211377446249344,
					2.0801464087312524
				],
				[
					-12.211377446249344,
					3.694603494441253
				],
				[
					-12.211377446249344,
					6.658831345165254
				],
				[
					-12.778701137596443,
					10.63944333868858
				],
				[
					-13.719466397274289,
					16.872802145114292
				],
				[
					-15.655414999989091,
					28.474292462325593
				],
				[
					-16.964968980721665,
					36.96031716257039
				],
				[
					-17.934136838554195,
					44.69468450025306
				],
				[
					-17.934136838554195,
					52.429011378394534
				],
				[
					-17.934136838554195,
					62.15605159601819
				],
				[
					-17.934136838554195,
					67.26423055246778
				],
				[
					-17.934136838554195,
					70.49318518342898
				],
				[
					-17.555921044322815,
					71.99892748104503
				],
				[
					-16.986250699566938,
					73.72448646779912
				],
				[
					-15.787798619878401,
					75.4689805199896
				],
				[
					-15.33157682957534,
					76.22302499550187
				],
				[
					-15.066850049338257,
					76.75721232233536
				],
				[
					-14.504260124350253,
					77.88712593867012
				],
				[
					-13.806939926064217,
					79.9885540662467
				],
				[
					-12.60848784637568,
					81.73300765889553
				],
				[
					-12.60848784637568,
					81.86539127878495
				],
				[
					-12.60848784637568,
					81.86539127878495
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 80,
			"versionNonce": 595775095,
			"isDeleted": false,
			"id": "caORztdHkhD3WRBY0ZIm4",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -324.49191311706477,
			"y": -3465.5511431834475,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 41.661918186175626,
			"height": 31.65360323582854,
			"seed": 2124701422,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914310,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.13238361988942415
				],
				[
					0,
					0.7516978221037789
				],
				[
					-1.482113925362114,
					2.065945109653967
				],
				[
					-5.424936707095526,
					4.722882742450565
				],
				[
					-7.155229460208545,
					5.540731914957178
				],
				[
					-8.885522213321508,
					6.195529135094148
				],
				[
					-11.743381929360737,
					6.708434743082307
				],
				[
					-14.97702986713955,
					6.708434743082307
				],
				[
					-20.579219825682173,
					6.708434743082307
				],
				[
					-23.43707954172146,
					6.708434743082307
				],
				[
					-24.812784872857094,
					6.3255256420329715
				],
				[
					-26.131806386307915,
					5.091631003963357
				],
				[
					-28.339602648569212,
					2.4630555097801334
				],
				[
					-29.311117159810635,
					-0.018894605894729466
				],
				[
					-29.807515274853927,
					-2.876754321934186
				],
				[
					-30.02498531058285,
					-4.607047075047376
				],
				[
					-30.02498531058285,
					-8.330012708101549
				],
				[
					-30.02498531058285,
					-11.18787242414055
				],
				[
					-30.02498531058285,
					-14.421520361919647
				],
				[
					-28.78870355956286,
					-16.90351093713616
				],
				[
					-27.05606415304112,
					-19.137322684601713
				],
				[
					-23.96418644878679,
					-21.059069988239116
				],
				[
					-21.111100958648194,
					-21.846210368724314
				],
				[
					-18.63384414979066,
					-22.094429656016473
				],
				[
					-16.532416022214193,
					-22.342608483767435
				],
				[
					-13.192359490208958,
					-22.342608483767435
				],
				[
					-11.090971822174026,
					-22.342608483767435
				],
				[
					-9.365372375878678,
					-21.697319255890307
				],
				[
					-7.384513682064437,
					-19.96463938982697
				],
				[
					-4.479397221517047,
					-16.066726699192714
				],
				[
					-3.0800635181273037,
					-14.234799577754075
				],
				[
					0.22455045549679653,
					-10.031943322601364
				],
				[
					4.450994623362249,
					-3.0871439378952346
				],
				[
					4.583378243251559,
					-1.8248467016705945
				],
				[
					4.583378243251559,
					-1.5577328084832516
				],
				[
					4.583378243251559,
					-0.5838716438333904
				],
				[
					4.583378243251559,
					0.3900299803585767
				],
				[
					3.881324278606371,
					1.5199031371521414
				],
				[
					1.519903137151971,
					3.025645434768194
				],
				[
					-1.8059520957759219,
					4.968714916792578
				],
				[
					-5.153089047549031,
					5.642366283283081
				],
				[
					-10.266001770357775,
					6.545342331171014
				],
				[
					-15.75474317444764,
					7.15049569384928
				],
				[
					-20.491786756433783,
					7.741447757450715
				],
				[
					-26.469805396257527,
					8.025069143582641
				],
				[
					-28.35615060105539,
					8.025069143582641
				],
				[
					-29.965873920406125,
					6.784094085744982
				],
				[
					-31.51891342207199,
					4.174453656998139
				],
				[
					-33.29885003264343,
					0.7209485705402585
				],
				[
					-34.00086353774708,
					-1.385172863853768
				],
				[
					-35.44988155813684,
					-5.746387764559131
				],
				[
					-36.341043419897744,
					-10.48343134654533
				],
				[
					-36.6270519189801,
					-16.461490445910385
				],
				[
					-36.6270519189801,
					-19.31930970240819
				],
				[
					-36.13304091688707,
					-21.801300277624705
				],
				[
					-34.62256485291181,
					-22.883916689910166
				],
				[
					-32.145308044054275,
					-23.6285340922459
				],
				[
					-27.67772500866431,
					-23.6285340922459
				],
				[
					-21.06853752095759,
					-23.6285340922459
				],
				[
					-13.710039324097579,
					-23.6285340922459
				],
				[
					-5.599843305133902,
					-23.302308808881662
				],
				[
					1.7586548917261666,
					-22.34734225012653
				],
				[
					4.767752374008126,
					-21.77767190537088
				],
				[
					5.034866267195525,
					-21.645288285481456
				],
				[
					5.034866267195525,
					-21.645288285481456
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "text",
			"version": 120,
			"versionNonce": 1706080377,
			"isDeleted": false,
			"id": "Jh0qgU65",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 780.2536657406323,
			"y": -5743.767662304612,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 318.9278564453125,
			"height": 20,
			"seed": 745871982,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914310,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 1,
			"text": "가장 중요한 점은 bandwidth는 \"양수\" 부분이다",
			"rawText": "가장 중요한 점은 bandwidth는 \"양수\" 부분이다",
			"textAlign": "right",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "가장 중요한 점은 bandwidth는 \"양수\" 부분이다",
			"lineHeight": 1.25,
			"baseline": 14
		},
		{
			"type": "text",
			"version": 306,
			"versionNonce": 355461015,
			"isDeleted": false,
			"id": "W7YhoNii",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 597.2449636778365,
			"y": -3577.8093576946476,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 436.9278564453125,
			"height": 140,
			"seed": 456929134,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914310,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 1,
			"text": "- 전까지 열심히 한 예제들\n\n- bandwidth가 2배가 됨 ⭐️\n\n- LSB / USB가 나뉘는데, y축에 가까운 기준임 (대칭이 되므로)\n\n- 진폭은 절반이 되는데, 통신에서 상수는 그리 중요하지 않다",
			"rawText": "- 전까지 열심히 한 예제들\n\n- bandwidth가 2배가 됨 ⭐️\n\n- LSB / USB가 나뉘는데, y축에 가까운 기준임 (대칭이 되므로)\n\n- 진폭은 절반이 되는데, 통신에서 상수는 그리 중요하지 않다",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "- 전까지 열심히 한 예제들\n\n- bandwidth가 2배가 됨 ⭐️\n\n- LSB / USB가 나뉘는데, y축에 가까운 기준임 (대칭이 되므로)\n\n- 진폭은 절반이 되는데, 통신에서 상수는 그리 중요하지 않다",
			"lineHeight": 1.25,
			"baseline": 134
		},
		{
			"type": "freedraw",
			"version": 56,
			"versionNonce": 64307545,
			"isDeleted": false,
			"id": "MlyofAWUwm3aoQ_TaYTn8",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -409.139504769227,
			"y": -2912.483755660424,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 51.68443443560005,
			"height": 7.786357848549869,
			"seed": 1825677746,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914310,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.13238361988942415
				],
				[
					0,
					0.7516978221037789
				],
				[
					0.3994975130767102,
					1.1511548756388947
				],
				[
					2.3330994623827337,
					3.2478492368559273
				],
				[
					3.6828297678555373,
					4.0018937123686555
				],
				[
					5.032560073328284,
					4.325731882782293
				],
				[
					6.162433230121849,
					4.807969158289779
				],
				[
					7.623265436638633,
					4.968714916792578
				],
				[
					8.972995742111436,
					5.183797839571071
				],
				[
					10.698554728865247,
					5.614004144669707
				],
				[
					12.799982856441716,
					6.044210449768343
				],
				[
					14.310458920416977,
					6.907010172916216
				],
				[
					15.92730311907718,
					7.2001395513075295
				],
				[
					16.194376552723043,
					7.2001395513075295
				],
				[
					16.593874065799696,
					7.332482711655302
				],
				[
					17.964886090117773,
					7.332482711655302
				],
				[
					19.69044507687164,
					7.493228470158101
				],
				[
					23.03050160887682,
					7.653974228660445
				],
				[
					24.380231914349622,
					7.653974228660445
				],
				[
					24.91445970072442,
					7.786357848549869
				],
				[
					25.668504176236866,
					7.786357848549869
				],
				[
					26.79837733303043,
					7.786357848549869
				],
				[
					29.542748035075363,
					7.786357848549869
				],
				[
					31.26834748137071,
					7.786357848549869
				],
				[
					32.24220864602091,
					7.786357848549869
				],
				[
					32.99625312153336,
					7.786357848549869
				],
				[
					34.01741149023326,
					7.786357848549869
				],
				[
					35.743010936528606,
					7.786357848549869
				],
				[
					38.22026774538614,
					7.299386806683287
				],
				[
					39.945826732140006,
					7.299386806683287
				],
				[
					41.29555703761275,
					7.081916770954194
				],
				[
					41.96216844387686,
					6.812456224357902
				],
				[
					42.95731132737228,
					6.379903265850771
				],
				[
					43.49153911374708,
					6.245132533011201
				],
				[
					44.24558358925958,
					6.110402259712828
				],
				[
					45.35182837379904,
					5.784217435890241
				],
				[
					46.10587284931148,
					5.486354291139378
				],
				[
					46.85995778436552,
					5.053801332631792
				],
				[
					48.58551677111933,
					4.618861261174061
				],
				[
					50.422177658917235,
					4.023175431213986
				],
				[
					51.55209127525228,
					3.6709751221869737
				],
				[
					51.68443443560005,
					3.4015145755906815
				],
				[
					51.68443443560005,
					3.4015145755906815
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 67,
			"versionNonce": 1075633335,
			"isDeleted": false,
			"id": "reEK2XQX-BD4hpwUD2KyL",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -307.77038919773605,
			"y": -2909.8528739723733,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 48.30893534521368,
			"height": 6.6021070679389595,
			"seed": 388298866,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914310,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.1347302732980893,
					0
				],
				[
					0.6193142022143547,
					0.5909520636009802
				],
				[
					1.018811715291065,
					0.8557193033798285
				],
				[
					1.88157097889723,
					0.8557193033798285
				],
				[
					2.1486848720846297,
					0.8557193033798285
				],
				[
					2.548182385161283,
					1.2551763569149443
				],
				[
					2.9476394386964557,
					1.7894041432896302
				],
				[
					3.347136951773166,
					2.056518036476973
				],
				[
					4.10118142728561,
					2.4843776881671147
				],
				[
					4.767792833549663,
					2.8838347417022305
				],
				[
					5.167249887084836,
					3.148601981480624
				],
				[
					5.566747400161546,
					3.2809856013700482
				],
				[
					6.4531754955633005,
					3.5457123816072453
				],
				[
					6.7202893887507,
					3.5457123816072453
				],
				[
					7.653974228660616,
					4.209936674920755
				],
				[
					7.921088121848015,
					4.342320294810179
				],
				[
					9.646647108601883,
					4.772526599908815
				],
				[
					10.400691584114327,
					5.096364770322452
				],
				[
					11.50697682819532,
					5.580948699238888
				],
				[
					12.745605232624087,
					5.826780873580901
				],
				[
					13.364919434838498,
					5.987526632083245
				],
				[
					14.118963910350942,
					6.148272390586044
				],
				[
					15.579796116867726,
					6.308977689546737
				],
				[
					16.333840592380227,
					6.469723448049535
				],
				[
					17.683570897852974,
					6.469723448049535
				],
				[
					19.033301203325777,
					6.469723448049535
				],
				[
					19.652615405540132,
					6.469723448049535
				],
				[
					20.319186352262705,
					6.6021070679389595
				],
				[
					21.66891665773545,
					6.6021070679389595
				],
				[
					23.018646963208255,
					6.6021070679389595
				],
				[
					24.74424640950366,
					6.6021070679389595
				],
				[
					26.580907297301508,
					6.6021070679389595
				],
				[
					27.06783787962661,
					6.6021070679389595
				],
				[
					28.684682078286755,
					6.6021070679389595
				],
				[
					29.218909864661555,
					6.6021070679389595
				],
				[
					30.348783021455063,
					6.6021070679389595
				],
				[
					31.478696637790165,
					6.6021070679389595
				],
				[
					33.847198199012496,
					6.6021070679389595
				],
				[
					34.82109982320418,
					6.6021070679389595
				],
				[
					35.22059733628089,
					6.6021070679389595
				],
				[
					35.97464181179333,
					6.6021070679389595
				],
				[
					37.81130269959118,
					6.3846370322098664
				],
				[
					38.94121631592628,
					6.3846370322098664
				],
				[
					40.66677530268015,
					5.949696960752135
				],
				[
					41.64067692687183,
					5.786604548840842
				],
				[
					42.231588530931504,
					5.162556580267392
				],
				[
					43.472604048310586,
					4.7016010236047805
				],
				[
					44.60247720510415,
					4.349400714578223
				],
				[
					46.079857364107056,
					3.6048237717836855
				],
				[
					46.83390183961956,
					3.3069606270328222
				],
				[
					47.45325650137545,
					2.9807758032102356
				],
				[
					47.85036690150184,
					2.5765445237743734
				],
				[
					48.174205071915594,
					2.0872672880404934
				],
				[
					48.174205071915594,
					2.0872672880404934
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "text",
			"version": 173,
			"versionNonce": 37072441,
			"isDeleted": false,
			"id": "sqFJaB0M",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 595.5530847733237,
			"y": -3137.58988250063,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 298.7998962402344,
			"height": 100,
			"seed": 1079467058,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914310,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 1,
			"text": "Power는 어떻게 계산하나요?\n\n- 결과적으로 u(t)의 power는 요렇게 나온다\n\n- power 손실이 거의 없는 방법",
			"rawText": "Power는 어떻게 계산하나요?\n\n- 결과적으로 u(t)의 power는 요렇게 나온다\n\n- power 손실이 거의 없는 방법",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Power는 어떻게 계산하나요?\n\n- 결과적으로 u(t)의 power는 요렇게 나온다\n\n- power 손실이 거의 없는 방법",
			"lineHeight": 1.25,
			"baseline": 94
		},
		{
			"type": "freedraw",
			"version": 66,
			"versionNonce": 669920727,
			"isDeleted": false,
			"id": "CF3lUJDiIdZSJIAiudJkh",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 810.5304081485035,
			"y": -3074.957055667211,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 262.96541455605325,
			"height": 130.39653042608643,
			"seed": 449929774,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914310,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.13238361988942415,
					0
				],
				[
					0.13238361988942415,
					0.2671138931873429
				],
				[
					0.13238361988942415,
					1.5057422976160524
				],
				[
					0.13238361988942415,
					4.845798829621344
				],
				[
					-0.030749251563520374,
					7.434157539522857
				],
				[
					-1.335569465936942,
					10.287243029661568
				],
				[
					-2.4702168486310256,
					12.388671157237695
				],
				[
					-4.399004112495049,
					15.697978437679467
				],
				[
					-9.188119124431523,
					21.97151356884524
				],
				[
					-12.932326016789375,
					26.959123091532547
				],
				[
					-17.25097747980385,
					31.585064772475107
				],
				[
					-24.784463193785314,
					38.48734117903177
				],
				[
					-29.776766023290293,
					42.85094319268728
				],
				[
					-35.13312380749085,
					47.2546810715412
				],
				[
					-40.85353654638698,
					51.69863573467728
				],
				[
					-50.01559972607265,
					57.378831689291474
				],
				[
					-56.36952796626042,
					60.87016644708092
				],
				[
					-62.723375287365116,
					64.04235634127463
				],
				[
					-69.81949335739705,
					67.90956023988656
				],
				[
					-76.91561142742876,
					71.77672367895684
				],
				[
					-88.67315419632519,
					77.6460275306872
				],
				[
					-96.88263793020587,
					81.58176989265257
				],
				[
					-105.09212166408656,
					85.51747179507674
				],
				[
					-113.67270031288922,
					89.47445541634579
				],
				[
					-126.54352782655178,
					96.07182871792565
				],
				[
					-135.8710705310989,
					100.3999477136581
				],
				[
					-145.90544142619206,
					104.07800325561311
				],
				[
					-160.14493431076357,
					108.37776011273263
				],
				[
					-176.75058210314887,
					114.5590879487495
				],
				[
					-180.99600179599224,
					115.86390816312269
				],
				[
					-189.86262940341885,
					118.48770943140562
				],
				[
					-194.10796817717915,
					119.79252964577881
				],
				[
					-202.59872664378304,
					122.07598525070307
				],
				[
					-217.32753722363032,
					126.22915718885588
				],
				[
					-225.93651847058754,
					128.68751939181857
				],
				[
					-230.29773337129268,
					129.56213330109358
				],
				[
					-237.1408983876729,
					130.12941653289909
				],
				[
					-238.75774258633305,
					130.39653042608643
				],
				[
					-241.61556184283086,
					130.39653042608643
				],
				[
					-244.84925024015115,
					130.39653042608643
				],
				[
					-249.2104651408563,
					130.39653042608643
				],
				[
					-254.81265509939885,
					130.39653042608643
				],
				[
					-256.32317162291565,
					130.39653042608643
				],
				[
					-256.72736244280986,
					130.39653042608643
				],
				[
					-257.9683375006475,
					130.39653042608643
				],
				[
					-260.4574084956321,
					130.39653042608643
				],
				[
					-260.8615993155263,
					130.39653042608643
				],
				[
					-261.2658710545036,
					130.39653042608643
				],
				[
					-261.88991902307725,
					130.39653042608643
				],
				[
					-262.4288401162696,
					130.26180015278806
				],
				[
					-262.56357038956776,
					130.26180015278806
				],
				[
					-262.8330309361638,
					130.12706987949014
				],
				[
					-262.8330309361638,
					130.12706987949014
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 28,
			"versionNonce": 934641433,
			"isDeleted": false,
			"id": "kPqOtFUtuoIDTI8VMlwKE",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 553.7841915593401,
			"y": -2952.387059414415,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 13.29638097148495,
			"height": 18.94582767453585,
			"seed": 797601262,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914310,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.26954146567913995,
					0.13238361988942415
				],
				[
					-2.16053951775325,
					1.0258921350591663
				],
				[
					-4.2667014116887,
					1.9832458067644438
				],
				[
					-6.372863305624378,
					2.6923801911775627
				],
				[
					-8.854813421299468,
					3.680442654905164
				],
				[
					-11.606305002653698,
					5.049067566273152
				],
				[
					-11.741035275951845,
					5.181451186162576
				],
				[
					-11.086238055814874,
					7.03939379280564
				],
				[
					-9.26847177391187,
					9.374839908597096
				],
				[
					-8.25916805088059,
					10.632362918920535
				],
				[
					-6.53591525799402,
					12.625035798861973
				],
				[
					-3.40863545490015,
					15.466347562415194
				],
				[
					1.422962075643909,
					18.94582767453585
				],
				[
					1.5553456955331058,
					18.94582767453585
				],
				[
					1.5553456955331058,
					18.94582767453585
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 167,
			"versionNonce": 1740135159,
			"isDeleted": false,
			"id": "qURmkO1L-coUe0Oy2bY-T",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 532.3917754084273,
			"y": -2979.3154332543845,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 76.82579124523016,
			"height": 71.52850439166468,
			"seed": 1443193902,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914310,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.2694605465958375
				],
				[
					-1.425389648135706,
					-2.1486848720842318
				],
				[
					-2.9925495297959515,
					-3.8222533479711274
				],
				[
					-6.2262379271162445,
					-5.169637000034982
				],
				[
					-7.956530680229207,
					-5.744041111150182
				],
				[
					-9.310954292519455,
					-6.1765940696573125
				],
				[
					-12.658091244292791,
					-6.424813356949926
				],
				[
					-15.515991419873444,
					-6.424813356949926
				],
				[
					-17.997941535548534,
					-6.424813356949926
				],
				[
					-19.728234288661497,
					-6.424813356949926
				],
				[
					-22.58605354515936,
					-6.424813356949926
				],
				[
					-28.188243503701926,
					-6.141151511276348
				],
				[
					-31.421931901022333,
					-5.33746317830537
				],
				[
					-33.65570318894646,
					-4.101181427285155
				],
				[
					-35.78792102762799,
					-1.4041079292901486
				],
				[
					-39.25085318726275,
					4.079899708440735
				],
				[
					-41.574444657385754,
					7.857242965312253
				],
				[
					-43.943027137691104,
					11.998641176879573
				],
				[
					-45.65438482536757,
					15.979253170403354
				],
				[
					-47.649444818259155,
					21.950231850000364
				],
				[
					-48.20495432347917,
					25.555015162242853
				],
				[
					-48.776971321643884,
					29.53562715576618
				],
				[
					-49.618448866404776,
					35.1307366945407
				],
				[
					-49.618448866404776,
					38.3596913255019
				],
				[
					-49.618448866404776,
					41.5886459564631
				],
				[
					-49.618448866404776,
					44.44177190614346
				],
				[
					-49.618448866404776,
					46.54315957417839
				],
				[
					-48.973119178985996,
					49.1315182840799
				],
				[
					-47.335074180563595,
					50.76964420158538
				],
				[
					-44.37553963665704,
					52.65121518048272
				],
				[
					-42.18198513301462,
					53.94895497508787
				],
				[
					-38.57720182077236,
					55.33886160530119
				],
				[
					-31.1028679565091,
					58.02412091716906
				],
				[
					-26.370477221799035,
					59.20602504437147
				],
				[
					-22.389905687817247,
					59.77334873571863
				],
				[
					-19.16091059731457,
					59.77334873571863
				],
				[
					-14.31749888064337,
					59.77334873571863
				],
				[
					-11.088584709223824,
					59.503888189122335
				],
				[
					-7.859589618720975,
					58.42596508365477
				],
				[
					-4.162639470871227,
					56.43094555030484
				],
				[
					0.8651868360980188,
					53.34380161240961
				],
				[
					3.992466639191889,
					50.78145838771252
				],
				[
					6.412999170823014,
					48.3561920897223
				],
				[
					8.625488739902039,
					45.299797403390585
				],
				[
					10.899476812107878,
					41.881775334854865
				],
				[
					13.31766269033028,
					37.031242738874425
				],
				[
					14.390811569897323,
					33.79755434155413
				],
				[
					15.463960449464594,
					30.56390640377549
				],
				[
					16.314905526943676,
					26.57852018435142
				],
				[
					16.894043404417744,
					22.217345743187707
				],
				[
					17.47318128189204,
					17.8561308424828
				],
				[
					17.47318128189204,
					11.502243061836452
				],
				[
					17.47318128189204,
					8.26855466451616
				],
				[
					16.66479964210339,
					3.4180625280769164
				],
				[
					13.355451902120194,
					-0.9691678578324172
				],
				[
					12.008068250056112,
					-2.0470505037587827
				],
				[
					7.167003186793863,
					-5.748774877509277
				],
				[
					3.385007082646098,
					-8.072366347631942
				],
				[
					-0.6807722457999716,
					-10.112336431623135
				],
				[
					-2.673485585282833,
					-10.968015275461312
				],
				[
					-6.020622537055942,
					-11.755155655946055
				],
				[
					-7.155189000666951,
					-11.755155655946055
				],
				[
					-8.133824391217786,
					-11.755155655946055
				],
				[
					-10.615774506892876,
					-11.488041762758712
				],
				[
					-14.714649740311415,
					-9.93738937404305
				],
				[
					-19.82752200357845,
					-7.538138561257256
				],
				[
					-25.44387280165705,
					-4.422672944290298
				],
				[
					-30.013130664914286,
					-1.0755359925174162
				],
				[
					-35.21825068287211,
					3.243115470497287
				],
				[
					-37.719135863983695,
					6.008767891387379
				],
				[
					-39.335980062643955,
					9.237722522348577
				],
				[
					-40.41382224902867,
					12.466677153309774
				],
				[
					-41.8510260832914,
					18.81344405464688
				],
				[
					-42.13707504191524,
					22.794096507711856
				],
				[
					-42.13707504191524,
					26.77474896077638
				],
				[
					-42.13707504191524,
					30.75536095430016
				],
				[
					-41.39715094639706,
					34.847115308408775
				],
				[
					-40.4728931796638,
					36.948502976443706
				],
				[
					-38.98843260089296,
					39.17758095755016
				],
				[
					-37.97912887786168,
					40.68332325516667
				],
				[
					-36.62939857238888,
					41.43736773067894
				],
				[
					-32.91351335910264,
					42.91948165604117
				],
				[
					-30.812125691067706,
					43.34730084818966
				],
				[
					-27.20726145974237,
					44.18173843272416
				],
				[
					-22.09916342237574,
					44.779770916093184
				],
				[
					-16.990984465926203,
					45.37780339946221
				],
				[
					-9.892519742485547,
					45.96875546306319
				],
				[
					-5.5359981485980825,
					45.96875546306319
				],
				[
					-1.1795574737936931,
					45.96875546306319
				],
				[
					2.8010949792712836,
					45.11307661922501
				],
				[
					6.498126046204106,
					43.11801662633343
				],
				[
					12.752685652391847,
					37.4260064855921
				],
				[
					14.173301074627034,
					36.003003950406764
				],
				[
					16.66949294892106,
					33.23261776315758
				],
				[
					20.22467286324627,
					26.94257513904722
				],
				[
					20.491786756433612,
					25.32573094038662
				],
				[
					20.758900649621182,
					20.47519834440618
				],
				[
					20.758900649621182,
					18.482525464465198
				],
				[
					20.758900649621182,
					14.497179704582777
				],
				[
					17.88449298109572,
					8.814596637017985
				],
				[
					14.575145241112523,
					4.607047075047376
				],
				[
					10.611081200075205,
					0.6429425744686341
				],
				[
					6.465030141231864,
					-1.72555898675364
				],
				[
					1.2386284044287095,
					-3.642612983573599
				],
				[
					-1.9950599928915835,
					-4.720495629499965
				],
				[
					-4.852879249389389,
					-5.238175463388416
				],
				[
					-8.086567646709682,
					-5.238175463388416
				],
				[
					-11.696044265769615,
					-5.238175463388416
				],
				[
					-19.177499009342228,
					-4.335199415500483
				],
				[
					-25.417897775994163,
					-2.1558057513939275
				],
				[
					-30.970484336619904,
					0.6193142022148095
				],
				[
					-35.5444355066947,
					3.9687978073966406
				],
				[
					-39.81340265270916,
					7.928168541616287
				],
				[
					-44.488988191109854,
					13.47363422293256
				],
				[
					-46.8575706714152,
					17.61503243449988
				],
				[
					-47.99691136092707,
					21.595644428023206
				],
				[
					-49.15988042269288,
					25.95212556236902
				],
				[
					-49.457743567443856,
					30.308606696715287
				],
				[
					-49.457743567443856,
					36.27954491677065
				],
				[
					-49.1906296742564,
					39.508499547731844
				],
				[
					-48.11748079468924,
					42.73745417869304
				],
				[
					-45.621288920395216,
					45.50310659958359
				],
				[
					-41.04733775032042,
					48.190753024402056
				],
				[
					-36.31502793469332,
					49.37261669206282
				],
				[
					-30.4551916156816,
					50.28979403902804
				],
				[
					-23.8459636684334,
					50.91618866101044
				],
				[
					-12.620302032502877,
					51.232946411656485
				],
				[
					-5.261844295184346,
					51.232946411656485
				],
				[
					0.22220380208796087,
					51.232946411656485
				],
				[
					4.57864447689235,
					50.94693791257396
				],
				[
					9.606470783861596,
					47.29251074287322
				],
				[
					12.504506824641112,
					43.51043371964215
				],
				[
					15.459267142646922,
					39.364301741715735
				],
				[
					17.823075397051753,
					35.21821022333097
				],
				[
					19.196434074778608,
					31.608693144729386
				],
				[
					20.354709829726744,
					24.878976682802204
				],
				[
					20.354709829726744,
					19.766063959993062
				],
				[
					19.4399195957119,
					14.277322555903538
				],
				[
					17.035894557025358,
					9.164450292636047
				],
				[
					12.157040281973195,
					2.151031525493636
				],
				[
					5.391800342581519,
					-3.990079526241516
				],
				[
					0.2150829227784925,
					-6.734450228286278
				],
				[
					-4.521920199666056,
					-8.807516217249486
				],
				[
					-6.514633539148917,
					-9.37718656200559
				],
				[
					-9.372452795646723,
					-9.646647108601428
				],
				[
					-11.854402911321813,
					-9.646647108601428
				],
				[
					-18.95998851407171,
					-9.024986252978579
				],
				[
					-26.748693016030472,
					-6.4271600103584205
				],
				[
					-35.28436157373375,
					-2.817642931757291
				],
				[
					-45.23837981934622,
					3.264397189342617
				],
				[
					-50.2306826488512,
					7.315934759169522
				],
				[
					-53.78820921658536,
					10.563824455567556
				],
				[
					-56.06689059560898,
					13.977112757743726
				],
				[
					-56.06689059560898,
					13.977112757743726
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "text",
			"version": 72,
			"versionNonce": 1388852217,
			"isDeleted": false,
			"id": "KHu9pbTm",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 743.5955182640978,
			"y": -3002.53354575734,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 189.3919219970703,
			"height": 20,
			"seed": 1037417838,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914311,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 1,
			"text": "외워도 좋지만 계산도 해봐...",
			"rawText": "외워도 좋지만 계산도 해봐...",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "외워도 좋지만 계산도 해봐...",
			"lineHeight": 1.25,
			"baseline": 14
		},
		{
			"type": "text",
			"version": 618,
			"versionNonce": 1140843543,
			"isDeleted": false,
			"id": "r6piIJBX",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 593.0861856070983,
			"y": -2697.905788189924,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 341.59991455078125,
			"height": 260,
			"seed": 904297138,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914311,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 1,
			"text": "이상적인 채널이란?\n- 크기가 상수\n- 위상의 변화가 linear -> 노이즈 감지 때문\n\n- u(t)를 받아서 다시 modulation을 하면 됨\n    - 이게 왜 그러냐면 modulation을 다시 할 때\n    - 원래 신호 성분이 0으로 가기 때문\n    - 요걸 LPF 같은 걸로 빼내면 된다\n\n- 하지만 time delay가 phase의 형태로 나타남\n    다를 경우는 문제가 없지만, (상수임)\n    phi = 90이라면 ? (cos phi = 0)\n    요걸 phase-coherent라고 함",
			"rawText": "이상적인 채널이란?\n- 크기가 상수\n- 위상의 변화가 linear -> 노이즈 감지 때문\n\n- u(t)를 받아서 다시 modulation을 하면 됨\n    - 이게 왜 그러냐면 modulation을 다시 할 때\n    - 원래 신호 성분이 0으로 가기 때문\n    - 요걸 LPF 같은 걸로 빼내면 된다\n\n- 하지만 time delay가 phase의 형태로 나타남\n    다를 경우는 문제가 없지만, (상수임)\n    phi = 90이라면 ? (cos phi = 0)\n    요걸 phase-coherent라고 함",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "이상적인 채널이란?\n- 크기가 상수\n- 위상의 변화가 linear -> 노이즈 감지 때문\n\n- u(t)를 받아서 다시 modulation을 하면 됨\n    - 이게 왜 그러냐면 modulation을 다시 할 때\n    - 원래 신호 성분이 0으로 가기 때문\n    - 요걸 LPF 같은 걸로 빼내면 된다\n\n- 하지만 time delay가 phase의 형태로 나타남\n    다를 경우는 문제가 없지만, (상수임)\n    phi = 90이라면 ? (cos phi = 0)\n    요걸 phase-coherent라고 함",
			"lineHeight": 1.25,
			"baseline": 254
		},
		{
			"type": "freedraw",
			"version": 100,
			"versionNonce": 1735478489,
			"isDeleted": false,
			"id": "2iXVLwFUlvkIhKBbSj4Yv",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 358.6835080711576,
			"y": -2573.1181033169623,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 20.432634906715407,
			"height": 8.828757476553164,
			"seed": 84986734,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914311,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.1323027008062354,
					0
				],
				[
					0.6641838337721993,
					0
				],
				[
					0.9289510735507065,
					-0.13473027329791876
				],
				[
					1.3284485866274736,
					-0.13473027329791876
				],
				[
					1.9477223293002908,
					-0.13473027329791876
				],
				[
					2.4796034622662546,
					-0.2694605465958375
				],
				[
					3.013831248641054,
					-0.2694605465958375
				],
				[
					3.5480590350158536,
					-0.2694605465958375
				],
				[
					4.302063050986817,
					-0.2694605465958375
				],
				[
					4.968674457250813,
					-0.2694605465958375
				],
				[
					5.101058077140124,
					-0.2694605465958375
				],
				[
					5.500555590216777,
					-0.2694605465958375
				],
				[
					5.767669483404234,
					-0.2694605465958375
				],
				[
					5.899972184210469,
					-0.2694605465958375
				],
				[
					6.566583590474579,
					-0.2694605465958375
				],
				[
					6.698967210363776,
					-0.2694605465958375
				],
				[
					6.831350830253086,
					-0.2694605465958375
				],
				[
					7.58535484622405,
					-0.2694605465958375
				],
				[
					7.984852359300703,
					-0.2694605465958375
				],
				[
					8.51673349226678,
					-0.2694605465958375
				],
				[
					9.136007234939598,
					-0.2694605465958375
				],
				[
					9.268390854828908,
					-0.2694605465958375
				],
				[
					9.802618641203708,
					-0.2694605465958375
				],
				[
					10.202116154280361,
					-0.2694605465958375
				],
				[
					10.469230047467704,
					-0.2694605465958375
				],
				[
					10.601613667357014,
					-0.2694605465958375
				],
				[
					11.596756550852433,
					-0.2694605465958375
				],
				[
					11.861523790631054,
					-0.2694605465958375
				],
				[
					12.395751577005854,
					-0.2694605465958375
				],
				[
					12.662865470193196,
					-0.2694605465958375
				],
				[
					12.929979363380653,
					-0.2694605465958375
				],
				[
					12.795168170999432,
					-0.2694605465958375
				],
				[
					12.256247077807075,
					-0.00238711295014582
				],
				[
					11.44074455870907,
					0.6453296874187799
				],
				[
					10.681966316837475,
					0.9384186062693516
				],
				[
					10.008314950347085,
					1.337916119345664
				],
				[
					9.604043211369685,
					1.6050300125334616
				],
				[
					9.334582664773507,
					1.7373731728812345
				],
				[
					8.306343876305732,
					2.3259785830732653
				],
				[
					8.036883329709553,
					2.5907053633104624
				],
				[
					7.632692509815342,
					2.8578192564978053
				],
				[
					7.008644541241779,
					3.1509486348895734
				],
				[
					6.14345770514376,
					3.366031557668066
				],
				[
					6.0087274318457276,
					3.49841517755749
				],
				[
					5.604536611951403,
					3.763141957794687
				],
				[
					5.469806338653257,
					3.763141957794687
				],
				[
					5.335076065355224,
					3.763141957794687
				],
				[
					4.9308852454609,
					3.8955255776836566
				],
				[
					4.796074053079792,
					4.1626394708709995
				],
				[
					4.9284576729691025,
					4.295023090760424
				],
				[
					5.949656501210484,
					4.295023090760424
				],
				[
					6.923517665860686,
					4.295023090760424
				],
				[
					7.677602600914611,
					4.295023090760424
				],
				[
					8.672745484410143,
					4.427406710649848
				],
				[
					10.022475789882833,
					4.427406710649848
				],
				[
					11.043593699041253,
					4.692133490887045
				],
				[
					11.797678634095178,
					4.824517110776014
				],
				[
					12.927551790888742,
					4.956860271123787
				],
				[
					13.32704930396551,
					4.956860271123787
				],
				[
					13.858930436931473,
					5.089243891013211
				],
				[
					13.991314056820784,
					5.089243891013211
				],
				[
					13.988886484328873,
					5.4887414040899785
				],
				[
					12.989050294015783,
					6.051331329078039
				],
				[
					11.499815489344314,
					6.427160010358875
				],
				[
					10.87576752077075,
					6.587905768861674
				],
				[
					10.47157670087654,
					6.855019662049017
				],
				[
					9.712798459004944,
					7.148108580899134
				],
				[
					8.578151076310746,
					7.495615583108702
				],
				[
					8.039229983118389,
					7.762689016754393
				],
				[
					7.365578616627886,
					8.16218652983116
				],
				[
					6.961387796733675,
					8.294570149720585
				],
				[
					6.557116057756275,
					8.426913310068358
				],
				[
					6.422385784458243,
					8.559296929957327
				],
				[
					6.554769404347439,
					8.559296929957327
				],
				[
					6.954266917424206,
					8.559296929957327
				],
				[
					7.708351852478131,
					8.559296929957327
				],
				[
					8.682213017128333,
					8.559296929957327
				],
				[
					10.031943322601137,
					8.341826894228689
				],
				[
					12.244432891680049,
					8.341826894228689
				],
				[
					14.721689700537581,
					8.341826894228689
				],
				[
					16.071420006010385,
					8.341826894228689
				],
				[
					17.79701945230579,
					8.341826894228689
				],
				[
					18.551023468276753,
					8.341826894228689
				],
				[
					20.1678676669369,
					8.341826894228689
				],
				[
					20.30025128682621,
					8.341826894228689
				],
				[
					20.432634906715407,
					8.341826894228689
				],
				[
					20.432634906715407,
					8.341826894228689
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 89,
			"versionNonce": 2092517687,
			"isDeleted": false,
			"id": "8tN-5_ucHUm0CfOe8pgNY",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 557.0273474893789,
			"y": -2443.986216780509,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 135.07215642402855,
			"height": 44.71596621909839,
			"seed": 1901197230,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914311,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.26476723977862093,
					0.39949751307676706
				],
				[
					0.26476723977862093,
					0.5318811329661912
				],
				[
					0.26476723977862093,
					1.0660684597992258
				],
				[
					0.26476723977862093,
					1.9524965552009235
				],
				[
					-0.004693306817557641,
					2.486724341576064
				],
				[
					-1.0873097191030183,
					3.9972004055512116
				],
				[
					-3.6756684290045314,
					5.566747400161603
				],
				[
					-11.873337976758194,
					7.332523171197408
				],
				[
					-18.113736743410186,
					7.951837373411763
				],
				[
					-27.09858713119013,
					8.873708027194425
				],
				[
					-30.21874605497453,
					9.183344898530777
				],
				[
					-34.95583009650227,
					9.774296962132212
				],
				[
					-39.69283321894693,
					9.774296962132212
				],
				[
					-44.05404811965195,
					9.774296962132212
				],
				[
					-48.79113216117969,
					9.774296962132212
				],
				[
					-56.64837512649183,
					9.774296962132212
				],
				[
					-61.38545916801945,
					10.069772993932474
				],
				[
					-66.12246229046411,
					10.365249025733192
				],
				[
					-70.48367719116925,
					10.365249025733192
				],
				[
					-77.58926279391926,
					10.365249025733192
				],
				[
					-82.32634683544688,
					10.365249025733192
				],
				[
					-87.06334995789155,
					10.365249025733192
				],
				[
					-91.80043399941928,
					10.365249025733192
				],
				[
					-95.7857797593017,
					9.793232027568592
				],
				[
					-101.01218149610486,
					8.429300423018503
				],
				[
					-103.87000075260255,
					7.393981214782798
				],
				[
					-106.35195086827764,
					5.90478686965298
				],
				[
					-109.04671817240558,
					3.748981118258598
				],
				[
					-113.08878820951452,
					0.5153331804799564
				],
				[
					-115.42896809166518,
					-1.555386155074757
				],
				[
					-117.4996065081366,
					-3.8955255776836566
				],
				[
					-118.98884131280806,
					-5.88111803785705
				],
				[
					-119.63886430704451,
					-7.611410790969785
				],
				[
					-120.29131487377265,
					-10.206890380180994
				],
				[
					-120.29131487377265,
					-12.31301181457502
				],
				[
					-120.29131487377265,
					-14.043304567687755
				],
				[
					-120.07615103191108,
					-15.773597320800945
				],
				[
					-118.09767945104716,
					-19.248384126104156
				],
				[
					-116.11678029769143,
					-21.23397658627755
				],
				[
					-109.55254336062569,
					-24.78442273424389
				],
				[
					-105.57189090756083,
					-26.495780421920244
				],
				[
					-92.61358986510845,
					-30.08405624121815
				],
				[
					-86.75375354609662,
					-31.317950879287764
				],
				[
					-81.26970544882442,
					-31.927797548783474
				],
				[
					-73.41950244373868,
					-33.13098339483122
				],
				[
					-67.93553526554945,
					-33.74083006432738
				],
				[
					-62.451487168277254,
					-34.3507171933652
				],
				[
					-53.84962680062927,
					-34.3507171933652
				],
				[
					-51.10768367107619,
					-34.3507171933652
				],
				[
					-43.25748066599044,
					-34.3507171933652
				],
				[
					-37.77343256871825,
					-34.3507171933652
				],
				[
					-31.16428554055301,
					-34.03395944271915
				],
				[
					-23.805746884151517,
					-33.074259117604925
				],
				[
					-12.58008524822094,
					-30.511875433366185
				],
				[
					-5.970938220055814,
					-28.625570688109747
				],
				[
					-0.11110190104398043,
					-26.779442267593822
				],
				[
					5.372946196228213,
					-24.954595565922773
				],
				[
					9.729386871032716,
					-23.214835280091847
				],
				[
					13.60128407646232,
					-21.28835421009535
				],
				[
					13.866051316240942,
					-21.023627429858152
				],
				[
					14.133165209428284,
					-20.269542494804227
				],
				[
					14.7808415502559,
					-19.134935571651567
				],
				[
					14.7808415502559,
					-16.170748180468763
				],
				[
					14.7808415502559,
					-13.693491371611344
				],
				[
					14.7808415502559,
					-11.592063244034762
				],
				[
					13.818794571732838,
					-9.738854403750793
				],
				[
					12.911044297944159,
					-8.013254957455501
				],
				[
					10.034370895093048,
					-4.077553055031331
				],
				[
					7.471987210854422,
					-0.6642242933135094
				],
				[
					5.989873285492308,
					0.6500634537778751
				],
				[
					2.174700357288998,
					2.9594940843649056
				],
				[
					-1.9713507015544565,
					5.323261879228539
				],
				[
					-7.462519678136118,
					8.779154078636566
				],
				[
					-8.809822411117011,
					9.854690071153982
				],
				[
					-9.433870379690575,
					9.854690071153982
				],
				[
					-9.433870379690575,
					9.854690071153982
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "text",
			"version": 54,
			"versionNonce": 1027885497,
			"isDeleted": false,
			"id": "KibxUpXJ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 473.4059716486091,
			"y": -2501.988125409377,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 104.87997436523438,
			"height": 20,
			"seed": 1377093998,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914311,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 1,
			"text": "파워도 손실나네",
			"rawText": "파워도 손실나네",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "파워도 손실나네",
			"lineHeight": 1.25,
			"baseline": 14
		},
		{
			"type": "text",
			"version": 336,
			"versionNonce": 1598622295,
			"isDeleted": false,
			"id": "biOHXWpg",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -957.2080343881416,
			"y": -2239.5242919921875,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 360.0798645019531,
			"height": 140,
			"seed": 1141428398,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914311,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 1,
			"text": "PLL\n- pilot signal이 필요하지 않은 사인함수를 보내는 것\n\nPilot tone = pilot signal\n- referene가 되는 시그널\n- 노이즈를 잡기 위한 기준이 되는 시그널\n- 송수신 측 모두 알고 있음",
			"rawText": "PLL\n- pilot signal이 필요하지 않은 사인함수를 보내는 것\n\nPilot tone = pilot signal\n- referene가 되는 시그널\n- 노이즈를 잡기 위한 기준이 되는 시그널\n- 송수신 측 모두 알고 있음",
			"textAlign": "right",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "PLL\n- pilot signal이 필요하지 않은 사인함수를 보내는 것\n\nPilot tone = pilot signal\n- referene가 되는 시그널\n- 노이즈를 잡기 위한 기준이 되는 시그널\n- 송수신 측 모두 알고 있음",
			"lineHeight": 1.25,
			"baseline": 134
		},
		{
			"type": "text",
			"version": 521,
			"versionNonce": 1566878361,
			"isDeleted": false,
			"id": "4xwsbrAu",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 590.5500489706344,
			"y": -2245.2072126913877,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 399.4078674316406,
			"height": 200,
			"seed": 2031926322,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914311,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 1,
			"text": "DSB-SC의 강점인 부분\n\nEnvelope detector\n- 다이오드와 RC로 이루어진 회로를 이용해 신호를 detect\n- 회로로 통과한 신호 (양수 부분만 존재)를 외곽선만 따옴\n- 편지봉투 뜯는거 같다해서 envelope\n\n- 다만 RC값 설정하는 게 귀찮음\n    - 너무크면 신호를 못따라가고\n    - 너무 작으면 신호가 뭔지 알 수가 없음 (왜곡)",
			"rawText": "DSB-SC의 강점인 부분\n\nEnvelope detector\n- 다이오드와 RC로 이루어진 회로를 이용해 신호를 detect\n- 회로로 통과한 신호 (양수 부분만 존재)를 외곽선만 따옴\n- 편지봉투 뜯는거 같다해서 envelope\n\n- 다만 RC값 설정하는 게 귀찮음\n    - 너무크면 신호를 못따라가고\n    - 너무 작으면 신호가 뭔지 알 수가 없음 (왜곡)",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "DSB-SC의 강점인 부분\n\nEnvelope detector\n- 다이오드와 RC로 이루어진 회로를 이용해 신호를 detect\n- 회로로 통과한 신호 (양수 부분만 존재)를 외곽선만 따옴\n- 편지봉투 뜯는거 같다해서 envelope\n\n- 다만 RC값 설정하는 게 귀찮음\n    - 너무크면 신호를 못따라가고\n    - 너무 작으면 신호가 뭔지 알 수가 없음 (왜곡)",
			"lineHeight": 1.25,
			"baseline": 194
		},
		{
			"type": "freedraw",
			"version": 27,
			"versionNonce": 411281271,
			"isDeleted": false,
			"id": "u2fjfK8-umTKUBqdO5ExY",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 615.2932538091784,
			"y": -2073.713812966632,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 54.06631689694609,
			"height": 11.813209010127594,
			"seed": 403181102,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914311,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.0847007143837573,
					-0.27260822331300005
				],
				[
					-2.978501012288234,
					-0.27260822331300005
				],
				[
					-6.561569349742513,
					-0.27260822331300005
				],
				[
					-11.229389128827279,
					0.6016758721088991
				],
				[
					-13.8699959514081,
					1.4759599675307982
				],
				[
					-19.337987318609066,
					3.6571808447597505
				],
				[
					-26.219645594496797,
					5.180520060629533
				],
				[
					-35.599671493454935,
					7.794495078737327
				],
				[
					-41.0676628606559,
					9.246714694852017
				],
				[
					-46.53565422785698,
					10.328422501685509
				],
				[
					-51.53238947399791,
					11.039719953731037
				],
				[
					-53.89739516571581,
					11.374621235887844
				],
				[
					-54.06631689694609,
					11.540600786814593
				],
				[
					-54.06631689694609,
					11.540600786814593
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 28,
			"versionNonce": 1619390329,
			"isDeleted": false,
			"id": "OagAZQ0Vh2DCjN4rFjclH",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 571.3389569798553,
			"y": -2072.8572834075258,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 14.685030622782847,
			"height": 17.458999376716747,
			"seed": 2114908718,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914311,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.5008808330835564
				],
				[
					-0.6223725887282399,
					2.6643471739971574
				],
				[
					-3.218542343273839,
					5.281264372408714
				],
				[
					-5.462056279347053,
					8.233082852977077
				],
				[
					-6.280033131025448,
					9.45413840626361
				],
				[
					-6.617876593486017,
					10.289869794257811
				],
				[
					-6.617876593486017,
					10.455849345184106
				],
				[
					-6.617876593486017,
					11.125651909498174
				],
				[
					-3.4437713182476273,
					13.41953800146075
				],
				[
					-0.809048856274103,
					13.955927907175464
				],
				[
					2.768084393326262,
					15.248103060217545
				],
				[
					5.4028068552997865,
					16.137199511651033
				],
				[
					7.121750334119724,
					16.922558743755417
				],
				[
					8.06715402929683,
					17.458999376716747
				],
				[
					8.06715402929683,
					17.458999376716747
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 31,
			"versionNonce": 1185783959,
			"isDeleted": false,
			"id": "gNWl5GGNn_dRCNMWCb0Dl",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 614.0721982558916,
			"y": -2052.5916976573017,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 61.06652474817474,
			"height": 106.5945329492572,
			"seed": 810475630,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914311,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5778847934461737,
					0.7764819639469351
				],
				[
					-3.5119487376991856,
					3.055555699897468
				],
				[
					-6.0162514486236205,
					5.216079860507307
				],
				[
					-11.718349058956164,
					10.930047646548019
				],
				[
					-14.436061296393063,
					14.311627360444618
				],
				[
					-19.572093561740758,
					21.021370997551685
				],
				[
					-24.829668309979752,
					29.50342317691866
				],
				[
					-29.648604556732607,
					37.929117385295285
				],
				[
					-37.36898712816458,
					51.321972855036165
				],
				[
					-42.279790418538596,
					61.14363016303059
				],
				[
					-47.63511657100594,
					71.43050704973803
				],
				[
					-51.73093591725194,
					81.25216435773245
				],
				[
					-54.89022883647863,
					89.53856154690266
				],
				[
					-58.716331412468776,
					99.85217169257635
				],
				[
					-60.106308696985934,
					104.37176645704994
				],
				[
					-60.728681285714174,
					106.25963166710017
				],
				[
					-61.06652474817474,
					106.5945329492572
				],
				[
					-61.06652474817474,
					106.5945329492572
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 24,
			"versionNonce": 2095814745,
			"isDeleted": false,
			"id": "WkckquQBYSOlaorynifRJ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 549.4759195064557,
			"y": -1961.4675545629318,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 17.989555649070326,
			"height": 17.4619922842669,
			"seed": 1894030702,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914311,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.16597955092652228
				],
				[
					0,
					1.2476873577600145
				],
				[
					0,
					6.988337675520597
				],
				[
					0,
					9.012557724473936
				],
				[
					0.6431200325939699,
					14.61391102302764
				],
				[
					1.4552125236648408,
					15.425952786851894
				],
				[
					4.90192602221623,
					17.12709100211009
				],
				[
					7.5366484841897545,
					17.4619922842669
				],
				[
					11.585037854850043,
					17.4619922842669
				],
				[
					17.989555649070326,
					16.323926506443286
				],
				[
					17.989555649070326,
					16.323926506443286
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 86,
			"versionNonce": 1266382263,
			"isDeleted": false,
			"id": "hJ3Gm_280ePejJyvA2TCa",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 321.11291378227617,
			"y": -1849.9682041384003,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 251.92127168860628,
			"height": 75.71893775138369,
			"seed": 1183345326,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914311,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.16592882368001938,
					0.3349012821568067
				],
				[
					0.16592882368001938,
					0.9454036951769922
				],
				[
					-1.1854957534092136,
					3.7134880885032544
				],
				[
					-3.8261025759902054,
					4.925615646385722
				],
				[
					-12.731980900831275,
					7.480290513199634
				],
				[
					-25.73362784467173,
					10.829252607522449
				],
				[
					-43.44154582053159,
					14.27895901362399
				],
				[
					-64.91930985588476,
					17.782030483165272
				],
				[
					-84.04094546767794,
					20.387128233115163
				],
				[
					-108.01413494579793,
					22.09714371653081
				],
				[
					-114.27935572081145,
					22.51204186660084
				],
				[
					-130.24763350123203,
					22.51204186660084
				],
				[
					-140.42189590045245,
					22.51204186660084
				],
				[
					-157.33263519574635,
					22.51204186660084
				],
				[
					-168.44938447346343,
					21.68518774676477
				],
				[
					-178.15246684249377,
					20.873145982940514
				],
				[
					-186.44482448314113,
					20.08185166298199
				],
				[
					-193.79771351646548,
					18.9260313488428
				],
				[
					-204.12017556667368,
					15.867482741395179
				],
				[
					-210.53062844874802,
					13.235753186971806
				],
				[
					-211.4819672317791,
					12.826790124755917
				],
				[
					-212.0598773888486,
					12.044373072955295
				],
				[
					-213.57134642901042,
					10.017210843698194
				],
				[
					-214.92870609395368,
					8.11747545793969
				],
				[
					-217.49821868040272,
					5.156779709213424
				],
				[
					-220.52709184858034,
					1.7693156347093009
				],
				[
					-223.2003162907352,
					-1.3069875090541245
				],
				[
					-225.3489956392603,
					-5.619158562115899
				],
				[
					-225.8646634647323,
					-7.788559990883641
				],
				[
					-225.8646634647323,
					-9.486756025837622
				],
				[
					-225.8646634647323,
					-13.069824363292128
				],
				[
					-225.5297875461987,
					-16.652892700746406
				],
				[
					-221.70365960658518,
					-22.681014325078195
				],
				[
					-219.92249915979096,
					-24.82373322212584
				],
				[
					-213.174202815256,
					-31.04152402155364
				],
				[
					-211.03445146213528,
					-32.47005401349861
				],
				[
					-205.84208658942077,
					-35.43962703038255
				],
				[
					-199.90879955263716,
					-38.40925077451311
				],
				[
					-190.53765092183673,
					-42.16717593105159
				],
				[
					-179.28162998853622,
					-46.05257865833573
				],
				[
					-167.0860897206661,
					-49.597094288362086
				],
				[
					-158.33140395436314,
					-50.794460217479354
				],
				[
					-149.57671818806017,
					-51.59463180559578
				],
				[
					-140.35077630069722,
					-51.59463180559578
				],
				[
					-126.27629881818106,
					-52.80675936347825
				],
				[
					-117.52158768825478,
					-53.20689588478285
				],
				[
					-108.7668765583285,
					-53.20689588478285
				],
				[
					-99.54096003458886,
					-53.20689588478285
				],
				[
					-86.40894406694605,
					-53.20689588478285
				],
				[
					-77.18302754320644,
					-53.20689588478285
				],
				[
					-66.54339338353344,
					-53.20689588478285
				],
				[
					-56.846271465980465,
					-53.20689588478285
				],
				[
					-47.14914954842743,
					-53.20689588478285
				],
				[
					-33.545877459724636,
					-53.20689588478285
				],
				[
					-19.942605371021898,
					-50.80927257349117
				],
				[
					-15.565249806058716,
					-49.61489955192428
				],
				[
					-7.278801889642125,
					-47.249893860206384
				],
				[
					4.448475164718388,
					-42.56431954480604
				],
				[
					12.266659867625378,
					-39.44058642545724
				],
				[
					19.61358844947233,
					-36.35246383323238
				],
				[
					25.17638904059811,
					-33.38877517695596
				],
				[
					25.748389473436873,
					-32.44337148177874
				],
				[
					26.05660822387398,
					-29.669352000598565
				],
				[
					26.05660822387398,
					-27.034680265871657
				],
				[
					25.783949273314477,
					-24.87116319771144
				],
				[
					24.752613622370404,
					-22.707696856798066
				],
				[
					19.972179355798858,
					-15.031751353401432
				],
				[
					15.668936298141261,
					-7.995983702295234
				],
				[
					10.53290403279351,
					-0.8950315392876291
				],
				[
					5.450186103638885,
					5.361261240321255
				],
				[
					0.09780213147507766,
					10.32542959413513
				],
				[
					-5.100523192716764,
					14.030040414480482
				],
				[
					-5.100523192716764,
					14.030040414480482
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "text",
			"version": 300,
			"versionNonce": 1416176953,
			"isDeleted": false,
			"id": "fO9vQ0Fk",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1032.166277436887,
			"y": -1788.2862057070342,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 437.5838623046875,
			"height": 100,
			"seed": 159502510,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914311,
			"link": null,
			"locked": false,
			"fontSize": 16,
			"fontFamily": 1,
			"text": "DSB-SC의 단점\n- 0을 사이로 왔다갔다하면 어딜 선택해야할지 모름\n\n그래서 conventional AM (DSB-LC)는 신호를 모두 양으로 옮김\n- 편리한 demodulation",
			"rawText": "DSB-SC의 단점\n- 0을 사이로 왔다갔다하면 어딜 선택해야할지 모름\n\n그래서 conventional AM (DSB-LC)는 신호를 모두 양으로 옮김\n- 편리한 demodulation",
			"textAlign": "right",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "DSB-SC의 단점\n- 0을 사이로 왔다갔다하면 어딜 선택해야할지 모름\n\n그래서 conventional AM (DSB-LC)는 신호를 모두 양으로 옮김\n- 편리한 demodulation",
			"lineHeight": 1.25,
			"baseline": 94
		},
		{
			"type": "freedraw",
			"version": 78,
			"versionNonce": 1578215127,
			"isDeleted": false,
			"id": "WdNIz_u0wFS2rjuEOYiyQ",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -585.0870658473888,
			"y": -1777.7714620285287,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 459.2688922303348,
			"height": 87.1616856794767,
			"seed": 12841458,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914311,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.2654926213222097,
					1.2417776335294093
				],
				[
					3.428958962235697,
					2.578389854606712
				],
				[
					6.063681424209335,
					3.7905427761124884
				],
				[
					11.054506946119545,
					5.574670766833833
				],
				[
					24.660746578749354,
					9.166641736069096
				],
				[
					36.71399691986244,
					11.656132090981828
				],
				[
					50.18093953328548,
					13.339515769924219
				],
				[
					63.647882146708525,
					15.02287408524353
				],
				[
					82.4346418399681,
					15.43779759893664
				],
				[
					94.95909757489449,
					15.43779759893664
				],
				[
					107.4836040370675,
					15.43779759893664
				],
				[
					120.0081104992405,
					15.019906541316459
				],
				[
					131.11889932548024,
					12.960152056108655
				],
				[
					145.66463292905632,
					8.920665317229577
				],
				[
					154.41934405898263,
					5.7317476859793715
				],
				[
					163.64526058272224,
					2.5191404305596734
				],
				[
					173.34238250027528,
					-0.7172071762763608
				],
				[
					189.30178301253812,
					-5.6339455545044075
				],
				[
					199.94136644496444,
					-8.093785833770198
				],
				[
					210.58100060463738,
					-10.553651476659297
				],
				[
					220.74932791600378,
					-12.592658518001372
				],
				[
					230.91770595461674,
					-14.222677133504021
				],
				[
					246.40590107306622,
					-17.079661026524263
				],
				[
					256.5742791116792,
					-19.115700523939267
				],
				[
					266.7426064230456,
					-21.56072844719324
				],
				[
					276.43977906784517,
					-23.990944014435627
				],
				[
					286.1369009853982,
					-25.60911781785353
				],
				[
					294.89161211532445,
					-27.203576633478633
				],
				[
					303.64632324525076,
					-28.798035449103736
				],
				[
					321.3068619727715,
					-32.635982837178744
				],
				[
					327.2401236459318,
					-33.7533011711364
				],
				[
					334.2551438531722,
					-34.80835180987333
				],
				[
					338.30353322383246,
					-34.80835180987333
				],
				[
					347.34272275277965,
					-34.80835180987333
				],
				[
					356.7138713835801,
					-34.80835180987333
				],
				[
					363.58959457161376,
					-34.80835180987333
				],
				[
					370.93657388070733,
					-34.42011082789986
				],
				[
					378.7547078563677,
					-32.86123717577584
				],
				[
					386.1016871654614,
					-31.32011805996717
				],
				[
					397.3577080987618,
					-28.217157748107184
				],
				[
					405.6441560151785,
					-25.063799916734524
				],
				[
					414.0017235313503,
					-21.483673759584008
				],
				[
					421.3486521131973,
					-18.395525803735836
				],
				[
					430.5182613931935,
					-12.681558017695352
				],
				[
					434.8837975096952,
					-8.67466353476675
				],
				[
					439.40039936661844,
					-3.775730420100899
				],
				[
					446.439159925275,
					6.608999325328114
				],
				[
					448.3477725791912,
					9.664555025225582
				],
				[
					448.5492612027489,
					10.609958720402801
				],
				[
					449.7080744244382,
					13.244681182376326
				],
				[
					450.55567598814014,
					15.879378280726542
				],
				[
					452.15606989161927,
					21.00950082184363
				],
				[
					452.7340054123122,
					23.64419792019362
				],
				[
					453.35044291318627,
					26.750125775980678
				],
				[
					454.2395393646199,
					29.384848237954202
				],
				[
					454.8559768654941,
					32.49077609374103
				],
				[
					455.5257794298079,
					36.53916546440132
				],
				[
					456.1688994624019,
					41.66928800551841
				],
				[
					456.7468349830948,
					44.30398510386863
				],
				[
					457.2180403769081,
					45.99624605096869
				],
				[
					457.6211190785166,
					47.21727624063237
				],
				[
					458.4301679347906,
					49.38076794516928
				],
				[
					459.1029126794082,
					51.683531305289534
				],
				[
					459.2688922303348,
					52.353333869603375
				],
				[
					459.2688922303348,
					52.353333869603375
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"type": "freedraw",
			"version": 29,
			"versionNonce": 39982617,
			"isDeleted": false,
			"id": "kjYqXLKRQKYkaLYJYzzTt",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -135.37305633509652,
			"y": -1733.5237841684036,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"width": 27.14430184580806,
			"height": 13.914458383066858,
			"seed": 237670194,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1710827914311,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.6105024130200718,
					0.40602088191212715
				],
				[
					2.7740194811802894,
					1.7426331029896573
				],
				[
					4.46628042828047,
					2.688062161789958
				],
				[
					8.17677560923346,
					5.047132765653714
				],
				[
					14.364941696637743,
					8.49389699145172
				],
				[
					17.942074946237994,
					10.435101901318376
				],
				[
					18.887478641414987,
					10.77000318347541
				],
				[
					19.628400805484148,
					9.818664400444277
				],
				[
					20.653852095820753,
					7.649237608053454
				],
				[
					22.51503477415133,
					4.537374664412482
				],
				[
					24.18654827738567,
					1.594458815625103
				],
				[
					24.89191064157717,
					0.17188927515735486
				],
				[
					26.237400130812375,
					-2.1931164165605423
				],
				[
					26.978322294881423,
					-2.9755334683611636
				],
				[
					27.14430184580806,
					-3.144455199591448
				],
				[
					27.14430184580806,
					-3.144455199591448
				]
			],
			"lastCommittedPoint": null,
			"simulatePressure": true,
			"pressures": []
		},
		{
			"id": "z_xR1APBmovkpMLPTkm19",
			"type": "freedraw",
			"x": -318.3624811241972,
			"y": -1699.3459931474915,
			"width": 88.22969973797547,
			"height": 27.625488954110097,
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
			"seed": 986505273,
			"version": 121,
			"versionNonce": 1560589303,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710827914311,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.0874976634480618,
					0.3572538628145594
				],
				[
					-2.3483169530161945,
					0.7433721832085212
				],
				[
					-3.8534500470814805,
					1.221434141842792
				],
				[
					-6.611534393212651,
					2.595238449942599
				],
				[
					-8.660371358787643,
					3.191500811966989
				],
				[
					-11.000820274301645,
					3.7036875732535464
				],
				[
					-14.17654005105004,
					4.273693170127899
				],
				[
					-17.352259827798434,
					4.546871432204625
				],
				[
					-22.32472464855107,
					4.843698767002252
				],
				[
					-25.082764034467914,
					5.390100251369859
				],
				[
					-27.423212949981917,
					5.390100251369859
				],
				[
					-30.181297296113087,
					5.6632785134463575
				],
				[
					-32.521701251412765,
					5.6632785134463575
				],
				[
					-36.65885025071668,
					5.6632785134463575
				],
				[
					-39.41693459684785,
					5.6632785134463575
				],
				[
					-42.59265437359625,
					5.936456775523084
				],
				[
					-47.56507423413461,
					5.936456775523084
				],
				[
					-49.48784275881707,
					5.936456775523084
				],
				[
					-52.24592710494824,
					5.936456775523084
				],
				[
					-55.004011451079464,
					5.936456775523084
				],
				[
					-57.762095797210634,
					5.936456775523084
				],
				[
					-62.316880227131776,
					5.936456775523084
				],
				[
					-65.49260000388017,
					5.936456775523084
				],
				[
					-68.25068435001134,
					5.936456775523084
				],
				[
					-71.42640412675973,
					5.936456775523084
				],
				[
					-75.56355312606365,
					5.936456775523084
				],
				[
					-78.32163747219482,
					5.936456775523084
				],
				[
					-79.82677056626011,
					5.936456775523084
				],
				[
					-80.42564062071386,
					5.786694301695434
				],
				[
					-80.7250756479408,
					5.4872592744684425
				],
				[
					-81.8125733113888,
					5.306024650631798
				],
				[
					-81.9622908250023,
					5.306024650631798
				],
				[
					-82.11200833861574,
					5.15630713701853
				],
				[
					-82.41148832605694,
					4.856827149577157
				],
				[
					-82.71092335328382,
					4.557392122350393
				],
				[
					-82.8921579771204,
					3.564490749786046
				],
				[
					-82.8921579771204,
					2.05935765572076
				],
				[
					-83.16798889184065,
					0.13658913103813575
				],
				[
					-83.16798889184065,
					-1.368543963026923
				],
				[
					-83.16798889184065,
					-3.1731120843192
				],
				[
					-83.16798889184065,
					-5.095880609001597
				],
				[
					-83.16798889184065,
					-5.789346954338953
				],
				[
					-83.16798889184065,
					-7.712115479021577
				],
				[
					-82.92893543241644,
					-9.516683600313854
				],
				[
					-82.45348116621153,
					-10.359867459264706
				],
				[
					-82.09361961096772,
					-11.053333804602062
				],
				[
					-81.79944492881373,
					-11.652226339163008
				],
				[
					-80.78024183088485,
					-12.97612480939165
				],
				[
					-80.03952230031979,
					-13.72473485756609
				],
				[
					-79.38283341027835,
					-14.56791871651717
				],
				[
					-78.30059609190323,
					-15.292902172077675
				],
				[
					-77.0397768023351,
					-16.19651255904546
				],
				[
					-75.95753948395992,
					-16.740238910662356
				],
				[
					-74.33425094671867,
					-17.102730638442836
				],
				[
					-72.50864144513486,
					-18.066745073320362
				],
				[
					-70.1734528746938,
					-18.6183619425467
				],
				[
					-67.00299344301834,
					-19.4694138389998
				],
				[
					-63.70902830266533,
					-20.01053249818733
				],
				[
					-60.53856887098982,
					-20.585798440134567
				],
				[
					-57.785744869931534,
					-21.137415309360676
				],
				[
					-55.03292086887325,
					-21.41322374397373
				],
				[
					-50.90368486728585,
					-21.689032178587013
				],
				[
					-47.315545044778844,
					-21.689032178587013
				],
				[
					-43.7274052222719,
					-21.689032178587013
				],
				[
					-41.80989704266233,
					-21.689032178587013
				],
				[
					-38.221757220155325,
					-21.689032178587013
				],
				[
					-33.674840827736375,
					-21.689032178587013
				],
				[
					-30.92201682667809,
					-21.689032178587013
				],
				[
					-28.16919282561986,
					-21.689032178587013
				],
				[
					-25.416368824561573,
					-21.689032178587013
				],
				[
					-21.287132822974115,
					-21.689032178587013
				],
				[
					-18.11667339129866,
					-21.689032178587013
				],
				[
					-14.946168999408883,
					-21.689032178587013
				],
				[
					-12.193344998350597,
					-21.689032178587013
				],
				[
					-9.44052099729231,
					-21.689032178587013
				],
				[
					-6.808550052267947,
					-21.029713116009134
				],
				[
					-5.970581578175654,
					-20.851086184601854
				],
				[
					-5.13265806429763,
					-20.525371912117635
				],
				[
					-3.609136242584327,
					-19.976385215427626
				],
				[
					-2.474385393908733,
					-19.50095342933014
				],
				[
					-1.7861793936441472,
					-19.17523915684569
				],
				[
					-0.9482558797661227,
					-19.02812933566156
				],
				[
					-0.35460121017098345,
					-18.73393217340049
				],
				[
					0.08929098559644899,
					-18.43973501113942
				],
				[
					0.9246068070451656,
					-17.63595878002093
				],
				[
					1.6128128073097514,
					-17.31024450753671
				],
				[
					2.0908747659439086,
					-16.35149041773184
				],
				[
					2.2695016973511883,
					-15.810371758544306
				],
				[
					2.7738204211355537,
					-14.431329585478807
				],
				[
					3.251882379769711,
					-12.931456836486404
				],
				[
					3.6958195357514683,
					-12.337824646998342
				],
				[
					3.874446467158748,
					-11.499878653013184
				],
				[
					4.021556288342879,
					-11.055963977138617
				],
				[
					4.620426342796691,
					-9.25928637345578
				],
				[
					4.767536163980822,
					-8.815349217474022
				],
				[
					4.914645985164952,
					-7.559790272978944
				],
				[
					5.061710846134815,
					-7.265570630610455
				],
				[
					5.061710846134815,
					-6.430254809161852
				],
				[
					5.061710846134815,
					-5.889158630081283
				],
				[
					5.061710846134815,
					-4.806921311706219
				],
				[
					5.061710846134815,
					-4.213311602325348
				],
				[
					5.061710846134815,
					-3.919091959957086
				],
				[
					5.061710846134815,
					-3.230885959692614
				],
				[
					4.9119933325213765,
					-2.9367112775385067
				],
				[
					4.462840791681003,
					-2.4927741215567494
				],
				[
					4.163360804239801,
					-2.048881925789374
				],
				[
					4.013643290626362,
					-1.901772104605243
				],
				[
					4.013643290626362,
					-1.901772104605243
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				4.013643290626362,
				-1.901772104605243
			]
		},
		{
			"id": "5JKmZB643nsPzM7q1dzvr",
			"type": "freedraw",
			"x": -536.4373696761844,
			"y": -1583.4015134698095,
			"width": 5.64751995833501,
			"height": 35.47154091152629,
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
			"seed": 941386873,
			"version": 62,
			"versionNonce": 1774840569,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710827914311,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.2994575073340684,
					-0.1497175136134956
				],
				[
					-0.5989150146680231,
					0.4438921957673756
				],
				[
					-0.7486325282815187,
					0.5910020169515064
				],
				[
					-1.710016790622717,
					2.022580200424727
				],
				[
					-2.0094742979567854,
					2.4665173564064844
				],
				[
					-2.6398839427408802,
					3.7220763009015627
				],
				[
					-3.1205760739114794,
					4.557392122350393
				],
				[
					-3.4830678016918455,
					5.245598122614865
				],
				[
					-3.6328077954123046,
					5.6895352785966224
				],
				[
					-3.6328077954123046,
					6.133427474364225
				],
				[
					-3.9952770430855935,
					7.21566479273929
				],
				[
					-4.38667818865963,
					8.618333558418499
				],
				[
					-4.536395702273126,
					9.062270714400483
				],
				[
					-4.686113215886621,
					10.168112145282066
				],
				[
					-4.686113215886621,
					10.76176681487732
				],
				[
					-5.017087833443725,
					11.896517663552913
				],
				[
					-5.017087833443725,
					12.978710021713823
				],
				[
					-5.198344937387446,
					13.816678495805945
				],
				[
					-5.198344937387446,
					15.072237440301251
				],
				[
					-5.198344937387446,
					15.665892109896504
				],
				[
					-5.497779964614324,
					16.800642958572098
				],
				[
					-5.497779964614324,
					17.244580114553855
				],
				[
					-5.497779964614324,
					17.68847231032123
				],
				[
					-5.497779964614324,
					18.132409466302988
				],
				[
					-5.64751995833501,
					19.117442801365087
				],
				[
					-5.64751995833501,
					19.711052510745958
				],
				[
					-5.64751995833501,
					20.966656415455645
				],
				[
					-5.64751995833501,
					21.654862415720117
				],
				[
					-5.64751995833501,
					22.73709973409518
				],
				[
					-5.64751995833501,
					24.533754857671056
				],
				[
					-5.64751995833501,
					25.61599217604612
				],
				[
					-5.64751995833501,
					26.453915689924088
				],
				[
					-5.64751995833501,
					27.04757035951934
				],
				[
					-5.50041013715088,
					27.938052363911993
				],
				[
					-5.50041013715088,
					28.626258364176692
				],
				[
					-5.353322796073826,
					29.46418187805466
				],
				[
					-5.174695864666546,
					30.152387878319132
				],
				[
					-5.0276085235894925,
					30.893107408884134
				],
				[
					-4.880498702405362,
					31.33704456486589
				],
				[
					-4.880498702405362,
					31.930699234461144
				],
				[
					-4.733411361328422,
					32.224873916615024
				],
				[
					-4.554784429921142,
					33.307111234990316
				],
				[
					-4.407697088844202,
					33.601285917144196
				],
				[
					-4.1108697540465755,
					33.89811325194182
				],
				[
					-3.6038983776185205,
					34.733429073390425
				],
				[
					-3.4568110365415805,
					34.880538894574556
				],
				[
					-3.3097012153574497,
					35.02760375554453
				],
				[
					-2.865786539482883,
					35.321823397912794
				],
				[
					-2.865786539482883,
					35.321823397912794
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				-2.865786539482883,
				35.321823397912794
			]
		},
		{
			"id": "Anl__l1YOOhTEr1sxH2cO",
			"type": "freedraw",
			"x": -444.96361063572687,
			"y": -1510.1889299494053,
			"width": 174.85706239857262,
			"height": 3.3727354358036337,
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
			"seed": 569916697,
			"version": 98,
			"versionNonce": 1616452887,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710827914311,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5936097093808712,
					0
				],
				[
					1.4315332232588958,
					0
				],
				[
					2.6871371279684126,
					0
				],
				[
					4.360376463295154,
					0
				],
				[
					6.401345391367897,
					0
				],
				[
					7.656949296077471,
					0
				],
				[
					8.100841491844903,
					0
				],
				[
					8.694496161440043,
					0
				],
				[
					9.1384333174218,
					0
				],
				[
					10.761766814877376,
					0
				],
				[
					12.679274994486946,
					0
				],
				[
					14.179147743479291,
					0
				],
				[
					16.931971744537577,
					0
				],
				[
					19.26716031497864,
					0
				],
				[
					21.33177831577234,
					0
				],
				[
					21.625952997926333,
					0
				],
				[
					22.463876511804358,
					0
				],
				[
					25.09589241704299,
					0
				],
				[
					26.178084775203843,
					0
				],
				[
					28.095637915027737,
					0
				],
				[
					29.76887725035448,
					0
				],
				[
					31.686385429964048,
					0
				],
				[
					34.98030561010273,
					0
				],
				[
					36.89785874992657,
					0
				],
				[
					38.39773149891897,
					0
				],
				[
					40.31523967852854,
					0
				],
				[
					42.773888997432834,
					0
				],
				[
					44.691397177042404,
					0
				],
				[
					46.60890535665192,
					0
				],
				[
					48.52645849647581,
					0
				],
				[
					50.02633124546816,
					0
				],
				[
					53.3202514256069,
					0
				],
				[
					55.65543999604796,
					0
				],
				[
					57.9905836062747,
					0.27317826207649887
				],
				[
					60.325772176715816,
					0.27317826207649887
				],
				[
					63.078596177774045,
					0.27317826207649887
				],
				[
					66.79019674874434,
					0.5463565241532251
				],
				[
					68.70770492835385,
					0.7854099835774377
				],
				[
					70.62525806817774,
					1.024418482787496
				],
				[
					73.37808206923597,
					1.024418482787496
				],
				[
					75.2955902488456,
					1.2634719422117087
				],
				[
					79.424826250433,
					1.5602992770093351
				],
				[
					82.17765025149123,
					2.109263493591925
				],
				[
					85.34815464338106,
					2.4060908283895515
				],
				[
					88.1009786444393,
					2.9524473525427766
				],
				[
					90.43612225466603,
					2.9524473525427766
				],
				[
					92.89477157357038,
					2.9524473525427766
				],
				[
					93.97700889194556,
					2.9524473525427766
				],
				[
					95.89451707155507,
					2.9524473525427766
				],
				[
					97.8120252511647,
					2.9524473525427766
				],
				[
					101.9412612527521,
					3.2256705748338845
				],
				[
					103.19686515746156,
					3.3727354358036337
				],
				[
					105.53205372790268,
					3.3727354358036337
				],
				[
					106.61424608606347,
					3.3727354358036337
				],
				[
					109.07289540496782,
					3.3727354358036337
				],
				[
					110.57276815396023,
					3.3727354358036337
				],
				[
					112.49027633356974,
					3.3727354358036337
				],
				[
					113.99014908256214,
					3.3727354358036337
				],
				[
					116.32533765300315,
					3.3727354358036337
				],
				[
					119.20162240252472,
					3.3727354358036337
				],
				[
					121.11913058213423,
					3.3727354358036337
				],
				[
					123.45431915257535,
					3.3727354358036337
				],
				[
					127.16587476333126,
					3.3727354358036337
				],
				[
					129.50106333377227,
					3.3727354358036337
				],
				[
					132.2538873348306,
					3.3727354358036337
				],
				[
					134.5890759052716,
					3.3727354358036337
				],
				[
					137.34189990632996,
					3.3727354358036337
				],
				[
					141.88877133853458,
					3.3727354358036337
				],
				[
					144.64164029980708,
					3.3727354358036337
				],
				[
					147.39446430086542,
					3.3727354358036337
				],
				[
					149.31197248047494,
					3.3727354358036337
				],
				[
					151.64716105091605,
					3.3727354358036337
				],
				[
					155.77639705250346,
					3.3727354358036337
				],
				[
					158.52922105356168,
					3.3727354358036337
				],
				[
					160.4467292331713,
					3.3727354358036337
				],
				[
					162.3642823729952,
					3.3727354358036337
				],
				[
					164.16093749657085,
					3.3727354358036337
				],
				[
					165.24317481494592,
					3.3727354358036337
				],
				[
					167.16068299455554,
					3.3727354358036337
				],
				[
					169.49587156499666,
					3.3727354358036337
				],
				[
					172.37215631451812,
					3.3727354358036337
				],
				[
					173.6277152590133,
					3.3727354358036337
				],
				[
					174.31596621949217,
					3.3727354358036337
				],
				[
					174.85706239857262,
					3.3727354358036337
				],
				[
					174.85706239857262,
					3.3727354358036337
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				174.85706239857262,
				3.3727354358036337
			]
		},
		{
			"id": "Dl2_GNsb2E2-gg4tMcjhg",
			"type": "freedraw",
			"x": -409.88610104231117,
			"y": -1583.4435512701782,
			"width": 90.26019293611671,
			"height": 23.553981867681614,
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
			"seed": 1958955321,
			"version": 167,
			"versionNonce": 1126441945,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710827914311,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.29943502722687754,
					0
				],
				[
					-1.142618886177786,
					0
				],
				[
					-2.9471870074699495,
					0
				],
				[
					-4.452320101535179,
					0
				],
				[
					-5.957453195600465,
					0
				],
				[
					-7.2182724851685975,
					0
				],
				[
					-11.355421484472515,
					0
				],
				[
					-12.860554578537801,
					0
				],
				[
					-15.618593964454647,
					0
				],
				[
					-18.376678310585874,
					0
				],
				[
					-20.71712722609982,
					0
				],
				[
					-24.01896040395502,
					0
				],
				[
					-25.52404853780604,
					0
				],
				[
					-27.44686202270276,
					0
				],
				[
					-28.707681312270893,
					-0.2416611518535774
				],
				[
					-29.795134015504686,
					-0.2416611518535774
				],
				[
					-31.182066706179626,
					-0.2416611518535774
				],
				[
					-32.687199800244855,
					-0.2416611518535774
				],
				[
					-33.53038365919582,
					-0.2416611518535774
				],
				[
					-34.61783636242956,
					-0.2416611518535774
				],
				[
					-36.666718288218874,
					-0.2416611518535774
				],
				[
					-39.00712224351855,
					-0.2416611518535774
				],
				[
					-40.51225533758378,
					-0.2416611518535774
				],
				[
					-42.01738843164907,
					-0.2416611518535774
				],
				[
					-44.35783734716301,
					-0.2416611518535774
				],
				[
					-47.659625564803946,
					-0.2416611518535774
				],
				[
					-49.16475865886923,
					-0.4833223037069274
				],
				[
					-50.25221136210297,
					-0.4833223037069274
				],
				[
					-51.930711042502594,
					-0.4833223037069274
				],
				[
					-54.2711599580166,
					-0.4833223037069274
				],
				[
					-57.155312745040305,
					-0.4833223037069274
				],
				[
					-59.07808126972276,
					-0.4833223037069274
				],
				[
					-60.756580950122384,
					-0.4833223037069274
				],
				[
					-61.86768272607708,
					-0.4833223037069274
				],
				[
					-64.33420008248356,
					-0.6645569275435719
				],
				[
					-66.25696860716602,
					-0.6645569275435719
				],
				[
					-68.17973713184853,
					-0.6645569275435719
				],
				[
					-70.52018604736247,
					-0.6645569275435719
				],
				[
					-72.86063496287647,
					-0.6645569275435719
				],
				[
					-76.5801035713489,
					-0.6645569275435719
				],
				[
					-78.08519170519986,
					-0.6645569275435719
				],
				[
					-80.4256406207138,
					-0.6645569275435719
				],
				[
					-81.9307737147791,
					-0.6645569275435719
				],
				[
					-83.73534183607126,
					-0.6645569275435719
				],
				[
					-83.8850593496847,
					-0.6645569275435719
				],
				[
					-84.18449437691157,
					-0.6645569275435719
				],
				[
					-84.33421189052501,
					-0.6645569275435719
				],
				[
					-84.48397436435278,
					-0.6645569275435719
				],
				[
					-84.78340939157965,
					-0.3703822453896919
				],
				[
					-85.05919534608563,
					1.3028570899371061
				],
				[
					-85.8156959118694,
					4.596822230290172
				],
				[
					-85.99697549592025,
					6.096694979282574
				],
				[
					-86.27276145042623,
					8.431838589509198
				],
				[
					-86.27276145042623,
					10.767027159950203
				],
				[
					-86.54859236514648,
					14.060947340089115
				],
				[
					-86.54859236514648,
					15.143184658464179
				],
				[
					-86.54859236514648,
					16.22537701662509
				],
				[
					-86.54859236514648,
					17.898616351951887
				],
				[
					-86.54859236514648,
					20.233804922392892
				],
				[
					-86.54859236514648,
					22.298422923186536
				],
				[
					-86.54859236514648,
					22.445532744370666
				],
				[
					-86.54859236514648,
					22.742360079168293
				],
				[
					-86.54859236514648,
					22.889424940138042
				],
				[
					-84.63103922532264,
					22.889424940138042
				],
				[
					-81.46057979364713,
					22.889424940138042
				],
				[
					-78.70775579258884,
					22.889424940138042
				],
				[
					-76.37256722214778,
					22.889424940138042
				],
				[
					-73.91391790324349,
					22.889424940138042
				],
				[
					-71.1610939021852,
					22.889424940138042
				],
				[
					-68.40826990112691,
					22.889424940138042
				],
				[
					-66.49076172151734,
					22.889424940138042
				],
				[
					-64.03211240261305,
					22.889424940138042
				],
				[
					-61.696968792386315,
					22.889424940138042
				],
				[
					-59.77941565256242,
					22.889424940138042
				],
				[
					-58.279542903570075,
					22.889424940138042
				],
				[
					-57.14479205489448,
					22.889424940138042
				],
				[
					-56.85061737274049,
					22.889424940138042
				],
				[
					-55.59501346803097,
					22.889424940138042
				],
				[
					-55.0014037586501,
					22.889424940138042
				],
				[
					-53.32816442332336,
					22.889424940138042
				],
				[
					-49.19888346152163,
					22.889424940138042
				],
				[
					-47.28137528191206,
					22.889424940138042
				],
				[
					-45.78150253291972,
					22.889424940138042
				],
				[
					-44.699310174758864,
					22.889424940138042
				],
				[
					-43.86134170066657,
					22.889424940138042
				],
				[
					-42.72659085199092,
					22.889424940138042
				],
				[
					-41.88866733811295,
					22.889424940138042
				],
				[
					-41.05074382423493,
					22.889424940138042
				],
				[
					-40.2128203103569,
					22.889424940138042
				],
				[
					-37.33653556083539,
					22.889424940138042
				],
				[
					-36.254298242460266,
					22.889424940138042
				],
				[
					-33.91915463223347,
					22.889424940138042
				],
				[
					-32.419281883241126,
					22.889424940138042
				],
				[
					-30.378267994954058,
					22.889424940138042
				],
				[
					-29.78465828557313,
					22.889424940138042
				],
				[
					-28.70242096719801,
					22.889424940138042
				],
				[
					-26.367232396756947,
					22.889424940138042
				],
				[
					-24.032088786530153,
					22.889424940138042
				],
				[
					-21.155804037008636,
					22.889424940138042
				],
				[
					-20.31788052313067,
					22.889424940138042
				],
				[
					-18.818007774138266,
					22.889424940138042
				],
				[
					-16.90045463431443,
					22.889424940138042
				],
				[
					-14.024169884792911,
					22.889424940138042
				],
				[
					-12.76861094029772,
					22.889424940138042
				],
				[
					-12.324673784315962,
					22.889424940138042
				],
				[
					-11.636467784051376,
					22.889424940138042
				],
				[
					-11.192530628069676,
					22.889424940138042
				],
				[
					-8.978195113662537,
					22.889424940138042
				],
				[
					-7.060686934052967,
					22.889424940138042
				],
				[
					-6.372480933788381,
					22.889424940138042
				],
				[
					-5.778826264193185,
					22.889424940138042
				],
				[
					-4.376157498513805,
					22.889424940138042
				],
				[
					-3.5382339846358377,
					22.889424940138042
				],
				[
					-2.700310470757813,
					22.889424940138042
				],
				[
					-1.027071135431072,
					22.889424940138042
				],
				[
					-0.1891026613387794,
					22.889424940138042
				],
				[
					0.6488208525392452,
					22.889424940138042
				],
				[
					0.9456481873368716,
					22.889424940138042
				],
				[
					1.4867443664172697,
					22.889424940138042
				],
				[
					2.3772263708100354,
					22.889424940138042
				],
				[
					2.674008745393337,
					22.889424940138042
				],
				[
					2.9682283877615987,
					22.440272399297783
				],
				[
					3.2072368869715433,
					21.32917062334309
				],
				[
					3.2072368869715433,
					20.730255608674952
				],
				[
					3.2072368869715433,
					19.46943631910699
				],
				[
					3.354346708155674,
					18.326772472714765
				],
				[
					3.354346708155674,
					17.483588613763914
				],
				[
					3.354346708155674,
					16.88471855931016
				],
				[
					3.532973639562954,
					16.191252213972575
				],
				[
					3.532973639562954,
					15.49778586863522
				],
				[
					3.532973639562954,
					15.198350841408228
				],
				[
					3.7116005709702335,
					13.961135664346784
				],
				[
					3.7116005709702335,
					13.661700637119793
				],
				[
					3.7116005709702335,
					12.40083638733745
				],
				[
					3.7116005709702335,
					11.801966332883694
				],
				[
					3.7116005709702335,
					10.809064960319347
				],
				[
					3.7116005709702335,
					10.21014994565121
				],
				[
					3.7116005709702335,
					9.099048169696516
				],
				[
					3.7116005709702335,
					8.50013315502838
				],
				[
					3.7116005709702335,
					7.901263100574624
				],
				[
					3.7116005709702335,
					7.058079241623773
				],
				[
					3.7116005709702335,
					6.364612896286189
				],
				[
					3.7116005709702335,
					6.065132908845044
				],
				[
					3.7116005709702335,
					5.615980368004784
				],
				[
					3.7116005709702335,
					5.017065353336648
				],
				[
					3.7116005709702335,
					4.567912812496388
				],
				[
					3.7116005709702335,
					4.268477785269397
				],
				[
					3.7116005709702335,
					3.66956277060126
				],
				[
					3.7116005709702335,
					2.920930242319855
				],
				[
					3.7116005709702335,
					2.0777463833690035
				],
				[
					3.7116005709702335,
					1.7783113561420123
				],
				[
					3.7116005709702335,
					1.478876328915021
				],
				[
					3.7116005709702335,
					1.3291138550873711
				],
				[
					3.7116005709702335,
					1.3291138550873711
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				3.7116005709702335,
				1.3291138550873711
			]
		},
		{
			"id": "UlQVOCd-cUW25jnLmxkig",
			"type": "freedraw",
			"x": -171.7822687843813,
			"y": -1604.0661271656088,
			"width": 33.20995221189162,
			"height": 26.790128172446884,
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
			"seed": 72057433,
			"version": 95,
			"versionNonce": 1787052217,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710827914311,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5122317215009389,
					0.6882060002644721
				],
				[
					-0.6619492351143776,
					0.8353158214488303
				],
				[
					-1.9227685246825104,
					1.221434141842792
				],
				[
					-2.5216835393505903,
					1.5182614766404186
				],
				[
					-3.5434943297087784,
					2.3850944083121703
				],
				[
					-6.845282547349655,
					3.385863818378766
				],
				[
					-8.35041564141494,
					3.8035442092102585
				],
				[
					-11.10849998754611,
					4.339380043217943
				],
				[
					-13.866584333677338,
					4.885736567371168
				],
				[
					-16.333101690083822,
					5.542425457412492
				],
				[
					-17.83823478414905,
					5.960105848244211
				],
				[
					-18.381983615873082,
					6.138687819437109
				],
				[
					-20.8484560120653,
					6.556368210268602
				],
				[
					-22.0856711891268,
					6.734995141675881
				],
				[
					-22.385106216353677,
					6.8820600026456304
				],
				[
					-22.534823729967172,
					6.8820600026456304
				],
				[
					-22.984021231021757,
					6.8820600026456304
				],
				[
					-24.09512300697645,
					6.8820600026456304
				],
				[
					-25.48205569765139,
					6.8820600026456304
				],
				[
					-27.822459652951068,
					6.8820600026456304
				],
				[
					-28.665643511902033,
					6.8820600026456304
				],
				[
					-29.209392343626064,
					6.8820600026456304
				],
				[
					-29.359109857239503,
					6.8820600026456304
				],
				[
					-29.658589844680705,
					6.8820600026456304
				],
				[
					-30.564807924077854,
					6.157076547085126
				],
				[
					-31.407991783028763,
					5.644889785798341
				],
				[
					-31.5577092966422,
					5.345409798357423
				],
				[
					-31.857144323869136,
					5.045974771130432
				],
				[
					-32.21965853175658,
					4.502225939406344
				],
				[
					-32.36937604537002,
					4.0530733985660845
				],
				[
					-32.76075471083698,
					1.830824886442315
				],
				[
					-32.76075471083698,
					1.2319548319885598
				],
				[
					-32.76075471083698,
					0.9325198047615686
				],
				[
					-33.06018973806391,
					0.4833223037069274
				],
				[
					-33.06018973806391,
					0.18388727648016356
				],
				[
					-33.06018973806391,
					-0.8090140960841836
				],
				[
					-33.20995221189162,
					-1.6521979550350352
				],
				[
					-33.20995221189162,
					-2.1013954560896764
				],
				[
					-33.20995221189162,
					-3.18884815932347
				],
				[
					-33.20995221189162,
					-4.993416280615747
				],
				[
					-33.03132528048434,
					-6.0809139440636955
				],
				[
					-32.85269834907706,
					-7.168366647297489
				],
				[
					-32.674071417669836,
					-8.673499741362775
				],
				[
					-32.52696159648565,
					-9.272414756030912
				],
				[
					-31.959608652255042,
					-11.250349463657358
				],
				[
					-31.334436872436697,
					-12.511168753225547
				],
				[
					-30.136651803314862,
					-14.194928778698113
				],
				[
					-29.298728289436838,
					-14.85687801381232
				],
				[
					-28.6420393993954,
					-15.700061872763172
				],
				[
					-27.239325673501696,
					-16.62992902488145
				],
				[
					-25.179968017780936,
					-17.698993000467226
				],
				[
					-22.844779447339874,
					-18.492271021546912
				],
				[
					-20.927271267730305,
					-18.975593325254067
				],
				[
					-19.671712323235056,
					-19.366971990720913
				],
				[
					-18.11928108372797,
					-19.908068169801254
				],
				[
					-17.675388887960537,
					-19.908068169801254
				],
				[
					-16.59315156958536,
					-19.908068169801254
				],
				[
					-15.214086916412612,
					-19.908068169801254
				],
				[
					-14.62047720703174,
					-19.908068169801254
				],
				[
					-13.782553693153716,
					-19.908068169801254
				],
				[
					-13.188899023558577,
					-19.908068169801254
				],
				[
					-13.041789202374389,
					-19.908068169801254
				],
				[
					-12.203865688496421,
					-19.908068169801254
				],
				[
					-11.610211018901225,
					-19.908068169801254
				],
				[
					-10.528018660740372,
					-19.188345059313633
				],
				[
					-10.233799018372054,
					-18.894170377159753
				],
				[
					-8.689280776581484,
					-17.34965213536907
				],
				[
					-8.245343620599726,
					-16.905714979387312
				],
				[
					-7.289219703331412,
					-14.9882067997778
				],
				[
					-5.744701461540785,
					-12.892071688761007
				],
				[
					-4.323643968213446,
					-9.997398211591417
				],
				[
					-3.330742595649042,
					-8.02733154146722
				],
				[
					-2.9445793150406985,
					-6.771727636757532
				],
				[
					-2.7974694938565676,
					-6.178117927376661
				],
				[
					-2.618887522663556,
					-5.095880609001597
				],
				[
					-2.3220601878659863,
					-4.5048785920500904
				],
				[
					-2.1749503666818555,
					-4.060941436068333
				],
				[
					-2.1749503666818555,
					-3.46728676647308
				],
				[
					-2.1749503666818555,
					-2.6293632525951125
				],
				[
					-1.9963234352745758,
					-1.7914397387171448
				],
				[
					-1.9963234352745758,
					-0.9561239172683145
				],
				[
					-1.9963234352745758,
					-0.8090140960841836
				],
				[
					-1.9963234352745758,
					-0.8090140960841836
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				-1.9963234352745758,
				-0.8090140960841836
			]
		},
		{
			"id": "Q1gNY2bl",
			"type": "text",
			"x": 592.6798474784772,
			"y": -1785.8159950580443,
			"width": 394.0478515625,
			"height": 360,
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
			"seed": 938217881,
			"version": 214,
			"versionNonce": 526910295,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710827914311,
			"link": null,
			"locked": false,
			"text": "- message가 1보다 작게 되도록\n\n- modulation index : 안전하게 1보다 작게 하려고\n\n\n\n\n\n\n\n\n\n\n\n\n\n- delta signal이 추가됨 > message의 noise를 추적가능\n",
			"rawText": "- message가 1보다 작게 되도록\n\n- modulation index : 안전하게 1보다 작게 하려고\n\n\n\n\n\n\n\n\n\n\n\n\n\n- delta signal이 추가됨 > message의 noise를 추적가능\n",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 354,
			"containerId": null,
			"originalText": "- message가 1보다 작게 되도록\n\n- modulation index : 안전하게 1보다 작게 하려고\n\n\n\n\n\n\n\n\n\n\n\n\n\n- delta signal이 추가됨 > message의 noise를 추적가능\n",
			"lineHeight": 1.25
		},
		{
			"id": "dHvF0lamdVHxbFPXMaRcW",
			"type": "freedraw",
			"x": 136.70248525712168,
			"y": -1656.8163729943415,
			"width": 9.214618400550307,
			"height": 0.32571427248444706,
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
			"seed": 195439831,
			"version": 27,
			"versionNonce": 1838006681,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710827914311,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.14709858113056384,
					0
				],
				[
					0.7407420106721645,
					0
				],
				[
					1.578676764603756,
					0.1786269314072797
				],
				[
					2.4166115185353476,
					0.1786269314072797
				],
				[
					4.116107619012297,
					0.32571427248444706
				],
				[
					4.412934953809895,
					0.32571427248444706
				],
				[
					4.856849629684461,
					0.32571427248444706
				],
				[
					6.112442294340411,
					0.32571427248444706
				],
				[
					6.259540875470975,
					0.32571427248444706
				],
				[
					6.853184305012576,
					0.32571427248444706
				],
				[
					7.935399143280591,
					0.32571427248444706
				],
				[
					8.920432478342747,
					0.32571427248444706
				],
				[
					9.067519819419743,
					0.32571427248444706
				],
				[
					9.214618400550307,
					0.32571427248444706
				],
				[
					9.214618400550307,
					0.32571427248444706
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				9.214618400550307,
				0.32571427248444706
			]
		},
		{
			"id": "l4NZLZ6tC4OgV2u8kQmt4",
			"type": "freedraw",
			"x": 140.6846339176321,
			"y": -1656.0730008111327,
			"width": 4.032054498381598,
			"height": 14.87261408881659,
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
			"seed": 1684679671,
			"version": 32,
			"versionNonce": 1281065079,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710827914311,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.1497287536670342,
					0.14710982118413085
				],
				[
					-0.8116667487278164,
					1.1295129837099012
				],
				[
					-1.1426301262314098,
					1.9674364975878689
				],
				[
					-1.6863677179018453,
					3.049651335855742
				],
				[
					-1.9858139851823182,
					3.643306005450995
				],
				[
					-2.7081672682064664,
					5.439983609133833
				],
				[
					-3.188870639430661,
					7.357514268850537
				],
				[
					-3.3701165033208156,
					8.195437782728504
				],
				[
					-3.5198340169342544,
					9.033361296606472
				],
				[
					-3.6695627706012885,
					9.923843300999351
				],
				[
					-3.850808634491443,
					10.76176681487732
				],
				[
					-3.850808634491443,
					10.90887663606145
				],
				[
					-3.850808634491443,
					11.05598645724558
				],
				[
					-3.850808634491443,
					11.352813792043207
				],
				[
					-3.850808634491443,
					11.499878653012956
				],
				[
					-4.032054498381598,
					12.188084653277656
				],
				[
					-4.032054498381598,
					12.781739322872909
				],
				[
					-4.032054498381598,
					14.281612071865084
				],
				[
					-4.032054498381598,
					14.87261408881659
				],
				[
					-4.032054498381598,
					14.87261408881659
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				-4.032054498381598,
				14.87261408881659
			]
		},
		{
			"id": "iQyooEpLMjvZs1l-S7Xtd",
			"type": "freedraw",
			"x": 133.6580942663387,
			"y": -1643.848138702559,
			"width": 10.693472249358194,
			"height": 4.5521767374916635,
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
			"seed": 1495054519,
			"version": 34,
			"versionNonce": 1500784249,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710827914311,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.14709858113056384,
					0.29682733479762646
				],
				[
					0.44129574339171995,
					0.890482004392652
				],
				[
					0.7381118381357226,
					1.1873093391902785
				],
				[
					0.8852104192662864,
					1.334374200160255
				],
				[
					1.210924691750563,
					2.172342674252377
				],
				[
					1.7520433509381235,
					2.532204229496301
				],
				[
					2.046229273145684,
					2.8263789116504086
				],
				[
					2.3719547856835277,
					3.5145849119148806
				],
				[
					2.6687708804275587,
					3.958522067896638
				],
				[
					2.9655982152251283,
					4.255349402694264
				],
				[
					3.1126967963557206,
					4.5521767374916635
				],
				[
					3.409512891099723,
					4.402414263664014
				],
				[
					5.080122053889994,
					3.701079880824409
				],
				[
					6.18598596487891,
					3.2204102297610007
				],
				[
					7.446816494500638,
					2.4980344666296332
				],
				[
					8.284751248432201,
					1.8360852315151988
				],
				[
					9.51406466783078,
					1.4736159838421372
				],
				[
					9.808261830091908,
					1.024418482787496
				],
				[
					10.252176505966503,
					0.7249834555605048
				],
				[
					10.54637366822763,
					0.42554842833374096
				],
				[
					10.693472249358194,
					0.42554842833374096
				],
				[
					10.693472249358194,
					0.42554842833374096
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				10.693472249358194,
				0.42554842833374096
			]
		},
		{
			"id": "b8ltQ6T63MnCi6sJ0N7uu",
			"type": "freedraw",
			"x": 469.08273895411656,
			"y": -1426.4272863879696,
			"width": 9.188384115507233,
			"height": 32.23800229919016,
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
			"seed": 179806745,
			"version": 165,
			"versionNonce": 1143101847,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710827914311,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.2994350272269344,
					0
				],
				[
					-2.3482719928019264,
					0
				],
				[
					-3.4357696562499314,
					0
				],
				[
					-3.585487169863427,
					0
				],
				[
					-4.129236001587458,
					0
				],
				[
					-4.278953515200897,
					0
				],
				[
					-4.578388542427774,
					0
				],
				[
					-4.877823569654652,
					0.14706486096974913
				],
				[
					-5.390055291155534,
					0.8352708612342212
				],
				[
					-5.539772804769029,
					1.129490503602483
				],
				[
					-5.689490318382468,
					1.4263178384003368
				],
				[
					-5.689490318382468,
					2.114523838664809
				],
				[
					-5.689490318382468,
					2.408698520818689
				],
				[
					-5.689490318382468,
					2.852635676800446
				],
				[
					-5.839207831995907,
					3.690559190678414
				],
				[
					-5.988970305823614,
					3.9873865254760403
				],
				[
					-5.988970305823614,
					4.578388542427547
				],
				[
					-5.988970305823614,
					5.0223256984095315
				],
				[
					-5.988970305823614,
					5.466262854391061
				],
				[
					-5.988970305823614,
					5.760437536544941
				],
				[
					-5.988970305823614,
					6.501157067110171
				],
				[
					-5.988970305823614,
					6.945094223091928
				],
				[
					-5.988970305823614,
					7.23931386546019
				],
				[
					-5.988970305823614,
					7.832923574841061
				],
				[
					-5.988970305823614,
					8.276860730822591
				],
				[
					-5.988970305823614,
					8.571035412976698
				],
				[
					-5.988970305823614,
					9.164690082571951
				],
				[
					-5.988970305823614,
					9.758344752166977
				],
				[
					-5.988970305823614,
					10.743378087229303
				],
				[
					-5.988970305823614,
					11.187270282996678
				],
				[
					-5.988970305823614,
					11.875476283261378
				],
				[
					-5.988970305823614,
					12.319413439242908
				],
				[
					-5.988970305823614,
					13.157336953121103
				],
				[
					-5.988970305823614,
					14.047818957513755
				],
				[
					-5.988970305823614,
					14.736024957778227
				],
				[
					-5.988970305823614,
					15.030199639932334
				],
				[
					-5.988970305823614,
					15.324419282300596
				],
				[
					-5.988970305823614,
					15.915421299252102
				],
				[
					-5.988970305823614,
					16.35935845523386
				],
				[
					-5.988970305823614,
					16.803250651001235
				],
				[
					-5.988970305823614,
					17.491456651265935
				],
				[
					-5.988970305823614,
					18.08511132086096
				],
				[
					-5.988970305823614,
					18.77331732112566
				],
				[
					-5.988970305823614,
					19.364319338077166
				],
				[
					-5.988970305823614,
					19.808256494058924
				],
				[
					-5.988970305823614,
					20.401911163654177
				],
				[
					-5.988970305823614,
					20.845803359421552
				],
				[
					-5.988970305823614,
					21.43685033658744
				],
				[
					-5.988970305823614,
					21.880742532354816
				],
				[
					-5.988970305823614,
					22.324679688336573
				],
				[
					-5.988970305823614,
					23.012885688601273
				],
				[
					-5.988970305823614,
					23.159995509785404
				],
				[
					-5.988970305823614,
					23.456822844582803
				],
				[
					-5.988970305823614,
					23.753650179380656
				],
				[
					-5.988970305823614,
					24.44185617964513
				],
				[
					-5.988970305823614,
					25.032858196596635
				],
				[
					-5.988970305823614,
					25.327032878750742
				],
				[
					-5.988970305823614,
					25.868174018045465
				],
				[
					-5.988970305823614,
					26.015238879015214
				],
				[
					-5.988970305823614,
					26.162348700199345
				],
				[
					-5.988970305823614,
					26.309458521383476
				],
				[
					-5.988970305823614,
					26.750743024721487
				],
				[
					-5.988970305823614,
					27.04757035951934
				],
				[
					-5.841860484639483,
					27.49150751550087
				],
				[
					-5.841860484639483,
					27.785682197654978
				],
				[
					-5.60280702521527,
					28.89152362853656
				],
				[
					-5.455742164245407,
					29.03863344972069
				],
				[
					-5.3086323430612765,
					29.33285309208918
				],
				[
					-5.3086323430612765,
					29.47991795305893
				],
				[
					-5.161522521877146,
					29.776745287856556
				],
				[
					-4.867347839723152,
					30.220682443838314
				],
				[
					-4.57312819735489,
					30.51485712599242
				],
				[
					-3.7378573361204417,
					30.809076768360683
				],
				[
					-3.44363769375218,
					31.103251450514563
				],
				[
					-2.6057141798741554,
					31.103251450514563
				],
				[
					-2.311494537505837,
					31.103251450514563
				],
				[
					-1.7178848281249657,
					31.103251450514563
				],
				[
					-0.8799163540326731,
					31.103251450514563
				],
				[
					-0.7328514930628103,
					31.103251450514563
				],
				[
					-0.43602415826524066,
					31.103251450514563
				],
				[
					-0.2889143370811098,
					30.953533936901067
				],
				[
					-0.14180451589697896,
					30.80381642328757
				],
				[
					-0.14180451589697896,
					30.654098909674303
				],
				[
					-0.14180451589697896,
					30.504381396060808
				],
				[
					0.03677745529603271,
					29.96063256433672
				],
				[
					0.03677745529603271,
					29.81091505072345
				],
				[
					0.18388727648016356,
					29.36171754966881
				],
				[
					0.3309970976642944,
					29.212000036055088
				],
				[
					0.47810691884842527,
					29.06228252244182
				],
				[
					0.47810691884842527,
					28.613085021387178
				],
				[
					0.47810691884842527,
					28.313649994160187
				],
				[
					0.6251717798182881,
					28.014214966933196
				],
				[
					0.8037987112255678,
					27.171031107982344
				],
				[
					0.8037987112255678,
					26.721833606927703
				],
				[
					0.9509085324096986,
					26.42239857970094
				],
				[
					0.9509085324096986,
					25.57921472074986
				],
				[
					1.0980183535938295,
					25.1300621799096
				],
				[
					1.0980183535938295,
					24.830582192468455
				],
				[
					1.4578799088376968,
					24.1371158471311
				],
				[
					1.4578799088376968,
					23.687963306290612
				],
				[
					1.4578799088376968,
					22.84477944733976
				],
				[
					1.4578799088376968,
					22.545344420112997
				],
				[
					1.4578799088376968,
					22.096146919058356
				],
				[
					1.6049447698075596,
					21.497276864604373
				],
				[
					1.6049447698075596,
					21.048079363549732
				],
				[
					1.7520545909916905,
					20.74864433632274
				],
				[
					1.7520545909916905,
					19.90546047737189
				],
				[
					1.7520545909916905,
					19.605980489930744
				],
				[
					1.7520545909916905,
					19.30654546270398
				],
				[
					1.991108050415903,
					18.34516120036278
				],
				[
					2.1696900216089148,
					17.651694855025198
				],
				[
					2.1696900216089148,
					17.501977341411703
				],
				[
					2.1696900216089148,
					17.20254231418494
				],
				[
					2.3167998427930456,
					16.209640941620364
				],
				[
					2.3167998427930456,
					15.760443440565723
				],
				[
					2.4639096639771765,
					15.161573386112195
				],
				[
					2.4639096639771765,
					15.011810912284318
				],
				[
					2.4639096639771765,
					14.412940857830563
				],
				[
					2.6110194851613073,
					13.814025843162426
				],
				[
					2.6110194851613073,
					13.514590815935662
				],
				[
					2.6110194851613073,
					13.065393314881021
				],
				[
					2.6110194851613073,
					11.654856511699336
				],
				[
					2.75808434613117,
					10.811672652748257
				],
				[
					2.905194167315301,
					10.118206307410901
				],
				[
					2.905194167315301,
					9.27502244846005
				],
				[
					2.905194167315301,
					8.282121075895702
				],
				[
					3.052303988499432,
					7.683206061227565
				],
				[
					3.052303988499432,
					7.234053520387079
				],
				[
					3.052303988499432,
					6.93457353294616
				],
				[
					3.052303988499432,
					6.0913896739950815
				],
				[
					3.1994138096836195,
					5.642237133154822
				],
				[
					3.1994138096836195,
					4.948770787817466
				],
				[
					3.1994138096836195,
					4.499618246976979
				],
				[
					3.1994138096836195,
					4.050420745922338
				],
				[
					3.1994138096836195,
					3.4515057312542012
				],
				[
					3.1994138096836195,
					2.852635676800446
				],
				[
					3.1994138096836195,
					2.15916933146309
				],
				[
					3.1994138096836195,
					1.859734304236099
				],
				[
					3.1994138096836195,
					1.4105368031814578
				],
				[
					3.049651335855856,
					0.9613842623411983
				],
				[
					3.049651335855856,
					0.8116667487277027
				],
				[
					2.899933822242417,
					0.6619042748998254
				],
				[
					2.899933822242417,
					0.36246924767306155
				],
				[
					2.899933822242417,
					0.21275173405956593
				],
				[
					2.899933822242417,
					0.0630342204462977
				],
				[
					2.7502163086289784,
					-0.08668329316742529
				],
				[
					2.450781281402044,
					-0.5358807942220665
				],
				[
					2.1513462541751665,
					-0.8353158214488303
				],
				[
					1.5524312395070865,
					-0.9850333350623259
				],
				[
					0.9535162248390066,
					-0.9850333350623259
				],
				[
					0.5043636839986902,
					-0.9850333350623259
				],
				[
					0.3546461703852515,
					-1.1347508486755942
				],
				[
					0.3546461703852515,
					-1.1347508486755942
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				0.3546461703852515,
				-1.1347508486755942
			]
		},
		{
			"id": "ukUG0AJM6YXmy8I_SCQ41",
			"type": "freedraw",
			"x": 67.82394837451461,
			"y": -1457.7565640758135,
			"width": 0.0001,
			"height": 0.0001,
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
			"seed": 173973945,
			"version": 13,
			"versionNonce": 1224404825,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710827914311,
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
			"id": "XrUVMy0nId9NnhN6CusUB",
			"type": "freedraw",
			"x": 67.82394837451461,
			"y": -1457.7565640758135,
			"width": 7.9984333637268605,
			"height": 43.92440964127354,
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
			"seed": 2063921241,
			"version": 98,
			"versionNonce": 200347319,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710827914311,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.5918051471788743,
					0.4728128536148688
				],
				[
					-2.2537431422396423,
					1.161018853879341
				],
				[
					-3.096927001190565,
					2.660891602871743
				],
				[
					-3.614396587657211,
					4.9960689332592665
				],
				[
					-4.4418218914965735,
					7.74889293431761
				],
				[
					-5.749939326506549,
					11.184673830621023
				],
				[
					-5.991600478360084,
					13.102204490337726
				],
				[
					-7.118472049479905,
					16.17811259134396
				],
				[
					-7.3942804840930165,
					18.392459345804582
				],
				[
					-7.635941635946551,
					20.727636676192105
				],
				[
					-7.817187499836706,
					21.268744095326156
				],
				[
					-7.817187499836706,
					23.30972426345261
				],
				[
					-7.817187499836706,
					24.39193910172048
				],
				[
					-7.817187499836706,
					26.18863918551051
				],
				[
					-7.9984333637268605,
					27.270854023778384
				],
				[
					-7.9984333637268605,
					28.10877753765635
				],
				[
					-7.9984333637268605,
					29.364358962258848
				],
				[
					-7.9984333637268605,
					31.578716956773178
				],
				[
					-7.9984333637268605,
					33.07858970576558
				],
				[
					-7.8513347825962825,
					33.67222189525364
				],
				[
					-7.375891756445,
					34.5101678892388
				],
				[
					-7.228793175314436,
					34.95408256511337
				],
				[
					-6.396118766455743,
					36.50649132451326
				],
				[
					-6.0099892060081,
					37.76207274911553
				],
				[
					-5.5660632900799385,
					38.355704938603594
				],
				[
					-5.271866127818797,
					38.64990210086489
				],
				[
					-4.680852870813652,
					39.540384105257544
				],
				[
					-4.236938194939071,
					39.98429878113211
				],
				[
					-3.5802493048976345,
					40.82222229501008
				],
				[
					-3.2834219701000364,
					41.119049629807705
				],
				[
					-3.1363233889694726,
					41.266136970884645
				],
				[
					-2.088255833461048,
					42.31422700650023
				],
				[
					-0.8326744088586793,
					43.08911629993213
				],
				[
					-0.17598551881724234,
					43.7773223001966
				],
				[
					-0.028886937686678493,
					43.92440964127354
				],
				[
					-0.028886937686678493,
					43.77469212766027
				],
				[
					-0.17861569135369848,
					43.47523462032609
				],
				[
					-0.47806195863415724,
					43.17577711299214
				],
				[
					-0.6277907123011772,
					42.72662457215165
				],
				[
					-1.2897287073619594,
					41.58398320586684
				],
				[
					-1.7389037283094382,
					40.9850906713059
				],
				[
					-1.9201495921995928,
					40.44134183958181
				],
				[
					-2.2195958594800516,
					40.141906812355046
				],
				[
					-2.2195958594800516,
					39.99216681863436
				],
				[
					-2.2195958594800516,
					39.842449305020864
				],
				[
					-2.3693133730935045,
					39.54299179768691
				],
				[
					-2.700287990650679,
					38.69980793873583
				],
				[
					-2.850016744317699,
					38.400372911509066
				],
				[
					-3.149463011598158,
					37.80148037694812
				],
				[
					-3.299180525211611,
					37.202565362279984
				],
				[
					-4.024163980772215,
					35.57136382732233
				],
				[
					-4.20540984466237,
					34.483888643981345
				],
				[
					-4.38665570855251,
					33.39641346064036
				],
				[
					-4.8095627242962,
					31.891302846682265
				],
				[
					-5.085371158909325,
					30.063085652669088
				],
				[
					-5.235099912576345,
					29.763628145335133
				],
				[
					-5.47676106442988,
					28.20335134843299
				],
				[
					-5.626478578043319,
					27.509885003095405
				],
				[
					-5.925924845323792,
					26.36726611691779
				],
				[
					-6.075653598990812,
					25.524059777859748
				],
				[
					-6.467043504511366,
					24.26322924823785
				],
				[
					-6.467043504511366,
					23.569774142953975
				],
				[
					-6.467043504511366,
					22.4586611269458
				],
				[
					-6.616761018124805,
					21.465748514327743
				],
				[
					-6.616761018124805,
					20.20491798470607
				],
				[
					-6.979252745905114,
					19.117442801365314
				],
				[
					-6.979252745905114,
					18.02996761802433
				],
				[
					-6.979252745905114,
					15.981108172342147
				],
				[
					-6.979252745905114,
					14.47598631833057
				],
				[
					-6.979252745905114,
					13.21514454865519
				],
				[
					-6.979252745905114,
					11.292376023972793
				],
				[
					-6.619391190661261,
					10.449192165021941
				],
				[
					-6.380360211344183,
					8.644612803676182
				],
				[
					-6.201733279936903,
					7.951157698392308
				],
				[
					-5.876019007452641,
					7.107973839441229
				],
				[
					-5.728920426322077,
					6.264789980490377
				],
				[
					-5.22196028994766,
					5.421606121539526
				],
				[
					-4.896246017463383,
					4.278964755254492
				],
				[
					-4.360387703348721,
					3.0181342256328207
				],
				[
					-3.91647302747414,
					2.5689592046853704
				],
				[
					-3.409512891099709,
					1.7257753457342915
				],
				[
					-3.1153157288385813,
					1.1268715711198638
				],
				[
					-2.789601456354319,
					0.4334164658359896
				],
				[
					-2.642502875223741,
					0.28368771216901223
				],
				[
					-2.495404294093177,
					0.13397019855551662
				],
				[
					-2.495404294093177,
					0.13397019855551662
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				-2.495404294093177,
				0.13397019855551662
			]
		},
		{
			"id": "H8vSIrSg",
			"type": "text",
			"x": 592.1386038274998,
			"y": -1267.7044666516372,
			"width": 313.1358947753906,
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
			"seed": 125278777,
			"version": 85,
			"versionNonce": 846568505,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710827914311,
			"link": null,
			"locked": false,
			"text": "- power를 구할때는 그냥 (1+m)을 적용하면 됨\n  ",
			"rawText": "- power를 구할때는 그냥 (1+m)을 적용하면 됨\n  ",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 34,
			"containerId": null,
			"originalText": "- power를 구할때는 그냥 (1+m)을 적용하면 됨\n  ",
			"lineHeight": 1.25
		},
		{
			"id": "XTCUHNDY",
			"type": "text",
			"x": 592.7340119454526,
			"y": -1047.0979583529397,
			"width": 276.6239013671875,
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
			"seed": 1325045847,
			"version": 176,
			"versionNonce": 241967063,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710827914311,
			"link": null,
			"locked": false,
			"text": "상수 부분은 정보를 담지 않음\n뒷 부분이 정보를 담는다 - power는 작음\n=> power 관점에서는 비효율적임",
			"rawText": "상수 부분은 정보를 담지 않음\n뒷 부분이 정보를 담는다 - power는 작음\n=> power 관점에서는 비효율적임",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 54,
			"containerId": null,
			"originalText": "상수 부분은 정보를 담지 않음\n뒷 부분이 정보를 담는다 - power는 작음\n=> power 관점에서는 비효율적임",
			"lineHeight": 1.25
		},
		{
			"id": "2pVp4TPB-unuAr0uv-8I7",
			"type": "freedraw",
			"x": -269.39478870462386,
			"y": -845.3417842224601,
			"width": 43.50678545070997,
			"height": 48.14557804104754,
			"angle": 0,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 661952151,
			"version": 64,
			"versionNonce": 1839729911,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710827914311,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.0218107903581881,
					1.0139202727488055
				],
				[
					-1.3212458175850657,
					1.310747607546432
				],
				[
					-1.620725805026268,
					1.6049447698076165
				],
				[
					-1.7704433186397068,
					1.4552272561941209
				],
				[
					-1.7704433186397068,
					-1.3028570899371061
				],
				[
					-1.7704433186397068,
					-4.478599346792635
				],
				[
					-1.7704433186397068,
					-7.654319123540972
				],
				[
					-1.7704433186397068,
					-18.886279859550314
				],
				[
					-1.4053214183229557,
					-28.73919842249404
				],
				[
					-0.6803379627623372,
					-38.17445907471347
				],
				[
					0.020996420077324274,
					-45.94174073667898
				],
				[
					0.020996420077324274,
					-46.540633271239926
				],
				[
					0.020996420077324274,
					-46.393545930162986
				],
				[
					0.8563122415260409,
					-43.64072192910464
				],
				[
					3.4646790740437723,
					-36.58790303255387
				],
				[
					7.404767454078126,
					-28.707681312271006
				],
				[
					11.670637546918158,
					-21.23985715763945
				],
				[
					15.51878228871243,
					-14.594197961774398
				],
				[
					20.102476136427356,
					-7.688488886407754
				],
				[
					21.513012939608927,
					-5.644867305691378
				],
				[
					19.566595342205574,
					-6.396130006509338
				],
				[
					17.226191386905896,
					-7.176257164906815
				],
				[
					12.25377152636753,
					-8.944070311010137
				],
				[
					6.572104285272985,
					-10.948261783786847
				],
				[
					1.30811743500999,
					-12.59524435396338
				],
				[
					-3.1205535938043454,
					-13.861323988604454
				],
				[
					-6.713953761384232,
					-15.059131537833423
				],
				[
					-10.85110276068815,
					-16.69033307279119
				],
				[
					-11.150537787915027,
					-16.840050586404686
				],
				[
					-12.143439160479375,
					-17.17102520396179
				],
				[
					-12.29315667409287,
					-17.17102520396179
				],
				[
					-12.742354175147454,
					-17.320742717575285
				],
				[
					-13.041789202374389,
					-17.320742717575285
				],
				[
					-13.640704217042469,
					-17.320742717575285
				],
				[
					-14.089856757882785,
					-17.320742717575285
				],
				[
					-14.239574271496224,
					-17.320742717575285
				],
				[
					-14.242226924139857,
					-17.769917738522736
				],
				[
					-10.769634852379568,
					-19.871313194612526
				],
				[
					-8.434491242152774,
					-21.132154964287793
				],
				[
					-3.1757197767483945,
					-23.09959146187566
				],
				[
					5.001329278332207,
					-25.589735410895855
				],
				[
					13.59601376402992,
					-28.45812964280799
				],
				[
					22.190743209942013,
					-31.326546354827315
				],
				[
					29.264558526570113,
					-33.55403273191678
				],
				[
					27.885493873397365,
					-31.518301668809727
				],
				[
					25.516180500303847,
					-28.521186343361478
				],
				[
					20.538500294692597,
					-24.145028844847616
				],
				[
					14.940908654335942,
					-18.909928932271214
				],
				[
					7.7252438615966526,
					-12.779109150336353
				],
				[
					0.8694406241011734,
					-6.6482893684014925
				],
				[
					-6.653527233367242,
					-0.17336658633439583
				],
				[
					-8.384585404281665,
					1.5524087593998956
				],
				[
					-8.384585404281665,
					1.5524087593998956
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				-8.384585404281665,
				1.5524087593998956
			]
		},
		{
			"id": "xKe1fpia2N1Ru8xaru6cM",
			"type": "freedraw",
			"x": -456.80773278954155,
			"y": -1304.493948804997,
			"width": 49.051818600551826,
			"height": 39.632294023336954,
			"angle": 0,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 836848759,
			"version": 58,
			"versionNonce": 711238137,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710827914311,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-1.1111242560618848
				],
				[
					0,
					-1.9543081150127364
				],
				[
					0.5962623620244472,
					-4.712392461143963
				],
				[
					1.4919822313829627,
					-8.014203158892087
				],
				[
					2.088255833461062,
					-10.772287505023314
				],
				[
					2.7002879906506223,
					-14.783323103220255
				],
				[
					3.343837258063388,
					-19.629674522866253
				],
				[
					4.289474205346664,
					-24.357803059014486
				],
				[
					4.436561546423604,
					-24.507520572627982
				],
				[
					5.179933729632239,
					-22.416645806684073
				],
				[
					7.084324766720329,
					-18.28740980509656
				],
				[
					10.228538673299113,
					-11.300255301528523
				],
				[
					13.811418150733175,
					-3.420033581245434
				],
				[
					16.955620817258477,
					3.5671209223226015
				],
				[
					19.217254477107474,
					8.555276857865238
				],
				[
					18.917796969773462,
					8.255841830638246
				],
				[
					17.830321786432535,
					7.530858375077742
				],
				[
					12.49541019811386,
					4.84632893953858
				],
				[
					3.3727354358036337,
					0.4675412684882758
				],
				[
					-7.407420106721702,
					-4.738649226294228
				],
				[
					-18.18757564924715,
					-9.574479955794232
				],
				[
					-29.535106616110284,
					-14.901523506610602
				],
				[
					-29.834564123444352,
					-14.901523506610602
				],
				[
					-29.687465542313817,
					-15.200981013944556
				],
				[
					-26.516983630531172,
					-15.799873548505502
				],
				[
					-23.346501718748527,
					-16.1177197834877
				],
				[
					-10.454441270041116,
					-17.197304449219246
				],
				[
					-1.0244297228410915,
					-18.652509225306176
				],
				[
					7.570277242963812,
					-20.441318791486765
				],
				[
					13.24667289893182,
					-21.77834564429054
				],
				[
					15.334917492339343,
					-22.07778067151753
				],
				[
					15.482027313523474,
					-22.07778067151753
				],
				[
					15.629114654600471,
					-21.930693330440363
				],
				[
					15.923311816861656,
					-21.930693330440363
				],
				[
					16.070421638045786,
					-21.930693330440363
				],
				[
					16.367226492736222,
					-21.930693330440363
				],
				[
					16.545853424143502,
					-21.38957467125283
				],
				[
					16.545853424143502,
					-20.551651157374863
				],
				[
					15.765703785638834,
					-18.21648506704082
				],
				[
					14.268461209182874,
					-14.628345244533875
				],
				[
					11.938555463921887,
					-9.663793421497758
				],
				[
					8.888892888012435,
					-3.9164842675277214
				],
				[
					4.7281397762018855,
					1.9726743625535619
				],
				[
					-1.5130123716210733,
					10.633068201448395
				],
				[
					-4.423444403902181,
					14.830598768555092
				],
				[
					-4.722890671182654,
					15.124773450708972
				],
				[
					-4.722890671182654,
					15.124773450708972
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				-4.722890671182654,
				15.124773450708972
			]
		},
		{
			"id": "itlk2jHlHA8WomYoMQE4D",
			"type": "freedraw",
			"x": 115.35216379563437,
			"y": -492.62914562889074,
			"width": 4.662430892030699,
			"height": 10.037798409390746,
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
			"seed": 1049690521,
			"version": 28,
			"versionNonce": 760216281,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710827914311,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.7631091556331171
				],
				[
					0,
					2.954238745818145
				],
				[
					-0.36379557770013093,
					4.911217932452814
				],
				[
					-0.5833272375777909,
					6.006782727545328
				],
				[
					-1.187562678315345,
					8.628601620302334
				],
				[
					-1.187562678315345,
					8.98195651632193
				],
				[
					-1.187562678315345,
					9.09904961129621
				],
				[
					-1.187562678315345,
					9.333200014846568
				],
				[
					-1.187562678315345,
					9.450293109820848
				],
				[
					-1.187562678315345,
					9.803648005840387
				],
				[
					-0.30734253450881965,
					9.920705314416466
				],
				[
					0.24043986303743736,
					10.037798409390746
				],
				[
					0.9073999132542525,
					10.037798409390746
				],
				[
					1.4969897705204716,
					10.037798409390746
				],
				[
					2.6908240151237948,
					10.037798409390746
				],
				[
					3.238606412670052,
					10.037798409390746
				],
				[
					3.4748682137153537,
					10.037798409390746
				],
				[
					3.4748682137153537,
					10.037798409390746
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				3.4748682137153537,
				10.037798409390746
			]
		},
		{
			"id": "GaaCJypnEz0KqAGp09Hy0",
			"type": "freedraw",
			"x": 126.85560309070529,
			"y": -490.34812060637825,
			"width": 6.119697760527487,
			"height": 9.088599983016138,
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
			"seed": 2040601369,
			"version": 40,
			"versionNonce": 199523127,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710827914311,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.11916870607100805,
					-0.23833741214207294
				],
				[
					-0.7903068182799586,
					-0.23833741214207294
				],
				[
					-1.2670084823626837,
					-0.23833741214207294
				],
				[
					-2.176492953313229,
					-0.23833741214207294
				],
				[
					-3.180068811782462,
					-0.23833741214207294
				],
				[
					-3.8512069239914126,
					-0.0961938384140808
				],
				[
					-4.735605129790059,
					0.21117553589340332
				],
				[
					-4.973951488531654,
					0.3282328444694258
				],
				[
					-5.212297847273234,
					0.6815877404890216
				],
				[
					-5.450644206014815,
					0.9157739304375809
				],
				[
					-5.688990564756409,
					1.2690930400589764
				],
				[
					-5.8081682174269815,
					2.26849978313561
				],
				[
					-5.927345870097554,
					2.740987598827985
				],
				[
					-6.119697760527487,
					4.051914938405616
				],
				[
					-6.119697760527487,
					5.05132168148225
				],
				[
					-6.119697760527487,
					6.577575779146741
				],
				[
					-6.119697760527487,
					7.675216185335955
				],
				[
					-6.119697760527487,
					8.028571081355551
				],
				[
					-6.119697760527487,
					8.14566417632983
				],
				[
					-6.119697760527487,
					8.26275727130411
				],
				[
					-6.119697760527487,
					8.37981457988019
				],
				[
					-6.119697760527487,
					8.49690767485447
				],
				[
					-6.119697760527487,
					8.733169475899786
				],
				[
					-5.647183105036447,
					8.850262570874065
				],
				[
					-5.1746595029458575,
					8.850262570874065
				],
				[
					-3.2176982095102886,
					8.850262570874065
				],
				[
					-1.8858716133724727,
					8.850262570874065
				],
				[
					-1.0056604161655116,
					8.850262570874065
				],
				[
					-0.4578690720196903,
					8.850262570874065
				],
				[
					-0.4578690720196903,
					8.850262570874065
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				-0.4578690720196903,
				8.850262570874065
			]
		},
		{
			"id": "wd0tKEwBywbvGnVdej6kL",
			"type": "freedraw",
			"x": 133.38091283525245,
			"y": -489.3320016153331,
			"width": 0.11709309497427967,
			"height": 0.2383374121420161,
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
			"seed": 859404057,
			"version": 12,
			"versionNonce": 1864185785,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710827914311,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.11709309497427967,
					-0.2383374121420161
				],
				[
					0.11709309497427967,
					-0.2383374121420161
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				0.11709309497427967,
				-0.2383374121420161
			]
		},
		{
			"id": "c9W6DX6nR2uBwL17gHxOm",
			"type": "freedraw",
			"x": 132.16199232549724,
			"y": -482.84013425992214,
			"width": 0,
			"height": 0.7066740056409913,
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
			"seed": 1529651865,
			"version": 13,
			"versionNonce": 104725591,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710827914311,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.5895809106667116
				],
				[
					0,
					0.7066740056409913
				],
				[
					0,
					0.7066740056409913
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				0,
				0.7066740056409913
			]
		},
		{
			"id": "FpHbmbhy",
			"type": "text",
			"x": 149.65359647443978,
			"y": -498.67332514257544,
			"width": 160.4479522705078,
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
			"seed": 2022841305,
			"version": 89,
			"versionNonce": 32495769,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710827914311,
			"link": null,
			"locked": false,
			"text": "LC는 뭔가가 추가될까요",
			"rawText": "LC는 뭔가가 추가될까요",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 14,
			"containerId": null,
			"originalText": "LC는 뭔가가 추가될까요",
			"lineHeight": 1.25
		},
		{
			"id": "U2qm0JUm3L6NV4gX7f28q",
			"type": "freedraw",
			"x": 265.2565637200608,
			"y": -501.4480593149245,
			"width": 16.627935214312544,
			"height": 26.161861136772416,
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
			"seed": 90344217,
			"version": 43,
			"versionNonce": 940202359,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710827914311,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.23835530534114469,
					-0.551969406137971
				],
				[
					-0.38262816976310887,
					-1.1039030258776847
				],
				[
					-0.38262816976310887,
					-2.8727173306741065
				],
				[
					-0.38262816976310887,
					-4.403158436930255
				],
				[
					-0.38262816976310887,
					-6.2660551826458
				],
				[
					-0.38262816976310887,
					-8.128916141963145
				],
				[
					-0.38262816976310887,
					-10.424577801347425
				],
				[
					-0.38262816976310887,
					-12.95235003958345
				],
				[
					-0.8133174723350862,
					-15.14766663836025
				],
				[
					-0.8133174723350862,
					-16.013232252095747
				],
				[
					-0.9575903367571073,
					-17.87612899781135
				],
				[
					-1.0767590428281437,
					-18.879686963081497
				],
				[
					-1.2210140140510362,
					-19.86445706928629
				],
				[
					-1.3402006133211444,
					-20.221963187499398
				],
				[
					-1.5325525037511056,
					-20.987183740627472
				],
				[
					-1.651721209822142,
					-21.344725645238725
				],
				[
					-1.7708899158931217,
					-21.583063057380798
				],
				[
					-2.0092452212342664,
					-22.059773668063087
				],
				[
					-2.3667692326464476,
					-22.29811108020516
				],
				[
					-2.724293244058572,
					-22.53644849234712
				],
				[
					-4.164838917987311,
					-23.39993849498609
				],
				[
					-6.360137623564924,
					-23.830627797557952
				],
				[
					-8.22303436928047,
					-24.43276973399969
				],
				[
					-9.559030080810828,
					-24.771487993147446
				],
				[
					-10.995388746147881,
					-25.29837113413356
				],
				[
					-12.19340999934289,
					-25.634977995786414
				],
				[
					-13.05899350627763,
					-25.779232967009364
				],
				[
					-14.06256936474685,
					-25.898437459478544
				],
				[
					-15.166490283823634,
					-26.017606165549466
				],
				[
					-15.59927309069144,
					-26.161861136772416
				],
				[
					-16.151242496829383,
					-26.161861136772416
				],
				[
					-16.627935214312544,
					-26.161861136772416
				],
				[
					-16.627935214312544,
					-26.161861136772416
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				-16.627935214312544,
				-26.161861136772416
			]
		},
		{
			"id": "tTPc-Cpah3Wxe4eSoERkI",
			"type": "freedraw",
			"x": 251.46162293439866,
			"y": -530.4512888975307,
			"width": 4.7126034223344675,
			"height": 10.238524317004021,
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
			"seed": 1625469369,
			"version": 29,
			"versionNonce": 1736138105,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710827914311,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.35752401141215273,
					0.11709309497427967
				],
				[
					-0.5958793167532974,
					0.3533548960195958
				],
				[
					-1.1478308296921398,
					0.7568823223430172
				],
				[
					-1.8189689419010904,
					1.1603739622680678
				],
				[
					-2.176492953313243,
					1.5137288582876636
				],
				[
					-2.534016964725396,
					1.8670837543072594
				],
				[
					-2.8915409761375486,
					2.3395715699996344
				],
				[
					-2.8915409761375486,
					2.5758333710449506
				],
				[
					-3.1298962814786933,
					2.6929264660192302
				],
				[
					-3.1298962814786933,
					2.927076869569646
				],
				[
					-2.8706417195773497,
					3.7111210681611055
				],
				[
					-2.6364734228278905,
					4.183644670251738
				],
				[
					-2.1388635555854023,
					5.063882707257335
				],
				[
					-1.246100279202949,
					6.1761597503184475
				],
				[
					0.562419034418042,
					8.260645873809153
				],
				[
					1.4656319390805947,
					9.690741919457878
				],
				[
					1.4656319390805947,
					10.121467008427999
				],
				[
					1.5827071408557742,
					10.238524317004021
				],
				[
					1.5827071408557742,
					10.238524317004021
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				1.5827071408557742,
				10.238524317004021
			]
		},
		{
			"id": "ZzUiZfe4gK6ZrYfSyAYUn",
			"type": "freedraw",
			"x": -210.6247687562784,
			"y": -362.0853750198172,
			"width": 49.22100576151388,
			"height": 26.912462946227834,
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
			"seed": 2025040921,
			"version": 63,
			"versionNonce": 1720586903,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710827914311,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.7903068182799871,
					0
				],
				[
					-1.0286442304220031,
					0
				],
				[
					-2.5590853366781516,
					0.3596175157080097
				],
				[
					-5.620003335588706,
					1.5095418496960065
				],
				[
					-6.410310153868693,
					1.8879651176683296
				],
				[
					-6.962279560006664,
					2.1743994490174146
				],
				[
					-8.298293164736151,
					2.5089306995735114
				],
				[
					-9.8287342709923,
					2.5089306995735114
				],
				[
					-11.791976077315383,
					2.5089306995735114
				],
				[
					-14.984588021673801,
					2.5089306995735114
				],
				[
					-19.174495311613896,
					1.9820475585874533
				],
				[
					-23.03198274849285,
					0.9533854349663216
				],
				[
					-27.98711059156102,
					-0.28017171166061416
				],
				[
					-30.8473026828583,
					-0.9952018412858479
				],
				[
					-32.18328050118953,
					-1.672620466382341
				],
				[
					-33.2997803392405,
					-2.7891024112341256
				],
				[
					-33.801541428676444,
					-3.792660376504273
				],
				[
					-34.57721161008459,
					-6.088339929087624
				],
				[
					-34.9138542581357,
					-7.286343289083561
				],
				[
					-35.32571991524418,
					-9.14924003479905
				],
				[
					-35.51807180567414,
					-10.679681141055255
				],
				[
					-35.51807180567414,
					-13.972656039220283
				],
				[
					-35.51807180567414,
					-14.97621400449043
				],
				[
					-35.51807180567414,
					-15.979789862959649
				],
				[
					-35.231637474325055,
					-17.510248862414926
				],
				[
					-34.73402760708257,
					-18.513806827685016
				],
				[
					-32.915076558380576,
					-20.48332914689564
				],
				[
					-30.943460734874122,
					-21.800519106161687
				],
				[
					-28.087455652168558,
					-22.515549235786864
				],
				[
					-25.89632606198353,
					-22.992259846469153
				],
				[
					-21.944756184185508,
					-23.450128918488872
				],
				[
					-19.088751101479943,
					-23.92683952917116
				],
				[
					-16.23278180517258,
					-24.403532246654322
				],
				[
					-13.709196575528154,
					-24.403532246654322
				],
				[
					-11.850486838404322,
					-24.403532246654322
				],
				[
					-6.901621615024567,
					-24.403532246654322
				],
				[
					-3.048356973135526,
					-24.403532246654322
				],
				[
					0.4725236020905754,
					-24.403532246654322
				],
				[
					3.993404177316677,
					-23.90173537082012
				],
				[
					8.277393908175952,
					-23.192967860883357
				],
				[
					10.80094335142212,
					-22.281398832236505
				],
				[
					12.992072941607148,
					-21.40744130811845
				],
				[
					13.226259131555707,
					-21.173273011368963
				],
				[
					13.343352226529987,
					-19.62819526824103
				],
				[
					13.485495800257922,
					-18.0036717210657
				],
				[
					13.70293395583974,
					-15.480104384620404
				],
				[
					13.70293395583974,
					-12.624099301914839
				],
				[
					13.483420189161222,
					-6.481399833931789
				],
				[
					12.109795079902995,
					-4.1773641573641385
				],
				[
					10.79260512063695,
					-1.9862345671791672
				],
				[
					9.25586560829413,
					-0.014636636871784958
				],
				[
					8.37773896878349,
					0.8613964983430833
				],
				[
					8.37773896878349,
					0.8613964983430833
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				8.37773896878349,
				0.8613964983430833
			]
		},
		{
			"id": "q35eetPr",
			"type": "text",
			"x": -1000.8815831832469,
			"y": -423.42234901492697,
			"width": 403.37579345703125,
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
			"seed": 437859415,
			"version": 100,
			"versionNonce": 1935348537,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710827914312,
			"link": null,
			"locked": false,
			"text": "- idea : ussb/lssb 둘 중 하나만 있어도 복구하는데 문제x",
			"rawText": "- idea : ussb/lssb 둘 중 하나만 있어도 복구하는데 문제x",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "right",
			"verticalAlign": "top",
			"baseline": 14,
			"containerId": null,
			"originalText": "- idea : ussb/lssb 둘 중 하나만 있어도 복구하는데 문제x",
			"lineHeight": 1.25
		},
		{
			"id": "kd20CvzXX_i_PlECr2xen",
			"type": "freedraw",
			"x": -476.2288320721158,
			"y": -219.41491077202562,
			"width": 47.830256148323315,
			"height": 24.055518806848852,
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
			"seed": 1164892823,
			"version": 97,
			"versionNonce": 1375574231,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710827914312,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.14161337064700774,
					0
				],
				[
					-0.5664747458568513,
					0.2807602021055118
				],
				[
					-1.595085377245482,
					0.6186760709226178
				],
				[
					-4.718170518464433,
					1.0460252485897854
				],
				[
					-6.931910703363656,
					1.326785450695354
				],
				[
					-8.12450366424622,
					1.4658897556161605
				],
				[
					-8.92204635286896,
					1.9156078921302537
				],
				[
					-10.464972931586317,
					2.0845658265387783
				],
				[
					-11.262515620209001,
					2.0845658265387783
				],
				[
					-13.47625580510828,
					2.3429570697974214
				],
				[
					-16.48007527125833,
					2.3429570697974214
				],
				[
					-19.878966272937078,
					2.623717271902933
				],
				[
					-23.27783601134695,
					2.904477474008445
				],
				[
					-24.21699207061664,
					3.0734354084170263
				],
				[
					-24.500240075179477,
					3.0734354084170263
				],
				[
					-26.602177992381712,
					2.6411106258352675
				],
				[
					-27.6307886237704,
					2.469686152238239
				],
				[
					-28.197263369627194,
					2.469686152238239
				],
				[
					-28.853192687602927,
					2.186416884406526
				],
				[
					-29.136419428896943,
					2.186416884406526
				],
				[
					-30.21721012208252,
					1.873379040162547
				],
				[
					-32.03590003472192,
					1.6447988998539245
				],
				[
					-33.086879624957476,
					1.274605388898351
				],
				[
					-34.27947258584004,
					0.9044118779427777
				],
				[
					-35.844725596866624,
					0.13668029227011402
				],
				[
					-36.89570518710218,
					-0.23351321868545938
				],
				[
					-38.31936609075058,
					-0.804984832725836
				],
				[
					-39.116908779373375,
					-1.289489677104541
				],
				[
					-39.40013552066728,
					-1.5727164183984996
				],
				[
					-39.824996895877234,
					-1.9975565303395229
				],
				[
					-40.309480476987005,
					-2.795099218962207
				],
				[
					-40.79398532136577,
					-3.592641907584948
				],
				[
					-41.16417883232134,
					-4.926869502383397
				],
				[
					-41.618851310481205,
					-5.724412191006081
				],
				[
					-41.618851310481205,
					-6.521954879628822
				],
				[
					-41.879730356197115,
					-8.10959811277121
				],
				[
					-41.879730356197115,
					-9.533216489881909
				],
				[
					-41.879730356197115,
					-10.845075125833375
				],
				[
					-41.53934794819156,
					-11.642617814456116
				],
				[
					-40.7591986135011,
					-13.088647676951496
				],
				[
					-40.418816205495546,
					-13.744576994927229
				],
				[
					-39.80016139784175,
					-15.056393104340998
				],
				[
					-39.29082105542773,
					-16.085024998998506
				],
				[
					-38.49825397171958,
					-16.71114321402422
				],
				[
					-38.078346938155505,
					-17.135983325965185
				],
				[
					-37.285779854447355,
					-17.44906369674692
				],
				[
					-36.493212770739206,
					-17.933526014587926
				],
				[
					-34.734145063999904,
					-19.073960176942364
				],
				[
					-34.17262465978877,
					-19.215573547589372
				],
				[
					-33.52167094672768,
					-19.3869980211864
				],
				[
					-32.334053590759765,
					-19.757191532141974
				],
				[
					-31.029658362180214,
					-20.24169637652068
				],
				[
					-30.23709127847212,
					-20.383309747167687
				],
				[
					-28.81840597973826,
					-20.611889887476252
				],
				[
					-27.6307886237704,
					-20.75350325812326
				],
				[
					-25.931343122931025,
					-20.982083398431826
				],
				[
					-25.138776039222876,
					-20.982083398431826
				],
				[
					-23.95115868325496,
					-20.982083398431826
				],
				[
					-22.532473384521154,
					-20.982083398431826
				],
				[
					-20.579612245337785,
					-20.982083398431826
				],
				[
					-17.580747120833507,
					-20.982083398431826
				],
				[
					-14.58188199632923,
					-20.982083398431826
				],
				[
					-11.583016871824952,
					-20.982083398431826
				],
				[
					-9.374252291840321,
					-20.813125464023244
				],
				[
					-7.048688575975234,
					-20.02055838031515
				],
				[
					-4.049823451470957,
					-19.501309354609532
				],
				[
					-1.446008599226559,
					-18.93727988467225
				],
				[
					1.1578062530178954,
					-18.2043350068642
				],
				[
					3.483348705614162,
					-17.175745638744445
				],
				[
					3.764108907719674,
					-17.036598807285884
				],
				[
					3.9032344759093576,
					-16.897451975827323
				],
				[
					4.7206583209217,
					-14.94459083664401
				],
				[
					5.17284299662424,
					-13.130876528919202
				],
				[
					5.692134548867614,
					-11.317162221194451
				],
				[
					5.9505257921262,
					-9.734494592966655
				],
				[
					5.9505257921262,
					-7.408930877101568
				],
				[
					5.9505257921262,
					-5.990245578367762
				],
				[
					5.607655581663323,
					-5.1976784946596695
				],
				[
					4.924402963194893,
					-3.383964186934861
				],
				[
					4.328095851119201,
					-2.3379389383450757
				],
				[
					3.9032344759093576,
					-1.495700858566181
				],
				[
					3.5901966316653215,
					-0.8447471455050959
				],
				[
					3.4485619977494935,
					-0.4248401119409664
				],
				[
					2.9938895195896293,
					0.6211426101110646
				],
				[
					2.5690281443797858,
					0.8994362730281864
				],
				[
					2.144166769169942,
					1.1776874094075538
				],
				[
					2.0025533985229913,
					1.3168342408660578
				],
				[
					1.7193053939600986,
					1.4559810723246187
				],
				[
					1.7193053939600986,
					1.4559810723246187
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				1.7193053939600986,
				1.4559810723246187
			]
		},
		{
			"id": "x25fvbQZFd2yNy4XjurU-",
			"type": "freedraw",
			"x": -465.3042323207239,
			"y": -217.38996715138683,
			"width": 105.8223560672804,
			"height": 1.175220870219107,
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
			"seed": 1934664247,
			"version": 61,
			"versionNonce": 731404537,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710827914312,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7925883469769701,
					0
				],
				[
					5.488389906594421,
					0
				],
				[
					7.697175749847872,
					0
				],
				[
					11.091069883343152,
					0
				],
				[
					14.206712880459065,
					0
				],
				[
					15.230347906933048,
					0
				],
				[
					16.254004196675908,
					0
				],
				[
					18.462768776660482,
					0
				],
				[
					20.671533356645114,
					0
				],
				[
					25.762406451791264,
					0
				],
				[
					27.971171031775896,
					0
				],
				[
					30.57498588402035,
					0
				],
				[
					32.78377172727386,
					-0.26090030898478744
				],
				[
					36.29444373338066,
					-0.26090030898478744
				],
				[
					38.108179304374346,
					-0.26090030898478744
				],
				[
					40.31694388435892,
					-0.26090030898478744
				],
				[
					42.130679455352606,
					-0.26090030898478744
				],
				[
					44.33944403533724,
					-0.26090030898478744
				],
				[
					47.850137304712916,
					-0.26090030898478744
				],
				[
					50.45395215695737,
					-0.26090030898478744
				],
				[
					53.057767009201825,
					-0.26090030898478744
				],
				[
					55.66158186144628,
					-0.26090030898478744
				],
				[
					58.265396713690734,
					-0.26090030898478744
				],
				[
					62.171140255326236,
					-0.26090030898478744
				],
				[
					64.77495510757069,
					-0.5217580914318205
				],
				[
					66.35762273579849,
					-0.5217580914318205
				],
				[
					68.56638731578306,
					-0.8050273592635335
				],
				[
					69.63971460159672,
					-0.9466407299105413
				],
				[
					71.45345017259035,
					-0.9466407299105413
				],
				[
					72.87213547132421,
					-0.9466407299105413
				],
				[
					74.29082077005802,
					-0.9466407299105413
				],
				[
					75.70950606879188,
					-0.9466407299105413
				],
				[
					77.8039805786222,
					-0.9466407299105413
				],
				[
					79.22266587735601,
					-1.175220870219107
				],
				[
					80.80533350558375,
					-1.175220870219107
				],
				[
					82.61904781330855,
					-1.175220870219107
				],
				[
					85.73469081042447,
					-1.175220870219107
				],
				[
					86.92232942966126,
					-1.175220870219107
				],
				[
					88.504997057889,
					-1.175220870219107
				],
				[
					89.5286108210941,
					-1.175220870219107
				],
				[
					91.73739666434761,
					-1.175220870219107
				],
				[
					94.85301839819465,
					-1.175220870219107
				],
				[
					97.0618042414481,
					-1.175220870219107
				],
				[
					98.2494003341472,
					-1.175220870219107
				],
				[
					98.90035404720828,
					-1.175220870219107
				],
				[
					99.69296365745413,
					-1.175220870219107
				],
				[
					100.39358836658602,
					-1.175220870219107
				],
				[
					101.18615545029411,
					-1.175220870219107
				],
				[
					102.60484074902797,
					-1.175220870219107
				],
				[
					103.67816803484158,
					-1.175220870219107
				],
				[
					103.81731486630014,
					-1.175220870219107
				],
				[
					105.12168883161081,
					-1.175220870219107
				],
				[
					105.68320923582189,
					-1.175220870219107
				],
				[
					105.8223560672804,
					-1.175220870219107
				],
				[
					105.8223560672804,
					-1.175220870219107
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				105.8223560672804,
				-1.175220870219107
			]
		},
		{
			"id": "PWATqiabi_ODb7w4RuiLK",
			"type": "freedraw",
			"x": -484.96206059745543,
			"y": -197.5408332446687,
			"width": 43.51953238786757,
			"height": 0,
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
			"seed": 1873416791,
			"version": 36,
			"versionNonce": 997232407,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710827914312,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5118281448714583,
					0
				],
				[
					2.7205927248560897,
					0
				],
				[
					4.139278023589895,
					0
				],
				[
					7.138143148094173,
					0
				],
				[
					11.043865426460854,
					0
				],
				[
					12.23148278242877,
					0
				],
				[
					13.02407112940574,
					0
				],
				[
					13.816638213113833,
					0
				],
				[
					15.235323511847696,
					0
				],
				[
					19.931146334734024,
					0
				],
				[
					22.139910914718598,
					0
				],
				[
					25.138776039222876,
					0
				],
				[
					27.347540619207507,
					0
				],
				[
					28.189821225524156,
					0
				],
				[
					28.32894679371384,
					0
				],
				[
					29.121513877421933,
					0
				],
				[
					30.145170167164792,
					0
				],
				[
					33.14401402840019,
					0
				],
				[
					36.25965702551605,
					0
				],
				[
					38.46844286876956,
					0
				],
				[
					39.65606022473747,
					0
				],
				[
					40.307013937798615,
					0
				],
				[
					40.5852863374468,
					0
				],
				[
					40.866025276283494,
					0
				],
				[
					41.658613623260464,
					0
				],
				[
					42.68224864973445,
					0
				],
				[
					42.96052104938269,
					0
				],
				[
					43.38040681967789,
					0
				],
				[
					43.51953238786757,
					0
				],
				[
					43.51953238786757,
					0
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				43.51953238786757,
				0
			]
		},
		{
			"id": "pWfnJxxmcmsKeJdxpADrG",
			"type": "freedraw",
			"x": -379.3335192258878,
			"y": -197.0911151081546,
			"width": 60.07417794303865,
			"height": 0,
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
			"seed": 240121431,
			"version": 41,
			"versionNonce": 1559548377,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710827914312,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.13914683145856088,
					0
				],
				[
					1.1628031212014207,
					0
				],
				[
					2.976517428926229,
					0
				],
				[
					4.395202727660035,
					0
				],
				[
					6.603988570913543,
					0
				],
				[
					7.677315856727148,
					0
				],
				[
					8.23879373440053,
					0
				],
				[
					9.657479033134337,
					0
				],
				[
					11.471235867396842,
					0
				],
				[
					14.586857601243878,
					0
				],
				[
					16.005542899977684,
					0
				],
				[
					17.424228198711546,
					0
				],
				[
					19.237942506436298,
					0
				],
				[
					21.16847721331044,
					0
				],
				[
					22.982191521035247,
					0
				],
				[
					25.1909773642887,
					0
				],
				[
					27.399720681004453,
					0
				],
				[
					30.003535533248908,
					0
				],
				[
					32.72412825810494,
					0
				],
				[
					35.327943110349395,
					0
				],
				[
					37.14169994461196,
					0
				],
				[
					38.56038524334576,
					0
				],
				[
					41.280977968201796,
					0
				],
				[
					43.48972128491755,
					0
				],
				[
					45.69850712817106,
					0
				],
				[
					48.30232198041551,
					0
				],
				[
					51.30120836818861,
					0
				],
				[
					53.39568287801899,
					0
				],
				[
					54.04663659108007,
					0
				],
				[
					55.23423268377917,
					0
				],
				[
					56.42187130301596,
					0
				],
				[
					58.74743501888105,
					0
				],
				[
					59.93503111158009,
					0
				],
				[
					60.07417794303865,
					0
				],
				[
					60.07417794303865,
					0
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				60.07417794303865,
				0
			]
		},
		{
			"id": "cy68SYBhvnAd2refgdGh1",
			"type": "freedraw",
			"x": -306.016662486233,
			"y": -114.80749536120584,
			"width": 93.2330975229138,
			"height": 1.336694133986839,
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
			"seed": 1780450295,
			"version": 63,
			"versionNonce": 920425527,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710827914312,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.1876386192367931,
					0
				],
				[
					2.8870841200761674,
					0
				],
				[
					4.700798427800976,
					0
				],
				[
					5.493365511509069,
					0
				],
				[
					5.913272545073141,
					0
				],
				[
					6.191523681452509,
					-0.2832267412940155
				],
				[
					6.611430715016581,
					-0.2832267412940155
				],
				[
					7.403997798724674,
					-0.4248401119409664
				],
				[
					8.054951511785816,
					-0.4248401119409664
				],
				[
					10.263737355039268,
					-0.4248401119409664
				],
				[
					13.379359088886304,
					-0.6534202522495889
				],
				[
					15.193073396611055,
					-0.6534202522495889
				],
				[
					16.380712015847905,
					-0.8820003925580977
				],
				[
					16.94223242005893,
					-1.0236562897429167
				],
				[
					17.73479950376708,
					-1.0236562897429167
				],
				[
					18.52736658747517,
					-1.195080763339888
				],
				[
					20.341080895199923,
					-1.195080763339888
				],
				[
					23.339967282973078,
					-1.195080763339888
				],
				[
					26.455589016820113,
					-1.195080763339888
				],
				[
					29.454475404593268,
					-1.195080763339888
				],
				[
					31.663218721309022,
					-1.195080763339888
				],
				[
					33.08190402004283,
					-1.195080763339888
				],
				[
					35.407467735907915,
					-1.195080763339888
				],
				[
					37.61625357916142,
					-1.195080763339888
				],
				[
					40.22006843140582,
					-1.195080763339888
				],
				[
					42.823883283650275,
					-1.195080763339888
				],
				[
					44.40655091187807,
					-1.195080763339888
				],
				[
					46.10599641271739,
					-1.195080763339888
				],
				[
					47.9197107204422,
					-1.195080763339888
				],
				[
					49.733425028167005,
					-1.195080763339888
				],
				[
					50.757081317909865,
					-1.195080763339888
				],
				[
					54.267774587285544,
					-1.195080763339888
				],
				[
					56.4765179040013,
					-1.195080763339888
				],
				[
					58.68530374725481,
					-1.195080763339888
				],
				[
					59.4778708309629,
					-1.195080763339888
				],
				[
					61.68665667421641,
					-1.195080763339888
				],
				[
					64.80227840806339,
					-1.195080763339888
				],
				[
					67.80116479583654,
					-1.195080763339888
				],
				[
					70.404979648081,
					-1.195080763339888
				],
				[
					71.59257574078003,
					-1.195080763339888
				],
				[
					72.38514282448818,
					-1.195080763339888
				],
				[
					72.94666322869921,
					-1.195080763339888
				],
				[
					75.04113773852959,
					-1.195080763339888
				],
				[
					76.45982303726339,
					-1.195080763339888
				],
				[
					78.2735798715259,
					-1.195080763339888
				],
				[
					79.85624749975369,
					-1.336694133986839
				],
				[
					83.76196977812032,
					-1.336694133986839
				],
				[
					86.76081363935577,
					-1.336694133986839
				],
				[
					88.96959948260923,
					-1.336694133986839
				],
				[
					90.38828478134309,
					-1.336694133986839
				],
				[
					91.08890949047498,
					-1.336694133986839
				],
				[
					91.22805632193348,
					-1.336694133986839
				],
				[
					91.87901003499462,
					-1.336694133986839
				],
				[
					92.67157711870271,
					-1.336694133986839
				],
				[
					92.95233732080823,
					-1.336694133986839
				],
				[
					93.2330975229138,
					-1.336694133986839
				],
				[
					93.2330975229138,
					-1.336694133986839
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				93.2330975229138,
				-1.336694133986839
			]
		},
		{
			"id": "Nuw3xXQP",
			"type": "text",
			"x": -203.4223769130419,
			"y": -132.313927357353,
			"width": 109.67994689941406,
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
			"seed": 2034843511,
			"version": 71,
			"versionNonce": 571420345,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710827914312,
			"link": null,
			"locked": false,
			"text": "<- domain 변환",
			"rawText": "<- domain 변환",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "right",
			"verticalAlign": "top",
			"baseline": 14,
			"containerId": null,
			"originalText": "<- domain 변환",
			"lineHeight": 1.25
		},
		{
			"id": "LRGsamuneiioIG6knsMFP",
			"type": "rectangle",
			"x": -534.7327388726756,
			"y": -160.17803783038897,
			"width": 191.59678792721536,
			"height": 27.143795976934257,
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
			"roundness": {
				"type": 3
			},
			"seed": 1220141241,
			"version": 65,
			"versionNonce": 751498583,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710827914312,
			"link": null,
			"locked": false
		},
		{
			"id": "aGT0urr5",
			"type": "text",
			"x": -223.76286788046662,
			"y": -68.41805957450583,
			"width": 63.3599853515625,
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
			"seed": 1821411895,
			"version": 41,
			"versionNonce": 294317977,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710827914312,
			"link": null,
			"locked": false,
			"text": "진짜 변환\n",
			"rawText": "진짜 변환\n",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 34,
			"containerId": null,
			"originalText": "진짜 변환\n",
			"lineHeight": 1.25
		},
		{
			"id": "j19pqYQ9OCSFFcNhOhBho",
			"type": "rectangle",
			"x": 258.9671454842597,
			"y": -363.53177616875246,
			"width": 76.59896986872195,
			"height": 24.490310128619114,
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
			"roundness": {
				"type": 3
			},
			"seed": 1385957463,
			"version": 46,
			"versionNonce": 1418736247,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710827914312,
			"link": null,
			"locked": false
		},
		{
			"id": "3CxaOIQAHfY0d-4n1QT1w",
			"type": "freedraw",
			"x": 314.88962765469074,
			"y": -308.46399235365567,
			"width": 196.2528271740535,
			"height": 1.3143251751399134,
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
			"seed": 1165015959,
			"version": 133,
			"versionNonce": 563844217,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710827914312,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.7006247091318869,
					0
				],
				[
					1.88826332836868,
					0
				],
				[
					2.449741206042006,
					0
				],
				[
					3.4957664546318483,
					0
				],
				[
					4.338004534410686,
					0
				],
				[
					4.618764736516255,
					0
				],
				[
					5.130614144656533,
					0
				],
				[
					5.923181228364626,
					0
				],
				[
					6.4349881099672075,
					0
				],
				[
					7.2275551936753,
					0
				],
				[
					7.647462227239373,
					0
				],
				[
					8.208982631450453,
					0
				],
				[
					9.232596394655616,
					0
				],
				[
					9.371743226114177,
					0
				],
				[
					9.649994362493487,
					0
				],
				[
					10.069901396057617,
					0
				],
				[
					10.86246847976571,
					0
				],
				[
					12.676225314028216,
					0
				],
				[
					15.001746503355548,
					0
				],
				[
					15.794313587063698,
					0
				],
				[
					16.701192004194922,
					0
				],
				[
					16.98195220630049,
					0
				],
				[
					17.888830623431716,
					0
				],
				[
					18.681397707139865,
					0
				],
				[
					19.70501147034497,
					0
				],
				[
					21.91379731359848,
					0
				],
				[
					22.93745360334134,
					0
				],
				[
					25.03192811317166,
					0
				],
				[
					25.451792620197978,
					0
				],
				[
					25.871699653762107,
					0
				],
				[
					26.29160668732618,
					0
				],
				[
					27.759962982130787,
					0
				],
				[
					28.55253006583888,
					0
				],
				[
					29.57618635558174,
					0
				],
				[
					30.994871654315546,
					0
				],
				[
					32.53033482566099,
					0
				],
				[
					34.11300245388878,
					0
				],
				[
					35.30059854658782,
					0
				],
				[
					37.50938438984133,
					0
				],
				[
					38.69698048254037,
					0
				],
				[
					40.27964811076811,
					0
				],
				[
					41.60643356146346,
					0
				],
				[
					42.630047324668624,
					0
				],
				[
					43.653703614411484,
					0
				],
				[
					45.467417922136235,
					0
				],
				[
					46.259985005844385,
					0
				],
				[
					46.821505410055465,
					0
				],
				[
					47.61407249376356,
					0
				],
				[
					48.63772878350642,
					0
				],
				[
					50.568220963842805,
					0
				],
				[
					51.98690626257661,
					0
				],
				[
					52.49871314417919,
					0
				],
				[
					54.08138077240693,
					0
				],
				[
					54.73233448546807,
					0
				],
				[
					57.61690953981804,
					0
				],
				[
					59.0355948385519,
					0
				],
				[
					59.828161922259994,
					0
				],
				[
					62.036947765513446,
					0
				],
				[
					65.54764103488918,
					0
				],
				[
					67.36135534261399,
					0
				],
				[
					70.36019920384939,
					0
				],
				[
					72.96405658263154,
					0
				],
				[
					76.07967831647858,
					0
				],
				[
					77.89339262420333,
					0
				],
				[
					79.70714945846589,
					0
				],
				[
					81.91589277518165,
					0
				],
				[
					84.1246786184351,
					0
				],
				[
					86.3334644616886,
					0
				],
				[
					88.03286743599023,
					0
				],
				[
					89.45155273472403,
					0
				],
				[
					90.47520902446689,
					0
				],
				[
					91.49886531420981,
					0
				],
				[
					93.98836883303107,
					0
				],
				[
					95.17600745226787,
					0
				],
				[
					96.7586750804956,
					0
				],
				[
					97.55124216420376,
					0
				],
				[
					99.08670533554914,
					0
				],
				[
					100.27430142824824,
					0
				],
				[
					101.46194004748503,
					0
				],
				[
					103.27565435520984,
					0
				],
				[
					105.08936866293459,
					0
				],
				[
					107.41493237879968,
					0
				],
				[
					109.62371822205318,
					0
				],
				[
					111.83246153876894,
					0
				],
				[
					114.04124738202239,
					0
				],
				[
					117.55194065139813,
					0
				],
				[
					119.76072649465158,
					0
				],
				[
					121.57444080237639,
					0
				],
				[
					123.7832266456299,
					0
				],
				[
					125.99196996234565,
					0
				],
				[
					129.89769224071227,
					0
				],
				[
					132.89657862848543,
					0
				],
				[
					136.29049402524953,
					0
				],
				[
					138.49923734196528,
					0
				],
				[
					141.10305219420974,
					0
				],
				[
					146.19394655262482,
					0.2807176755677574
				],
				[
					149.19279041386022,
					0.2807176755677574
				],
				[
					152.19167680163338,
					0.2807176755677574
				],
				[
					154.79549165387772,
					0.539151445364098
				],
				[
					157.79433551511323,
					0.539151445364098
				],
				[
					161.70005779347986,
					1.3143251751399134
				],
				[
					164.3038726457243,
					1.3143251751399134
				],
				[
					166.90768749796877,
					1.3143251751399134
				],
				[
					169.51150235021322,
					1.3143251751399134
				],
				[
					173.4172671551176,
					1.3143251751399134
				],
				[
					175.62601047183335,
					1.3143251751399134
				],
				[
					177.43976730609592,
					1.3143251751399134
				],
				[
					179.2534816138206,
					1.3143251751399134
				],
				[
					180.72183790862522,
					1.3143251751399134
				],
				[
					182.14052320735908,
					1.3143251751399134
				],
				[
					182.93313281760487,
					1.3143251751399134
				],
				[
					183.95674658081003,
					1.3143251751399134
				],
				[
					186.05122109064035,
					1.3143251751399134
				],
				[
					187.46990638937422,
					1.3143251751399134
				],
				[
					188.26247347308237,
					1.3143251751399134
				],
				[
					189.28612976282517,
					1.3143251751399134
				],
				[
					191.61169347869026,
					1.3143251751399134
				],
				[
					192.79928957138935,
					1.3143251751399134
				],
				[
					193.36080997560038,
					1.3143251751399134
				],
				[
					193.641570177706,
					1.3143251751399134
				],
				[
					194.20309058191702,
					1.3143251751399134
				],
				[
					194.62048854975495,
					1.3143251751399134
				],
				[
					195.13229543135748,
					1.3143251751399134
				],
				[
					195.6938158355686,
					1.3143251751399134
				],
				[
					195.97457603767413,
					1.3143251751399134
				],
				[
					196.2528271740535,
					1.3143251751399134
				],
				[
					196.2528271740535,
					1.3143251751399134
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				196.2528271740535,
				1.3143251751399134
			]
		},
		{
			"id": "pfAJMPXwxrV3LWxlh6abK",
			"type": "freedraw",
			"x": 328.18201997391543,
			"y": -275.2777707365567,
			"width": 36.00373232144591,
			"height": 0.5217580914318205,
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
			"seed": 1486143671,
			"version": 26,
			"versionNonce": 116444055,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710827914312,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.9317139151666538,
					0
				],
				[
					3.535528767411108,
					-0.5217580914318205
				],
				[
					6.651150501258144,
					-0.5217580914318205
				],
				[
					9.649994362493544,
					-0.5217580914318205
				],
				[
					11.858780205746996,
					-0.5217580914318205
				],
				[
					13.55822570658637,
					-0.5217580914318205
				],
				[
					14.11974611079745,
					-0.5217580914318205
				],
				[
					15.143359874002556,
					-0.5217580914318205
				],
				[
					17.352145717256064,
					-0.5217580914318205
				],
				[
					19.560931560509573,
					-0.5217580914318205
				],
				[
					23.8616828478672,
					-0.5217580914318205
				],
				[
					26.070468691120652,
					-0.5217580914318205
				],
				[
					27.258064783819748,
					-0.5217580914318205
				],
				[
					27.769914191960027,
					-0.5217580914318205
				],
				[
					29.096657116117626,
					-0.5217580914318205
				],
				[
					30.003535533248908,
					-0.5217580914318205
				],
				[
					33.90925781161559,
					-0.5217580914318205
				],
				[
					35.72297211934034,
					-0.5217580914318205
				],
				[
					36.00373232144591,
					-0.5217580914318205
				],
				[
					36.00373232144591,
					-0.5217580914318205
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				36.00373232144591,
				-0.5217580914318205
			]
		},
		{
			"id": "ks7tEA5LbczbR-08i7SJc",
			"type": "freedraw",
			"x": 399.82426671076627,
			"y": -271.47139045033157,
			"width": 89.33728392783866,
			"height": 0.2583912432585862,
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
			"seed": 1845443959,
			"version": 45,
			"versionNonce": 906272089,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710827914312,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5118068816025811,
					0
				],
				[
					1.0236562897428598,
					0
				],
				[
					3.6274711419873142,
					0
				],
				[
					5.441185449712123,
					0
				],
				[
					7.76674916557721,
					0
				],
				[
					8.790362928782315,
					0
				],
				[
					10.604119763044878,
					0
				],
				[
					12.022805061778683,
					0
				],
				[
					14.231548378494438,
					0
				],
				[
					17.34721263887917,
					0
				],
				[
					19.951027491123625,
					0
				],
				[
					21.764741798848434,
					0
				],
				[
					24.36855665109283,
					0
				],
				[
					27.879249920468567,
					0
				],
				[
					30.088035763722075,
					0
				],
				[
					32.29677908043783,
					0
				],
				[
					34.50556492369128,
					0
				],
				[
					37.50440878492674,
					0
				],
				[
					41.41013106329336,
					0
				],
				[
					44.40901745106652,
					0
				],
				[
					47.40786131230192,
					0
				],
				[
					49.22161814656448,
					0
				],
				[
					52.61553354332858,
					0
				],
				[
					57.3113138396771,
					0
				],
				[
					60.31020022745025,
					0
				],
				[
					62.91401507969471,
					0
				],
				[
					65.12280092294822,
					0
				],
				[
					67.33154423966397,
					0
				],
				[
					71.2372665180306,
					0
				],
				[
					73.8411238968128,
					0
				],
				[
					77.23499676703915,
					0
				],
				[
					80.62891216380325,
					0
				],
				[
					83.51348721815333,
					0
				],
				[
					84.07500762236435,
					0
				],
				[
					84.8675747060725,
					0
				],
				[
					86.45024233430019,
					0
				],
				[
					88.5447168441305,
					0.2583912432585862
				],
				[
					89.33728392783866,
					0.2583912432585862
				],
				[
					89.33728392783866,
					0.2583912432585862
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				89.33728392783866,
				0.2583912432585862
			]
		},
		{
			"id": "IxrZl5wC1uqOTGlFqkvPf",
			"type": "freedraw",
			"x": 419.6162874773106,
			"y": -276.98963398641376,
			"width": 27.846929751792345,
			"height": 16.39810536978024,
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
			"seed": 2110538391,
			"version": 74,
			"versionNonce": 1103499735,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710827914312,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.5652742742954615,
					0.45222720224029445
				],
				[
					-2.4746192306151897,
					0.9044118779428345
				],
				[
					-3.2722044457756283,
					1.2447942859483874
				],
				[
					-5.090894358415028,
					1.672143463615555
				],
				[
					-6.141852685381764,
					2.263474970776656
				],
				[
					-6.849962065154443,
					2.822486309261535
				],
				[
					-7.27480217709541,
					3.1007374456409025
				],
				[
					-7.841298186221138,
					3.2398842770994634
				],
				[
					-9.264959089869592,
					3.2398842770994634
				],
				[
					-10.345728519786292,
					3.2398842770994634
				],
				[
					-12.559447441416637,
					3.2398842770994634
				],
				[
					-15.16823789857574,
					3.2398842770994634
				],
				[
					-17.777028355734785,
					3.2398842770994634
				],
				[
					-19.990789803902885,
					3.2398842770994634
				],
				[
					-22.204508725533287,
					3.2398842770994634
				],
				[
					-22.346164622717993,
					3.2398842770994634
				],
				[
					-22.80081583760898,
					2.4423415884767223
				],
				[
					-23.367311846734708,
					1.8758455793509938
				],
				[
					-23.73750535769028,
					0.683273881737307
				],
				[
					-24.661734602216086,
					-0.9043693514050801
				],
				[
					-25.086617240694807,
					-1.7540921018247673
				],
				[
					-25.315197381003372,
					-2.6634370581444387
				],
				[
					-25.45681075165038,
					-3.2298905407324128
				],
				[
					-25.45681075165038,
					-4.027433229355154
				],
				[
					-25.45681075165038,
					-4.5939292384808255
				],
				[
					-25.45681075165038,
					-6.069770203926225
				],
				[
					-25.45681075165038,
					-7.120728530892961
				],
				[
					-25.31766392019182,
					-7.687224540018633
				],
				[
					-24.977281512186266,
					-8.201497960809661
				],
				[
					-24.358647967801346,
					-9.140654020079353
				],
				[
					-24.219501136342842,
					-9.423923287911066
				],
				[
					-23.367311846734708,
					-10.281088182433848
				],
				[
					-22.94740481317058,
					-10.564314923727807
				],
				[
					-22.296451100109493,
					-11.048819768106569
				],
				[
					-20.99207713479882,
					-11.704749086082302
				],
				[
					-19.55102287721803,
					-11.965606868529335
				],
				[
					-18.900069164156946,
					-12.137031342126363
				],
				[
					-18.480162130592873,
					-12.420300609958076
				],
				[
					-18.201910994213506,
					-12.420300609958076
				],
				[
					-17.409343910505413,
					-12.561913980605027
				],
				[
					-16.22170529126862,
					-13.016565195496014
				],
				[
					-15.42913820756047,
					-13.016565195496014
				],
				[
					-15.009231173996398,
					-13.158221092680776
				],
				[
					-14.58936666697008,
					-13.158221092680776
				],
				[
					-14.077517258829744,
					-13.158221092680776
				],
				[
					-13.14580334366309,
					-13.158221092680776
				],
				[
					-12.238967453069563,
					-13.158221092680776
				],
				[
					-9.749421407710543,
					-13.158221092680776
				],
				[
					-8.561825315011504,
					-13.158221092680776
				],
				[
					-6.748068480748998,
					-12.817838684675223
				],
				[
					-5.955501397040848,
					-12.648880750266642
				],
				[
					-5.393980992829825,
					-12.509733918808081
				],
				[
					-4.320653707016163,
					-12.231482782428714
				],
				[
					-4.1815494020953565,
					-12.231482782428714
				],
				[
					-3.900789199989788,
					-12.09233595097021
				],
				[
					-3.761642368531284,
					-11.953189119511649
				],
				[
					-2.519357148309041,
					-10.991664101394974
				],
				[
					-1.3317610556100021,
					-10.400332594233873
				],
				[
					0.22109546966777316,
					-9.01894306909088
				],
				[
					1.4087340889045663,
					-8.285998191282829
				],
				[
					1.6869852252839337,
					-7.866091157718699
				],
				[
					1.8261320567424377,
					-7.30707981923382
				],
				[
					1.9950899911510191,
					-5.8883945205000146
				],
				[
					2.2211610657334404,
					-4.700755901263221
				],
				[
					2.390119000141965,
					-3.7690419860965676
				],
				[
					2.390119000141965,
					-3.1180882730354256
				],
				[
					2.390119000141965,
					-2.6982237660091073
				],
				[
					2.390119000141965,
					-2.278316732444978
				],
				[
					2.390119000141965,
					-0.9515738082873781
				],
				[
					2.390119000141965,
					-0.9515738082873781
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				2.390119000141965,
				-0.9515738082873781
			]
		},
		{
			"id": "Y1J-yC0xBQ5yO31EjMbBD",
			"type": "freedraw",
			"x": 568.175517532042,
			"y": -242.5131146879932,
			"width": 8.19158927751812,
			"height": 20.947296690567157,
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
			"seed": 1632682903,
			"version": 33,
			"versionNonce": 851303193,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710827914312,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.1391043049208065
				],
				[
					0,
					0.27825113637931054
				],
				[
					0.7925670837080361,
					0.6186335443849202
				],
				[
					1.2124741172721087,
					0.8969272073019852
				],
				[
					3.6423554301934473,
					4.037384439184393
				],
				[
					4.06226246375752,
					4.598904843395474
				],
				[
					4.201409295216081,
					4.877155979774841
				],
				[
					5.393980992829711,
					5.898345730329254
				],
				[
					6.735650731731198,
					7.500873251677774
				],
				[
					7.215179971195312,
					8.15182696473886
				],
				[
					7.493431107574679,
					8.430078101118227
				],
				[
					7.493431107574679,
					8.569224932576788
				],
				[
					7.7716822439540465,
					8.98913196614086
				],
				[
					8.052442446059558,
					9.269892168246429
				],
				[
					8.052442446059558,
					9.54814330462574
				],
				[
					8.19158927751812,
					9.968050338189869
				],
				[
					8.19158927751812,
					10.760617421897962
				],
				[
					8.19158927751812,
					11.322137826109042
				],
				[
					8.19158927751812,
					13.416612335939362
				],
				[
					7.565471062492406,
					14.835297634673168
				],
				[
					6.439963714881742,
					16.649011942397976
				],
				[
					5.247392017268112,
					18.743486452228296
				],
				[
					4.904500543536415,
					19.767142741971156
				],
				[
					4.390227122745387,
					20.10752514997671
				],
				[
					4.248613752098322,
					20.388285352082278
				],
				[
					4.106957854913617,
					20.527432183540782
				],
				[
					3.965344484266666,
					20.666536488461645
				],
				[
					3.965344484266666,
					20.947296690567157
				],
				[
					3.965344484266666,
					20.947296690567157
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				3.965344484266666,
				20.947296690567157
			]
		},
		{
			"id": "J2ahmtxq8ipuV-audRjzX",
			"type": "freedraw",
			"x": 314.5691051398059,
			"y": -198.72030676866092,
			"width": 130.55366408522576,
			"height": 2.571537210105987,
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
			"seed": 908889719,
			"version": 102,
			"versionNonce": 1156824823,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710827914312,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.5118068816025811,
					0
				],
				[
					1.5851341674162427,
					0.34038240800555286
				],
				[
					2.236087880477328,
					0.34038240800555286
				],
				[
					4.049844714739891,
					0.34038240800555286
				],
				[
					5.095827436791922,
					0.34038240800555286
				],
				[
					5.796494672461563,
					0.34038240800555286
				],
				[
					6.447448385522648,
					0.34038240800555286
				],
				[
					7.09840209858379,
					0.47952923946411374
				],
				[
					7.890969182291883,
					0.47952923946411374
				],
				[
					8.683536265999976,
					0.47952923946411374
				],
				[
					10.010279190157576,
					0.7056428405842325
				],
				[
					10.430186223721705,
					0.7056428405842325
				],
				[
					10.850050730748023,
					0.7056428405842325
				],
				[
					11.411571134959104,
					0.844747145505039
				],
				[
					12.599209754195897,
					0.844747145505039
				],
				[
					14.134672925541338,
					1.0137050799136205
				],
				[
					15.553358224275144,
					1.0137050799136205
				],
				[
					16.74095431697424,
					1.0137050799136205
				],
				[
					17.928592936211032,
					1.2398186810337393
				],
				[
					18.721160019919125,
					1.2398186810337393
				],
				[
					20.139845318652988,
					1.4658897556161605
				],
				[
					21.18582804070502,
					1.4658897556161605
				],
				[
					22.20948433044788,
					1.4658897556161605
				],
				[
					23.23309809365304,
					1.4658897556161605
				],
				[
					25.558661809518128,
					1.4658897556161605
				],
				[
					27.372376117242936,
					1.4658897556161605
				],
				[
					29.350115280999375,
					1.4658897556161605
				],
				[
					30.76880057973318,
					1.4658897556161605
				],
				[
					32.073174545043855,
					1.4658897556161605
				],
				[
					32.634694949254936,
					1.4658897556161605
				],
				[
					33.65830871246004,
					1.4658897556161605
				],
				[
					35.472065546722604,
					1.4658897556161605
				],
				[
					36.89075084545641,
					1.4658897556161605
				],
				[
					39.38025436427773,
					1.4658897556161605
				],
				[
					41.589040207531184,
					1.4658897556161605
				],
				[
					43.40275451525599,
					1.4658897556161605
				],
				[
					45.2165113495185,
					1.4658897556161605
				],
				[
					46.635196648252304,
					1.4658897556161605
				],
				[
					47.93957061356298,
					1.4658897556161605
				],
				[
					48.73213769727113,
					1.4658897556161605
				],
				[
					50.94092354052458,
					1.4658897556161605
				],
				[
					52.871415720860966,
					1.4658897556161605
				],
				[
					54.685130028585775,
					1.4658897556161605
				],
				[
					56.893915871839226,
					1.4658897556161605
				],
				[
					59.102701715092735,
					1.4658897556161605
				],
				[
					60.12631547829784,
					1.4658897556161605
				],
				[
					62.220832514665915,
					1.4658897556161605
				],
				[
					63.24444627787108,
					1.4658897556161605
				],
				[
					64.43208489710787,
					1.4658897556161605
				],
				[
					65.22465198081596,
					1.4658897556161605
				],
				[
					67.945244705672,
					1.4658897556161605
				],
				[
					70.1540305489255,
					1.4658897556161605
				],
				[
					72.36277386564126,
					1.4658897556161605
				],
				[
					73.78145916437506,
					1.4658897556161605
				],
				[
					75.59521599863757,
					1.4658897556161605
				],
				[
					77.52570817897401,
					1.4658897556161605
				],
				[
					79.10837580720175,
					1.4658897556161605
				],
				[
					80.52706110593556,
					1.4658897556161605
				],
				[
					82.34077541366037,
					1.7242809988747467
				],
				[
					83.75946071239417,
					1.7242809988747467
				],
				[
					85.06383467770485,
					1.7242809988747467
				],
				[
					86.48251997643871,
					1.7242809988747467
				],
				[
					87.6701585956755,
					1.7242809988747467
				],
				[
					88.4627256793836,
					1.7242809988747467
				],
				[
					91.18331840423963,
					1.7242809988747467
				],
				[
					93.39210424749314,
					1.7242809988747467
				],
				[
					94.41571801069824,
					1.7242809988747467
				],
				[
					95.8344033094321,
					1.7242809988747467
				],
				[
					98.32394935479113,
					1.7242809988747467
				],
				[
					99.11651643849922,
					1.7242809988747467
				],
				[
					100.53520173723302,
					1.7242809988747467
				],
				[
					101.55885802697588,
					2.064705933417997
				],
				[
					102.35142511068398,
					2.064705933417997
				],
				[
					103.28313902585063,
					2.064705933417997
				],
				[
					104.30675278905579,
					2.064705933417997
				],
				[
					105.33040907879865,
					2.064705933417997
				],
				[
					107.53919492205216,
					2.064705933417997
				],
				[
					111.44491720041879,
					2.064705933417997
				],
				[
					113.42261383763753,
					2.3454236089858114
				],
				[
					114.61025245687432,
					2.571537210105987
				],
				[
					115.63386622007948,
					2.571537210105987
				],
				[
					117.05255151881329,
					2.571537210105987
				],
				[
					120.16817325266032,
					2.571537210105987
				],
				[
					122.37695909591383,
					2.571537210105987
				],
				[
					123.56459771515057,
					2.571537210105987
				],
				[
					125.37831202287538,
					2.571537210105987
				],
				[
					125.93732336136026,
					2.571537210105987
				],
				[
					126.4988437655714,
					2.571537210105987
				],
				[
					126.7796039676769,
					2.571537210105987
				],
				[
					127.34112437188793,
					2.571537210105987
				],
				[
					127.85293125349057,
					2.571537210105987
				],
				[
					128.78464516865716,
					2.571537210105987
				],
				[
					129.06289630503653,
					2.571537210105987
				],
				[
					129.4828033386006,
					2.571537210105987
				],
				[
					130.1337570516617,
					2.571537210105987
				],
				[
					130.41451725376731,
					2.571537210105987
				],
				[
					130.55366408522576,
					2.571537210105987
				],
				[
					130.55366408522576,
					2.571537210105987
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				130.55366408522576,
				2.571537210105987
			]
		},
		{
			"id": "CxziGTxY0mbhkhPL9Pwte",
			"type": "freedraw",
			"x": 51.87419752601862,
			"y": -168.9503269806355,
			"width": 9.724575278040732,
			"height": 111.49956380140418,
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
			"seed": 2055489271,
			"version": 174,
			"versionNonce": 73732089,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710827914312,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5963071120757206,
					0.7925670837080929
				],
				[
					-1.562797103472576,
					1.7540921018247673
				],
				[
					-2.777748391567627,
					3.0460908446554527
				],
				[
					-3.8436229016437835,
					4.367858163898461
				],
				[
					-4.126860274572181,
					4.648618366003973
				],
				[
					-5.06602696547634,
					5.408907807573655
				],
				[
					-5.632501711333191,
					5.970428211784679
				],
				[
					-5.774125713614609,
					6.109532516705542
				],
				[
					-6.057363086543035,
					6.387826179622607
				],
				[
					-6.48222446175285,
					6.666077316001974
				],
				[
					-6.765461834681275,
					7.085984349566047
				],
				[
					-6.907085836962693,
					7.225088654486854
				],
				[
					-7.190323209891119,
					7.505848856592422
				],
				[
					-7.190323209891119,
					7.925755890156495
				],
				[
					-7.331947212172537,
					8.487276294367575
				],
				[
					-7.473560582819545,
					9.048796698578656
				],
				[
					-8.211481065542245,
					10.236392791277694
				],
				[
					-8.382916170773683,
					11.168106706444348
				],
				[
					-8.382916170773683,
					11.58801374000842
				],
				[
					-8.382916170773683,
					12.007878247034796
				],
				[
					-8.524529541420662,
					13.19551686627159
				],
				[
					-8.524529541420662,
					14.127230781438243
				],
				[
					-8.524529541420662,
					14.639037663040824
				],
				[
					-8.524529541420662,
					15.570751578207421
				],
				[
					-8.66615354370208,
					16.1322719824185
				],
				[
					-8.66615354370208,
					17.319868075117597
				],
				[
					-8.66615354370208,
					17.881388479328677
				],
				[
					-8.66615354370208,
					19.18576244463935
				],
				[
					-8.66615354370208,
					19.978372054885142
				],
				[
					-8.66615354370208,
					20.398236561911517
				],
				[
					-8.66615354370208,
					21.47156384772518
				],
				[
					-8.66615354370208,
					22.03308425193626
				],
				[
					-8.66615354370208,
					22.825651335644352
				],
				[
					-8.66615354370208,
					23.618218419352445
				],
				[
					-8.66615354370208,
					24.805857038589238
				],
				[
					-8.66615354370208,
					25.8791843244029
				],
				[
					-8.66615354370208,
					26.44070472861398
				],
				[
					-8.66615354370208,
					27.233271812322073
				],
				[
					-8.66615354370208,
					27.65313631934839
				],
				[
					-8.66615354370208,
					28.443236863868037
				],
				[
					-8.66615354370208,
					28.72153052678516
				],
				[
					-8.66615354370208,
					29.141395033811534
				],
				[
					-8.66615354370208,
					29.79234874687262
				],
				[
					-8.66615354370208,
					30.212255780436692
				],
				[
					-8.66615354370208,
					30.77126711892157
				],
				[
					-8.66615354370208,
					31.422220831982713
				],
				[
					-8.66615354370208,
					31.702981034088225
				],
				[
					-8.66615354370208,
					32.495548117796375
				],
				[
					-8.66615354370208,
					33.14650183085746
				],
				[
					-8.66615354370208,
					33.936602375377106
				],
				[
					-8.66615354370208,
					34.217362577482675
				],
				[
					-8.66615354370208,
					34.49561371386204
				],
				[
					-8.66615354370208,
					35.42732762902864
				],
				[
					-8.66615354370208,
					35.84723466259277
				],
				[
					-8.66615354370208,
					36.63980174630086
				],
				[
					-8.66615354370208,
					37.059708779864934
				],
				[
					-8.66615354370208,
					37.62118665753826
				],
				[
					-8.66615354370208,
					38.41379626778411
				],
				[
					-8.837588648933519,
					39.48712355359777
				],
				[
					-8.837588648933519,
					39.90698806062409
				],
				[
					-8.837588648933519,
					40.93064435036695
				],
				[
					-9.009023754164957,
					41.58159806342809
				],
				[
					-9.009023754164957,
					43.000283362161895
				],
				[
					-9.009023754164957,
					44.4686396569665
				],
				[
					-9.009023754164957,
					45.261206740674595
				],
				[
					-9.150637124811965,
					46.05381635092044
				],
				[
					-9.150637124811965,
					46.985530266087096
				],
				[
					-9.150637124811965,
					47.40539477311347
				],
				[
					-9.150637124811965,
					47.96691517732455
				],
				[
					-9.150637124811965,
					48.61786889038564
				],
				[
					-9.150637124811965,
					48.896120026765004
				],
				[
					-9.150637124811965,
					49.31356052114063
				],
				[
					-9.150637124811965,
					49.96451423420177
				],
				[
					-9.150637124811965,
					50.38437874122809
				],
				[
					-9.150637124811965,
					50.66513894333366
				],
				[
					-9.150637124811965,
					51.08504597689773
				],
				[
					-9.150637124811965,
					51.78567068602962
				],
				[
					-9.150637124811965,
					52.436624399090704
				],
				[
					-9.150637124811965,
					52.856531432654776
				],
				[
					-9.150637124811965,
					53.649098516362926
				],
				[
					-9.150637124811965,
					54.72242580217653
				],
				[
					-9.150637124811965,
					56.14111110091039
				],
				[
					-9.150637124811965,
					57.5597963996442
				],
				[
					-9.150637124811965,
					58.978481698378005
				],
				[
					-9.150637124811965,
					61.072956208208325
				],
				[
					-9.150637124811965,
					61.865523291916475
				],
				[
					-9.150637124811965,
					63.28420859065028
				],
				[
					-9.150637124811965,
					64.33023383924007
				],
				[
					-9.150637124811965,
					65.12280092294822
				],
				[
					-9.150637124811965,
					66.68063305314058
				],
				[
					-9.150637124811965,
					67.86822914583962
				],
				[
					-9.150637124811965,
					68.2881361794037
				],
				[
					-9.150637124811965,
					68.56638731578306
				],
				[
					-9.150637124811965,
					69.125398654268
				],
				[
					-9.150637124811965,
					69.2645454857265
				],
				[
					-9.150637124811965,
					69.40369231718506
				],
				[
					-9.150637124811965,
					69.82359935074913
				],
				[
					-9.150637124811965,
					70.47455306381028
				],
				[
					-9.322072230043403,
					72.03234266746489
				],
				[
					-9.322072230043403,
					72.45224970102896
				],
				[
					-9.322072230043403,
					73.24481678473705
				],
				[
					-9.322072230043403,
					73.80633718894813
				],
				[
					-9.322072230043403,
					75.50578268978751
				],
				[
					-9.322072230043403,
					77.31949699751232
				],
				[
					-9.322072230043403,
					78.73818229624612
				],
				[
					-9.322072230043403,
					80.94696813949963
				],
				[
					-9.582951275759314,
					83.15571145621539
				],
				[
					-9.582951275759314,
					84.96946829047789
				],
				[
					-9.724575278040732,
					87.06394280030821
				],
				[
					-9.724575278040732,
					88.25153889300731
				],
				[
					-9.724575278040732,
					89.27519518275017
				],
				[
					-9.724575278040732,
					90.34852246856377
				],
				[
					-9.724575278040732,
					90.7684295021279
				],
				[
					-9.724575278040732,
					90.90753380704871
				],
				[
					-9.724575278040732,
					91.04668063850721
				],
				[
					-9.724575278040732,
					91.32744084061278
				],
				[
					-9.724575278040732,
					91.60569197699215
				],
				[
					-9.724575278040732,
					92.02559901055622
				],
				[
					-9.724575278040732,
					92.6765527236173
				],
				[
					-9.724575278040732,
					93.09645975718144
				],
				[
					-9.724575278040732,
					93.65547109566631
				],
				[
					-9.724575278040732,
					93.93623129777183
				],
				[
					-9.724575278040732,
					94.3561383313359
				],
				[
					-9.724575278040732,
					94.63685600690371
				],
				[
					-9.724575278040732,
					96.33630150774309
				],
				[
					-9.724575278040732,
					97.12886859145118
				],
				[
					-9.724575278040732,
					97.40962879355675
				],
				[
					-9.724575278040732,
					97.82953582712082
				],
				[
					-9.724575278040732,
					98.53016053625271
				],
				[
					-9.724575278040732,
					98.95006756981678
				],
				[
					-9.724575278040732,
					99.22831870619615
				],
				[
					-9.724575278040732,
					99.64822573976022
				],
				[
					-9.724575278040732,
					99.78737257121878
				],
				[
					-9.724575278040732,
					100.48799728035067
				],
				[
					-9.724575278040732,
					100.90790431391474
				],
				[
					-9.724575278040732,
					101.32781134747881
				],
				[
					-9.724575278040732,
					101.46691565239962
				],
				[
					-9.724575278040732,
					101.74520931531674
				],
				[
					-9.555627975266589,
					102.25701619691932
				],
				[
					-9.416491775442495,
					102.8160275354042
				],
				[
					-9.076098735802503,
					103.46698124846529
				],
				[
					-8.90715143302836,
					104.11793496152643
				],
				[
					-8.087250417193133,
					105.36022018174862
				],
				[
					-7.806490215087592,
					105.63851384466574
				],
				[
					-7.66735401526347,
					105.91676498104505
				],
				[
					-7.3890922472496925,
					106.33667201460918
				],
				[
					-7.24995604742557,
					106.61492315098849
				],
				[
					-6.971683647777354,
					106.89321681390561
				],
				[
					-6.832547447953232,
					107.17146795028498
				],
				[
					-6.693411248129138,
					107.31061478174354
				],
				[
					-6.554275048305016,
					107.59137498384905
				],
				[
					-6.415138848480893,
					107.87213518595456
				],
				[
					-5.995253078185698,
					108.29199969298094
				],
				[
					-5.856116878361576,
					108.4311465244395
				],
				[
					-5.716980678537453,
					108.570293355898
				],
				[
					-5.297084276607819,
					108.85105355800357
				],
				[
					-5.157948076783697,
					108.99015786292438
				],
				[
					-4.877198506312595,
					109.12930469438294
				],
				[
					-4.598926106664379,
					109.4075983573
				],
				[
					-4.459789906840257,
					109.54670266222081
				],
				[
					-4.181517507192041,
					109.82499632513793
				],
				[
					-4.0423813073679185,
					110.10575652724344
				],
				[
					-3.9032557391782348,
					110.24486083216425
				],
				[
					-3.7641195393541125,
					110.38400766362281
				],
				[
					-3.4833593372485723,
					110.52315449508137
				],
				[
					-3.3442231374244784,
					110.66225880000218
				],
				[
					-2.7827133648478366,
					110.94055246291924
				],
				[
					-2.6435771650237143,
					111.36045949648337
				],
				[
					-2.5044409651996205,
					111.49956380140418
				],
				[
					-2.5044409651996205,
					111.49956380140418
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				-2.5044409651996205,
				111.49956380140418
			]
		},
		{
			"id": "OP-bgTgz4O8bSfUKvu09C",
			"type": "freedraw",
			"x": -432.07573932511923,
			"y": 53.55936269941728,
			"width": 36.26960823534529,
			"height": 30.912880489568607,
			"angle": 0,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1813857913,
			"version": 60,
			"versionNonce": 741263383,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710827914312,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.1416133706469509,
					-0.1416346339158565
				],
				[
					-0.1416133706469509,
					-3.264719775134779
				],
				[
					-0.1416133706469509,
					-4.688380678783233
				],
				[
					-0.1416133706469509,
					-6.902120863682484
				],
				[
					-0.1416133706469509,
					-10.300990602092355
				],
				[
					0.4546724781598641,
					-14.489960885021873
				],
				[
					1.0509795902355563,
					-20.77340567778171
				],
				[
					1.6298720851101507,
					-24.567325688451405
				],
				[
					2.049757855405346,
					-26.550019193853615
				],
				[
					2.049757855405346,
					-27.2059272485605
				],
				[
					3.1380119559628383,
					-25.6530919865516
				],
				[
					4.673453864039402,
					-23.347409427076144
				],
				[
					6.144319224570211,
					-21.421871588385528
				],
				[
					8.23383939275476,
					-17.548448215426163
				],
				[
					11.028959874985844,
					-13.195495603002712
				],
				[
					15.687508187550236,
					-6.666077316001974
				],
				[
					18.435424212898965,
					-2.6957572268206604
				],
				[
					19.55597721886386,
					-0.8820216558270033
				],
				[
					19.695102787053486,
					-0.6037492561787587
				],
				[
					19.834249618512047,
					-0.46462368798907505
				],
				[
					19.834249618512047,
					-0.3254768565305426
				],
				[
					15.526013660513627,
					-0.3254768565305426
				],
				[
					13.70732374787417,
					-0.3254768565305426
				],
				[
					8.728252920425007,
					-1.565274274295433
				],
				[
					1.3838985908691939,
					-2.9019684082823005
				],
				[
					-5.567893268884063,
					-4.226244793251453
				],
				[
					-12.641438606163547,
					-5.143053156943097
				],
				[
					-12.924665347457562,
					-5.284666527590076
				],
				[
					-14.467591926174919,
					-5.97040694851583
				],
				[
					-15.496202557563493,
					-6.14183142211283
				],
				[
					-16.29374524618629,
					-6.454890529625715
				],
				[
					-16.43535861683324,
					-6.596503900272694
				],
				[
					-15.955829377369128,
					-7.394046588895435
				],
				[
					-12.57435299289159,
					-9.729540251320884
				],
				[
					-9.970538140647136,
					-11.033935479900435
				],
				[
					-5.786543462632267,
					-12.817859947944072
				],
				[
					2.4646892840547707,
					-15.985661743588025
				],
				[
					7.04373423432952,
					-17.819257207702464
				],
				[
					10.042599358833797,
					-19.190738049553943
				],
				[
					11.62524572379266,
					-19.85413077490162
				],
				[
					13.043931022526522,
					-20.254135388807214
				],
				[
					14.348326251106073,
					-20.59700559927009
				],
				[
					14.860154395977474,
					-20.939875809732968
				],
				[
					14.999279964167158,
					-20.939875809732968
				],
				[
					15.138426795625719,
					-20.939875809732968
				],
				[
					15.277552363815403,
					-20.659115607627427
				],
				[
					14.072541653915152,
					-18.676443365494066
				],
				[
					12.596721951738573,
					-16.75090552680345
				],
				[
					10.338243849145442,
					-13.523460261990579
				],
				[
					7.287219926113153,
					-9.553140172809265
				],
				[
					4.129348077029533,
					-4.81508849795523
				],
				[
					1.6398020316705129,
					-0.4621358855317794
				],
				[
					-0.34038240800555286,
					2.633625955194475
				],
				[
					-0.6534415155183524,
					3.426193038902568
				],
				[
					-0.795054886165417,
					3.706953241008108
				],
				[
					-0.795054886165417,
					3.706953241008108
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				-0.795054886165417,
				3.706953241008108
			]
		},
		{
			"id": "UUDABM9f",
			"type": "text",
			"x": 96.47817788931694,
			"y": 382.9515525058672,
			"width": 179.95193481445312,
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
			"seed": 324994713,
			"version": 49,
			"versionNonce": 688573241,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710827924320,
			"link": null,
			"locked": false,
			"text": "그냥 BPF를 사용해도 ㄱㅊ",
			"rawText": "그냥 BPF를 사용해도 ㄱㅊ",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 14,
			"containerId": null,
			"originalText": "그냥 BPF를 사용해도 ㄱㅊ",
			"lineHeight": 1.25
		},
		{
			"id": "JPO7ISlP_s86mLiNnw0d6",
			"type": "arrow",
			"x": -270.4577152229241,
			"y": 806.5919908174275,
			"width": 26.54753139139632,
			"height": 28.567456880582768,
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
			"roundness": {
				"type": 2
			},
			"seed": 314183929,
			"version": 14,
			"versionNonce": 735333527,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710827994373,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					26.54753139139632,
					-28.567456880582768
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": "arrow"
		},
		{
			"id": "qABMPyEUthc6HwIOmmMud",
			"type": "arrow",
			"x": -271.1707576810737,
			"y": 832.0661949230101,
			"width": 30.89051153072171,
			"height": 17.02418105826814,
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
			"roundness": {
				"type": 2
			},
			"seed": 366098679,
			"version": 19,
			"versionNonce": 995540185,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710827999389,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					30.89051153072171,
					17.02418105826814
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": "arrow"
		},
		{
			"id": "JHcRK4Sb",
			"type": "text",
			"x": 368.19755702210017,
			"y": 734.3893293663465,
			"width": 197.00791931152344,
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
			"seed": 291825175,
			"version": 110,
			"versionNonce": 2126303097,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710828194633,
			"link": null,
			"locked": false,
			"text": "잡음에 의한 영향이 훨씬 큼\n-> pilot tone이 무조건 필요",
			"rawText": "잡음에 의한 영향이 훨씬 큼\n-> pilot tone이 무조건 필요",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 34,
			"containerId": null,
			"originalText": "잡음에 의한 영향이 훨씬 큼\n-> pilot tone이 무조건 필요",
			"lineHeight": 1.25
		},
		{
			"id": "WOaAx25o",
			"type": "text",
			"x": -603.5189479816319,
			"y": 1169.2706372904097,
			"width": 77.19998168945312,
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
			"seed": 973067255,
			"version": 89,
			"versionNonce": 790937017,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710828210150,
			"link": null,
			"locked": false,
			"text": "근데 어려움",
			"rawText": "근데 어려움",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "right",
			"verticalAlign": "top",
			"baseline": 14,
			"containerId": null,
			"originalText": "근데 어려움",
			"lineHeight": 1.25
		},
		{
			"id": "3WD4rw9x5mT9a4BVaicbz",
			"type": "freedraw",
			"x": -508.0139212189288,
			"y": 1254.9465989522266,
			"width": 227.55082798932148,
			"height": 3.393915396764214,
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
			"seed": 64578425,
			"version": 109,
			"versionNonce": 1271366903,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710828219341,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.13914683145850404,
					-0.1416133706468372
				],
				[
					1.1627818579324867,
					-0.1416133706468372
				],
				[
					2.7454494861602825,
					-0.1416133706468372
				],
				[
					3.3964031992213677,
					-0.1416133706468372
				],
				[
					4.420038225695407,
					-0.1416133706468372
				],
				[
					4.698310625343595,
					-0.1416133706468372
				],
				[
					5.398956597744359,
					-0.1416133706468372
				],
				[
					5.8188423680395545,
					-0.1416133706468372
				],
				[
					6.3803415089818145,
					-0.2832692678316562
				],
				[
					6.941861913192838,
					-0.2832692678316562
				],
				[
					7.36174768348809,
					-0.2832692678316562
				],
				[
					8.062393655888854,
					-0.2832692678316562
				],
				[
					8.340666055537099,
					-0.2832692678316562
				],
				[
					8.902186459748123,
					-0.2832692678316562
				],
				[
					9.463685600690383,
					-0.2832692678316562
				],
				[
					10.648815154200975,
					-0.2832692678316562
				],
				[
					11.441403501177945,
					-0.2832692678316562
				],
				[
					12.002902642120148,
					-0.2832692678316562
				],
				[
					13.02653766859413,
					-0.2832692678316562
				],
				[
					14.725983169433505,
					-0.2832692678316562
				],
				[
					15.518550253141598,
					-0.2832692678316562
				],
				[
					16.542206542884458,
					-0.2832692678316562
				],
				[
					17.729823898852374,
					-0.2832692678316562
				],
				[
					18.753458925326413,
					-0.2832692678316562
				],
				[
					20.6839511056628,
					-0.2832692678316562
				],
				[
					22.89273694891631,
					-0.2832692678316562
				],
				[
					25.101501528900883,
					-0.05715566671142369
				],
				[
					27.705316381145337,
					0.2236045353940881
				],
				[
					29.91410222439879,
					0.4496756099763388
				],
				[
					33.424774230505705,
					0.6757892110965713
				],
				[
					34.84345952923945,
					0.6757892110965713
				],
				[
					35.86709455571349,
					0.6757892110965713
				],
				[
					36.89072958218753,
					0.6757892110965713
				],
				[
					39.38027562754655,
					1.0161716191021242
				],
				[
					40.56789298351441,
					1.2422852202223567
				],
				[
					41.47475013737687,
					1.2422852202223567
				],
				[
					43.17419563821619,
					1.2422852202223567
				],
				[
					43.874841610616954,
					1.2422852202223567
				],
				[
					44.898476637090994,
					1.2422852202223567
				],
				[
					45.69104372079903,
					1.2422852202223567
				],
				[
					46.48363206777606,
					1.4112006280931837
				],
				[
					48.29734637550081,
					1.4112006280931837
				],
				[
					50.78687115759101,
					1.669591871351713
				],
				[
					52.205556456324814,
					1.669591871351713
				],
				[
					53.62424175505862,
					1.669591871351713
				],
				[
					55.83302759831213,
					1.669591871351713
				],
				[
					57.020644954280044,
					1.8087387028101602
				],
				[
					60.13626668812708,
					2.0348523039303927
				],
				[
					61.95000225912071,
					2.0348523039303927
				],
				[
					64.55381711136516,
					2.0348523039303927
				],
				[
					67.15763196360962,
					2.0348523039303927
				],
				[
					69.4831956794747,
					2.0348523039303927
				],
				[
					71.29690998719946,
					2.293243547188922
				],
				[
					72.71559528593332,
					2.293243547188922
				],
				[
					74.529330856927,
					2.293243547188922
				],
				[
					77.24992358178304,
					2.293243547188922
				],
				[
					79.45868816176767,
					2.293243547188922
				],
				[
					81.66747400502112,
					2.293243547188922
				],
				[
					84.27128885726557,
					2.293243547188922
				],
				[
					86.08500316499033,
					2.293243547188922
				],
				[
					89.20064616210624,
					2.293243547188922
				],
				[
					92.19951128661052,
					2.293243547188922
				],
				[
					95.1983764111148,
					2.293243547188922
				],
				[
					98.19724153561907,
					2.293243547188922
				],
				[
					100.40600611560365,
					2.293243547188922
				],
				[
					103.91669938497938,
					2.5193146217714
				],
				[
					105.73041369270419,
					2.7454282228916327
				],
				[
					107.54414926369782,
					2.7454282228916327
				],
				[
					109.75291384368245,
					2.7454282228916327
				],
				[
					113.26360711305819,
					2.7454282228916327
				],
				[
					115.47237169304276,
					2.9714992974738834
				],
				[
					118.07618654528721,
					2.9714992974738834
				],
				[
					120.28497238854072,
					2.9714992974738834
				],
				[
					124.1906946669074,
					2.9714992974738834
				],
				[
					127.5846100636715,
					2.9714992974738834
				],
				[
					129.0032953624053,
					2.9714992974738834
				],
				[
					132.39718949590053,
					2.9714992974738834
				],
				[
					135.3960546204048,
					2.9714992974738834
				],
				[
					140.09187744329114,
					2.9714992974738834
				],
				[
					143.48579284005524,
					2.9714992974738834
				],
				[
					146.87968697355052,
					2.9714992974738834
				],
				[
					150.66865264257444,
					2.9714992974738834
				],
				[
					154.4575970483295,
					2.9714992974738834
				],
				[
					159.15341987121582,
					2.9714992974738834
				],
				[
					162.1522849957201,
					2.9714992974738834
				],
				[
					164.75609984796455,
					2.9714992974738834
				],
				[
					167.359914700209,
					2.9714992974738834
				],
				[
					170.3587585614444,
					2.9714992974738834
				],
				[
					174.65955237533979,
					2.9714992974738834
				],
				[
					178.0534677721039,
					2.9714992974738834
				],
				[
					181.447383168868,
					2.9714992974738834
				],
				[
					184.84125603909433,
					2.9714992974738834
				],
				[
					189.53707886198066,
					2.9714992974738834
				],
				[
					192.93099425874476,
					2.9714992974738834
				],
				[
					196.71993866449986,
					2.9714992974738834
				],
				[
					200.11385406126396,
					2.9714992974738834
				],
				[
					205.20470589314124,
					2.9714992974738834
				],
				[
					208.99369282543404,
					2.9714992974738834
				],
				[
					210.6906292605472,
					2.9714992974738834
				],
				[
					215.78148109242454,
					2.9714992974738834
				],
				[
					218.50207381728057,
					2.9714992974738834
				],
				[
					220.9916198626396,
					2.9714992974738834
				],
				[
					223.20036317935535,
					2.9714992974738834
				],
				[
					225.1781023431118,
					2.9714992974738834
				],
				[
					226.9918166508366,
					2.9714992974738834
				],
				[
					227.55082798932148,
					3.110646128932558
				],
				[
					227.55082798932148,
					3.110646128932558
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				227.55082798932148,
				3.110646128932558
			]
		},
		{
			"id": "ZDjuN5VhO4DnVj5gvAZWz",
			"type": "freedraw",
			"x": -174.72950075206558,
			"y": -1605.1351911411946,
			"width": 33.73261470310973,
			"height": 31.318655837218103,
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
			"seed": 1325414137,
			"version": 69,
			"versionNonce": 193159735,
			"isDeleted": true,
			"boundElements": null,
			"updated": 1710827914311,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-2.0646180007937005,
					1.3028570899371061
				],
				[
					-5.46887054682054,
					3.4042525460267825
				],
				[
					-8.644590323568934,
					4.273693170127899
				],
				[
					-10.98503923908288,
					5.337541760855174
				],
				[
					-13.743123585214107,
					6.1728126220893955
				],
				[
					-16.627276372237816,
					6.889928040147879
				],
				[
					-18.967680327537494,
					7.402159761648818
				],
				[
					-20.890493812434215,
					7.880221720283089
				],
				[
					-23.230897767733893,
					7.880221720283089
				],
				[
					-25.98898211386512,
					7.880221720283089
				],
				[
					-29.708450722337545,
					7.880221720283089
				],
				[
					-30.007885749564423,
					7.880221720283089
				],
				[
					-30.15764822339213,
					7.880221720283089
				],
				[
					-30.307365737005625,
					7.880221720283089
				],
				[
					-30.85106960851533,
					7.880221720283089
				],
				[
					-31.213583816402775,
					7.1867553749455055
				],
				[
					-32.55321836163591,
					4.964551823036118
				],
				[
					-33.010283900192746,
					3.0417383381393392
				],
				[
					-33.49095355125621,
					0.7013343828396046
				],
				[
					-33.73261470310973,
					-1.6391145326742844
				],
				[
					-33.73261470310973,
					-5.35858314114671
				],
				[
					-33.73261470310973,
					-7.698987096446444
				],
				[
					-33.73261470310973,
					-11.292387264026274
				],
				[
					-33.45943644103306,
					-13.632836179540163
				],
				[
					-32.76862274833917,
					-16.516988966563986
				],
				[
					-31.859752016298387,
					-18.439757491246382
				],
				[
					-30.738129550197925,
					-20.118257171646064
				],
				[
					-30.14447488060273,
					-20.71712722609982
				],
				[
					-28.98085957434762,
					-22.038418003899324
				],
				[
					-28.142936060469594,
					-22.369370141349236
				],
				[
					-26.225382920645757,
					-22.611031293202814
				],
				[
					-24.552143585319016,
					-22.886817247708677
				],
				[
					-22.634635405709446,
					-23.438434116935014
				],
				[
					-21.1347626567171,
					-23.438434116935014
				],
				[
					-18.258477907195584,
					-23.438434116935014
				],
				[
					-17.176240588820406,
					-23.438434116935014
				],
				[
					-15.652763727321428,
					-23.01819099388854
				],
				[
					-15.355936392523859,
					-23.01819099388854
				],
				[
					-14.27369907414868,
					-22.479702507237334
				],
				[
					-13.11008376789357,
					-21.316042240767956
				],
				[
					-12.272115293801278,
					-20.659353350726406
				],
				[
					-11.300255301528523,
					-19.411662443733576
				],
				[
					-10.856318145546766,
					-18.82061546656746
				],
				[
					-10.438682714929541,
					-17.320742717575285
				],
				[
					-10.052519434321198,
					-16.06518377307998
				],
				[
					-9.230376955661882,
					-13.312359772021637
				],
				[
					-8.502740847457687,
					-10.853710453117401
				],
				[
					-8.229562585381018,
					-8.936202273507888
				],
				[
					-7.9563843233043485,
					-7.26296293818109
				],
				[
					-7.9563843233043485,
					-6.180725619806026
				],
				[
					-7.420548489296834,
					-2.051489618218511
				],
				[
					-7.147370227220165,
					0.7013343828396046
				],
				[
					-7.147370227220165,
					1.9568933273349103
				],
				[
					-7.147370227220165,
					3.4567660763273125
				],
				[
					-7.000260406036034,
					4.050420745922338
				],
				[
					-7.000260406036034,
					4.050420745922338
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				-7.000260406036034,
				4.050420745922338
			]
		},
		{
			"id": "czX_BT0w1ubku6n-0N5Ek",
			"type": "freedraw",
			"x": -200.97073776827818,
			"y": -842.7255493524401,
			"width": 74.86482643565324,
			"height": 59.54566749842547,
			"angle": 0,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 270251769,
			"version": 62,
			"versionNonce": 1976020249,
			"isDeleted": true,
			"boundElements": null,
			"updated": 1710827914311,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.59891501466808,
					0.14710982118413085
				],
				[
					-1.0480675555083963,
					0.14710982118413085
				],
				[
					-1.6469825701764762,
					0.14710982118413085
				],
				[
					-3.330697635434717,
					-0.5752434618400457
				],
				[
					-4.804313619276854,
					-3.4515282113616195
				],
				[
					-5.615980368004671,
					-8.423970552007063
				],
				[
					-5.954845503171157,
					-14.523273223718775
				],
				[
					-5.954845503171157,
					-20.62255341532341
				],
				[
					-5.954845503171157,
					-26.72185608703512
				],
				[
					-3.9138765750984135,
					-36.288468005327104
				],
				[
					-1.2871210149326657,
					-41.224110410569324
				],
				[
					1.8702549943820372,
					-44.70454803972473
				],
				[
					4.6230789954403235,
					-46.359398647403395
				],
				[
					8.628854248564494,
					-47.276137416946426
				],
				[
					16.51694400634966,
					-46.2727153542362
				],
				[
					22.73970742652466,
					-42.45080489748511
				],
				[
					29.185743270905107,
					-36.71925429862654
				],
				[
					34.16081578408705,
					-29.960632564336947
				],
				[
					38.3215688958976,
					-19.92121903248369
				],
				[
					39.31181761581837,
					-14.662470047186389
				],
				[
					39.60864495061594,
					-11.074352704786634
				],
				[
					39.60864495061594,
					-10.630438028911954
				],
				[
					37.685876425933486,
					-10.270553993560952
				],
				[
					33.54877238684384,
					-10.270553993560952
				],
				[
					26.19912615549549,
					-10.987669411619436
				],
				[
					16.346230072658898,
					-13.913859999012061
				],
				[
					5.151046791945646,
					-19.143699566515465
				],
				[
					-14.23431392642334,
					-30.16814643343082
				],
				[
					-24.71768709436543,
					-37.28136937789145
				],
				[
					-31.484154386050136,
					-42.61365079367363
				],
				[
					-34.35783144314229,
					-46.38565541255366
				],
				[
					-35.2561814850373,
					-51.77573318381633
				],
				[
					-34.158163131443416,
					-54.533817529947555
				],
				[
					-30.362531919949618,
					-57.04761055168865
				],
				[
					-24.686125023928014,
					-58.7129818495132
				],
				[
					-18.17444726667196,
					-59.39855767724134
				],
				[
					-7.780410044540645,
					-59.39855767724134
				],
				[
					-0.4360691184795087,
					-59.39855767724134
				],
				[
					5.658018168373644,
					-59.39855767724134
				],
				[
					6.251627877754515,
					-58.954643001366776
				],
				[
					6.763859599255397,
					-56.61945443092566
				],
				[
					6.763859599255397,
					-54.28428834059173
				],
				[
					6.763859599255397,
					-48.90207860683131
				],
				[
					6.409258389084471,
					-41.97535063128021
				],
				[
					3.9138316148841454,
					-33.798301576199606
				],
				[
					-2.9813567703366743,
					-20.740776298820833
				],
				[
					-7.993206738814649,
					-13.575017343952595
				],
				[
					-12.39562100247872,
					-8.831107772585597
				],
				[
					-12.545338516092215,
					-8.684020431508543
				],
				[
					-12.545338516092215,
					-8.684020431508543
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				-12.545338516092215,
				-8.684020431508543
			]
		},
		{
			"id": "rVXyqMWJNQcYaCqh0aaZb",
			"type": "freedraw",
			"x": 123.57936728030741,
			"y": -494.88093316405786,
			"width": 11.428171553015716,
			"height": 6.8117619690953575,
			"angle": 0,
			"strokeColor": "#2f9e44",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 717618071,
			"version": 29,
			"versionNonce": 355030551,
			"isDeleted": true,
			"boundElements": null,
			"updated": 1710827914311,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.11917765267055813,
					0.47252360209063227
				],
				[
					-0.11917765267055813,
					1.139474705707869
				],
				[
					-0.11917765267055813,
					1.687257103254126
				],
				[
					-0.11917765267055813,
					2.784933295841597
				],
				[
					-0.11917765267055813,
					3.257421111533972
				],
				[
					-0.11917765267055813,
					4.256827854610606
				],
				[
					-0.11917765267055813,
					4.729351456701238
				],
				[
					-0.11917765267055813,
					5.632564361363791
				],
				[
					-0.11917765267055813,
					5.985883470985129
				],
				[
					-0.11917765267055813,
					6.458407073075762
				],
				[
					-0.11917765267055813,
					6.694668874121021
				],
				[
					0.547782397546257,
					6.8117619690953575
				],
				[
					2.738911987731285,
					6.8117619690953575
				],
				[
					5.5949081238373,
					6.8117619690953575
				],
				[
					7.121180114700891,
					6.8117619690953575
				],
				[
					11.07273209929987,
					6.8117619690953575
				],
				[
					11.308993900345158,
					6.8117619690953575
				],
				[
					11.308993900345158,
					6.8117619690953575
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				11.308993900345158,
				6.8117619690953575
			]
		},
		{
			"id": "p45Ko5-RhfFOxQV9hGn60",
			"type": "freedraw",
			"x": -599.4943010873044,
			"y": -422.3582225706703,
			"width": 0.0001,
			"height": 0.0001,
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
			"seed": 1818213433,
			"version": 11,
			"versionNonce": 520308313,
			"isDeleted": true,
			"boundElements": null,
			"updated": 1710827914312,
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
			"id": "w9a_S-tujBhPpsDOYh6oA",
			"type": "freedraw",
			"x": -599.4943010873044,
			"y": -422.3582225706703,
			"width": 0.0001,
			"height": 0.0001,
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
			"seed": 166599385,
			"version": 10,
			"versionNonce": 981313463,
			"isDeleted": true,
			"boundElements": null,
			"updated": 1710827914312,
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
			"id": "it-pTjipE4WqxbTmsY7qQ",
			"type": "freedraw",
			"x": -468.97391105141,
			"y": -221.2683873925297,
			"width": 98.8108994750894,
			"height": 0.8000092278111879,
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
			"seed": 1894777079,
			"version": 82,
			"versionNonce": 149308441,
			"isDeleted": true,
			"boundElements": null,
			"updated": 1710827914312,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.1391255681896837,
					0
				],
				[
					0.9316926518977766,
					0
				],
				[
					2.1193312711345698,
					0
				],
				[
					4.049823451470957,
					0
				],
				[
					4.842390535179106,
					0
				],
				[
					5.63497888215602,
					-0.17142447359697144
				],
				[
					5.915717820992711,
					-0.17142447359697144
				],
				[
					6.708306167969681,
					-0.17142447359697144
				],
				[
					7.269805308911884,
					-0.17142447359697144
				],
				[
					8.805268480257325,
					-0.3428489471939997
				],
				[
					10.619004051250954,
					-0.5714290875025654
				],
				[
					11.411571134959104,
					-0.5714290875025654
				],
				[
					13.111016635798478,
					-0.5714290875025654
				],
				[
					13.672515776740624,
					-0.5714290875025654
				],
				[
					14.09240154703582,
					-0.5714290875025654
				],
				[
					14.370673946684065,
					-0.5714290875025654
				],
				[
					14.790580980248137,
					-0.5714290875025654
				],
				[
					16.743442119431506,
					-0.8000092278111879
				],
				[
					18.557156427156315,
					-0.8000092278111879
				],
				[
					19.580812716899175,
					-0.8000092278111879
				],
				[
					21.394527024623926,
					-0.8000092278111879
				],
				[
					23.0939725254633,
					-0.8000092278111879
				],
				[
					23.744926238524442,
					-0.8000092278111879
				],
				[
					24.025686440629954,
					-0.8000092278111879
				],
				[
					25.21330379659787,
					-0.8000092278111879
				],
				[
					26.23693882307191,
					-0.8000092278111879
				],
				[
					29.121513877421876,
					-0.8000092278111879
				],
				[
					30.54019917615568,
					-0.8000092278111879
				],
				[
					31.958884474889544,
					-0.8000092278111879
				],
				[
					33.37756977362335,
					-0.8000092278111879
				],
				[
					35.47204428345367,
					-0.8000092278111879
				],
				[
					36.26461136716176,
					-0.8000092278111879
				],
				[
					38.07834693815545,
					-0.8000092278111879
				],
				[
					39.89208250914908,
					-0.8000092278111879
				],
				[
					41.07969986511705,
					-0.8000092278111879
				],
				[
					43.683514717361504,
					-0.8000092278111879
				],
				[
					45.61400689769789,
					-0.8000092278111879
				],
				[
					47.82279274095134,
					-0.8000092278111879
				],
				[
					49.63650704867615,
					-0.8000092278111879
				],
				[
					51.8452928919296,
					-0.8000092278111879
				],
				[
					53.032910247897576,
					-0.8000092278111879
				],
				[
					55.358452700493785,
					-0.8000092278111879
				],
				[
					56.77713799922759,
					-0.8000092278111879
				],
				[
					58.35980562745539,
					-0.8000092278111879
				],
				[
					59.43313291326899,
					-0.8000092278111879
				],
				[
					60.45676793974303,
					-0.8000092278111879
				],
				[
					63.06058279198743,
					-0.8000092278111879
				],
				[
					66.0594479164917,
					-0.8000092278111879
				],
				[
					70.75527073937803,
					-0.8000092278111879
				],
				[
					72.96403531936267,
					-0.8000092278111879
				],
				[
					74.77777089035635,
					-0.8000092278111879
				],
				[
					76.59150646134998,
					-0.8000092278111879
				],
				[
					78.80027104133461,
					-0.8000092278111879
				],
				[
					81.52086376619064,
					-0.8000092278111879
				],
				[
					83.33459933718433,
					-0.8000092278111879
				],
				[
					85.5433639171689,
					-0.8000092278111879
				],
				[
					87.35709948816259,
					-0.8000092278111879
				],
				[
					89.45157399799291,
					-0.8000092278111879
				],
				[
					90.244141081701,
					-0.8000092278111879
				],
				[
					91.0367081654091,
					-0.8000092278111879
				],
				[
					91.45661519897322,
					-0.8000092278111879
				],
				[
					92.10756891203431,
					-0.8000092278111879
				],
				[
					92.38586257495143,
					-0.8000092278111879
				],
				[
					92.66411371133074,
					-0.8000092278111879
				],
				[
					93.22563411554182,
					-0.8000092278111879
				],
				[
					94.01820119924997,
					-0.8000092278111879
				],
				[
					95.88162902958322,
					-0.8000092278111879
				],
				[
					96.02073333450403,
					-0.8000092278111879
				],
				[
					96.3014935366096,
					-0.8000092278111879
				],
				[
					96.95244724967068,
					-0.8000092278111879
				],
				[
					97.97610353941354,
					-0.8000092278111879
				],
				[
					98.25435467579291,
					-0.8000092278111879
				],
				[
					98.6717951701686,
					-0.8000092278111879
				],
				[
					98.8108994750894,
					-0.8000092278111879
				],
				[
					98.8108994750894,
					-0.8000092278111879
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				98.8108994750894,
				-0.8000092278111879
			]
		},
		{
			"id": "i2rdYj47j7csm73zrCjir",
			"type": "freedraw",
			"x": -466.4421574173522,
			"y": -220.56274455194546,
			"width": 95.18842520128555,
			"height": 3.277137524152522,
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
			"seed": 1844917593,
			"version": 81,
			"versionNonce": 312632823,
			"isDeleted": true,
			"boundElements": null,
			"updated": 1710827914312,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.2807602021055118,
					0
				],
				[
					1.1876173559679728,
					-0.45469374142868446
				],
				[
					4.303260353083829,
					-0.45469374142868446
				],
				[
					5.721945651817634,
					-0.6261182150257127
				],
				[
					7.535681222811263,
					-0.6261182150257127
				],
				[
					9.23510546038176,
					-0.7975426886226842
				],
				[
					10.027693807358787,
					-0.9391985858074463
				],
				[
					10.820260891066823,
					-0.9391985858074463
				],
				[
					11.612827974774973,
					-0.9391985858074463
				],
				[
					14.333420699631006,
					-1.167778726116012
				],
				[
					16.93723555187546,
					-1.167778726116012
				],
				[
					18.355920850609266,
					-1.167778726116012
				],
				[
					18.917441254820346,
					-1.167778726116012
				],
				[
					19.05656682301003,
					-1.167778726116012
				],
				[
					19.334839222658275,
					-1.167778726116012
				],
				[
					19.98579293571936,
					-1.167778726116012
				],
				[
					21.031796921040325,
					-1.167778726116012
				],
				[
					21.45168269133552,
					-1.167778726116012
				],
				[
					23.151128192174895,
					-1.167778726116012
				],
				[
					23.712627333117098,
					-1.167778726116012
				],
				[
					24.13253436668117,
					-1.167778726116012
				],
				[
					24.410806766329415,
					-1.167778726116012
				],
				[
					24.97230590727162,
					-1.167778726116012
				],
				[
					25.904019822438272,
					-0.9988207917074305
				],
				[
					27.345052816750183,
					-0.9988207917074305
				],
				[
					28.137641163727153,
					-0.9988207917074305
				],
				[
					29.95135547145196,
					-0.7727071905873117
				],
				[
					31.5340230996797,
					-0.2534581648816925
				],
				[
					33.464536543284964,
					-0.2534581648816925
				],
				[
					34.48817156975895,
					-0.08450023047311106
				],
				[
					35.67578892572686,
					-0.08450023047311106
				],
				[
					37.23359979265041,
					0.14161337064700774
				],
				[
					38.25725608239327,
					0.14161337064700774
				],
				[
					39.30323880444536,
					0.367684445229429
				],
				[
					40.49085616041327,
					0.506831276687933
				],
				[
					41.678494779650066,
					0.506831276687933
				],
				[
					44.16801956174021,
					0.7329448778081087
				],
				[
					44.81897327480135,
					0.7329448778081087
				],
				[
					46.6326875825261,
					0.9590159523904731
				],
				[
					47.65634387226896,
					1.1279738867990545
				],
				[
					49.47005817999377,
					1.1279738867990545
				],
				[
					51.959582962083914,
					1.6919608301985818
				],
				[
					52.752171309060884,
					1.6919608301985818
				],
				[
					53.17205707935614,
					1.8311076616571427
				],
				[
					53.45281728146165,
					1.8311076616571427
				],
				[
					54.615577876125315,
					1.8311076616571427
				],
				[
					56.19824550435311,
					1.8311076616571427
				],
				[
					57.78091313258085,
					1.9702544931156467
				],
				[
					58.57348021628894,
					2.10935879803651
				],
				[
					59.992165515022805,
					2.10935879803651
				],
				[
					60.8344461213394,
					2.10935879803651
				],
				[
					61.25433189163459,
					2.10935879803651
				],
				[
					63.0680461993594,
					2.10935879803651
				],
				[
					64.88178177035309,
					2.10935879803651
				],
				[
					66.69551734134672,
					2.10935879803651
				],
				[
					70.99628989197322,
					2.10935879803651
				],
				[
					71.78885697568131,
					2.10935879803651
				],
				[
					72.5814240593894,
					2.10935879803651
				],
				[
					73.60508034913227,
					2.10935879803651
				],
				[
					76.32567307398836,
					2.10935879803651
				],
				[
					78.53443765397293,
					2.10935879803651
				],
				[
					80.74320223395756,
					2.10935879803651
				],
				[
					82.95198807721107,
					2.10935879803651
				],
				[
					84.65141231478157,
					2.10935879803651
				],
				[
					85.16324045965297,
					2.10935879803651
				],
				[
					87.25773623275217,
					2.10935879803651
				],
				[
					88.67642153148603,
					2.10935879803651
				],
				[
					90.09510683021983,
					2.10935879803651
				],
				[
					92.81569955507587,
					2.10935879803651
				],
				[
					93.83931331828103,
					2.10935879803651
				],
				[
					94.63188040198912,
					2.10935879803651
				],
				[
					94.91017406490619,
					2.10935879803651
				],
				[
					95.18842520128555,
					2.10935879803651
				],
				[
					95.18842520128555,
					2.10935879803651
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				95.18842520128555,
				2.10935879803651
			]
		},
		{
			"id": "of0f2mkA9RjPjlIBr7WuX",
			"type": "freedraw",
			"x": 419.46221383110816,
			"y": -274.2217942781376,
			"width": 24.835625615001504,
			"height": 22.857928977782763,
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
			"seed": 1302729623,
			"version": 65,
			"versionNonce": 270614711,
			"isDeleted": true,
			"boundElements": null,
			"updated": 1710827914312,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.0285893681197535,
					0
				],
				[
					-2.847279280759153,
					0
				],
				[
					-5.456069737918256,
					1.038540577948993
				],
				[
					-8.184147133415081,
					1.7839032047747878
				],
				[
					-11.18796659956513,
					2.323054650138886
				],
				[
					-13.401685521195475,
					2.8075169679798933
				],
				[
					-16.010475978354577,
					2.8075169679798933
				],
				[
					-18.224237426522677,
					3.0659082112384795
				],
				[
					-20.43795634815308,
					3.0659082112384795
				],
				[
					-21.518768304607477,
					3.0659082112384795
				],
				[
					-21.801995045901492,
					3.0659082112384795
				],
				[
					-22.316310993230218,
					3.0659082112384795
				],
				[
					-22.457924363877225,
					3.0659082112384795
				],
				[
					-23.11385368185296,
					2.7528703669945003
				],
				[
					-23.628127102643987,
					1.7242809988747467
				],
				[
					-24.231876358822774,
					-0.09445144030240726
				],
				[
					-24.4033433589575,
					-0.7503382317403862
				],
				[
					-24.57476783255447,
					-2.17399913538884
				],
				[
					-24.835625615001504,
					-3.761642368531227
				],
				[
					-24.835625615001504,
					-4.41757168650696
				],
				[
					-24.835625615001504,
					-7.3095888849600215
				],
				[
					-24.835625615001504,
					-8.502160582573708
				],
				[
					-24.835625615001504,
					-9.299745797734204
				],
				[
					-24.835625615001504,
					-10.723364174844903
				],
				[
					-24.21448300489044,
					-12.430251819787316
				],
				[
					-24.21448300489044,
					-12.855134458266036
				],
				[
					-24.075378699969633,
					-13.279974570207003
				],
				[
					-23.484047192808532,
					-14.472588794358444
				],
				[
					-23.20575352989141,
					-14.89742890629941
				],
				[
					-22.61693108845651,
					-15.978240862753864
				],
				[
					-22.167212951942417,
					-16.634127654191843
				],
				[
					-21.34730130447275,
					-17.459014906576158
				],
				[
					-20.927436797446433,
					-17.88389754505488
				],
				[
					-19.79448730573273,
					-18.85286470727459
				],
				[
					-19.00187769548694,
					-19.16590255151857
				],
				[
					-17.58323492329083,
					-19.3373270251156
				],
				[
					-16.16454962455697,
					-19.792020766544283
				],
				[
					-15.371940014311178,
					-19.792020766544283
				],
				[
					-12.651347289455089,
					-19.792020766544283
				],
				[
					-10.837632981730337,
					-19.792020766544283
				],
				[
					-10.186679268669195,
					-19.792020766544283
				],
				[
					-9.766772235105122,
					-19.792020766544283
				],
				[
					-8.74315847189996,
					-19.792020766544283
				],
				[
					-8.092204758838875,
					-19.792020766544283
				],
				[
					-7.530684354627795,
					-19.792020766544283
				],
				[
					-6.507028064884935,
					-19.62306283213576
				],
				[
					-6.367923759964128,
					-19.483916000677198
				],
				[
					-6.0896300970470065,
					-19.20566486429783
				],
				[
					-4.509471534545469,
					-14.904871050402505
				],
				[
					-4.024966690166707,
					-12.696127733686751
				],
				[
					-3.5081842036495345,
					-10.092312881442297
				],
				[
					-2.7180836591298885,
					-7.488498029197842
				],
				[
					-2.1988346334242124,
					-4.884683176953388
				],
				[
					-2.029876699015688,
					-1.7690189165686547
				],
				[
					-1.5776920233131477,
					0.04469539115615362
				],
				[
					-1.5776920233131477,
					1.2323340103929468
				],
				[
					-1.5776920233131477,
					1.6521985174193219
				],
				[
					-1.4385451918545868,
					1.9304921803363868
				],
				[
					-1.4385451918545868,
					2.350356687362762
				],
				[
					-1.4385451918545868,
					2.350356687362762
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				-1.4385451918545868,
				2.350356687362762
			]
		},
		{
			"id": "UjdE0PQ0h87g_EWVfqj_7",
			"type": "freedraw",
			"x": 419.17652055062575,
			"y": -275.3075818395067,
			"width": 18.077690977498833,
			"height": 17.943477224417165,
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
			"seed": 994044215,
			"version": 47,
			"versionNonce": 1847167545,
			"isDeleted": true,
			"boundElements": null,
			"updated": 1710827914312,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-0.1416133706469509
				],
				[
					-2.4969881894621153,
					-0.1416133706469509
				],
				[
					-4.710749637630215,
					-0.1416133706469509
				],
				[
					-7.319540094789318,
					-0.1416133706469509
				],
				[
					-9.928330551948363,
					0.1167778726116353
				],
				[
					-14.236523983409086,
					0.6807648160111626
				],
				[
					-15.66018488705754,
					0.6807648160111626
				],
				[
					-16.457727575680224,
					0.6807648160111626
				],
				[
					-16.740996843511937,
					0.6807648160111626
				],
				[
					-17.16583695545296,
					0.2559247040701962
				],
				[
					-17.84911083719021,
					-0.4273491776671108
				],
				[
					-18.077690977498833,
					-1.4783075046338467
				],
				[
					-18.077690977498833,
					-3.185195149576259
				],
				[
					-18.077690977498833,
					-4.772838382718646
				],
				[
					-18.077690977498833,
					-5.965410080332333
				],
				[
					-17.45654836738771,
					-7.389070983980787
				],
				[
					-17.198157124129125,
					-8.976714217123174
				],
				[
					-16.71862788466501,
					-10.288530326536886
				],
				[
					-15.898716237195345,
					-11.1134175789212
				],
				[
					-15.41918699773123,
					-11.769346896896934
				],
				[
					-15.111124758401843,
					-12.425276214872667
				],
				[
					-14.460171045340758,
					-12.738314059116647
				],
				[
					-13.468834924274063,
					-13.737092324286436
				],
				[
					-12.907314520062982,
					-13.878748221471142
				],
				[
					-11.488629221329177,
					-14.05017269506817
				],
				[
					-10.069943922595371,
					-14.450177308973707
				],
				[
					-8.370498421755997,
					-14.733404050267723
				],
				[
					-7.808978017544916,
					-14.733404050267723
				],
				[
					-7.389113510518541,
					-14.733404050267723
				],
				[
					-6.969206476954469,
					-14.733404050267723
				],
				[
					-6.268581767822582,
					-14.733404050267723
				],
				[
					-5.0809431485857885,
					-14.36818614422674
				],
				[
					-4.288376064877696,
					-13.747043534115676
				],
				[
					-2.827461914176183,
					-12.025271600967073
				],
				[
					-0.8820429190959089,
					-8.81273188762924
				],
				[
					-0.3975380747171471,
					-6.603946044375732
				],
				[
					-0.1167778726116353,
					-3.6050596566026343
				],
				[
					-0.1167778726116353,
					-0.6062157953671772
				],
				[
					-0.1167778726116353,
					1.6025700478862746
				],
				[
					-0.1167778726116353,
					2.929312972043874
				],
				[
					-0.1167778726116353,
					3.210073174149443
				],
				[
					-0.1167778726116353,
					3.210073174149443
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				-0.1167778726116353,
				3.210073174149443
			]
		},
		{
			"id": "LyTqZQZ0s0A5jGYgMTkcQ",
			"type": "freedraw",
			"x": 50.27659245141278,
			"y": 391.45690257877084,
			"width": 0.0001,
			"height": 0.0001,
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
			"seed": 1913278167,
			"version": 5,
			"versionNonce": 152217817,
			"isDeleted": true,
			"boundElements": null,
			"updated": 1710827914312,
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
			"id": "fAv5QebT1dOHwVWSyl3aB",
			"type": "freedraw",
			"x": 50.27659245141278,
			"y": 391.45690257877084,
			"width": 0.0001,
			"height": 0.0001,
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
			"seed": 56429111,
			"version": 4,
			"versionNonce": 525987031,
			"isDeleted": true,
			"boundElements": null,
			"updated": 1710827914046,
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
		"currentItemTextAlign": "right",
		"currentItemStartArrowhead": null,
		"currentItemEndArrowhead": "arrow",
		"scrollX": 663.2392418792052,
		"scrollY": -753.2668700971396,
		"zoom": {
			"value": 1.4352251442354718
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