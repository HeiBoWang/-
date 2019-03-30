
import requests
import json
from fake_useragent import UserAgent
from elasticsearch import Elasticsearch
es = Elasticsearch(['127.0.0.1'])
# ua = UserAgent()
# # header = str(ua.random)
# header = ua.random

es = Elasticsearch(['127.0.0.1'])

# 获取数据方法
def getData():
    ua = UserAgent()
    headers = {'User-Agent': ua.random}
    url = 'https://gongyi-api.shuidichou.com/api/pf/v1/fundraising/fundraising-list?limit=300'
    dataText = requests.post(url, headers = headers).content
    # str
    dataJson = json.loads(dataText)
    # print(type(dataJson))
    # 转化为字典 - 可以遍历
    shuidiList = dataJson['data']['data']

    # 遍历拿到infonum - 一个一个存储
    for mid, value in enumerate(shuidiList):
        ua = UserAgent()
        headers = {'User-Agent': ua.random}

        detailUrl = 'https://gongyi-api.shuidichou.com/api/pf/v1/fundraising/detail?infoNum=' + value['infoNum']
        dataText = requests.post(detailUrl, headers = headers).content
        dataJson = json.loads(dataText)
        shuidiList = dataJson['data']
        # print(shuidiList)
        # # 解析完毕 -- 存储
        ES_SAVE = es.index(
            index = 'db_shuidi4',
            doc_type = 'doc',
            id = mid ,
            body = shuidiList
        )
        print(ES_SAVE)

getData()

# headers = {
# 'Host': 'gongyi-api.shuidichou.com',
# 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
# 'Referer': 'https://www.shuidichou.com/gongyi/' ,
# 'Content-Type': 'application/x-www-form-urlencoded'
#     }