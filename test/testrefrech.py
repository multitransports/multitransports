import unittest
import sqlite3
import os
from back.refresh import refresh


class TestApp(unittest.TestCase):
    
    def test_refresh(self):
        list_ville = [
        {
        "name" : 'Montpellier',
        "file" : 'Montpelliertest.csv',
        "url" : 'https://data.montpellier3m.fr/sites/default/files/ressources/TAM_MMM_TpsReel.csv'
        }]
        conn = sqlite3.connect('./test/transport_test.db')
        c = conn.cursor()
        self.assertEqual(os.path.exists('Montpelliertest.csv'), False)
        refresh(list_ville[0],c,conn)
        self.assertEqual(os.path.exists('Montpelliertest.csv'), True)
        os.remove('Montpelliertest.csv')

if __name__ == '__main__':
    unittest.main()