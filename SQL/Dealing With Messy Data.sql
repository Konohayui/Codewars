select c.first_name,
       c.last_name,
       c.credit_limit as old_limit,
       max(p.credit_limit) as new_limit
from customers as c
join prospects as p on 
     lower(p.full_name) like '%' || lower(c.first_name) || '%' and
     lower(p.full_name) like '%' || lower(c.last_name) || '%' and
     p.credit_limit > c.credit_limit
group by c.first_name, c.last_name, c.credit_limit
order by c.first_name, c.last_name
