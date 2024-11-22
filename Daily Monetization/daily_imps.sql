WITH Display_Result AS (SELECT t1.Dimension_DATE, 
       t1.Creative_Type, 
       SUM(t1.Impressions) AS Impressions
FROM Daily t1
JOIN (
    SELECT Creative_Type, SUM(Impressions) AS Impressions
    FROM Daily
    WHERE Dimension_DATE = '2024-11-18' AND Creative_Type = 'Display'
    GROUP BY Creative_Type
) t2
ON t1.Creative_Type = t2.Creative_Type
WHERE t1.Creative_Type = 'Display'
GROUP BY t1.Dimension_DATE, t1.Creative_Type
HAVING SUM(t1.Impressions) > t2.Impressions
ORDER BY t1.Dimension_DATE DESC
LIMIT 1),

Video_Result AS (
    SELECT t1.Dimension_DATE, 
       t1.Creative_Type, 
       SUM(t1.Impressions) AS Impressions
FROM Daily t1
JOIN (
    SELECT Creative_Type, SUM(Impressions) AS Impressions
    FROM Daily
    WHERE Dimension_DATE = '2024-11-18' AND Creative_Type = 'Pre Roll'
    GROUP BY Creative_Type
) t2
ON t1.Creative_Type = t2.Creative_Type
WHERE t1.Creative_Type = 'Pre Roll'
GROUP BY t1.Dimension_DATE, t1.Creative_Type
HAVING SUM(t1.Impressions) > t2.Impressions
ORDER BY t1.Dimension_DATE DESC
LIMIT 1
)

SELECT * FROM Display_Result
UNION ALL
SELECT * FROM Video_Result
ORDER BY Dimension_DATE DESC;
