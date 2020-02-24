# -*- coding: utf-8 -*-
import scrapy


class Day026HwSpider(scrapy.Spider):
    name = 'Day026_HW'
    allowed_domains = ['https://www.ptt.cc']
    start_urls = ['https://www.ptt.cc/bbs/Gossiping/M.1582539066.A.C00.html']

    def parse(self, response):
        pass
