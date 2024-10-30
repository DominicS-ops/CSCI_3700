# Flask PostgreSQL Integration Project

## Overview  
This project demonstrates how to connect PostgreSQL with Flask and perform basic CRUD operations. It includes API endpoints to insert and retrieve data from two tables: `basket_a` and `basket_b`.  

---

## 1. Local Test Setup  (Quick Start)

First, install a Python 3 virtual environment:  
```bash
sudo apt-get install python3-venv
```  

Create a virtual environment:  
```bash
python3 -m venv python_venv
```  

Activate the virtual environment:  
```bash
source python_venv/bin/activate
```  

Install the necessary dependencies:  
```bash
pip3 install -r requirements.txt
```  

Start the Flask server:  
```bash
python3 main.py
```  

---

## 2. Setting up the PostgreSQL Database  (Ignore if database is set up)

Ensure PostgreSQL is installed and running on your machine. If not, install it:  
```bash
sudo apt-get install postgresql postgresql-contrib
```  

Log in to the PostgreSQL shell:  
```bash
sudo -u postgres psql
```  

Create a new database and the required tables:  
```sql
CREATE DATABASE fruit_db;
\c fruit_db;

CREATE TABLE basket_a (
    a INT PRIMARY KEY,
    fruit_a VARCHAR(100) NOT NULL
);

CREATE TABLE basket_b (
    b INT PRIMARY KEY,
    fruit_b VARCHAR(100) NOT NULL
);
```  

Insert initial data into the tables:  
```sql
INSERT INTO basket_a (a, fruit_a) VALUES
    (1, 'Apple'),
    (2, 'Orange'),
    (3, 'Banana'),
    (4, 'Cucumber');

INSERT INTO basket_b (b, fruit_b) VALUES
    (1, 'Orange'),
    (2, 'Apple'),
    (3, 'Watermelon');
```  


---

## 3. API Endpoints  

- **Insert into Basket A**  
- 
  **URL:** `127.0.0.1:5000/api/update_basket_a`  
  
  **Description:**  
  - This endpoint inserts a new row with `(5, 'Cherry')` into `basket_a`.  
  - If the operation is successful, the browser will display:  
    ```text
    Success!
    ```  
  - If there’s an error, the error message from PostgreSQL will be shown in the browser.  
---
- **View Unique Fruits**  
- 
  **URL:** `127.0.0.1:5000/api/unique`  
  
  **Description:**  
  - This endpoint retrieves and displays unique fruits from `basket_a` and `basket_b` in an HTML table.  
  - If there’s an error, the error message from PostgreSQL will be shown in the browser.  


---

## 4. Team Members  

- [Dominic Segobiano]  
- [Ricardo Sanchez-McKenzie]  


