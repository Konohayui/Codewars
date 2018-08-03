-- Replace with your SQL query
select (date_trunc('month', created_at))::timestamp::date as date,
       count(*) as count,
       round(((count(*) - lag(count(*), 1) over w)*1.0/(lag(count(*), 1) over w))*100, 1) || '%' as percent_growth
       from posts
group by date
window w as (order by (date_trunc('month', created_at))::timestamp::date)
order by date
