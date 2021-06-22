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

4. order by 뒤에는 having 을 where 대신 쓰면 됨

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
     hh24:mi:ss
     
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

9. 

