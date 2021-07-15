
-- loading data from local csv into mysql
LOAD DATA LOCAL INFILE '/home/myfile.csv'
INTO TABLE mock_data FIELDS TERMINATED BY ','
ENCLOSED BY '"' LINES TERMINATED BY '\n';

-- check constraints tutorial 
CREATE TABLE parts (
    part_no VARCHAR(18) PRIMARY KEY,
    description VARCHAR(40),
    cost DECIMAL(10,2 ) NOT NULL CHECK (cost >= 0),
    price DECIMAL(10,2) NOT NULL CHECK (price >= 0)
);

SHOW CREATE TABLE parts;

INSERT INTO parts(part_no, description,cost,price) 
VALUES('A-001','Cooler',0,-100);

drop table if exists parts;


CREATE TABLE parts (
    part_no VARCHAR(18) PRIMARY KEY,
    description VARCHAR(40),
    cost DECIMAL(10,2 ) NOT NULL CHECK (cost >= 0),
    price DECIMAL(10,2) NOT NULL CHECK (price >= 0),
    CONSTRAINT parts_chk_price_gt_cost 
        CHECK(price >= cost)
);

SHOW CREATE TABLE parts;

INSERT INTO parts(part_no, description,cost,price) 
VALUES('A-001','Cooler',200,100);

CREATE TABLE suppliers (
    supplier_id INT AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    phone VARCHAR(15) NOT NULL UNIQUE,
    address VARCHAR(255) NOT NULL,
    PRIMARY KEY (supplier_id),
    CONSTRAINT uc_name_address UNIQUE (name , address)
);

CREATE TABLE suppliers (
    supplier_id INT AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    phone VARCHAR(15) NOT NULL UNIQUE,
    address VARCHAR(255) NOT NULL,
    PRIMARY KEY (supplier_id),
    CONSTRAINT uc_name_address UNIQUE (name , address)
);
-- insert a value into the table

INSERT INTO suppliers(name, phone, address) 
VALUES( 'ABC Inc', 
       '(408)-908-2476',
       '4000 North 1st Street');
-- insert another value that violates the unique constraint

INSERT INTO suppliers(name, phone, address) 
VALUES( 'XYZ Corporation','(408)-908-2476','3000 North 1st Street');
-- so change the phone number

INSERT INTO suppliers(name, phone, address) 
VALUES( 'XYZ Corporation','(408)-908-3333','3000 North 1st Street');
-- Show the values of the table

SELECT * FROM suppliers;
INSERT INTO suppliers(name, phone, address) 
VALUES( 'ABC Inc', 
       '(408)-908-1111',
       '4000 North 1st Street');
-- How to drop a a key

DROP INDEX uc_name_address ON suppliers;
-- How to view the constraint

SHOW INDEX FROM suppliers;
-- Adding a new unique constraint programmatically

ALTER TABLE table_name
ADD CONSTRAINT constraint_name 
UNIQUE (column_list);

