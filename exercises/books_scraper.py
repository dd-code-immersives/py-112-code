
"""
- extract all information you can about each book from http://books.toscrape.com/ 
- make an sql database with this information. 
- write a function that returns all the books in sorted order different sorting methods (most expensive, least expensive, amount of stars, alphabetically by title) 
def sort_books(type_of_sorting):
    books = []
    if type_of_sorting == "most expensive":
        pass
"""
import requests
from bs4 import BeautifulSoup
from pprint import pprint
import mysql.connector
from dotenv import dotenv_values

url = 'http://books.toscrape.com/'
result = requests.get(url)
soup = BeautifulSoup(result.content, 'html.parser')
#print(soup.prettify())

rating_word_mappings = {'one':1,'two':2, 'three':3, 'four': 4, 'five':5}
in_stock_word_mappings = {'in stock': 1, 'out of stock': 0}
 
articles = soup.find_all('article', {'class':'product_pod'})
print(articles)

books_info = []

price, instock, rating, title = None,True, 0, None
for article in articles:

	all_p_in_article = article.find_all('p')
	for p in all_p_in_article:
		if 'star-rating' in p['class']:
			rating_str = p['class'][1].lower()
			rating = rating_word_mappings[rating_str]
		if p['class'][0] == 'price_color':
			price = float(p.get_text()[1:])
		if p['class'] == 'instock availability':
			instock_str = p['instock availability'].get_text().strip().lower()
			instock = in_stock_word_mappings[instock_str]
	title = article.find('h3').find('a')['title']
	books_info.append((price, instock,rating,title))
print(books_info)


config = dotenv_values("../sql-notebooks/.env") 
mydb = mysql.connector.connect(
  host=config['HOST'],
  user=config['USER'],
  password=config['PASSWORD'],
  database="mock_data"
)

curr = mydb.cursor()

tags_table_query="""
drop table if exists books;
create table books(
    tag_id int primary key not null auto_increment,
    price float(5),
    in_stock bool,
    rating tinyint(1),
    title varchar(100)
);
"""

insert_into_books ="""
INSERT INTO books(price, in_stock, rating, title)
VALUES (%s, %s, %s, %s);
"""

curr.executemany(insert_into_books, books_info)
mydb.commit()

def sort_books(type_of_sorting, cursor):
    books = []


    sql = None
    if type_of_sorting == "rating":
        sql = "SELECT * FROM books ORDER BY rating;"
    elif type_of_sorting == "alphabetically":
    	sql = "SELECT * FROM books ORDER BY title;"
    elif type_of_sorting == "price highest":
    	sql = "SELECT * FROM books ORDER BY price DESC;"
    elif type_of_sorting == "price lowest":
    	sql = "SELECT * FROM books ORDER BY price ASC;"
    cursor.execute(sql)
    for entry in cursor:
    	books.append(entry)
    return books


books = sort_books("rating",curr)
print(books)



curr.close()
mydb.close()