import sqlite3


class DataBase:
    def __init__(self, file):
        self.con = sqlite3.connect(file)
        self.cur = self.con.cursor()

    def clear(self):
        self.cur.execute('''DELETE FROM game''')
        self.con.commit()

    def new_user(self, id, msg):
        self.cur.execute('''INSERT INTO game(id_user, choice) VALUES (?, ?)''', (id, msg))
        self.con.commit()

    def check_id(self, id):
        res = self.cur.execute('''SELECT id_user FROM game WHERE id_user = ?''', (id, )).fetchall()
        return bool(len(res))

    def get_info(self):
        return self.cur.execute('''SELECT choice FROM game''').fetchall()

    def get_id(self):
        print(self.cur.execute('''SELECT id_user FROM game''').fetchall())
        return self.cur.execute('''SELECT id_user FROM game''').fetchall()
