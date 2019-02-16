import scrapy
"""
定义网络爬虫类
"""
class ItcastSpider(scrapy.Spider):
    # 每个爬虫必须要一个名字
    name = "test2"
    url = "https://www.jd.com/"
