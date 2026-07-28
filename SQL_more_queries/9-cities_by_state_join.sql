-- lists cities with their state name using JOIN, sorted by cities.id
SELECT cities.id, cities.name, states.name FROM cities JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC;
