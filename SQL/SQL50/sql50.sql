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