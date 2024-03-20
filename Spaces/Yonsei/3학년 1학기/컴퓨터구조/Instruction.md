![[Instruction 2024-03-10 14.08.07.excalidraw|100]]

## Function Call Transition - example

![](https://i.imgur.com/AeEOISG.png)
- 위의 간단한 함수 호출 코드를 assembly로 변환하면 어떻게 될까?

![](https://i.imgur.com/V2q0j05.png)

1. Stack pointer 의 값을 -3 bytes 만큼 옮긴다. - stack에서 사용해야 하기 때문
2. 원래 register 의 값을 저장
3. 계산 진행 & return value 저장
4. 원래 register 값 복원 (stack 이용)
5. x1 에 담긴 return address 로 jump

![](https://i.imgur.com/C97RsJm.png)

## Calling Convention 

![](https://i.imgur.com/KeKc5iV.png)

* register 에 따라 정해져 있다
* temporary register: 자유롭게 이용가능
* x2(sp)가 내려가는데 공간이 부족할 경우 → x8 (fp) 를 이용, 처음 주소를 저장
* 함수의 caller, callee 가 쓰는 temporary register 가 다름
* <font color="#c00000">이거를 굳이 왜 나눌까?</font>
	* 레지스터의 상태를 관리하는 책임을 명확하게 하기 위함! 호출하는 레지스터의 종류에 따라 백업의 책임이 다르다
	* 만약 역할이 나누어져 있지 않다면 레지스터의 복원이 꼬여 값을 잃어버리거나 원래 값을 덮어쓸 수 있다

## Nested Function Calls

![](https://i.imgur.com/rURcqKJ.png)

recursive function (재귀함수)는 어떻게 컴파일될까?
-> 이는 x1(ra), x10(return value)를 스택에 계속 쌓아가며 이루어진다. 아래의 사진 및 코드를 참고하자. 가장 핵심이 되는 부분은 재귀를 if-else문으로 다시 구현한 점, x1과 x10의 값이 계속 업데이트 된다는 점이다.

![](https://i.imgur.com/bZunXzt.png)


![](https://i.imgur.com/dtY2T9y.png)
