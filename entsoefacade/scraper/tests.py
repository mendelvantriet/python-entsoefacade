from django.test import TestCase
from entsoefacade.scraper.scrapers import TransmissionScraper
import pandas as pd


class ScraperTestCase(TestCase):

    def test_entsoe_client(self):
        start = pd.Timestamp('20220101', tz='Europe/Brussels')
        end = pd.Timestamp('20220102', tz='Europe/Brussels')
        country_code_from = 'NL'
        country_code_to = 'DE'

        ts = TransmissionScraper()
        df = ts.cross_border_flows(country_code_from, country_code_to, start, end)
        self.assertIn('capacity', df, 'cross_border_flows should return capacity')
        self.assertEquals(df['capacity'].squeeze().dtype, float, 'Capacity should be float')
