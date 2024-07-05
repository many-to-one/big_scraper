# schedule_scraper.py

import schedule
import time
from .spiders import run_spider

# Schedule the spider to run every minute
schedule.every(1).minutes.do(run_spider)

if __name__ == '__main__':
    while True:
        schedule.run_pending()
        time.sleep(1)
