# Write your MySQL query statement below
SELECT managing.name
  FROM Employee managing
  JOIN Employee managed
    ON managing.id = managed.managerId
 GROUP BY managing.id
HAVING COUNT(managing.id) >= 5