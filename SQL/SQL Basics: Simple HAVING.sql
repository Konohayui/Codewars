-- Create your SELECT statement here
select age, count(age) as total_people from people
group by age
having count(age) >= 10
