from utils import *
import unittest


class TestUtils(unittest.TestCase):
    def test_views_budget(self):
        self.assertEqual(views_budget(1.), 30)
        self.assertEqual(views_budget(2.30), 69)
        self.assertEqual(views_budget(100), 3000)

    def test_clicks_views(self):
        self.assertEqual(clicks_views(100), 12)
        self.assertEqual(clicks_views(167), 20.04)
        self.assertEqual(clicks_views(170), 20.4)

    def test_shares_clicks(self):
        self.assertEqual(shares_clicks(100), 15)
        self.assertEqual(shares_clicks(130), 19.5)
        self.assertEqual(shares_clicks(170), 25.5)

    def test_views_shares(self):
        self.assertEqual(views_shares(100), 4000)
        self.assertEqual(views_shares(130), 5200)
        self.assertEqual(views_shares(170), 6800)

    def test_views_multiplier(self):
        self.assertEqual(views_multiplier(100), 400)
        self.assertEqual(views_multiplier(130), 520)
        self.assertEqual(views_multiplier(170), 680)

    def test_total_views(self):
        self.assertEqual(total_views(100), 20640)
        self.assertEqual(total_views(130), 26832)
        self.assertEqual(total_views(170), 35088)
