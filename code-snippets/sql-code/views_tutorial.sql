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
    
SELECT * FROM customerPayments;



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