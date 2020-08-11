import pytest
import datetime
import os
import sys
import time
import smtplib
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr, formataddr

#获取最新html报告
class Report():  
#     sys.path.append('../report')
    def get_new_report(self,file_path):
        dir_list = os.listdir(file_path)
        if not dir_list:
            return
        else:
            for i in dir_list:
                html_path ='../report/' + i 
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


def x():
        #传入路径获取最新测试报告的地址
        html_path=Report().get_new_report('../report')
        #传入html报告地址发送邮件
        Smtp().send_mail(html_path)

if __name__ == "__main__":
        now_time='%s' % datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        # pytest.main(
        #                 [
        #                 '../conftest/',
        #                 '-v',
        #                 '--html=../report/NEWCRM__%s.html' % now_time,
        #                 '--self-contained-html'
        #                 ]
        #         )
        # x()


