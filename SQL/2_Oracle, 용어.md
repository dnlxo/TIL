## Oracle, 용어

- 정보시스템 구축 절차
  - 분석, 설계, 구현, 시험, 유지보수
- 데이터베이스 모델링이 중요하다.
  - 현실세계에서 사용되는 데이터를 Oracle에 어떻게 옮길 것인가.
  - 예를 들면 물건의 경우.. 제조일자, 제조회사, 물건이름 등..
  - 테이블이라는 형식에 맞춰서!

![image-20210603200955499](img/1.png)

- 데이터 : 정보는 있으나 체계화 되지 않은 하나하나 단편적인 정보들..
- 테이블 : 데이터를 입력하기 위해 표 형태로 표현한 것
- 스키마 : 테이블, 뷰 등이 저장되는 저장소 or 테이블, 뷰 등의 묶음
  - 사용자 별 고유의 공간 = 스키마 = 사용자
- 데이터베이스 : 여러 개의 스키마가 저장되는 저장공간
  - Oracle XE는 XE라는 이름의 db를 기본적으로 제공하며, 1개의 db만 운영 가능하다.
  - 각 DBMS 마다 데이터베이스 용어가 조금씩 다르게 사용된다.
    - MySQL, MariaDB, SQL Server 등에서는 스키마 = db 라고 부른다.
- 데이터 유형 : 테이블을 생성할 때 열 이름과 함께 지정해 주어야 한다.
- 행 (row) : 실질적인 데이터.
  - 회원 테이블에서 회원이 몇 명인가 -> 행이 몇 개인가
  - We / 위태 / 서울 / 남자
- 기본 키 (Primary Key) 열 : 
  - 각 행을 구분하는 유일한 열
  - 기본 키 열은 중복되어서는 안 되며, 비어있어서도 안 된다.
  - 각 테이블에는 기본 키가 하나만 지정되어야 한다.
  - ex) 중복되지 않는 ID 는 기본 키로 설정하기 적합하다.
  - ex) 주소나 이름은 적합하지 않다.
- 외래 키 (Foreign Key) 필드 :
  - 두 테이블의 관계를 맺어주는 키
- SQL : 사람과 DBMS가 소통하기 위해 사용하는 언어

> - localhost = 127.0.0.1
>   - 자신의 컴퓨터를 의미한다.
> - 1521번 포트 : 컴퓨터의 가상 연결 통로 개념으로 0 ~ 65535번 까지 이용 가능
> - SID : Oracle XE의 시스템 아이디
> - 쿼리, 쿼리문, SQL, SQL문 모두 동일한 용어로 생각하자

---

## 오라클

- 롤 (Role) :
  - 가장 높은 롤 : DBA
  - 일반적으로 CONNECT, RESOURCE 두 개의 롤을 부여하면 스키마에 대한 대부분의 작업을 할 수 있다.

- 스키마 생성
- 테이블 생성
  - 열 이름, 데이터 유형, 크기, null 인지 아닌지
  - CHAR : 고정형 길이
  - VARCHAR2 : 가변형 길이
- 오라클은 기본적으로 테이블 등의 이름을 대문자로 처리
- 하지만 큰 따옴표 안에 이름을 넣을 경우에는 그대로 사용한다.
- 오라클에서 "" 을 사용해서 테이블 등의 이름을 지정하는 방식은 권장하지 않는다.
- **대문자로 지정하고 띄어쓰기를 사용하지 않도록 한다.**

---

## 테이블 외의 데이터베이스 객체들

뷰, 인덱스, 스토어드 포르시저, 트리거, 함수, 커서 등이 있다.

1. 인덱스 :

   - 쿼리에 대한 응답을 줄이기 위해 가장 집중적으로 보는 부분 중 하나
   - 실제 책에 비유하면, 맨 뒷장의 찾아보기 부분
   - 모든 데이터를 읽어서 찾기엔 오래걸림
   - 필요한 열에는 인덱스를 생성해줘야 한다.
   - 인덱스 생성하는 법 : CREATE INDEX ...

2. 뷰

   - 가상의 테이블
   - 사용자 입장에서는 테이블과 동일하게 보이지만, 뷰는 실제 행 데이터가 없다.
   - 실제 테이블에 링크된 개념이라고 생각
   - 회원정보에서 중요정보 제외한, 아이디와 주소만 있는 VIEW를 생성할 수 있다.
   - 링크된 개념이라 데이터의 중복이 발생되지 않는다.
   - 뷰 생성하는 법 : CREATE VIEW ...
   - 테이블과 동일하게 사용하면 된다.

3. 스토어드 프로시저 (Stored Procedure)

   - 오라클에서 제공해주는 프로그래밍 기능

   - 함수 같은 느낌..?

   - ```sql
     SELECT COUNT(*) FROM memberTBL;
     SELECT COUNT(*) FROM productTBL;
     
     >>> myProc 라는 프로시저 생성
     
     CREATE PROCEDURE Shop.myProc AS -- shop
     var1 INT;
     var2 INT;
     BEGIN
     	SELECT COUNT(*) INTO var1 FROM Shop.memberTBL;
     	SELECT COUNT(*) INTO var2 FROM Shop.productTBL;
     	DBMS_OUTPUT.PUT_LINE(var1+var2);
     END;
     
     >>> 프로시저 실행
     
     EXECUTE myProc;
     ```

> 생성과 삭제
>
> CREATE 개체종류 개체이름 ~~~
>
> DROP 개체종류 개체이름 

4. 트리거 (Trigger)

   - 테이블에 부착되어 INSERT, UPDATE, DELETE 작업이 발생 시 실행되는 코드

   - ex) 회원 정보를 지울 때, 탈퇴 회원 이라는 곳에 그 정보를 모아둘 수 있다.

     - 탈퇴 멤버 보관할 테이블을 생성한다.

     - 트리거를 생성한다.

     - ```sql
       CREATE TRIGGER trg_deletedMemberTBL
       	AFTER DELETE
       	ON memberTBL
       	FOR EACH ROW
       BEGIN
       	-- :old
       	INSERT INTO deletedMemberTBL
       		VALUES(:old.memberID, :old.memberName, old.memberAddress, SYSDATE());
       END;
       ```

---

## 데이터의 백업 및 복원

백업 : 현재 스키마를 다른 매체에 보관하는 작업

복원 : 데이터베이스에 문제가 발생시 다른 매체에 백업된 데이터를 이용해서 원상태로 돌려놓는 작업

DBA(database admin : 스키마 관리자) 의 가장 중요한 역할이다.

- 백업용 폴더 생성

- ```sql
  --백업
  exp userid=SYSTEM/1234@xe OWNER=Shop FILE=C:경로\Shop01.dmp -- 파일이름
  
  --복원
  imp userid=SYSTEM/1234@xe FROMUSER=Shop TOUSER=Shop FILE=C:경로\Shop01.dmp TABLES=(productTBL)
  ```

- 자세한 exp.exe, imp.exe 명령어는 책 89p 참고

---

