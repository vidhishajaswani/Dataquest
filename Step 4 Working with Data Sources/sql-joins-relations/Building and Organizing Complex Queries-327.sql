## 3. The With Clause ##

WITH playlist_info AS
    (
    SELECT
    playlist.playlist_id,
    playlist.name playlist_name,
    track.name track_name,
    (track.milliseconds/1000) length_seconds
    FROM playlist
    LEFT JOIN playlist_track ON playlist_track.playlist_id=playlist.playlist_id
    LEFT JOIN track ON playlist_track.track_id=track.track_id
        
    )
SELECT playlist_id,playlist_name, COUNT(track_name) number_of_tracks, SUM(length_seconds) length_seconds from playlist_info
GROUP by 1,2
order by 1

## 4. Creating Views ##

CREATE VIEW chinook.customer_gt_90_dollars AS
    SELECT c.* FROM chinook.invoice i
    INNER JOIN chinook.customer c
    ON i.customer_id=c.customer_id
    GROUP BY 1
    HAVING sum(i.total)>90;
    
SELECT * FROM chinook.customer_gt_90_dollars;

## 5. Combining Rows With Union ##

SELECT * from chinook.customer_usa 
UNION
SELECT * FROM chinook.customer_gt_90_dollars

## 6. Combining Rows Using Intersect and Except ##

CREATE VIEW chinook.customers_usa_gt_90_view AS
    SELECT * from chinook.customer_usa 
    INTERSECT
    SELECT * FROM chinook.customer_gt_90_dollars;


SELECT e.first_name || " " || e.last_name employee_name,
        COUNT(c.customer_id) customers_usa_gt_90
FROM employee e
left join customers_usa_gt_90_view c
on e.employee_id=c.support_rep_id
where e.title='Sales Support Agent'
group by 1
order by 1

## 7. Multiple Named Subqueries ##

WITH
india AS (SELECT * FROM customer where country="India"),
sum_total AS (SELECT customer_id,sum(total) total from invoice GROUP by 1)


SELECT
    ci.first_name || " " || ci.last_name customer_name,
    spc.total total_purchases
FROM india ci
INNER JOIN sum_total spc ON ci.customer_id = spc.customer_id
ORDER BY 1;




## 8. Challenge: Each Country's Best Customer ##

WITH 
    totals as (select i.customer_id, c.country, sum(i.total) total_purchased from invoice i inner join customer c on c.customer_id=i.customer_id group by 1,2),
    max_from_totals as (SELECT country,max(total_purchased) max_purchase from totals group by country),
    country_best_customer as (SELECT mft.country, mft.max_purchase max_purchase, (select customer_id from totals where totals.country=mft.country and totals.total_purchased=mft.max_purchase) customer_id from max_from_totals mft)
    
    
SELECT
    cbc.country country,
    c.first_name || " " || c.last_name customer_name,
    cbc.max_purchase total_purchased
FROM customer c
INNER JOIN country_best_customer cbc ON cbc.customer_id = c.customer_id
ORDER BY 1 ASC