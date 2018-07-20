with recursive Fibonacci (number, number2) as
(select 0::bigint, 1::bigint 
  union all
  select number2::bigint, number + number2::bigint
  from Fibonacci)
  
select number 
from Fibonacci
limit 90
