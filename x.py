# # from mitmproxy import http,ctx

# # def request(flow):
# #     print(flow.request.host)    #host标头值
# #     print(flow.request.url)     #请求的url地址
# #     print(flow.request.scheme)  #请求的协议
# #     print(flow.request.port)    #请求的端口
# #     print(flow.request.method)  #请求的方法
# #     print(flow.request.headers) #请求的头信息
# #     print(flow.request.cookies) #请求cookies
# #     print(flow.request.get_text())  #请求body
# # from mitmproxy import http,ctx
# # def response(flow):

# #     print(flow.repsonse.status_code)    #响应状态码
# #     print(flow.request.headers)         #响应头信息
# #     print(flow.repsonse.cookies)        #响应cookies
# #     print(flow.response.text)           #响应内容


import random
import datetime
import pymysql


def sql_insert(table,data,id):
    conn = pymysql.connect('localhost','root','root','newcrm')
    cur = conn.cursor()
    try:
        # create table
        sql="create table %s(%s varchar(40) primary key)" % (table,'insert_date')
        cur.execute(sql)
        # for add col
        for i in data:
            sql="alter table %s add %s varchar(120)" % (table,i)  
            cur.execute(sql) 
    except:
        pass
    finally:
        for i,n in data.items():
            # date desc select first col data whether equal now_date
            sql="select %s from %s where %s=%s" % (id,table,id,data['%s' % id])
            cur.execute(sql)
            x=cur.fetchall()
            now=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
            # exist update data
            if x and str(x[0][0])==str(data['%s' % id]):
                sql="update %s set %s='%s' where insert_date='%s'" % (table,i,n,now)
                cur.execute(sql)
            # inexistence insert data
            else:
                sql="insert into %s(insert_date,%s) values('%s','%s')" % (table,i,now,n)
                cur.execute(sql)
    cur.close()
    conn.commit()
    conn.close()





data={
	'tknTpName': '电子券',
	'tknFrm': 0,
	'tknNtu': 0,
	'sttName': None,
	'rcvRulName': None,
	'cpnID': '0001',
	'tknID': '667056',
	'name': '消费338,即可使用',
	'tknvl': 55,
	'consumeMoney': 338,
	'tknImg': None,
	'tknDsc': None,
	'tknTpID': '01',
	'sndRul': '消费大于等于338,即可使用面额为55的优惠券',
	'rcvRul': None,
	'vipTpID': None,
	'brfId': None,
	'sDt': '2020-07-10 15:18:34',
	'eDt': '2020-07-13 15:18:34',
	'tStt': 'F',
	'useSDy': 0,
	'useADy': 0,
	'tknSdt': None,
	'tknEdt': None,
	'rjcStt': 'F',
	'brf': 'apitest update',
	'impCRM': 0,
	'stt': 2,
	'uptDtt': '2020-07-10 15:18:34'
}
