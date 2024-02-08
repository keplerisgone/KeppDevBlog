---
tags:
  - Main
sticker: lucide//alarm-check
---
# Questions
```dataview
LIST FROM #Question 
SORT file.name ASC
```
# Tasks

```dataview
TASK
WHERE contains(file.tags,"#Tasks")
```
### 니가 싼 똥
```dataview
LIST
FROM #Incomplete 
SORT file.name ASC
```

