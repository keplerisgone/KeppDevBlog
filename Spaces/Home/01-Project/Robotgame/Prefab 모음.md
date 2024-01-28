---
tags:
  - Unity
  - Project
---
## Alert 

- 몬스터의 공격을 알려주는 느낌표 표시
- [[몬스터 구현#AttackWait()|몬스터 공격 스크립트]]에 의해 생성되고, `alertTime`이후에 자동으로 사라진다.
- 현재 자동으로 사라지는 기능이 **Update**에서의 count를 이용해 구현되어있는데, 이거 그냥 코루틴으로 시행하면 안되나 -> 그래도 Update하고 오브젝트가 사라지니까 괜찮을지도
- **Alert_Prefab.cs** 스크립트 존재. 위의 기능을 수행한다

## Atk1

- 몬스터의 공격 (임시, 일반 공격임)
- 몬스터의 자식 오브젝트로 소환되며, 자동으로 같이 움직인다
- `atkTime` 이후에 자동으로 사라진다
- 플레이어가 충돌시 [[Spaces/Home/01-Project/Robotgame/플레이어 구현#TakeDamage(Transform other, int damage)|데미지 함수]] 호출
- [ ] #Project   이거 이름 바꿔야함
- **Atk1_Prefab.cs**

## Coin

- 적을 죽일시 나오는 코인 오브젝트
- 타이머를 통해서 10초가 지나면 자동으로 사라짐
- OverlapCircle을 이용하여 플레이어가 범위 내에 들어오면 Gamemanager의 Coin+=1 그 후 파괴.
- 적을 쓰러뜨리면 코인 생성(TestEnemy.cs에 적 죽을 때 랜덤으로 코인 드랍)
- 적 캐릭터 위치에 코인 생성 후 (랜덤한 방향으로 Thrust 힘을 받아서 날아감)
- **Coin_Prefab.cs**

## PlayerNormalAtk

- 플레이어의 공격으로 소환됨
- 적이 충돌시 [[몬스터 구현#TakeDamage(int damage)|데미지]]와 [[몬스터 구현#KnockbackAction(Vector2 hitDirection, Vector2 constForceDirection)|넉백]]을 줌
- `atkTime` 이후에 자동으로 사라짐
- 플레이어의 자식 오브젝트로 소환되며, 같이 움직임