import unittest
import sqlite3
from back.load_csv import load_csv


class TestApp(unittest.TestCase):
    def test_loadcsv(self):
        conn = sqlite3.connect('./test/transport_test.db')
        c = conn.cursor()
        c.execute(
            """
            DROP TABLE IF EXISTS 'infoarret'"""
            )
        c.execute("""
            CREATE TABLE IF NOT EXISTS 'infoarret' (
            "Station"	TEXT,
            "Ligne"	TEXT,
            "Direction"	TEXT,
            "Horaire"	TEXT,
            "Ville" TEXT);""")
        self.assertEqual(len(c.fetchall()),0)
        load_csv("./test/Montpellier_test.csv",c,"Montpellier")
        c.execute(
            """
            SELECT * FROM 'infoarret';
            """)
        self.assertEqual(len(c.fetchall()),21)
        
        conn.commit()
        conn.close()