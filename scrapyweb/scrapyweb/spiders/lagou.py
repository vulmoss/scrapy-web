# -*- coding: utf-8 -*-
import scrapy


class LagouSpider(scrapy.Spider):
    name = 'lagou'
    allowed_domains = ['https://www.lagou.com']
    start_urls = ['http://https://www.lagou.com/']

    def parse(self, response):
        for course in response.css('div.class=menu_box'):
            yield({
                'name': course.xpath('.//h2/text()').extract()
                })
