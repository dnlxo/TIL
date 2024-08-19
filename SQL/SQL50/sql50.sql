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

--

