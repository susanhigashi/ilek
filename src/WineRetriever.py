import sqlite3

class WineRetriever:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def retrieve_wines_by_score_mean(self, min_price, max_price):
        self.cursor.execute('''
            SELECT wp.wine_id, wp.name, wp.price, AVG(ws.score) as avg_score
            FROM wine_properties wp
            LEFT JOIN wine_scores ws ON wp.wine_id = ws.wine_id
            WHERE wp.price BETWEEN ? AND ?
            GROUP BY wp.wine_id, wp.name, wp.price
            ORDER BY avg_score DESC
        ''', (min_price, max_price))

        wine_results = self.cursor.fetchall()
        return wine_results

    def close(self):
        self.conn.close()
