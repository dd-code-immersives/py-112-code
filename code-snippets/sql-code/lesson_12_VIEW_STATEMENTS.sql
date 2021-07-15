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
    Concat(LastName,",",FirstName) as "Full Name",   
    InvoiceDate, 
    Total
FROM
    Customer
INNER JOIN
    Invoice USING (customerId);

-- view subquery 

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
                Invoce)
    ORDER BY Total DESC;


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
    1703,
    'Lily',
    'Bush',
    'IT Support',
    'lilybush@classicmodelcars.com',
    1002
);






-- with check option
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
WITH CHECK OPTION;



INSERT INTO sales_peeps(
    employeeId,
    firstName,
    lastName,
    Title,
    email,
    PostalCode
) 
VALUES(
    1704,
    'John',
    'Doe',
    'IT Support',
    'JohnDoe@classicmodelcars.com',
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
    1704,
    'John',
    'Doe',
    'Sales Manager',
    'JohnDoe@classicmodelcars.com',
    1002
);

SELECT * FROM sales_peeps;

 -- drops a view
DROP VIEW customerPayments;
-- to see all tables, you will also see views 
SHOW TABLES;  
-- in order to distinguish between views and tables
SHOW FULL TABLES; 