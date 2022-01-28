from django.apps import AppConfig
import os
from entsoefacade import settings
from .helpers import persist
from .scrapers import scrape_all


class ScraperConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'entsoefacade.scraper'

    def ready(self):
        if os.environ.get('RUN_MAIN'):
            if settings.APP_SCRAPER_RUN_ON_START:
                print("SCRAPING...")
                df = scrape_all(int(settings.APP_SCRAPER_WINDOW_HOURS_ON_FIRST_RUN))
                print("SCRAPING FINISHED!")
                persist(df)
                print("DATA PERSISTED!")
