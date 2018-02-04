import sqlite3
import unittest
from sqldao import SimpleDAO

class TestSQLite(unittest.TestCase):
    """ sqlite db 가 동작하는지 간단하게 테스트하는 클래스 """
    def setUp(self):
        print('Preapre test')
        self.con = sqlite3.connect('test.db')
        self.cur = self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS PhoneBook(Name text, PhonNum text);")
        self.cur.execute("DELETE FROM PhoneBook")

    def test_insert_one(self):
        name = 'Ryan'
        phone = '010-1234'
        self.cur.execute("INSERT INTO PhoneBook VALUES(?,?);",(name, phone))
        self.cur.execute("SELECT COUNT(*) FROM  PhoneBook;")
        result = self.cur.fetchall()
        print(result)
        self.assertEqual(1, result[0][0])
        self.cur.execute("INSERT INTO PhoneBook VALUES(?,?);",(name, phone))
        self.cur.execute("SELECT COUNT(*) FROM  PhoneBook;")
        result = self.cur.fetchall()
        print(result)
        self.assertEqual(2, result[0][0])


    def tearDown(self):
        print('Terminate test')
        
class TestSimpleDAO(unittest.TestCase):
    """ sqlite db 에 대한 DAO 클래스에 대한 유닛테스트 """
    def setUp(self):
        print('Preapre test for SimpleDAO')
        self.con = sqlite3.connect('test.db')
        self.cur = self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS Members(Name text, Age integer);")
        self.dao = SimpleDAO(self.con, 'Members', 2)

    def test_insertOne(self):
        self.dao.delteAll()
        self.assertEqual(0, self.dao.count())
        data = ('Shanon', 20)
        self.dao.insertOne(data)
        self.assertEqual(1, self.dao.count())

if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    load_from = unittest.defaultTestLoader.loadTestsFromTestCase
    suite.addTests(load_from(TestSimpleDAO))
    unittest.TextTestRunner(verbosity=2).run(suite)