Use Chinook;
SELECT 
    Concat(LastName,",",FirstName) as "Full Name",  
    BillingCity, 
    InvoiceDate, 
    Total
FROM
    Customer
INNER JOIN
    Invoice USING (customerId);
    
DROP View customerPayments;
    
CREATE VIEW customerPayments
AS 
SELECT 
    Concat(LastName,",",FirstName) as "Full Name",  
    BillingCity, 
    InvoiceDate, 
    Total
FROM
    Customer
INNER JOIN
    Invoice USING (customerId);


SELECT * FROM customerPayments;

CREATE or REPLACE VIEW customerPayments
AS 
SELECT 
    InvoiceDate
    Total
FROM
    Customer
INNER JOIN
    Invoice USING (customerId);
    
SELECT * FROM customerPayments;


SHOW FULL TABLES ;


-- pemdas : order of operations
CREATE VIEW aboveAvgTotals AS
    SELECT 
        InvoiceId, 
        BillingAddress, 
        Total
    FROM
        Invoice
    WHERE
        Total > (
            SELECT 
                AVG(Total)
            FROM
                Invoice)
    ORDER BY Total DESC; 
    
SELECT * FROM aboveAvgTotals;

CREATE OR REPLACE VIEW sales_peeps AS
    SELECT 
        employeeId,
        FirstName,
        LastName,
        Title,
        Email,
        PostalCode
    FROM
        employee
    WHERE
        Title LIKE '%Sales%';

SELECT * FROM sales_peeps;

INSERT INTO sales_peeps(
    employeeId,
    firstName,
    lastName,
    Title,
    email,
    PostalCode
) 
VALUES(
    1707,
    'Lily',
    'Bush',
    'IT Support',
    'lilybush@classicmodelcars.com',
    1002
);

SELECT * FROM sales_peeps;
SELECT * FROM employee;


CREATE OR REPLACE VIEW sales_peeps AS
    SELECT 
		employeeId,
		FirstName,
        LastName,
		Title,
		Email,
		PostalCode
	FROM
		employee
	WHERE
		Title LIKE '%Sales%'
WITH CHECK OPTION;


EXPLAIN Table sales_peeps;

INSERT INTO sales_peeps(
    employeeId,
    firstName,
    lastName,
    Title,
    PostalCode
) 
VALUES(
    1715,
    'Jack',
    'Doe',
    'Sales Support',
    1002
);

INSERT INTO sales_peeps(
    employeeId,
    firstName,
    lastName,
    Title,
    email,
    PostalCode
) 
VALUES(
    1710,
    'John',
    'Doe',
    'Sales Manager',
    'JohnDoe@classicmodelcars.com',
    1002
);
select * from sales_peeps;
DROP VIEW sales_peeps;

