---
id: 06e970a3-4808-44df-8437-8ae4ba751029
---

# PHP 문자열 비교

[Read on Omnivore](https://omnivore.app/me/php-18e0fbc2c2a)
[Read Original](https://shk1354.tistory.com/44)

## PHP의 문자열 비교

- *모두 문자로 이루어져 있을 경우*: 사전 순으로 비교, 먼저 나온 문자열이 작다.
- *모두 숫자로 이루어진 경우*: 숫자로 변환한 후 대소비교
- *두 문자열이 숫자, 문자가 혼합된 경우*: 사전 순 비교
- *하나는 숫자로 시작, 다른 하나는 숫자일 경우*: 숫자로 변환 후 대소비교

> <mark class="omni omni-yellow">먼저 나온 문자열이 나중에 나온 문자열 보다 '작다'고 판단한다</mark> [⤴️](https://omnivore.app/me/php-18e0fbc2c2a#5afa5c21-86f3-43db-ba52-c7f0e6c5f149)  ^5afa5c21

> <mark class="omni omni-yellow">전부 숫자로 이루어진 문자열이나 숫자로 시작하는 문자열을 비교할 때는 예측과 다른 결과가 나올 수도 있다. PHP엔진은 이러한 문자열을 발견하면 문자열을 숫자로 변환해 비교한다</mark> [⤴️](https://omnivore.app/me/php-18e0fbc2c2a#ddce838e-b92c-40c3-aa79-0562b8cf90a6)  ^ddce838e

```php
// 사전 순서로 비교
if ("x54321" > "x5678") {
	print '문자열 "x54321"은 문자열 "x5678"보다 크다.';
}else{
		print '문자열 "x54321"은 문자열 "x5678"보다 크지 않다.';
}

//숫자 순서로 비교
if ("54321" > "5678"){
	print '문자열 "54321"은 문자열 "5678"보다 크다.';
}else{
	print '문자열 "54321"은 문자열 "5678"보다 크지 않다.';
}

// 사전 순서로 비교
if('6 pack' < '55 card stud'){
	print '문자열 "6 pack"은 문자열 "55 card stud"보다 작다.';
} else{
	print '문자열 "6 pack"은 문자열 "55 card stud"보다 작지 않다.';
}

// 숫자 순서로 비교
if ('6 pack' <55) {
	print '문자열 "6 pack"은 숫자 55보다 작다.';
}else{
	print '문자열 "6 pack"은 숫자 55보다 작지 않다.';
}

/* 출력화면
문자열 "x54321"은 문자열 "x5678"보다 크지 않다.
문자열 "54321"은 문자열 "5678"보다 크다.
문자열 "6 pack"은 문자열 "55 card stud"보다 작지 않다.
문자열 "6 pack"은 숫자 55보다 작다.
```