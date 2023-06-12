-- 코드를 입력하세요
SELECT BOOK_ID, DATE_FORMAT(PUBLISHED_DATE, '%Y-%m-%d') AS PUBLISHED_DATE
FROM BOOK
WHERE 1=1
    AND DATE_FORMAT(PUBLISHED_DATE, '%Y') = '2021'
    AND CATEGORY = '인문'
ORDER BY PUBLISHED_DATE