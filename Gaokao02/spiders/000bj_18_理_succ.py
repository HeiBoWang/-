
# 'provincecode','year','type','category' ,'batch','highestscore','lowestscore'
import scrapy
from Gaokao02.items import ScoreProvinceItem
import numpy as np
class scoreProvince(scrapy.Spider):
    name = "li"
    # 1 发起请求
    def start_requests(self):
        urls = [
            'http://www.eol.cn/html/g/fsx/index.shtml'
        ]
        for url in urls:
            yield scrapy.Request(url = url, callback=self.parse)

    # 2 处理请求
    def parse(self, response):
        # 1 首先批量获取34个省份
        # provinceList = response.xpath("//div[@class='fsshowli']")[0]
        #  北京省数据测试
        province = response.xpath("//div[@class='fsshowli']")[0]

        # 然后循环拿到每个省份
        # for province in provinceList:
        #     # 拿到省份编码 -- 当前循环下面 进行循环
        #     # 不全拿所有的省份 - 只拿一个北京测试
        #     province = province[0]
        #     print(province)
# ------------- 不循环之后 ----------------------

        provinceCode = province.css(".topline .city::text").extract_first()
        # print(provinceCode)
        # 取所有的年份的数据，一年一年爬取
        year = province.css(".sline .year::text").extract()
        print(year)
        # print(year * 6)

        # 学位类型
        type = "高考"
        # 理科
        category = province.css(".tline .td3::text").extract()[0]
        # print(category)
        # print(category.__len__())
        # 所有18年的 批次 都搞出来 -- 批次循环有问题
        # 文理科一样 -- 不变
        batch = province.css(".tline > div .tr-cont > td:nth-child(1)::text").extract()
        # print(batch)
        # 最高分没有 - 设置为0 -- 不变
        highestscore = "0"
        # 最低分 -- 理科 -- 文理不一样 -- 变化
        lowestscore = province.css(".tline > div .tr-cont > td:nth-child(3)::text").extract()
        # print(lowestscore)
        # print(lowestscore.__len__())
# ---------------------  北京省  18 年 文科 所有批次的最低录取分数线爬取完毕 ----------------------------
        # 开始存储

        for i in range(0, lowestscore.__len__()):
            scoreProvinceItem = ScoreProvinceItem()

            scoreProvinceItem['provincecode'] = provinceCode
            scoreProvinceItem['year'] = year[i]
            scoreProvinceItem['type'] = type
            scoreProvinceItem['category'] = category
            scoreProvinceItem['batch'] = batch[i]
            # 33 个 数据
            scoreProvinceItem['highestscore'] = highestscore
            scoreProvinceItem['lowestscore'] = lowestscore[i]
            yield scoreProvinceItem



