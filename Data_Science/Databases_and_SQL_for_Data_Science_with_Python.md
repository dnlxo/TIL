## SQL

- Structured English Query Language

- A database is a repository of data. It is a program that stores data. 

- A database also provides the functionality for adding, modifying, and querying that data

- Create a table

- Insert data to populate the table

- Select data from the table

- Update data in the table

- Delete data from the table

- The main purpose of a database management system, is not just to store the data but also facilitate retrieval of the data

- The SELECT statement is a data manipulation language statement.

  - Data Manipulation Language statements or DML statements are used to read and modify data

- The INSERT statement is one of the data manipulation language statements

  - ```
    INSERT INTO AUTHOR
    	(AUTHOR_ID, LASTNAME, FIRSTNAME, EMAIL, CITY, COUNTRY)
    VALUES
    	('A1', 'CHONG', 'RAUL', 'RFC@IBM.COM', 'TORONTO', 'CA')
    	('B1', 'PENWG', 'RCSE', 'AAD@IBM.COM', 'TODDDO', 'CV')
    ```

- The UPDATE statement is one of the data manipulation language

  - After a table is created and populated with data, the data in a table can be altered with the UPDATE statement

  - ```
    UPDATE [TableName] 
    SET [ColumnName] = [Value]
    WHERE [Condition]
    ```

  - Note that if you do not specify the WHERE clause, all the rows in the table will be updated

- The DELETE statement is one of the data manipulation language

  - ```
    DELETE FROM [TABLEName]
    WHERE [Condition]
    ```

  - Note that if you do not specify the WHERE clause, all the rows in the table will be removed

### Database

- Advantages of using cloud databases
  - Ease of Use and Management
  - Scalability
  - Disaster Recovery
  - Cost and paying for only the resources you utilize
- SQL statements fall into two different categories
  - DDL
  - DML
- Common DDL statement types include CREATE, ALTER, TRUNCATE, and DROP.
  - CREATE: which is used for creating tables and defining its columns; 
  - ALTER: is used for altering tables including adding and dropping columns and modifying their datatypes; 
  - TRUNCATE: is used for deleting data in a table but not the table itself; 
  - DROP: is used for deleting tables
- Data Manipulation Language (or DML) statements are used to read and modify data in tables
  - These are also sometimes referred to as CRUD operations
    - Create, Read, Update and Delete
  - Common DML statement types include INSERT, SELECT, UPDATE, and DELETE
    - INSERT: is used for inserting a row or several rows of data into a table;
    - SELECT: reads or selects row or rows from a table;
    - UPDATE: edits row or rows in a table;
    - DELETE: removes a row or rows of data from a table.

- summary

  - DDL are used for defining or changing objects in a database such as tables.
  - DML are used for manipulating or working with data in tables

- DELETE 명령어는 데이터는 지워지지만 테이블 용량은 줄어 들지 않는다. 원하는 데이터만 지울 수 있다. 삭제 후 잘못 삭제한 것을 되돌릴 수 있다.

- TRUNCATE 명령어는 용량이 줄어 들고, 인덱스 등도 모두 삭제 된다. 테이블은 삭제하지는 않고, 데이터만 삭제한다. 한꺼번에 다 지워야 한다. 삭제 후 절대 되돌릴 수 없다.

- DROP 명령어는 데이블 전체를 삭제, 공간, 객체를 삭제한다. 삭제 후 절대 되돌릴 수 없다.

- ```sql
  -- create 구문 예시
  CREATE TABLE table_name (
      column1 datatype,
      column2 datatype,
      column3 datatype,
      ...
  	);
  	
  create table COUNTRY (
  	ID int NOT NULL,
  	CCODE char(2),
  	NAME varchar(60),
  	PRIMARY KEY (ID)
  	);
  ```

- ```sql
  -- alter 구문 예시
  ALTER TABLE table_name
  ADD COLUMN column_name data_type column_constraint;
  
  ALTER TABLE table_name
  DROP COLUMN column_name;
  
  ALTER TABLE table_name
  ALTER COLUMN column_name SET DATA TYPE data_type;
  
  ALTER TABLE table_name
  RENAME COLUMN current_column_name TO new_column_name;
  ```

