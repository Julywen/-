# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class Comment(scrapy.Item):
    id = scrapy.Field
    score = scrapy.Field
    nickname = scrapy.Field
    userClientShow = scrapy.Field
    content = scrapy.Field
    referenceName = scrapy.Field
    pass
