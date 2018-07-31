create function weekdays(date,date) returns integer as
$$
select count(days)::int
from generate_series(least($1,$2),greatest($1,$2),'1 day') as days
where extract(dow from days) not in (0,6)
$$
language sql
