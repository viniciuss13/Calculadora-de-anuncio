from unittest import TestCase
from datetime import date

from ad import Advertising


class TestAdvertising(TestCase):
    def setUp(self) -> None:
        self.ad = Advertising(
            name="test",
            client="client1",
            start_date=date(2020, 3, 1),
            end_date=date(2021, 3, 1),
            budget_per_day=10.5
        )

    def test_total_investment(self):
        self.assertEqual(self.ad.total_investment, 3_832.5)

    def test_total_views(self):
        self.assertEqual(self.ad.total_views, 791_028)

    def test_total_clicks(self):
        self.assertEqual(self.ad.total_clicks, 13_797)

    def test_total_shares(self):
        self.assertEqual(self.ad.total_shares, 2_069)
