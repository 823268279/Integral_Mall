import pytest
import requests
import sys
import json
import datetime
from comm.comm_way import Way#公共方法
comm_way=Way()

CpnID='0001'
SubID='3378049226@qq.com'
url='http://api.newcrm.group.weixin.wuerp.com/member/v1.0%s'
#短信验证码
# def test_smscode():
#         data={
#                 "cpnID":"",
#                 "SubID":"",
#                 "tel":"13183807891",
#                 }
#         try:
#                 data['CpnID'] = CpnID
#                 data['SubID'] = SubID
#                 response=requests.post(url=url % '/SMS/SendSMSCode',data=data)
#                 print(response.status_code)
#                 print(response.json())
#         except:
#                 raise

        


#会员注册   
def test_menber_register(headers_x):
        #随机openid
        random_openid = comm_way.get_openid()
        #随机会员信息
        random_menber = comm_way.menber_information_random()
        data={
                "CpnID":"",
                "SubID":"",
                "OpnID":"",
                "SMSCode":"0000",#验证码
                "Name":"",
                "OrgID":"",
                "IDSource":"100",
                "UserSource":"",
                "Tel":"13183805656",
                "Eml":"",
                "IDntTp":"",
                "IDntNmb":"",
                "Brth":"2020-06-03",
                "Sex":"1",
                "Prvc":"",
                "City":"",
                "Addr":"",
                "UnionID":"",
                "JsCode":"",
                "EmployeeNumber":"",
                "AppID":"",
                "AppSecret":""
                }
        try:
                data['CpnID'] = CpnID
                data['SubID'] = SubID
                data['OpnID'] = random_openid
                data['Name'] = random_menber[1]
                data['Tel'] = random_menber[2]
                data['Brth'] = random_menber[3]
                response=requests.post(url=url % '/Guest/Register',data=data,headers=headers_x)
                response_json=response.json()
                print(response_json)
                assert response.status_code == 200
                assert response_json['message'] =='注册成功'
                if response_json['data']['Data']:
                        for i in response_json['data']['Data']:
                                print('OPENID：%s' % i['opnID'])
                                print('会员电话：%s' % i['tel'])
                                print('会员卡面号：%s' % i['crdFaceID'])
                                print('会员卡账号：%s' % i['crdID'])
                else:
                        print('没有会员')
                #写入响应数据
                test_data=["test_case","request_way","request_url","request_body","response_body"]
                test_data[0]="会员注册"
                test_data[1]="POST"
                test_data[2]=str(url)
                test_data[3]=str(data)
                test_data[4]=str(response_json)
                comm_way.xlsx_write_way(2,test_data)
        except:
                raise

#获取首页的会员数据
def test_get_index_menber_data(headers_x,menber_register_data):
        data={
                "CpnID":"",
                "SubID":"",
                "gstID":""}

        try:    
                data['CpnID']=CpnID
                data['SubID']=SubID
                data['gstID']=menber_register_data['gstID']
                response=requests.post(url=url % '/Guest/GetMainGst',data=data,headers=headers_x)
                response_json=response.json()
                assert response.status_code == 200
                assert response_json['message'] == "获取成功"
                print('会员卡号：%s' % response_json["data"]['Data']['vipID'])
                print('我的积分%s' % response_json["data"]['Data']['intgAva'])
                print('优惠券%s' % response_json["data"]['Data']['tknQty'])
                print('签到天数：%s' % response_json["data"]['Data']['signInDay'])
        except:
                raise

        
#获取某个会员积分明细
def test_select_integral(headers_x,menber_register_data):  
        data = {
                 "CpnID":"",
                 "crdNo":"",
                 "pageIndex":"1",
                 "pageSize":"10",
                 "sort":"1",
                }
        try:
                data['CpnID'] = CpnID
                data['crdNo'] = menber_register_data['crdFaceID']
                response=requests.post(url=url % '/IntgAct/GetIntgActPage',data=data,headers=headers_x)
                response_json=response.json()
                assert response.status_code == 200
                assert response_json['message'] =='获取数据成功'
                if response_json['data']['PageDataList']:
                        for i in response_json['data']['PageDataList']:
                                print('时间：%s' % i['uptDtt'])
                                print('积分：%s' % i['intgAmt'])
                else:
                        print('没有积分明细')
        except:
                raise

#查询某个会员总积分
def test_select_menber_sum_integral(headers_x,menber_register_data):  
        data={
                "CpnID":"",
                "crdNo":""
        }
        try:
                data['CpnID'] = CpnID
                data['crdNo'] =menber_register_data['crdFaceID']
                response=requests.post(url=url % '/Intg/GetIntgSum',data=data,headers=headers_x)
                response_json=response.json()
                print('会员总积分：%s'% response_json['data']['SumIntg'])
                assert response.status_code == 200
                assert response_json['message'] =='数据更新成功'
        except :
                raise

#获取某个会员的全部卡
def test_select_menber_allcard(headers_x,menber_register_data):  
        data={
                "CpnID":"",
                "SubID":"",
                "opnID":"",
                }
        try:
                data['CpnID']=CpnID
                data['SubID']=SubID
                data['opnID']=menber_register_data['opnID']
                response=requests.post(url=url % '/VipCrd/Get',data=data,headers=headers_x)
                response_json=response.json()
                assert response.status_code == 200
                assert response_json['message'] =='获取数据成功'
                if response_json['data']['Data']:
                        for i in response_json['data']['Data']:
                                print('会员卡号：%s' % i['vipID'])
                else:
                        print('没有会员卡')

        except:
                raise

