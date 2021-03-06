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
        response_json = comm_way.response_dispose(response.json())
        print(response_json['Message'])
        assert response.status_code == 200
        assert response_json['Success'] == True
        headers={}
        headers['Authorization']=response_json['Data']['Data']['token']
        # headers['Content-Type']='text/json;charset=utf-8'
        return headers
    except:
        raise


#phone端的配置    
@pytest.fixture(scope='session')    
def member():
    data={
        "CpnID":'0001',
        "SubID":'3378049226@qq.com',
        "PayAppID":"wx85013334c4606398",
        "PayAppSecrect":"9ea8b31f0d8f7fadae85afde14c77fa8",
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
    data['later']=(datetime.datetime.now()-datetime.timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')
    return data


#随机会员数据
@pytest.fixture(scope='module')   
def member_data_random():
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
    data['UnionID']='%s%s%s'%(x,y,z)
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

#随机优惠券数据
@pytest.fixture(scope='module')   
def ticket_data_random():
    data={}
    # 券ID
    TknID = sum(random.sample(range(100000,1000000),2))
    # 满送金额线
    ConsumeMoney = random.choice(range(200,500))
    # 满送券面额
    Tknvl = random.choice(range(50,150))
    # 券名称
    name = '消费%s,即可使用' % (ConsumeMoney)
    # 送券描述
    SndRul = '消费大于等于%s,即可使用面额为%s的优惠券' % (ConsumeMoney,Tknvl)
    data['ConsumeMoney']=ConsumeMoney
    data['Tknvl']=Tknvl
    data['Name']=name
    data['SndRul']=SndRul
    data['TknID']=TknID
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

# random parking data
@pytest.fixture(scope='function')   
def parking_data_random():
    data={}
    #停车场编号
    data['ParkID']=sum(random.sample(range(10000000,999999999),4))
    #故障热线
    data['Tel']='13%s%s' % (sum(random.sample(range(10000,100000),1)),sum(random.sample(range(1000,10000),1)))
    return data

# random car data
@pytest.fixture(scope='function') 
def car_data_random():
    a = ['法拉利','兰博基尼','大众','丰田','马自达','别克','雪佛兰','福特','标志','现代','奔驰','奥迪','宝马','比亚迪']
    b = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    data={}
    #车辆编号
    data['CarID'] = '川Y%s%s%s'% (random.choice(b),random.choice(b),sum(random.sample(range(300),3)))
    data['carTp'] = random.choice(a)
    return data

# mysql random select table:commodity_data
@pytest.fixture(scope='session')    
def commodity_data_random():
    return comm_way.sql_select_commodity_data('commodity_data')


# random park order data
@pytest.fixture(scope='function') 
def park_order_data_random():
    data={}
    # 停车订单号
    data['BllNo'] = sum(random.sample(range(10000000,999999999),4))
    data['JoinDt'] = (datetime.datetime.now()-datetime.timedelta(hours=random.choice(range(1,24)))).strftime('%Y-%m-%d %H:%M:%S')
    return data

# random store data
@pytest.fixture(scope='function') 
def store_data_random():
    data={}
    # store code
    data['StoreID'] = sum(random.sample(range(10000000,999999999),4))
    # telephone number
    data['Tel'] = '13%s%s' % (sum(random.sample(range(10000,100000),1)),sum(random.sample(range(1000,10000),1)))
    return data

# random putaway activity data
@pytest.fixture(scope='function') 
def putaway_activity_data_random():
    data={}
    # bllno_number
    data['BllNo'] = sum(random.sample(range(10000000,999999999),4))
    # activity name
    data['Name'] = '上架活动%s'% sum(random.sample(range(100,700),2))
    # exchange integral
    data['FcttsIntg'] = sum(random.sample(range(500,1000),2))
    return data


# random integral rule
@pytest.fixture(scope='function') 
def integral_rule_data_random():
    data={}
    # integral thread
    data['Amt'] = sum(random.sample(range(1,100),2))
    # integral price
    data['Intgr'] = sum(random.sample(range(100,500),2))
    return data

# random receipt data
@pytest.fixture(scope='function') 
def receipt_data_random():
    data={}
    # bllno_number
    data['BllNo'] = sum(random.sample(range(10000000,999999999),4))
    # receipt money
    data['Money'] = sum(random.sample(range(100,500),2))
    return data









#########################################################################################################@test_001
# mysql select organization_response_data
@pytest.fixture(scope='session')
def organization_response_data():
    return comm_way.sql_select('organization_response_data')


# mysql select table： register_response
@pytest.fixture(scope='session')    
def register_response_data(): 
    return comm_way.sql_select('register_response_data')


# mysql select table： member_page_response_data
@pytest.fixture(scope='session')
def member_page_response_data():
    return comm_way.sql_select('member_page_response_data')


# mysql select table： member_response_data
@pytest.fixture(scope='session')
def member_response_data():
    return comm_way.sql_select('member_response_data')


# mysql select table： vipcard_page_response_data
@pytest.fixture(scope='session')
def vipcard_page_response_data():
    return comm_way.sql_select('vipcard_page_response_data')

# mysql select table： vipcard_response_data
@pytest.fixture(scope='session')
def vipcard_response_data():
    return comm_way.sql_select('vipcard_response_data')


# mysql select table： park_page_response_data
@pytest.fixture(scope='session')    
def park_page_response_data():
    return comm_way.sql_select('park_page_response_data')

# mysql select table： park_rule_page_response_data
@pytest.fixture(scope='session')    
def park_rule_page_response_data():
    return comm_way.sql_select('park_rule_page_response_data')


# mysql select table:  signin_rule_response_data
@pytest.fixture(scope='session')    
def signin_rule_response_data():
    return comm_way.sql_select('signin_rule_response_data')


# mysql select table： upload_advert_response_data
@pytest.fixture(scope='session')    
def upload_advert_response_data():
    return comm_way.sql_select('upload_advert_response_data')


# mysql select table: advert_position_response_data
@pytest.fixture(scope='session')    
def advert_position_response_data():
    return comm_way.sql_select('advert_position_response_data')


#########################################################################################################@test_002
# mysql select table:store_page_response_data
@pytest.fixture(scope='session')    
def store_page_response_data():
    return comm_way.sql_select('store_page_response_data')


# mysql select table:commodity_page_response_data
@pytest.fixture(scope='session')    
def commodity_page_response_data():
    return comm_way.sql_select('commodity_page_response_data')


# mysql select table:commodity_putaway_page_response_data
@pytest.fixture(scope='session')    
def commodity_putaway_page_response_data():
    return comm_way.sql_select('commodity_putaway_page_response_data')


# mysql select table:putaway_commodity_page_response_data
@pytest.fixture(scope='session')    
def putaway_commodity_page_response_data():
    return comm_way.sql_select('putaway_commodity_page_response_data')

#########################################################################################################@test_003
# mysql select table:ticket_type_page_response_data
@pytest.fixture(scope='session')    
def ticket_type_page_response_data():
    return comm_way.sql_select('ticket_type_page_response_data')


# mysql select table:ticket_seed_page_response_data
@pytest.fixture(scope='session')    
def ticket_seed_page_response_data():
    return comm_way.sql_select('ticket_seed_page_response_data')


# mysql select table： ticket_activity_response_data
@pytest.fixture(scope='session')    
def ticket_activity_response_data():
    return comm_way.sql_select('ticket_activity_response_data')
#########################################################################################################@test_004
# mysql select table： integral_rule_response_data
@pytest.fixture(scope='session')    
def integral_rule_response_data():
    return comm_way.sql_select('integral_rule_response_data')

# mysql select table： integral_coefficient_page_response_data
@pytest.fixture(scope='session')    
def integral_coefficient_page_response_data():
    return comm_way.sql_select('integral_coefficient_page_response_data')
#########################################################################################################@test_005
# mysql select table： upload_receipt_s3_response_data
@pytest.fixture(scope='session')    
def upload_receipt_s3_response_data():
    return comm_way.sql_select('upload_receipt_s3_response_data')


# mysql select table： upload_receipt_user_response_data
@pytest.fixture(scope='session')    
def upload_receipt_user_response_data():
    return comm_way.sql_select('upload_receipt_user_response_data')


# mysql select table:shop_commodity_page_response_data
@pytest.fixture(scope='session')    
def shop_commodity_page_response_data():
    return comm_way.sql_select('shop_commodity_page_response_data')


# mysql select table:shop_commodity_response_data
@pytest.fixture(scope='session')    
def shop_commodity_response_data():
    return comm_way.sql_select('shop_commodity_response_data')


# mysql select table: car_data_response_data
@pytest.fixture(scope='session')    
def car_data_response_data():
    return comm_way.sql_select('car_data_response_data')


# mysql select table:park_order_page_response_data
@pytest.fixture(scope='session')    
def park_order_page_response_data():
    return comm_way.sql_select('park_order_page_response_data')
#########################################################################################################@test_006
# mysql select table:shop_order_page_response_data
@pytest.fixture(scope='session')    
def shop_order_page_response_data():
    return comm_way.sql_select('shop_order_page_response_data')


# mysql select table:personal_order_page_response_data
@pytest.fixture(scope='session')    
def personal_order_page_response_data():
    return comm_way.sql_select('personal_order_page_response_data')
#########################################################################################################@test_007
# mysql select table:staff_page_response_data
@pytest.fixture(scope='session')    
def staff_page_response_data():
    return comm_way.sql_select('staff_page_response_data')



