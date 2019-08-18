# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MusicStoreItem(scrapy.Item):
    brand = scrapy.Field()
    name = scrapy.Field()
    global_rating = scrapy.Field()
    rating = scrapy.Field()
    votes = scrapy.Field()
    price = scrapy.Field()
    image = scrapy.Field()
    description = scrapy.Field()
    url = scrapy.Field()
