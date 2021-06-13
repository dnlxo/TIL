CREATE TABLE userTBL
( userID CHAR(8) NOT NULL PRIMARY KEY,
userName NVARCHAR2(10) NOT NULL,
birthYear NUMBER(4) NOT NULL,
addr NCHAR(2) NOT NULL,
mobile1 CHAR(3),
mobile2 CHAR(8),
height NUMBER(3),
mDate DATE
);

CREATE TABLE buyTBL
( idNum NUMBER(8) NOT NULL PRIMARY KEY,
userID CHAR(8) NOT NULL,
prodName NCHAR(6) NOT NULL,
groupName NCHAR(4),
price NUMBER(8) NOT NULL,
amount NUMBER(3) NOT NULL,
FOREIGN KEY (userID) REFERENCES userTBL(userID)
);

INSERT INTO userTBL VALUES('LSG', '이승기', 1987, '서울', '011', '11111111', 182, '2008-8-8');
INSERT INTO userTBL VALUES('KBS', '김범수', 1979, '경남', '011', '22222222', 173, '2012-4-4');
INSERT INTO userTBL VALUES('KKH', '김경호', 1971, '전남', '019', '33333333', 177, '2007-7-7');
INSERT INTO userTBL VALUES('JYP', '조용필', 1950, '경기', '011', '44444444', 166, '2009-4-4');
INSERT INTO userTBL VALUES('SSK', '성시경', 1979, '서울', NULL, NULL, 186, '2013-12-12');
INSERT INTO userTBL VALUES('LJB', '임재범', 1963, '서울', '016', '66666666', 182, '2009-9-9');
INSERT INTO userTBL VALUES('YJS', '윤종신', 1969, '경남', NULL, NULL, 170, '2005-5-5');
INSERT INTO userTBL VALUES('EJW', '은지원', 1972, '경북', '011', '88888888', 174, '2014-3-3');
INSERT INTO userTBL VALUES('JKW', '조관우', 1965, '경기', '018', '99999999', 172, '2010-10-10');
INSERT INTO userTBL VALUES('BBK', '바비킴', 1973, '서울', '010', '00000000', 176, '2013-5-5');

CREATE SEQUENCE idSEQ; -- 순차번호 입력을 위해서 시퀀스 생성
INSERT INTO buyTBL VALUES(idSEQ.NEXTVAL, 'KBS', '운동화', NULL, 30, 2);
INSERT INTO buyTBL VALUES(idSEQ.NEXTVAL, 'KBS', '노트북', '전자', 1000, 1);
INSERT INTO buyTBL VALUES(idSEQ.NEXTVAL, 'JYP', '모니터', '전자', 200, 1);
INSERT INTO buyTBL VALUES(idSEQ.NEXTVAL, 'BBK', '모니터', '전자', 200, 5);
INSERT INTO buyTBL VALUES(idSEQ.NEXTVAL, 'KBS', '청바지', '의류', 50, 3);
INSERT INTO buyTBL VALUES(idSEQ.NEXTVAL, 'BBK', '메모리', '전자', 80, 10);
INSERT INTO buyTBL VALUES(idSEQ.NEXTVAL, 'SSK', '책', '서적', 15, 5);
INSERT INTO buyTBL VALUES(idSEQ.NEXTVAL, 'EJW', '책', '서적', 15, 2);
INSERT INTO buyTBL VALUES(idSEQ.NEXTVAL, 'EJW', '청바지', NULL, 50, 1);
INSERT INTO buyTBL VALUES(idSEQ.NEXTVAL, 'BBK', '운동화', NULL, 30, 2);
INSERT INTO buyTBL VALUES(idSEQ.NEXTVAL, 'EJW', '책', '서적', 15, 1);
INSERT INTO buyTBL VALUES(idSEQ.NEXTVAL, 'BBK', '운동화', NULL, 30, 2);

COMMIT;
SELECT * FROM userTBL;
SELECT * FROM buyTBL;

SELECT * FROM userTBL WHERE userName = '김경호' OR userName = '은지원';
SELECT * FROM userTBL WHERE birthYear >= 1970 AND height >= 182;
SELECT userid, username FROM userTBL WHERE birthYear >= 1970 AND height >= 182;
SELECT username, height FROM userTBL WHERE height BETWEEN 180 AND 183;
SELECT username, height FROM userTBL WHERE height <= 183 AND height >= 180;
SELECT userName, addr FROM userTBL WHERE addr IN ('경남', '전남', '경북') ;

SELECT userName, height FROM userTBL WHERE userName LIKE '김%';
SELECT userName, height FROM userTBL WHERE userName LIKE '_종신';
SELECT userName, height FROM userTBL WHERE userName LIKE '_종_';


SELECT userName, height FROM userTBL
	WHERE height > (SELECT height FROM userTBL WHERE userName = '김경호');

