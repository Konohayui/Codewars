-- Replace with your query (in pure SQL)
select c.customer_id, 
  c.email, 
  count(p.payment_id) as payments_count,
  cast(sum(p.amount) as float) as total_amount
from customer as c 
join payment as p on p.customer_id = c.customer_id
group by c.customer_id
order by total_amount desc
limit 10
