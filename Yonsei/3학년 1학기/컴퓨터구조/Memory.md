# Ideal Architecture

**Ideal Architecture**는 다음과 같은 특징을 지닌다. 

![|237](https://i.imgur.com/RRkSrvA.png)

- **Ideal processor**
	- pipeline stall이 없음 (perfect data flow + perfect control flow): 이거는 perfect branch prediction으로 봐도 된다
	- execution latency가 없음 (zero cycle)
- **Ideal memory**
	- No access latency (zero cycle)
	- Intifity capacity: 용량이 무한
	- Infinite bandwidth: 한 번에 보내는 양에 제한 X
	- No silicon cost: 크기 상관 없음

# Locality Principles

![|450](https://i.imgur.com/TI1NrLw.png)

- memory system은 **locality principles**에 기반해 동작한다.
- **Temporal locality**는 최근 접근한 데이터에 접근할 가능성이 높다는 경향을 의미한다
- **Spatial locality**는 특정 메모리 영역의 데이터를 연속적으로 사용할 가능성이 높다는 것을 의미한다.
- 위 코드에서는 `a[i]`, `a[i+1]`의 접근에서 위 경향을 볼 수 있다.

# Real-World Memory Problems

- 큰 메모리는 느리고, 작은 메모리는 빠르다. bandwidth가 크면 비싸다.
- 메모리의 계층 구조는 각각의 장점을 살리기 위해 다음과 같은 구조를 가지고 있다.

![](https://i.imgur.com/ocVLL6A.png)

- **Register**는 직접 processor가 사용하는 저장 공간이다. 제일 작지만 제일 빠르다.
- **SRAM cache**는 자주 사용하는 데이터가 저장되는 공간이다. register의 크기를 극복한다. register에 접근하는데 100cycle 정도가 걸린다.
	- **L1, L2, L3 cache**로 나뉜다. L4는 DRAM에 있는 편...
- **DRAM memory**는 적당히 background에 있는 데이터를 저장하는 곳이다.
- **HDD/SDD storage**는 모든 데이터가 저장되는 곳이다.

![](https://i.imgur.com/3jDe8Kc.png)

- processor의 core는 register + L1 cache로 이루어져 있다.
	- 그 아래는 L2, L3가 존재한다. L2는 core마다 따로 있고, L3는 공유한다.
	- 그 아래는 **MC**(Memory Controller)가 있다. 이는 DRAM을 조절한다.
	- DRAM은 아무것도 혼자서 할 수 있는게 없기 때문에 MC가 cycle, latency 정보를 모두 준다.

# Multi-Level Memory Hierarchy

- 각각의 data element는 block이라고 한다.

![](https://i.imgur.com/LNjfAPa.png)

- upper-level memory에 data가 이동하는 방식은 move가 아닌 **copy**이다.

# Cache Access: Hit or Miss

- **cache hit**: cache에 접근하고자 하는 데이터가 있을 경우를 말한다.
- **cache miss**: 반대로 없는 경우. lower-memory에서 데이터를 뽑아온다.

![|475](https://i.imgur.com/lNKNy2K.png)

- **hit rate**는 총 cache accesses에 대해 cache hit이 일어난 비율이다
	- **hit time**은 cache에 접근하는 시간을 나타낸다. cycle 단위이다.
- **miss rate**는 총 cache accesses에 대해 cache miss이 일어난 비율이다
	- **miss time**은 cache에서 lower-level memory에 접근하는데 걸린 시간을 나타낸다.
- 데이터가 cache에 존재하는지, 어느 block에 데이터가 있는지를 판단해야 한다.

# Direct-Mapped Cache and Indexing

![|600](https://i.imgur.com/J0gWShc.png)

- **direct-mapped cache**는 cache와 memory간의 저장 방식을 나타내는 무언가이다.
- cache는 모든 memory를 저장하기에는 부족하기 때문에, 특정한 방식에 따라 memory의 data를 저장한다.
- memory의 data가 저장되는 **location**은 뒤의 *index*에 의해 결정된다. 
	- `cache_index = block_address % num_cache_entries`
- 나머지 bit는 **tag**가 되며, 이는 cache에 data가 저장되어있는지 판단하는 기준이 된다.
- **valid bit**는 cache block에 존재하는 bit로, data의 유무를 알린다.
- 아래는 판단 예시이다.

![|550](https://i.imgur.com/FRHTQSo.png)

## Direct-Mapped Cache Organization

- cache의 정보가 다음과 같을 때..
	- `# of cache block`: $2^n$ blocks
	- `cache block size`: $2^m$ doublewords = $2^{m+3}$ bytes
	- `total cache size`: $2^{n}\times 2^{m+3}$ bytes
- memory address는 다음과 같은 정보를 가진다.
	- `block offset`: $m+3$
		- 요거는 cache block의 byte size만큼 memory를 차지하기 때문..
	- `index`: $n$
	- `tag`: $64-(n+m+3)$
- total bits in cache는 $2^{n}\times (\text{block size}+\text{tag size}+\text{valid bit})= 2^{n}\times [2^{m}\times 64 + 64 - (n+m+3)+1]$가 되지만, 실제 cache size는 cache block의 byte로만 판정한다.

![|525](https://i.imgur.com/EMPvwAg.png)

- [ ] 참고) 데이터 사이즈

## Example

![|600](https://i.imgur.com/uMovHYl.png)

![|600](https://i.imgur.com/36rigfO.png)

# Data Consistency and Write-Through Cache

- `load` 명령은 다른 instruction이 dependency를 가질 수 있기 때문에 stall을 일으킬 수 있어 performance에 큰 하자를 일으킨다.
- `store` 명령은 dependency를 가지지 않기 때문에 영향을 안 받을 것 같지만, **consistency** 문제를 일으킬 수 있다.

![|600](https://i.imgur.com/sp2Cg9a.png)

- `ld`의 경우 MEM에서 data를 불러오는 경우 consistency 문제가 발생하지 않지만, `sd`의 경우 core에 저장된 data를 cache까지밖에 전달하지 않으며, 이러면 cache와 mem이 일치하지 않는 경우가 발생한다. 이를 **consistency problem**이라고 한다.
- 이를 해결하기 위해서는 **write-through cache**를 사용한다. 간단하게는 cache에 저장된 data를 MEM에 그대로 옮기는 것이다.

## Write-Through Cache and Write Buffer

- 하지만 위에서 배웠듯이 cache-MEM 접근은 엄청 오래 걸린다. (100cycle 정도)
- 이걸 기다리려면 큰 stall이 발생할 것이다.
- 일반적인 CPI가 1.0일 때, 10%가 store이고 cache->MEM이 100cycles가 걸린다면...
	- 전체 CPI는 $1.0 + (0.1 \times 100) = 11$이 되어버린다.

![|450](https://i.imgur.com/0H8yrQx.png)

- 위와 같이 **write buffer**를 이용하면 이를 기다리지 않고 프로그램을 진행시킬 수 있다. buffer에서도 트래픽이 발생할 수는 있지만 그건 프로그램 알 바가 아니다.
- write buffer의 사이즈는 latency gap을 없앨 만큼 커야 한다. 또한 cache-MEM 사이의 data 이동이 너무 많아진다는 단점이 있다.

## Write-Back Cache

- 위의 단점을 해결하기 위해서 **write-back cache**를 사용하기도 한다.
- 이는 *우선 cache에만 data를 저장하고 있다가*, cache가 다른 data로 교체될 때(drity) cache의 data를 memory에 씌우는 방식이다.
	- 따라서 cache와 memory가 항상 같은 data를 갖는다는 보장이 없다.
- cache에서 memory로 data가 이동한다는 것은 동일하기 때문에 write buffer는 여전히 필요하다.

> [!note]
> **dirty**는 더럽다는 뜻이 아니라 modify 되었다는 뜻이다.

# Handling Cache Misses

- cache miss는 원하는 data가 cache에 없을 경우이다. 이 때는 lower-level memory에 data를 요청한다.
	- valid bit가 0이거나 tag가 안맞음
- miss가 발생할 경우 data가 오는 걸 기다려야 하기 때문에 **stall**이 발생한다.
- 두 가지 경우로 나뉜다.
	- **instruction cache**: IF가 중지된다. insruction을 불러올 때까지 중지.
	- **data cache**: data가 cache에 생길 때까지 중지된다.

# Processor Execution Time

- multi-level memory에서 execution time은 다음과 같은 두 가지로 나눌 수 있다.
	- **pipeline execution cycles**
	- **memory stalls**
- 위 cycles에 clock period를 곱하면 총 execution time이 된다. 
- memory stall는 주로 cache miss에 의해 일어나기 때문에, memory stall은 $\text{read stall cycles}+\text{write stall cycles}$로 계산할 수 있다. 

$$\text{Read stall cycles} = \text{\# of reads} \times \text{read miss rate} \times \text{read miss penalty}$$
$$\text{Write stall cycles}= (\text{\# of writes}\times\text{write miss rate}\times\text{write miss penalty}) +\text{write buffer stalls}$$

- \# of OO 은 instruction의 개수를 말한다. `ld`나 `sd`.
- 보통 두 명령의 penalty는 동일하다.

## Memory Stall Cycles

- write buffer는 buffer가 다 찼을 때만 stall이 일어난다.
	- buffer가 적당히 크다고 가정하면 stall이 rare하게 일어난다.
- 따라서 write buffer stall은 무시하고, write과 read는 동일한 miss rate를 가지므로 **cache miss rate**를 다음과 같이 정의하자.

$$\text{Memory stall cycles}=\text{\# of memory accesses}\times\text{miss rate}\times\text{miss penalty}$$

## Example*

![|475](https://i.imgur.com/wETuk1T.png)

![|475](https://i.imgur.com/Mxd2a8S.png)

![|500](https://i.imgur.com/qYzftfH.png)

![|350](https://i.imgur.com/1PntAbk.png)

# Average Memory Access Time

- **AMAT**은 memory에 접근하는 평균 시간이다.

$$\text{AMAT}= \text{time for a hit}+(\text{miss rate}\times\text{miss penalty})$$

- 예를 들어 cache에 접근하는데 1cycle, miss penalty가 20cycle, miss rate가 5%면..
	- $1+(0.05\times 20)=2\text{cycles}$.

## Decreasing AMAT with Multi-Level Caches

- cache는 L1, L2, L3의 계층 구조로 이루어져 있다. (L4는 생각하지 말자)
- L1에 접근하는데 1cycle, miss rate는 2%.
- L2에 접근하는데 20cycle(아래에 있으니까), miss rate는 25%.
- 모든 miss penalty는 400cyles로 동일하다면...
	- $1 + (0.02\times (20+(0.25\times 400)))=3.4\text{cycles}$이다.
	- L1 단독은 $1 + (0.02 \times 400) = 9\text{cycles}$로, 계층을 활용하는 것이 이득이다.

# Cache Miss Types

- Cache Miss가 일어나는 이유에 따라 다음과 같이 나눌 수 있다.
- **Compulsory miss**: 데이터에 처음 접근할 경우 발생하는 miss. 필수적이다.
- **Capacity miss**: 캐시 용량이 적어서 발생하는 miss. 
	- 아래와 뭐가 다르겠냐 싶지만, 32kB cache에서 128kB array data에 접근하려는 경우를 말하는 것이다.
- **Conflict miss**: 같은 캐시 세트에 여러 데이터가 있어 발생하는 miss.
- compulsory miss와 capacity는 어쩔 수 없거나 hardware 문제이므로 conflict miss만 살펴보기로 하자.

## Reducing Conflict Misses

![](https://i.imgur.com/ffSKTEK.png)

- direct-mapped cache에서 다른 data가 존재하면 miss가 발생한다.
- 위와 같은 경우는 cache의 빈 공간이 많음에도 miss가 발생하는 안타까운 상태이다.
	- cache block은 8byte, 8-entry이다. (3bit offset, 3bit index)

## Set-Associative Cache

![|550](https://i.imgur.com/kn89bLo.png)

- cache를 n-way로 나눈다. 나눈 뒤의 각 block의 모음을 set이라고 한다.
- index는 $\text{block address}\  \% \ \text{\# of sets}$로 바뀐다.
- 이러면 하나의 인덱스에 여러 개의 데이터를 담을 수 있어 이득이다.

![](https://i.imgur.com/Z1StBI0.png)
- 위와 같이 n-way로 나눌 수 있다.
- data를 탐색하기 위해서는 하나의 index의 각 way를 모두 봐야한다.
- **direct**의 경우에는 data의 유무를 확인하기 위해 **tag comparison**만 진행하면 된다.
- **fully**의 경우 하나를 찾을 때마다 모든 way의 tag를 봐야하지만, 저장할 수 있는 data가 가장 많다.

![](https://i.imgur.com/VGHXdtc.png)

- 이렇게 way 수를 늘릴 때마다 index가 줄어드는 만큼 tag가 길어진다.

## Example

- cache는 4096 blocks이고, 각각은 2 doublewords (16byte) 이다. 
- memory address는 32bit이다.
- total number of tag bits in a direct-mapped, two-way, four-way, fullay-associative structure? (tag size를 구하는 거면 cache block을 곱해야 한다.)
	- $4096 = 2^{12}$, $16 = 2^4$, offset = 4 bit, index = 12 bit, tag = 16bit
	- two-way : offset = 4 bit, index = 11 bit, tag = 17 bit 

# Cache Block Replacement

- 위 cache map에서, 각 set이 모두 차있을 수도 있다. 이 때 다른 data가 사용될 경우, 이미 존재하는 cache block을 치워야 한다.
- 이 때 **Least Recently Used**(LRU) 방법을 사용한다. 즉, 가장 먼저 사용된 cache를 먼저 대체한다.
- two-way의 경우, 이를 나타내는 1bit가 사용된다.

# Cache-Aware Matrix Multiplication Example

![|600](https://i.imgur.com/EMSRgKA.png)

- Matrix 연산은 큰 메모리에 접근해야 하기 때문에 cache 성능에 큰 영향을 받는다.
- 일반적인 연산의 경우, 행~의 경우에는 4개의 cache block에 접근하지만, 열의 경우 16개의 cache block에 접근해야 하는 끔찍한 경우가 발생한다.

![|600](https://i.imgur.com/mzvv9VK.png)

- 따라서 위와 같이 block을 새로 나누어 연산을 진행한다. 
- Spatial locality : cache에 있는 data에 모두 접근.
- Temporal locality : 각각의 cache block이 여러 번 사용된다.
- cass miss가 감소하며, 메모리 효율을 증가시킬 수 있다.