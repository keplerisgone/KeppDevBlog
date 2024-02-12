---
tags:
  - Incomplete
  - Dev
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

pure function은 불변성을 가진다.
[[함수의 불변성]]은 해당 문서를 참고

### First Class Function

[[First Class Function]]

## Lambda Calculus

[[Lambda Calculus]]
## Category Theory

이건 그냥 수학이야긴데요
## FP Fact Checking 

프로그래밍의 특성상 input와 output은 존재할 수 밖에 없다. FP는 이렇게 input/output이 존재하는 impure한 부분을 제외한 모든 부분을 pure하게 작성한다는 점이 핵심이다.
따라서, *pure function*에 대해서만 다음과 같은 특징을 지닌다.
1. 테스트가 쉽다
2. 예측가능한 함수들
3. 버그가 적다 + 발견하기 쉽다
4. 충돌 가능성이 적다 (외부 변수를 이용하지 않으므로)
5. 더욱 선언적이다 (무조건 장점은 아님)
## Effect Handling Basics

sum이랑 똑같은 함수인디

- [?] 재귀를 짤 때 뭐 순수 재귀로 짜면 스택이 안 쌓인다구요?? 컴파일러에서 알아서 짜준다구요??
- [?] 근데 게임 같은 분야에서는 이게 가능할까요 밥먹듯이 쓰는게 전역변수인데 (싱글톤 패턴같은 것도 있음)
