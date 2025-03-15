# Write your MySQL query statement below
WITH cte (id) AS (
  	SELECT min(id)
      FROM Person
     GROUP BY email
)
DELETE FROM Person
 WHERE TRUE
   AND id NOT IN (SELECT * FROM cte)