# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from __future__ import unicode_literals
from builtins import str
from builtins import object
import logging
from django.db.utils import IntegrityError
from scrapy.exceptions import DropItem
from scrapy_django_dashboard.models import SchedulerRuntime


class MainScraperPipeline(object):
    def process_item(self, item, spider):
          item.save()
          return item
    
    # def process_item(self, item, spider):
    #     return item

    # def process_item(self, item, spider):
    #     if spider.conf['DO_ACTION']:
    #         try:
    #             item['news_website'] = spider.ref_object

    #             checker_rt = SchedulerRuntime(runtime_type='C')
    #             checker_rt.save()
    #             item['checker_runtime'] = checker_rt

    #             item.save()
    #             spider.action_successful = True
    #             spider.logger.info("{cs}Item {id} saved to Django DB.{ce}".format(
    #                 id=item._id_str,
    #                 cs=spider.bcolors['OK'],
    #                 ce=spider.bcolors['ENDC']))

    #         except IntegrityError as e:
    #             spider.logger.error(str(e))
    #             raise DropItem("Missing attribute.")

    #     return item
