import csv, sqlite3


from pprint import pprint

def read_inventory_file(filename='../sql-data/inventory.csv'):


	with open(filename,'r') as fin:
		dr = csv.DictReader(fin)
		all_vals = []
		for entry in dr:
			csv_vals = list(entry.values())[:-1]
			price_quantity = round(float(entry['price']) * int(entry['quantity']), 2)
			csv_vals.append(price_quantity)
			all_vals.append(tuple(csv_vals))
	return all_vals
		

def run_execute_many(vals_to_insert):
	#create database, add new table, drop table if already there.	
	con = sqlite3.connect("hardware_store.db") # change to 'sqlite:///your_filename.db'
	cur = con.cursor()
	cur.execute("""DROP TABLE inventory""")
	cur.execute("""CREATE TABLE IF NOT EXISTS inventory (
	    item_id TEXT,
	    item TEXT,
	    price REAL,
	    quantity INTEGER,
	   	price_extended REAL)
	""")

	cur.executemany("""INSERT INTO inventory VALUES (?,?,?,?,?)""", vals_to_insert )
	cur.execute("""SELECT * from inventory""")
	data = cur.fetchall()
	pprint(data) 
	return data 

def generate_sql_from_input(n=3):

	#amount of entries to input
	#split string by comma, cast to tuple
	rows = []
	while n > 0:
		data = tuple(input("Enter Row Data: ").split(','))
		rows.append(data)
		n -= 1

	return rows 


if __name__ == '__main__':
	# for second part 
	# data = generate_sql_from_input()
	data = read_inventory_file()
	run_execute_many(data)



