# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from connector import Elasticsearch


"""
EvianCrawlerPipeline - 
    Auto-generated, not used.
"""
class EvianCrawlerPipeline(object):
    def process_item(self, item, spider):
        return item


"""
JsonWriterPipeline - 
    Write json into jsonLines as local file. 
"""
class JsonWriterPipeline(object):

    def open_spider(self, spider):
        self.file = open('items.jl', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(item) + "\n"
        self.file.write(line)
        return item


"""
ElasticSearchPipeline - 
    Write items into ES.
"""
class ElasticSearchPipeline(object):
    def __init__(self, es_uri, es_index, es_batch_size):
        self.es_batch_size = es_batch_size
        self.items = []

        self.es_uri = es_uri
        self.es_index = es_index

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            es_uri=crawler.settings.get("ES_URI"),
            es_index=crawler.settings.get("ES_INDEX"),
            es_batch_size=crawler.settings.get("ES_BATCH_SIZE")
        )

    def open_spider(self, spider):
        self.es = Elasticsearch(
            self.es_uri, 
            self.es_index
        )


    def process_item(self, item, spider):
        self.items.append(item)

        # trigger batch insert
        if len(self.items) >= self.es_batch_size:
            self.es.bulk_insert_into_es(self.items, spider)
            self.items = []

        return item
