import logging
logger = logging.getLogger('file')
from celery import shared_task
from django.core.management import call_command

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scraper.spiders.touch_spider import MainSpider

from twisted.internet import reactor
from twisted.internet.task import deferLater
from scrapy.crawler import CrawlerRunner


@shared_task
def health_check():
    logger.info('Task Runner is healthy 🍎')

# @app.task
@shared_task
def run_spider():

    if reactor.running:
        logger.warning('Reactor is already running. Stopping it now...')



    # logger.info('Spiders are crawling 🕸️️')

    try:
        call_command('crawl')
        # logger.info('Spiders have finished crawling 🕸️️')
    except Exception as e:
        logger.error(f'An error occurred during crawling: {e}')


    return True


