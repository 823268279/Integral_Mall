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
import pymysql



class Way():
    # sql insert 
    def sql_insert(self,table,data):
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
            data['%s' % row_name[i][0]]=select_data[i]
        return data



    # create excel
    def create_excel_file(self):
        # global __file__
        # now = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M')
        # __file__ = r'../test_data/%s_test_data.xlsx' % now
        __file__ = r'../test_data/2020-05-09-09-27_test_data.xlsx'
        workbook=xlsxwriter.Workbook(__file__)
        workbook.add_worksheet('Sheet1')
        workbook.close()
    # write data
    def xlsx_write_way(self,x,y):
        __file__ = r'../test_data/2020-05-09-09-27_test_data.xlsx'
        wb=load_workbook(filename=__file__)
        sheet1=wb['Sheet1']
        # adjustment col width
        sheet1.column_dimensions['A'].width = 20
        sheet1.column_dimensions['B'].width = 30
        sheet1.column_dimensions['C'].width = 20
        sheet1.column_dimensions['D'].width = 30
        sheet1.column_dimensions['E'].width = 50
        sheet1.column_dimensions['F'].width = 50
        sheet1.column_dimensions['G'].width = 30
        # adjustment row height
        for i in range(1,2):
                sheet1.row_dimensions[i].height = 80
        # align center and auto line feed
        for i in range(1,200):
                sheet1['A%s' % i ].alignment = Alignment(horizontal='center', vertical='center',wrap_text=True)
                sheet1['B%s' % i ].alignment = Alignment(horizontal='center', vertical='center',wrap_text=True)
                sheet1['C%s' % i ].alignment = Alignment(horizontal='center', vertical='center',wrap_text=True)
                sheet1['D%s' % i ].alignment = Alignment(horizontal='center', vertical='center',wrap_text=True)
                sheet1['E%s' % i ].alignment = Alignment(horizontal='center', vertical='center',wrap_text=True)
                sheet1['F%s' % i ].alignment = Alignment(horizontal='center', vertical='center',wrap_text=True)
                sheet1['G%s' % i ].alignment = Alignment(horizontal='center', vertical='center',wrap_text=True)
        # write table_head
        table_head=["test_case","test_name","request_way","request_url","request_body","response_body","备注"]
        for i in range(1,len(table_head)+1):
                sheet1.cell(1,i).value=table_head[i-1]
        # wirte data rule
        for i in range(len(y)):
                sheet1.cell(x,2+i).value=y[i]  
        wb.save(__file__)

# get new html report 
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


# send html
class Smtp():
    def format_addr(self,x):
        name, addr = parseaddr(x)
        return formataddr((Header(name, 'utf-8').encode(), addr))
    def send_mail(self,local_file):
        user='503645047@qq.com'
        password='hufvhexcdiifbidg'
        user_to='823268279@qq.com'
        msg = MIMEMultipart()
        msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))
        msg['From'] = Smtp().format_addr('徐铃纹 <%s>' % user)
        msg['To'] = Smtp().format_addr('管理员 <%s>' % user_to)
        msg['Subject'] = Header('来自测试部————徐……', 'utf-8').encode()
        att1 = MIMEText(open('%s' % local_file, 'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = 'attachment; filename= %s' %  local_file
        msg.attach(att1)
        stmp_server='smtp.qq.com'
        server=smtplib.SMTP(stmp_server,25)
        server.set_debuglevel(1)
        server.login(user,password)
        server.sendmail(user,[user_to],msg.as_string())
        server.quit()


# z=Way().sql_select('car_data_response')
# print(z)