SELECT ONLINE_SALE.USER_ID, ONLINE_SALE.PRODUCT_ID
FROM ONLINE_SALE 
JOIN
    (SELECT USER_ID, PRODUCT_ID, count(SALES_DATE) as cnt_sale
    FROM ONLINE_SALE
    GROUP BY USER_ID, PRODUCT_ID) cnt
    ON ONLINE_SALE.USER_ID = cnt.USER_ID 
    AND ONLINE_SALE.PRODUCT_ID = cnt.PRODUCT_ID
WHERE 1=1
    AND cnt_sale > 1
GROUP BY USER_ID, PRODUCT_ID
ORDER BY ONLINE_SALE.USER_ID ASC, ONLINE_SALE.PRODUCT_ID DESC