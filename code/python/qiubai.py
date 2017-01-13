# coding: utf-8

import os
import requests
import json
import urllib
from pyquery import PyQuery as pq

################################
#
# Consts
#
################################


app_id = 'APP-ID'
app_key = 'APP_KEY'

PROXIES = None

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)'
                  ' AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/38.0.2125.122 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,'
              'application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip,deflate,sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8'
}


################################
#
# requests Operation
#
################################


def GetPage(url, proxies=PROXIES, headers=HEADERS):
    r = requests.get(url, proxies=proxies, headers=headers)
    assert r.status_code == 200
    return r.text


def GetMedia(
        url, proxies=PROXIES, headers=HEADERS, chunk_size=512,
        media_type='image'):
    r = requests.get(url, proxies=proxies, headers=headers, stream=True)
    filename = 'download/' + media_type + '/' + os.path.basename(url)
    with open(filename, 'wb') as fd:
        for chunk in r.iter_content(chunk_size):
            fd.write(chunk)
    return filename

################################
#
# qiubai transfer
#
################################
def TransferPageToData_qiubai(url):
    page = GetPage(url)
    results = []
    d = pq(page)
    contents = d("div .article")
    for item in contents:
        i = pq(item)
        pic_url = i("div .thumb img").attr.src
        content = i("div .content").text()
        qiubai_id = i.attr.id
        print("qiubai:", qiubai_id)
        if pic_url:
            # pic_path = GetMedia(pic_url)
            dct = {
                'id': qiubai_id,
                'type': 'pic',
                'mediapath': pic_url,
                'content': content
            }
        else:
            dct = {
                'id': qiubai_id,
                'type': 'text',
                # 'mediapath': '',
                'content': content
            }
        results.append(dct)
    return results

# save to leancloud
# TODO: 判断 obj.id 不重复插入
def save(obj):
    proxies = PROXIES
    headers = {
        'Content-Type': 'application/json',
        'X-LC-Id': app_id,
        'X-LC-Key': app_key,
    }
    url_post = 'https://api.leancloud.cn/1.1/classes/Joke'
    r = requests.post(url_post, data=json.dumps(obj),  headers=headers, proxies=proxies)
    print(r.json())

# TODO:
def post_twitter():
    pass

# TODO: 定时清理 原则上删除上礼拜发布的东西 清除
def clean():
    pass


if __name__ == '__main__':
    url = 'http://www.qiushibaike.com/'
    results = TransferPageToData_qiubai(url)
    print('-------------id--------------')
    for obj in results:
        print(obj['id'])
    # for obj in results:
    #     save(obj)
