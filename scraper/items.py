# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from ..main.models import Job


class MainScraperItem(DjangoItem):
    django_model = Job
