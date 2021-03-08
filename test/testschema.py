import unittest
import sqlite3
from back.create_schema import create_schema


class TestApp(unittest.TestCase):

    def test_createschema(self):
        conn = sqlite3.connect(":memory:")
        c = conn.cursor()
        create_schema(c)
        self.assertEqual(c.rowcount,-1)
        self.assertIsNotNone(":memory:")
        self.assertEqual(len(c.fetchall()),0)
        #print(c.rowcount)
        # nbrligne = c.execute("""SELECT COUNT(*) FROM ":memory:" """)
        # print(nbrligne)
        # self.assertEqual(nbrligne,1)
        conn.commit()
        conn.close()







if __name__ == '__main__':
    unittest.main()