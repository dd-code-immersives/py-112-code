import math

def calcMean(numList):
    return round(sum(numList)/len(numList),2)

def calcMode(numList):
    mode = 0
    for i in set(numList):
        if numList.count(i) > 1:
            mode = i
    return mode

def calcMode(alist = [2,2,3,3,4]):
    max_val = max(alist)
    modes = []
    for val in alist:
        if alist.count(val) == alist.count(max_val):
            modes.append(val)
    return modes
    
def calcMedian(numList):
    numList.sort()
    if len(numList)%2 == 0:
        middle = int(len(numList)/2)
        median = (numList[middle-1] + numList[middle])/2
    else:
        # Odd number of values
        median = int((len(numList) - 1)/2)
    return median

numList = [88,89,90,93,84,86,88,91,88,87]
mean = calcMean(numList)
median = calcMedian(numList)
mode = calcMode(numList)
print(f'The mean is {mean}')
print(f'The mode is {mode}')
print(f'The median is {median}')



def isPrime(num):
    prime = False
    if num >= 2:
        #
        prime = True
        for i in range(2,int(math.sqrt(num))+1):
            if num % i == 0:
                prime = False
                break
    return prime
    
for i in range(1000,1101):
    if isPrime(i):
        print(i)

import math
def isPrime(num):
    prime = False
    if num >= 2:
        #
        prime = True
        for i in range(2,int(math.sqrt(num))+1):
            if num % i == 0:
                prime = False
                break
    return prime
    
for i in range(1000,1101):
    if isPrime(i):
        sum_of_digits = sum([ int(x) for x in list(str(i))])
        print(i, sum_of_digits,isPrime(sum_of_digits))

#sum([ int(x) for x in list(str(i))])
digits = []
num = 1009 
total = 0
for i in list(str(num)):
    total += int(i)
print(total)
    

import random

students = ['Renee','Julia','Warren','Stacey','Charles','Linda','Dwight','Ann','Franklin','George','Walter','Susan']
volunteers = []
n = 5
for i in range(n):
    picked = random.choice(students)
    print('{0} was picked'.format(picked))
    students.remove(picked)
    volunteers.append(picked)
    print(students)
print(f'I randomly picked the following students: {volunteers}')
print(f'Remaining students: {students}')


students = ['Renee','Julia','Warren','Stacey','Charles','Linda','Dwight','Ann','Franklin','George','Walter','Susan']
def student_picker(x):
    return f"{random.sample(x, 5)} were chosen to volunteer"
print(student_picker(students))


students = ['Renee','Julia','Warren','Stacey','Charles','Linda','Dwight','Ann','Franklin','George','Walter','Susan']
random.shuffle(students)
print(students[0:5])

import os

work_dir = r"../sql-data/"
with open(work_dir+"World_country_populations.csv",'r') as fh:
    line = fh.readline()
    i = 0
    while line:
        if i > 0:
            print(line)
        line = fh.readline()
        i += 1

import os
import sqlite3

work_dir = r"../sql-data/"
fn = "World_country_populations.csv"
db_name = "world_populations.db"

conn = sqlite3.connect(work_dir+ db_name)
c = conn.cursor()
c.executescript('''
    create table IF NOT EXISTS pop_data(
        num INTEGER,
        country TEXT,
        population INTEGER,
        year_change REAL,
        net_change INTEGER,
        density INTEGER,
        land_area_km INTEGER,
        migrants INTEGER,
        fert_rate REAL,
        median_age INTEGER,
        urban_pop_pct REAL,
        world_share REAL
    );
    DELETE FROM pop_data;    
''')
conn.commit()

# num	Country	population	year_change	net_change	density	land_area_km2	migrants	
# fertility_rate	Median_age	Urban_pop_pct	World_share

