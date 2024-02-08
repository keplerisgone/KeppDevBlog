---
tags:
  - Incomplete
---
## 반복문이란?

우리의 귀찮음을 해소해주는 
## for

**for**은 *일정 기준을 만족하는 상황*에서 반복을 시행하도록 하는 문이다.
`for (initiation ; condition ; iteration)` 의 형식으로 이루어져 있으며, 가운데의 condition을 만족한다면 for 문 내의 코드를 반복해서 시행한다. 아래는 5번 `Hello World`를 출력하는 코드이다.

```cpp
for (int i=0 ; i<5 ; i++){
	std::cout << "Hello World\n";
}
```

for 문 내부의 코드가 실행될 때마다 `i`가 1씩 증가하며, i가 5가 되는 순간 

### 범위 기반 for문

간단히 설명하자면 *특정 조건을 이용하는* 일반 for문과는 달리 *반복 가능한 구조에 대하여 알아서 반복해주는* for_each같은 역할을 한다.