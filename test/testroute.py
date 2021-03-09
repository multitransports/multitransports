import unittest
import app
from back.route import *


class TestApp(unittest.TestCase):
    def test_nexttram(self):
        tester = app.app.test_client(self)
        response = tester.get("/Montpellier/stations/JACOU")
        status_code = response.status_code
        self.assertEqual(status_code, 200)
        self.assertEqual(response.content_type, "application/json")
        self.assertTrue(b'Horaire' in response.data)

    def test_citystation(self):
        tester = app.app.test_client(self)
        response = tester.get("/Montpellier/stations/")
        status_code = response.status_code
        self.assertEqual(status_code, 200)
        self.assertEqual(response.content_type, "application/json")
        self.assertTrue(b'Station' in response.data)

    def test_line_station(self):
        tester = app.app.test_client(self)
        response = tester.get("/Montpellier/ligne/2")
        status_code = response.status_code
        self.assertEqual(status_code, 200)
        self.assertEqual(response.content_type, "application/json")
        self.assertTrue(b'Station' in response.data)

    def test_next_to_direction(self):
        tester = app.app.test_client(self)
        response = tester.get("/Montpellier/JACOU/2/SABINES")
        status_code = response.status_code
        self.assertEqual(status_code, 200)
        self.assertEqual(response.content_type, "application/json")
        self.assertTrue(b'Direction' in response.data)

    def test_station_like(self):
        tester = app.app.test_client(self)
        response = tester.get("/Montpellier/stationslike/COMEDIE")
        status_code = response.status_code
        self.assertEqual(status_code, 200)
        self.assertEqual(response.content_type, "application/json")
        self.assertTrue(b'Ligne' in response.data)