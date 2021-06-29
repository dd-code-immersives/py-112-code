USE Chinook;
-- Provide a query showing Customers (just their full names, customer ID and country) who are not in the US.
SELECT  CONCAT(lastname, ',',firstname) as 'full name', CustomerId, country 
FROM Customer 
WHERE country != 'USA';

-- Provide a query only showing the Customers from Brazil.
SELECT * FROM Customer WHERE country = 'Brazil';

-- Provide a query showing the Invoices of customers who are from Brazil. 
-- The resultant table should show the customer's full name, Invoice ID, Date of the invoice and billing country.
Select a.FirstName, a.LastName, b.InvoiceID, b.InvoiceDate, b.BillingCountry
From Customer AS a
Inner Join Invoice AS b
ON a.CustomerID = b.CustomerID
Where Country = "Brazil";


-- Provide a query showing only the Employees who are Sales Agents.
SELECT title FROM Employee WHERE title LIKE "Sa%";

-- Provide a query showing a unique list of billing countries from the Invoice table.
SELECT DISTINCT BillingCountry as bc 
FROM Invoice 
ORDER BY bc;

-- Provide a query showing the invoices of customers who are from Brazil.
SELECT * FROM Invoice WHERE BillingCountry = 'Brazil';


-- Provide a query that shows the invoices associated with each sales agent. 
-- The resultant table should include the Sales Agent's full name.
select e.EmployeeId
, CONCAT(e.LastName, "," , e.FirstName) as 'Full Name'
, c.CustomerId
, i.*
from Employee as e 
inner join Customer as c 
	on e.EmployeeId = c.SupportRepId
inner join Invoice as i
	on c.CustomerId = i.CustomerId;


--  Provide a query that shows the Invoice Total, Customer name, Country and Sale Agent name for all invoices and customers.
select c.CustomerId
, c.LastName
, c.FirstName
, c.Company
, c.Country
, e.LastName
, e.FirstName
, i.Total
from Customer as c 
inner join Employee as e 
on e.EmployeeId = c.SupportRepId
inner join Invoice as i
on c.CustomerId = i.CustomerId;


--  How many Invoices were there in 2009 and 2011? What are the respective total sales for each of those years?

select sum(Total) from Invoice where InvoiceDate like '2010%';
select sum(Total) from Invoice where InvoiceDate like '2011%';

--  Looking at the InvoiceLine table, provide a query that COUNTs the number of line items for Invoice ID 37.
select count(InvoiceLineId) from InvoiceLine where InvoiceId = 37;

-- Looking at the InvoiceLine table, provide a query that COUNTs the number of line items for each Invoice. HINT: GROUP BY
SELECT invoiceid, count(invoicelineid)
FROM invoiceline
GROUP BY invoiceid;

-- 12) Provide a query that includes the track name with each invoice line item. 
Select i.InvoiceLineID, t.Name
From Track as t
Inner Join InvoiceLine as i
On t.TrackID = i.TrackID
Order By InvoiceLineId;

-- Provide a query that includes the purchased track name AND artist name with each invoice line item.
SELECT 
    i.InvoiceLineId,
    t.Name,
    a.Name
FROM InvoiceLine AS i
INNER JOIN Track AS t
    ON i.TrackId = t.TrackId
INNER JOIN Artist AS a
    ON a.ArtistId = t.AlbumId;

-- Provide a query that shows the # of invoices per country. HINT: GROUP BY
select BillingCountry, count(InvoiceId) from Invoice group by BillingCountry;

-- Provide a query that shows the total number of tracks in each playlist. The Playlist name should be include on the resultant table.
SELECT a.Name, COUNT(b.Trackid) as "Total Number of Tracks"
FROM Playlist AS a
INNER JOIN PlaylistTrack AS b
ON a.Playlistid = b.Playlistid
GROUP BY b.Playlistid;
-- Provide a query that shows all the Tracks, but displays no IDs. The resultant table should include the Album name, Media type and Genre.
select t.Name
, t.AlbumId
, t.MediaTypeId
, t.GenreId
, t.Composer
, t.Milliseconds
, t.Bytes
, t.UnitPrice
, a.Title
, g.Name
from Track as t
inner join Album as a
	on t.AlbumId = a.AlbumId
inner join Genre as g
	on t.GenreId = g.GenreId;
