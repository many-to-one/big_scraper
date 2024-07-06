import logging
logger = logging.getLogger('file')
from celery import shared_task
from django.core.management import call_command


@shared_task
def health_check():
    logger.info('Task Runner is healthy 🍎')

# @app.task
@shared_task
def run_spider():
    # logger.info('Spiders are crawling 🕸️️')

    try:
        call_command('crawl')
        # logger.info('Spiders have finished crawling 🕸️️')
    except Exception as e:
        logger.error(f'An error occurred during crawling: {e}')


    return True