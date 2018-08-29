# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class SpiderProject4Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field(),
    author = scrapy.Field(),
    price = scrapy.Field(),
    aedition_year = scrapy.Field(),
    publisher = scrapy.Field(),
    ratings = scrapy.Field()