-- Provide a query that shows all Invoices but includes the # of invoice line items.
SELECT a.*, COUNT(b.invoicelineid) as "number of invoice line items"
  FROM invoice AS a
  INNER JOIN invoiceline AS b
  ON a.invoiceid = b.invoiceid
  GROUP BY a.invoiceid;

-- Provide a query that shows total sales made by each sales agent.

-- SELECT e.*, sum(i.total) AS 'Total Number of Sales'
-- FROM employee AS e
-- 	JOIN customer AS c 
--     ON e.employeeid = c.supportrepid
-- 	JOIN invoice AS i 
--     ON i.customerid = c.customerid
-- GROUP BY e.employeeid;

SELECT CONCAT(e.FirstName, ",", e.LastName) as "Full Name", SUM(i.Total)
FROM Employee AS e
INNER JOIN Customer AS c
on e.EmployeeId = c.SupportRepId
INNER JOIN Invoice AS i
ON c.CustomerId = i.CustomerId
GROUP BY e.EmployeeId;

-- Which sales agent made the most in sales in 2009?
select c.SupportRepId
, sum(i.Total)
from Customer as c
inner join Invoice as i
	on i.CustomerId = c.CustomerId
where i.InvoiceDate like '2009%'
group by c.SupportRepId 
order by (sum(i.Total)) desc
limit 1;


-- Which sales agent made the most in sales in 2010?
-- select c.SupportRepId
-- , sum(i.Total)
-- from Customer as c
-- inner join Invoice as i
-- 	on i.CustomerId = c.CustomerId
-- where i.InvoiceDate like '2010%'
-- group by c.SupportRepId 
-- order by (sum(i.Total)) desc
-- limit 1;

select c.SupportRepId
, sum(i.Total)
from Customer as c
inner join Invoice as i
	on i.CustomerId = c.CustomerId
WHERE YEAR(i.InvoiceDate) = "2010"
group by c.SupportRepId 
order by (sum(i.Total)) desc
limit 1;

-- Which sales agent made the most in sales over all?
 select c.SupportRepId
, sum(i.Total)
from Customer as c
inner join Invoice as i
on i.CustomerId = c.CustomerId
group by c.SupportRepId 
limit 1;

-- Provide a query that shows the # of customers assigned to each sales agent.
SELECT e.LastName, e.FirstName, count(c.customerid) AS 'TotalCustomers'
FROM employee as e
JOIN customer AS c ON e.employeeid = c.supportrepid
GROUP BY e.employeeid;

-- Provide a query that shows the total sales per country. Which country's customers spent the most?
SELECT i.billingcountry, sum(total) AS 'Total Sales'
FROM invoice AS i
GROUP BY billingcountry
ORDER BY totalsales DESC;

-- 24) Provide a query that shows the most purchased track of 2013.
Select t.Name As 'Track Name', Count(il.InvoiceId) As '# Purchased'
From Track t
Inner Join InvoiceLine il
On il.TrackId = t.TrackId
Inner Join Invoice i
On il.invoiceId = i.invoiceId
WHERE YEAR(i.InvoiceDate) = "2013"
Group By Name
Order By Count(il.InvoiceId) DESC
Limit 1;
-- Provide a query that shows the top 5 most purchased tracks over all.
select il.TrackId, t.name ,count(i.InvoiceId) as "# Track Purchases"
from Invoice as i
inner join InvoiceLine as il
on i.InvoiceId = il.InvoiceId
inner join Track as t 
on t.trackid = il.trackid
group by il.TrackId
order by (count(i.InvoiceId)) desc
limit 5;

-- Provide a query that shows the top 3 best selling artists.
Select t.composer As 'Artist', count(il.InvoiceID) As "Tracks Sold"
From Track t
Inner Join InvoiceLine il
On t.TrackId = il.TrackId
Group By Composer
Order by count(il.InvoiceID) DESC;

-- Provide a query that shows the most purchased Media Type.
select mt.Name, count(i.InvoiceId) as "Purchase Counts"
from Invoice as i
inner join InvoiceLine as il
	on i.InvoiceId = il.InvoiceId
inner join Track as t
	on t.TrackId = il.TrackId
inner join MediaType as mt
	on t.MediaTypeId = mt.MediaTypeId
group by mt.Name
order by count(i.InvoiceId) desc;