- ``` sql
  -- truncate 구문 예시
  TRUNCATE TABLE table_name;
  ```

- ```sql
  -- drop 구문 예시
  drop table table_name;
  ```

- ```sql
  -- 실습
  CREATE TABLE PETSALE (
      ID INTEGER NOT NULL,
      PET CHAR(20),
      SALEPRICE DECIMAL(6,2),
      PROFIT DECIMAL(6,2),
      SALEDATE DATE
      );
      
  CREATE TABLE PET (
      ID INTEGER NOT NULL,
      ANIMAL VARCHAR(20),
      QUANTITY INTEGER
      );
      
  INSERT INTO PETSALE VALUES
      (1,'Cat',450.09,100.47,'2018-05-29'),
      (2,'Dog',666.66,150.76,'2018-06-01'),
      (3,'Parrot',50.00,8.9,'2018-06-04'),
      (4,'Hamster',60.60,12,'2018-06-11'),
      (5,'Goldfish',48.48,3.5,'2018-06-14');
      
  INSERT INTO PET VALUES
      (1,'Cat',3),
      (2,'Dog',4),
      (3,'Hamster',2);
      
  ALTER TABLE PETSALE
  ADD COLUMN QUANTITY INTEGER;
  
  UPDATE PETSALE SET QUANTITY = 9 WHERE ID = 1;
  UPDATE PETSALE SET QUANTITY = 3 WHERE ID = 2;
  UPDATE PETSALE SET QUANTITY = 2 WHERE ID = 3;
  UPDATE PETSALE SET QUANTITY = 6 WHERE ID = 4;
  UPDATE PETSALE SET QUANTITY = 24 WHERE ID = 5;
  
  ALTER TABLE PETSALE
  DROP COLUMN PROFIT;
  
  ALTER TABLE PETSALE
  ALTER COLUMN PET SET DATA TYPE VARCHAR(20);
  
  ALTER TABLE PETSALE
  RENAME COLUMN PET TO ANIMAL;
  
  TRUNCATE TABLE PET IMMEDIATE;
  
  DROP TABLE PET;
  ```

- SUMMARY

  - A database is a repository of data that provides functionality for adding, modifying, and querying the data. 
  - SQL is a language used to query or retrieve data from a relational database. 
  - The Relational Model is the most used data model for databases because it allows for data independence. 
  - The primary key of a relational table uniquely identifies each tuple or row, preventing duplication of data and providing a way of defining relationships between tables. 
  - SQL statements fall into two different categories: Data Definition Language (DDL) statements and Data Manipulation Language (DML) statements.

## WHERE 절

```sql
SELECT * FROM tbl WHERE col LIKE '정규표현식'
SELECT * FROM tbl WHERE col IN(1,2,3)
```

- 순서는 order by

  - 여러개 줄 수 있다.

  - 원하는 순서에 따라서 순서대로...

  - ```sql
    order by dep_id desc, l_name;
    -- 이런식으로
    ```

- group by

  - having
  - count()

- ```sql
  -- group by 예제
  -- 부서 별 평균연봉
  SELECT DEP_ID, COUNT(*), AVG(SALARY)
  FROM EMPLOYEES
  GROUP BY DEP_ID;
  ```

- where 절에 함께 쓰는 함수들 (db2)

  - UCASE()
  - LCASE()
  - 등등

### SUBQUERY

```sql
-- fail
select * 
from employees 
where salary < AVG(salary);

-- answer
select EMP_ID, F_NAME, L_NAME, SALARY 
from employees 
where SALARY < (select AVG(SALARY) 
                from employees);
```

```sql
-- fail
select EMP_ID, SALARY, MAX(SALARY) AS MAX_SALARY 
from employees;	

-- answer
select EMP_ID, SALARY, ( select MAX(SALARY) from employees ) AS MAX_SALARY 
from employees;
```

- INNER JOIN
  - 기준 테이블, join 테이블에 모두 데이터가 존재해야 보임
- OUTER JOIN
  - 기준 테이블에만 존재하면 됨
- CROSS JOIN
  - 카르테시안 곱
  - 모든 경우의 수