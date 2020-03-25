# -*- coding: utf-8 -*-
import scrapy


class XiaohuaSpider(scrapy.Spider):
    name = 'xiaohua'
    allowed_domains = ['xiaohua.zol.com.cn']
    start_urls = ['http://xiaohua.zol.com.cn/']

    def parse(self, response):
        pass

    def start_requests(self):
        return super().start_requests()
