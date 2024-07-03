# from __future__ import absolute_import, unicode_literals
# from celery import shared_task
# from django.core.management import call_command

# @shared_task
# def run_scrapy_crawl():
#     call_command('crawl')  # This will call your custom management command to run the Scrapy spider

from celery import shared_task
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from scraper.spiders.touch_spider import MainSpider

@shared_task
def run_spider():
    process = CrawlerProcess(get_project_settings())
    process.crawl(MainSpider)
    process.start()