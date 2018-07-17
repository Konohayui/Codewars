-- Create your SELECT statement here
select * 
from(
select 'US' as location, * from ussales
union all
select 'EU' as location, * from eusales
) as all_sales
where all_sales.price > 50.00
