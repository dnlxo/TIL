## Redis

- Remote dictionary server
- In-memory Data Structure Store
- Cache
  - Memory Hierarchy
    - CPU Register
    - CPU Cache (SRAM)
    - Main Memory (DRAM)
      - 휘발성 (컴 끄면 날아감)
    - Storage

- 기본적으로 데이터는 컴퓨터가 꺼져도 저장이 되어야하므로 Storage에 저장
- 더 자주 접근하는 데이터들을 더 빠른 Main Memory에 저장하자
  - In-memory Database (Cache)
- 자료구조
- String
- List (linked list)
- Set (hashSet)
- Sorted Set (TreeSet)

- Hash (HashMap)

---

- 캐시
  - 데이터의 원래 소스보다 더 빠르고 효율적으로 액세스할 수 있는 임시 데이터 저장소
  - 같은 데이터에 반복적으로 엑세스 할 때, 잘 변하지 않는 데이터일 수록 효과적
- 레디스를 캐시로 사용하기
  - key-value 구조
  - 모든 데이터를 ram에 올려두는 in-memory 데이터 저장소라 작업속도가 빠르다.
    - 지연속도감소, 처리량 증가
  - caching 전략
    - read 할 때 사용하는 전략
      - 가장 일반적
      - Look-Aside(Lazy Loading)
      - 초기 캐시 miss 부하 방지를 위해서
      - db에서 cache로 데이터를 올려주는 캐시 워밍작업을 하기도 한다.
    - write 전략
      - write-Around
        - db에 모든 데이터를 저장, 캐시 미스 된 경우 캐시로 데이터 끌어온다.
        - 
      - write-Through
        - 데이터를 write할 때, 캐시에 하고 db에도 함.
        - 캐시에 항상 최신 데이터가 있다는 장점.
        - 리소스 낭비
- Redis 데이터 타입
  - String
  - Bitmaps
  - Lists
  - Hashes
  - Sets
  - Sorted Sets
  - HyperLogLogs
  - Streams

- 카운팅 예시

  - String 자료구조의 INCR 이용해서 증감을 한다.

  - bits 연산으로 이진분류 시 저장공간 절약하며 사용가능 (방문 / 미방문)

- List

  - 키가 있을 때만 데이터 저장하는 기능도 있고,, 여러 기능있음

- Redis의 데이터 영구 저장

  - 서버 재시작 시 모든 데이터 유실
  - 캐시 이외 용도로 사용할 때, 데이터 백업이 필요.
  - AOF, RDB가 있음
  - AOF는 모든 추가 삭제 기록들
  - RDB는 현재 상태만

- 사용하면 안되는 커맨드

  - Redis는 싱글 스레드
    - 장애 빈번
    - keys *
      - 쓰면 망함
    - scan 0 으로 대체
  - hash나 sorted set 등의 자료구조에는
    - 키 하나당 만개 이하로 저장
    - 키 하나에 데이터 많을 때 del 사용하면 느림 unlink 하삼

---

## Write Back

- 인메모리 쓰기 읽기 빠르다.
- 쓰기가 빈번하면, 캐시에 먼저 저장해두고, batch로 특정 시간에 몰아서
- INSERT 쿼리 모아서 한번에,,,
- 로그 디비 저장할 때 보통..

---

- Redis는 메모리 관리를 잘 해야 한다.

