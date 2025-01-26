# **Problem-Solving Strategy:**

- Read the problem carefully.
- Clarify return constraints, is there a demanded order, rounding etc.?
- Does the table need to be joined with itself?


## Learnings in January:

- UNION, INTERSECT and DIFFERENCE need the same columns for joining together.
- UNION does not keep duplicates! UNION ALL keeps it.
- INTERSECT only returns rows that match from botch sides
- DIFFERENCE would return only rows which are NOT in both tables

## NULLS

SQL can not count or do comparisons with NULL values. These need to be handled specifically.


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

## JOINS:

LEFT JOIN: Returns ALL rows from the left table and inserts NULLs where there is no entry from the right table.

RIGHT JOIN: Returns ALL rows from the right table and inserts NULLs where there is no entry from the left table.

INNER JOIN: Returns rows which have entries in BOTH tables, so only matchin rows.

CROSS JOIN: Creates a cartesian-product of tables, so all rows from one table are matched with all rows from the other table - does not need a joining condition.

SELF JOIN (with aliases): Lets you create joins with only one table - usually with aliases to make a differentiation.

You can use multiple conditions on joins.

## Aggregations

Return a single value, examples: MAX, MIN, AVG, SUM, COUNT.

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

SQL supports modulo function!



