from scrapy_djangoitem import DjangoItem
from api.models import ScraperRealtor

class ScraperItem(DjangoItem):
    django_model = ScraperRealtor
