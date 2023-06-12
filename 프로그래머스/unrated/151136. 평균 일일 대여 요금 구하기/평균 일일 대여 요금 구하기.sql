-- 코드를 입력하세요
SELECT ROUND(AVG(daily_fee)) AVERAGE_FEE 
FROM CAR_RENTAL_COMPANY_CAR 
WHERE 1=1
    AND car_type = 'SUV'
GROUP BY car_type