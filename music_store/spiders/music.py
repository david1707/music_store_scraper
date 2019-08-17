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
        items = response.xpath(
            '//div[contains(@class, "image-box")]/a[@class="js-tracking"]/@href').extract()
        for item in items:
            yield Request(item, callback=self.parse_instrument)

        next_page_url = response.xpath(
            '//a[@title="to next page"]/@href').extract_first().strip()
        yield Request(next_page_url, callback=self.parse)

    def parse_instrument(self, response):
        brand = response.xpath(
            '//h1/span[@itemprop="brand"]/text()').extract_first()
        name = response.xpath(
            '//h1/span[@itemprop="name"]/text()').extract_first()
        rating = len(response.xpath(
            '//div[@class="headline-box row"]//i[@class="icon icon-star orange"]'))
        rating = 'This produce has not been rated yet' if rating == 0 else f'{rating} out of 5'
        price = response.xpath(
            '//span[@class="final kor-product-sale-price-value"]/text()').extract_first()
        image = response.xpath(
            '//a[@id="js-easyzoom-large-image"]/@href').extract_first().replace('//', 'http://')
        description = ' '.join(response.xpath(
            '//div[@class="contentText"]//text()').extract()).strip()
        url = response.url

        yield {
            'brand': brand,
            'name': name,
            'rating': rating,
            'price': price,
            'image': image,
            'description': description,
            'url': url,
        }
