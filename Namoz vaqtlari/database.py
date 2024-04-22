import sqlite3


class Data:
    def __init__(self, database):
        self.conn = sqlite3.connect(database, check_same_thread=False)
        self.cur = self.conn.cursor()

    def get_regions(self):
        self.cur.execute("""select * from regions""")
        regions = dict_fetchall(self.cur)
        return regions

    def get_cities(self, id):
        self.cur.execute("""select * from cities where region_id == ? """, (id,))
        regions = dict_fetchall(self.cur)
        return regions

def dict_fetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def dict_fetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))
