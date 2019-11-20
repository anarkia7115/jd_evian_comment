import json
from elasticsearch import Elasticsearch as ES
from elasticsearch import helpers
# from elasticsearch import Elasticsearch, helpers

class Elasticsearch(object):
    def __init__(self, es_uri, es_index):
        self.es_uri = es_uri
        self.es_index = es_index
        self.es = ES([self.es_uri])

    def bulk_insert_into_es(self, items, logger):
        actions = []
        for item in items:
            action = {
                "_index": self.es_index,
                "_id": item["id"],
                "_type": "jd_comment",
                "_source": item
                }
            actions.append(action)

        logger.log("bulk inserting")
        helpers.bulk(self.es, actions)
