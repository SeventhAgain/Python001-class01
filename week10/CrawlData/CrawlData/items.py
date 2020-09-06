# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawldataItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    price = scrapy.Field()
    zhi = scrapy.Field()
    buzhi = scrapy.Field()
    collectcount = scrapy.Field()
    commentcount = scrapy.Field()
    platform = scrapy.Field()
    publish = scrapy.Field()
    comments = scrapy.Field()
