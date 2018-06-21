## 1. Introduction ##


SELECT COUNT(Major) FROM recent_grads WHERE ShareWomen < 0.5

## 2. Finding a Column's Minimum and Maximum Values in SQL ##


SELECT Major, Major_category, MIN(Median) 
FROM recent_grads
WHERE Major_category='Engineering'

## 3. Calculating Sums and Averages in SQL ##


Select SUM(Total) from recent_grads

## 4. Combining Multiple Aggregation Functions ##


SELECT AVG(Total), MIN(Men), MAX(Women) FROM recent_grads

## 5. Customizing The Results ##


SELECT COUNT(*) "Number of Majors", MAX(Unemployment_rate) "Highest Unemployment Rate" FROM recent_grads

## 6. Counting Unique Values ##


SELECT COUNT(DISTINCT(Major)) unique_majors, COUNT(DISTINCT(Major_category)) unique_major_categories, COUNT(DISTINCT(Major_code)) unique_major_codes
FROM recent_grads

## 7. Performing Arithmetic in SQL ##


SELECT Major, Major_category, (P75th - P25th) quartile_spread FROM recent_grads ORDER BY quartile_spread LIMIT 20