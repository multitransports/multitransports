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

    def test_request_line_station(self):
        conn = sqlite3.connect('./test/transport_test.db')
        c = conn.cursor()
        self.assertEqual(type(request_line_station(c, "Montpellier","2")),list)
        self.assertIsNotNone(request_line_station(c, "Montpellier","2"))

    def test_request_next_to_direction(self):
        conn = sqlite3.connect('./test/transport_test.db')
        c = conn.cursor()
        self.assertEqual(type(request_next_to_direction(c,"Montpellier", "JACOU", "2", "SABINES")),list)
        self.assertIsNotNone(request_next_to_direction(c,"Montpellier", "JACOU", "2", "SABINES"))

    def test_request_station_like(self):
        conn = sqlite3.connect('./test/transport_test.db')
        c = conn.cursor()
        self.assertEqual(type(request_station_like(c,"JACOU","Montpellier")),list)
        self.assertIsNotNone(request_station_like(c,"JACOU","Montpellier"))


if __name__ == '__main__':
    unittest.main()