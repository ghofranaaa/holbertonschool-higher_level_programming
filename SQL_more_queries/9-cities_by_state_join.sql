-- selecting from two tables
USE hbtn_0d_usa;
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states_id
ORDER BY cities.id ASC;