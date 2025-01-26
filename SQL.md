# Learnings in January:


- UNION, INTERSECT and DIFFERENCE need the same columns for joining together.
- UNION does not keep duplicates! UNION ALL keeps it.
- INTERSECT only returns rows that match from botch sides
- DIFFERENCE would return only rows which are NOT in both tables
  

## JOINS:

LEFT JOIN: Returns ALL rows from the left table and inserts NULLs where there is no entry from the right table.

RIGHT JOIN: Returns ALL rows from the right table and inserts NULLs where there is no entry from the left table.

INNER JOIN: Returns rows which have entries in BOTH tables, so only matchin rows.

CROSS JOIN: Creates a cartesian-product of tables, so all rows from one table are matched with all rows from the other table - does not need a joining condition.

SELF JOIN (with aliases): Lets you create joins with only one table - usually with aliases to make a differentiation.


