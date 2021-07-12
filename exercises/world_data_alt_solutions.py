
""" 

taro's solution

"""

url = 'http://www.scrapethissite.com/pages/simple/'
result = requests.get(url)
soup = BeautifulSoup(result.content, 'html.parser')

# COUNTRY NAMES
country_name_raw = soup.find_all("h3", {"class":"country-name"})
country_name = [i.get_text().strip() for i in country_name_raw]
country_name_tup = [(i,) for i in country_name]

# CAPITAL CITIES
capital_raw = soup.find_all("span", {"class":"country-capital"})
capital = [i.get_text().strip() for i in capital_raw]
capital_tup = [(i,) for i in capital]

# POPULATION
population_raw = soup.find_all("span", {"class":"country-population"})
population = [int(i.get_text().strip()) for i in population_raw]
population_tup = [(i,) for i in population]

# AREA KM2
area_raw = soup.find_all("span", {"class":"country-area"})
area = [float(i.get_text().strip()) for i in area_raw]
area_tup = [(i,) for i in area]

# POPULATION DENSITY
population_density_list = list(zip(population, area))
population_density = [x/y if y else 0 for x, y in population_density_list]
population_density_tup = [(i,) for i in population_density]

all_data_list = list(zip(country_name, capital, population, area, population_density))

mc.executemany('''insert into Countries_In_The_World (
    Country_Name
, Capital_City
, Population
, Area_km2
, Population_Density
)
values
(%s, %s, %s, %s, %s)
''', 
all_data_list)

mydb.commit()
mydb.close()

SQL COMMANDS
create table if not exists Countries_In_The_World
(
countryID int primary key auto_increment
, Country_Name varchar(50)
, Capital_City varchar(50)
, Population int
, Area_km2 real
, Population_Density real
)
;

PROBLEM 1
select Country_Name
, Population
from Countries_In_The_World
order by Population
desc limit 20;

PROBLEM 2
select Country_Name
, LENGTH(Country_Name) as Country_Name_Length
from Countries_In_The_World
order by Country_Name_Length
desc limit 20;

PROBLEM 3
select Country_Name
, Population
from Countries_In_The_World
where Population between 30000 and 50000
order by countryID
asc
;

PROBLEM 4
select * from Countries_In_The_World
where Population > 500000 and Country_Name like 'A%'
order by Population desc
; 

""" 
Dakota's solution 

""" 

url = 'http://www.scrapethissite.com/pages/simple'
result = requests.get(url)
soup = BeautifulSoup(result.content, 'html.parser')

countries = soup.find_all('div', {'class' : 'col-md-4 country'})
country_info = []
countryName, countryCapital, countryPopulation, countryArea, countryDensity = None, None, 0, None, 0
for country in countries:

  countryName = country.find('h3').getText().strip().lower()

  countryCapital = country.find('span', {'class' : 'country-capital'}).getText().lower()

  countryPopulation = int(country.find('span', {'class' : 'country-population'}).getText())

  area = country.find('span', {'class' : 'country-area'}).getText()
  floatedArea = float(area)
  countryArea = floatedArea

  if(countryArea != 0):
    countryDensity = round(countryPopulation / countryArea, 2)

  country_info.append((countryName, countryCapital, countryPopulation, countryArea, countryDensity))


config = dotenv_values("sqlToPython.env")



mydb = mysql.connector.connect(
  host = config['HOST'], 
  user=config['USER'],
  password=config['PASSWORD'],
  database=config['DATABASE']
)

mycursor = mydb.cursor()

mycursor.execute(''' DROP TABLE countries ''')

mycursor.execute(''' CREATE TABLE countries(
  countryId INT AUTO_INCREMENT PRIMARY KEY,
  country_name VARCHAR(100) NOT NULL,
  country_capital VARCHAR(100) NOT NULL,
  country_population INT NOT NULL,
  country_area REAL NOT NULL, 
  country_density REAL NOT NULL
) ''')


mycursor.executemany(''' INSERT INTO countries(country_name, country_capital, country_population, country_area, country_density) VALUES (%s, %s, %s, %s, %s) ''', country_info)
mydb.commit()

mycursor.execute(''' SELECT country_name, country_population FROM countries ORDER BY country_population DESC LIMIT 1; ''')

for x in mycursor:
  print(x)

mycursor.execute(''' SELECT country_name, country_population FROM countries WHERE country_population BETWEEN 30000 AND 500000; ''')

for x in mycursor:
  print(x)

mycursor.execute(''' SELECT country_name, country_population FROM countries WHERE country_population > 500000 AND country_name LIKE 'a%' ; ''')

for x in mycursor:
  print(x)