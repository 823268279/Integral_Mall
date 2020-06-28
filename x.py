# from mitmproxy import http,ctx

# def request(flow):
#     print(flow.request.host)    #host标头值
#     print(flow.request.url)     #请求的url地址
#     print(flow.request.scheme)  #请求的协议
#     print(flow.request.port)    #请求的端口
#     print(flow.request.method)  #请求的方法
#     print(flow.request.headers) #请求的头信息
#     print(flow.request.cookies) #请求cookies
#     print(flow.request.get_text())  #请求body
# from mitmproxy import http,ctx
# def response(flow):

#     print(flow.repsonse.status_code)    #响应状态码
#     print(flow.request.headers)         #响应头信息
#     print(flow.repsonse.cookies)        #响应cookies
#     print(flow.response.text)           #响应内容


import random

import sqlite3
import json


conn = sqlite3.connect('./test_data/test.db')

cur = conn.cursor()

# cur.execute('create table viprgst(success bool,errorCode int(2),message varchar(120),opnID varchar(120) primary key,unionID null,tel varchar(60),smsCode null,crdFaceID varchar(120),crdID varchar(120),crmGuestId varchar(120),idTyp null,isBind boll,isMember boll,lvlID null,memberName null,memberTypID varchar(20),orgID varchar(20),jsCode null,appID null,appSecret null,sessionKey null,cpnID null,subID null,idSource int(3),gstID int(3))')
cur.execute("select * from sqlite_master")
# cur.execute("insert into viprgst(success,errorCode,message,opnID,tel,crdFaceID,crdID,crmGuestId,isBind,isMember,memberTypID,orgID,idSource,gstID) values (True,0,'注册成功','FQAZEJC-kfn-zvluVBWOS-XV',13168867862,88000100000143,188000100000143161,88000100000143,True,True,01,0000,0,195)")

# cur.execute("PRAGMA table_info(viprgsto)")

data={
        'opnID': 'FQAZEJC-kfn-zvluVBWOS-XV',
        'unionID': None,
        'tel': '13168867862',
        'smsCode': None,
        'crdFaceID': '88000100000143',
        'crdID': '188000100000143161',
        'crmGuestId': '88000100000143',
        'idTyp': None,
        'isBind': True,
        'isMember': True,
        'lvlID': None,
        'memberName': None,
        'memberTypID': '01',
        'orgID': '0000',
        'jsCode': None,
        'appID': None,
        'appSecret': None,
        'sessionKey': None,
        'cpnID': None,
        'subID': None,
        'idSource': 0,
        'gstID': 195
		}

# cur.execute('create table viprgsto(success bool,errorCode int(2),message varchar(255),data varchar(255))')
cur.execute("insert into viprgsto(success,errorCode,message,data) values (True,0,'注册成功',%s)"% str(data))
cur.execute("PRAGMA table_info(viprgsto)")
cur.execute("select * from viprgsto")
z=cur.fetchall()
print(z) 


cur.close()
conn.commit()
conn.close()