#根据卡账户获取单张卡
def test_select_only_card(headers_x,menber_register_data):
        data={
                "CpnID":"0001",
                "crdID":"",
                }
        try:
                data['CpnID']=CpnID
                data['crdID']=menber_register_data['crdID']
                response=requests.post(url=url % '/VipCrd/GetByCrdID',data=data,headers=headers_x)
                response_json=response.json()
                assert response.status_code == 200
                assert response_json['message'] =='获取数据成功'
                print('会员卡号：%s' % response_json['data']['Data']['vipID'])
        except:
                raise

class Test_dynamic_code():
        #生成会员动态码
        def test_create_dynamic_code(self,headers_x,menber_register_data):
                data={"CpnID":"0001",   
                        "Code":"",      #卡账号/券账号
                        "Tp":"0",        #帐号类型 0-会员卡、1-优惠券
                        "expires":"5"}   #动态码过期时间(分钟)
                try:
                        data['CpnID']=CpnID
                        data['Code']=menber_register_data['crdID']
                        data['Tp']=0
                        response=requests.post(url=url % '/DynamicCode/GetDynamicCode',data=data,headers=headers_x)
                        response_json=response.json()
                        global response_menber_dynamic_code
                        response_menber_dynamic_code = response_json['data']['dynamicCode']
                        assert response.status_code == 200
                        assert response_json['message'] =='获取数据成功'
                        print('会员动态码：%s' % response_menber_dynamic_code)
                except:
                        raise

        #根据动态码获取会员卡
        def test_check_dynamic_code(self,headers_x):
                data={"DynamicCode":""} #动态码
                try:
                        data['DynamicCode']=response_menber_dynamic_code
                        response=requests.post(url=url % '/DynamicCode/QueryDynamicCode',data=data,headers=headers_x)
                        response_json=response.json()
                        assert response.status_code == 200
                        assert response_json['message'] =='获取数据成功'
                        print('会员卡账号：%s' % response_json['data']['Data'])
                except:
                        raise
class Test_sign_in():
        #签到
        def test_signin(self,headers_x,menber_register_data):
                data={
                        "CpnID":"",
                        "SubID":"",
                        "GstID":"",
                        "VipID":"",
                        "Brf":"apitest"
                        }
                try:
                        data['CpnID']=CpnID
                        data['SubID']=SubID
                        data['GstID']=menber_register_data['gstID']
                        data['VipID']=menber_register_data['crdFaceID']
                        response=requests.post(url=url % '/SignIn/SignIn',data=data,headers=headers_x)
                        response_json=response.json()
                        print(response_json)
                        assert response.status_code == 200
                        assert response_json['message'] =='签到成功'
                except:
                        raise
        #获取签到记录
        def test_signin_record(self,headers_x,menber_register_data):
                data={
                        "CpnID":"",
                        "SubID":"",
                        "gstid":"",
                        "EndTime":""
                        }
                try:
                        data['CpnID']=CpnID
                        data['SubID']=SubID
                        data['gstid']=menber_register_data['gstID']
                        data['EndTime']=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        response=requests.post(url=url % '/SignIn/GetSign',data=data,headers=headers_x)
                        response_json=response.json()
                        assert response.status_code == 200
                        if response_json['data']['Data']:
                                for i in response_json['data']['Data']:
                                        print('签到时间：%s' % i['signTime'])
                                        print('获得积分：%s' % i['integral'])
                        else:
                                print('没有签到记录')
                except:
                        raise

#会员解绑
def test_menber_untie(headers_x):
        data={
                "CpnID":"",
                "SubID":"",
                "Tel":""
                }
        try:
                data['CpnID']=CpnID
                data['SubID']=SubID
                data['Tel']=13183807891
                response=requests.post(url=url % '/Guest/UntieBind',data=data,headers=headers_x)
                response_json=response.json()
                assert response.status_code == 200
                assert response_json['message'] =='解绑成功'
        except:
                raise











































# def test_login():
#         url='http://api.newcrm.group.weixin.wuerp.com/member/v1.0/Guest/Login'
#         data={
#                 "OpnID":"ofcOiw5HWKiiSQAfan-Mg1NyPCGU",
#                 "UnionID":"",
#                 "Tel":"",
#                 "SMSCode":"0000",
#                 "CrdFaceID":"",
#                 "CrdID":"",
#                 "CrmGuestId":"",
#                 "IDTyp":"",
#                 "IsBind":"false",
#                 "IsMember":"false",
#                 "LvlID":"",
#                 "MemberName":"",
#                 "MemberTypID":"",
#                 "OrgID":"",
#                 "JsCode":"",
#                 "AppID":"wx85013334c4606398",
#                 "AppSecret":"8e9f9471396b6592fef575f7a7ccd391",
#                 "SessionKey":"",
#                 "CpnID":"0001",
#                 "SubID":"3378049226@qq.com",
#                 "IsSource":"100",
#                 "GstID":"",
#         }
#         response=requests.post(url=url,data=data)
#         print(response.status_code)
#         print(response.json())


