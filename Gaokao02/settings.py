# -*- coding: utf-8 -*-

# Scrapy settings for Gaokao02 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Gaokao02'

SPIDER_MODULES = ['Gaokao02.spiders']
NEWSPIDER_MODULE = 'Gaokao02.spiders'

# 添加与数据库连接相关的变量
HOST = '47.93.225.12'
DBNAME = 'school-matriculate'
USER = 'zkrt'
PASSWD = 'zkrtFCZ812'
#
ITEM_PIPELINES = {
    # 'Gaokao02.pipelines.mingyanPipeline': 300,
    # 'Gaokao02.pipelines.scoreProvince01Pipeline': 300,
    'Gaokao02.pipelines.ScoreProvincePipeline': 400,
}


# Obey robots.txt rules
# 不然的话会默认遵循robots协议，你将爬取不到任何数据。
ROBOTSTXT_OBEY = False
