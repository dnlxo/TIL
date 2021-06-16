## 11_JOIN

두 개 이상의 테이블을 서로 묶어서 하나의 결과 집합으로 만들어 내는 것.

1. INNER JOIN

   ```sql
   -- 양쪽 테이블에 모두 내용이 있는 것만 조인
   
   SELECT 열 목록
   FROM 첫번째 테이블
   	INNER JOIN 두번째 테이블
   	ON 조인 조건
   WHERE 검색 조건
   
   SELECT *
   	FROM buyTBL
   		INNER JOIN userTBL
   			ON buyTBL.userID = userTBL.userID
   	WHERE buyTBL.userID = 'JYP' OR buyTBL.userID = 'BBK';
   	
   SELECT B.userID, U.userName, B.prodName, U.addr FROM buyTBL B
       INNER JOIN userTBL U
           ON B.userID = U.userID
       ORDER BY U.userID;
   ```

2. OUTER JOIN

   ```SQL
   -- 한쪽에만 내용이 있어도 그 결과가 표시되는 조인
   LEFT : 왼쪽 테이블은 모두 출력
   ```

   

