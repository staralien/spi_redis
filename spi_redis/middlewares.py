# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from .settings import USER_AGENT
import random


class SpiRedisDownloaderMiddleware:
    def process_request(self, request, spider):
        user_agent = random.choice(USER_AGENT)
        request.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
        request.headers['referer'] = 'https://book.jd.com/'


