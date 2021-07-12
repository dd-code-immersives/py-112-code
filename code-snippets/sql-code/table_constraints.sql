use mock_data;
CREATE TABLE suppliers (
    supplier_id INT AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    phone VARCHAR(15) NOT NULL UNIQUE,
    address VARCHAR(255) NOT NULL,
    PRIMARY KEY (supplier_id),
    CONSTRAINT uc_name_address UNIQUE (name , address)
);

SHOW CREATE TABLE suppliers;

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
       
INSERT INTO suppliers(name, phone, address) 
VALUES( 'ABC Inc', 
       '(408)-908-1115',
       '56000 North 1st Street');
SELECT * FROM suppliers;


SHOW INDEX FROM suppliers;

DROP INDEX uc_name_address ON suppliers;


ALTER TABLE suppliers
ADD CONSTRAINT uc_name_address
UNIQUE (name , address);

DROP TABLE suppliers;
