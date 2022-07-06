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

## How to Access Databases Using Python

- The two main concepts in the Python DB-API are connection objects and query objects. 

  - You use connection objects to connect to a database and manage your transactions. 
  - Cursor objects are used to run queries. 
    - Cursors are used to scan through the results of a database. 

- These connection methods are: 

  - The cursor() method, which returns a new cursor object using the connection. 

  - The commit() method, which is used to commit any pending transaction to the database. 

  - The rollback() method, which causes the database to roll back to the start of any pending transaction. 

  - The close() method, which is used to close a database connection. 

- Cursors created from the same connection are not isolated 

  - that is, any changes done to the database by a cursor are immediately visible by the other cursors. 

- Cursors created from different connections can or cannot be isolated depending on how the transaction support is implemented.

- A database cursor is a control structure that enables traversal over the records in a database.

- 파이썬에서 db 연결하는 법

  - ```python
    #Replace the placeholder values with your actual Db2 hostname, username, and password:
    
    dsn_hostname = "YourDb2Hostname" # e.g.: "54a2f15b-5c0f-46df-8954-7e38e612c2bd.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud"
    dsn_uid = "YourDb2Username"        # e.g. "abc12345"
    dsn_pwd = "YoueDb2Password"      # e.g. "7dBZ3wWt9XN6$o0J"
    
    dsn_driver = "{IBM DB2 ODBC DRIVER}"
    dsn_database = "BLUDB"            # e.g. "BLUDB"
    dsn_port = "YourPort"                # e.g. "32733" 
    dsn_protocol = "TCPIP"            # i.e. "TCPIP"
    dsn_security = "SSL"              #i.e. "SSL"
    
    dsn = (
        "DRIVER={0};"
        "DATABASE={1};"
        "HOSTNAME={2};"
        "PORT={3};"
        "PROTOCOL={4};"
        "UID={5};"
        "PWD={6};"
        "SECURITY={7};").format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd,dsn_security)
    
    #print the connection string to check correct values are specified
    print(dsn)
    
    try:
        conn = ibm_db.connect(dsn, "", "")
        print ("Connected to database: ", dsn_database, "as user: ", dsn_uid, "on host: ", dsn_hostname)
    
    except:
        print ("Unable to connect: ", ibm_db.conn_errormsg() )
        
    # 연결 되었는지 확인
    #Retrieve Metadata for the Database Server
    server = ibm_db.server_info(conn)
    
    print ("DBMS_NAME: ", server.DBMS_NAME)
    print ("DBMS_VER:  ", server.DBMS_VER)
    print ("DB_NAME:   ", server.DB_NAME)
    
    # 커넥션 닫기
    ibm_db.close(conn)
    ```

- 파이썬으로 쿼리하기

  - ```python
    # To create a table, we use the ibm_db.exec_immediate function
    
    # 먼저 드랍하기
    #Lets first drop the table INSTRUCTOR in case it exists from a previous attempt
    dropQuery = "drop table INSTRUCTOR"
    
    #Now execute the drop statment
    dropStmt = ibm_db.exec_immediate(conn, dropQuery)
    
    
    # 만들기
    #Construct the Create Table DDL statement - replace the ... with rest of the statement
    createQuery = "create table INSTRUCTOR(\
                            ID INTEGER PRIMARY KEY NOT NULL, \
                            FNAME VARCHAR(20), \
                            LNAME VARCHAR(20), \
                            CITY VARCHAR(20), \
                            CCODE CHAR(2))"
    
    createStmt = ibm_db.exec_immediate(conn, createQuery)
    
    insertQuery = "insert into INSTRUCTOR values (1, 'Rav', 'Ahuja', 'TORONTO', 'CA')"
    
    insertStmt = ibm_db.exec_immediate(conn, insertQuery)
    
    insertQuery2 = "insert into INSTRUCTOR values (2, 'Raul', 'Chong', 'Markham', 'CA'), (3, 'Hima', 'Vasudevan', 'Chicago', 'US')"
    
    insertStmt2 = ibm_db.exec_immediate(conn, insertQuery2)
    
    #Construct the query that retrieves all rows from the INSTRUCTOR table
    selectQuery = "select * from INSTRUCTOR"
    
    #Execute the statement
    selectStmt = ibm_db.exec_immediate(conn, selectQuery)
    
    #Fetch the Dictionary (for the first row only)
    ibm_db.fetch_both(selectStmt)
    
    #Fetch the rest of the rows and print the ID and FNAME for those rows
    while ibm_db.fetch_row(selectStmt) != False:
        print (" ID:",  ibm_db.result(selectStmt, 0), " FNAME:", ibm_db.result(selectStmt, "FNAME"))
    
        
    updateQuery = "update INSTRUCTOR set CITY='MOOSETOWN' where FNAME='Rav'"
    updateStmt = ibm_db.exec_immediate(conn, updateQuery)
    ```

