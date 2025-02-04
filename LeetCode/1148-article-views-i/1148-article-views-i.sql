# Write your MySQL query statement below
SELECT author_id AS id
  FROM Views
 WHERE TRUE
   AND author_id = viewer_id
GROUP BY id
ORDER BY id