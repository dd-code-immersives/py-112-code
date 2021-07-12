-- Which country has the largest population ( using sql)
SELECT * FROM country_data ORDER BY population DESC LIMIT 5;

-- Which countries have a population between 30,000 and 500,000? (using sql)
SELECT * FROM country_data WHERE population BETWEEN 30000 AND 500000;

-- Which countries have a population greater than 500,000 and start with the letter A? 
SELECT * FROM country_data WHERE population > 500000 AND country_name LIKE "A%";