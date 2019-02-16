import scrapy
import re
import json
"""
定义网络爬虫类
"""
class ItcastSpider(scrapy.Spider):
    # 每个爬虫必须要一个名字
    name = "test3"
    heads = {
        ":authority": "sclub.jd.com",
        ":method": "GET",
        ":path": "/comment/productPageComments.action?callback=fetchJSON_comment98vv165&productId=100002997682&score=0&sortType=5&page=1&pageSize=10&isShadowSku=0&rid=0&fold=1",
        ":scheme": "https",
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "cookie": "__jdu=1078358146; PCSYCityID=14; shshshfpa=b57a7fc5-b26f-1c33-3f1b-f03ec29b04fa-1550210696; shshshfpb=knGtWAljz4tAP51JweZ7QYA%3D%3D; user-key=90715c21-3409-4505-bfa3-85692be51198; cn=0; unpl=V2_ZzNtbUNVQRx0C0VccxEMV2IAR1RKAkNAdw4VUH9NCFY3CxYIclRCFX0UR1dnGVgUZwoZXktcRhBFCEdkeBBVAWMDE1VGZxBFLV0CFSNGF1wjU00zQwBBQHcJFF0uSgwDYgcaDhFTQEJ2XBVQL0oMDDdRFAhyZ0AVRQhHZHsYWgxlBxtdR1BzJXI4dmRzGV0FZwsiXHJWc1chVEJRfBhVAyoDE1tLVUccdQ1BZHopXw%3d%3d; __jdc=122270672; __jdv=122270672|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_0338022999ac42d89d1d37b55eeba95d|1550226726893; ipLoc-djd=1-72-2799-0; 3AB9D23F7A4B3C9B=2JMDAOF25G6HITUDVOPKBIT354KZP6NYTDNJ567PA5GSHTYZ3MRXH5PS76Q7SZPUHWEGYGX3JSNBD3T5222R5IM3HE; mt_xid=V2_52007VwMTVFRaVlMfTB5sBmBUQVcJWlpGT08bCRliBRJbQQhVWExVHA9WMwFAUF0KVl0eeRpdBW8fE1FBWFZLH0ESWARsAhZiX2hSah1NHlsMZgsQUG1YV1wY; shshshfp=2675716b34d65abfe500d2c1b8a0e739; shshshsID=181b93c708c8d18d8e195b7ffacdcee1_1_1550231409058; __jda=122270672.1078358146.1550210694.1550229110.1550231409.4; __jdb=122270672.1.1078358146|4.1550231409; _gcl_au=1.1.474423321.1550231409; JSESSIONID=8CF35642BADDF200E55E98DAE0CF2EA1.s1",
        "referer: https":"//item.jd.com/100002997682.html?jd_pop=26fb4e39-a73d-4718-a63b-4bbe3c31c560&abt=0",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36"
    }
    url = "https://item.jd.com/100002997682.html"


    """
    注：
    入口方法，当爬虫启动之后会先执行这个方法
    url :请求的url
    callback: 回调函数
    headers:请求头
    re是正则表达式    [(](.*)[)]    匹配() 中间的内容
    """
    def start_requests(self):
        yield scrapy.Request(url=self.url, headers=self.heads, callback=self.parse)
    def parse(self, response):
        print(response.text)
        p = re.compile(r'[(](.*)[)]', re.S)  # 贪婪匹配
        r= re.findall(p, response.text)  # 匹配之后返回一个数组
        jsonstr=r[0]