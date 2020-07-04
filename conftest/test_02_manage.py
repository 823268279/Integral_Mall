import pytest
import requests
import sys
import json
import random
from comm.comm_way import Way#公共方法
comm_way=Way()


class Test_login():
        #后台正确账号和正确密码登录
        def test_login_correct(self,manage,phone_code):
                data={}
                try:
                        data['loginID'] = manage['username']
                        data['loginPwd'] = manage['password']
                        data['checkCode'] = phone_code
                        response=requests.post(url=manage['url'] % '/User/Login',data=data)
                        response_json=response.json()
                        global loginID
                        loginID = response_json['data']['Data']
                        assert response.status_code == 200
                        assert response_json['success'] == True
                except:
                        raise
        #后台正确账号和错误密码登录
        def test_login_error_pwd(self,manage,phone_code):
                data={}
                try:
                        data['loginID'] = manage['username']
                        data['loginPwd'] = '#$%^&***%$#^^%^%$^%$^$^%$%'
                        data['checkCode'] = phone_code
                        response=requests.post(url=manage['url'] % '/User/Login',data=data)
                        response_json=response.json()
                        assert response.status_code == 200
                        assert response_json['Message'] == '帐号或密码错误'
                        print(response_json['Message'])
                except:
                        raise
        #获取用户信息
        def test_get_user_message(self,manage):
                data={}
                try:
                        data['usrFlg'] = loginID
                        response=requests.post(url=manage['url'] % '/User/GetUser',data=data)
                        response_json=response.json()
                        assert response.status_code == 200
                        assert response_json['success'] == True
                except:
                        raise
                


class Test_select_vipdata():
        #查询会员资料分页
        def test_select_menber_data_page(self,headers,manage):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['SubID'] = manage['SubID']
                        data['Name'] = ""
                        data['VipID'] = ""
                        data['pageIndex'] = 1
                        data['pageSize'] = 10
                        data['sort'] = "uptDtt desc"
                        data['Stt'] = ""
                        response=requests.post(url=manage['url'] % '/Gst/GetGstPage',data=data,headers=headers)
                        response_json=response.json()
                        assert response.status_code == 200
                        assert response_json['message'] == "获取数据成功"
                        print(response_json['message'])
                        if response_json['data']['PageDataList']:
                                for i in response_json['data']['PageDataList']:
                                        print('id:%s；name:%s；tel:%s；vipID:%s；' % (i['id'],i['name'],i['tel'],i['vipID']))
                        else:
                                print('没有会员')
                except:
                        raise
        #根据会员姓名查询会员数据
        def test_select_menber_data_page_vipid(self,headers,manage,menber_register_response_data):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['SubID'] = manage['SubID']
                        data['Name'] = menber_register_response_data['crdFaceID']
                        data['VipID'] = ""
                        data['pageIndex'] = 1
                        data['pageSize'] = 10
                        data['sort'] = "uptDtt desc"
                        data['Stt'] = ""
                        response=requests.post(url=manage['url'] % '/Gst/GetGstPage',data=data,headers=headers)
                        response_json=response.json()
                        assert response.status_code == 200
                        assert response_json['message'] == "获取数据成功" 
                        print(response_json['message'])
                        if response_json['data']['PageDataList']:
                                for i in response_json['data']['PageDataList']:
                                        print('id:%s；name:%s；tel:%s；vipID:%s；' % (i['id'],i['name'],i['tel'],i['vipID']))
                        else:
                                print('没有会员')
                except:
                        raise
        #根据会员卡面号查询会员数据
        def test_select_menber_data_page_vipid(self,headers,manage,menber_register_response_data):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['SubID'] = manage['SubID']
                        data['Name'] = ""
                        data['VipID'] = menber_register_response_data['crdFaceID']
                        data['pageIndex'] = 1
                        data['pageSize'] = 10
                        data['sort'] = "uptDtt desc"
                        data['Stt'] = ""
                        response=requests.post(url=manage['url'] % '/Gst/GetGstPage',data=data,headers=headers)
                        response_json=response.json()
                        assert response.status_code == 200
                        assert response_json['message'] == "获取数据成功" 
                        print(response_json['message'])
                        if response_json['data']['PageDataList']:
                                for i in response_json['data']['PageDataList']:
                                        print('id:%s；name:%s；tel:%s；vipID:%s；' % (i['id'],i['name'],i['tel'],i['vipID']))
                        else:
                                print('没有会员')
                except:
                        raise
  
