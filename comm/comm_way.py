# -*- coding: utf-8 -*-
__author__ = "wowo-x"


import datetime
import xlrd
import xlsxwriter
from openpyxl import load_workbook
from openpyxl.styles import Font, colors, Alignment
import random
import json
import xmltodict
import dicttoxml


import os
import sys
import time
import smtplib
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr, formataddr



class Way():
      def now_time(self):
            nowtime_x=datetime.datetime.now().strftime('%Y-%m-%d')
            nowtime_y=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            return nowtime_x ,nowtime_y
      def xmltodict(self,xml):
            data_xml = xmltodict.parse(xml)
            data_json = json.dumps(data_xml)
            return data_json
      def dicttoxml(self,json):
            data_xml = dicttoxml.dicttoxml(json,root=False,attr_type=False).decode('utf-8') 
            return data_xml
      #创建excel
      def create_excel_file(self):
            # global __file__
            # now = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M')
            # __file__ = r'../test_data/%s_test_data.xlsx' % now
            __file__ = r'../test_data/2020-05-09-09-27_test_data.xlsx'
            workbook=xlsxwriter.Workbook(__file__)
            workbook.add_worksheet('Sheet1')
            workbook.close()
      #写入数据
      def xlsx_write_way(self,x,y):
            __file__ = r'../test_data/2020-05-09-09-27_test_data.xlsx'
            wb=load_workbook(filename=__file__)
            sheet1=wb['Sheet1']
            # 调整列宽
            sheet1.column_dimensions['A'].width = 20
            sheet1.column_dimensions['B'].width = 30
            sheet1.column_dimensions['C'].width = 20
            sheet1.column_dimensions['D'].width = 30
            sheet1.column_dimensions['E'].width = 50
            sheet1.column_dimensions['F'].width = 50
            sheet1.column_dimensions['G'].width = 30
            # 调整行高
            for i in range(1,2):
                  sheet1.row_dimensions[i].height = 80
            # 设置居中，自动换行
            for i in range(1,200):
                  sheet1['A%s' % i ].alignment = Alignment(horizontal='center', vertical='center',wrap_text=True)
                  sheet1['B%s' % i ].alignment = Alignment(horizontal='center', vertical='center',wrap_text=True)
                  sheet1['C%s' % i ].alignment = Alignment(horizontal='center', vertical='center',wrap_text=True)
                  sheet1['D%s' % i ].alignment = Alignment(horizontal='center', vertical='center',wrap_text=True)
                  sheet1['E%s' % i ].alignment = Alignment(horizontal='center', vertical='center',wrap_text=True)
                  sheet1['F%s' % i ].alignment = Alignment(horizontal='center', vertical='center',wrap_text=True)
                  sheet1['G%s' % i ].alignment = Alignment(horizontal='center', vertical='center',wrap_text=True)
            #写入表头
            table_head=["test_case","test_name","request_way","request_url","request_body","response_body","备注"]
            for i in range(1,len(table_head)+1):
                  sheet1.cell(1,i).value=table_head[i-1]
         

            #写入数据的规则
            for i in range(len(y)):
                  sheet1.cell(x,2+i).value=y[i]
                  
            wb.save(__file__)
      #读取excel数据
      def xlsx_read_way(self):
            __file__ = r'../test_data/2020-05-09-09-27_test_data.xlsx'
            workbook=load_workbook(__file__)
            worksheet=workbook['Sheet1']
            return worksheet
      #商品资料
      def commodity_random(self):
            list=[]
            a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                        'u', 'v', 'w', 'x', 'y', 'z']
            b = ['袋','包','盒','瓶','件','箱','个']
            c = ['黑龙江','山东','河南','湖北','山西','安徽','湖南','陕西','福建','吉林','四川','甘肃','江苏','云南','贵州',
                  '江西','浙江','海南','辽宁','台湾','河北','青海','广东']
            #赠品编码
            list.append('%s%s' % (sum(random.sample(range(10000,90000),4)),sum(random.sample(range(100,900000),4))))
            #赠品品牌
            list.append('赠品品牌%s%s' % (random.choice(a),sum(random.sample(range(100,1000),2))))
            #赠品名称
            list.append('赠品名称%s%s' % (random.choice(a),sum(random.sample(range(100,1000),2))))
            #赠品规格
            list.append('%sg' % sum(random.sample(range(50,400),2))) 
            #赠品单位
            list.append(random.choice(b))
            #赠品进货价
            purchasing_price = int(sum(random.sample(range(2000,7000),2)))
            list.append(purchasing_price)
            #赠品零售价
            list.append(purchasing_price + sum(random.sample(range(500,2000),2)))
            #赠品产地
            list.append(random.choice(c))
            return list
      #活动名称
      def activity_name_random(self):
            a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']
            x = '会员活动%s%s%s%s'% (random.choice(a),random.choice(a),sum(random.sample(range(10,100),2)),sum(random.sample(range(10,100),2)))
            return x
      #随机openid
      def get_openid(self):
            a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']
            x = '%s%s%s%s%s%s%s-'%(random.choice(a),random.choice(a),random.choice(a),random.choice(a),random.choice(a),random.choice(a),random.choice(a))
            y = '%s%s%s-%s%s%s%s'%(random.choice(a),random.choice(a),random.choice(a),random.choice(a),random.choice(a),random.choice(a),random.choice(a))
            z = '%s%s%s%s%s-%s%s'%(random.choice(a),random.choice(a),random.choice(a),random.choice(a),random.choice(a),random.choice(a),random.choice(a))
            v = '%s%s%s'%(x,y,z)
            return v

      #随机会员信息
      def menber_information_random(self):
            list=[]
            a = ['01','02','03','04']
            b = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                        'U', 'V', 'W', 'X', 'Y', 'Z']
            c = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z']
            #卡类型
            list.append(random.choice(a))      
            #姓名
            q1 = '%s%s' % (random.choice(b),random.choice(b))
            q2 = '%s%s%s%s%s' % (random.choice(c),random.choice(c),random.choice(c),random.choice(c),random.choice(c))
            list.append('%s%s' % (q1,q2))
            #手机
            list.append('13%s%s' % (sum(random.sample(range(10000,100000),1)),sum(random.sample(range(1000,10000),1))))
            #生日
            e1 = '19%s'% (sum(random.sample(range(10,100),1)))
            e2 = '0%s'% sum(random.sample(range(1,10),1))
            e3 = '%s'% sum(random.sample(range(10,29),1))
            list.append('%s-%s-%s'% (e1,e2,e3))
            #身份证
            r1 = '%s'% sum(random.sample(range(1000,10000),1)) 
            r2 = '%s%s%s'% (e1,e2,e3)
            r3 = '%s'% sum(random.sample(range(1000,10000),1)) 
            list.append('51%s%s%s'% (r1,r2,r3))
            return list
      #随机停车场信息
      def parking_data_random(self):
            list=[]
            #停车场编号
            list.append(sum(random.sample(range(10000000,999999999),4)))
            #故障热线
            list.append('13%s%s' % (sum(random.sample(range(10000,100000),1)),sum(random.sample(range(1000,10000),1))))
            return list
      #储值兑换线/返利兑换线
      def exchange_money_random(self):
            z='%s' % sum(random.sample(range(1000,7000),1))    
            return str(z)
      #充值金额/冲正积分
      def top_up_random(self):
            z='%s' % sum(random.sample(range(50000,100000),1))    
            return str(z)
      def cash_register_header(self):
            hdr_json = {
                  "hdr": {
                        "row": {
                              "command": "0",#指令
                              "postype": "0",#商城类型
                              "corpid": "200002",#企业编号
                              "organ": "0000",#机构
                              "posid": "POS006",#收银机编号
                              "billid": "",#消费小票号
                              "receid": "1001",#门店
                              "credential": "28ee304a-8aae-11ea-aa9f-00e04c361826",#收银机标识符
                              "keyid": "",
                              "types": "1"
                        }
                  }
            }
            return hdr_json
      #会员消费小票号
      def billid_random_a(self):
            x = sum(random.sample(range(80000,900000),4))
            return x
      #会员消费随机金额
      def expenditure_sum(self):
            x = sum(random.sample(range(50,300),1))
            return x
      #会员消费流水号
      def billid_random_b(self):
            x = sum(random.sample(range(80000,900000),4))
            y = sum(random.sample(range(80000,900000),4))
            z = '%s%s' % (x,y)
            return z
      #会员消费订单号
      def Orderid_random(self):
            a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                                    'u', 'v', 'w', 'x', 'y', 'z']
            x = '%s%s%s%s' % (sum(random.sample(range(0,10000),3)),random.choice(a),sum(random.sample(range(0,10000),3)),random.choice(a))
            y = '%s%s%s%s' % (sum(random.sample(range(0,10000),3)),random.choice(a),sum(random.sample(range(0,10000),3)),random.choice(a))
            z = '%s%s' % (x,y)
            return z
      

