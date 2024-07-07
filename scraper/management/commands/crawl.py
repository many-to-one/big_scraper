from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from scraper import settings as my_settings
from scraper.spiders.touch_spider import MainSpider

from scrapy import cmdline


class Command(BaseCommand):
    help = 'Release spider'


    def handle(self, *args, **options):
        crawler_settings = Settings()
        crawler_settings.setmodule(my_settings)

        process = CrawlerProcess(settings=crawler_settings)

        process.crawl(MainSpider)
        process.start()
        if process:
            print(' ***************** PROCESS ***************** ', process)
        else:
            print(' ***************** NO NO NO PROCESS ***************** ')

        # process.stop()

    # def handle(self, *args, **options):
    #     cmdline.execute("scrapy crawl allegro".split())