class Test_menber_data():
        #查询会员单个资料
        def test_select_menber_data(self,headers,manage,menber_register_response_data):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data["gstID"] = menber_register_response_data['gstID']
                        print(data)
                        response=requests.post(url=manage['url'] % '/Gst/GetSingerData',data=data,headers=headers)
                        response_json=response.json()
                        assert response.status_code == 200
                        assert response_json['message'] == "获取成功"
                        # mysql insert response data
                        comm_way.sql_insert('menber_data_response',response_json['data']['Data'])
                        print(response_json['message'])
                        if response_json['data']['Data']:
                                print('id:%s；tel:%s；vipID:%s；' % (response_json['data']['Data']['id'],response_json['data']['Data']['tel'],response_json['data']['Data']['vipID']))
                        else:
                                print('没有会员')

                except:
                        raise

        #修改会员信息
        def test_update_menber_data(self,headers,manage,menber_data,menber_data_random):
                data={}
                try:
                        data['ID'] = menber_data['id']
                        data['CpnID'] = menber_data['cpnID']
                        data['UsrFlg'] = menber_data['usrFlg']
                        data['NickName'] = menber_data['nickName']
                        data['Pwd'] = menber_data['pwd']
                        data['PwdDt'] = menber_data['pwdDt']
                        data['Tel'] = menber_data_random['Tel']
                        data['Eml'] = menber_data['eml']
                        data['Name'] = menber_data_random['Name']
                        data['IDntTp'] = '001'
                        data['IDntNmb'] = menber_data_random['IDntNmb']
                        data['VipID'] = menber_data['vipID']
                        data['OrgID'] = menber_data['orgID']
                        data['VipTpID'] = menber_data_random['VipTpID']
                        data['Strvlstt'] = menber_data['strvlstt']
                        data['LastDate'] = menber_data['lastDate']
                        data['RgstApp'] = menber_data['rgstApp']
                        data['Lne'] = menber_data['lne']
                        data['RegstMonth'] = menber_data['regstMonth']
                        data['RgWxMonth'] = menber_data['rgWxMonth']
                        data['Rcmd'] = menber_data['rcmd']
                        data['EcrpBase'] = menber_data['ecrpBase']
                        data['Ecrp1'] = menber_data['ecrp1']
                        data['Ecrp2'] = menber_data['ecrp2']
                        data['IsUpToERP'] = menber_data['isUpToERP']
                        data['Brth'] = menber_data_random['Brth']
                        data['Sex'] = menber_data['sex']
                        data['Mrry'] = menber_data['mrry']
                        data['BabyStt'] = menber_data['babyStt']
                        data['Babydt'] = menber_data['babydt']
                        data['Edu'] = menber_data['edu']
                        data['Ntn'] = menber_data['ntn']
                        data['Prvc'] = menber_data['prvc']
                        data['City'] = menber_data['city']
                        data['Addr'] = menber_data['addr']
                        data['Avt'] = menber_data['avt']
                        data['EmployeeNumber'] = menber_data['employeeNumber']
                        data['RegDt'] = menber_data['regDt']
                        data['Stt'] = menber_data['stt']
                        data['Brf'] = menber_data['brf']
                        data['Uptr'] = menber_data['uptr']
                        data['UptDtt'] = menber_data['uptDtt']
                        data['updateProNames'] = 'tel,Name,IDntTp,IDntNmb,VipTpID,Brth'        #修改字段
                        response=requests.post(url=manage['url'] % '/Gst/Update',data=data,headers=headers)
                        response_json=response.json()
                        print(response_json)
                        assert response.status_code == 200
                        assert response_json['message'] == "修改成功"
                        print(response_json['message'])
                except:
                        raise


