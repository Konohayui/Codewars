-- Create your SELECT statement here
select 
  p.id, 
  p.name,
  count(s.sale) as sale_count,
  Rank() over(order by count(s.sale)) as sale_rank
from people p
join sales s on s.people_id = p.id
group by p.id
