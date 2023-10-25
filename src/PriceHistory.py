import sqlite3
import matplotlib.pyplot as plt

class PriceHistory:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def get_price_history(self, wine_id):
        self.cursor.execute('''
            SELECT sale_date, price
            FROM sale_details
            JOIN sales ON sale_details.sale_id = sales.sale_id
            WHERE sale_details.wine_id = ?
            ORDER BY sale_date
        ''', (wine_id,))
        return self.cursor.fetchall()

    def plot_price_history(self, wine_id, start_date=None, end_date=None):
        price_history = self.get_price_history(wine_id)
        
        if not price_history:
            print("No price history found for the specified wine.")
            return

        sale_dates, prices = zip(*price_history)

        if start_date and end_date:
            filtered_dates, filtered_prices = [], []
            for date, price in zip(sale_dates, prices):
                if start_date <= date <= end_date:
                    filtered_dates.append(date)
                    filtered_prices.append(price)
            sale_dates, prices = filtered_dates, filtered_prices

        plt.figure(figsize=(10, 6))
        plt.plot(sale_dates, prices, marker='o', linestyle='-')
        plt.title("Price History for Wine (Wine ID: {})".format(wine_id))
        plt.xlabel("Sale Date")
        plt.ylabel("Price")
        plt.grid()
        plt.xticks(rotation=45)
        plt.tight_layout()

        plt.show()

    def close(self):
        self.conn.close()
