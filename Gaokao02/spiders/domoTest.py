


#  上海 --  有空值 【】 -- 没有tr-head --  容易出现数组越界
# 江苏  --  有'\r\n\t\t\t\t\t\t\t\t\t\t'
# 浙江 --  有空值 【】
# 湖北  --  有'\r\n\t\t\t\t\t\t\t\t\t\t'
# 宁夏  --  有'\r\n\t\t\t\t\t\t\t\t\t\t'
# 青海  --  有'\r\n\t\t\t\t\t\t\t\t\t\t'
#  浙江和上海不分文理科

import scrapy
from Gaokao02.items import ScoreProvinceItem

class scoreProvince(scrapy.Spider):
    name = "all2222"
    def start_requests(self):
        urls = [
            'http://www.eol.cn/html/g/fsx/index.shtml'
        ]
        for url in urls:
            yield scrapy.Request(url = url, callback=self.parse)

    # 2 处理请求
    def parse(self, response):
        # zj > div:nth-child(3) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2)
        testnone = response.css("#zj > div:nth-child(3) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(3)::text").extract()
        test2 = response.css("#ln > div:nth-child(3) > div:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(5) > td:nth-child(2)::text").extract()
        print(test2)