class Test_get_vipcard():
        #查询会员卡分页
        def test_get_vipcard_paging(self,headers,manage):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['CrdID'] = ""
                        data['CrdNo'] = ""
                        data['GstID'] = ""
                        data['pageIndex'] = 1
                        data['pageSize'] = 10
                        data['sort'] = "uptDtt desc"
                        response=requests.post(url=manage['url'] % '/VipCrd/GetPageByParam',data=data,headers=headers)
                        response_json=response.json()
                        assert response.status_code == 200
                        assert response_json['message'] =='获取数据成功'
                        print(response_json['message'])
                        if response_json['data']['PageDataList']:
                                for i in response_json['data']['PageDataList']:
                                        print('name:%s；mbl:%s；vipID:%s' % (i['name'],i['mbl'],i['vipID']))
                        else:
                                print('没有会员')
                except:
                        raise

        #根据卡账号查询会员
        def test_get_vipcard_paging_gstid(self,headers,manage,menber_register_response_data):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['CrdID'] = ""
                        data['CrdNo'] = ""
                        data['GstID'] = menber_register_response_data['gstID']
                        data['pageIndex'] = 1
                        data['pageSize'] = 10
                        data['sort'] = "uptDtt desc"
                        response=requests.post(url=manage['url'] % '/VipCrd/GetPageByParam',data=data,headers=headers)
                        response_json=response.json()
                        assert response.status_code == 200
                        assert response_json['message'] =='获取数据成功'
                        print(response_json['message'])
                        if response_json['data']['PageDataList']:
                                for i in response_json['data']['PageDataList']:
                                        print('name:%s；mbl:%s；vipID:%s' % (i['name'],i['mbl'],i['vipID']))
                        else:
                                print('没有会员')
                except:
                        raise
        #根据卡面号查询会员
        def test_get_vipcard_paging_cardface(self,headers,manage,menber_register_response_data):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['CrdID'] = ""
                        data['CrdNo'] = menber_register_response_data['crdFaceID']
                        data['GstID'] = ""
                        data['pageIndex'] = 1
                        data['pageSize'] = 10
                        data['sort'] = "uptDtt desc"
                        response=requests.post(url=manage['url'] % '/VipCrd/GetPageByParam',data=data,headers=headers)
                        response_json=response.json()
                        assert response.status_code == 200
                        assert response_json['message'] =='获取数据成功'
                        print(response_json['message'])
                        if response_json['data']['PageDataList']:
                                for i in response_json['data']['PageDataList']:
                                        print('name:%s；mbl:%s；vipID:%s' % (i['name'],i['mbl'],i['vipID']))
                        else:
                                print('没有会员')
                except:
                        raise
        #根据卡账号查询会员
        def test_get_vipcard_paging_cardid(self,headers,manage,menber_register_response_data):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['CrdID'] = menber_register_response_data['crdID']
                        data['CrdNo'] = ""
                        data['GstID'] = ""
                        data['pageIndex'] = 1
                        data['pageSize'] = 10
                        data['sort'] = "uptDtt desc"
                        response=requests.post(url=manage['url'] % '/VipCrd/GetPageByParam',data=data,headers=headers)
                        response_json=response.json()
                        assert response.status_code == 200
                        assert response_json['message'] =='获取数据成功'
                        print(response_json['message'])
                        if response_json['data']['PageDataList']:
                                for i in response_json['data']['PageDataList']:
                                        print('name:%s；mbl:%s；vipID:%s' % (i['name'],i['mbl'],i['vipID']))
                        else:
                                print('没有会员')
                except:
                        raise


