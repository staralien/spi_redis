# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiRedisItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    shop_name = scrapy.Field()
    comment_count = scrapy.Field()
    price = scrapy.Field()
    link = scrapy.Field()
    CategoryName = scrapy.Field()

