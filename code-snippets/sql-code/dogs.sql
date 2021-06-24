--How to select a database to use

CREATE DAT


USE pets;

--How to create a table in the database 
CREATE TABLE dogs
(
  id              INT unsigned NOT NULL AUTO_INCREMENT, # Unique ID for the record
  name            VARCHAR(150) NOT NULL,                # Name of the cat
  owner           VARCHAR(150) NOT NULL,                # Owner of the cat
  birth           DATE NOT NULL,                        # Birthday of the cat
  PRIMARY KEY     (id)                                  # Make the id the primary key
);

--How to insert values into a table 
INSERT INTO cats ( name, owner, birth) VALUES
  ( 'Sandy', 'Lennon', '2015-01-03' ),
  ( 'Cookie', 'Casey', '2013-11-13' ),
  ( 'Charlie', 'River', '2016-05-21' );



--Show all entries in the table , cats 
SELECT * FROM cats;


--Selecting specific columns 
SELECT name FROM cats WHERE owner = 'Casey';

--deleting an entry 
DELETE FROM cats WHERE name='Cookie';

--alter the table structure by adding another field after name
ALTER TABLE cats ADD gender CHAR(1) AFTER name;

--How to list a database
SHOW DATABASES;
--How to describe the attributes of a table
DESCRIBE cats; 