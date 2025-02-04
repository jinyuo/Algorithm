# Write your MySQL query statement below
SELECT name
  FROM Customer
 WHERE TRUE
   AND referee_id != 2
    OR referee_id is null