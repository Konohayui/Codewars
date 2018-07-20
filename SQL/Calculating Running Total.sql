select created_at::timestamp::date as date,
       count(title) as count, 
       sum(count(title)::int) over (order by created_at::timestamp::date) as total
from posts 
group by date
order by date
