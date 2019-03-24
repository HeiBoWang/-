
import scrapy
from Gaokao02.items import ScoreProvinceItem

class scoreProvince(scrapy.Spider):
    name = "all"
    def start_requests(self):
        urls = [
            'http://www.eol.cn/html/g/fsx/index.shtml'
        ]
        for url in urls:
            yield scrapy.Request(url = url, callback=self.parse)

    # 2 处理请求
    def parse(self, response):
        # 1 首先批量获取34个省份 selector
        provinceList = response.xpath("//div[@class='fsshowli']")

        # 依次遍历每个省份
        for provinceItem in provinceList:
            # 1 拿到各个省份代码
            provincecode = provinceItem.css(".topline .city::text").extract_first()
            print(provincecode)
            # 2 拿到6个年份 -- 循环 -- 列表 987654 987654 - 只能一个一个年份拿
            # year = provinceItem.css(".sline .year::text").extract()[1: 6]
            # 来遍历i 年份和 i 个 table
            for i in range(0, 6):
                # 拿到每个省的 年份数量
                year = provinceItem.css(".sline .year::text").extract()
                # print(year)
                # print(year.__len__())
                # 拿到 每个省份每年的数据表格 -- 拿到6个selector, 除去 19年的
                # yeartable = provinceItem.css(".tline > div")[1:6] -- 这里的限制非常重要
                yeartable = provinceItem.css(".tline > div")[i]
                # print(yeartable)
                # print(yeartable.__len__())

                # 高考
                type = "高考"
                highestscore = "0"

                # 文理科 -- 各个省的年份数量相等 - 可遍历 -- 2 文科 ，3 理科
                category = yeartable.css(".tr-head .td2::text").extract_first()
                print(category)
                # 批次 -- 数量不一样 -- 每个省每年的批次数量 1 批次 ，2 文， 3 理
                batchNum = yeartable.css(".tr-cont td:nth-child(1)::text").extract()
                # print(batchNum.__len__())
                # 拿到了批次对应的年份
                print(batchNum)
                # 对应年份和批次 最低分 -- 文科 ::::  2: 文科 ， 3：理科
                lowestscore = yeartable.css(".tr-cont td:nth-child(2)::text").extract()
                print(lowestscore)

                # 呜呜呜， 开始存储 -- 这里应该循环
                # 首先在年份的大循环里面嵌套两层
                for j in range(0, 6):       # 循环依次一年
                    scoreProvinceItem = ScoreProvinceItem()
                    # 这些是常量
                    scoreProvinceItem['type'] = type
                    scoreProvinceItem['category'] = category
                    scoreProvinceItem['highestscore'] = highestscore
                    scoreProvinceItem['provincecode'] = provincecode
                    # 两层循环解决
                    for k in range(0,batchNum.__len__()):
                        scoreProvinceItem['year'] = year[i]
                        scoreProvinceItem['batch'] = batchNum[k]   # print(scoreProvinceItem['batchNum'])
                        scoreProvinceItem['lowestscore'] = lowestscore[k]
                        yield scoreProvinceItem



