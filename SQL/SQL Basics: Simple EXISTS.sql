-- Create your SELECT statement here
select * from departments
where exists
(select department_id from sales 
where price > 98.00)