with open(work_dir+fn,'r') as fh:
    line = fh.readline()
    i = 0
    while line:
        if i > 0:
            num,country,population,year_change,net_change,density,land_area_km,migrants,fert_rate,median_age,\
            urban_pop_pct,world_share = line.split(',')
            print(f"""{num} {country} {population} {year_change} {net_change} {density} {land_area_km}
            {migrants} {fert_rate} {median_age} {urban_pop_pct} {world_share}""")
            num = int(num)
            country = country.strip().replace("'"," ")
            population = int(population)
            year_change = float(year_change)
            net_change = int(net_change)
            density = int(density)
            land_area_km = int(land_area_km)
            migrants = float(migrants) if migrants else 0
            fert_rate = 0 if fert_rate.strip() == 'N.A.' else float(fert_rate)
            median_age = 0 if median_age.strip() == 'N.A.' else float(median_age)
            urban_pop_pct = 0 if urban_pop_pct.strip() == 'N.A.' else float(urban_pop_pct)
            world_share = float(world_share)
            
            # Store the data
            sql = f"""INSERT INTO pop_data (num,country,population,year_change,net_change,density,land_area_km,
            migrants,fert_rate,median_age,urban_pop_pct,world_share) 
            VALUES ({num},'{country}',{population},{year_change},{net_change},{density},{land_area_km},{migrants},
            {fert_rate},{median_age},{urban_pop_pct},{world_share});"""
            print(sql)
            c.execute(sql)
            conn.commit()
            
        line = fh.readline()
        i += 1

# CREATE THE DATABASE
import sqlite3, csv, pathlib
path = pathlib.Path('../sql-data/')
con = sqlite3.connect(path/'world_country_populations.db')
cur = con.cursor()
cur.executescript("""create table if not exists wcp (
    num integer,
    country text,
    population integer,
    year_change real,
    net_change real,
    density integer,
    land_area_km2 integer,
    migrants integer,
    fert_rate real,
    median_age integer,
    urban_pop_pct real,
    world_share real);
    delete from wcp;
    """)
con.commit()
# CREATE THE TABLE IN A WAY THAT DOES NOT COUNT "N.A." AS A NUMERICAL VALUE
with open(path/'World_country_populations.csv', 'r') as data:
    line = data.readline()
    i = 0
    while line:
        if i > 0:
            num,country,population,year_change,net_change,density,land_area_km2,migrants,fert_rate,median_age,\
            urban_pop_pct,world_share = line.split(',')
            print(f"""{num} {country} {population} {year_change} {net_change} {density} {land_area_km2}
            {migrants} {fert_rate} {median_age} {urban_pop_pct} {world_share}""")
            num = int(num)
            country = country.strip().replace("'"," ")
            population = int(population)
            year_change = float(year_change)
            net_change = int(net_change)
            density = int(density)
            land_area_km2 = int(land_area_km2)
            migrants = float(migrants) if migrants else 0
            fert_rate = 0 if fert_rate.strip() == 'N.A.' else float(fert_rate)
            median_age =  0 if median_age.strip() == 'N.A.' else float(median_age)
            urban_pop_pct =  0 if urban_pop_pct.strip() == 'N.A.' else float(urban_pop_pct)
            world_share = float(world_share)
            sql = f"""INSERT INTO wcp (num,country,population,year_change,net_change,density,land_area_km2,
            migrants,fert_rate,median_age,urban_pop_pct,world_share) 
            VALUES ({num},'{country}',{population},{year_change},{net_change},{density},{land_area_km2},{migrants},
            {fert_rate},{median_age},{urban_pop_pct},{world_share});"""
            print(sql)
            cur.execute(sql)
            con.commit()
        line = data.readline()
        i += 1

import os
import sqlite3

work_dir = r"../sql-data/"
fn = "World_country_populations.csv"

conn = sqlite3.connect(work_dir+"world_populations.db")
c = conn.cursor()
c.execute('''SELECT country, population FROM pop_data ORDER BY population DESC''')
rows = c.fetchall()
for row in rows:
    print(f'{row[0]} - population in mm {row[1]/1000000}') 
