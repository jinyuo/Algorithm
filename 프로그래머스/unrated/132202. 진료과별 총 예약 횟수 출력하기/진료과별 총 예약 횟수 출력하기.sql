-- 코드를 입력하세요
SELECT MCDP_CD AS '진료과코드', count(1) AS '5월예약건수'
FROM APPOINTMENT 
WHERE 1=1
    AND (year(APNT_YMD) = 2022 AND month(APNT_YMD) = 5)
GROUP BY MCDP_CD
ORDER BY 5월예약건수 ASC, 진료과코드 ASC
;