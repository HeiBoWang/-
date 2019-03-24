
import scrapy

# http://www.eol.cn/html/g/fsx/index.shtml
class test01(scrapy.Spider):

    name = 't1'
    #  1 发起请求的方法
    def start_requests(self):
        urls = [
            'http://www.eol.cn/html/g/fsx/index.shtml'
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse())

    # 2 请求后执行的回调函数
    # def parse(self, response):