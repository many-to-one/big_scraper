# from django.shortcuts import render
# from django.http import HttpResponse

# from .tasks import run_spider
# from django.core.management import call_command
# import schedule
# import time

# # Create your views here.
# # celery -A scr_app worker -l info
# # celery -A scr_app beat -l info

# def getScraper(request):

#     # print('result crawl called')
#     # call_command('crawl')

#     return HttpResponse('Scraping started!')


# main/views.py

from django.http import HttpResponse
from django.views import View
from threading import Thread
import time
import schedule
from django.core.management import call_command
# from .tasks import run_spider
from celery.result import AsyncResult


from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.settings import Settings
from scraper import settings as my_settings
from scraper.spiders.touch_spider import MainSpider

class StartScraperView(View):

    # def start_scraper(self):

    #     # res = run_spider.apply(args=(2, 2)).get()
    #     res = run_spider.apply().get()
    #     return res

    def get(self, request, *args, **kwargs):

        # result_value= self.start_scraper()
        # call_command('crawl')
        # run_spider.apply().get()

        return HttpResponse(f"Scraper completed. Result ")
