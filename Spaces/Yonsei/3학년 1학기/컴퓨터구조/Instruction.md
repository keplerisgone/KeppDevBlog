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

# Calling Convention 

![](https://i.imgur.com/KeKc5iV.png)

* register 에 따라 정해져 있다
* temporary register: 자유롭게 이용가능
* x2(sp)가 내려가는데 공간이 부족할 경우 → x8 (fp) 를 이용, 처음 주소를 저장
* 함수의 caller, callee 가 쓰는 temporary register 가 다름
* <font color="#c00000">이거를 굳이 왜 나눌까?</font>
	* 레지스터의 상태를 관리하는 책임을 명확하게 하기 위함! 호출하는 레지스터의 종류에 따라 백업의 책임이 다르다
	* 만약 역할이 나누어져 있지 않다면 레지스터의 복원이 꼬여 값을 잃어버리거나 원래 값을 덮어쓸 수 있다

# Nested Function Calls

![](https://i.imgur.com/rURcqKJ.png)

recursive function (재귀함수)는 어떻게 컴파일될까?
-> 이는 x1(ra), x10(return value)를 스택에 계속 쌓아가며 이루어진다. 아래의 사진 및 코드를 참고하자. 가장 핵심이 되는 부분은 재귀를 if-else문으로 다시 구현한 점, x1과 x10의 값이 계속 업데이트 된다는 점이다.

![](https://i.imgur.com/bZunXzt.png)


![](https://i.imgur.com/dtY2T9y.png)

# Function Frame and Frame Pointer

![](https://i.imgur.com/GRJU77J.png)
- 함수를 이용하다 보면 커다란 변수들을 담는 경우가 많아질 것.
- 해당 변수들은 **스택**에 저장된다.
	- 변수의 종류마다 함께 쌓이게 되는데, 이들을 function frame이라고 한다.
	- **Frame pointer** 요런 frame들의 시작 부분을 담고, 스택에 저장된다.
	- **x8**이 FP의 역할을 함.
![](https://i.imgur.com/Q9G6aWW.png)
## Stack pointer vs Frame Pointer

![](https://i.imgur.com/BV38AkA.png)
- 근데 왜 굳이 둘을 분리해서 사용할까?
	- **stack pointer**는 그냥 현재 스택의 제일 밑부분을 가리키는 포인터
	- **frame pointer**는 일종의 북마크 같은 것
		- sp의 위치는 계속해서 바뀔 수 있으므로, 원하는 값에 접근하기 위해서는 많은 노력이 필요하다...
# Data in Heap Memory Region and Memory Leak

![](https://i.imgur.com/bqnTmuU.png)
- **heap**은 동적 메모리이고, C 같은 경우는 malloc() 함수로 동적 할당 가능
- 하지만 컴파일러가 이를 자동으로 해제해주지 않으므로, **free**를 이용해서 꼭 해제해주어야 함
- 안 그러면 메모리 누수가 일어남
	- 컴퓨터가 메모리 공간이 없다고 인식