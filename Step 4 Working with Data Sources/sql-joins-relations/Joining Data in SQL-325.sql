## 1. Introducing Joins ##

select * from facts
INNER JOIN cities
ON facts.id=cities.facts_id
limit 10

## 2. Understanding Inner Joins ##

select c.*, f.name country_name
from facts f
inner join cities c
on f.id=c.facts_id
limit 5

## 3. Practicing Inner Joins ##

SELECT f.name country, c.name capital_city from cities c
inner join facts f
on f.id=c.facts_id
where c.capital=1

## 4. Left Joins ##

SELECT f.name country, f.population
from facts f
left join cities c
on f.id=c.facts_id
where c.name is null

## 6. Finding the Most Populous Capital Cities ##

select c.name capital_city,f.name country ,c.population population
from facts f
inner join cities c
on f.id=c.facts_id
where c.capital=1
order by 3 DESC
limit 10

## 7. Combining Joins with Subqueries ##

SELECT c.name capital_city,f.name country, c.population population
from facts f
inner join (select * from cities where population>10000000 and capital=1) c
on c.facts_id=f.id
order by 3 desc

## 8. Challenge: Complex Query with Joins and Subqueries ##

SELECT f.name country,c.urban_pop, f.population total_pop, (c.urban_pop/cast(f.population as float)) urban_pct
from facts f
inner join (select facts_id,sum(population) urban_pop from cities group by 1) c
on f.id=c.facts_id
where urban_pct > 0.5
order by 4 asc