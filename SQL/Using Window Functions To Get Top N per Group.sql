select c.id as category_id,
  c.category as category,
  p.title as title,
  p.views as views,
  p.id as post_id
from categories c 
left join (
  select category_id,
    title,
    views,
    id,
    rank() over (partition by category_id order by views desc, id) as rnk
  from posts) p on p.category_id = c.id and rnk <= 2
order by category, views desc, post_id
