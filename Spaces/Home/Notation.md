---
tags:
  - Main
sticker: lucide//alarm-check
---
# Questions
```dataview
LIST FROM #Question 
```
# Tasks

```dataview
TABLE
	wakeup as "기상",
	sleep as "취침",
	english as "언어",
	reading as "독서",
	workout as "운동",
	diary as "일기",
	blog as "블로그"
FROM #daily_note and !#Template 
WHERE file.cday > (date("today") - dur(5 days))
SORT file.cday DESC
```
### 그 외 Tasks
```dataview
TASK
WHERE contains(file.tags,"#Tasks")
```
- [ ] 유니티 프로젝트
    - [x] 문서작성하기
    - [x] 변수 변경하기
    - [ ] 칸반 써보기 - 프로젝트용
- [ ] 백준
- [ ] 모니터 닦rl
### 니가 싼 똥
```dataview
LIST
FROM #Incomplete 
SORT file.name ASC
```
## Weekly

- [ ] 유니티 블로그 날먹하기
- [x] 옵시디언 깨우치기
- [ ] 더 나은 코드 로직을 생각하는 법 → 디자인 패턴?
- [ ] 싼 똥 치우기
## Monthly

- [ ] 유니티 프로젝트 대충이라도 해보기
- [ ] DAS.
- [ ] 자격증 하나 날먹하기
