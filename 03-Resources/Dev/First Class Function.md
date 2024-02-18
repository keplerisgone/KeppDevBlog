---
tags:
  - Incomplete
  - Dev
---
**First Class Function**은 한국어로 '일급 함수' 정도로 번역되곤 한다. 간단히 설명하자면 함수를 변수처럼 다룰 수 있는 경우에 이를 first class function이라고 한다. 

퍼스트 클래스 함수는 프로그래밍 언어에서 함수를 일급 객체로 취급하는 개념이다. 이는 함수를 변수에 할당하거나, 다른 함수의 인자로 사용하고, 다른 함수의 반환 값으로 쓸 수 있음을 의미한다. 이러한 특성은 프로그래밍에서 함수를 더욱 유연하게 사용할 수 있게 해준다. 예를 들어 파이썬에서 함수는 객체로 취급되어 다양한 용도로 활용된다. 함수를 이용해 고차 함수를 구현하거나 다른 함수 내에서 동적으로 함수를 생성하고 조작하는 것도 가능하다. 퍼스트 클래스 함수의 개념은 프로그래밍의 다양한 패러다임을 가능하게 하는 중요한 기초이다.

first class function을 지원하는 언어에는 python, JS, 그리고 대부분의 함수형 언어들이 있다. 파이썬에서는 [[Lambda Function|람다 함수]]를 이용하여 쉽게 구현할 수 있다.


```python
def add(x):
	def _add():
		return x+1
	return _add

add(5) # 6
```

퍼스트 클래스 함수의 예시를 들어볼게요. 파이썬에서 함수는 변수에 할당될 수 있습니다. 예를 들어, `square`라는 함수가 있다고 가정해 보겠습니다.

```python
def square(x):
    return x * x

f = square
print(f(5))
```

이 코드에서 `square` 함수는 `f`라는 변수에 할당되었습니다. 그리고 `f(5)`를 호출하면 `square` 함수가 실행되어 25를 출력합니다.

또 다른 예로, 함수를 다른 함수의 인자로 전달할 수도 있습니다. 

```python
def square(x):
    return x * x

def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

num_list = [1, 2, 3, 4, 5]
squares = my_map(square, num_list)
print(squares)
```

여기서 `my_map` 함수는 함수를 인자로 받아, 그 함수를 리스트의 각 요소에 적용합니다. 이 경우 `square` 함수가 `my_map`에 인자로 전달되어, 리스트의 각 요소를 제곱합니다. 이 예시는 함수를 다른 함수의 인자로 사용하는 퍼스트 클래스 함수의 특성을 잘 보여줍니다.