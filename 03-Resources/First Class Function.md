---
tags:
  - Incomplete
  - Dev
---
**First Class Function**은 한국어로 '일급 함수' 정도로 번역되곤 한다. 간단히 설명하자면 함수를 변수처럼 다룰 수 있는 경우에 이를 first class function이라고 한다. 

first class function을 지원하는 언어에는 python, JS, 그리고 대부분의 함수형 언어들이 있다. 파이썬에서는 [[Lambda Function|람다 함수]]를 이용하여 쉽게 구현할 수 있다.


```python
def add(x):
	def _add():
		return x+1
	return _add

add(5) # 6
```
