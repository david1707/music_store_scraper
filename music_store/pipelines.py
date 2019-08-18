# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class MusicStorePipeline(object):
    def process_item(self, item, spider):
        item['global_rating'] = 'This product has not been rated yet' if item.get(
            'global_rating') == 0 else f'{item["global_rating"]} out of 5'
            
        item['votes'] = 'This product has not been voted yet.' if len(
            item.get('votes')) == 0 else list(zip(item['votes'][::2], item['votes'][1::2]))

        if len(item.get('rating')) == 0:
            item['rating'] = 'This product has not been voted yet.'

        return item
