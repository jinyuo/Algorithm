# Write your MySQL query statement below
SELECT Register.contest_id
     , ROUND(count(Users.user_id) / (SELECT count(1) FROM Users) * 100, 2) AS percentage
  FROM Register
  JOIN Users
    ON Register.user_id = Users.user_id
 GROUP BY Register.contest_id  
 ORDER BY percentage DESC
      , Register.contest_id ASC