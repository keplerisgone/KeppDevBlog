
디버깅을 하기 위해 필요한 것
- VSCode C/C++ extension
- GCC 컴파일러 (이미 있음)
- Code runner settings

# code runer settings

https://omnivore.app/keplerisgone/vs-code-c-ide-mac-c-1903af0a3f4

- 이건 처음봐서 적는다
- **Run In Terminal** 옵션은 켠다
- 각 언어별로 실행 명령어를 설정 가능 (*setting.json*)
- 
![|575](https://i.imgur.com/iovhyOR.png)
- C++ 버전 설정
	- `"cpp": "cd $dir && g++ -std=c++17 $fileName -o $fileNameWithoutExt && $dir$fileNameWithoutExt"`
- 프로젝트 단위 컴파일
	- `"cpp": "cd $dir && g++ -std=c++17 *.cpp -o $fileNameWithoutExt && $dir$fileNameWithoutExt",`