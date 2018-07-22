select title from film
join film_actor on film.film_id = film_actor.film_id
where film.film_id in 
(select film_id from film_actor
where actor_id = 105) and actor_id = 122


-- good solutions

SELECT f.title
FROM film f
JOIN film_actor fa on fa.film_id = f.film_id
WHERE fa.actor_id IN (105,122)
GROUP BY f.film_id
HAVING COUNT(*) = 2
ORDER BY f.title ASC

SELECT f.title 
  FROM film f 
  INNER JOIN film_actor a ON f.film_id = a.film_id
  INNER JOIN film_actor b ON f.film_id = b.film_id
  WHERE a.actor_id = 105 AND b.actor_id = 122
  ORDER BY title;