- 파이썬으로 디비 읽고 판다스 객체로 사용하기

  - ```python
    import pandas
    import ibm_db_dbi
    #connection for pandas
    pconn = ibm_db_dbi.Connection(conn)
    
    #query statement to retrieve all rows in INSTRUCTOR table
    selectQuery = "select * from INSTRUCTOR"
    
    #retrieve the query results into a pandas dataframe
    pdf = pandas.read_sql(selectQuery, pconn)
    
    #print just the LNAME for first row in the pandas data frame
    pdf.LNAME[0]
    
    #print the entire data frame
    pdf
    
    pdf.shape
    
    ibm_db.close(conn)
    ```

- 주피터 노트북에서 sql 가져다 쓰기

  - ```python
    %sql ibm_db_sa://vhp94362:bMOGnon8hfhk6M4r@19af6446-6171-4641-8aba-9dcff8e1b6ff.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud:30699/BLUDB?security=SSL
                
    # 이런식으로 입력하면 댐
    
    %%sql
    
    CREATE TABLE INTERNATIONAL_STUDENT_TEST_SCORES (
    	country VARCHAR(50),
    	first_name VARCHAR(50),
    	last_name VARCHAR(50),
    	test_score INT
    );
    INSERT INTO INTERNATIONAL_STUDENT_TEST_SCORES (country, first_name, last_name, test_score)
    VALUES
    ('United States', 'Marshall', 'Bernadot', 54),
    ('Ghana', 'Celinda', 'Malkin', 51),
    ('Ukraine', 'Guillermo', 'Furze', 53),
    ('Greece', 'Aharon', 'Tunnow', 48),
    ('Russia', 'Bail', 'Goodwin', 46),
    ('Poland', 'Cole', 'Winteringham', 49),
    ('Sweden', 'Emlyn', 'Erricker', 55),
    ('Russia', 'Cathee', 'Sivewright', 49),
    ('China', 'Barny', 'Ingerson', 57),
    ('Uganda', 'Sharla', 'Papaccio', 55),
    ('China', 'Stella', 'Youens', 51),
    ('Poland', 'Julio', 'Buesden', 48),
    ('United States', 'Tiffie', 'Cosely', 58),
    ('Poland', 'Auroora', 'Stiffell', 45),
    ('China', 'Clarita', 'Huet', 52),
    ('Poland', 'Shannon', 'Goulden', 45),
    ('Philippines', 'Emylee', 'Privost', 50),
    ('France', 'Madelina', 'Burk', 49),
    ('China', 'Saunderson', 'Root', 58),
    ('Indonesia', 'Bo', 'Waring', 55),
    ('China', 'Hollis', 'Domotor', 45),
    ('Russia', 'Robbie', 'Collip', 46),
    ('Philippines', 'Davon', 'Donisi', 46),
    ('China', 'Cristabel', 'Radeliffe', 48),
    ('China', 'Wallis', 'Bartleet', 58),
    ('Moldova', 'Arleen', 'Stailey', 38),
    ('Ireland', 'Mendel', 'Grumble', 58),
    ('China', 'Sallyann', 'Exley', 51),
    ('Mexico', 'Kain', 'Swaite', 46),
    ('Indonesia', 'Alonso', 'Bulteel', 45),
    ('Armenia', 'Anatol', 'Tankus', 51),
    ('Indonesia', 'Coralyn', 'Dawkins', 48),
    ('China', 'Deanne', 'Edwinson', 45),
    ('China', 'Georgiana', 'Epple', 51),
    ('Portugal', 'Bartlet', 'Breese', 56),
    ('Azerbaijan', 'Idalina', 'Lukash', 50),
    ('France', 'Livvie', 'Flory', 54),
    ('Malaysia', 'Nonie', 'Borit', 48),
    ('Indonesia', 'Clio', 'Mugg', 47),
    ('Brazil', 'Westley', 'Measor', 48),
    ('Philippines', 'Katrinka', 'Sibbert', 51),
    ('Poland', 'Valentia', 'Mounch', 50),
    ('Norway', 'Sheilah', 'Hedditch', 53),
    ('Papua New Guinea', 'Itch', 'Jubb', 50),
    ('Latvia', 'Stesha', 'Garnson', 53),
    ('Canada', 'Cristionna', 'Wadmore', 46),
    ('China', 'Lianna', 'Gatward', 43),
    ('Guatemala', 'Tanney', 'Vials', 48),
    ('France', 'Alma', 'Zavittieri', 44),
    ('China', 'Alvira', 'Tamas', 50),
    ('United States', 'Shanon', 'Peres', 45),
    ('Sweden', 'Maisey', 'Lynas', 53),
    ('Indonesia', 'Kip', 'Hothersall', 46),
    ('China', 'Cash', 'Landis', 48),
    ('Panama', 'Kennith', 'Digance', 45),
    ('China', 'Ulberto', 'Riggeard', 48),
    ('Switzerland', 'Judy', 'Gilligan', 49),
    ('Philippines', 'Tod', 'Trevaskus', 52),
    ('Brazil', 'Herold', 'Heggs', 44),
    ('Latvia', 'Verney', 'Note', 50),
    ('Poland', 'Temp', 'Ribey', 50),
    ('China', 'Conroy', 'Egdal', 48),
    ('Japan', 'Gabie', 'Alessandone', 47),
    ('Ukraine', 'Devlen', 'Chaperlin', 54),
    ('France', 'Babbette', 'Turner', 51),
    ('Czech Republic', 'Virgil', 'Scotney', 52),
    ('Tajikistan', 'Zorina', 'Bedow', 49),
    ('China', 'Aidan', 'Rudeyeard', 50),
    ('Ireland', 'Saunder', 'MacLice', 48),
    ('France', 'Waly', 'Brunstan', 53),
    ('China', 'Gisele', 'Enns', 52),
    ('Peru', 'Mina', 'Winchester', 48),
    ('Japan', 'Torie', 'MacShirrie', 50),
    ('Russia', 'Benjamen', 'Kenford', 51),
    ('China', 'Etan', 'Burn', 53),
    ('Russia', 'Merralee', 'Chaperlin', 38),
    ('Indonesia', 'Lanny', 'Malam', 49),
    ('Canada', 'Wilhelm', 'Deeprose', 54),
    ('Czech Republic', 'Lari', 'Hillhouse', 48),
    ('China', 'Ossie', 'Woodley', 52),
    ('Macedonia', 'April', 'Tyer', 50),
    ('Vietnam', 'Madelon', 'Dansey', 53),
    ('Ukraine', 'Korella', 'McNamee', 52),
    ('Jamaica', 'Linnea', 'Cannam', 43),
    ('China', 'Mart', 'Coling', 52),
    ('Indonesia', 'Marna', 'Causbey', 47),
    ('China', 'Berni', 'Daintier', 55),
    ('Poland', 'Cynthia', 'Hassell', 49),
    ('Canada', 'Carma', 'Schule', 49),
    ('Indonesia', 'Malia', 'Blight', 48),
    ('China', 'Paulo', 'Seivertsen', 47),
    ('Niger', 'Kaylee', 'Hearley', 54),
    ('Japan', 'Maure', 'Jandak', 46),
    ('Argentina', 'Foss', 'Feavers', 45),
    ('Venezuela', 'Ron', 'Leggitt', 60),
    ('Russia', 'Flint', 'Gokes', 40),
    ('China', 'Linet', 'Conelly', 52),
    ('Philippines', 'Nikolas', 'Birtwell', 57),
    ('Australia', 'Eduard', 'Leipelt', 53)
    
    # 와 걍 이거도 되네
    
    country = "Canada"
    %sql select * from INTERNATIONAL_STUDENT_TEST_SCORES where country = :country
    # 파이썬 변수 앞에 : 붙여주면 됨
    
    test_score_distribution = %sql SELECT test_score as "Test Score", count(*) as "Frequency" from INTERNATIONAL_STUDENT_TEST_SCORES GROUP BY test_score;
    test_score_distribution
    # 이렇게도 가능
    
    # 위에서 만든 쿼리를 df로 바로 바꾸기
    
    dataframe = test_score_distribution.DataFrame()
    
    %matplotlib inline
    # uncomment the following line if you get an module error saying seaborn not found
    # !pip install seaborn==0.9.0
    import seaborn
    
    plot = seaborn.barplot(x='Test Score',y='Frequency', data=dataframe)
    ```

