---
tags:
  - Incomplete
  - CPP
---
# Summary

C++의 string은 문자열을 처리하기 위한 데이터 타입으로, 표준 라이브러리의 일부로 사용할 수 있다. [[C++ Vector 벡터]]와 마찬가지로 동적으로 데이터를 관리할 수 있으며, 길이가 가변적인 문자열 사용에도 알맞다. 
# Contents

## 사용 방식

`<string>` 헤더파일을 불러와 사용할 수 있다. 내부에서 동적으로 메모리를 할당해 문자열을 저장한다. 문자열의 끝에는 NULL 문자(*\0*)을 사용한다 

## 연산자

1. **할당 연산자(=)**: 문자열의 복사나 대입에 사용됩니다.
2. **덧셈 연산자(+)**: 두 개의 문자열을 결합하여 새로운 문자열을 생성합니다.
3. **출력 연산자(<<)**: 문자열을 표준 출력에 출력합니다.
4. **비교 연산자(==, !=, <, >, <=, >=)**: 두 개의 문자열을 비교하여 관계를 판단합니다.
5. **인덱스 연산자([])**: 특정 인덱스의 문자에 접근합니다.
6. **추출 연산자(<<)**: 특정 범위의 문자열을 추출합니다.
7. **할당 및 결합 연산자(+=)**: 문자열을 추가하거나 결합하여 현재 문자열에 할당합니다.
8. **스트림 연산자(>>, <<)**: 문자열을 스트림으로 읽거나 쓸 때 사용됩니다.
9. **소멸 연산자(~)**: 소멸자로서 문자열이 메모리에서 해제될 때 호출됩니다.

## 함수

1. **void** **push_back**(**문자 또는 문자열**): 문자열의 끝에 문자 또는 문자열을 추가합니다.
2. **void** **pop_back**(): 문자열의 끝에 있는 문자를 제거합니다.
3. **string::iterator** **insert**(**string::iterator 위치, 문자 또는 문자열**): 특정 위치에 문자 또는 문자열을 삽입합니다.
4. **string::iterator** **erase**(**string::iterator 위치 또는 범위**): 특정 위치나 범위에 있는 문자를 제거합니다.
5. **void** **clear**(): 문자열을 모두 제거하여 빈 문자열로 만듭니다.
6. **void** **resize**(**size_t 새로운_크기, 문자**): 문자열의 크기를 변경하고 추가 문자로 초기화합니다.
7. **size_t** **size**(): 현재 문자열의 길이(문자 수)를 반환합니다.
8. **size_t** **length**(): 현재 문자열의 길이(문자 수)를 반환합니다. (size()와 동일)
9. **size_t** **capacity**(): 현재 할당된 메모리 공간의 크기를 반환합니다.
10. **bool** **empty**(): 문자열이 비어 있는지 여부를 확인합니다.
11. **char&** **front**(): 첫 번째 문자에 대한 참조를 반환합니다.
12. **char&** **back**(): 마지막 문자에 대한 참조를 반환합니다.
13. **char&** **at**(**size_t 인덱스**): 특정 인덱스 위치의 문자에 대한 참조를 반환합니다. 범위를 체크하여 안전하게 접근합니다.
14. **char&** **operator[]**(**size_t 인덱스**): 특정 인덱스 위치의 문자에 대한 참조를 반환합니다. 범위를 체크하지 않으므로 주의가 필요합니다.
15. **string** **substr**(**size_t 시작_인덱스, size_t 길이**): 문자열에서 지정된 범위의 부분 문자열을 추출하여 반환합니다.
16. **size_t** **find**(**문자열 검색_문자열, size_t 시작_인덱스**): 문자열에서 검색 문자열의 첫 번째 발생 위치를 반환합니다.
17. **void** **swap**(**string& 다른_문자열**): 현재 문자열과 다른 문자열의 내용을 서로 교환합니다.

### 타입 변환 함수

1. **int stoi**(const string& str): 문자열을 정수로 변환합니다. 문자열이 정수를 나타내지 않는 경우 예외를 발생시킵니다.
2. **long stol**(const string& str): 문자열을 long 타입으로 변환합니다. 문자열이 long 타입으로 표현할 수 있는 범위를 벗어나는 경우 예외를 발생시킵니다.
3. **unsigned long stoul**(const string& str): 문자열을 unsigned long 타입으로 변환합니다. 문자열이 unsigned long 타입으로 표현할 수 있는 범위를 벗어나는 경우 예외를 발생시킵니다.
4. **long long stoll**(const string& str): 문자열을 long long 타입으로 변환합니다. 문자열이 long long 타입으로 표현할 수 있는 범위를 벗어나는 경우 예외를 발생시킵니다.
5. **unsigned long long stoull**(const string& str): 문자열을 unsigned long long 타입으로 변환합니다. 문자열이 unsigned long long 타입으로 표현할 수 있는 범위를 벗어나는 경우 예외를 발생시킵니다.
6. **float stof**(const string& str): 문자열을 float 타입으로 변환합니다. 문자열이 부동 소수점 수를 나타내지 않는 경우 예외를 발생시킵니다.
7. **double stod**(const string& str): 문자열을 double 타입으로 변환합니다. 문자열이 double 타입으로 표현할 수 있는 범위를 벗어나는 경우 예외를 발생시킵니다.
8. **long double stold**(const string& str): 문자열을 long double 타입으로 변환합니다. 문자열이 long double 타입으로 표현할 수 있는 범위를 벗어나는 경우 예외를 발생시킵니다.
9. **string to_string**(int val): 정수를 문자열로 변환합니다.
10. **string to_string**(long val): long 타입을 문자열로 변환합니다.
11. **string to_string**(unsigned val): unsigned 정수를 문자열로 변환합니다.
12. **string to_string**(long long val): long long 타입을 문자열로 변환합니다.
13. **string to_string**(unsigned long val): unsigned long 정수를 문자열로 변환합니다.
14. **string to_string**(unsigned long long val): unsigned long long 정수를 문자열로 변환합니다.
15. **string to_string**(float val): float 타입을 문자열로 변환합니다.
16. **string to_string**(double val): double 타입을 문자열로 변환합니다.
17. **string to_string**(long double val): long double 타입을 문자열로 변환합니다.
# Reference




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