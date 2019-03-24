# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymysql
from Gaokao02 import settings

class ScoreProvincePipeline(object):
    # 首先初始化数据库
    def __init__(self):
        self.connect = pymysql.connect( # 打开数据库链接
            host = settings.HOST,
            port = 3306,
            db = settings.DBNAME,
            user = settings.USER,
            passwd = settings.PASSWD,
            charset='utf8',
            use_unicode=True
        )
        # 获取数据库操作的句柄
        self.cursor = self.connect.cursor()

    def process_item(self, scoreProvinceItem, spider):
        try:
            sql = " INSERT INTO `score_province` (`provincecode`,`year`,`type`,`category` ,`batch`,`highestscore`,`lowestscore`) " \
                "values ('%s','%s','%s','%s','%s','%s','%s')" % \
                  (scoreProvinceItem['provincecode'], scoreProvinceItem['year'], scoreProvinceItem['type'], scoreProvinceItem['category'], scoreProvinceItem['batch'], scoreProvinceItem['highestscore'],scoreProvinceItem['lowestscore'],)

            # sql = "insert into `score_province_01` (`provincename`,`year`,`type`,`batch`,`category` ,`scoreline`) " \
            #       "values ('%s','%s','%s','%s','%s','%s')" % \
            #       ( item['provincename'], item['year'], item['type'], item['batch'], item['category'], item['scoreline'],)
            print(sql)


            # 书写sql 语句 -- 执行
            self.cursor.execute(sql)
            self.connect.commit()
            # 关闭数据库链接
        except Exception as error:
            print(error)
        return scoreProvinceItem

    def close_spider(self,spider):
        self.cursor.close()
        self.connect.close()


 # 省份录取分数线的
class scoreProvince01Pipeline(object):
    # 初始化数据库操作
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host="47.93.225.12",
            port=3306,
            db="school-matriculate",
            user="zkrt",
            passwd="zkrtFCZ812",
            charset='utf8',
            use_unicode=True)

        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()
    #  执行SQL语句
    def process_item(self, item, spider):
        try:
            sql = "insert into `score_province_01` (`provincename`,`year`,`type`,`batch`,`category` ,`scoreline`) " \
              "values ('%s','%s','%s','%s','%s','%s')" % \
              (item['provincename'], item['year'], item['type'],item['batch'], item['category'], item['scoreline'],)
            self.cursor.execute(sql)
            # 执行SQL语句
            self.connect.commit()
            # 在这里进行关闭链接试试
            self.cursor.close()
            self.connect.close()
        except Exception as error:
            #  打印错误日志
            print(error)
        return item
    # def close_spider(self,spider):
    #     self.cursor.close()
    #     self.connect.close()


#  名言网站数据库操作都在这个管道里面操作
class mingyanPipeline(object):

    # 初始化数据库操作
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host="47.93.225.12",
            port=3306,
            db="scrapytest",
            user="zkrt",
            passwd="zkrtFCZ812",
            charset='utf8',
            use_unicode=True)

        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()

    #  执行SQL语句
    def process_item(self, item, spider):
        print("succeed")

        try:
            sql = "insert into `mingyan` (`text`,`author`,`tags`) " \
              "values ('%s','%s','%s')" % \
              (item['text'], item['author'], item['tags'])

            self.cursor.execute(sql)
            # 执行SQL语句
            self.connect.commit()
        except Exception as error:
            #  打印错误日志
            print(error)
        return item
    def close_spider(self,spider):
        self.cursor.close()
        self.connect.close()
