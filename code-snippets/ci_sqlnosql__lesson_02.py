# Enter your code here

import csv, sqlite3

#con = sqlite3.connect("hardware_store.db") # change to 'sqlite:///your_filename.db'
#cur = con.cursor()

with open('inventory.csv','r') as fin:
    dr = csv.DictReader(fin)
        
    
#you are going to use executemany



import sqlite3
import os
# MAKE SURE YOU ARE IN THE CORRECT DIRECTORY or use the full path in you connect statement
print(os.getcwd())
os.chdir(r'../sql-data')  
print(os.getcwd())
#=====================================================
conn = sqlite3.connect('customer.db')
c = conn.cursor()

c.execute('SELECT rowid,* FROM customers WHERE lName = "Smith" ')  # rowid is now the first element in the returned tuple
customers = c.fetchall()

# ITERATE over the results
for customer in customers:
    # Use indexing to return the elements of the tuple
    print(f'Customer {customer[0]}')
    print(f'First name: {customer[1]}\nLast name: {customer[2]}\nAddress 1: {customer[3]}\nAddress 2: {customer[4]}\nZip: {customer[5]}' )
    print('='*30)
conn.commit()
conn.close()

conn = sqlite3.connect('customer.db')
c = conn.cursor()

# All last names that begin with 'T'
c.execute('SELECT rowid,* FROM customers WHERE lName LIKE "T%" ')  # <== The % sign is used as a wildcard
customers = c.fetchall()

# i = 1
for customer in customers:
    # Use indexing to return the elements of the tuple
    print(f'Customer {customer[0]}')
    print(f'First name: {customer[1]}\nLast name: {customer[2]}\nAddress 1: {customer[3]}\nAddress 2: {customer[4]}\nZip: {customer[5]}' )
    print('='*30)
conn.commit()
conn.close()

conn = sqlite3.connect('customer.db')
c = conn.cursor()

c.execute('SELECT rowid,* FROM customers WHERE address1 LIKE "%brooklyn%" ') #  NOTE Case does not matter 
customers = c.fetchall()

for customer in customers:
    # Use indexing to return the elements of the tuple
    print(f'Customer {customer[0]}')
    print(f'First name: {customer[1]}\nLast name: {customer[2]}\nAddress 1: {customer[3]}\nAddress 2: {customer[4]}\nZip: {customer[5]}' )
    print('='*30)
conn.commit()
conn.close()

import os
import sqlite3

# Notice the defaults for the fields and whereClause
def queryDB(db,table,fields='*',whereClause=''):  
    #customers.db
    conn = sqlite3.connect(db if db[-3:] == '.db' else db+'.db')# <=== The .db extension is necessary
    c = conn.cursor()
    sql = '''SELECT {0} FROM {1} {2}'''.format(fields,table,whereClause)
    #sql2 = f'''SELECT {fields} FROM {table} {whereClause}'''
    print(sql)
    c.execute(sql)  
    qResults = c.fetchall()

    for result in qResults:
        print(result)
        print('='*30)
    conn.commit()
    conn.close()
    
#
print(os.getcwd())
os.chdir(r'../sql-data')  
print(os.getcwd()) 
queryDB('customer','customers')  
print("*"*35)
queryDB('customer','customers','lName,fName')
print("*"*35)
queryDB('customer','customers','*',"WHERE address2 = '' ")

conn = sqlite3.connect('customer.db')
c = conn.cursor()

# All last names that begin with 'T'
c.execute('SELECT * FROM customers WHERE fName = "Larry" and lName = "Gantt" ')  # <== The % sign is used as a wildcard
customers = c.fetchall()

for customer in customers:
    # Use indexing to return the elements of the tuple
    print(customer)
    print('='*30)
conn.commit()
conn.close()

conn = sqlite3.connect('customer.db')
c = conn.cursor()

# All last names that begin with 'T'
c.execute('''UPDATE customers SET 
address1 = "1 Park Avenue",
address2 = "Penthouse A"
WHERE fName = "Larry" and lName = "Gantt" ''') 
conn.commit()
c.execute('''SELECT * FROM customers WHERE fName = "Larry" and lName = "Gantt" ''') 
customers = c.fetchall()

for customer in customers:
    # Use indexing to return the elements of the tuple
    print(customer)
    print('='*30)
conn.close()

# Add your code here


# Add your code here


import sqlite3
conn = sqlite3.connect('customer.db')
c = conn.cursor()
conn.commit()
c.execute('''SELECT SUBSTR('I LOVE PYTHON AND SQL',3,11)''') 
sqlResults = c.fetchall()
print(sqlResults)

conn = sqlite3.connect('customer.db')
c = conn.cursor()
conn.commit()
c.execute('''SELECT TRIM(' SQL   ')''') 
sqlResults = c.fetchall()
print(sqlResults)

conn = sqlite3.connect('customer.db')
c = conn.cursor()
conn.commit()
c.execute('''SELECT LTRIM('         SQL   ')''') 
sqlResults = c.fetchall()
print(sqlResults)

conn = sqlite3.connect('customer.db')
c = conn.cursor()
conn.commit()
c.execute('''SELECT RTRIM('   SQL   ')''') 
sqlResults = c.fetchall()
print(sqlResults)

conn = sqlite3.connect('customer.db')
c = conn.cursor()
conn.commit()
c.execute('''SELECT LENGTH('         SQL   ')''') 
sqlResults = c.fetchall()
print(sqlResults)

# Execute two commands
conn = sqlite3.connect('customer.db')
c = conn.cursor()
conn.commit()
c.execute('''SELECT LENGTH(TRIM('         SQL   '))''') 
sqlResults = c.fetchall()
print(sqlResults)

conn = sqlite3.connect('customer.db')
c = conn.cursor()
conn.commit()
c.execute('''SELECT REPLACE('I LOVE PYTHON','PYTHON','SQL')''') 
sqlResults = c.fetchall()
print(sqlResults)

conn = sqlite3.connect('customer.db')
c = conn.cursor()
conn.commit()
c.execute('''SELECT 'I LOVE PYTHON ' || '- I LOVE SQL' ''') 
sqlResults = c.fetchall()
print(sqlResults)

# We can delete one row in a table by adding a where clause
# We can delete allitems in a table by omitting the where clause




