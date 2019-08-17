# -*- coding: utf-8 -*-
from scrapy import Spider, Request


class MusicSpider(Spider):
    name = 'music'
    allowed_domains = ['musicstore.com']

    def __init__(self, instrument=''):
        self.instrument = instrument
        self.start_urls = [
            f'https://www.musicstore.com/en_OE/EUR/search;pgid=NwXg2xauQc5SRpGRd7yx_mNm0000Q2bzyey0?SearchTerm={self.instrument}&SearchParameter=%26%40QueryTerm%3Dbass%26FollowSearch%3D9753']

    def parse(self, response):
        items = response.xpath('//div[contains(@class, "image-box")]/a[@class="js-tracking"]/@href').extract()
        for item in items:
            yield Request(item, callback=self.parse_instrument)

        next_page_url = response.xpath('//a[@title="to next page"]/@href').extract_first().strip()
        yield Request(next_page_url, callback=self.parse)

    def parse_instrument(self, response):
        print(response.url)