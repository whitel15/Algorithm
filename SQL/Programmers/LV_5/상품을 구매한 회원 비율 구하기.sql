SELECT DATE_FORMAT(A.SALES_DATE, "%Y") AS YEAR,
DATE_FORMAT(A.SALES_DATE, "%m") AS MONTH,
COUNT(DISTINCT B.USER_ID) AS PUCHASED_USERS,
ROUND(COUNT(DISTINCT B.USER_ID)/(SELECT COUNT(*) FROM USER_INFO WHERE JOINED LIKE "2021%"), 1) AS PUCHASED_RATIO
FROM ONLINE_SALE A
JOIN USER_INFO B ON A.USER_ID = B.USER_ID
WHERE JOINED LIKE "2021%"
GROUP BY YEAR, MONTH
ORDER BY YEAR, MONTH