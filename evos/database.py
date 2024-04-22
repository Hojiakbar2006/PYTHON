import sqlite3


class Database:
    def __init__(self, db_name):
        self.connect = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.connect.cursor()

    def create_user(self, chat_id):
        self.cursor.execute("""insert into user ("chat_id) values(?)""", (chat_id,))
        self.connect.commit()

    def update_user(self, chat_id, key, value):
        self.cursor.execute("""update users_info set ? = ? where chat_id = ?""", (key, value, chat_id))

    def get_user(self, chat_id):
        self.cursor.execute("""select * from users_info where chat_id = ?""", (chat_id,))
        user = dict_fetchone(self.cursor)


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



# connect = sqlite3.connect("user_db.db")
# cursor = connect.cursor()
#
# cursor.execute("""
# create table users_info (
#     "id" integer not null,
#     "name" text,
#     "last_name" text,
#     "phone_number" integer,
#     "chat_id" integer,
#     primary key("id" autoincrement)
# )
# """)
