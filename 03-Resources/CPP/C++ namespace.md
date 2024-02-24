# Summary

C++의 namespace에 대해서 알아봅시다.

# Contents

## namespace

이름 공간(*namespace*)은 C++에서 각종 개체의 **소속된 공간**을 알려주는 역할을 합니다. 같은 이름의 `print()` 함수더라도 소속된 곳이 다르다면 C++에서는 다른 함수로 취급합니다.


```cpp
namespace header1 {
	void foo();
	int bar();
}

namespace header2 {
	void foo();
	int bar();
}
```

위에서는 두 개의 이름이 같은 함수 `foo(), bar()`는 같은 이름의 함수이지만, 다른 namespace에 정의되어있기 때문에 다른 함수로 취급됩니다. 따라서 아래의 두 개는 다른 함수로 취급됩니다.

```cpp
header1::foo();
header2::foo();
```

namespace 내부의 함수는 다음과 같은 조건에 의해 실행됩니다.
1. namespace 내부에서 namespace를 붙이지 않고 함수를 실행하면 자동으로 namespace 내부의 함수가 실행됩니다.
2. `using namespace` 를 이용하면 namespace를 붙이지 않고 함수르 ㄹ시행할 수 있습니다. 이름이 같은 다른 함수를 시행하려면 namespace를 붙여야 합니다.

이름이 없는 namespace는 자동으로 해당 파일 내부에서만 접근할 수 있습니다.

```cpp
namespace {
	int foo() {}
}
```

## std
# Reference

