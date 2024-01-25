---
tags:
  - Incomplete
sticker: lucide//airplay
---
함수형 프로그래밍은 뭘까?
> 함수형 프로그래밍은 pure function의 합성이다.

예를 들어, 일반적인 절차 지향 프로그래밍은 "챡챡챡 이런걸 수행해줘"라면 함수형 프로그래밍은 *이런 인풋을 받아서 저런 아웃풋을 내는 함수1*과 *다른 함수 2*를 받아 연결하는 방식에 가깝다. 여기서 중요한 점은 이 함수들 간의 연관성이 없다는 말이다. 일단 **pure function**이 뭔지부터 알아보자.

## Overall Structure

### Purity

pure function이란 말 그대로 순수한 함수를 말한다. 여기서 말하는 함수의 순수성이 뭐냐면...

1. SIde Effect가 존재하지 않는다
2. Referential Transparency를 가짐

이 두 가지를 핵심으로 본다. 

Side effect는 [[함수의 Side Effect]]를 참고.

Referential Transparency는 [[참조 투명성]]을 참고.
### Immutabiliy

불변성 -> 함수를 사용할 때 

### First Class Function

함수를 인자, 변수로 사용가능함
python에서의 map, 람다 함수 사용 (어렵다!)

## Lambda Calculus


## Category Theory


## FP Fact Checking 


## Effect Handling Basics

sum이랑 똑같은 함수인디

- [?] 재귀를 짤 때 뭐 순수 재귀로 짜면 스택이 안 쌓인다구요?? 컴파일러에서 알아서 짜준다구요??
- [?] 근데 게임 같은 분야에서는 이게 가능할까요 밥먹듯이 쓰는게 전역변수인데 (싱글톤 패턴같은 것도 있음)

fmap의 타입 거시기가 아니라 fmap() 자체의 그거를 말하는 거겠지?? 그래서 fmap()에다가 변수로 주는 건가봐

전혀 직관적이지 않아요!