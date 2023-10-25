import sqlite3

class WineScores:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def add_score(self, wine_id, user_id, score, comment=None):
        self.cursor.execute('''
            INSERT INTO wine_scores (wine_id, user_id, score, comment)
            VALUES (?, ?, ?, ?)
        ''', (wine_id, user_id, score, comment))
        self.conn.commit()
        return self.cursor.lastrowid

    def get_scores_by_wine(self, wine_id):
        self.cursor.execute('SELECT * FROM wine_scores WHERE wine_id = ?', (wine_id,))
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()
