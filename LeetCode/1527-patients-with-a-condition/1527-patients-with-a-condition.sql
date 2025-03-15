# Write your MySQL query statement below
SELECT patient_id
     , patient_name
     , conditions   
  FROM Patients
 WHERE TRUE
   AND conditions REGEXP '^DIAB1| DIAB1'
