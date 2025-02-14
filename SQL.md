# **Problem-Solving Strategy:**

- Read the problem carefully.
- Clarify return constraints, is there a demanded order, rounding etc.?
- Does the table need to be joined with itself?


## Functions I am not aware of:

### Series Generation:

```sql
SELECT generate_series('2023-01-01'::date, '2023-12-31'::date, '1 month'::interval);

SELECT generate_series('2023-01-01'::date, '2023-01-31'::date, '1 day'::interval);
  

WITH hours_cte(hour_of_day) AS (
    SELECT generate_series(0, 23)
)
SELECT hour_of_day
FROM hours_cte;


```

## REGEX

```sql
select (REGEXP_MATCH(distance, '\d+\.?\d*'))[1]::numeric as distance
```

## Casts

```sql
If you need to specifically cast something, use ::numeric or ::float or ::timestamp

or ::text

```

## GROUP_CONCAT, STRING_SPLIT and therelike

Using PostGreSQL, here are some string functions to work with:
```sql
string_to_array(string, delimiter) -- example string_to_array('1, 2, 3', ',') creates {1, 2, 3}
unnest(ARRAY[1, 2, 3])::int as topping_id -- creates three rows
string_agg(column, delimiter) -- combines multiple rows into one string, e.g. string_agg(name, ',') might create 'John, Mary, Steve'

```

Window Functions:

ROW_NUMBER()
RANK()
DENSE_RANK()
LAG() and LEAD()
FIRST_VALUE() and LAST_VALUE()

Aggregation Functions:

COUNT(DISTINCT)
STRING_AGG()
PERCENTILE_CONT()
MEDIAN()

String Manipulation:

SUBSTRING()
CONCAT()
REPLACE()
TRIM()
LOWER() and UPPER()

Date/Time Functions:

DATE_TRUNC()
EXTRACT()
INTERVAL
NOW()
DATEADD()

Advanced Functions:

COALESCE()
NULLIF()
GREATEST()
LEAST()
CASE statements

Performance/Optimization:

EXPLAIN ANALYZE
Subquery optimization
Indexing strategies

Analytical Functions:

NTILE()
CUME_DIST()
PERCENT_RANK()


## SET Operations:

- UNION, INTERSECT and DIFFERENCE need the same columns for joining together.
- UNION does not keep duplicates! UNION ALL keeps it.
- INTERSECT only returns rows that match from botch sides
- DIFFERENCE would return only rows which are NOT in both tables

## NULLS

SQL can not count or do comparisons with NULL values. These need to be handled specifically.

To incoroprate customers which might not end up in a filter table, you can do:

```sql

select customer_id, coalesce(change_counter, 0) as counter
from all_customers -- which is defined via a CTE
left join changes using  (customer_id)

```


## SELECT
```sql
select distinct building_name, role
from buildings
left join employees on building_name = building
```
will product distinct PAIRS of building_names and roles!

## Conditions

use AND and OR. 
is not NULL
is NULL
NOT in ('usa', 'canada')
!= (<>) both work

#### Usage of IN:

where skill in ('Python', 'Tableau', 'PostgreSQL')

#### Usage of BETWEEN

where skill_level between 5 and 10

## JOINS:

Simple joins could be like:

```sql
select * from
customer_orders
join pzza_names
USING (pizza_id)
```

This removes double columns!


LEFT JOIN: Returns ALL rows from the left table and inserts NULLs where there is no entry from the right table.

RIGHT JOIN: Returns ALL rows from the right table and inserts NULLs where there is no entry from the left table.

INNER JOIN: Returns rows which have entries in BOTH tables, so only matchin rows.

CROSS JOIN: Creates a cartesian-product of tables, so all rows from one table are matched with all rows from the other table - does not need a joining condition.

SELF JOIN (with aliases): Lets you create joins with only one table - usually with aliases to make a differentiation.

You can use multiple conditions on joins.

## Aggregations

Return a single value, examples: MAX, MIN, AVG, SUM, COUNT.

Aggregations can not be nested! No max(count( ...). order by and then limit for the max element

####  you cannot use aggregate functions like COUNT() directly in a WHERE clause.

Others include ROUND(EXPRESSION, decimals) and CAST(value AS DECIMAL):

```sql
ROUND(SUM(CAST(units * price AS DECIMAL)) / SUM(units), 2) AS average_price
```

### Using AGGREGATIONS or HAVING, demand you to have all non-aggregated select fields in the group by clause!


## Filters

WHERE looks at every row, so this is used BEFORE grouping.
HAVING looks at every group. So you need to group first.

Filter text with:

```sql
WHERE city LIKE 'New%' # starts with New

WHERE city LIKE '%x%' # contains x

WHERE city LIKE '_r%' # second letter is r
```


## CASE Statements

```sql
CASE
  WHEN cost < 100 then 'cheap'
  WHEN cost between 100 and 200 then 'mid-tier'
  else 'luxury' end as product_type
```

SQL supports modulo function!

```sql
select
    p.product_id, 
    case 
        when sum(u.units) is null then 0
        else round(sum(u.units * p.price) / sum(u.units), 2)
    end as average_price
from prices p
left join unitssold u
on p.product_id = u.product_id
and u.purchase_date between p.start_date and p.end_date
group by p.product_id
```

## DATE Functions

Between dates include the boundaries.
To take the last 30 days including a certain last date, starting from a certain date you can do:

```sql
SELECT activity_date AS day, COUNT(DISTINCT user_id) AS active_users
FROM activity
WHERE activity_date BETWEEN DATE_SUB('2019-07-27', INTERVAL 29 DAY) AND '2019-07-27'
GROUP BY activity_date;
```
Why 29? Well because you want the last day included, which then results in the date_sub of 29 - the 29 days before it. Since the boundaries are included, this gives you the last 30 days.


### Get part of a timestamp
```sql
select DATE_PART('hour' from order_time)

-- Gets the hour, can also be month, day, minute
```

### Get the day of the week:

```sql
SELECT 
    order_time,
    EXTRACT(DOW FROM order_time) as day_number,
    TO_CHAR(order_time, 'Day') as day_name
FROM customer_orders;

```

### Creating a custom week starting at a certain point:
```sql
-- How many runners signed up for each 1 week period? (i.e. week starts 2021-01-01)

select count(runner_id) , 
((registration_date - date('2021-01-01')) / 7 ) + 1 as week
from runners
group by week
order by week asc
```

### Getting the minutes of a timestamp difference:

```sql
select runner_id, avg(extract(epoch from (pickup_time::timestamp - order_time)) / 60) as time_diff
```


### Getting Unique Items:

```sql
Select num
from numbers
group by num
having count(num) = 1

```