class Test_parking():
        #添加停车场
        def test_add_parking(self,headers,manage,parking_data_random,now_time):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['ID'] = "0"
                        data['ParkID'] = parking_data_random['ParkID']
                        data['PayExplain'] = "apitest"
                        data['Tel'] = parking_data_random['Tel']
                        data['IsSupWXPay'] = 0
                        data['IsSupIntg'] = 0
                        data['IsSupIntgAuto'] = 0
                        data['ParkUrl'] = "0"
                        data['LoginUrl'] = "0"
                        data['BllNoUrl'] = "0"
                        data['ParkUser'] = "0"
                        data['ParkPwd'] = "0"
                        data['ParkKey'] = "0"
                        data['SecretKey'] = "0"
                        data['Uptr'] = manage['username']
                        data['UptDtt'] = now_time['ymd_hms']
                        response=requests.post(url=manage['url'] % '/Park/AddParkConfig',data=data,headers=headers)
                        response_json=response.json()
                        assert response.status_code == 200
                        assert response_json['message'] =='添加成功'
                        print(response_json['message'])
                except:
                        raise

        #获取停车场数据分页
        def test_select_parking_data_page(self,headers,manage):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['ParkID'] = ""
                        data['IsSupWXPay'] = ""
                        data['IsSupIntg'] = ""
                        data['pageIndex'] = 10
                        data['pageSize'] = 1
                        data['sort'] = "uptDtt desc"
                        response=requests.post(url=manage['url'] % '/Park/GetParkConfigPage',data=data,headers=headers)
                        response_json=response.json()
                        # mysql insert response data
                        comm_way.sql_insert('parking_response',response_json['data']['PageDataList'][0])
                        assert response.status_code == 200
                        assert response_json['message'] =='获取数据成功'
                        print(response_json['message'])
                        if response_json['data']['PageDataList']:
                                for i in response_json['data']['PageDataList']:
                                        print('id:%s；parkID:%s；tel:%s；' %(i['id'],i['parkID'],i['tel']))
                        else:
                                print('没有停车场')
                except:
                        raise
        #修改停车场数据
        def test_modify_parking_data(self,headers,manage,parking_data_random,now_time,parking_page_data):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['ID'] = parking_page_data['id']
                        data['ParkID'] = parking_data_random['ParkID']
                        data['PayExplain'] = "apitest"
                        data['Tel'] = parking_data_random['Tel']
                        data['IsSupWXPay'] = 0
                        data['IsSupIntg'] = 0
                        data['IsSupIntgAuto'] = 0
                        data['ParkUrl'] = "0"
                        data['LoginUrl'] = "0"
                        data['BllNoUrl'] = "0"
                        data['ParkUser'] = "0"
                        data['ParkPwd'] = "0"
                        data['ParkKey'] = "0"
                        data['SecretKey'] = "0"
                        data['Uptr'] = manage['username']
                        data['UptDtt'] = now_time['ymd_hms']
                        data['updateName'] = 'ID,CpnID,ParkID,Tel,UptDtt'
                        response=requests.post(url=manage['url'] % '/Park/UpdateParkConfig',data=data,headers=headers)
                        response_json=response.json()
                        assert response.status_code == 200
                        assert response_json['message'] =='修改成功'
                        print(response_json['message'])
                except:
                        raise
        #获取单个停车场数据
        def test_select_parking_data(self,headers,manage,parking_page_data):
                data={}
                try:
                        data['CpnID']=manage['CpnID']
                        data['ID']=parking_page_data['id']
                        response=requests.post(url=manage['url'] % '/Park/GetParkConfigSinger',data=data,headers=headers)
                        response_json=response.json()
                        assert response.status_code == 200
                        assert response_json['message'] =='获取成功'
                        print(response_json['message'])
                        if response_json['data']['Data']:
                                print('id:%s；' % response_json['data']['Data']['id'])
                                print('parkID:%s；' % response_json['data']['Data']['parkID'])
                                print('tel:%s；' % response_json['data']['Data']['tel'])
                        else:
                                print('没有停车场')
                except:
                        raise

        #添加停车场缴费规则
        def test_add_parking_rule(self,headers,manage,now_time,parking_page_data):
                for i in range(1,random.choice(range(3,6))):
                        data={}
                        try:
                                data['CpnID'] = manage['CpnID']
                                data['SubID'] = manage['SubID']
                                data['ID'] = parking_page_data['id']
                                data['ParkID'] = parking_page_data['parkID']
                                data['VipTpID'] = '0%s'% i
                                data['IsEv'] = "0"
                                data['CalculaTyp'] = "0"
                                data['FreeMinute'] = "0"
                                data['StartMinute'] = "0"
                                data['StartMoney'] = "0"
                                data['StartIntg'] = "0"
                                data['StartGold'] = "0"
                                data['IntrvalTime'] = "5"
                                data['IntrvalMoney'] = "5"
                                data['IntrvalIntg'] = "5"
                                data['IntrvalGold'] = "5"
                                data['ConsumMoney'] = "0"
                                data['ConsFreeMinute'] = "0"
                                data['IntgSupportHour'] = "0"
                                data['Uptr'] = manage['username']
                                data['UptDtt'] = now_time['ymd_hms']
                                response=requests.post(url=manage['url'] % '/Park/AddParkRule',data=data,headers=headers)
                                response_json=response.json()
                                assert response.status_code == 200
                                assert response_json['message'] =='添加成功'
                                print(response_json['message'])
                        except:
                                raise
        #获取停车场缴费规则分页
        def test_get_parking_rule_page(self,headers,manage,parking_page_data):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['ParkID'] = parking_page_data['parkID']
                        data['pageIndex'] = 1
                        data['pageSize'] = 10
                        data['sort'] = "uptDtt desc"
                        response=requests.post(url=manage['url'] % '/Park/GetParkRulePage',data=data,headers=headers)
                        response_json=response.json()
                        # mysql insert response data
                        comm_way.sql_insert('parking_rule_response',response_json['data']['PageDataList'][0])
                        assert response.status_code == 200
                        assert response_json['message'] =='获取数据成功'
                        print(response_json['message'])
                        if response_json['data']['PageDataList']:
                                for i in response_json['data']['PageDataList']:
                                        print('id:%s；parkID:%s；vipTPID:%s；' % (i['id'],i['parkID'],i['vipTpID']))
                        else:
                                print('没有停车场缴费规则')
                except:
                        raise
        #获取停车场缴费规则单条
        def test_get_parking_rule(self,headers,manage,parking_rule_page_data):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['id'] = parking_rule_page_data['id']
                        response=requests.post(url=manage['url'] % '/Park/GetParkRuleSinger',data=data,headers=headers)
                        response_json=response.json()
                        assert response.status_code == 200
                        assert response_json['message'] =='获取成功'
                        print(response_json['message'])
                        if response_json['data']['Data']:
                                print('id:%s；' % response_json['data']['Data']['id'])
                                print('parkID:%s；' % response_json['data']['Data']['parkID'])
                                print('vipTpID:%s；' % response_json['data']['Data']['vipTpID'])
                        else:
                                print('没有停车场')
                except:
                        raise
        # 修改停车场缴费规则
        def test_update_parking_rule(self,headers,manage,now_time,parking_rule_page_data,parking_data_random):
                data={}
                try:
                        data['ID']=parking_rule_page_data['id']
                        data['CpnID']=parking_rule_page_data['cpnID']
                        data['SubID']=parking_rule_page_data['subID']
                        data['ParkID']=parking_data_random['ParkID']
                        data['VipTpID']='02'
                        data['IsEv']=parking_rule_page_data['isEv']
                        data['CalculaTyp']=parking_rule_page_data['calculaTyp']
                        data['FreeMinute']=parking_rule_page_data['freeMinute']
                        data['StartMinute']=parking_rule_page_data['startMinute']
                        data['StartMoney']=parking_rule_page_data['startMoney']
                        data['StartIntg']=parking_rule_page_data['startIntg']
                        data['StartGold']=parking_rule_page_data['startGold']
                        data['IntrvalTime']=parking_rule_page_data['intrvalTime']
                        data['IntrvalMoney']=parking_rule_page_data['intrvalMoney']
                        data['IntrvalIntg']=parking_rule_page_data['intrvalIntg']
                        data['IntrvalGold']=parking_rule_page_data['intrvalGold']
                        data['ConsumMoney']=parking_rule_page_data['consumMoney']
                        data['ConsFreeMinute']=parking_rule_page_data['consFreeMinute']
                        data['IntgSupportHour']=parking_rule_page_data['intgSupportHour']
                        data['Uptr']=parking_rule_page_data['uptr']
                        data['UptDtt']=now_time['ymd_hms']
                        data['updateName']='ParkID'
                        response=requests.post(url=manage['url'] % '/Park/UpdateParkRule',data=data,headers=headers)
                        response_json=response.json()
                        assert response.status_code == 200
                        assert response_json['message'] =='修改成功'
                        print(response_json['message'])
                except:
                        raise


