## WHERE 문

```SQL
SELECT * FROM userTBL WHERE userName = '김경호';
SELECT * FROM userTBL WHERE userName = '김경호' OR userName = '은지원';

-- 관계 연산자 (NOT AND OR)

-- 1970 이후 출생이면서 키 182 이상
SELECT userid, username FROM userTBL WHERE birthYear >= 1970 AND height >= 182;

-- 조건 연산자 (= < > <= >= <> !=)

-- BETWEEN ... AND 연속적인 값 (숫자) 일 때
SELECT username, height FROM userTBL WHERE height BETWEEN 180 AND 183; -- 180이상 183이하
-- 180 <= height <= 183 이렇게 안 됨
SELECT username, height FROM userTBL WHERE height <= 183 AND height >= 180;
-- 이렇게 해야함

-- IN () 이산적인 값들..
SELECT userName, addr FROM userTBL WHERE addr IN ('경남', '전남', '경북') ;

-- 문자열의 내용 검색 LIKE
SELECT userName, height FROM userTBL WHERE userName LIKE '김%'; --김으로 시작 하는놈

-- 오로지 한 글자만 매치
SELECT userName, height FROM userTBL WHERE userName LIKE '_종신';

-- _와 %를 섞어서 사용 가능하다.
```

---

## ANY/ALL/SOME 그리고 서브쿼리(SubQuery)

- 서브쿼리 : 쿼리문 안에 쿼리문이 또 들어있는 것
- 예를 들어 김경호보다 키가 큰 사람들을 찾고 싶으면, 김경호의 키를 알아내서 WHERE height > 김경호 키
- 이렇게 하는 게 아니고 쿼리를 이용한다.

```SQL
SELECT userName, height FROM userTBL
	WHERE height > (SELECT height FROM userTBL WHERE userName = '김경호');
	
-- 본 구문은 RETURN 값이 김경호의 키 177 하나이다.
-- 하지만 RETURN 값이 두 개인 경우는 오류가 난다.
```

- RETURN 값이 두 개 이상인 경우 ANY 구문을 이용한다.
- 예를 들어 경남 사람들의 키보다 크거나 같은 사람이 궁금하다.
- 경남 사람은 여러명이다. (173과 170인 사람이 있음 실제로)

```SQL
SELECT rownum, userName, height FROM userTBL
	WHERE height >= ANY (SELECT height FROM userTBL WHERE addr = '경남');
	
-- ANY 구문 사용 시 170보다 큰 사람이거나, 173보다 큰 사람 모두 출력 되므로
-- 170보다 큰 사람들이 모두 출력된다.
```

- ALL 문으로 바꿔서 실행해보자

```SQL
SELECT rownum, userName, height FROM userTBL
	WHERE height >= ALL (SELECT height FROM userTBL WHERE addr = '경남');
	
-- 173보다 크거나 같은 사람들이 출력된다.
-- 170보다 크거나 같아야하고, 또 173보다 크거나 같아야 하기 때문이다.
```

- 즉 ANY 는 OR 과 비슷하다고 생각하면 된다.
- 실제로  =ANY 와 IN () 은 같은 효과를 낸다.

```SQL
SELECT userName, height FROM userTBL
	WHERE height = ANY (SELECT height FROM userTBL WHERE addr = '경남');
	
SELECT userName, height FROM userTBL
	WHERE height IN (SELECT height FROM userTBL WHERE addr = '경남');
	
-- 두 구문은 같다.
```

---

## ORDER BY 문

- 결과물에 대해 영향을 미치지는 않지만, 출력 순서를 조절할 수 있다.
- 기본적으로는 오름차순이다.
- 내림차순으로 만들기 위해선 DESC를 적어준다.

```SQL
SELECT userName, mDate FROM userTBL ORDER BY mDate DESC;

-- SELECT 에 없는 COLUMN 도 ORDER BY 의 기준으로 삼을 수 있다.
```

---

## DISTINCT 문

중복된 것은 하나만 남기고 출력한다.

```SQL
SELECT DISTINCT addr FROM userTBL;
```

---

## ROWNUM 과 SAMPLE 구문

```SQL
SELECT * FROM
	(SELECT employee_id, hire_date FROM employees ORDER BY hire_date)
	WHERE ROWUNM <= 5;
	
-- 정렬 후 위에서부터 5개만 출력하여 보여준다.
-- 일단 모든 데이터를 정렬해야 하기 때문에 성능이 떨어진다.

-- 임의의 데이터를 추출하고 싶다면 SAMPLE(퍼센트) 문을 사용한다.
SELECT employee_id, hire_date FROM EMPLOYEES SAMPLE(5);

-- EMPLOYEES 테이블에서 랜덤하게 5%개를 출력해준다.
-- 퍼센트는 0초과 100미만 이어야 한다. 말 그대로 데이터 개수의 퍼센트 만큼 출력이다.
```

---

## 테이블을 복사하는 CREATE TABLE ... AS SELECT

테이블을 복사해서 사용할 경우에 주로 사용한다.

```SQL
-- buyTBL 을 buyTBL2 로 복사
CREATE TABLE buyTBL2 AS (SELECT * FROM buyTBL);

-- 일부 열만 복사도 가능
CREATE TABLE buyTBL3 AS (SELECT userID, prodName FROM buyTBL);

-- 하지만 PK나 FK 등 제약 조건은 복사되지 않는다.
```

