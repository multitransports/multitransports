import unittest
import sqlite3
from back.addtotable import insert_csv_row


class TestApp(unittest.TestCase):

    def test_addtotable(self):
        conn = sqlite3.connect('./test/transport_test.db')
        c = conn.cursor()
        c.execute(
            """
            DROP TABLE IF EXISTS 'infoarret'"""
            )
        c.execute("""
            CREATE TABLE IF NOT EXISTS "infoarret" (
            "Station"	TEXT,
            "Ligne"	TEXT,
            "Direction"	TEXT,
            "Horaire"	TEXT,
            "Ville" TEXT);""")
        c.execute(
            """
            SELECT * FROM 'infoarret';
            """)
        self.assertEqual(c.fetchone(), None)
        with open('./test/Montpellier_test.csv', "r", encoding="utf-8") as f:    
            f.readline()
            line = f.readline()
            while line:
                insert_csv_row(line, c, "Montpellier")
                line = f.readline()
        conn.commit()
        c.execute(
            """
            SELECT * FROM 'infoarret';
            """)
        self.assertEqual(c.fetchone(), ('BOUTONNET', '1', 'MOSSON', '19:14:38', 'Montpellier'))


if __name__ == '__main__':
    unittest.main()