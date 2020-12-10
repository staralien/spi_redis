import scrapy
from spi_redis.items import SpiRedisItem
import json


class JdBookSpider(scrapy.Spider):
    name = 'jd_book'
    allowed_domains = ['jd.com']
    start_urls = ['https://pjapi.jd.com/book/sort?source=bookSort']

    def parse(self, response):
        json_dict = json.loads(response.text)
        base_title = json_dict['data']
        for title in base_title:
            sonList = title['sonList']
            first = int(title['fatherCategoryId'])
            for s in sonList:
                item = SpiRedisItem()
                second = int(s['fatherCategoryId'])
                third = int(s['categoryId'])
                item['CategoryName'] = s['categoryName']
                item['link'] = f'https://list.jd.com/list.html?cat={first},{second},{third}'
                yield scrapy.Request(
                    url=item['link'],
                    callback=self.parse_book_list,
                    meta=item
                )

    def parse_book_list(self, response):
        r = response.text
        print(type(response))
        item = response.meta
        book_sku_list = response.xpath('//*[@id="J_goodsList"]/ul/li')
        for book in book_sku_list:
            sku_id = book.xpath('./@data-sku').extract_first()
            url2 = f'https://p.3.cn/prices/mgets?skuIds=J_{sku_id}'
            item['name'] = book.xpath('./div/div[3]/a/em/text()').extract_first()
            item['shop_name'] = book.xpath('./div/div[6]/a/@title').extract_first()
            item['link'] = book.xpath('./div/div[3]/a/@href').extract_first().replace('//', '')
            yield scrapy.Request(
                url=url2,
                callback=self.parse_book_price,
                meta=item,

            )


    def parse_book_price(self, response):
        print(response.text)
        pass
