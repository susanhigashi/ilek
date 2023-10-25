import sqlite3

class Wine:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS wine_properties (
                wine_id INTEGER PRIMARY KEY,
                name TEXT,
                type TEXT,
                flavor TEXT,
                description TEXT,
                country TEXT,
                region TEXT,
                producer TEXT,
                year INTEGER,
                score_avg REAL 
            )
        ''')
        self.conn.commit()

    def insert_wine(self, name, wine_type, flavor, description, country, region, vintage):
        self.cursor.execute('''
            INSERT INTO wine_properties (name, type, flavor, description, country, region, producer, year, score_avg)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (name, wine_type, flavor, description, country, region, vintage))
        self.conn.commit()

    def get_wine(self, wine_id):
        self.cursor.execute('SELECT * FROM wine_properties WHERE wine_id = ?', (wine_id,))
        return self.cursor.fetchone()

    def update_wine(self, wine_id, name, wine_type, flavor, description, country, region, vintage):
        self.cursor.execute('''
            UPDATE wine_properties
            SET name = ?, type = ?, flavor = ?, description = ?, country = ?, region = ?, vintage = ?
            WHERE wine_id = ?
        ''', (name, wine_type, flavor, description, country, region, vintage, wine_id))
        self.conn.commit()

    def delete_wine(self, wine_id):
        self.cursor.execute('DELETE FROM wine_properties WHERE wine_id = ?', (wine_id,))
        self.conn.commit()

    def close(self):
        self.conn.close()

# Example usage:
if __name__ == "__main__":
    wine_db = Wine("your_database_file.db")
    wine_db.create_table()
    
    wine_db.insert_wine("Wine Name", "Red", "Fruity", "A great red wine", "France", "Bordeaux", 2019)
    wine = wine_db.get_wine(1)
    print(wine)

    wine_db.update_wine(1, "New Wine Name", "White", "Crisp", "A new white wine", "Italy", "Tuscany", 2020)
    updated_wine = wine_db.get_wine(1)
    print(updated_wine)

    wine_db.delete_wine(1)
    wine_db.close()