conn.close()

import os
import sqlite3

work_dir = r"../sql-data/"

conn = sqlite3.connect(work_dir+"world_populations.db")
c = conn.cursor()
c.execute('''SELECT sum(population) FROM pop_data ORDER BY population DESC''')
rows = c.fetchall()
for row in rows:
    print(f'{row[0]}')
    
# alternate: row = c.fetchone()

import os
import sqlite3

work_dir = r"../sql-data/"
fn = "World_country_populations.csv"

conn = sqlite3.connect(work_dir+"world_populations.db")
c = conn.cursor()
c.execute('''SELECT country, median_age FROM pop_data ORDER BY median_age DESC LIMIT 10''')
rows = c.fetchall()
for row in rows:
    print(f'{row[0]} - median age is {row[1]}') 
conn.close()

import os
import sqlite3

work_dir = r"../sql-data/"
fn = "World_country_populations.csv"

conn = sqlite3.connect(work_dir+"world_populations.db")
c = conn.cursor()
c.execute('''SELECT country, net_change FROM pop_data WHERE net_change < 0 ORDER BY net_change ASC LIMIT 10''')
rows = c.fetchall()
for row in rows:
    print(f'{row[0]} - people who left {row[1]}') 
conn.close()

import os
import sqlite3

work_dir = r"../sql-data/"
fn = "World_country_populations.csv"

conn = sqlite3.connect(work_dir+"world_populations.db")
c = conn.cursor()
['']
c.execute('''SELECT country, migrants FROM pop_data WHERE migrants > 0 ORDER BY migrants DESC LIMIT 10''')
rows = c.fetchall()
for row in rows:
    print(f'{row[0]} - migrants {row[1]}') 
conn.close()

import os
import sqlite3

work_dir = r"../sql-data/"
fn = "World_country_populations.csv"

conn = sqlite3.connect(work_dir+"world_populations.db")
c = conn.cursor()
c.execute('''SELECT country, population, year_change FROM pop_data WHERE population < 10000000 ORDER BY year_change DESC LIMIT 10''')
rows = c.fetchall()
for row in rows:
    print(f'{row[0]} - year change {row[2]} - population - {row[1]}') 
conn.close()

alist = [1,2,3]
3 in alist

import os
import sqlite3

work_dir = r"../sql-data/"
fn = "World_country_populations.csv"

conn = sqlite3.connect(work_dir+"world_populations.db")
c = conn.cursor()

countries = ('Canada', 'France','Germany','Italy','United States','United Kingdom','Japan')

c.execute("""select sum(migrants) from pop_data where country in {0} and migrants > 0""".format(countries))
total_g7_migrants = c.fetchone()[0]
c.execute("""select sum(migrants) from pop_data where migrants > 0""")
total_migrants_world_wide =  c.fetchone()[0]
total_migrants_rest_of_world = total_migrants_world_wide - total_g7_migrants
print(f"Percentage of migrants G7 takes {round((total_g7_migrants/total_migrants_world_wide)*100,2)}")
print(f"Percentage of migrants the rest of the world takes {round((total_migrants_rest_of_world/total_migrants_world_wide)*100,2)}")

for country in countries:
    c.execute("""select sum(migrants) from pop_data where country = '{0}' and migrants > 0""".format(country))
    g_country_count = c.fetchone()[0]
    print(f"Percentage of migrants {country} takes: { round((g_country_count/total_g7_migrants)*100,2 ) }")


# alternate solution 
looking_for = str(20)
stringOfNumbers = '32040230213340205020112'
found_indicies = []
for index, entry in enumerate(stringOfNumbers):
    tmp_str = stringOfNumbers[index:index + 2]
    if tmp_str == looking_for:
        print(f"index: {index}, {tmp_str}")
        found_indicies.append(index)
print("There are {0} - 20's found in the following positions {1}".format(len(found_indicies),found_indicies))
        

