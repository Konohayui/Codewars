-- Create your SELECT statement here
with recursive employee_levels(level, id, first_name, last_name, manager_id) as
(select 1 as level,
        id, 
        first_name, 
        last_name,
        manager_id
        from employees
        where manager_id is Null
  union all
  select el.level + 1,
         e.id,
         e.first_name,
         e.last_name,
         e.manager_id
         from employees as e, employee_levels as el
         where el.id = e.manager_id)
         
select * from employee_levels
