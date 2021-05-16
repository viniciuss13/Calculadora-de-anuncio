from datetime import date
from unittest import TestCase

from ad import Advertising
from report import filter_ads, create_report


def create_ad_report_dict(ad: Advertising):
    return {
        "investment": ad.total_investment,
        "clicks": ad.total_clicks,
        "views": ad.total_views,
        "shares": ad.total_shares
    }


class TestReport(TestCase):
    def setUp(self) -> None:
        self.ad_list = [
            Advertising("test1", "client1", start_date=date(2020, 3, 1), end_date=date(2021, 3, 1), budget_per_day=1.5),
            Advertising("test2", "client2", start_date=date(2015, 3, 1), end_date=date(2018, 3, 1), budget_per_day=1.5),
        ]

    def test_filter_ads(self):
        for ad in self.ad_list:
            self.assertEqual(filter_ads(self.ad_list, client=ad.client), [ad], "Falha no filtro de cliente")
            self.assertEqual(filter_ads(self.ad_list, start_date=ad.start_date, end_date=ad.end_date),
                             [ad], "Falha no filtro de data")

        self.assertEqual(filter_ads(self.ad_list), self.ad_list, "Falha no filtro vazio")
        self.assertEqual(filter_ads(self.ad_list, client="unknown"), [], "Falha no filtro errado")

    def test_print_report(self):
        for ad in self.ad_list:
            self.assertEqual(create_report([ad], False), create_ad_report_dict(ad))
        self.assertEqual(create_report([], False),
                         create_ad_report_dict(Advertising("", "", date(2020, 1, 1), date(2020, 1, 1), 0)))
