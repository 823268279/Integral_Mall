import requests
import random
import xlsxwriter
from time import sleep
from bs4 import BeautifulSoup
import datetime
import sqlite3
import pymysql



class Way():
    # response dispose to capitalize
    def response_dispose(self,dict_info):
        new_dict = {}
        for i, n in dict_info.items():
                new_dict[i.capitalize()] = n
        return new_dict

    # sql insert 
    def sql_insert(self,table,data):
        # sqlite3 connect
        # conn = sqlite3.connect('../test_data/test.db')

        # pymysql connect
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
                sql="select insert_date from %s order by insert_date DESC limit 0,1" % (table)
                cur.execute(sql)
                x=cur.fetchall()
                now=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
                # exist update data
                if x and str(x[0][0])==str(now):
                    sql="update %s set %s='%s' where insert_date='%s'" % (table,i,n,now)
                    cur.execute(sql)
                # inexistence insert data
                else:
                
                    sql="insert into %s(insert_date,%s) values('%s','%s')" % (table,i,now,n)
                    cur.execute(sql)
        cur.close()
        conn.commit()
        conn.close()

    # sql select 
    def sql_select(self,table):
        data={}
        # sqlite3 connect
        # conn = sqlite3.connect('../test_data/test.db')

        # pymysql connect
        conn = pymysql.connect('localhost','root','root','newcrm')

        cur = conn.cursor()
        # date desc select first row
        sql="select * from %s order by insert_date DESC limit 0,1" % table
        cur.execute(sql)
        select_data=cur.fetchone()

        # sqlinte3 select col_naame
        # sql="PRAGMA table_info(%s)" % table

        # pymysql select col_naame
        sql="select COLUMN_NAME from information_schema.COLUMNS where table_name = '%s'" % table

        cur.execute(sql)
        row_name=cur.fetchall()
        for i in range(len(row_name)):
            # pymysql
            data['%s' % row_name[i][0]]=select_data[i]

            # sqlinte3
            # data['%s' % row_name[i][1]]=select_data[i]

        cur.close()
        conn.close()
        return data
        
comm_way=Way()


#请求头
headers = {
            'Accept': "application/json, text/javascript, */*; q=0.01",
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
          }

def cookie_z():
    url_start='http://category.dangdang.com/cid4005626.html'   
    headers["Referer"]=url_start
    #创建会话
    global session_z
    session_z=requests.session()
    session_z.get(url=url_start,headers=headers,verify=False).text
    #获取cookie
    global cookie
    cookie=session_z.cookies



#开始爬数据
def start():
    #商品名称
    list_a=[]
    #商品图片url
    list_b=[]
    #商品价格
    list_c=[]
    #商品品牌
    list_d=[]
    for i in range(7):
        # 休闲食品
        # url='http://category.dangdang.com/pg%s-cid4005626.html'% str(i+1)
        # 酒
        # url='http://category.dangdang.com/pg%s-cid4005626.html'% str(i+1)
        # 茶
        url='http://category.dangdang.com/pg%s-cid4005625.html'% str(i+1)


        response= session_z.get(url=url,headers=headers,cookies=cookie)
        soup=BeautifulSoup(response.text,'html.parser')
        for  n in soup.find_all('li'):
            for m in n.find_all('img'):
                if m.get('data-original')== None:
                    list_a.append(m.get('alt'))
                    list_b.append(m.get('src'))
                else:
                    list_a.append(m.get('alt'))
                    list_b.append(m.get('data-original'))

            for k in n.find_all('span',class_='price_n'):
                list_c.append(k.string[1:])
            for p in n.find_all('p',class_='link'):
                list_d.append(p.string)


    c = ['黑龙江','山东','河南','湖北','山西','安徽','湖南','陕西','福建','吉林','四川','甘肃','江苏','云南','贵州',
                  '江西','浙江','海南','辽宁','台湾','河北','青海','广东']
    for i in range(len(list_d)):
        data={}
        data['commodity_code']=sum(random.sample(range(10000,999999),10))
        data['commodity_name']=list_a[i]
        data['commodity_image']=list_b[i]
        data['commodity_price']=list_c[i]
        data['commodity_brand']=list_d[i]
        data['commodity_place']=random.choice(c)
        print(data['commodity_code'],data['commodity_name'],data['commodity_image'],data['commodity_price'],data['commodity_brand'],data['commodity_place'])
        comm_way.sql_insert('commodity_data',data)
   



if __name__ == "__main__":
    cookie_z()
    start()


