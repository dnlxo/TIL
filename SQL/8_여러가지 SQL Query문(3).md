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