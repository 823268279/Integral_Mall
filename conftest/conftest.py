#coding=utf-8


import xlsxwriter
from openpyxl import load_workbook
from openpyxl.styles import Font, colors, Alignment

import datetime
from py._xmlgen import html
import pytest
import requests
import json
import random

from comm.comm_way import Way#公共方法
comm_way=Way()


# 添加接口地址与项目名称
def pytest_configure(config):
    config._metadata["项目名称"] = "NEW_CRM_v1.0"
    config._metadata['测试地址'] = 'http://api.newcrm.group.weixin.wuerp.com'
# 添加所属部门与测试人员
@pytest.mark.optionalhook
def pytest_html_results_summary(prefix):
    prefix.extend([html.p("所属部门: 测试部")])
    prefix.extend([html.p("测试人员: wowo")])



#获取请求头
@pytest.fixture(scope='session')    
def headers():
    url='http://api.newcrm.group.weixin.wuerp.com/api/v1.0/Token/Get'
    data={
        "id":"wx5f1e0495dc540bb1",
        "key":"7947ff3cbf06647f312e4e6ec5e32943"
        }
    try:
        response=requests.post(url=url,data=data)
        response_json=response.json()
        assert response.status_code == 200
        assert response_json['message'] =='获取授权成功'
        print(response_json['message'])
        headers={}
        headers['Authorization']=response_json['data']['Data']['token']
        return headers
    except:
        raise

#获取验证码
@pytest.fixture(scope='session')   
def phone_code():
    response=requests.post('http://api.newcrm.group.weixin.wuerp.com/manage/v1.0/User/GetCode')
    response_json=response.json()
    auth_code = response_json['data']['Data']
    assert response.status_code == 200
    assert response_json['success'] == True
    print(response_json['message'])
    return auth_code

#phone端的配置    
@pytest.fixture(scope='session')    
def menber():
    data={
        "CpnID":'0001',
        "SubID":'3378049226@qq.com',
        "url":'http://api.newcrm.group.weixin.wuerp.com/member/v1.0%s'
        }
    return data

#web端的配置
@pytest.fixture(scope='session')   
def manage():
    data={
        "username":"miscs3",
        "password":"111111",
        "CpnID":'0001',
        "SubID":'3378049226@qq.com',
        "url":'http://api.newcrm.group.weixin.wuerp.com/manage/v1.0%s'
        }
    return data


#获取当前时间
@pytest.fixture(scope='function')  
def now_time():
    data={}
    data['ymd']=datetime.datetime.now().strftime('%Y-%m-%d')
    data['ymd_hms']=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data['StDt']=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data['EdDt']=(datetime.datetime.now()+datetime.timedelta(days=3)).strftime('%Y-%m-%d %H:%M:%S')
    return data


#随机会员数据
@pytest.fixture(scope='module')   
def menber_data_random():
    data={}
    a = ['01','02','03','04']
    b = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                'U', 'V', 'W', 'X', 'Y', 'Z']
    c = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']
    #openid
    x = '%s%s%s%s%s%s%s-'%(random.choice(b),random.choice(b),random.choice(b),random.choice(b),random.choice(b),random.choice(b),random.choice(b))
    y = '%s%s%s-%s%s%s%s'%(random.choice(c),random.choice(c),random.choice(c),random.choice(c),random.choice(c),random.choice(c),random.choice(c))
    z = '%s%s%s%s%s-%s%s'%(random.choice(b),random.choice(b),random.choice(b),random.choice(b),random.choice(b),random.choice(b),random.choice(b))
    data['OpnID']='%s%s%s'%(x,y,z)
    #卡类型
    data['VipTpID']=random.choice(a)  
    #姓名
    q1 = '%s%s' % (random.choice(b),random.choice(b))
    q2 = '%s%s%s%s%s' % (random.choice(c),random.choice(c),random.choice(c),random.choice(c),random.choice(c))
    data['Name']='%s%s' % (q1,q2)
    #手机
    data['Tel']='13%s%s' % (sum(random.sample(range(10000,100000),1)),sum(random.sample(range(1000,10000),1)))
    #生日
    e1 = '19%s'% (sum(random.sample(range(10,100),1)))
    e2 = '0%s'% sum(random.sample(range(1,10),1))
    e3 = '%s'% sum(random.sample(range(10,29),1))
    data['Brth']='%s-%s-%s'% (e1,e2,e3)
    #身份证
    r1 = '%s'% sum(random.sample(range(1000,10000),1)) 
    r2 = '%s%s%s'% (e1,e2,e3)
    r3 = '%s'% sum(random.sample(range(1000,10000),1)) 
    data['IDntNmb']='51%s%s%s'% (r1,r2,r3)
    return data


#获取s3小票
@pytest.fixture(scope='session')  
def get_s3_ticket():
    data={}
    data['ticket']={'file': open('../img/ticket_one.jpg', 'rb')}
    return data

#获取s3广告
@pytest.fixture(scope='session')  
def get_s3_advert():
    data={}
    data['ticket']={'file': open('../img/advert_one.jpg', 'rb')}
    return data

#随机停车场信息
@pytest.fixture(scope='function')   
def parking_data_random():
    data={}
    #停车场编号
    data['ParkID']=sum(random.sample(range(10000000,999999999),4))
    #故障热线
    data['Tel']='13%s%s' % (sum(random.sample(range(10000,100000),1)),sum(random.sample(range(1000,10000),1)))
    return data

#随机车辆信息
@pytest.fixture(scope='function') 
def car_data_random():
    a = ['法拉利','兰博基尼','大众','丰田','马自达','别克','雪佛兰','福特','标志','现代','奔驰','奥迪','宝马','比亚迪']
    b = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    data={}
    #车辆编号
    data['CarID'] = '川Y.%s%s%s'% (random.choice(b),random.choice(b),sum(random.sample(range(300),3)))
    data['carTp'] = random.choice(a)
    return data



# mysql select table：register_request
@pytest.fixture(scope='session')
def menber_register_request_data():
    return comm_way.sql_select('register_request')


# mysql select table： register_response
@pytest.fixture(scope='session')    
def menber_register_response_data(): 
    return comm_way.sql_select('register_response')


# mysql select table： menber_data_response
@pytest.fixture(scope='session')
def menber_data():
    return comm_way.sql_select('menber_data_response')

    
# mysql select table： parking_response
@pytest.fixture(scope='session')    
def parking_page_data():
    return comm_way.sql_select('parking_response')

# mysql select table： parking_rule_response
@pytest.fixture(scope='session')    
def parking_rule_page_data():
    return comm_way.sql_select('parking_rule_response')

# mysql select table： upload_ticket_response
@pytest.fixture(scope='session')    
def upload_ticket_response_data():
    return comm_way.sql_select('upload_ticket_response')

# mysql select table： upload_advert_response
@pytest.fixture(scope='session')    
def upload_advert_response_data():
    return comm_way.sql_select('upload_advert_response')

# mysql select table: car_data_response
@pytest.fixture(scope='session')    
def car_data_response_data():
    return comm_way.sql_select('car_data_response')

# mysql select table: advert_position_response
@pytest.fixture(scope='session')    
def advert_position_response_data():
    return comm_way.sql_select('advert_position_response')



