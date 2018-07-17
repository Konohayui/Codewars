--but on the land of Lórien no shadow lay--
select initcap(concat(firstname, ' ', lastname)) as shortlist
from Elves
  where firstname like '%tegil%' 
  or lastname like '%astar%'
