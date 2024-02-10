---
tags:
  - Incomplete
  - CPP
---



# String to int / Int to String

모두 `<string>` 헤더 파일에 있는 함수를 이용한다.

## String to int

`stoi(str)` 함수를 이용해 변환한다.

```cpp
string str = "773";
int str_to_int = stoi(str);

std::cout << str_to_int << "\n"; // 773
```

## Int to String 

`to_string(int)` 함수를 이용해 변환한다.

```cpp
int num = 773;
string int_to_str = to_string(num);

std::cout << int_to_str << "\n"; // 773
```

## 사용 예제