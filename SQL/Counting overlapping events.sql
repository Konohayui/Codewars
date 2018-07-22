select v1.entry_time as when_happened, count(*) as visits_count 
  from visits v1 
  join visits v2 on v1.entry_time >= v2.entry_time and v1.entry_time < v2.exit_time
 group by v1.id
 order by visits_count desc
 limit 1
