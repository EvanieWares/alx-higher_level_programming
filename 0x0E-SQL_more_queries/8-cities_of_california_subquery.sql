-- Lists all the cities of California that can be found
-- in the database hbtn_0d_usa.
SELECT id, name
FROM cities, states
WHERE cities.state_id = state_id
AND states.name = 'California'
ORDER BY cities.id ASC;
