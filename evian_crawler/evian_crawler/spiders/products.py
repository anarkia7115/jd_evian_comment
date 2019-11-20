# -*- coding: utf-8 -*-
import scrapy
import json
import pprint as pp
from url_utils import *


class ItemsSpider(scrapy.Spider):
    name = 'products'
    allowed_domains = ['item.jd.com']

    def start_requests(self):
        min_page_num = self.settings.get("PAGE_MIN")
        max_page_num = self.settings.get("PAGE_MAX")

        for page_num in range(min_page_num, max_page_num):
            # generate url using params
            url = generate_comment_request_url(page_num=page_num)

            # create request
            request = scrapy.Request(
                url=url, 
                callback=self.parse, 
                headers=self.get_headers(), 
                cb_kwargs=dict(page_num=page_num))
            self.log("Request headers: {}".format(request.headers))
            yield request

    def get_headers(self):
        headers = {
            "referer": "https://item.jd.com/1384071.html"
        }
        return headers

    def parse(self, response, page_num):
        # get json string
        comments_json = response.body.decode('gbk')
        self.log("size of comments json: {}".format(len(comments_json)))

        # load json as dict
        comments = json.loads(comments_json)
        return comments["comments"]

    def print_comments(self, comments, page_num):
        self.log("printing comments: ")
        for comment in comments["comments"]:
            self.log("{}: {}".format(page_num, comment["content"]))
