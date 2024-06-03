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

![|575](https://i.imgur.com/TI1NrLw.png)

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
	- `# of cache block` : $2^n$ blocks
	- `cache block size` : $2^m$ doublewords = $2^{m+3}$ bytes
	- `total cache size` : $2^{n}\times 2^{m+3}$ bytes
- memory address는 다음과 같은 정보를 가진다.
	- `block offset` : $m+3$
		- 요거는 cache block의 byte size만큼 memory를 차지하기 때문..
	- `index` : $n$
	- `tag` : $64-(n+m+3)$
- total bits in cache는 $2^{n}\times (\text{block size}+\text{tag size}+\text{valid bit})= 2^{n}\times [2^{m}\times 64 + 64 - (n+m+3)+1]$가 되지만, 실제 cache size는 cache block의 byte로만 판정한다.

![|525](https://i.imgur.com/EMPvwAg.png)

- 참고 ) 데이터 사이즈


## Example

![|600](https://i.imgur.com/uMovHYl.png)

![|600](https://i.imgur.com/36rigfO.png)

# Data consistency and Write-Through Cache

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


