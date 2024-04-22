import sqlite3

class Database:
    def __init__(self, db_name):
        self.connect = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.connect.cursor()

    def get_all_regions(self):
        self.cursor.execute("""SELECT * FROM regions""")
        regions = dict_fetch_all(self.cursor)
        return regions

    def get_countries_by_region(self, region_id):
        self.cursor.execute("""SELECT * FROM countries WHERE region_id = ?""", (region_id,))
        countries = dict_fetch_all(self.cursor)
        return countries

def dict_fetch_all(cursor):
    keys = [i[0] for i in cursor.description]
    return [dict(zip(keys, row)) for row in cursor.fetchall()]
