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