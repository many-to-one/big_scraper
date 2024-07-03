from django.shortcuts import render
from django.http import HttpResponse

from .tasks import run_spider

# Create your views here.
# celery -A scr_app worker -l info
# celery -A scr_app beat -l info

def getScraper(self, request):
    # Call the Celery task to start the scraping process
    run_spider.delay()
    # Return a response indicating that the scraping has started
    return HttpResponse('Scraping started!')