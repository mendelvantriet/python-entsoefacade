from django.apps import AppConfig
from entsoefacade.scraper.scrapers import scrape_all
from entsoefacade import settings


class ScraperConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'entsoefacade.scraper'

    def ready(self):
        df = scrape_all(int(settings.APP_SCRAPER_WINDOW_HOURS_ON_FIRST_RUN))
