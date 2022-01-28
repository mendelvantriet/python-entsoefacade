import time

import pandas as pd
from entsoe import EntsoePandasClient

from entsoefacade import settings

country_connections = {
    'DE': ['AT', 'BE', 'CZ', 'DK', 'FR', 'LU', 'NL', 'NO', 'PL', 'SE', 'CH'],
    'NL': ['BE', 'DK', 'DE', 'NO', 'UK'],
}
tz = 'UTC'


def scrape_all(window_hours):
    end = pd.Timestamp.now(tz=tz)
    start = end - pd.Timedelta(hours=window_hours)
    ts = TransmissionScraper()
    return ts.all_cross_border_flows(start, end)


class TransmissionScraper:

    def __init__(self):
        self.client = EntsoePandasClient(api_key=settings.APP_ENTSOE_API_KEY)

    def all_cross_border_flows(self, start, end):
        dfs = [self.cross_border_flows_from(country_code_from, start, end) for country_code_from in
               country_connections.keys()]
        return pd.concat(dfs, ignore_index=True)

    def cross_border_flows_from(self, country_code_from, start, end):
        country_code_to_list = country_connections[country_code_from]
        dfs = [self.cross_border_flows(country_code_from, country_code_to, start, end) for country_code_to in
               country_code_to_list]
        return pd.concat(dfs, ignore_index=True)

    def cross_border_flows(self, country_code_from, country_code_to, start, end):
        s = self.client.query_crossborder_flows(country_code_from, country_code_to, start=start, end=end)
        s.name = 'capacity'
        s.index.name = 'timestamp'
        s.index = s.index.tz_convert(tz)
        df = s.to_frame()
        df.reset_index(inplace=True)
        df.insert(loc=0, column="country_code_from", value=country_code_from)
        df.insert(loc=1, column="country_code_to", value=country_code_to)
        time.sleep(float(settings.APP_BACKOFF_PERIOD))  # Do not stress the api
        return df
