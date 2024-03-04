---
annotation-target: PDFs/컴퓨터구조/1_computer_abstraction.pdf
---
# Introduction

## computer architecture

컴퓨터는 어떻게 만들어지나요
재료 - 소자 - 회로 - (기능을 하는) 논리 회로 - microarchitecture? (메모리 관리, CPU 구조 등등)
컴퓨터는 복잡한 계산기이다 <- 사실 처음부터 계산기로 시작함

비유가 맞나

traditional classes of computing systems

personal computers
good performance for single users (personal!!!)
	server computers? for anyone
Servers
	 large system <- many small computers - enable to run parallel, sizable workloads, many jobs (good)
	 security
	 reliability <- slow running speed
Supercomputers
	extremely large... servers
	PB 단위 살면서 처음본당
	<span style="background:#affad1">flash memory</span>
Embedded system
	wide range
	automobile! - navigation

Post-PC era

PMDs
	그래서 블루스택 돌리는게 그렇게 부담이었니
SoC
	asdf

New computing devices

Important concepts in computer achitecture

1.asfd
2.fu
3.ashfassddfj
	잘 짜여진 싱글스레드는 멀티스레드를 이긴다
4.fdshafg
5.drt
6.ghgh
7.ghjfj

translating 

under the hood: processor components




>%%
>```annotation-json
>{"created":"2024-03-04T04:49:47.545Z","text":"휴대폰이 컴퓨터보다 이제 빨라용","updated":"2024-03-04T04:49:47.545Z","document":{"title":"1_computer_abstraction.pdf","link":[{"href":"urn:x-pdf:51af6068cd596a9f4afd1219e5c73b0c"},{"href":"vault:/PDFs/%EC%BB%B4%ED%93%A8%ED%84%B0%EA%B5%AC%EC%A1%B0/1_computer_abstraction.pdf"}],"documentFingerprint":"51af6068cd596a9f4afd1219e5c73b0c"},"uri":"vault:/PDFs/%EC%BB%B4%ED%93%A8%ED%84%B0%EA%B5%AC%EC%A1%B0/1_computer_abstraction.pdf","target":[{"source":"vault:/PDFs/%EC%BB%B4%ED%93%A8%ED%84%B0%EA%B5%AC%EC%A1%B0/1_computer_abstraction.pdf","selector":[{"type":"TextPositionSelector","start":601,"end":638},{"type":"TextQuoteSelector","exact":"our daily lives depend highly on them","prefix":"vices are everywhere today, and ","suffix":".•The computing industry has tre"}]}]}
>```
>%%
>*%%PREFIX%%vices are everywhere today, and%%HIGHLIGHT%% ==our daily lives depend highly on them== %%POSTFIX%%.•The computing industry has tre*
>%%LINK%%[[#^p7jzl2bivx8|show annotation]]
>%%COMMENT%%
>휴대폰이 컴퓨터보다 이제 빨라용
>%%TAGS%%
>
^p7jzl2bivx8


>%%
>```annotation-json
>{"created":"2024-03-04T04:50:41.597Z","text":"컴퓨터를 처음부터 만든다면 어떻게 할 것인가?\n\n1. Materials and Physics\n- silicon\n- metal\n- 집 지을때 진흙과 같은 것\n\n2. Decives\n- Active / Passive\n- 트랜지스터\n- 집 지을 때 파이프, 벽돌과 같은 것\n\n3. Circuits\n- Device를 연결해 만든 무언가\n\n4. Logic gate & register\n- 회로가 특정한 기능을 가지게 된 것\n- 블록으로 사용\n\n5. microarchitecture\n- 게이트가 여러개 모인거\n- state를 저장가능\n\n... OS, Compiler 등은 software level","updated":"2024-03-04T04:50:41.597Z","document":{"title":"1_computer_abstraction.pdf","link":[{"href":"urn:x-pdf:51af6068cd596a9f4afd1219e5c73b0c"},{"href":"vault:/PDFs/%EC%BB%B4%ED%93%A8%ED%84%B0%EA%B5%AC%EC%A1%B0/1_computer_abstraction.pdf"}],"documentFingerprint":"51af6068cd596a9f4afd1219e5c73b0c"},"uri":"vault:/PDFs/%EC%BB%B4%ED%93%A8%ED%84%B0%EA%B5%AC%EC%A1%B0/1_computer_abstraction.pdf","target":[{"source":"vault:/PDFs/%EC%BB%B4%ED%93%A8%ED%84%B0%EA%B5%AC%EC%A1%B0/1_computer_abstraction.pdf","selector":[{"type":"TextPositionSelector","start":708,"end":737},{"type":"TextQuoteSelector","exact":"What is Computer Architecture","prefix":"s impacts on the world economy.3","suffix":"?4ApplicationsAlgorithmsProgramm"}]}]}
>```
>%%
>*%%PREFIX%%s impacts on the world economy.3%%HIGHLIGHT%% ==What is Computer Architecture== %%POSTFIX%%?4ApplicationsAlgorithmsProgramm*
>%%LINK%%[[#^2sxh6o2sc0d|show annotation]]
>%%COMMENT%%
>컴퓨터를 처음부터 만든다면 어떻게 할 것인가?
>
>1. Materials and Physics
>- silicon
>- metal
>- 집 지을때 진흙과 같은 것
>
>2. Decives
>- Active / Passive
>- 트랜지스터
>- 집 지을 때 파이프, 벽돌과 같은 것
>
>3. Circuits
>- Device를 연결해 만든 무언가
>
>4. Logic gate & register
>- 회로가 특정한 기능을 가지게 된 것
>- 블록으로 사용
>
>5. microarchitecture
>- 게이트가 여러개 모인거
>- state를 저장가능
>
>... OS, Compiler 등은 software level
>%%TAGS%%
>
^2sxh6o2sc0d


>%%
>```annotation-json
>{"created":"2024-03-04T05:11:53.108Z","updated":"2024-03-04T05:11:53.108Z","document":{"title":"1_computer_abstraction.pdf","link":[{"href":"urn:x-pdf:51af6068cd596a9f4afd1219e5c73b0c"},{"href":"vault:/PDFs/%EC%BB%B4%ED%93%A8%ED%84%B0%EA%B5%AC%EC%A1%B0/1_computer_abstraction.pdf"}],"documentFingerprint":"51af6068cd596a9f4afd1219e5c73b0c"},"uri":"vault:/PDFs/%EC%BB%B4%ED%93%A8%ED%84%B0%EA%B5%AC%EC%A1%B0/1_computer_abstraction.pdf","target":[{"source":"vault:/PDFs/%EC%BB%B4%ED%93%A8%ED%84%B0%EA%B5%AC%EC%A1%B0/1_computer_abstraction.pdf","selector":[{"type":"TextPositionSelector","start":1538,"end":1591},{"type":"TextQuoteSelector","exact":"deliver good performance to single users at low costs","prefix":"sktops and laptops.•They aim to ","suffix":", usually executing third-party "}]}]}
>```
>%%
>*%%PREFIX%%sktops and laptops.•They aim to%%HIGHLIGHT%% ==deliver good performance to single users at low costs== %%POSTFIX%%, usually executing third-party*
>%%LINK%%[[#^uqgs4ieeobb|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^uqgs4ieeobb


>%%
>```annotation-json
>{"created":"2024-03-04T05:13:02.647Z","updated":"2024-03-04T05:13:02.647Z","document":{"title":"1_computer_abstraction.pdf","link":[{"href":"urn:x-pdf:51af6068cd596a9f4afd1219e5c73b0c"},{"href":"vault:/PDFs/%EC%BB%B4%ED%93%A8%ED%84%B0%EA%B5%AC%EC%A1%B0/1_computer_abstraction.pdf"}],"documentFingerprint":"51af6068cd596a9f4afd1219e5c73b0c"},"uri":"vault:/PDFs/%EC%BB%B4%ED%93%A8%ED%84%B0%EA%B5%AC%EC%A1%B0/1_computer_abstraction.pdf","target":[{"source":"vault:/PDFs/%EC%BB%B4%ED%93%A8%ED%84%B0%EA%B5%AC%EC%A1%B0/1_computer_abstraction.pdf","selector":[{"type":"TextPositionSelector","start":1860,"end":1933},{"type":"TextQuoteSelector","exact":"processing sizable workloads (e.g., scientific applications) or many jobs","prefix":" networks.•They are oriented to ","suffix":" (e.g., web servers).•Servers ar"}]}]}
>```
>%%
>*%%PREFIX%%networks.•They are oriented to%%HIGHLIGHT%% ==processing sizable workloads (e.g., scientific applications) or many jobs== %%POSTFIX%%(e.g., web servers).•Servers ar*
>%%LINK%%[[#^z4pvlmczkok|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^z4pvlmczkok


>%%
>```annotation-json
>{"created":"2024-03-04T05:13:08.841Z","text":"그래서 게임은 못돌리지만 큰 업무를 처리가능\n호그와트 레거시는 못돌리지만 핑퐁 천억개 돌리기는 가능","updated":"2024-03-04T05:13:08.841Z","document":{"title":"1_computer_abstraction.pdf","link":[{"href":"urn:x-pdf:51af6068cd596a9f4afd1219e5c73b0c"},{"href":"vault:/PDFs/%EC%BB%B4%ED%93%A8%ED%84%B0%EA%B5%AC%EC%A1%B0/1_computer_abstraction.pdf"}],"documentFingerprint":"51af6068cd596a9f4afd1219e5c73b0c"},"uri":"vault:/PDFs/%EC%BB%B4%ED%93%A8%ED%84%B0%EA%B5%AC%EC%A1%B0/1_computer_abstraction.pdf","target":[{"source":"vault:/PDFs/%EC%BB%B4%ED%93%A8%ED%84%B0%EA%B5%AC%EC%A1%B0/1_computer_abstraction.pdf","selector":[{"type":"TextPositionSelector","start":1791,"end":1811},{"type":"TextQuoteSelector","exact":"many small computers","prefix":"er is a large system connecting ","suffix":" and accessed via networks.•They"}]}]}
>```
>%%
>*%%PREFIX%%er is a large system connecting%%HIGHLIGHT%% ==many small computers== %%POSTFIX%%and accessed via networks.•They*
>%%LINK%%[[#^t30nypajaps|show annotation]]
>%%COMMENT%%
>그래서 게임은 못돌리지만 큰 업무를 처리가능
>호그와트 레거시는 못돌리지만 핑퐁 천억개 돌리기는 가능
>%%TAGS%%
>
^t30nypajaps


>%%
>```annotation-json
>{"created":"2024-03-04T05:19:10.152Z","text":"안전 safety","updated":"2024-03-04T05:19:10.152Z","document":{"title":"1_computer_abstraction.pdf","link":[{"href":"urn:x-pdf:51af6068cd596a9f4afd1219e5c73b0c"},{"href":"vault:/PDFs/%EC%BB%B4%ED%93%A8%ED%84%B0%EA%B5%AC%EC%A1%B0/1_computer_abstraction.pdf"}],"documentFingerprint":"51af6068cd596a9f4afd1219e5c73b0c"},"uri":"vault:/PDFs/%EC%BB%B4%ED%93%A8%ED%84%B0%EA%B5%AC%EC%A1%B0/1_computer_abstraction.pdf","target":[{"source":"vault:/PDFs/%EC%BB%B4%ED%93%A8%ED%84%B0%EA%B5%AC%EC%A1%B0/1_computer_abstraction.pdf","selector":[{"type":"TextPositionSelector","start":2067,"end":2109},{"type":"TextQuoteSelector","exact":"Servers are built to havegreat reliability","prefix":"uting power, storage, and I/Os.•","suffix":" becausecrashes are more costlyt"}]}]}
>```
>%%
>*%%PREFIX%%uting power, storage, and I/Os.•%%HIGHLIGHT%% ==Servers are built to havegreat reliability== %%POSTFIX%%becausecrashes are more costlyt*
>%%LINK%%[[#^t6ko17f5ixq|show annotation]]
>%%COMMENT%%
>안전 safety
>%%TAGS%%
>
^t6ko17f5ixq
