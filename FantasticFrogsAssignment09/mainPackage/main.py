# File Name : main.py
# Student Name: Jacob Brumfield, Nikki Carfora, Ray Happel
# email:  brumfijb@mail.uc.edu, happelrc@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date:  4/3/2025
# Course #/Section:  IS 4010 001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  Connect to the professors SQL database to produce interesting results
 
# Brief Description of what this module does: This module initializes the databaseManagement class and 
# randomly selects the productID and states the manufacurer that created the product.
# Citations: In Class work, https://stackoverflow.com/questions/28981770/store-sql-result-in-a-variable-in-python,
 
# Anything else that's relevant:

import pyodbc
import random
from dataPackage.databaseManagement import databaseManagement

def main():
    dbm = databaseManagement()
    conn = dbm.connect_to_database()

    if conn is None:
        print("Failed to connect to the database.")
        return

 
    sql_query = "SELECT ProductID, [UPC-A ], Description, ManufacturerID, BrandID FROM tProduct"
    product_rows = dbm.submit_sql_to_server(sql_query, conn)

    if not product_rows:
        print("No data found in tProduct.")
        return

   
    selected_row = random.choice(product_rows)
    product_id = selected_row[0]
    description = selected_row[2]
    manufacturer_id = selected_row[3]
    brand_id = selected_row[4]

    print(f"Randomly selected product: {description} (ProductID: {product_id})")

   
    manufacturer_name = dbm.fetch_manufacturer_name(manufacturer_id, conn)

    if manufacturer_name:
        print(f"The manufacturer of this product is: {manufacturer_name}")
    else:
        print(f"Manufacturer with ID {manufacturer_id} not found.")

if __name__ == "__main__":
    main()