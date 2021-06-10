## SQL 기본

SQL : 데이터베이스에서 사용되는일종의 공통언어

- ANSI/ISO SQL : 모든 DBMS의 공통 SQL 표준

DBMS들은 ANSI-92/99 SQL의 내용을 포함하면서 각자의 특징을 반영하는 내용이 포함된, 확장된 SQL 문들을 사용한다.

- PL/SQL : 오라클에서 사용되는 확장된 SQL

---

## 기본적인 SQL 문 4가지

- SELECT

  - 가장 많이 사용되는 구문

  - 데이터베이스 내의 테이블에서 원하는 정보를 추출하는 명령

    ```sql
    -- 가장 기본
    SELECT 열 이름
    FROM 테이블이름 (원래는 스키마이름.테이블이름)
    WHERE 조건
    
    -- 사용자 조회
    SELECT * FROM SYS.DBA_USERS;
    
    -- HR 사용자에 있는 테이블의 정보 조회
    SELECT * FROM SYS.DBA_TABLES WHERE OWNER = 'HR';
    
    -- HR.departments 테이블의 컬럼이 무엇무엇이 있나
    SELECT * FROM SYS.DBA_TAB_COLUMNS WHERE OWNER = 'HR' AND TABLE_NAME = 'DEPARTMENTS';
    
    -- 열 이름 별칭 지정하기
    SELECT department_id 부서번호, department_name AS "부서 이름" FROM HR.departments;
    -- AS는 생략 가능하며, 별칭의 중간에 공백이 있다면 큰 따옴표 처리 해줘야 함
    ```

---

## 실습에 사용할 스키마, 테이블 만들기

1. 사용자 만들기

   ```sql
   CREATE USER sqlDB IDENTIFIED BY 1234
       DEFAULT TABLESPACE USERS
       TEMPORARY TABLESPACE TEMP;
   ```

2. 역할 부여하기 (connect, resource, dba)

   ```sql
   GRANT connect, resource, dba TO sqlDB;
   ```

3. 테이블 만들기

   ```sql
   -- 회원 테이블
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
   
   -- 회원 구매 테이블
   CREATE TABLE buyTBL
   ( idNum NUMBER(8) NOT NULL PRIMARY KEY,
   userID CHAR(8) NOT NULL,
   prodName NCHAR(6) NOT NULL,
   groupName NCHAR(4),
   price NUMBER(8) NOT NULL,
   amount NUMBER(3) NOT NULL,
   FOREIGN KEY (userID) REFERENCES userTBL(userID) -- 외래 키 부여
   );
   
   -- CHAR, VARCHAR2 : 영문자 기준으로 1바이트 할당 >>> 영어나 숫자
   -- NCHAR, NVARCHAR2 : 유니코드 기준 2바이트 할당 >>> 한글
   -- NUMBER : 정수형
   ```

   > 데이터베이스 개체에 이름을 줄 때 따라야 할 규칙
   >
   > - 알파벳과 숫자, #$_를 사용할 수 있다.
   > - 기본 설정은 대문자로 생성된다.
   > - 식별자(스키마 개체의 이름)는 영문자로 시작해야한다.
   > - 개체 이름은 최대 30자
   > - 데이터베이스 이름은 8자
   > - 예약어 사용 금지
   > - 원칙적으로 공백 사용 금지, 꼭 사용해야 한다면 큰 따옴표 붙여서

4. 테이블에 데이터 입력

   ```SQL
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
   ```

5. 테이블에 데이터 입력

   ```SQL
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
   ```

6. 입력한 데이터 커밋, 데이터 확인해보기

   ```SQL
   COMMIT;
   SELECT * FROM userTBL;
   SELECT * FROM buyTBL;
   ```

---