#获取最新html报告
class Report():  
    sys.path.append('./report')
    def get_new_report(self,file_path):
        dir_list = os.listdir(file_path)
        if not dir_list:
            return
        else:
            for i in dir_list:
                html_path ='./report/' + i 
                html_crate_time = time.localtime(os.stat(html_path).st_mtime)
                html_crate_time=time.strftime("%Y-%m-%d %H:%M", html_crate_time)
                nowtime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
                if html_crate_time == nowtime:
                    return html_path    
                else:
                    pass


#发送html
class Smtp():
    #格式化邮箱地址
    def format_addr(self,x):
        name, addr = parseaddr(x)
        return formataddr((Header(name, 'utf-8').encode(), addr))
    def send_mail(self,local_file):
        #发送邮箱
        user='503645047@qq.com'
        #qq邮箱登录授权码
        password='hufvhexcdiifbidg'
        #接受邮箱
        user_to='823268279@qq.com'
        #邮件对象
        msg = MIMEMultipart()
        # 邮件正文是MIMEText:
        msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))
        msg['From'] = Smtp().format_addr('徐铃纹 <%s>' % user)
        msg['To'] = Smtp().format_addr('管理员 <%s>' % user_to)
        msg['Subject'] = Header('来自测试部————徐……', 'utf-8').encode()
        # 构造附件
        att1 = MIMEText(open('%s' % local_file, 'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att1["Content-Disposition"] = 'attachment; filename= %s' %  local_file
        msg.attach(att1)

        #SMTP——qq邮箱服务器地址
        stmp_server='smtp.qq.com'
        server=smtplib.SMTP(stmp_server,25)
        #打印和SMTP服务器交互的信息
        server.set_debuglevel(1)
        #login()方法用来登录SMTP服务器
        server.login(user,password)
        #sendmaill()方法用来发邮件，[]表示可以发送多个人
        #as_string()方法用来把MIMEText对象变成str
        server.sendmail(user,[user_to],msg.as_string())
        server.quit()



z=Way().parking_data_random()
print(z)