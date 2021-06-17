import string
print(string.ascii_letters)





import sqlite3
import os
print("hello world")

!pip3 install pysqlite3 

!python3 -m pip install --upgrade pip

print(os.getcwd())
os.chdir(r'/Users/andrewdoyle/Documents/code-immersives/py-112-code/sql-data')  
print(os.getcwd()) #this gets the working directory

conn = sqlite3.connect('customer.db')
#print(sqlite3.version_info)
# If we attempt to connect to a database that does not exist.  It creates it.

nums = []
for i in range(5):
    nums.append(i)
print(nums)
[i for i in range(5)] == nums
nums = range(5)



from pprint import pprint
pprint(dir(nums))

#### Let's examine the methods available for the object we just created

#name = "Dominic"
#print(name.startswith("D"))

methods = [x for x in dir(conn) if not x.startswith('_')]
pprint(methods)

from pprint import pprint

# Create a cursor to access the database
c = conn.cursor()
# This is equivalent to creating a filehandle when using the 'open' function
pprint(dir(c))
print(c.rowcount)

conn = sqlite3.connect('customer.db')
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS customers (
    fName TEXT,
    lName TEXT,
    address1 TEXT,
    address2 TEXT,
    zip TEXT)
""")
#conn.commit()  # <=== commit our table to the database
#conn.close()   # <=== close the connection


'''
WARNING !!!! If the table was created previously It will give you 
an error

'''

c.execute("DESCRIBE customers")
conn.commit()  # <=== commit our table to the database
conn.close()   # <=== close the connection


# Use the IF NOT EXISTS clause if we might have created the table previously
c.execute("""CREATE TABLE IF NOT EXISTS customers (
    fName TEXT,
    lName TEXT,
    address1 TEXT,
    address2 TEXT,
    zip TEXT)
""")

conn.commit()  # <=== commit our table to the database
conn.close()

'''
There are several tools we can use to view our SQLite database and the tables outside of python
1. Install full version of SQLite3 - www.sqlite.org
2. Install a browser add in - SQLite Manager by Lunu ( PREFERRED)

Examine the customer.db file we created
Examine the chinook.db file 

Look at the syntax

'''

conn = sqlite3.connect('customer.db')
c = conn.cursor()

for row in c.execute("""SELECT * FROM sqlite_master"""):
    p(row)
c.execute("""CREATE TABLE IF NOT EXISTS depts (
    dept_id TEXT,
    dept_name TEXT)
""")
for row in c.execute("""SELECT name FROM sqlite_master"""):
    print(row)
conn.commit()  # <=== commit our table to the database
conn.close()

conn = sqlite3.connect('customer.db')
c = conn.cursor()
#print(c.rowcount)
c.execute("""INSERT INTO customers VALUES
('Mary','Jones','15 Main street','','99995')""")
conn.commit()
conn.close()
#print(c.rowcount)

conn = sqlite3.connect('customer.db')
c = conn.cursor()
print(c.rowcount)
all_customers = [
    ('Harry','Teague','100 Centre Street','Apt 1A','88888'),
    ('Henrietta','Teague','100 Centre Street','Apt 1A','88888'),
    ('Larry','Gantt','10 Bond Street','Apt 11C','88000'),
    ('Horace','Penn','50 Gansavort Street','Apt 9B','88770'),
    ('Patrice','Wright','60 Brooklyn Bridge Park Street','Apt 44M','11234'),
]
c.executemany("""INSERT INTO customers VALUES (?,?,?,?,?)""", all_customers)
conn.commit()
print(c.rowcount)
conn.close()


conn = sqlite3.connect('customer.db')
c = conn.cursor()

# The asterick allows you to retreive all of the fields
c.execute('SELECT * FROM customers')
data = c.fetchall()
#print(c.description)
print(data)

# A list of tuples were returned
# Check the data type of the elements in the list
print(data[0])

print(data[0][0]) # Return the first name of the first element in the list
print(data[1][2])
conn.commit()
conn.close()



conn = sqlite3.connect('customer.db')
c = conn.cursor()

c.execute('SELECT * FROM customers')
print(c.fetchone())

conn.commit()
conn.close()
# A first record is returned

conn = sqlite3.connect('customer.db')
c = conn.cursor()

c.execute('SELECT * FROM customers')
print(c.fetchmany(3))

conn.commit()
conn.close()
# The first record is returned

conn = sqlite3.connect('customer.db')
c = conn.cursor()

c.execute('SELECT * FROM customers')
ans = c.fetchone()

# Use indexing to return the elements of the tuple
print(f'First name: {ans[0].upper()}\nLast name: {ans[1].upper()}\nAddress 1: {ans[2].title()}\nAddress 2: {ans[3]}\nZip: {ans[4]}' )

conn.commit()
conn.close()
# A first record is returned

conn = sqlite3.connect('customer.db')
c = conn.cursor()

c.execute('SELECT * FROM customers')
customers = c.fetchall()

i = 1
for customer in customers:
    # Use indexing to return the elements of the tuple
    print(f'Customer {i}')
    print(f'First name: {customer[0]}\nLast name: {customer[1]}\nAddress 1: {customer[2]}\nAddress 2: {customer[3]}\nZip: {customer[4]}' )
    print('='*30)
    i += 1
conn.commit()
conn.close()

conn = sqlite3.connect('customer.db')
c = conn.cursor()

c.execute('SELECT rowid,* FROM customers')  # rowid is now the first element in the returned tuple
customers = c.fetchall()

# i = 1
for customer in customers:
    # Use indexing to return the elements of the tuple
    print(f'Customer {customer[0]}')
    print(f'First name: {customer[1]}\nLast name: {customer[2]}\nAddress 1: {customer[3]}\nAddress 2: {customer[4]}\nZip: {customer[5]}' )
    print('='*30)
conn.commit()
conn.close()

'''
In case of a database locked issue.
Recreate your database by running the code again and changing the database name to customer1.db

'''

