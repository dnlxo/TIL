## SQL의 분류

1. DML (Data Manipulation Language)
   - DML은 데이터를 조작 (선택, 삽입, 수정, 삭제) 하는 데 사용되는 언어
   - DML 구문이 사용되는 대상은 테이블의 행
   - DML을 사용하기 위해서는 테이블이 정의되어 있어야 한다.
   - SELECT, INSERT, UPDATE, DELETE
   - Transaction이 발생하는 SQL도 DML이다.

> 트랜잭션이란 테이블에 임시적용 시키는 것.
>
> 즉 커밋하기 전,
>
> COMMIT 으로 확정시키고,
>
> ROLLBACK 으로 취소시킨다.

2. DDL (Data Definition Language)
   - 데이터베이스 개체를 생성, 삭제, 변경하는 역할
   - CREATE, DROP, ALTER 등
   - DDL은 트랜잭션을 발생시키지 않는다.
   - 실행 즉시 Oracle에 적용된다.
3. DCL (Data Control Language)
   - 사용자에게 어떤 권한을 부여하거나 빼앗을 때 주로 사용하는 구문
   - GRANT, REVOKE, DENY 등