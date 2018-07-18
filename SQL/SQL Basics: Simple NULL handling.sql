select id,
  coalesce(nullif(name, ''), '[product name not found]') as name,
  coalesce(nullif(card_name, ''), '[card name not found]') as card_name,
  coalesce(price) as price,
  card_number,
  transaction_date
from eusales
where price > 50
