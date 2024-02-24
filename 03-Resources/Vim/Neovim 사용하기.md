---
tags:
  - Incomplete
  - Productive
---
# Summary

튜닝의 끝은 순정이고, VSCode와 sublime text를 쓰던 나는 결국 전필 때 교수님 서버에서 쓰던 vim으로 회귀했다. Git도 GUI에 둘러싸이며 쓰는 나지만, 텍스트 에디터 하나쯤은 CLI로 써도 나쁘지 않다 생각했다. 지금 쓰는 언어가 많이 없기도 하고 말이다. 그러던 중 [[Neovim으로 생산성 퀀텀점프하기 by 이재열 - PPT]] 문서를 보고 설득당해 Neovim으로 갈아탈 준비를 하게 되었다.

아래는 Neovim 설정법, 대략적인 사용법 등을 다룬다.

# Contents

## Neovim 설치 & Lunarvim 설치

나는 mac에서 Homebrew를 사용중이므로 `brew install neovim`을 터미널에 입력한다
세팅을 위해서 *LunarVim*을 사용, 링크는 [Installation - LunarVim](https://www.lunarvim.org/docs/installation)를 참고했다.

사실 위에 들어가면 다 알려준다 사용법부터 시작해가지고..
들어가서 `~/.local/bin/lvim`을 실행시켜주면 neovim 기반의 IDE를 사용할 수 있다!

여기서 명령어 `lvim`이 먹지 않을 경우 터미널 설정 문서에서 경로 변수를 추가해줘야 한다. `~/.zshrc`에 다음과 같은 내용을 추가한다. : `export "~/.local/bin:$PATH"` 그 뒤 `lvim` 명령어를 실행하면 LunarVim을 실행시킬 수 있다.

## LunarVim 설정

설정 해야할 것은 다음과 같다 : 
1. 테마 설정
2. 폰트 설정
3. 플러그인 다운받기

# Reference



