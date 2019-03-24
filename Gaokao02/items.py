# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#   定义数据库实体对象
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

#  正式表格 -- 省份批次录取分数线
class ScoreProvinceItem(scrapy.Item):
    #把要存储的字段都在这里列出
    # 1. score_province 数据库
    # name = scrapy.Field()
    provincecode = scrapy.Field()
    year = scrapy.Field()
    type = scrapy.Field()
    category = scrapy.Field()
    batch = scrapy.Field()
    highestscore = scrapy.Field()
    lowestscore = scrapy.Field()
    # 然后再爬虫文件里面先去导入items里面声明字段的类
    # 接着创建item对象，写入值，最后别忘了把item给yield出去
    pass

# 名言测试数据库表
class mingyanItem(scrapy.Item):
    text = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()
    pass

# 自己测试 -- 省份录取分数线表
class scoreProvince01Item(scrapy.Item):
    # 省份编号
    provincename = scrapy.Field()
    year = scrapy.Field()
    # 考试的分类， 中考还是高考
    type = scrapy.Field()
    # 一二本的批次
    batch = scrapy.Field()
    # 文理科的分类
    category = scrapy.Field()
    scoreline = scrapy.Field()
    pass