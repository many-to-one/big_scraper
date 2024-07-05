# from __future__ import absolute_import, unicode_literals
# from celery import shared_task
# from django.core.management import call_command

# @shared_task
# def run_scrapy_crawl():
#     call_command('crawl')  # This will call your custom management command to run the Scrapy spider
import logging
logger = logging.getLogger('file')
from celery import shared_task
from scr_app.celery import app
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.settings import Settings
from scraper import settings as my_settings

from scraper.spiders.touch_spider import MainSpider
from django.core.management import call_command

import os
import subprocess

from billiard import Process
from scrapy import signals as scrapy_signals
from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy import signals

# class UrlCrawlerScript(Process):
#     def __init__(self, spider):
#         Process.__init__(self)
#         crawler_settings = Settings()
#         crawler_settings.setmodule(my_settings)
#         self.crawler = Crawler(
#           spider,
#           settings = crawler_settings
#         )
#         self.crawler.signals.connect(reactor.stop, signal=scrapy_signals.spider_closed)
#         self.spider = spider

#     def run(self):
#         self.crawler.crawl(self.spider)
#         self.crawler.start()
#         reactor.run()


# @shared_task
# def run_spider():
#     spider = MainSpider
#     crawler = UrlCrawlerScript(spider)
#     crawler.start()
#     crawler.join()


# @shared_task
# def run_spider(x, y):

#     # call_command('crawl')
#     # print('run_spider called')
#     return x + y

@shared_task
def health_check():
    logger.info('Task Runner is healthy 🍎')

# @app.task
@shared_task
def run_spider():
    logger.info('Spiders are crawling 🕸️️')
    call_command('crawl')
    logger.info('Spiders just finished crawling 🕸️️')
    # return 'per_task called'