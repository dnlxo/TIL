## 저장 프로시저

- SQL Server에서 제공하는 프로그래밍 기능

- RETURN 문 사용가능

- 오류처리도 가능

- ```sql
  CREATE PROCEDURE usp_users1
  	@userName NVARCHAR(10) -- 매개변수 타입 정의
  AS
  	SELECT * FROM userTbl WHERE name = @userName;
  GO -- GO를 경계로 일괄처리(batch)가 구분된다.
  
  EXEC usp_users1 '위태영'; -- 실행부
  ```

- ```sql
  CREATE PROCEDURE usp_users2
  	@userBirth INT = 1995, -- 디폴트 값 설정 가능
  	@userHeight INT
  AS
  	SELECT * FROM userTbl
  	WHERE birthYear > @userBirth AND height > @userHeight;
  GO
  
  EXEC usp_users2 1995, 183;
  ```

- ```sql
  CREATE PROCEDURE usp_users3
  	@txtValue NCHAR(10), -- 입력 매개변수
  	@outValue INT OUTPUT -- 출력 매개변수
  AS
  	INSERT INTO testTbl VALUES(@txtValue);
  	SELECT @outValue = IDENT_CURRENT('testTbl'); -- 테이블의 현재 identity 값
  GO
  
  CREATE TABLE testTbl (id INT IDENTITY, txt NCHAR(10));
  GO
  
  DECLARE @myValue INT;
  EXEC usp_users4 '테스트 값1', @myValue OUTPUT;
  PRINT '현재 입력된 ID 값 ==> ' + CAST(@myValue AS CHAR(5));
  ```

- ```sql
  CREATE PROC usp_ifElse
  	@userName NVARCHAR(10)
  AS
  	DECLARE @bYear INT
  	SELECT @bYear = birthYear FROM userTbl
  		WHERE name = @userName;
  	IF (@bYear >= 1980)
  		BEGIN
  			PRINT '고고'
  		END
  	ELSE
  		BEGIN
  			PRINT 'not go'
  		END
  GO
  ```

- ```sql
  CREATE PROC usp_case
  	@userName NVARCHAR(10)
  AS
  	DECLARE @bYear INT
  	DECLARE @tti NCHAR(3)
  	SELECT @bYear = birthYear FROM userTbl
  		WHERE name = @userName;
  	
  	SET @tti = 
  		CASE
  			WHEN ( @bYear%12 = 0) THEN '원숭이'
  			-- 어쩌고 저쩌고
  			ELSE '양'
  		END;
  	PRINT @userName + '의 띠는' + @tti;
  GO
  
  EXEC usp_case '위태영'
  ```

- ```sql
  ALTER TABLE userTbl
  	ADD grade NVARCHAR(5); -- 고객 등급 column 추가
  
  CREATE PROCEDURE usp_while
  AS
  	DECLARE userCur CURSOR FOR -- 커서 선언
  		SELECT U.userid, sum(price*amount)
  		FROM buyTbl B
  			RIGHT OUTER JOIN userTbl U
  			ON B.userid = U.userid
  		GROUP BY U.userid, U.name
  	
  	OPEN userCur -- 커서 열기
  
  	DECLARE @id NVARCHAR(10)
  	DECLARE @sum BIGINT
  	DECLARE @userGrade NCHAR(5)
  	
  	FETCH NEXT FROM userCur INTO @id, @sum
  	
  	WHILE (@@FETCH_STATUS=0)
  	BEGIN
  		SET @userGrade =
  			CASE
  				WHEN (@sum >= 1500) THEN '최우수'
  				WHEN (@sum >= 1000) THEN '우수'
  				WHEN (@sum >= 1) THEN '일반'
  				ELSE '유령'
  			END
  		UPDATE userTbl SET grade = @userGrade WHERE userID = @id
  		FETCH NEXT FROM userCur INTO @id, @sum
  	END
  ```

- 데이터베이스 커서

  - 일련의 데이터에 순차적으로 액세스할 때 검색 및 "현재 위치"를 포함하는 데이터 요소.

- decimal(numeric) 과 float 차이점

  - decimal은 정확한 값
  - float, real은 근사값
  - 값 비교 시에는 decimal 사용할 것

- ```sql
  -- 리턴 문 이용해보기
  CREATE PROC usp_return
  	@userName NVARCHAR(10)
  AS
  	DECLARE @userID char(8);
  	SELECT @userID = userID FROM userTbl
  		WHERE name = @userName;
  	IF (@userID <> '')
  		RETURN 0;
  	ELSE
  		RETURN -1;
  
  DECLARE @retVal INT;
  EXEC @retVal=usp_return '위태영';
  SELECT @retVal;
  ```

- ```sql
  -- 에러처리
  @@ERROR 값이 0이면 정상
  0이 아니면 오류번호를 돌려준다.
  ```

- ```sql
  -- 에러처리 TRY/CATCH
  BEGIN TRY
  	구문
  END TRY
  
  BEGIN CATCH
  	구문
  	SELECT ERROR_NUMBER()
  	SELECT ERROR_MESSAGE()
  END CATCH
  ```

- ```sql
  -- 프로시저 보는법
  -- 텍스트로 결과보기 클릭
  
  USE sqlDB;
  SELECT o.name, m.definition
  FROM sys.sql_modules m
  	JOIN sys.objects o
  	ON m.object_id = o.object_id AND o.TYPE = 'P';
  
  EXECUTE sp_helptext 프로시저이름; -- 하나씩 볼때
  ```

- MS SQL에서 'N'의 의미

  - 'N' 안붙이면 유니코드 깨짐

- 