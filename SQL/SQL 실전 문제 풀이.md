## SQL 실전 문제 풀이

1. 상위 몇 개 줄 출력
   - 서브쿼리 생성 후
   - where rownum 을 통해 출력

2. 개수 세기

   - ```sql
     SELECT COUNT(mobile1) FROM userTBL;
     -- mobile1 열의 값이 NULL 인 행을 제외하고 COUNT 한다.
     ```

3. 중복은 하나로 치기

   - distinct 셀렉트 뒤에 붙이면 됨

4. group by 뒤에는 having 을 where 대신 쓰면 됨

   - ```sql
     select name, count(name) from animal_ins group by name having name != 'null' and count(name) >= 2 order by name
     ```

5. group by 를 잘 하자

6. 날짜형식 바꾸기 (datetime type)

   - ```sql
     -- datetime 열이 있다. 타입은 datetime
     -- 형식은 2013-12-22 11:30:00 이런 식이다.
     -- 바꾸는 법?
     
     TO_CHAR(날짜열이름, '형식')
     하면 되고, 24시간 표시하고싶으면 hh24 쓰면 됨
     yyyy-mm-dd hh24:mi:ss
     
     -- 예제
     select 
     	TO_NUMBER(hour) HOUR, count(animal_id) COUNT 
     from 
     	(select 
        		animal_id, TO_CHAR(datetime, 'HH24') hour 
        from 
        		animal_outs) 
     group by hour 
     	having hour >= 9 and hour <= 19
     		order by hour
     ```

7. dual 과 connect by level

   - ```sql
     -- 연속된 빈 테이블이 필요할 때
     select 
     		level-1, 
     		null 
     from 
     		dual 
     connect by level <= 24
     
     >>> 0 부터 23 까지 행 생성
     
     -- 예제
     
     select 
         a.hour, nvl(b.count, 0) count
     from (select level-1 hour, null count from dual connect by level <= 24) a
         left outer join (select TO_NUMBER(hour) HOUR, count(animal_id) COUNT from (select animal_id, TO_CHAR(datetime, 'HH24') hour from animal_outs) group by hour order by hour) b
         on a.hour = b.hour
         order by hour
     ```

8. null 처리 방법

   - ```sql
     SELECT NVL(Column명, "Null일 경우 대체 값") FROM 테이블명; 
     ```

   - null 의 경우 비교연산자 안먹으니까 is null, is not null 로 하세요

9. where like 절

   - ```sql
     select animal_id, animal_type, name from 테이블 
     where 
     sex_upon_intake like 'Intact%' and (sex_upon_outcome like 'Spayed%' or sex_upon_outcome like 'Neutered%') order by animal_id
     ```

   - ```sql
     -- 위랑 같은 여러개 like
     where
     sex_upon_intake like 'Intact%' and regexp_like(sex_upon_outcome, 'Spayed|Neutered') order by animal_id
     ```

10. String, Date 처리

    - where ~~ in (~~)

    ```sql
    select animal_id, name, sex_upon_intake from animal_ins
    where name in ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty') order by animal_id
    ```

    - 대소문자 구분해야할 때?

    ```sql
    select animal_id, name from animal_ins where animal_type = 'Dog' and regexp_like(name, 'el|EL|eL|El') order by name
    
    -- 위처럼 하기 보다는? 테이블을 모두 대문자로 바꾸거나 소문자로 바꾼뒤
    
    select animal_id, name from animal_ins where animal_type = 'Dog' and UPPER(name) like '%EL%' order by name
    ```

    - 조건에 따라 조회할 때 열추가 할때

    ```sql
    -- 코드를 입력하세요
    SELECT animal_id, name,
    case when SEX_UPON_INTAKE like '%Intact%' then 'X' else 'O' end 중성화
    from animal_ins order by animal_id
    ```

    - 각 행의 데이터를 기반으로 열 추가

    ```sql
    select animal_id, name, outtime - intime as 시간 from 테이블
    -- 데이터 as 컬럼명
    ```

    

