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

class StartScraperView(View):
    # Thread to run the schedule in background
    def start_scraper_thread(self):
        def run_schedule():
            while True:
                schedule.run_pending()
                time.sleep(1)
                
        # Define the task to be scheduled
        def do_scrap():
            # Here you can call your scrapy command or any other long-running task
            print("Running scheduled task...")
            call_command('crawl')  # Uncomment if you want to run the Scrapy spider

        # Schedule the task every 10 minutes
        schedule.every(1).minutes.do(do_scrap)

        # Start the schedule loop in a separate thread
        thread = Thread(target=run_schedule)
        thread.daemon = True  # Daemonize thread to stop when main thread stops
        thread.start()

    def get(self, request, *args, **kwargs):
        # Start the scraper thread if not already started
        self.start_scraper_thread()
        return HttpResponse("Scraper started in background thread.")

