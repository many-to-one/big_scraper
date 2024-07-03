# my_django_project/scraper/tasks.py
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.management import call_command

@shared_task
def run_scrapy_crawl():
    call_command('crawl')  # This will call your custom management command to run the Scrapy spider
