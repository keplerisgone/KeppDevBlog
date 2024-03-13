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

그래서 conventional AM (DSB-LC)는 신호를 모두 양으로 옮김 ^fO9vQ0Fk


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
			"version": 8,
			"versionNonce": 393707374,
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
			"updated": 1710337036349,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 8,
			"versionNonce": 1565849202,
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
			"updated": 1710337036350,
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
			"version": 8,
			"versionNonce": 124871086,
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
			"updated": 1710337036350,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 8,
			"versionNonce": 1813076018,
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
			"updated": 1710337036350,
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
			"version": 8,
			"versionNonce": 443874286,
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
			"updated": 1710337036350,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 8,
			"versionNonce": 811303410,
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
			"updated": 1710337036350,
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
			"version": 8,
			"versionNonce": 915099182,
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
			"updated": 1710337036350,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 8,
			"versionNonce": 1161458610,
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
			"updated": 1710337036350,
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
			"version": 8,
			"versionNonce": 412964974,
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
			"updated": 1710337036350,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 8,
			"versionNonce": 1289039218,
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
			"updated": 1710337036350,
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
			"version": 8,
			"versionNonce": 2020874926,
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
			"updated": 1710337036350,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 8,
			"versionNonce": 208842546,
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
			"updated": 1710337036350,
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
			"version": 8,
			"versionNonce": 750294254,
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
			"updated": 1710337036350,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 8,
			"versionNonce": 142211314,
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
			"updated": 1710337036350,
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
			"version": 8,
			"versionNonce": 1324599086,
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
			"updated": 1710337036350,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 8,
			"versionNonce": 544344754,
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
			"updated": 1710337036350,
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
			"version": 8,
			"versionNonce": 1603187054,
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
			"updated": 1710337036350,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 8,
			"versionNonce": 721544306,
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
			"updated": 1710337036350,
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
			"version": 8,
			"versionNonce": 1775391662,
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
			"updated": 1710337036350,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 8,
			"versionNonce": 300975666,
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
			"updated": 1710337036350,
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
			"version": 8,
			"versionNonce": 669494766,
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
			"updated": 1710337036350,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 8,
			"versionNonce": 1847914482,
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
			"updated": 1710337036350,
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
			"version": 8,
			"versionNonce": 651673646,
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
			"updated": 1710337036350,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 8,
			"versionNonce": 598090162,
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
			"updated": 1710337036350,
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
			"version": 8,
			"versionNonce": 1787529838,
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
			"updated": 1710337036350,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 8,
			"versionNonce": 2107317106,
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
			"updated": 1710337036350,
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
			"version": 8,
			"versionNonce": 298585262,
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
			"updated": 1710337036350,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 8,
			"versionNonce": 1246420274,
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
			"updated": 1710337036350,
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
			"version": 8,
			"versionNonce": 2051163886,
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
			"updated": 1710337036350,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 8,
			"versionNonce": 1998350066,
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
			"updated": 1710337036350,
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
			"version": 8,
			"versionNonce": 1685535022,
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
			"updated": 1710337036350,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 8,
			"versionNonce": 748075186,
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
			"updated": 1710337036350,
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
			"version": 8,
			"versionNonce": 399762286,
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
			"updated": 1710337036350,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 8,
			"versionNonce": 1784730226,
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
			"updated": 1710337036350,
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
			"version": 8,
			"versionNonce": 111232430,
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
			"updated": 1710337036350,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 8,
			"versionNonce": 591508530,
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
			"updated": 1710337036350,
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
			"version": 8,
			"versionNonce": 1913151470,
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
			"updated": 1710337036350,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 8,
			"versionNonce": 1495293426,
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
			"updated": 1710337036350,
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
			"version": 8,
			"versionNonce": 236073518,
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
			"updated": 1710337036350,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 8,
			"versionNonce": 956551090,
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
			"updated": 1710337036350,
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
			"version": 8,
			"versionNonce": 631749742,
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
			"updated": 1710337036350,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 8,
			"versionNonce": 923994482,
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
			"updated": 1710337036350,
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
			"version": 8,
			"versionNonce": 1049755310,
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
			"updated": 1710337036350,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 8,
			"versionNonce": 714410802,
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
			"updated": 1710337036350,
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
			"version": 8,
			"versionNonce": 1031403758,
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
			"updated": 1710337036350,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 8,
			"versionNonce": 1777390834,
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
			"updated": 1710337036350,
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
			"version": 8,
			"versionNonce": 166243118,
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
			"updated": 1710337036350,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 8,
			"versionNonce": 1722640050,
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
			"updated": 1710337036350,
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
			"version": 8,
			"versionNonce": 843519342,
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
			"updated": 1710337036350,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 8,
			"versionNonce": 1232191602,
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
			"updated": 1710337036350,
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
			"version": 8,
			"versionNonce": 266221486,
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
			"updated": 1710337036350,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 8,
			"versionNonce": 235201074,
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
			"updated": 1710337036350,
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
			"version": 8,
			"versionNonce": 1792479726,
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
			"updated": 1710337036350,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 8,
			"versionNonce": 525192178,
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
			"updated": 1710337036350,
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
			"version": 8,
			"versionNonce": 507159598,
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
			"updated": 1710337036350,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 8,
			"versionNonce": 1934851506,
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
			"updated": 1710337036350,
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
			"version": 8,
			"versionNonce": 1005710958,
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
			"updated": 1710337036350,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 8,
			"versionNonce": 658306930,
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
			"updated": 1710337036350,
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
			"version": 8,
			"versionNonce": 818278574,
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
			"updated": 1710337036350,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 8,
			"versionNonce": 458307890,
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
			"updated": 1710337036350,
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
			"version": 8,
			"versionNonce": 1751100142,
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
			"updated": 1710337036350,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 8,
			"versionNonce": 251085554,
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
			"updated": 1710337036350,
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
			"version": 8,
			"versionNonce": 1900551470,
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
			"updated": 1710337036350,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 8,
			"versionNonce": 1018565810,
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
			"updated": 1710337036350,
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
			"version": 8,
			"versionNonce": 552093550,
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
			"updated": 1710337036350,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 8,
			"versionNonce": 1983164018,
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
			"updated": 1710337036350,
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
			"version": 8,
			"versionNonce": 931735982,
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
			"updated": 1710337036350,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 8,
			"versionNonce": 1077547058,
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
			"updated": 1710337036350,
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
			"version": 8,
			"versionNonce": 72598510,
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
			"updated": 1710337036350,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 8,
			"versionNonce": 1856846322,
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
			"updated": 1710337036350,
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
			"version": 8,
			"versionNonce": 156309038,
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
			"updated": 1710337036350,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 8,
			"versionNonce": 1083517874,
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
			"updated": 1710337036350,
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
			"version": 8,
			"versionNonce": 527048814,
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
			"updated": 1710337036350,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 8,
			"versionNonce": 2082006386,
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
			"updated": 1710337036350,
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
			"version": 8,
			"versionNonce": 443015854,
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
			"updated": 1710337036350,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 8,
			"versionNonce": 176121650,
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
			"updated": 1710337036350,
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
			"version": 8,
			"versionNonce": 1827888366,
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
			"updated": 1710337036350,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 8,
			"versionNonce": 338669810,
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
			"updated": 1710337036350,
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
			"version": 8,
			"versionNonce": 1284869934,
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
			"updated": 1710337036350,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 8,
			"versionNonce": 481346226,
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
			"updated": 1710337036350,
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
			"version": 8,
			"versionNonce": 1438087534,
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
			"updated": 1710337036350,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 8,
			"versionNonce": 514432114,
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
			"updated": 1710337036350,
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
			"version": 8,
			"versionNonce": 799153070,
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
			"updated": 1710337036350,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 8,
			"versionNonce": 669072946,
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
			"updated": 1710337036350,
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
			"version": 8,
			"versionNonce": 813594094,
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
			"updated": 1710337036350,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 8,
			"versionNonce": 1967040498,
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
			"updated": 1710337036350,
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
			"version": 8,
			"versionNonce": 22382638,
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
			"updated": 1710337036350,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 8,
			"versionNonce": 248043954,
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
			"updated": 1710337036350,
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
			"version": 8,
			"versionNonce": 1108365934,
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
			"updated": 1710337036350,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 8,
			"versionNonce": 1671877490,
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
			"updated": 1710337036350,
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
			"version": 8,
			"versionNonce": 762827950,
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
			"updated": 1710337036350,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 8,
			"versionNonce": 1713345842,
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
			"updated": 1710337036350,
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
			"version": 8,
			"versionNonce": 1026887406,
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
			"updated": 1710337036350,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 8,
			"versionNonce": 664411890,
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
			"updated": 1710337036350,
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
			"version": 8,
			"versionNonce": 1305542958,
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
			"updated": 1710337036350,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 8,
			"versionNonce": 1956475058,
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
			"updated": 1710337036350,
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
			"version": 8,
			"versionNonce": 1119136622,
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
			"updated": 1710337036350,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 8,
			"versionNonce": 1892715122,
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
			"updated": 1710337036350,
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
			"version": 8,
			"versionNonce": 707333550,
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
			"updated": 1710337036350,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 8,
			"versionNonce": 855272498,
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
			"updated": 1710337036350,
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
			"version": 8,
			"versionNonce": 1633101806,
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
			"updated": 1710337036350,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 8,
			"versionNonce": 1627526642,
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
			"updated": 1710337036350,
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
			"version": 8,
			"versionNonce": 944241198,
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
			"updated": 1710337036350,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 8,
			"versionNonce": 1273923506,
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
			"updated": 1710337036350,
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
			"version": 8,
			"versionNonce": 367297646,
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
			"updated": 1710337036350,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 8,
			"versionNonce": 199672178,
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
			"updated": 1710337036350,
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
			"version": 8,
			"versionNonce": 469092014,
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
			"updated": 1710337036350,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 8,
			"versionNonce": 473023282,
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
			"updated": 1710337036350,
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
			"version": 8,
			"versionNonce": 1260699886,
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
			"updated": 1710337036350,
			"link": null,
			"locked": true
		},
		{
			"type": "image",
			"version": 8,
			"versionNonce": 2000063730,
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
			"updated": 1710337036351,
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
			"id": "99BQVgc2",
			"type": "text",
			"x": 592.8348307053371,
			"y": -6311.877664611609,
			"width": 466.7198486328125,
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
			"seed": 591648754,
			"version": 324,
			"versionNonce": 846995122,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710337036351,
			"link": null,
			"locked": false,
			"text": "- analog signal - continuous한 신호를 보냄\n    그렇다고 digital이 non continuous인 건 아님\n    digital은 그냥 level이 존재함\n\n- bandwidth를 유지하는 것이 중요하기 때문에 따로 변형을 가하지 x\n- 보내는 정보에 따라 bandwidth가 다름",
			"rawText": "- analog signal - continuous한 신호를 보냄\n    그렇다고 digital이 non continuous인 건 아님\n    digital은 그냥 level이 존재함\n\n- bandwidth를 유지하는 것이 중요하기 때문에 따로 변형을 가하지 x\n- 보내는 정보에 따라 bandwidth가 다름",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 114,
			"containerId": null,
			"originalText": "- analog signal - continuous한 신호를 보냄\n    그렇다고 digital이 non continuous인 건 아님\n    digital은 그냥 level이 존재함\n\n- bandwidth를 유지하는 것이 중요하기 때문에 따로 변형을 가하지 x\n- 보내는 정보에 따라 bandwidth가 다름",
			"lineHeight": 1.25
		},
		{
			"id": "NZqpQiJX",
			"type": "text",
			"x": -960.4043506536436,
			"y": -5857.998360384538,
			"width": 361.8878479003906,
			"height": 320,
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
			"seed": 27092654,
			"version": 617,
			"versionNonce": 1507843438,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710337036351,
			"link": null,
			"locked": false,
			"text": "analog signal은 carrier modulation에 의해 전달됨\n\n- analog를 전해주는 신호 = carrier wave\n\n- 왜 사인함수인가 : 진동을 보기 좋아서\n-> rectangular 함수를 써도 됨\n\n- 뭐든 지 level을 적당히 정해야 효율적임\n    예를 들어 phase는 360도까지만 존재\n\n- carrier에는 정보가 담기는데...\n이 정보는 A, P, F 중에 하나에 담김\n각 종류마다 modulation이 있음\n\n- 이런 modulation을 진행하는 게 바로 modem\n+ demodulation도 진행",
			"rawText": "analog signal은 carrier modulation에 의해 전달됨\n\n- analog를 전해주는 신호 = carrier wave\n\n- 왜 사인함수인가 : 진동을 보기 좋아서\n-> rectangular 함수를 써도 됨\n\n- 뭐든 지 level을 적당히 정해야 효율적임\n    예를 들어 phase는 360도까지만 존재\n\n- carrier에는 정보가 담기는데...\n이 정보는 A, P, F 중에 하나에 담김\n각 종류마다 modulation이 있음\n\n- 이런 modulation을 진행하는 게 바로 modem\n+ demodulation도 진행",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "right",
			"verticalAlign": "top",
			"baseline": 314,
			"containerId": null,
			"originalText": "analog signal은 carrier modulation에 의해 전달됨\n\n- analog를 전해주는 신호 = carrier wave\n\n- 왜 사인함수인가 : 진동을 보기 좋아서\n-> rectangular 함수를 써도 됨\n\n- 뭐든 지 level을 적당히 정해야 효율적임\n    예를 들어 phase는 360도까지만 존재\n\n- carrier에는 정보가 담기는데...\n이 정보는 A, P, F 중에 하나에 담김\n각 종류마다 modulation이 있음\n\n- 이런 modulation을 진행하는 게 바로 modem\n+ demodulation도 진행",
			"lineHeight": 1.25
		},
		{
			"id": "dgFz7CDC",
			"type": "text",
			"x": 593.4410202439296,
			"y": -5852.822735372356,
			"width": 253.37591552734375,
			"height": 300,
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
			"seed": 368782386,
			"version": 361,
			"versionNonce": 447314034,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710337036351,
			"link": null,
			"locked": false,
			"text": "- m(t)\n    메세지를 담은 signal\n    analog\n    baseband = 중심이 0이라는 뜻\n    bandwidth가 W\n    modulating (당하는)\n\n- c(t)\n    그냥 코사인 함수\n    carrier\n\n- u(t)\n    Passband = 밴드의 중심이 fc\n    Modulated (당한)\n    transmitted = 전달되는",
			"rawText": "- m(t)\n    메세지를 담은 signal\n    analog\n    baseband = 중심이 0이라는 뜻\n    bandwidth가 W\n    modulating (당하는)\n\n- c(t)\n    그냥 코사인 함수\n    carrier\n\n- u(t)\n    Passband = 밴드의 중심이 fc\n    Modulated (당한)\n    transmitted = 전달되는",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 294,
			"containerId": null,
			"originalText": "- m(t)\n    메세지를 담은 signal\n    analog\n    baseband = 중심이 0이라는 뜻\n    bandwidth가 W\n    modulating (당하는)\n\n- c(t)\n    그냥 코사인 함수\n    carrier\n\n- u(t)\n    Passband = 밴드의 중심이 fc\n    Modulated (당한)\n    transmitted = 전달되는",
			"lineHeight": 1.25
		},
		{
			"id": "SeJ3G_dxOvcqiA90syyMP",
			"type": "freedraw",
			"x": -515.0706561758109,
			"y": -5106.533342482828,
			"width": 13.18527907044097,
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
			"seed": 1279235822,
			"version": 13,
			"versionNonce": 148756974,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710337036351,
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
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				13.18527907044097,
				0
			]
		},
		{
			"id": "oNSn96fvjK7EzB-uOWrLt",
			"type": "freedraw",
			"x": -427.6668796354779,
			"y": -5146.453194189305,
			"width": 31.577984352707176,
			"height": 21.43020536270342,
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
			"seed": 1093093614,
			"version": 26,
			"versionNonce": 1610056690,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710337036351,
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
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				31.577984352707176,
				21.43020536270342
			]
		},
		{
			"id": "o03IG-ohDHVPsw51ZupoO",
			"type": "freedraw",
			"x": -395.9328832906274,
			"y": -5130.944283189199,
			"width": 1.1771703608432063,
			"height": 10.46688339405955,
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
			"seed": 907073582,
			"version": 20,
			"versionNonce": 1613261870,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710337036351,
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
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				0.27658142590564694,
				10.46688339405955
			]
		},
		{
			"id": "9UEg7K2gNlZiMsSw1dvQ7",
			"type": "freedraw",
			"x": -276.49728772023445,
			"y": -5139.345221473604,
			"width": 11.480961342990895,
			"height": 6.989749935346481,
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
			"seed": 1780689390,
			"version": 20,
			"versionNonce": 1711682994,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710337036351,
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
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				-11.480961342990895,
				6.720248929209447
			]
		},
		{
			"id": "AfvEnGWz8NKdXNJpGEcJ8",
			"type": "freedraw",
			"x": -287.71348182344684,
			"y": -5142.106140128135,
			"width": 15.097558841360296,
			"height": 13.01741243262859,
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
			"seed": 526463918,
			"version": 15,
			"versionNonce": 216446574,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710337036351,
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
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				15.097558841360296,
				13.01741243262859
			]
		},
		{
			"id": "DW3OULcJ8OFC6U7x00_Zc",
			"type": "freedraw",
			"x": -271.0108929695534,
			"y": -5131.06719927637,
			"width": 24.210018623128803,
			"height": 22.772814788866526,
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
			"seed": 680071726,
			"version": 34,
			"versionNonce": 584626034,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710337036351,
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
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				-2.1770470106978337,
				-2.8105625119897013
			]
		},
		{
			"id": "4kMKvnhF_UZOqF0l_irCi",
			"type": "freedraw",
			"x": -203.12973532782155,
			"y": -5125.164799519667,
			"width": 31.42905278033163,
			"height": 19.111307199397743,
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
			"seed": 876579694,
			"version": 24,
			"versionNonce": 400668846,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710337036351,
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
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				31.42905278033163,
				-18.846580419161
			]
		},
		{
			"id": "jCIb5e1ovLn2qFGk5G02W",
			"type": "freedraw",
			"x": -179.72809834448128,
			"y": -5143.472418386094,
			"width": 11.722019291432389,
			"height": 11.790598214327474,
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
			"seed": 405650990,
			"version": 20,
			"versionNonce": 448131378,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710337036351,
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
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				11.722019291432389,
				11.65586794103001
			]
		},
		{
			"id": "KOduWe3iBVI-A2RP7ILvW",
			"type": "freedraw",
			"x": -136.24606722299393,
			"y": -5017.075435018967,
			"width": 8.211830387289524,
			"height": 16.352735198275695,
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
			"seed": 1280888814,
			"version": 26,
			"versionNonce": 146961134,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710337036351,
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
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				-8.211830387289524,
				13.445272084319186
			]
		},
		{
			"id": "MK7H03tIznms3_k3DSxde",
			"type": "freedraw",
			"x": -148.10993766703382,
			"y": -5006.821287894278,
			"width": 7.613757444378734,
			"height": 0.6216608556233041,
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
			"seed": 1539309358,
			"version": 15,
			"versionNonce": 822409970,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710337036351,
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
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				7.613757444378734,
				-0.6216608556233041
			]
		},
		{
			"id": "uvcWbHVOuqEmGTNY7JjVq",
			"type": "freedraw",
			"x": -132.8114567424309,
			"y": -5003.256680906776,
			"width": 6.105749412436921,
			"height": 4.66611800568262,
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
			"seed": 1543994798,
			"version": 28,
			"versionNonce": 168944942,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710337036351,
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
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				-3.314041046800753,
				3.8009716291253426
			]
		},
		{
			"id": "f5fpmUNp3zdoQ-KFGHpls",
			"type": "freedraw",
			"x": -148.14076783768041,
			"y": -5120.035379303915,
			"width": 12.979663680380668,
			"height": 13.317662690329598,
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
			"seed": 828158318,
			"version": 49,
			"versionNonce": 1145883826,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710337036351,
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
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				12.979663680380668,
				-3.8624701322523833
			]
		},
		{
			"id": "Q7VatEu8ukYeh7IScACCb",
			"type": "freedraw",
			"x": -474.8577560100252,
			"y": -4637.633979666198,
			"width": 28.935248018987977,
			"height": 15.468694215823234,
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
			"seed": 716342382,
			"version": 39,
			"versionNonce": 221843310,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710337036351,
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
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				5.131807328703701,
				-2.5552628049290433
			]
		},
		{
			"id": "zeCcV0Iy",
			"type": "text",
			"x": -469.58110352264066,
			"y": -4638.71623194261,
			"width": 41.07196044921875,
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
			"seed": 1172683186,
			"version": 35,
			"versionNonce": 1853944238,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710337036351,
			"link": null,
			"locked": false,
			"text": "Gibbs",
			"rawText": "Gibbs",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 14,
			"containerId": null,
			"originalText": "Gibbs",
			"lineHeight": 1.25
		},
		{
			"id": "gaHr29zo",
			"type": "text",
			"x": 596.5779451900742,
			"y": -4947.68762473993,
			"width": 345.6479187011719,
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
			"seed": 1609638514,
			"version": 276,
			"versionNonce": 1803733042,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710337036351,
			"link": null,
			"locked": false,
			"text": "왜 하는가?\n\n1. 채널의 주파수 대역을 맞추기 위해서\n\n2. transmitter를 맞추기 위해서\n    - 안테나의 크기는 신호의 반파장이어야 하는데,\n    - 주파수를 크게 하면 파장이 줄어든다\n\n",
			"rawText": "왜 하는가?\n\n1. 채널의 주파수 대역을 맞추기 위해서\n\n2. transmitter를 맞추기 위해서\n    - 안테나의 크기는 신호의 반파장이어야 하는데,\n    - 주파수를 크게 하면 파장이 줄어든다\n\n",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 174,
			"containerId": null,
			"originalText": "왜 하는가?\n\n1. 채널의 주파수 대역을 맞추기 위해서\n\n2. transmitter를 맞추기 위해서\n    - 안테나의 크기는 신호의 반파장이어야 하는데,\n    - 주파수를 크게 하면 파장이 줄어든다\n\n",
			"lineHeight": 1.25
		},
		{
			"id": "ITytvav6aOCvln2zUzNNV",
			"type": "freedraw",
			"x": 325.94973622530665,
			"y": -4664.184178171473,
			"width": 216.8122445026919,
			"height": 0.3261848238225866,
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
			"seed": 830268274,
			"version": 56,
			"versionNonce": 420645870,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710337036351,
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
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				216.8122445026919,
				-0.3261848238225866
			]
		},
		{
			"id": "n1V75BuxcD88E9JsjR_cy",
			"type": "freedraw",
			"x": 398.65771717168184,
			"y": -4840.201997517955,
			"width": 141.05256217680267,
			"height": 7.375046149345508,
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
			"seed": 1363291762,
			"version": 26,
			"versionNonce": 538898930,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710337036351,
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
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				141.05256217680267,
				-7.375046149345508
			]
		},
		{
			"id": "cPNITFe_YwpDEMzlP_fUm",
			"type": "freedraw",
			"x": 102.44556447247714,
			"y": -4821.747834192102,
			"width": 181.617622192074,
			"height": 1.0282387884681157,
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
			"seed": 1059327218,
			"version": 43,
			"versionNonce": 720821806,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710337036351,
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
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				181.617622192074,
				-1.0282387884681157
			]
		},
		{
			"id": "5xLJkgZS",
			"type": "text",
			"x": -1026.566559808847,
			"y": -4493.417542030982,
			"width": 388.5438232421875,
			"height": 160,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [
				"g94ixqIAcN-ZKggGAbYUq"
			],
			"frameId": null,
			"roundness": null,
			"seed": 580924146,
			"version": 272,
			"versionNonce": 1451007346,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710337036351,
			"link": null,
			"locked": false,
			"text": "3. Freauency-division\n- 더 많은 사람들이 이용할 수 있게 한다\n\n4. 노이즈에 강해진다\n근데 AM만 이게 해당이 안 됨\nPM,FM의 경우는 bandwidth를 5배로 늘리는 경우만 해당\n\n아무튼 takeoff가 있다~",
			"rawText": "3. Freauency-division\n- 더 많은 사람들이 이용할 수 있게 한다\n\n4. 노이즈에 강해진다\n근데 AM만 이게 해당이 안 됨\nPM,FM의 경우는 bandwidth를 5배로 늘리는 경우만 해당\n\n아무튼 takeoff가 있다~",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "right",
			"verticalAlign": "top",
			"baseline": 154,
			"containerId": null,
			"originalText": "3. Freauency-division\n- 더 많은 사람들이 이용할 수 있게 한다\n\n4. 노이즈에 강해진다\n근데 AM만 이게 해당이 안 됨\nPM,FM의 경우는 bandwidth를 5배로 늘리는 경우만 해당\n\n아무튼 takeoff가 있다~",
			"lineHeight": 1.25
		},
		{
			"id": "x4RbemzLAEVsr6MXAJ1l0",
			"type": "freedraw",
			"x": -975.4840347517368,
			"y": -4374.216227435825,
			"width": 78.62935622805571,
			"height": 36.021898556301494,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [
				"g94ixqIAcN-ZKggGAbYUq"
			],
			"frameId": null,
			"roundness": null,
			"seed": 1212014126,
			"version": 32,
			"versionNonce": 1396419246,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710337036351,
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
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				6.814802877767079,
				-0.9502327923964913
			]
		},
		{
			"id": "p6QpW7hZ",
			"type": "text",
			"x": -1105.6793170364472,
			"y": -4428.039980359646,
			"width": 128.06393432617188,
			"height": 20,
			"angle": 0,
			"strokeColor": "#1971c2",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 0.5,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [
				"g94ixqIAcN-ZKggGAbYUq"
			],
			"frameId": null,
			"roundness": null,
			"seed": 101363822,
			"version": 60,
			"versionNonce": 1336680242,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710337036351,
			"link": null,
			"locked": false,
			"text": "angle modulation",
			"rawText": "angle modulation",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "right",
			"verticalAlign": "top",
			"baseline": 14,
			"containerId": null,
			"originalText": "angle modulation",
			"lineHeight": 1.25
		},
		{
			"id": "dP6Pf2UT",
			"type": "text",
			"x": -1048.3344678332194,
			"y": -3603.5747422430777,
			"width": 451.391845703125,
			"height": 320,
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
			"seed": 746753970,
			"version": 515,
			"versionNonce": 1745757422,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710337036351,
			"link": null,
			"locked": false,
			"text": "DSB-SC AM\n- 원래 y축에 의해서 쪼개져 있던게 나와서 bandwidth가 두배가 됨\n- cos이 사라져요..\n\nDSB-LC AM\n- carrier(cos)이 살아있어요\n- 간섭을 억제할 수 있음\n\nSSB AM\n- 신호의 절반만 보내요\n\nVSB AM\n- SSB가 현실적인 건 아니니까\n신호의 60%만 보내요\n\n위 모두 analog, digital 상관없이 스펙트럼에 관한 이야기",
			"rawText": "DSB-SC AM\n- 원래 y축에 의해서 쪼개져 있던게 나와서 bandwidth가 두배가 됨\n- cos이 사라져요..\n\nDSB-LC AM\n- carrier(cos)이 살아있어요\n- 간섭을 억제할 수 있음\n\nSSB AM\n- 신호의 절반만 보내요\n\nVSB AM\n- SSB가 현실적인 건 아니니까\n신호의 60%만 보내요\n\n위 모두 analog, digital 상관없이 스펙트럼에 관한 이야기",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "right",
			"verticalAlign": "top",
			"baseline": 314,
			"containerId": null,
			"originalText": "DSB-SC AM\n- 원래 y축에 의해서 쪼개져 있던게 나와서 bandwidth가 두배가 됨\n- cos이 사라져요..\n\nDSB-LC AM\n- carrier(cos)이 살아있어요\n- 간섭을 억제할 수 있음\n\nSSB AM\n- 신호의 절반만 보내요\n\nVSB AM\n- SSB가 현실적인 건 아니니까\n신호의 60%만 보내요\n\n위 모두 analog, digital 상관없이 스펙트럼에 관한 이야기",
			"lineHeight": 1.25
		},
		{
			"id": "c1vX80zjc6gJMhMYRVxoG",
			"type": "freedraw",
			"x": -483.19964359356567,
			"y": -3375.859217731373,
			"width": 18.699995500193722,
			"height": 96.05289365248927,
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
			"seed": 1307002926,
			"version": 69,
			"versionNonce": 50686194,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710337036351,
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
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				-12.60848784637568,
				81.86539127878495
			]
		},
		{
			"id": "caORztdHkhD3WRBY0ZIm4",
			"type": "freedraw",
			"x": -324.49191311706477,
			"y": -3465.5511431834475,
			"width": 41.661918186175626,
			"height": 31.65360323582854,
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
			"seed": 2124701422,
			"version": 69,
			"versionNonce": 689395502,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710337036351,
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
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				5.034866267195525,
				-21.645288285481456
			]
		},
		{
			"id": "Jh0qgU65",
			"type": "text",
			"x": 780.2536657406323,
			"y": -5743.767662304612,
			"width": 318.9278564453125,
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
			"seed": 745871982,
			"version": 109,
			"versionNonce": 529060146,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710337054085,
			"link": null,
			"locked": false,
			"text": "가장 중요한 점은 bandwidth는 \"양수\" 부분이다",
			"rawText": "가장 중요한 점은 bandwidth는 \"양수\" 부분이다",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "right",
			"verticalAlign": "top",
			"baseline": 14,
			"containerId": null,
			"originalText": "가장 중요한 점은 bandwidth는 \"양수\" 부분이다",
			"lineHeight": 1.25
		},
		{
			"id": "W7YhoNii",
			"type": "text",
			"x": 597.2449636778365,
			"y": -3577.8093576946476,
			"width": 436.9278564453125,
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
			"seed": 456929134,
			"version": 295,
			"versionNonce": 1809156210,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710337170079,
			"link": null,
			"locked": false,
			"text": "- 전까지 열심히 한 예제들\n\n- bandwidth가 2배가 됨 ⭐️\n\n- LSB / USB가 나뉘는데, y축에 가까운 기준임 (대칭이 되므로)\n\n- 진폭은 절반이 되는데, 통신에서 상수는 그리 중요하지 않다",
			"rawText": "- 전까지 열심히 한 예제들\n\n- bandwidth가 2배가 됨 ⭐️\n\n- LSB / USB가 나뉘는데, y축에 가까운 기준임 (대칭이 되므로)\n\n- 진폭은 절반이 되는데, 통신에서 상수는 그리 중요하지 않다",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 134,
			"containerId": null,
			"originalText": "- 전까지 열심히 한 예제들\n\n- bandwidth가 2배가 됨 ⭐️\n\n- LSB / USB가 나뉘는데, y축에 가까운 기준임 (대칭이 되므로)\n\n- 진폭은 절반이 되는데, 통신에서 상수는 그리 중요하지 않다",
			"lineHeight": 1.25
		},
		{
			"id": "MlyofAWUwm3aoQ_TaYTn8",
			"type": "freedraw",
			"x": -409.139504769227,
			"y": -2912.483755660424,
			"width": 51.68443443560005,
			"height": 7.786357848549869,
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
			"seed": 1825677746,
			"version": 45,
			"versionNonce": 1595339566,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710337210528,
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
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				51.68443443560005,
				3.4015145755906815
			]
		},
		{
			"id": "reEK2XQX-BD4hpwUD2KyL",
			"type": "freedraw",
			"x": -307.77038919773605,
			"y": -2909.8528739723733,
			"width": 48.30893534521368,
			"height": 6.6021070679389595,
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
			"seed": 388298866,
			"version": 56,
			"versionNonce": 1975587118,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710337212443,
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
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				48.174205071915594,
				2.0872672880404934
			]
		},
		{
			"id": "sqFJaB0M",
			"type": "text",
			"x": 595.5530847733237,
			"y": -3137.58988250063,
			"width": 298.7998962402344,
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
			"seed": 1079467058,
			"version": 162,
			"versionNonce": 351509874,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710337269538,
			"link": null,
			"locked": false,
			"text": "Power는 어떻게 계산하나요?\n\n- 결과적으로 u(t)의 power는 요렇게 나온다\n\n- power 손실이 거의 없는 방법",
			"rawText": "Power는 어떻게 계산하나요?\n\n- 결과적으로 u(t)의 power는 요렇게 나온다\n\n- power 손실이 거의 없는 방법",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 94,
			"containerId": null,
			"originalText": "Power는 어떻게 계산하나요?\n\n- 결과적으로 u(t)의 power는 요렇게 나온다\n\n- power 손실이 거의 없는 방법",
			"lineHeight": 1.25
		},
		{
			"id": "CF3lUJDiIdZSJIAiudJkh",
			"type": "freedraw",
			"x": 810.5304081485035,
			"y": -3074.957055667211,
			"width": 262.96541455605325,
			"height": 130.39653042608643,
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
			"seed": 449929774,
			"version": 55,
			"versionNonce": 1094394994,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710337238209,
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
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				-262.8330309361638,
				130.12706987949014
			]
		},
		{
			"id": "kPqOtFUtuoIDTI8VMlwKE",
			"type": "freedraw",
			"x": 553.7841915593401,
			"y": -2952.387059414415,
			"width": 13.29638097148495,
			"height": 18.94582767453585,
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
			"seed": 797601262,
			"version": 17,
			"versionNonce": 546710066,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710337238826,
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
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				1.5553456955331058,
				18.94582767453585
			]
		},
		{
			"id": "qURmkO1L-coUe0Oy2bY-T",
			"type": "freedraw",
			"x": 532.3917754084273,
			"y": -2979.3154332543845,
			"width": 76.82579124523016,
			"height": 71.52850439166468,
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
			"seed": 1443193902,
			"version": 156,
			"versionNonce": 1444274994,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710337241705,
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
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				-56.06689059560898,
				13.977112757743726
			]
		},
		{
			"id": "KHu9pbTm",
			"type": "text",
			"x": 743.5955182640978,
			"y": -3002.53354575734,
			"width": 189.3919219970703,
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
			"seed": 1037417838,
			"version": 61,
			"versionNonce": 602923822,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710337249363,
			"link": null,
			"locked": false,
			"text": "외워도 좋지만 계산도 해봐...",
			"rawText": "외워도 좋지만 계산도 해봐...",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 14,
			"containerId": null,
			"originalText": "외워도 좋지만 계산도 해봐...",
			"lineHeight": 1.25
		},
		{
			"id": "r6piIJBX",
			"type": "text",
			"x": 593.0861856070983,
			"y": -2697.905788189924,
			"width": 341.59991455078125,
			"height": 260,
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
			"seed": 904297138,
			"version": 607,
			"versionNonce": 498144498,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710337545792,
			"link": null,
			"locked": false,
			"text": "이상적인 채널이란?\n- 크기가 상수\n- 위상의 변화가 linear -> 노이즈 감지 때문\n\n- u(t)를 받아서 다시 modulation을 하면 됨\n    - 이게 왜 그러냐면 modulation을 다시 할 때\n    - 원래 신호 성분이 0으로 가기 때문\n    - 요걸 LPF 같은 걸로 빼내면 된다\n\n- 하지만 time delay가 phase의 형태로 나타남\n    다를 경우는 문제가 없지만, (상수임)\n    phi = 90이라면 ? (cos phi = 0)\n    요걸 phase-coherent라고 함",
			"rawText": "이상적인 채널이란?\n- 크기가 상수\n- 위상의 변화가 linear -> 노이즈 감지 때문\n\n- u(t)를 받아서 다시 modulation을 하면 됨\n    - 이게 왜 그러냐면 modulation을 다시 할 때\n    - 원래 신호 성분이 0으로 가기 때문\n    - 요걸 LPF 같은 걸로 빼내면 된다\n\n- 하지만 time delay가 phase의 형태로 나타남\n    다를 경우는 문제가 없지만, (상수임)\n    phi = 90이라면 ? (cos phi = 0)\n    요걸 phase-coherent라고 함",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 254,
			"containerId": null,
			"originalText": "이상적인 채널이란?\n- 크기가 상수\n- 위상의 변화가 linear -> 노이즈 감지 때문\n\n- u(t)를 받아서 다시 modulation을 하면 됨\n    - 이게 왜 그러냐면 modulation을 다시 할 때\n    - 원래 신호 성분이 0으로 가기 때문\n    - 요걸 LPF 같은 걸로 빼내면 된다\n\n- 하지만 time delay가 phase의 형태로 나타남\n    다를 경우는 문제가 없지만, (상수임)\n    phi = 90이라면 ? (cos phi = 0)\n    요걸 phase-coherent라고 함",
			"lineHeight": 1.25
		},
		{
			"id": "2iXVLwFUlvkIhKBbSj4Yv",
			"type": "freedraw",
			"x": 358.6835080711576,
			"y": -2573.1181033169623,
			"width": 20.432634906715407,
			"height": 8.828757476553164,
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
			"seed": 84986734,
			"version": 89,
			"versionNonce": 1606339250,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710337330560,
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
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				20.432634906715407,
				8.341826894228689
			]
		},
		{
			"id": "8tN-5_ucHUm0CfOe8pgNY",
			"type": "freedraw",
			"x": 557.0273474893789,
			"y": -2443.986216780509,
			"width": 135.07215642402855,
			"height": 44.71596621909839,
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
			"seed": 1901197230,
			"version": 78,
			"versionNonce": 2017531698,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710337554074,
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
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				-9.433870379690575,
				9.854690071153982
			]
		},
		{
			"id": "KibxUpXJ",
			"type": "text",
			"x": 473.4059716486091,
			"y": -2501.988125409377,
			"width": 104.87997436523438,
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
			"seed": 1377093998,
			"version": 43,
			"versionNonce": 1253367470,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710337560251,
			"link": null,
			"locked": false,
			"text": "파워도 손실나네",
			"rawText": "파워도 손실나네",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 14,
			"containerId": null,
			"originalText": "파워도 손실나네",
			"lineHeight": 1.25
		},
		{
			"id": "biOHXWpg",
			"type": "text",
			"x": -957.2080343881416,
			"y": -2239.5242919921875,
			"width": 360.0798645019531,
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
			"seed": 1141428398,
			"version": 325,
			"versionNonce": 737656558,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710337805072,
			"link": null,
			"locked": false,
			"text": "PLL\n- pilot signal이 필요하지 않은 사인함수를 보내는 것\n\nPilot tone = pilot signal\n- referene가 되는 시그널\n- 노이즈를 잡기 위한 기준이 되는 시그널\n- 송수신 측 모두 알고 있음",
			"rawText": "PLL\n- pilot signal이 필요하지 않은 사인함수를 보내는 것\n\nPilot tone = pilot signal\n- referene가 되는 시그널\n- 노이즈를 잡기 위한 기준이 되는 시그널\n- 송수신 측 모두 알고 있음",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "right",
			"verticalAlign": "top",
			"baseline": 134,
			"containerId": null,
			"originalText": "PLL\n- pilot signal이 필요하지 않은 사인함수를 보내는 것\n\nPilot tone = pilot signal\n- referene가 되는 시그널\n- 노이즈를 잡기 위한 기준이 되는 시그널\n- 송수신 측 모두 알고 있음",
			"lineHeight": 1.25
		},
		{
			"id": "4xwsbrAu",
			"type": "text",
			"x": 590.5500489706344,
			"y": -2245.2072126913877,
			"width": 399.4078674316406,
			"height": 200,
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
			"seed": 2031926322,
			"version": 510,
			"versionNonce": 361491442,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710337992772,
			"link": null,
			"locked": false,
			"text": "DSB-SC의 강점인 부분\n\nEnvelope detector\n- 다이오드와 RC로 이루어진 회로를 이용해 신호를 detect\n- 회로로 통과한 신호 (양수 부분만 존재)를 외곽선만 따옴\n- 편지봉투 뜯는거 같다해서 envelope\n\n- 다만 RC값 설정하는 게 귀찮음\n    - 너무크면 신호를 못따라가고\n    - 너무 작으면 신호가 뭔지 알 수가 없음 (왜곡)",
			"rawText": "DSB-SC의 강점인 부분\n\nEnvelope detector\n- 다이오드와 RC로 이루어진 회로를 이용해 신호를 detect\n- 회로로 통과한 신호 (양수 부분만 존재)를 외곽선만 따옴\n- 편지봉투 뜯는거 같다해서 envelope\n\n- 다만 RC값 설정하는 게 귀찮음\n    - 너무크면 신호를 못따라가고\n    - 너무 작으면 신호가 뭔지 알 수가 없음 (왜곡)",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 194,
			"containerId": null,
			"originalText": "DSB-SC의 강점인 부분\n\nEnvelope detector\n- 다이오드와 RC로 이루어진 회로를 이용해 신호를 detect\n- 회로로 통과한 신호 (양수 부분만 존재)를 외곽선만 따옴\n- 편지봉투 뜯는거 같다해서 envelope\n\n- 다만 RC값 설정하는 게 귀찮음\n    - 너무크면 신호를 못따라가고\n    - 너무 작으면 신호가 뭔지 알 수가 없음 (왜곡)",
			"lineHeight": 1.25
		},
		{
			"id": "u2fjfK8-umTKUBqdO5ExY",
			"type": "freedraw",
			"x": 615.2932538091784,
			"y": -2073.713812966632,
			"width": 54.06631689694609,
			"height": 11.813209010127594,
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
			"seed": 403181102,
			"version": 16,
			"versionNonce": 1430320178,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710337972149,
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
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				-54.06631689694609,
				11.540600786814593
			]
		},
		{
			"id": "OagAZQ0Vh2DCjN4rFjclH",
			"type": "freedraw",
			"x": 571.3389569798553,
			"y": -2072.8572834075258,
			"width": 14.685030622782847,
			"height": 17.458999376716747,
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
			"seed": 2114908718,
			"version": 17,
			"versionNonce": 1749318130,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710337972601,
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
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				8.06715402929683,
				17.458999376716747
			]
		},
		{
			"id": "gNWl5GGNn_dRCNMWCb0Dl",
			"type": "freedraw",
			"x": 614.0721982558916,
			"y": -2052.5916976573017,
			"width": 61.06652474817474,
			"height": 106.5945329492572,
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
			"seed": 810475630,
			"version": 20,
			"versionNonce": 1420676338,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710337973272,
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
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				-61.06652474817474,
				106.5945329492572
			]
		},
		{
			"id": "WkckquQBYSOlaorynifRJ",
			"type": "freedraw",
			"x": 549.4759195064557,
			"y": -1961.4675545629318,
			"width": 17.989555649070326,
			"height": 17.4619922842669,
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
			"seed": 1894030702,
			"version": 13,
			"versionNonce": 1119822770,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710337973617,
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
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				17.989555649070326,
				16.323926506443286
			]
		},
		{
			"id": "hJ3Gm_280ePejJyvA2TCa",
			"type": "freedraw",
			"x": 321.11291378227617,
			"y": -1849.9682041384003,
			"width": 251.92127168860628,
			"height": 75.71893775138369,
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
			"seed": 1183345326,
			"version": 75,
			"versionNonce": 2106230514,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710337976925,
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
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				-5.100523192716764,
				14.030040414480482
			]
		},
		{
			"id": "fO9vQ0Fk",
			"type": "text",
			"x": -1032.166277436887,
			"y": -1788.2862057070342,
			"width": 437.5838623046875,
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
			"seed": 159502510,
			"version": 254,
			"versionNonce": 1557030510,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710338080324,
			"link": null,
			"locked": false,
			"text": "DSB-SC의 단점\n- 0을 사이로 왔다갔다하면 어딜 선택해야할지 모름\n\n그래서 conventional AM (DSB-LC)는 신호를 모두 양으로 옮김",
			"rawText": "DSB-SC의 단점\n- 0을 사이로 왔다갔다하면 어딜 선택해야할지 모름\n\n그래서 conventional AM (DSB-LC)는 신호를 모두 양으로 옮김",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "right",
			"verticalAlign": "top",
			"baseline": 74,
			"containerId": null,
			"originalText": "DSB-SC의 단점\n- 0을 사이로 왔다갔다하면 어딜 선택해야할지 모름\n\n그래서 conventional AM (DSB-LC)는 신호를 모두 양으로 옮김",
			"lineHeight": 1.25
		},
		{
			"id": "WdNIz_u0wFS2rjuEOYiyQ",
			"type": "freedraw",
			"x": -585.0870658473888,
			"y": -1777.7714620285287,
			"width": 459.2688922303348,
			"height": 87.1616856794767,
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
			"seed": 12841458,
			"version": 67,
			"versionNonce": 2010871918,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710338043874,
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
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				459.2688922303348,
				52.353333869603375
			]
		},
		{
			"id": "kjYqXLKRQKYkaLYJYzzTt",
			"type": "freedraw",
			"x": -135.37305633509652,
			"y": -1733.5237841684036,
			"width": 27.14430184580806,
			"height": 13.914458383066858,
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
			"seed": 237670194,
			"version": 18,
			"versionNonce": 2070943982,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1710338044490,
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
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				27.14430184580806,
				-3.144455199591448
			]
		},
		{
			"id": "klB9UgUm",
			"type": "text",
			"x": 599.4637219897694,
			"y": -6312.692110253825,
			"width": 8,
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
			"seed": 1017404338,
			"version": 13,
			"versionNonce": 653947694,
			"isDeleted": true,
			"boundElements": null,
			"updated": 1710337036351,
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
			"id": "GcA-luDFjCV12vhF6eXne",
			"type": "freedraw",
			"x": -515.354277561943,
			"y": -5107.003765572208,
			"width": 17.44243203032852,
			"height": 2.3945170464266994,
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
			"seed": 1454022194,
			"version": 37,
			"versionNonce": 1495138222,
			"isDeleted": true,
			"boundElements": null,
			"updated": 1710337036351,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.29308891885034427,
					-0.4892772357334252
				],
				[
					1.0471333943628451,
					-0.8155025190972083
				],
				[
					2.021035018554585,
					-0.8155025190972083
				],
				[
					3.0421933872544287,
					-1.1133252043073298
				],
				[
					3.1745770071436255,
					-1.1133252043073298
				],
				[
					3.439303787380709,
					-1.1133252043073298
				],
				[
					4.32573188278252,
					-1.1133252043073298
				],
				[
					5.675462188255267,
					-1.1133252043073298
				],
				[
					7.401021175009134,
					-1.1133252043073298
				],
				[
					8.53093479134418,
					-1.3307952400355134
				],
				[
					8.79804868453158,
					-1.4655659728759929
				],
				[
					8.930391844879352,
					-1.4655659728759929
				],
				[
					9.062775464768663,
					-1.4655659728759929
				],
				[
					9.329889357956063,
					-1.4655659728759929
				],
				[
					10.083933833468507,
					-1.600296246173457
				],
				[
					12.296463862089013,
					-2.259786773128326
				],
				[
					12.695920915624129,
					-2.259786773128326
				],
				[
					12.963034808811528,
					-2.3945170464266994
				],
				[
					13.095418428700839,
					-2.3945170464266994
				],
				[
					13.362532321888239,
					-2.3945170464266994
				],
				[
					13.896760108262981,
					-2.3945170464266994
				],
				[
					14.161486888500065,
					-2.3945170464266994
				],
				[
					14.428600781687464,
					-2.3945170464266994
				],
				[
					15.182645257199908,
					-2.3945170464266994
				],
				[
					15.80195945941432,
					-1.966657394736103
				],
				[
					16.775861083606003,
					-1.805952095775865
				],
				[
					17.310088869980802,
					-1.6735684758859861
				],
				[
					17.44243203032852,
					-1.6735684758859861
				],
				[
					17.44243203032852,
					-1.6735684758859861
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				17.44243203032852,
				-1.6735684758859861
			]
		},
		{
			"id": "hPunSyLjvjMPaCehV_yvA",
			"type": "freedraw",
			"x": -515.3968409996335,
			"y": -5109.0649769155025,
			"width": 13.57292193784906,
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
			"seed": 577441326,
			"version": 23,
			"versionNonce": 1334155826,
			"isDeleted": true,
			"boundElements": null,
			"updated": 1710337036351,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0.2671138931873429,
					0
				],
				[
					0.6665709467224588,
					0
				],
				[
					2.0635984562450176,
					0
				],
				[
					4.164986124279835,
					0
				],
				[
					6.642283392678905,
					0
				],
				[
					7.992013698151709,
					0
				],
				[
					10.09340136618664,
					0
				],
				[
					11.355698602410996,
					0
				],
				[
					11.488041762758769,
					0
				],
				[
					12.022269549133568,
					0
				],
				[
					12.556497335508311,
					0
				],
				[
					13.175811537722723,
					0
				],
				[
					13.44053831795975,
					0
				],
				[
					13.57292193784906,
					0
				],
				[
					13.57292193784906,
					0
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				13.57292193784906,
				0
			]
		},
		{
			"id": "6Ircg8c4f0DeflllQmxhi",
			"type": "freedraw",
			"x": -454.44870901602224,
			"y": -4646.200397475464,
			"width": 9.842835425485475,
			"height": 9.41736288674656,
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
			"seed": 1425901806,
			"version": 24,
			"versionNonce": 1244948082,
			"isDeleted": true,
			"boundElements": null,
			"updated": 1710337036351,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.5673236913470987,
					-0.7587782418722782
				],
				[
					-1.0566009270809786,
					-0.7587782418722782
				],
				[
					-1.8153791689525747,
					-0.7587782418722782
				],
				[
					-3.545712381607075,
					-0.7587782418722782
				],
				[
					-5.457992152526344,
					0.6618776399045601
				],
				[
					-8.523854371576249,
					3.7206189796452236
				],
				[
					-9.516650601662889,
					6.325525642032517
				],
				[
					-9.842835425485475,
					7.299427266224484
				],
				[
					-9.842835425485475,
					7.6988843197596
				],
				[
					-9.842835425485475,
					7.965998212946943
				],
				[
					-9.710492265137702,
					8.233112106134286
				],
				[
					-9.310994752061049,
					8.365495726024164
				],
				[
					-8.556950276548548,
					8.497838886371937
				],
				[
					-7.074836351186491,
					8.658584644874281
				],
				[
					-5.944963194392926,
					8.658584644874281
				],
				[
					-5.6778493012055264,
					8.658584644874281
				],
				[
					-5.6778493012055264,
					8.658584644874281
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				-5.6778493012055264,
				8.658584644874281
			]
		},
		{
			"id": "IKJUF7Qzu0UtBdi1KHDpr",
			"type": "freedraw",
			"x": -974.4061521058104,
			"y": -4376.050501210673,
			"width": 48.33021706405896,
			"height": 46.88593281002886,
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
			"seed": 1346770606,
			"version": 39,
			"versionNonce": 1259332530,
			"isDeleted": true,
			"boundElements": null,
			"updated": 1710337036351,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-0.2694605465961786,
					0.26707343364614644
				],
				[
					-2.6971139575367715,
					2.689993078227417
				],
				[
					-4.930885245461013,
					4.174453656998594
				],
				[
					-7.573621579180099,
					6.379862806309575
				],
				[
					-13.119087260496372,
					9.147861880608616
				],
				[
					-23.654529347679613,
					13.29868716535293
				],
				[
					-29.143270751769478,
					14.511340544118866
				],
				[
					-29.547481801434515,
					14.511340544118866
				],
				[
					-30.84993513262839,
					13.045774571242873
				],
				[
					-32.145287814283506,
					8.946939797366213
				],
				[
					-34.57763453204166,
					3.4581983932757794
				],
				[
					-35.84935884144272,
					-0.0354830179221608
				],
				[
					-38.30535416122575,
					-11.01294559633152
				],
				[
					-38.30535416122575,
					-13.0056387060431
				],
				[
					-38.30535416122575,
					-16.61515578464423
				],
				[
					-37.77112637485095,
					-19.848823952193925
				],
				[
					-36.74050047343292,
					-22.706663438462783
				],
				[
					-35.192214967896916,
					-25.564482694960134
				],
				[
					-31.289588740674503,
					-29.77441936988089
				],
				[
					-28.81233193181697,
					-31.26361371501116
				],
				[
					-25.20754861957471,
					-32.08856353705687
				],
				[
					-19.23659016974807,
					-32.374592265909996
				],
				[
					-17.246263943215695,
					-32.374592265909996
				],
				[
					-11.275325723159881,
					-32.09093042023596
				],
				[
					-3.800971629125911,
					-29.39620357564945
				],
				[
					-1.3639316045502028,
					-27.87391332554762
				],
				[
					4.198082029252191,
					-23.212508856453496
				],
				[
					7.687070133632915,
					-16.77353465996748
				],
				[
					8.599473254697614,
					-14.031510611331214
				],
				[
					9.757749009645863,
					-9.675049706755999
				],
				[
					10.024862902833206,
					-7.793458498088512
				],
				[
					10.024862902833206,
					-7.1741442958737025
				],
				[
					10.024862902833206,
					-7.041780905755331
				],
				[
					10.024862902833206,
					-7.041780905755331
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				10.024862902833206,
				-7.041780905755331
			]
		},
		{
			"id": "yNi5AuDhV4Qkkys9H3h5I",
			"type": "freedraw",
			"x": -980.9893241083128,
			"y": -4372.344083530104,
			"width": 116.70777282083418,
			"height": 46.97338610904808,
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
			"seed": 299965166,
			"version": 35,
			"versionNonce": 420931694,
			"isDeleted": true,
			"boundElements": null,
			"updated": 1710337036351,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					0.1323836198889694
				],
				[
					-1.784670376930535,
					1.4773801590026778
				],
				[
					-2.2739880722059524,
					1.6381259175050218
				],
				[
					-10.12888438410937,
					4.027909197572626
				],
				[
					-19.74716935409799,
					5.351624017841459
				],
				[
					-32.74568718083208,
					5.689663487331927
				],
				[
					-55.9983723620262,
					5.339809831713865
				],
				[
					-71.24959654212103,
					2.2196104483882664
				],
				[
					-83.15841753680184,
					-2.2030624959024863
				],
				[
					-90.30889300088029,
					-6.408265404464146
				],
				[
					-94.17842332313057,
					-12.608487846376192
				],
				[
					-94.18079020631012,
					-17.345551658133445
				],
				[
					-91.39861006270439,
					-22.58609400470141
				],
				[
					-84.53885663429651,
					-27.80772151560359
				],
				[
					-73.72211958461935,
					-32.20201209151037
				],
				[
					-54.60846573181311,
					-36.30084686538703
				],
				[
					-41.617028324846956,
					-37.329085653855145
				],
				[
					-28.999072945753028,
					-37.329085653855145
				],
				[
					-16.754599594531328,
					-36.650680291234494
				],
				[
					-5.599843305133845,
					-33.27044743448914
				],
				[
					8.533281444753015,
					-24.18873690428427
				],
				[
					15.49466924148669,
					-16.898797400548574
				],
				[
					20.040258272948336,
					-9.762482776005527
				],
				[
					22.222039050005264,
					-3.5291644291210105
				],
				[
					22.52698261452406,
					3.1934716130381275
				],
				[
					20.640677869267734,
					6.152965697403488
				],
				[
					16.938953495517353,
					8.143291923935976
				],
				[
					11.82608123225009,
					9.341744003623717
				],
				[
					3.968797807396413,
					9.644300455192933
				],
				[
					3.968797807396413,
					9.644300455192933
				]
			],
			"pressures": [],
			"simulatePressure": true,
			"lastCommittedPoint": [
				3.968797807396413,
				9.644300455192933
			]
		},
		{
			"id": "ufCQSv34yyQTXh1vuNfbF",
			"type": "freedraw",
			"x": 751.433219270851,
			"y": -5740.798498389821,
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
			"seed": 1162472878,
			"version": 5,
			"versionNonce": 403667634,
			"isDeleted": true,
			"boundElements": null,
			"updated": 1710337036351,
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
			"id": "1qL3BSyYs7OQTrVkj7WPO",
			"type": "freedraw",
			"x": 751.433219270851,
			"y": -5740.798498389821,
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
			"seed": 103900270,
			"version": 4,
			"versionNonce": 392058158,
			"isDeleted": true,
			"boundElements": null,
			"updated": 1710337036167,
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
			"id": "HIxIyHTk",
			"type": "text",
			"x": -661.7311667123604,
			"y": -2215.6674194335938,
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
			"seed": 1572921458,
			"version": 3,
			"versionNonce": 716538926,
			"isDeleted": true,
			"boundElements": null,
			"updated": 1710337704379,
			"link": null,
			"locked": false,
			"text": "",
			"rawText": "",
			"fontSize": 16,
			"fontFamily": 1,
			"textAlign": "right",
			"verticalAlign": "top",
			"baseline": 14,
			"containerId": null,
			"originalText": "",
			"lineHeight": 1.25
		},
		{
			"id": "Pq5rD2yq",
			"type": "text",
			"x": 848.9375239057666,
			"y": -2123.8651531515184,
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
			"seed": 1060776434,
			"version": 2,
			"versionNonce": 1419915374,
			"isDeleted": true,
			"boundElements": null,
			"updated": 1710337933631,
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
		"scrollX": 564.8036494699791,
		"scrollY": 2234.3008673508166,
		"zoom": {
			"value": 1.2032026242696483
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