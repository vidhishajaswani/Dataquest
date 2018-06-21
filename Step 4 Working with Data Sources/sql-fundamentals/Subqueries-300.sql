## 2. Subqueries ##

SELECT Major, Unemployment_rate
from recent_grads
where Unemployment_rate< (SELECT AVG(Unemployment_rate) from recent_grads)
order by Unemployment_rate ASC

## 3. Subquery In SELECT ##

SELECT CAST(COUNT(*) AS FLOAT)/CAST((SELECT COUNT(*) FROM recent_grads) AS FLOAT) proportion_abv_avg
from recent_grads
where ShareWomen> (SELECT AVG(ShareWomen) from recent_grads)


## 4. Returning Multiple Results In Subqueries ##

SELECT Major, Major_category
from recent_grads
where Major_category in (select Major_category from recent_grads
                         group by Major_category
                         order by sum(Total) desc
                         limit 5)


## 5. Building Complex Subqueries ##

select AVG(cast(Sample_size as float)/cast(Total as float)) avg_ratio
from recent_grads


## 6. Practice Integrating A Subquery With The Outer Query ##

SELECT Major, Major_category, (cast(Sample_size as float)/cast(Total as float)) ratio
from recent_grads
where ratio>(select AVG(cast(Sample_size as float)/cast(Total as float)) avg_ratio from recent_grads)