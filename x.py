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


# import random

# import sqlite3
# import json


# conn = sqlite3.connect('./test_data/test.db')
# cur = conn.cursor()

# # cur.execute('create table viprgst(opnID varchar(40) primary key,unionID varchar(40),tel varchar(40),smsCode varchar(40),crdFaceID varchar(40),crdID varchar(40),crmGuestId varchar(40),idTyp varchar(40),isBind bool,isMember bool,lvlID varchar(40),memberName varchar(40),memberTypID varchar(40),orgID varchar(40),jsCode varchar(40),appID varchar(40),appSecret varchar(40),sessionKey varchar(40),cpnID varchar(40),subID varchar(40),idSource varchar(40),gstID varchar(40),insert_date text)')
# # cur.execute("select * from sqlite_master")
# # cur.execute("insert into viprgst(success,errorCode,message,opnID,tel,crdFaceID,crdID,crmGuestId,isBind,isMember,memberTypID,orgID,idSource,gstID) values (True,0,'注册成功','FQAZEJC-kfn-zvluVBWOS-XV',13168867862,88000100000143,188000100000143161,88000100000143,True,True,01,0000,0,195)")

# # cur.execute("PRAGMA table_info(viprgst)")









# data={
#         'opnID': 'FQAZEJC-kfn-zvluVBWOS-XV1iL',
#         'unionID': None,
#         'tel': '13168867862',
#         'smsCode': None,
#         'crdFaceID': '88000100000143',
#         'crdID': '188000100000143161',
#         'crmGuestId': '88000100000143',
#         'idTyp': None,
#         'isBind': True,
#         'isMember': True,
#         'lvlID': None,
#         'memberName': None,
#         'memberTypID': '01',
#         'orgID': '0000',
#         'jsCode': None,
#         'appID': None,
#         'appSecret': None,
#         'sessionKey': None,
#         'cpnID': None,
#         'subID': None,
#         'idSource': 0,
#         'gstID': 195
# 		}

# def sql_insert(table,data,primary_key):
#     import sqlite3
#     import datetime
#     conn = sqlite3.connect('./test_data/test.db')
#     cur = conn.cursor()
#     for i,n in data.items():
#         #查询数据进行判断插入主键是否存在
#         cur.execute("select %s from %s order by insert_date DESC limit 0,1" % (primary_key,table))
#         x=cur.fetchall()
#         #存在就更新数据
#         if x and str(x[0][0])==data['%s' % primary_key]:
#             cur.execute("update %s set %s='%s' where %s='%s'" % (table,i,n,primary_key,data['%s' % primary_key]))
#         #不存在就插入数据 
#         else:
#             cur.execute("insert into %s(%s) values('%s')" % (table,i,n))
#             cur.execute("update %s set insert_date='%s' where %s='%s'" % (table,datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S'),primary_key,data['%s' % primary_key]))
            
#     cur.close()
#     conn.commit()
#     conn.close()
# insert_sql('viprgst',data,'opnID')
     
# def sql_select(table):
#     data={}
#     import sqlite3
#     conn = sqlite3.connect('./test_data/test.db')
#     cur = conn.cursor()

#     #查询数据
#     cur.execute("select * from %s order by insert_date DESC limit 0,1" % table)
#     select_data=cur.fetchone()
#     # print(len(select_data))

#     #查询列名    
#     cur.execute("PRAGMA table_info(viprgst)")
#     row_name=cur.fetchall()
#     for i in range(len(row_name)):
#         data['%s' % row_name[i][1]]=select_data[i]
#     return data



# select_sql('viprgst')

# import datetime

# # cur.execute("drop table viprgst")
# # cur.execute("insert into viprgst(%s) values('%s')" % (i,data[i]))
# # cur.execute("delete from viprgst")
# # cur.execute("insert into viprgst(opnID,gstID) values('FQAZEJC-kfn-zvluVBWOS-XV','134')")
# # cur.execute("insert into viprgst(insert_date) values(%s)" % datetime.datetime.now().strftime('%Y-%m-%d-%H-%M'))

# # cur.execute("select * from viprgst  order by insert_date ASC")
# cur.execute("select * from viprgst order by insert_date DESC")
# # cur.execute("delete from viprgst where insert_date is NULL")

# # cur.execute("update viprgst set tel='232323232' where opnID ='FQAZEJC-kfn-zvluVBWOS-XV'")
# z=cur.fetchall()
# # print(z)


# cur.close()
# conn.commit()
# conn.close()










data={
	'nickName': None,
	'name': None,
	'avt': None,
	'opnID': 'UTJAXED-pkf-ojgqTYFJY-FG',
	'unionID': None,
	'tel': '13286546126',
	'smsCode': None,
	'crdFaceID': '88000100000147',
	'crdID': '188000100000147370',
	'crmGuestId': '88000100000147',
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
	'idSource': None,
	'gstID': 199,
	'vipTpStt': None
}


def zz(table,data):
    import sqlite3
    import datetime
    conn = sqlite3.connect('./test_data/test.db')
    cur = conn.cursor()
    sql="create table %s(%s varchar(40))" % (table,'insert_date')
    cur.execute(sql)
    for i in data:
        print(i)
        sql="alter table %s add %s varchar(40)" % (table,i)  
        cur.execute(sql) 
    cur.close()
    conn.commit()
    conn.close()
# zz('vip',data)



def sql_insert(table,data):
    import pymysql
    import datetime
    #与数据库建立连接
    conn = pymysql.connect('localhost','root','root','newcrm')
    cur = conn.cursor()
    try:
        #创建表
        sql="create table %s(%s varchar(40) primary key)" % (table,'insert_date')
        cur.execute(sql)
        #循环添加列
        for i in data:
            sql="alter table %s add %s varchar(40)" % (table,i)  
            cur.execute(sql) 
    except:
        pass
    finally:
        for i,n in data.items():
            #查询数据进行判断插入主键是否存在
            sql="select insert_date from %s order by insert_date DESC limit 0,1" % (table)
            cur.execute(sql)
            x=cur.fetchall()
            now=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
            #存在就更新数据
            if x and str(x[0][0])==str(now):
                sql="update %s set %s='%s' where insert_date='%s'" % (table,i,n,now)
                cur.execute(sql)
            #不存在就插入数据 
            else:
                sql="insert into %s(insert_date) values('%s')" % (table,now)
                cur.execute(sql)
    cur.close()
    conn.commit()
    conn.close()





# sql_insert('vip',data)

    
            
def sql_select(table):
    data={}
    import sqlite3
    conn = sqlite3.connect('./test_data/test.db')
    cur = conn.cursor()

    #查询数据
    cur.execute("select * from %s order by insert_date DESC limit 0,1" % table)
    select_data=cur.fetchone()

    #查询列名    
    cur.execute("PRAGMA table_info(%s)" % table)
    row_name=cur.fetchall()
    for i in range(len(row_name)):
        data['%s' % row_name[i][1]]=select_data[i]
    return data

# z=sql_select('prakrule')
# print(z)
import sqlite3


conn=sqlite3.connect('./test_data/test.db')
cur=conn.cursor()



# cur.execute("delete from parking")
# cur.execute("drop table viprgst")
# cur.execute("select * from register_response")
cur.execute("select * from sqlite_master")
# cur.execute("drop table vipzy")
# cur.execute("select * from prakrule")
# x=cur.fetchall()

# print(x)


cur.close()
conn.commit()
conn.close()



