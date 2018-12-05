-- Lists all cities with states
SELECT cities.id, cities.name, states.name
FROM states
INNER JOIN cities 
ON cities.state_id = states.id;
