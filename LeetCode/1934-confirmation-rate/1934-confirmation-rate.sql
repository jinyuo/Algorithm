# Write your MySQL query statement below
SELECT Signups.user_id
     , ROUND(IFNULL(SUM(CASE Confirmations.action WHEN 'confirmed' THEN 1 ELSE 0 END), 0) / COUNT(Signups.user_id), 2) AS confirmation_rate
FROM Signups
LEFT JOIN Confirmations
ON Signups.user_id = Confirmations.user_id
GROUP BY Signups.user_id