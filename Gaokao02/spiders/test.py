import requests
import json
from fake_useragent import UserAgent
from elasticsearch import Elasticsearch
es = Elasticsearch(['127.0.0.1'])
ua = UserAgent()
header = str(ua.random)
# print(header)
url = 'https://gongyi-api.shuidichou.com/api/pf/v1/fundraising/fundraising-list?limit=300'
headers = {
    'User-Agent': header
}
response = requests.post(url, headers = headers).content
dd = json.loads(response)
# print(dd)
#
s = dd['data']
f = s['data']

# count = 0
# print(f)
# i = 1
# for g in f:
#     # print(g['infoNum'])
#     url_key = 'https://gongyi-api.shuidichou.com/api/pf/v1/fundraising/detail?infoNum=' + g['infoNum']
# #     count = count+1
# #     print(url_key)
#     res = requests.post(url_key, headers=headers).text
#     yy = json.loads(res)
#     bb = yy['data']
#     print(bb)
#
#     a = es.index(
#         index='demo-shuidi',
#         doc_type='doc',
#         id=i,
#         body=bb
#     )
#     i += 1
#     print(a)
