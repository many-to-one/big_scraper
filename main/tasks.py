# from __future__ import absolute_import, unicode_literals
# from celery import shared_task
# from django.core.management import call_command

# @shared_task
# def run_scrapy_crawl():
#     call_command('crawl')  # This will call your custom management command to run the Scrapy spider

from celery import shared_task
from scr_app.celery import app
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from scraper.spiders.touch_spider import MainSpider
from django.core.management import call_command

import os
import subprocess

@shared_task
def run_spider():
    # print(" task one called and worker is running good")
    # return "success"

    # call_command('crawl')
    print('run_spider called')
    # return True

    # process = CrawlerProcess(get_project_settings())
    # process.crawl(MainSpider)
    # process.start()