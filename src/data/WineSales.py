import sqlite3

class WineSales:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS sales (
                sale_id INTEGER PRIMARY KEY,
                sale_date DATE,
                total_price REAL
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS sale_details (
                detail_id INTEGER PRIMARY KEY,
                sale_id INTEGER,
                wine_id INTEGER,
                price REAL,
                FOREIGN KEY (sale_id) REFERENCES sales(sale_id),
                FOREIGN KEY (wine_id) REFERENCES wine_properties(wine_id)
            )
        ''')
        self.conn.commit()

    def insert_sale(self, sale_date, total_price):
        self.cursor.execute('''
            INSERT INTO sales (sale_date, total_price)
            VALUES (?, ?)
        ''', (sale_date, total_price))
        self.conn.commit()
        return self.cursor.lastrowid

    def insert_sale_detail(self, sale_id, wine_id, price):
        self.cursor.execute('''
            INSERT INTO sale_details (sale_id, wine_id, price)
            VALUES (?, ?, ?)
        ''', (sale_id, wine_id, price))
        self.conn.commit()

    def get_sale(self, sale_id):
        self.cursor.execute('SELECT * FROM sales WHERE sale_id = ?', (sale_id,))
        return self.cursor.fetchone()

    def get_sale_details(self, sale_id):
        self.cursor.execute('SELECT * FROM sale_details WHERE sale_id = ?', (sale_id,))
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()

# Example usage:
if __name__ == "__main__":
    wine_sales_db = WineSales("your_database_file.db")
    wine_sales_db.create_tables()
    
    # Insert a sale
    sale_id = wine_sales_db.insert_sale("2023-10-23", 150.99)

    # Insert sale details
    wine_sales_db.insert_sale_detail(sale_id, wine_id, 30.99)
    wine_sales_db.insert_sale_detail(sale_id, another_wine_id, 45.99)

    # Retrieve sale and sale details
    sale = wine_sales