#系统配置表
class Test_system_config():
        #查询系统配置分页
        def test_get_system_config_page(self,headers,manage):
                data={}
                try:    
                        data['CpnID'] = manage['CpnID']
                        data['SubID'] = manage['SubID']
                        data['Code'] = ""
                        data['PageIndex'] = 1
                        data['PageSize'] = 10
                        data['Sort'] = "id"
                        response=requests.post(url=manage['url'] % '/SysPara/GetSysParaPage',data=data,headers=headers)
                        response_json=response.json()
                        global response_system_config
                        response_system_config=response_json['data']['PageDataList']
                        assert response.status_code == 200
                        assert response_json['message'] =='获取数据成功'
                        print(response_json['message'])
                        if response_system_config:
                                for i in response_system_config:
                                        print('id:%s；code:%s；name:%s；crtVl:%s' % (i['id'],i['code'],i['name'],i['crtVl']))
                        else:
                                print('没有系统配置')
                except:
                        raise
        #修改wifi密码
        def test_update_wifi_password(self,headers,manage):
                data=response_system_config[1]
                try:
                        data['crtVl']='66668888'
                        data['updateProNames']='crtVl'  #修改字段
                        response=requests.post(url=manage['url'] % '/SysPara/Update',data=data,headers=headers)
                        response_json=response.json()
                        assert response.status_code == 200
                        assert response_json['message'] =='修改成功'       
                        print(response_json['message'])            
                except:
                        raise
        #获取wifi配置信息
        def test_get_system_config_wifi(self,headers,manage):
                data={}
                try:
                        data['id']=response_system_config[1]['id']
                        response=requests.post(url=manage['url'] % '/SysPara/Get',data=data,headers=headers)
                        response_json=response.json()
                        assert response.status_code == 200
                        assert response_json['message'] =='获取成功'
                        print(response_json['message'])
                        print('id:%s；' % response_json['data']['Data']['id'])
                        print('code:%s；' % response_json['data']['Data']['code'])
                        print('name:%s；' % response_json['data']['Data']['name'])
                        print('crtVl:%s；'% response_json['data']['Data']['crtVl'])
                    
                except:
                        raise

                
