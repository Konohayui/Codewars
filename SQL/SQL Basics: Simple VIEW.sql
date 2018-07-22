create view members_approved_for_voucher as (
select m.id, m.name, m.email, sum(p.price) as total_spending
from members m
join sales s on s.member_id = m.id
join departments d on s.department_id = d.id
join products p on s.product_id = p.id
where d.id in 
(select distinct d.id from departments d
  join sales s on s.department_id = d.id
  join products p on s.product_id = p.id
  group by d.id
  having sum(p.price) > 10000)
group by m.id
having sum(p.price) > 1000
order by m.id
);

select * from members_approved_for_voucher
