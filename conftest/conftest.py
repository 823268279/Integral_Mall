#coding=utf-8


from openpyxl import load_workbook
import datetime
from py._xmlgen import html
import pytest
import requests
import json


# 添加接口地址与项目名称
def pytest_configure(config):
    config._metadata["项目名称"] = "NEW_CRM_v1.0"
    config._metadata['测试地址'] = 'http://api.newcrm.group.weixin.wuerp.com'
# 添加所属部门与测试人员
@pytest.mark.optionalhook
def pytest_html_results_summary(prefix):
    prefix.extend([html.p("所属部门: 测试部")])
    prefix.extend([html.p("测试人员: wowo")])



@pytest.fixture(scope='session')    
def headers_x():
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
        headers={}
        headers['Authorization']=response_json['data']['Data']['token']
        return headers
    except:
        raise
    



#读取excel数据
def xlsx_read_way():
    __file__ = r'../test_data/2020-05-09-09-27_test_data.xlsx'
    workbook=load_workbook(__file__)
    worksheet=workbook['Sheet1']
    return worksheet
@pytest.fixture(scope='session')    
def menber_register_data():
    #获取会员手机注册资料
    response_menber_register=eval(xlsx_read_way().cell(2,6).value,{"true":"0","false":"0"})['data']['Data'][0]
    return response_menber_register

@pytest.fixture(scope='session')    
def menber():
    data={
        "CpnID":'0001',
        "SubID":'3378049226@qq.com',
        "url":'http://api.newcrm.group.weixin.wuerp.com/member/v1.0%s'
        }
    
    return data

def manage():
    data={
        "CpnID":'0001',
        "SubID":'3378049226@qq.com',
        "url":'http://api.newcrm.group.weixin.wuerp.com/manage/v1.0%s'
        }
    return data