


#  上海 --  有空值 【】 -- 没有tr-head --  容易出现数组越界
# 江苏  --  有'\r\n\t\t\t\t\t\t\t\t\t\t'
# 浙江 --  有空值 【】
# 湖北  --  有'\r\n\t\t\t\t\t\t\t\t\t\t'
# 宁夏  --  有'\r\n\t\t\t\t\t\t\t\t\t\t'
# 青海  --  有'\r\n\t\t\t\t\t\t\t\t\t\t'
#  浙江和上海不分文理科

# 辽宁，重庆， 上海 ，山东， 浙江  ， 江西 ,湖北， 海南 ，， 广东 ，四川，66666666 新疆 需要单独采集


import scrapy
from Gaokao02.items import ScoreProvinceItem

class scoreProvince(scrapy.Spider):
    name = "a2"
    def start_requests(self):
        urls = [
            'http://www.eol.cn/html/g/fsx/index.shtml'
        ]
        for url in urls:
            yield scrapy.Request(url = url, callback=self.parse)

    # 2 处理请求
    def parse(self, response):
        # 1 首先批量获取31个省份 selector
        # provinceList = response.xpath("//div[@class='fsshowli']")[3:31] 去掉上海
        provinceList = response.xpath("//div[@class='fsshowli']")[23:31]
        # 依次遍历每个省份
        for provinceItem in provinceList:
            # 1 拿到各个省份代码
            provincecode = provinceItem.css(".topline .city::text").extract_first()
            # print(provincecode)
            # 2 拿到6个年份 -- 循环 -- 列表 987654 987654 - 只能一个一个年份拿
            # year = provinceItem.css(".sline .year::text").extract()[1: 6]
            # 来遍历i 年份和 i 个 table
            for i in range(0, 6):
                # 拿到每个省的 年份数量
                year = provinceItem.css(".sline .year::text").extract()
                # 每次都打印6， 跟循环无关
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
                category = yeartable.css(".tr-head .td3::text").extract_first()
                if (category is None):
                    category = "综合"
                    print(category)
                # print(category)
                # 批次 -- 数量不一样 -- 每个省每年的批次数量 1 批次 ，2 文， 3 理
                batch = yeartable.css(".tr-cont td:nth-child(1)::text").extract()
                batchNum = yeartable.css(".tr-cont")
                # 对应省每年的批次个数 -- 和循环大 有关
                # print(batchNum.__len__())
                # 拿到了批次对应的年份
                # print(batch)
                # 对应年份和批次 最低分 -- 文科 ::::  2: 文科 ， 3：理科

                # 判断
                lowestscore = yeartable.css(".tr-cont td:nth-child(3)::text").extract()
                if (lowestscore is None):
                    lowestscore = yeartable.css(".tr-cont td:nth-child(2)::text").extract()
                # print(lowestscore)

                # ---------------------- 存储测试 1  ----------------------------------
                scoreProvinceItem = ScoreProvinceItem()
                # 这些是常量
                scoreProvinceItem['type'] = type
                scoreProvinceItem['category'] = category
                scoreProvinceItem['highestscore'] = highestscore
                scoreProvinceItem['provincecode'] = provincecode
                # 这个年份和循环i 无关 - 放在外面
                scoreProvinceItem['year'] = year[i]
                # 两层循环解决
                for k in range(0,batchNum.__len__()):
                    scoreProvinceItem['batch'] = batch[k]   # print(scoreProvinceItem['batchNum'])
                    scoreProvinceItem['lowestscore'] = lowestscore[k]
                    yield scoreProvinceItem

                # ---------------------------   循环22222   -----------------------------

                # 呜呜呜， 开始存储 -- 这里应该循环
                # 首先在年份的大循环里面嵌套两层
                # for j in range(0, 6):       # 循环依次一年
                #     scoreProvinceItem = ScoreProvinceItem()
                #     # 这些是常量
                #     scoreProvinceItem['type'] = type
                #     scoreProvinceItem['category'] = category
                #     scoreProvinceItem['highestscore'] = highestscore
                #     scoreProvinceItem['provincecode'] = provincecode
                #     # 两层循环解决
                #     for k in range(0,batchNum.__len__()):
                #         scoreProvinceItem['year'] = year[i]
                #         scoreProvinceItem['batch'] = batch[k]   # print(scoreProvinceItem['batchNum'])
                #         scoreProvinceItem['lowestscore'] = lowestscore[k]
                #         yield scoreProvinceItem



