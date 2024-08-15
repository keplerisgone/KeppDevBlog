---
tags:
  - Linux
  - Docker
---

- Docker 엔진이 QEMU 에뮬을 사용해 amd64 컨테이너를 arm64 명령어로 번역하는 방식으로 작동한다

```
docker run --platform linux/amd64 hello-world
```

- 위 명령어를 이미지 실행시에 입력해 플랫폼을 바꿀 수 있다.