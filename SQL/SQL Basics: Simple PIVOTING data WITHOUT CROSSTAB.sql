-- https://modern-sql.com/use-case/pivot


select p.name,
  count(d.id) filter (where d.detail = 'good') as good,
  count(d.id) filter (where d.detail = 'ok') as ok,
  count(d.id) filter (where d.detail = 'bad') as bad
from products p
join details d on p.id = d.product_id
group by p.name
order by p.name
