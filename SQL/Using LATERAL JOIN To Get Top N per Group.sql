-- Replace with your SQL query
select
  categories.id as category_id,
  categories.category,
  p.title,
  p.views,
  p.id as post_id
from categories
left join lateral (
    select title, views, id 
    from posts
    where posts.category_id = categories.id
    order by posts.views desc
    limit 2) p on true
order by categories.category, p.views desc, post_id
