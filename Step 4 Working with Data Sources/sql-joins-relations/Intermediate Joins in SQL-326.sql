## 2. Joining Three Tables ##

SELECT i.track_id track_id, t.name track_name, m.name track_type, t.unit_price unit_price, i.quantity quantity
from invoice_line i
inner join track t on i.track_id=t.track_id
inner join media_type m on t.media_type_id=m.media_type_id
where invoice_id=4

## 3. Joining More Than Three Tables ##

SELECT i.track_id track_id, t.name track_name,artist.name artist_name, m.name track_type, t.unit_price unit_price, i.quantity quantity
from invoice_line i
inner join track t on i.track_id=t.track_id
inner join media_type m on t.media_type_id=m.media_type_id
inner join album a on a.album_id=t.album_id
inner join artist on artist.artist_id=a.artist_id
where invoice_id=4

## 4. Combining Multiple Joins with Subqueries ##

SELECT
    a.album_title album,
    a.artist_name artist,
    count(*) tracks_purchased
from invoice_line
inner join ( select t.track_id, al.title album_title, ar.name artist_name from track t INNER JOIN album al ON al.album_id = t.album_id
                INNER JOIN artist ar ON ar.artist_id = al.artist_id) a
on invoice_line.track_id=a.track_id
group by 1,2
ORDER BY 3 desc LIMIT 5;

## 5. Recursive Joins ##

SELECT e1.first_name || " " || e1.last_name employee_name, e1.title employee_title,
       e2.first_name || " " || e2.last_name supervisor_name,
       e2.title supervisor_title
from employee e1
left join employee e2 
on e1.reports_to=e2.employee_id
order by 1

## 6. Pattern Matching Using Like ##

SELECT first_name, last_name, phone
from customer
where first_name like '%Belle%'

## 7. Generating Columns With The Case Statement ##

SELECT c.first_name || " " || c.last_name customer_name, 
count(i.invoice_id ) number_of_purchases, 
sum(i.total) total_spent,
CASE
    WHEN sum(i.total) < 40 THEN 'small spender'
    WHEN sum(i.total) > 100 THEN 'big spender'
    ELSE 'regular'
    END
    as customer_category
    
from invoice i
inner join customer c
on i.customer_id=c.customer_id
group by 1
order by 1
    