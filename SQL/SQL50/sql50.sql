# Write your MySQL query statement below

SELECT machine_id, ROUND(AVG(processing_time), 3) AS processing_time
FROM (
    SELECT machine_id, process_id, ROUND(SUM(timestamp), 3) AS processing_time
    FROM (
        SELECT machine_id, process_id, CASE WHEN activity_type = 'start' THEN -ROUND(timestamp, 3) ELSE ROUND(timestamp, 3) END AS timestamp
        FROM Activity
    ) a
    GROUP BY 1, 2
) b
GROUP BY 1
;

-- 셀프조인을 좀 활용하자 CTE, 섭쿼리 말고..

SELECT a1.machine_id, ROUND(AVG(a2.timestamp - a1.timestamp),3) as processing_time
FROM Activity a1
inner join Activity a2
on a1.process_id = a2.process_id
and a1.machine_id = a2.machine_id
and a1.timestamp < a2.timestamp
GROUP BY machine_id
;

-- 성능은 비슷하네..

SELECT user_id, ROUND(COUNT(CASE WHEN action ='confirmed' THEN 1 END) / COUNT(*), 2) confirmation_rate
FROM Signups s
LEFT JOIN Confirmations c
USING (user_id)
GROUP BY 1
;

SELECT user_id, ROUND(AVG(IF(action ='confirmed', 1, 0)), 2) confirmation_rate
FROM Signups s
LEFT JOIN Confirmations c
USING (user_id)
GROUP BY 1
;

--
-- 결론적으로, IFNULL과 COALESCE의 성능 차이는 대부분의 상황에서 무시할 만한 수준입니다. 
-- 따라서 성능보다는 가독성, 유지보수성, 그리고 특정 상황에 더 적합한 함수를 선택하는 것이 중요합니다.

-- WHERE 절에 2개 컬럼 넣기.. 를 잘 써볼까

# Write your MySQL query statement below
SELECT ROUND(COUNT(DISTINCT b.player_id) / COUNT(DISTINCT a.player_id), 2) AS fraction
FROM (SELECT *, ROW_NUMBER() OVER (PARTITION BY player_id ORDER BY event_date) rn FROM Activity) a
LEFT JOIN Activity b 
ON a.player_id = b.player_id AND a.event_date = DATE_SUB(b.event_date, INTERVAL 1 DAY) AND rn = 1
;

# Write your MySQL query statement below
SELECT
    ROUND(COUNT(*)/(SELECT COUNT(DISTINCT player_id) FROM Activity),2) AS fraction
FROM activity 
WHERE (player_id,DATE_SUB(event_date, INTERVAL 1 DAY)) IN (SELECT player_id,min(event_date) FROM Activity GROUP BY player_id)
;


-- COUNT(*), COUNT(0), COUNT(컬럼명)의 성능 차이에 대해 설명드리겠습니다:

-- COUNT(*):

-- 모든 행을 카운트합니다 (NULL 포함).
-- 일반적으로 가장 빠른 성능을 보입니다.
-- 옵티마이저가 가장 효율적인 방법으로 처리합니다.


-- COUNT(0):

-- COUNT(*)와 동일한 결과를 반환합니다.
-- 대부분의 데이터베이스 시스템에서 COUNT(*)와 성능이 동일합니다.
-- 일부 오래된 MySQL 버전에서는 약간의 성능 차이가 있을 수 있지만, 최신 버전에서는 무시할 만한 수준입니다.


-- COUNT(컬럼명):

-- 지정된 컬럼의 NULL이 아닌 값만 카운트합니다.
-- NULL 체크가 필요하므로 COUNT(*)보다 일반적으로 느립니다.
-- 인덱스된 컬럼을 사용할 경우, 성능이 향상될 수 있습니다.



-- 성능 비교:

-- 일반적으로: COUNT(*) ≈ COUNT(0) > COUNT(컬럼명)
-- 대부분의 경우 COUNT(*)과 COUNT(0)의 성능 차이는 무시할 만한 수준입니다.
-- COUNT(컬럼명)은 NULL 체크로 인해 추가적인 작업이 필요하므로 상대적으로 느릴 수 있습니다.

-- 
--
-- 역시나 셀프 조인을 잘쓰자

# Write your MySQL query statement below

SELECT m.employee_id, m.name, COUNT(e.employee_id) AS reports_count, ROUND(AVG(e.age)) AS average_age
FROM Employees e
INNER JOIN Employees m
ON e.reports_to = m.employee_id
GROUP BY 1, 2
ORDER BY 1

-- 둘 중 뭐가더 좋을까

-- -- -- # Write your MySQL query statement below

SELECT person_name FROM Queue WHERE turn = (
    SELECT MAX(turn) FROM (
        SELECT turn, SUM(weight) OVER (ORDER BY turn) AS sum
        FROM Queue
    ) a WHERE sum <= 1000
)

SELECT person_name 
FROM (
    SELECT person_name, turn, SUM(weight) OVER (ORDER BY turn) AS sum
    FROM Queue
) a 
WHERE sum <= 1000
ORDER BY turn DESC
LIMIT 1

-- 일반적으론 밑에께 좋대


