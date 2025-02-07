# Write your MySQL query statement below
SELECT b.id
  FROM Weather a
  JOIN Weather b
    ON a.recordDate = DATE_ADD(b.recordDate, INTERVAL -1 DAY)
 WHERE TRUE
   AND a.temperature < b.temperature