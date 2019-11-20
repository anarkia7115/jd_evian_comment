# jd_evian_comment

## Crawler
Most codes are auto generated. If you want to crawl using this project, run `scrapy crawl products`.  
The following codes contains the project-specific work:
* jd_evian_comment/evian_crawler/evian_crawler/spiders/products.py
* jd_evian_comment/evian_crawler/evian_crawler/pipelines.py 
* jd_evian_comment/evian_crawler/connector.py
* jd_evian_comment/evian_crawler/url_utils.py

Configurations can be done in `jd_evian_comment/evian_crawler/evian_crawler/settings.py`
* ES_URI - url of elasticsearch entrypoint
* ES_INDEX - name of elasticsearch index
* ES_BATCH_SIZE - batch_size for bulk insertion
* PAGE_MIN - minimum page number of jd product comments
* PAGE_MAX - maximum page number of jd product comments

## RESTful API
Provided by elasticsearch
```shell
curl -u artefact:facteart \
	-H 'Content-Type: application/json' \
	-X GET 'https://portal4883-9.tangible-elastic-search-53.2839618036.composedb.com:34842/jd_comments/_search/?pretty' \
	-d'
	  {
             "_source": "*", 
	     "query": {
	       "match": {
	         "content": "颜值"
               }
	     }
	  }'
```
* Use \_source to limit output fields. For example, `"_source": "content"` outputs field `content` only.
* Use **content** to search keywords.
