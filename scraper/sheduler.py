import schedule
import time
from django.core.management import call_command

def do_scrap():
    call_command('crawl')
    print("Scraping job executed")

# Schedule the task to run every 10 minutes
# schedule.every(1).minutes.do(do_scrap)

# # Keep the script running to execute the scheduled tasks
# while True:
#     schedule.run_pending()
#     time.sleep(1)