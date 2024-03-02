---
tags:
  - Incomplete
  - CPP
---


# Summary

## 반복문이란?

우리의 귀찮음을 해소해주는 좋은 것이다.

# Contents

## for

**for**은 *일정 기준을 만족하는 상황*에서 반복을 시행하도록 하는 문이다.
`for (initiation ; condition ; iteration)` 의 형식으로 이루어져 있으며, 가운데의 condition을 만족한다면 for 문 내의 코드를 반복해서 시행한다. 아래는 5번 `Hello World`를 출력하는 코드이다.

```cpp
for (int i=0 ; i<5 ; i++){
	std::cout << "Hello World\n";
}
```

for 문 내부의 코드가 실행될 때마다 `i`가 1씩 증가하며, i가 5가 되는 순간 반복이 종료된다.

### 범위 기반 for문

간단히 설명하자면 *특정 조건을 이용하는* 일반 for문과는 달리 *반복 가능한 구조에 대하여 알아서 반복해주는* for_each같은 역할을 한다.

```cpp 
string str = "Hello, World!";
for (char c : str){
	std::cout << c << "\n";
}
```

반복 가능한 것들을 넣으면 하나하나 원소에 대해 반복문을 시행한다.

## while 문

*while*은 *특정 조건을 만족하면 해당 명령어를 반복 수행하는 반복문*이다. for문과 비슷해보이지만, 선언시에 시행문이 없다는 것이 다르다. 

```cpp
while (i <= 10){
	std::cout << i << "\n";
	i++;
}
```

주로 길이가 정해지지 않은 벡터나 리스트에 대해서 반복할 때 쓰이지만, 이럴떄는 범위 기반 for문을 쓰는 것이 훨씬 낫다.

## switch 문

switch 문은 특정 변수의 값에 따라 명령을 시행하는 조건문이다. 그럼 여기 있으면 안되잖아
# Reference

