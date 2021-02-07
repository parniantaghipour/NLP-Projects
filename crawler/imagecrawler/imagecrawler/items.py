# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ImagecrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    image1 = scrapy.Field()
    image2 = scrapy.Field()
    summery = scrapy.Field()
    pass
