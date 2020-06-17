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

