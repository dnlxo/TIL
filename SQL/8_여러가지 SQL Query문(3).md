## 8_여러가지 SQL Query문(3)

## INSERT문 기본

```sql
INSERT INTO 테이블[(열1, 열2, ...)] VALUES (값1, 값2, ...)

-- 열1, 열2, ... 는 생략 가능 하지만 VALUES 뒤 순서가 테이블에 정의된 열 순서랑 동일해야한다.
```

## SEQUENCE

```SQL
CREATE SEQUENCE idSEQ
	START WITH 1
	INCREMENT BY 1
	
INSERT INTO ~~~ VALUES (idSEQ.NEXTVAL, ~~~)
-- 이렇게 사용

ALTER SEQUENCE idSEQ
	INCREMENT BY 10
-- 증가값 10으로 변경

SELECT idSEQ.CURRVAL FROM DUAL;
-- 시퀀스 현재값 확인하는 법
-- DUAL 은 오라클에 내장된 가상의 테이블

-- CYCLE, NOCACHE 를 이용해여 값 반복하기
-- 1,2,3,4,... 이렇게 말고 1,2,3,1,2,3,... 이런 식으로
CREATE SEQUENCE cycleSEQ
	START WITH 100
	INCREMENT BY 100
	MINVALUE 100
	MAXVALUE 300
	CYCLE
	NOCACHE ;
```

---

## 다른 테이블에서 데이터를 가져와서 대량으로 입력하기

```SQL
INSERT INTO 테이블이름 (열1, 열2, ...)
	SELECT 문..
```

---

## UPDATE

```SQL
-- 기존 입력값 변경
UPDATE testTBL4
	SET Phone = '없음'
	WHERE FirstName = 'David';
-- 데이비드의 폰을 없음으로 변경

UPDATE buyTBL SET PRICE = PRICE * 1.5 ;
```

---

## DELETE

```sql
DELETE FROM testTBL4 WHERE FirstName = 'peter';
-- WHERE 생략시 테이블 전체 삭제

ROLLBACK; -- 지운거 되돌리기

DELETE FROM testTBL4 WHERE FirstName = 'peter' AND ROWNUM <= 2;
-- peter 중에서 상위 2개만 삭제

DELETE, DROP, TRUNCATE 로 테이블 삭제
-- DML문인 DELETE는 트랜잭션 로그를 기록해야해서 (되돌릴 수 있음) 느리다
-- DDL문인 DROP은 바로 삭제 (테이블 자체를 없애버림) (롤백 불가) (빠름)
-- TRUNCATE는 롤백 불가이면서 (빠름) DELETE와 같은 기능. 곧 테이블 자체는 남겨두고 데이터만 지움
```

---

## MERGE

중요한 멤버 테이블에 정보를 INSERT, UPDATE, DELETE 할 시 직접적으로 바로 적용하지 않고, 다른 테이블에 INSERT 해놓고 나중에 적용시킨다.

```SQL
CREATE TABLE memberTBL AS
(SELECT userID, userName, addr FROM userTBL);

SELECT * FROM memberTBL;

CREATE TABLE changeTBL
( userID CHAR(8),
userName NVARCHAR2(10),
addr NCHAR(2),
changeType NCHAR(4)
);

INSERT INTO changeTBL VALUES('TKV', '태권브이', '한국', '신규가입');
INSERT INTO changeTBL VALUES('LSG', null, '제주', '주소변경');
INSERT INTO changeTBL VALUES('LJB', null, '영국', '주소변경');
INSERT INTO changeTBL VALUES('BBK', null, '탈퇴', '회원탈퇴');
INSERT INTO changeTBL VALUES('SSK', null, '탈퇴', '회원탈퇴');

-- MERGE 실행

MERGE INTO memberTBL M --M 테이블을 변경
	USING (SELECT changeType, userID, userName, addr FROM changeTBL) C -- C 테이블을 참고해서
	ON (M.userID = C.userID) -- 두 테이블을 userID를 기준으로 비교
	WHEN MATCHED THEN
		UPDATE SET M.addr = C.addr -- 동일한 이름이 있으면 주소 변경
		DELETE WHERE C.changeType = '회원탈퇴' -- 근데 회원탈퇴였으면 지우셈
	WHEN NOT MATCHED THEN -- 이름 없으면 추가
		INSERT (userID, userName, addr) VALUES(C.userID, C.userName, C.addr);
```

