-- Replace with your SQL Query
with stars(actor1, actor2, counts) as
(select fa1.actor_id as a1, fa2.actor_id as a2, count(fa1.actor_id) as counts
 from film_actor as fa1, film_actor as fa2
 where fa1.film_id = fa2.film_id and 
       fa1.actor_id <> fa2.actor_id
 group by fa1.actor_id, fa2.actor_id
 order by counts desc, fa1.actor_id
 limit 1)
 
select a1.first_name|| ' ' ||a1.last_name as first_actor,
       a2.first_name|| ' ' ||a2.last_name as second_actor,
       f.title
      from actor as a1, actor as a2, stars as s, film as f
where a1.actor_id = s.actor1 and
      a2.actor_id = s.actor2 and
      f.film_id in (select fa1.film_id 
                    from film_actor as fa1, film_actor as fa2
                    where fa1.film_id = fa2.film_id and
                          fa1.actor_id = a1.actor_id and
                          fa2.actor_id = a2.actor_id)
