# coding: utf-8

import requests
import urllib
import json

# App_id and app_key  # noqa
app_id = 'your-app-id'
app_key = 'your-app-key'

# proxies = None
_usr = 'username'
_pwd = 'password'
_encoded_pwd = urllib.parse.quote(_pwd)

proxies = {
    'http': 'http://{usr}:{pwd}@svwproxy.csvw.com:8080'.format(usr=_usr, pwd=_encoded_pwd),
    'https': 'https://{usr}:{pwd}@svwproxy.csvw.com:8080'.format(usr=_usr, pwd=_encoded_pwd),
}


headers = {
    'Content-Type': 'application/json',
    'X-LC-Id': app_id,
    'X-LC-Key': app_key,
}
post = dict(content='hello world', user='bonfy')

url_post = 'https://api.leancloud.cn/1.1/classes/Post'
# 坑点： 居然是dumps到string, 好好看文档啊，真的是string
r = requests.post(url_post, data=json.dumps(post),  headers=headers, proxies=proxies)
print(r.json())
