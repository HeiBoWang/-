# -*- coding: UTF-8 -*-
import scrapy
import pymysql
#  导入实体类
from Gaokao02.items import scoreProvince01Item

class scoreSpider(scrapy.Spider):
    # 爬虫名称- 省份录取成绩
    name = 'sp'
    # 此方法爬取页面
    def start_requests(self):
        # 爬取的url
        urls = [
            'http://www.eol.cn/html/g/fsx/index.shtml',
        ]
        for url in urls:
            # 爬取的页面交给回调函数处理
            yield scrapy.Request(url=url, callback=self.parse)

    # 回调函数实现
    def parse(self, response):
        # 只有一个，那就用不到循环， 依次提取，保存到数据库
        provinceli = response.css("div.fsshowli")[0]

        # 1 先定义数据库实体类实例 ==========
        item = scoreProvince01Item()

        # 2 数据解析 ==========

        # 省份名称, 多个省份循环-- 不会有数组的符号， 取第几个值
        # //*[@id="bj"]/div[1]/div.text()
        provincename = provinceli.xpath("//*[@id='bj']/div[1]/div//text()").extract_first()
        # 去掉19年的 - 多个年份循环遍历
        year = provinceli.css("div.year::text").extract()[1]
        # 考试的分类， 中考还是高考
        type = "高考"
        # 一二本的批次 - 多个批次，取第一个
        # 这是历史性的一刻**************************北京18年一批文科录取分数
        batch = provinceli.css("tr.tr-cont:nth-child(2) td:nth-child(1)::text").extract()[1]
        # 文理科的分类 - 两个循环 -- 只取文科
        category = provinceli.css("tr.tr-head:nth-child(1) td.td2::text").extract()[0]
        # #bj > div.tline > div:nth-child(2) > table
        # 又是历史性一刻， 文科分数
        scoreline = provinceli.css("div.tline > div:nth-child(2) > table tr.tr-cont td:nth-child(2)::text").extract()[0]

        # 3 到此，数据解析完毕， 存入数据库==========

        item['provincename'] = provincename
        item['year'] = year
        item['type'] = type
        item['batch'] = batch
        item['category'] = category
        item['scoreline'] = scoreline

        #  4 最后返回
        yield item




