select rank() over (order by sum(points) desc) as rank, 
  coalesce(nullif(clan, ''), '[no clan specified]') as clan,
  sum(points) as total_points, 
  count(name) as total_people
from people
group by clan
