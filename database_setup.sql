-- Create the database
CREATE DATABASE IF NOT EXISTS medical;

-- Use the medical database
USE medical;

-- Create the stock table
CREATE TABLE IF NOT EXISTS stock (
    mcode INT PRIMARY KEY,
    mname VARCHAR(100),
    dateofexp DATE,
    quan INT,
    price DECIMAL(10, 2)
);

-- Create the bill table
CREATE TABLE IF NOT EXISTS bill (
    bill_id INT AUTO_INCREMENT PRIMARY KEY,
    mobile INT,
    mcode INT,
    mname VARCHAR(100),
    quan INT,
    price DECIMAL(10, 2),
    FOREIGN KEY (mcode) REFERENCES stock(mcode)
);

-- Create the staff table
CREATE TABLE IF NOT EXISTS staff (
    sid INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    profile VARCHAR(100),
    mobile INT
);

-- Sample data for stock table
INSERT INTO stock (mcode, mname, dateofexp, quan, price)
VALUES 
    (101, 'DOLO TABLET', '2025-12-31', 100, 150),
    (102, 'CIPLOX', '2025-12-31', 200, 120),
    (103, 'SANITIZER', '2025-12-31', 50, 220),
    (104, 'LIFEBOY SOAP', '2025-12-31', 300, 60),
    (105, 'SURGICAL MASK', '2025-12-31', 500, 20),
    (106, 'DETTOL', '2025-12-31', 150, 90),
    (107, 'VICKS', '2025-12-31', 250, 50);

-- Sample data for staff table
INSERT INTO staff (sid, name, age, profile, mobile)
VALUES 
    (1, 'John Doe', 30, 'Pharmacist', 1234567890),
    (2, 'Jane Smith', 25, 'Sales', 9876543210);
