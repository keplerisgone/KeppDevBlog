---
tags:
  - Unity
---
타일맵 생성, 타일맵 사용, 물리적용에 대해서 다룹니다.

# 타일맵 생성

- 우선 *우클릭 - 2D Object - TileMap - Rectangular 선택,* 그리드와 타일맵이 생성된다.
- **타일맵**은 타일을 그리는 곳, 타일을 그리기 위해서는 지형지물이 그려져있는 **타일팔레트**가 필요.

## 타일팔레트 생성

- *Window - 2D - Tile Palette*를 들어간 뒤, *Create new Palette*를 눌러 새로운 타일팔레트 생성.
- 모드는 *Rectangular*, Cell Size는 *Automatic*으로 설정하면 유니티가 자동으로 잘 지정해줌.

## 타일팔레트 이미지 세팅

- 이미지를 타일맵에 사용하기 위해서 세팅을 해야함
- *Pixels per Unit*이 중요, *한 칸에 몇 픽셀을 담을 것인가?*(NxN)를 결정함. 사용하는 이미지에 따라 달라짐