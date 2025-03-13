# Write your MySQL query statement below
SELECT x
     , y
     , z
     , IF(x + y + z - greatest(x, y, z) > greatest(x, y, z), 'Yes', 'No') AS triangle 
FROM Triangle