- 두번째 예제

  - ```python
    import pandas
    chicago_socioeconomic_data = pandas.read_csv('https://data.cityofchicago.org/resource/jcxq-k9xf.csv')
    %sql PERSIST chicago_socioeconomic_data
    
    # The PERSIST command in SQL "magic" simplifies the process of table creation and writing the data from a pandas dataframe into the table
    
    # 여러가지 select 해보기
    
    %sql SELECT COUNT(*) FROM chicago_socioeconomic_data;
    
    %sql SELECT COUNT(*) FROM chicago_socioeconomic_data WHERE hardship_index > 50.0;
    
    %sql SELECT MAX(hardship_index) FROM chicago_socioeconomic_data;
    
    #We can use the result of the last query to as an input to this query:
    %sql SELECT community_area_name FROM chicago_socioeconomic_data where hardship_index=98.0
    
    #or another option:
    %sql SELECT community_area_name FROM chicago_socioeconomic_data ORDER BY hardship_index DESC NULLS LAST FETCH FIRST ROW ONLY;
    
    #or you can use a sub-query to determine the max hardship index:
    %sql select community_area_name from chicago_socioeconomic_data where hardship_index = ( select max(hardship_index) from chicago_socioeconomic_data ) 
    
    %sql SELECT community_area_name FROM chicago_socioeconomic_data WHERE per_capita_income_ > 60000;
    ```

  - 시각화 하기

    ```python
    # 시각화
    
    import matplotlib.pyplot as plt
    %matplotlib inline
    import seaborn as sns
    
    income_vs_hardship = %sql SELECT per_capita_income_, hardship_index FROM chicago_socioeconomic_data;
    plot = sns.jointplot(x='per_capita_income_',y='hardship_index', data=income_vs_hardship.DataFrame())
    ```

- Summary

  - You can access a database from a language like Python by using the appropriate API. Examples include ibm_db API for IBM DB2, psycopg2 for ProstgreSQL, and dblib API for SQL Server.
  - DB-API is Python's standard API for accessing relational databases. It allows you to write a single program that works with multiple kinds of relational databases instead of writing a separate program for each one.
  - The DB_API  connect constructor creates a connection to the database and returns a Connection Object, which is then used by the various connection methods.
  - The connection methods are: The cursor() method, which returns a new cursor object using the connection. The commit() method, which is used to commit any pending transaction to the database. The rollback() method, which causes the database to roll-back to the start of any pending transaction. The close() method, which is used to close a database connection. 
  - You can use **SQL Magic** commands to execute queries more easily from Jupyter Notebooks.  Magic commands have the general format **%sql select \* from tablename**. **Cell magics** start with a double %% (percent) sign and apply to the entire cell. **Line magics** start with a single % (percent) sign and apply to a particular line in a cell.