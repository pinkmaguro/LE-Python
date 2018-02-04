import sqlite3

class SimpleDAO:
    """ 간단한 DAO 클래스를 만들어보겠다. """
    def __init__(self, con, table, num_col):
        self.con = con
        self.cur = self.con.cursor()
        self.table = table
        self.num_col = num_col
    
    def insertOne(self, data):
        val_str = ','.join('?' * self.num_col)
        sql = 'INSERT INTO ' + self.table + ' VALUES(' + val_str + ');'
        print('sql : ', sql)
        self.cur.execute(sql, data)
        self.con.commit()
    
    def delteAll(self):
        sql = 'DELETE FROM ' + self.table
        self.cur.execute(sql)
        self.con.commit()

    def count(self):
        sql = 'SELECT COUNT(*) FROM ' + self.table
        self.cur.execute(sql)
        result = [r for r in self.cur]
        return result[0][0]
