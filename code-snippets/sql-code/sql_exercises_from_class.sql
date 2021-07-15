

VIEWS
CREATE VIEW `By_Country` AS
select * from Customer
order by Country asc
with check option
;
create or replace view by_country as
select CustomerId
, Country
, PostalCode
, SupportRepId
from Customer
order by Country asc
with check option
;

-- add 
alter table Countries_In_The_World
modify column Country_Name varchar(50) unique;
alter table Countries_In_The_World
modify column Population int check(Population > 0)
, modify column Area_km2 real check(Area_km2 > 0)
;

-- find country name with the longest name 
select countryID
, length(Country_Name) as name_length
, Country_Name
from Countries_In_The_World
order by name_length
desc
;
select countryID
, length(Country_Name) as name_length
, Country_Name
from Countries_In_The_World
order by name_length
asc
;
select countryID
, Country_Name
, Population
from Countries_In_The_World
where (length(Country_Name) - length(replace(Country_Name, ' ', ''))) = 1
order by Population
desc
;
select countryID
, Country_Name
, Population
from Countries_In_The_World
where (length(Country_Name) - length(replace(Country_Name, ' ', ''))) = 2
order by Population
desc
;