# -*- coding:utf-8 -*-
import json
import requests
from elasticsearch import Elasticsearch

es=Elasticsearch(['127.0.0.1'])
a = 0
def recursion(infoid):
    print('------------------------------------------------')
    # if infoid != 'None':
    response1 = requests.post('https://api.shuidichou.com/api/cf/content/user/related-case',
                             data={'infoId': infoid })
    d = json.loads(response1.text)['data']
    for i in range(len(d)):

        es.index(
            index='test',
            doc_type="doc",
            id=a,
            body=d[i]
        )

        i = i + 1
        for j in d[i]:
            if j == 'infoId':
                infoid = d[i][j]
                print('infoid:',infoid)
            if j == 'title':
                print('title:',d[i][j])
            if j == 'description':
                print('description:',d[i][j])
            if j == 'amount':
                print('amount',d[i][j])
            if j == 'donationCount':
                print('donationCount:',d[i][j])
            if j == 'targetAmount':
                print('targetAmount:',d[i][j])
        recursion(infoid)

{"authorizationV2":"8uz_hBIPBVhTCiTzVd5qxH88rL-kSN511CE7zgSnKYQ="}
response = requests.post('https://api.shuidichou.com/api/cf/v1/publicity/list', data = {'AuthorizationV2':'eE4DaYzF-yJfT7Of5lhCS06VsWZ17o1fRCmJNsguP6o='})
d = json.loads(response.text)['data']
for i in range(len(d)):
    # infoid
    print(i)
    es.index(
        index='test',
        doc_type="doc",
        id=a,
        body=d[i]
    )

    i=i+1

    for j in d[i]:
        if j == 'title':
            print(d[i][j])
        if j == 'amount':
            print(d[i][j])
        if j == 'description' or j == 'content':
            print(d[i][j])
        if j == 'donationCount':
            print(d[i][j])
        if j == 'targetAmount':
            print(d[i][j])
        if j == 'infoId':
            infoid = d[i][j]
            print(infoid)
            recursion(infoid)
