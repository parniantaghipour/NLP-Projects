# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
# from scrapy import signals
# from scrapy.exporters import CsvItemExporter
#
# from imagecrawler import settings
#
#
# class ImagecrawlerPipeline:
#     # def process_item(self, item, spider):
#     #     return item
#     def __init__(self):
#         self.exporters = {}
#
#     @classmethod
#     def from_crawler(cls, HouzzSpider):
#         pipeline = cls()
#         HouzzSpider.signals.connect(pipeline.spider_opened, signals.spider_opened)
#         HouzzSpider.signals.connect(pipeline.spider_closed, signals.spider_closed)
#         return pipeline
#
#     def spider_opened(self, HouzzSpider):
#         ...
#         self.exporters = {}
#         for category in settings.CATEGORIES:
#             file = open('./output/%s.csv' % category, 'w+b')
#             exporter = CsvItemExporter(file)
#             exporter.start_exporting()
#             self.exporters[category] = exporter
#             print("________________________________________________________________________________________________")
#     def spider_closed(self, HouzzSpider):
#         for exporter in self.exporters.itervalues():
#             exporter.finish_exporting()
#
#     def process_item(self, item, HouzzSpider):
#         self.exporters[item['category']].export_item(item)
#         return item
