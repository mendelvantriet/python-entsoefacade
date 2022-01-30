import os

from django.apps import AppConfig

from entsoefacade import settings
from .helpers import persist
from .helpers import schedule_at_fixed_rate
from .scrapers import scrape_all


class ScraperConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'entsoefacade.scraper'

    def ready(self):
        if os.environ.get('RUN_MAIN'):
            if settings.APP_SCRAPER_RUN_ON_START == 'True':
                self.scrape(int(settings.APP_SCRAPER_WINDOW_HOURS_ON_FIRST_RUN))

            schedule_at_fixed_rate(int(settings.APP_SCRAPER_INTERVAL_MINUTES), self.scrape,
                                   args=[int(settings.APP_SCRAPER_WINDOW_HOURS)],
                                   delay=int(settings.APP_SCRAPER_INTERVAL_MINUTES))

    def scrape(self, window_hours):
        print("SCRAPING...")
        df = scrape_all(window_hours)
        print("SCRAPING FINISHED!")
        persist(df)
        print("DATA PERSISTED!")
