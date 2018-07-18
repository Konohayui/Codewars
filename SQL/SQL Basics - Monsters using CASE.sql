select t.id,
  heads,
  legs,
  arms,
  tails,
  case when heads > arms or tails > legs then 'BEAST' else 'WEIRDO' end as species
from top_half t
join bottom_half b on t.id = b.id
order by species
limit 10
