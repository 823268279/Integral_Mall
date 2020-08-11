import requests
import chardet

x=requests.get(url='https://weibo.com/u/7430024741?from=myfollow_all&is_all=1',verify=True)
y=x.text

print(y)