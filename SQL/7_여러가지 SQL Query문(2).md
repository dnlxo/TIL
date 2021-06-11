## 7_여러가지 SQL Query문(2)

## GROUP BY 절

```SQL
-- 그룹으로 묶어주는 역할
-- 집계함수와 같이 사용

SELECT userID, amount FROM buyTBL ORDER BY userID;
-- 물건마다 amount가 있기 때문에 amount가 합산되어 출력되지 않고 각각 뜬다.
-- wty 3
-- wty 9
-- 이런 식으로.. 이걸 더해주려면
SELECT userID, SUM(amount) FROM buyTBL GROUP BY userID;

-- 열 이름 바꾸는 것 까지 해보면
SELECT userID AS 아이디, SUM(amount) AS 총수량 FROM buyTBL GROUP BY userID;

-- 총 구매 가격을 출력해보자.
-- (각 물건 별 금액) * (각 물건 별 수량) 이므로
SELECT userID AS 아이디, SUM(price*amount) AS 총구매가격 FROM buyTBL GROUP BY userID;


-- 가장 큰 키인 사람, 가장 작은 키인 사람 출력해보자
SELECT userName, height FROM userTBL 
    WHERE height = (SELECT MAX(height) FROM userTBL) 
        OR height = (SELECT MIN(height) FROM userTBL)
    ORDER BY height DESC;
```

> 집계 함수
>
> - AVG()
> - MIN()
> - MAX()
> - COUNT() : 행의 개수를 센다.
> - COUNT(DISTINCT)
> - STDEV()
> - VARIANCE()

---

## COUNT

```SQL
-- 휴대폰 번호가 있는 사용자 수를 출력해보자
SELECT COUNT(mobile1) FROM userTBL;
-- mobile1 열의 값이 NULL 인 행을 제외하고 COUNT 한다.
```

## HAVING

```SQL
-- 총 구매 가격을 출력해보자
SELECT userID AS 아이디, SUM(price*amount) AS 총구매가격 FROM buyTBL GROUP BY userID;
-- 총 구매 가격이 1000 이상인 사람들이 궁금하다.
-- 집계함수는 WHERE절에 나타날 수 없다.
-- WHERE SUM() >= 1000 이게 안된다고

SELECT userID AS 아이디, SUM(price*amount) AS 총구매가격 FROM buyTBL GROUP BY userID
HAVING SUM(price*amount) >= 1000;
-- HAVING은 WHERE과 비슷하게 조건을 제한하지만 집계 함수에 대해서 조건을 제한한다.
-- GROUP BY 절 다음에 나와야 한다.
```

---

## ROLLUP(), GROUPING_ID(), CUBE()

```SQL
-- 분류별로 합계와 총합을 출력해보자
SELECT groupName, SUM(price*amount) AS 비용, GROUPING_ID(groupName) AS 추가행인가
	FROM buyTBL
	GROUP BY ROLLUP(groupName);
	
-- 데이터인지, 세느라 추가된 열인지 구분하는 법
-- GROUPING_ID() 가 0이면 데이터고, 1이면 추가된 것이다.
```

