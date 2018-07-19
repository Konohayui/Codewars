-- solution 1
select min(score) as min,
  percentile_count(0.5) within group (order by score) as median,
  max(score) as max
from result

-- solution 2
with ordered_score as (
  select score,
    row_number() over (order by score) as row_id,
    (select count(1) from result) as ct
  from result
)

select min(score) as min,
  (select avg(score)::float
  from ordered_score
  where row_id between ct/2.0 and ct/2.0 + 1) as median,
  max(score) as max
from result
