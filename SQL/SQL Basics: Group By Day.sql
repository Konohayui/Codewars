select cast(created_at as date) as day,
  description,
  count(id) as "count"
from events
where name = 'trained'
group by day, description
