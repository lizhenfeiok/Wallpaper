# -*- coding: utf-8 -*-
import scrapy


class MyboatSpider(scrapy.Spider):
    name = 'myboat'
    allowed_domains = ['http://roll.news.sina.com.cn/news/gnxw/gdxw1/index.shtml']
    start_urls = ['http://http://roll.news.sina.com.cn/news/gnxw/gdxw1/index.shtml/']

    def parse(self, response):

        pass
