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