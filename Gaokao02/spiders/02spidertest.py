
import scrapy
import pymysql
from Gaokao02.items import mingyanItem

class test02(scrapy.Spider):
    name = 'my1'
    def start_requests(self):
        urls=[
            'http://lab.scrapyd.cn/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        #  先测试只有一个名言的
        # 一定要加div.........
        # ！！！！！！！！###  这个class类名一定不要加空格
        # !!!!!!解析之前和之后的差别巨大.extract()

        mingyan = response.css('div.quote')
        print(mingyan)
        for v in mingyan:
            item = mingyanItem()

            text = v.css('.text::text').extract_first()
            author = v.css('.author::text').extract_first()
            # 数组
            tags = v.css('.tags .tag::text').extract()
            tags = tags[0] + tags[1]

            item['text'] = text
            item['author'] = author
            # 数组
            item['tags'] = tags
            yield item

