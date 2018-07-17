select extract(month from payment_date) as month,
       count(payment_id) as total_count,
       sum(amount) as total_amount,
       sum(case when staff_id = 1 then 1 else 0 end) as mike_count,    
       sum(case when staff_id = 1 then amount else 0 end) as mike_amount, 
       sum(case when staff_id = 2 then 1 else 0 end) as jon_count, 
       sum(case when staff_id = 2 then amount else 0 end) as jon_amount, 
from payment 
group by month 
order by month
