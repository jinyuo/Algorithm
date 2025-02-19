# Write your MySQL query statement below
SELECT A.product_id
     , IFNULL(ROUND(SUM(A.price * A.units) / SUM(A.units), 2), 0) AS average_price
  FROM (SELECT Prices.product_id
             , CASE WHEN UnitsSold.purchase_date BETWEEN Prices.start_date AND Prices.end_date THEN Prices.price ELSE 0 END AS price
             , CASE WHEN UnitsSold.purchase_date BETWEEN Prices.start_date AND Prices.end_date THEN UnitsSold.units ELSE 0 END AS units
          FROM Prices
          LEFT JOIN UnitsSold
            ON Prices.product_id = UnitsSold.product_id) AS A
GROUP BY A.product_id