#添加签到规则
def test_add_signin_rule(headers,manage,now_time):
        data={}
        try:    
                data['CpnID'] = manage['CpnID']
                data['SubID'] = manage['SubID']
                data['ID'] = "0"
                data['Typ'] = "1"       #赠送类型[0-金币、1-积分]  
                data['Days'] = "1"      #累积达到天数赠送 
                data['Integral'] = "20" #赠送值
                data['LngValid'] = "1"  #是否长期有效[0-是、1-否]
                data['IsStop'] = "0"    #是否终止[0-正常、1-终止]
                data['StDt'] = now_time['StDt']
                data['EdDt'] = now_time['EdDt']
                data['Brf'] = "apitest"
                data['Uptr'] = manage['username']
                data['UptDtt'] = now_time['ymd_hms']
                response=requests.post(url=manage['url'] % '/SignInRules/AddSignInRules',data=data,headers=headers)
                response_json=response.json()
                print(response_json)
                assert response.status_code == 200
                assert response_json['Message'] =='添加成功'
                print(response_json['Message'])
        except:
                raise




#获取签到规则分页
def test_get_signin_rule_page(headers,manage):
        data={}
        try:    
                data['CpnID'] = manage['CpnID']
                data['SubID'] = manage['SubID']
                data['Typ'] = "-99"       #赠送类型[0-金币、1-积分]  
                data['Days'] = ""      #累积达到天数赠送 
                data['Integral'] = "" #赠送值
                data['LngValid'] = "-99"  #是否长期有效[0-是、1-否]
                data['IsStop'] = "-99"    #是否终止[0-正常、1-终止]
                data['StDt'] = ""
                data['EdDt'] = ""
                data['PgIndex'] = 1
                data['PgSize'] = 10
                print(data)
                response=requests.post(url=manage['url'] % '/SignInRules/GetWhereSignInRules',data=data,headers=headers)
                response_json=response.json()
                print(response_json)
                assert response.status_code == 200
        except:
                raise


    











