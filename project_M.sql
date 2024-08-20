create database Hospital;

 use Hospital;
 
 create table Inventory (
BillDate date,
TQty int,
UCPwithoutGST float,
PurGSTPer float,
MRP float,
TotalCost float,
TotalDiscount float,
NetSales float,
ReturnMRP float,
GenericName varchar(500),
SubCategory varchar(150),
SubCategoryL3 varchar(150),
AnonymizedBillNo varchar(150),
AnonymizedSpecialisation varchar(50) );


set global local_infile = ON;

LOAD DATA LOCAL INFILE '/Users/mac/Documents/Project 1/SAMPLEMIODATA.csv'
INTO TABLE Inventory 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n' 
IGNORE 1 ROWS;

select* from Inventory;




select count(TQty) from Inventory where TQty < 0 ;

select count(TQty) from Inventory where TQty > 0 ;


-- null values checking--

select * from Inventory where Genericname is null   ;

-- no null values present in this data 


-- top sales drugs --

SELECT GenericName, SUM(TQty) AS Total_Quantity, SUM(NetSales) AS Sales
FROM Inventory
GROUP BY GenericName
ORDER BY Sales DESC;


-- top 10 sales drugs--

SELECT GenericName, SUM(NetSales) AS TotalSales
FROM Inventory
GROUP BY GenericName
ORDER BY TotalSales DESC
LIMIT 10;

SELECT SubCategoryL3, SUM(NetSales) AS TotalSales
FROM Inventory
GROUP BY SubCategoryL3
ORDER BY TotalSales DESC;



SELECT GenericName, Subcategory, SUM(TQty) AS Total_Quantity, SUM(NetSales) AS Sales
FROM Inventory
GROUP BY GenericName, Subcategory
ORDER BY Sales DESC;


-- Sub-Categorywise Sales --

WITH RankedSales AS (
    SELECT 
        GenericName, 
        Subcategory, 
        SUM(TQty) AS Total_Quantity, 
        SUM(NetSales) AS Sales,
        ROW_NUMBER() OVER (PARTITION BY Subcategory ORDER BY SUM(NetSales) DESC) AS rn
    FROM Inventory
    GROUP BY GenericName, Subcategory
)
SELECT GenericName, Subcategory, Total_Quantity, Sales
FROM RankedSales
WHERE rn = 1;


-- SubCategorywiseL3 wise Sales --

SELECT SubCategoryL3, SUM(NetSales) AS TotalSales
FROM Inventory
GROUP BY SubCategoryL3
ORDER BY TotalSales DESC;








SELECT GenericName, TQty, COUNT(*) AS SalesCount 
FROM Inventory 
GROUP BY GenericName, TQty
Order By SalesCount DESC;



SELECT GenericName, TQty, COUNT(*) AS SalesCount 
FROM Inventory 
WHERE GenericName = 'MEROPENEM 1GM INJ'
GROUP BY GenericName, TQty
ORDER BY SalesCount DESC;


select day(BillDate) as Day ,sum(TQty) as Total_Quantity_sold
from Inventory 
group by Day(BillDate)
Order by day(BillDate) ;

-- week wise sales --
SELECT week(BillDate) AS week, SUM(TQty) AS Total_Quantity_sold
FROM Inventory 
GROUP BY week(BillDate)
ORDER BY week ASC;

-- year wuse sales --
SELECT year(BillDate) AS year, SUM(TQty) AS Total_Quantity_sold 
FROM Inventory 
GROUP BY year(BillDate)
ORDER BY year ASC;


-- Month wise sales in 2020-- 

SELECT MONTH(BillDate) AS Month, SUM(TQty) AS Total_Quantity_sold
FROM Inventory
WHERE YEAR(BillDate) = 2020
GROUP BY MONTH(BillDate)
ORDER BY MONTH(BillDate) ASC;


-- Month wise sales in 2021-- 
SELECT MONTH(BillDate) AS Month, SUM(TQty) AS Total_Quantity_sold
FROM Inventory
WHERE YEAR(BillDate) = 2021
GROUP BY MONTH(BillDate)
ORDER BY MONTH(BillDate) ASC;

-- Month wise sales in 2022-- 
SELECT MONTH(BillDate) AS Month, SUM(TQty) AS Total_Quantity_sold
FROM Inventory
WHERE YEAR(BillDate) = 2022
GROUP BY MONTH(BillDate)
ORDER BY MONTH(BillDate) ASC;

select* from Inventory;

-- All three year Sales -- 
SELECT DATE_FORMAT(BillDate, '%Y-%m') AS Month, SUM(NetSales) AS TotalSales, SUM(TQty) AS TotalQuantity
FROM Inventory
GROUP BY Month
ORDER BY Month;


SELECT GenericName, SUM(NetSales) AS TotalSales
FROM Inventory
GROUP BY GenericName
ORDER BY TotalSales DESC
LIMIT 10;

-- sales by Annonymization --

SELECT AnonymizedSpecialisation, SUM(NetSales) AS TotalSales
FROM Inventory
GROUP BY AnonymizedSpecialisation
ORDER BY TotalSales DESC;

SELECT GenericName, SUM(TotalCost) AS TotalCost, SUM(NetSales) AS TotalSales, 
       (SUM(NetSales) - SUM(TotalCost)) AS Profit
FROM Inventory
GROUP BY GenericName
ORDER BY Profit DESC;

SELECT 
    DATE_FORMAT(BillDate, '%Y-%m') AS Month, 
    SUM(NetSales) AS TotalSales, 
    SUM(TQty) AS TotalQuantity, 
    (SUM(NetSales) / SUM(TQty)) AS AvgSalesPricePerUnit,(SUM(NetSales) - SUM(TotalCost)) AS Profit
FROM Inventory
GROUP BY Month
ORDER BY Month;


SELECT 
    GenericName,
    MONTH(BillDate) AS Month,
    SUM(NetSales) AS TotalSales,
    AVG(SUM(NetSales)) OVER (PARTITION BY GenericName, MONTH(BillDate)) AS AvgMonthlySales
FROM Inventory
GROUP BY GenericName, Month
ORDER BY GenericName, Month;




-- Returnrate by generic name ---

SELECT 
    GenericName, 
    SUM(ReturnMRP) AS TotalReturns, 
    SUM(NetSales) AS TotalSales, 
    (SUM(ReturnMRP) / SUM(NetSales)) * 100 AS ReturnRate
FROM Inventory
GROUP BY GenericName
ORDER BY ReturnRate DESC;











