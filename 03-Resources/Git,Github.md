---
aliases:
  - "[Git/GitHub]"
tags:
  - "#Resources"
  - Git
---
# Git이란?

# 목적

# 기본개념
## Local, Remote

## Layers

# 사용방법

## 충돌해결
### 예방 방법
branch를 이용한 작업 공간 분리
작업 공간이 통합되어 있으면 한 번에 여러 명이 작업을 할 때 충돌을 피할 수 없다
예를 들어 A라는 작업공간에서 누가 어떻게 수정하고 누가 어떻게 수정하고 하면 쟤가 못 건든다 알겠지??
그래서 작업공간을 분리해서 




memo

```
$ git config pull.rebase false
$ git config pull.rebase true
$ git config pull.ff only
```
오 그래도 최고다~~~
아마 충돌이 일어나는 경우에는 GUI 같은 경우에는 웹으로 에디터를 열어주고 VSCode는 자체적으로 에디터를 제공해주며 CLI 같은 경우는.. "니가 알아서 해라" -> 그래도 코드에 경고 표시 추가해줘서 다행이다

충돌 해결을 하나 빼놔야겠다

똑똑한 사람들이 많은 깃헙에 쳐보자

clone vs fork
clone은 그냥 잘 쓰겠습니다~하고 로컬에 저장하는 것
fork는 진짜 repo를 하나 생성해서(copy로) 작업하는 것
근데 tensorflow는 좀 fork하기 그렇
branch를 나누는 방법?

fork로 맛있게 개발할 수 있구나
오픈소스는 신이다
	오픈소스를 아예 안 건들고 밖에서 건드는 걸 말하는 거
	오픈소스를 사용했는데 구형이 된 건에 대하여