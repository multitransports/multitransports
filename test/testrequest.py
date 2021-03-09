import unittest
import sqlite3
from back.requestsapi import *


class TestApp(unittest.TestCase):
    def test_requestnexttram(self):
        conn = sqlite3.connect('./test/transport_test.db')
        c = conn.cursor()
        self.assertEqual(type(requestnexttram(c,"JACOU","Montpellier")),list)
        self.assertIsNotNone(requestnexttram(c,"JACOU","Montpellier"))

    def test_request_city_station(self):
        conn = sqlite3.connect('./test/transport_test.db')
        c = conn.cursor()   
        self.assertIs(type(request_city_station(c,"Montpellier")), list)
        self.assertIsNotNone(request_city_station(c,"Montpellier"))



if __name__ == '__main__':
    unittest.main()