SELECT rownum, userName, height FROM userTBL
	WHERE height >= ANY (SELECT height FROM userTBL WHERE addr = '경남');
    
SELECT rownum, userName, height FROM userTBL
	WHERE height >= ALL (SELECT height FROM userTBL WHERE addr = '경남');
    
SELECT userName, height FROM userTBL
	WHERE height IN (SELECT height FROM userTBL WHERE addr = '경남');

SELECT * FROM buyTBL;
SELECT userID, SUM(amount) FROM buyTBL GROUP BY userID ORDER BY userID;
SELECT userID AS 아이디, SUM(amount) AS 총수량 FROM buyTBL GROUP BY userID;
SELECT userID AS 아이디, SUM(price*amount) AS 총구매가격 FROM buyTBL GROUP BY userID;
    
SELECT userName, height FROM userTBL 
    WHERE height = (SELECT MAX(height) FROM userTBL) 
        OR height = (SELECT MIN(height) FROM userTBL)
    ORDER BY height DESC;
    
SELECT COUNT(*) FROM userTBL;
SELECT * FROM userTBL;

SELECT userID AS 아이디, SUM(price*amount) AS 총구매가격 FROM buyTBL GROUP BY userID
HAVING SUM(price*amount) >= 1000;
    
SELECT idNum, groupName, SUM(price*amount) AS "비용"
	FROM buyTBL
	GROUP BY ROLLUP (groupName, idNum);    

SELECT groupName, SUM(price*amount) AS 비용, GROUPING_ID(groupName) AS 추가행인가
	FROM buyTBL
	GROUP BY ROLLUP(groupName);
    
CREATE TABLE cubeTBL(prodName NCHAR(3), color NCHAR(2), amount INT);
INSERT INTO cubeTBL VALUES('컴퓨터', '검정', 11);
INSERT INTO cubeTBL VALUES('컴퓨터', '파랑', 22);
INSERT INTO cubeTBL VALUES('모니터', '검정', 33);
INSERT INTO cubeTBL VALUES('모니터', '검정', 44);
SELECT prodName, color, SUM(amount) AS "수량합계"
    FROM cubeTBL
    GROUP BY CUBE (color, prodName)
    ORDER BY prodName, color;
    WITH abc(userID, total)
AS
( SELECT userID, SUM(price*amount)
	FROM buyTBL GROUP BY userID)
SELECT * FROM abc ORDER BY total DESC;

CREATE TABLE EMPTBL ( EMP NCHAR(3), MANAGER NCHAR(3), DEPARTMENT NCHAR(3));
INSERT INTO EMPTBL VALUES('나사장', '없음', '없음');
INSERT INTO EMPTBL VALUES('김재무', '나사장', '재무부');
INSERT INTO EMPTBL VALUES('김부장', '김재무', '내무부');
INSERT INTO EMPTBL VALUES('이부장', '김재무', '재무부');
INSERT INTO EMPTBL VALUES('우대리', '이부장', '재무부');
INSERT INTO EMPTBL VALUES('지사원', '이부장', '재무부');
INSERT INTO EMPTBL VALUES('이영업', '나사장', '영업부');
INSERT INTO EMPTBL VALUES('한과장', '이영업', '영업부');
INSERT INTO EMPTBL VALUES('최정보', '나사장', '정보부');
INSERT INTO EMPTBL VALUES('윤차장', '최정보', '정보부');
INSERT INTO EMPTBL VALUES('이주임', '윤차장', '정보부');

WITH empCTE(empName, mgrName, dept, empLevel)
AS
( 
	(SELECT emp, manager, department, 0
		FROM empTBL
		WHERE manager = '없음')
	UNION ALL
	(SELECT empTBL.emp, empTBL.manager, empTBL.department, empCTE.empLevel + 1
    	FROM empTBL INNER JOIN empCTE
    		ON empTBL.manager = empCTE.empName)
)
SELECT * FROM empCTE ORDER BY dept, empLevel;

SELECT * FROM BUYTBL;

UPDATE buyTBL SET PRICE = PRICE * 1.5 ;

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

MERGE INTO memberTBL M --M 테이블을 변경
	USING (SELECT changeType, userID, userName, addr FROM changeTBL) C -- C 테이블을 참고해서
	ON (M.userID = C.userID) -- 두 테이블을 userID를 기준으로 비교
	WHEN MATCHED THEN
		UPDATE SET M.addr = C.addr -- 동일한 이름이 있으면 주소 변경
		DELETE WHERE C.changeType = '회원탈퇴' -- 근데 회원탈퇴였으면 지우셈
	WHEN NOT MATCHED THEN -- 이름 없으면 추가
		INSERT (userID, userName, addr) VALUES(C.userID, C.userName, C.addr);