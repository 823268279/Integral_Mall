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
                        response_json = comm_way.response_dispose(response.json())
                        global loginID
                        loginID = response_json['Data']['Data']
                        assert response.status_code == 200
                        assert response_json['Success'] == True
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
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == False
                        
                except:
                        raise
                
        #获取用户信息
        def test_get_user_message(self,manage):
                data={}
                try:
                        data['usrFlg'] = loginID
                        response=requests.post(url=manage['url'] % '/User/GetUser',data=data)
                        response_json = comm_way.response_dispose(response.json())
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                except:
                        raise

class Test_menber_select():
        #查询会员单个资料
        def test_get_menber_data(self,headers,manage,menber_register_response_data):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data["gstID"] = menber_register_response_data['gstID']
                        response=requests.post(url=manage['url'] % '/Gst/GetSingerData',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])  
                        assert response.status_code == 200
                        assert response_json['Success'] == True    
                        # mysql insert response data
                        comm_way.sql_insert('menber_data_response',response_json['Data']['Data'])
                        print(response_json['Data']['Data'])
                except:
                        raise

        #修改会员信息
        def test_update_menber_data(self,headers,manage,menber_select_response_data,menber_data_random):
                data={}
                try:
                        data['ID'] = menber_select_response_data['id']
                        data['CpnID'] = menber_select_response_data['cpnID']
                        data['UsrFlg'] = menber_select_response_data['usrFlg']
                        data['NickName'] = menber_select_response_data['nickName']
                        data['Pwd'] = menber_select_response_data['pwd']
                        data['PwdDt'] = menber_select_response_data['pwdDt']
                        data['Tel'] = menber_data_random['Tel']
                        data['Eml'] = menber_select_response_data['eml']
                        data['Name'] = menber_data_random['Name']
                        data['IDntTp'] = '001'
                        data['IDntNmb'] = menber_data_random['IDntNmb']
                        data['VipID'] = menber_select_response_data['vipID']
                        data['OrgID'] = menber_select_response_data['orgID']
                        data['VipTpID'] = menber_data_random['VipTpID']
                        data['Strvlstt'] = menber_select_response_data['strvlstt']
                        data['LastDate'] = menber_select_response_data['lastDate']
                        data['RgstApp'] = menber_select_response_data['rgstApp']
                        data['Lne'] = menber_select_response_data['lne']
                        data['RegstMonth'] = menber_select_response_data['regstMonth']
                        data['RgWxMonth'] = menber_select_response_data['rgWxMonth']
                        data['Rcmd'] = menber_select_response_data['rcmd']
                        data['EcrpBase'] = menber_select_response_data['ecrpBase']
                        data['Ecrp1'] = menber_select_response_data['ecrp1']
                        data['Ecrp2'] = menber_select_response_data['ecrp2']
                        data['IsUpToERP'] = menber_select_response_data['isUpToERP']
                        data['Brth'] = menber_data_random['Brth']
                        data['Sex'] = menber_select_response_data['sex']
                        data['Mrry'] = menber_select_response_data['mrry']
                        data['BabyStt'] = menber_select_response_data['babyStt']
                        data['Babydt'] = menber_select_response_data['babydt']
                        data['Edu'] = menber_select_response_data['edu']
                        data['Ntn'] = menber_select_response_data['ntn']
                        data['Prvc'] = menber_select_response_data['prvc']
                        data['City'] = menber_select_response_data['city']
                        data['Addr'] = menber_select_response_data['addr']
                        data['Avt'] = menber_select_response_data['avt']
                        data['EmployeeNumber'] = menber_select_response_data['employeeNumber']
                        data['RegDt'] = menber_select_response_data['regDt']
                        data['Stt'] = menber_select_response_data['stt']
                        data['Brf'] = menber_select_response_data['brf']
                        data['Uptr'] = menber_select_response_data['uptr']
                        data['UptDtt'] = menber_select_response_data['uptDtt']
                        data['updateProNames'] = 'tel,Name,IDntTp,IDntNmb,VipTpID,Brth'        #修改字段
                        response=requests.post(url=manage['url'] % '/Gst/Update',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True                      
                        
                except:
                        raise


class Test_select_vipdata():
        #查询会员资料分页
        def test_get_menber_data_page(self,headers,manage):
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
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True                        
                        if response_json['Data']['PageDataList']:
                                for i in response_json['Data']['PageDataList']:
                                        print(i)
                        else:
                                print('没有会员')
                except:
                        raise
        #根据会员姓名查询会员数据
        def test_get_menber_data_page_name(self,headers,manage,menber_select_response_data):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['SubID'] = manage['SubID']
                        data['Name'] = menber_select_response_data['name']
                        data['VipID'] = ""
                        data['pageIndex'] = 1
                        data['pageSize'] = 10
                        data['sort'] = "uptDtt desc"
                        data['Stt'] = ""
                        response=requests.post(url=manage['url'] % '/Gst/GetGstPage',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        if response_json['Data']['PageDataList']:
                                for i in response_json['Data']['PageDataList']:
                                        print(i)
                        else:
                                print('没有会员')
                except:
                        raise
        #根据会员卡面号查询会员数据
        def test_get_menber_data_page_vipid(self,headers,manage,menber_data_response):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['SubID'] = manage['SubID']
                        data['Name'] = ""
                        data['VipID'] = menber_data_response['vipID']
                        data['pageIndex'] = 1
                        data['pageSize'] = 10
                        data['sort'] = "uptDtt desc"
                        data['Stt'] = ""
                        response=requests.post(url=manage['url'] % '/Gst/GetGstPage',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        if response_json['Data']['PageDataList']:
                                for i in response_json['Data']['PageDataList']:
                                        print(i)
                        else:
                                print('没有会员')
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
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        print(response_json)
                        assert response.status_code == 200
                        assert response_json['Success'] == True                       
                        if response_json['Data']['PageDataList']:
                                for i in response_json['Data']['PageDataList']:
                                        print(i)
                        else:
                                print('没有会员')
                except:
                        raise

        #根据会员ID查询会员
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
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True                       
                        if response_json['Data']['PageDataList']:
                                for i in response_json['Data']['PageDataList']:
                                        print(i)
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
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True                       
                        if response_json['Data']['PageDataList']:
                                for i in response_json['Data']['PageDataList']:
                                        print(i)
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
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True                       
                        if response_json['Data']['PageDataList']:
                                for i in response_json['Data']['PageDataList']:
                                        print(i)
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
                        data['ParkID'] = parking_data_random['ParkID']          #停车场编号
                        data['PayExplain'] = "apitest"                          #缴费说明
                        data['Tel'] = parking_data_random['Tel']                #故障热线
                        data['IsSupWXPay'] = 0                                  #是否支持微信支持(0-支持，1-不支持)
                        data['IsSupIntg'] = 0                                   #是否支持积分(0-支持，1-不支持)
                        data['IsSupIntgAuto'] = 0                               #是否支持积分自动扣除(0-支持，1-不支持)
                        data['ParkUrl'] = "0"                                    #停车系统url
                        data['LoginUrl'] = "0"                                   #获取令牌url
                        data['BllNoUrl'] = "0"                                   #获取订单号url
                        data['ParkUser'] = "0"                                   #账号
                        data['ParkPwd'] = "0"                                    #密码
                        data['ParkKey'] = "0"
                        data['SecretKey'] = "0"
                        data['Uptr'] = manage['username']
                        data['UptDtt'] = now_time['ymd_hms']
                        print(data)
                        response=requests.post(url=manage['url'] % '/Park/AddParkConfig',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True                     
                except:
                        raise

        #获取停车场数据分页
        def test_get_parking_data_page(self,headers,manage):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['ParkID'] = ""
                        data['IsSupWXPay'] = ""
                        data['IsSupIntg'] = ""
                        data['pageIndex'] = 1
                        data['pageSize'] = 10
                        data['sort'] = "uptDtt desc"
                        response=requests.post(url=manage['url'] % '/Park/GetParkConfigPage',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True                       
                        if response_json['Data']['PageDataList']:
                                # mysql insert response data
                                comm_way.sql_insert('parking_response',response_json['Data']['PageDataList'][0])
                                for i in response_json['Data']['PageDataList']:
                                        print(i)
                        else:
                                print('没有停车场')
                except:
                        raise
        #修改停车场数据
        def test_update_parking_data(self,headers,manage,parking_data_random,now_time,parking_page_data):
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
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True                     
                except:
                        raise
        #获取单个停车场数据
        def test_get_parking_data(self,headers,manage,parking_page_data):
                data={}
                try:
                        data['CpnID']=manage['CpnID']
                        data['ID']=parking_page_data['id']
                        response=requests.post(url=manage['url'] % '/Park/GetParkConfigSinger',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True    
                        print(response_json['Data']['Data'])                 
                except:
                        raise

class Test_park_rule():
        #添加停车场缴费规则
        def test_add_parking_rule(self,headers,manage,now_time,parking_page_data):
                for i in range(1,random.choice(range(3,6))):
                        data={}
                        try:
                                data['CpnID'] = manage['CpnID']
                                data['SubID'] = manage['SubID']
                                data['ID'] = parking_page_data['id']
                                data['ParkID'] = parking_page_data['parkID']    #停车场编号
                                data['VipTpID'] = '0%s'% i                      #会员类型ID
                                data['IsEv'] = "0"                              #是否是新能源车牌(0-所有车型，1-新能源车票)
                                data['CalculaTyp'] = "0"                        #计算类型(0-按次数计算，1-按时长计算)
                                data['FreeMinute'] = "0"                        #免费时长(多少分钟内免费)
                                data['StartMinute'] = "0"                       #起步时长
                                data['StartMoney'] = "5"                        #起步金额
                                data['StartIntg'] = "0"                         #起步积分
                                data['StartGold'] = "0"                         #起步金币
                                data['IntrvalTime'] = "5"                       #单价时间
                                data['IntrvalMoney'] = "5"                      #单价金额
                                data['IntrvalIntg'] = "5"                       #单价积分
                                data['IntrvalGold'] = "5"                       #单价金币
                                data['ConsumMoney'] = "0"                       #消费金额线
                                data['ConsFreeMinute'] = "0"                    #优惠时长
                                data['IntgSupportHour'] = "0"
                                data['Uptr'] = manage['username']
                                data['UptDtt'] = now_time['ymd_hms']
                                response=requests.post(url=manage['url'] % '/Park/AddParkRule',data=data,headers=headers)
                                response_json = comm_way.response_dispose(response.json())
                                print(response_json['Message'])
                                assert response.status_code == 200
                                assert response_json['Success'] == True                        
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
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True                       
                        if response_json['Data']['PageDataList']:
                                # mysql insert response data
                                comm_way.sql_insert('parking_rule_response',response_json['Data']['PageDataList'][0])
                                for i in response_json['Data']['PageDataList']:
                                        print(i)
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
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True     
                        print(response_json['Data']['Data'])  
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
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True                     
                except:
                        raise
# 停车订单
class Test_park_order():
        # 新增停车订单
        def test_add_park_order(self,headers,manage,car_data_response_data,now_time,park_order_data_random):
                data={}
                try:    
                        data['CpnID'] = manage['CpnID']
                        data['SubID'] = manage['SubID']
                        data['JoinDt'] = park_order_data_random['JoinDt'] #入场时间
                        data['ParkDt'] = '0'                              #停车时长
                        data['LeaveDt'] = ''                              #离场时间
                        data['PayTyp'] = '0'                              #支付方式(1-微信支付，1-积分支付，)
                        data['PayMoney'] = '0'                            #支付金额(PayTyp=0有效)
                        data['PayIntg'] = '0'                             #支付积分(PayTyp=1有效)
                        data['PayGold'] = '0'                             #支付金币(PayTyp=2有效)
                        data['GstID'] = car_data_response_data['gstID']
                        data['CarNum'] = car_data_response_data['carID']#车牌号
                        data['BllNo'] = park_order_data_random['BllNo']                        #订单号
                        data['Stt'] = 0                                 #状体(0-录入，50-成功)
                        data['Deleted'] = '0'
                        data['Uptr'] = manage['username']
                        data['UptDtt'] = now_time['ymd_hms']
                        data['PgIndex'] = 0
                        data['PgSize'] = 0
                        data['MemberTypID'] = '01'
                        response=requests.post(url=manage['url'] % '/Park/AddParkOrder',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True    
                        print(response_json['Data']['Data'])                   
                except:
                        raise

        # 查询订单分页
        def test_get_parking_order_page(self,manage,headers):
                data={}
                try:    
                        data['ID'] = ''
                        data['CpnID'] = manage['CpnID']
                        data['SubID'] = manage['SubID']
                        data['JoinDt'] = ''
                        data['ParkDt'] ='0'
                        data['LeaveDt'] = ''
                        data['PayTyp'] =  '0'                        
                        data['PayMoney'] =  '0'                    
                        data['PayIntg'] = '0'                    
                        data['PayGold'] = '0'                     
                        data['GstID'] = ''
                        data['CarNum'] = ''
                        data['BllNo'] =  ''                 
                        data['Stt'] = '0'                          
                        data['Deleted'] = ''
                        data['Uptr'] = ''
                        data['UptDtt'] = ''
                        data['PgIndex'] = 1
                        data['PgSize'] = 10
                        data['MemberTypID'] = ''
                        response=requests.post(url=manage['url'] % '/Park/GetParkOrderAll',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json)
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True                       
 
                        # if response_system_config:
                        #         for i in response_system_config:
                        #                 print(i)
                        # else:
                        #         print('没有停车订单')
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
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True                       
                        global response_system_config
                        response_system_config=response_json['Data']['PageDataList']
                        if response_system_config:
                                for i in response_system_config:
                                        print(i)
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
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])   
                        assert response.status_code == 200
                        assert response_json['Success'] == True            
                except:
                        raise
        #获取wifi配置信息
        def test_get_system_config_wifi(self,headers,manage):
                data={}
                try:
                        data['id']=response_system_config[1]['id']
                        response=requests.post(url=manage['url'] % '/SysPara/Get',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True     
                        print(response_json['Data']['Data'])
                except:
                        raise


class Test_signin():
        #添加签到规则
        def test_add_signin_rule(self,headers,manage,now_time):
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
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True                     
                except:
                        raise
        #获取签到规则分页
        def test_get_signin_rule_page(self,headers,manage):
                data={}
                try:    
                        data['CpnID'] = manage['CpnID']
                        data['SubID'] = manage['SubID']
                        data['Typ'] = "-99"       #赠送类型 
                        data['Days'] = ""      #累积达到天数赠送 
                        data['Integral'] = "" #赠送值
                        data['LngValid'] = "-99"  #是否长期有效
                        data['IsStop'] = "-99"    #是否终止
                        data['StDt'] = ""
                        data['EdDt'] = ""
                        data['PgIndex'] = 1
                        data['PgSize'] = 12
                        data['Stt '] = '-99'
                        print(data)
                        response=requests.post(url=manage['url'] % '/SignInRules/GetWhereSignInRules',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True                       
                        if response_json['Data']['PageDataList']:
                                for i in response_json['Data']['PageDataList']:
                                        # mysql insert response data
                                        comm_way.sql_insert('signin_rule_response',response_json['Data']['PageDataList'][0]) 
                                        print(i)
                        else:
                                print('没有签到规则')
                except:
                        raise
        # 修改签到规则
        def test_update_signin_rule(self,headers,manage,signin_rule_response_data,now_time):
                data={}
                try:    
                        data['CpnID'] = manage['CpnID']
                        data['SubID'] = manage['SubID']
                        data['ID'] = signin_rule_response_data['id']
                        data['Typ'] = signin_rule_response_data['typ']       #赠送类型[0-金币、1-积分]  
                        data['Days'] = signin_rule_response_data['days']      #累积达到天数赠送 
                        data['Integral'] = "3000000"                                 #赠送值
                        data['LngValid'] = signin_rule_response_data['lngValid']  #是否长期有效[0-是、1-否]
                        data['IsStop'] = signin_rule_response_data['isStop']    #是否终止[0-正常、1-终止]
                        data['StDt'] = now_time['StDt']
                        data['EdDt'] = now_time['EdDt']
                        data['Stt'] = '50'
                        data['Brf'] = "apitest update"
                        data['Uptr'] = manage['username']
                        data['UptDtt'] = now_time['ymd_hms']
                        data['parm'] = 'Integral,Stt'
                        print(data)
                        response=requests.post(url=manage['url'] % '/SignInRules/UpSignInRules',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json)
                        print(response_json['Message'])
                        response_json = comm_way.response_dispose(response.json())
                        assert response.status_code == 200
                        assert response_json['Success'] == True  
                except:
                        raise
        
        # 获取单个签到规则
        def test_get_signin_rule(self,headers,manage,signin_rule_response_data):
                data={}
                try:    
                        data['CpnID'] = manage['CpnID']
                        data['SubID'] = manage['SubID']
                        data['ID'] = signin_rule_response_data['id']
                        response=requests.post(url=manage['url'] % '/SignInRules/GetSignInRules',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True                    
                        if response_json['Data']['Data']:
                                for i in response_json['Data']['Data']:
                                        print(i)
                        else:
                                print('没有签到规则')
                except:
                        raise

class Test_advert():
        #上传广告到s3
        def test_upload_advert_s3(self,headers,menber,get_s3_advert):   
                data={}
                try:
                        data['CpnID'] = menber['CpnID']
                        response=requests.post(url=menber['url'] % '/Guest/UnloadPic',files=get_s3_advert['ticket'],data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True                     
                        # mysql insert response data
                        comm_way.sql_insert('upload_advert_response',response_json['Data'])
                except:
                        raise 
        #添加广告位
        def test_add_advert_position(self,headers,manage,now_time,upload_advert_response_data):
                data={}
                data_sublist={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['SubID'] = manage['SubID']
                        data['ID'] = '0'
                        data['Name'] = '浪漫热夏'       #广告位名称
                        data['KyWrd'] = ''              #关键词
                        data['ShwPosi'] = '1'           #显示位置代码
                        data['Clms'] = '1'              #显示列数
                        data['AdWidth'] = '0'           #广告位宽度
                        data['AdHeight'] = '0'          #广告位高度
                        data['AdTyp'] = '0'             #类型（0-手机端，1-pc端）
                        data['OpnTyp'] = '0'            #打开方式（0-当前页，-1-新开窗口）
                        data['Stt'] = '0'               #状态（0-启用，-1关闭）
                        data['StDt'] = now_time['StDt'] #为空立即生效
                        data['EdDt'] = now_time['EdDt'] #为空则无过期时间
                        data['Brf'] = 'apitest'
                        data['Deleted'] = 'N'           #（N-正常，Y-删除）
                        data['Uptr'] = manage['username']
                        data['UptDtt'] = now_time['ymd_hms']
                        data_sublist['ID'] = '1'
                        data_sublist['CpnID'] = manage['CpnID']
                        data_sublist['SubID'] = manage['SubID']
                        data_sublist['Name'] = '浪漫热夏'
                        data_sublist['AdPosiID'] = '0'
                        data_sublist['AdText'] = ''
                        data_sublist['KyWrd'] = ''
                        data_sublist['Rdx'] = '0'
                        data_sublist['StDt'] = now_time['StDt']
                        data_sublist['EdDt'] = now_time['EdDt']
                        data_sublist['AdTyp'] = '4'     #类型（0-品牌，1-分类，2-商品，3-店铺，4-广告内容）
                        data_sublist['Intro'] = upload_advert_response_data['Data']
                        data_sublist['ShwTyp'] = '0'    #显示方式（0-图片，1-文字，2-网页，3-视频）
                        data_sublist['IsShw'] = '0'     #（0-显示，1-隐藏）
                        data_sublist['Stt'] = '50'      #（-1-作废，0-录入，50-审核通过）
                        data_sublist['CrtUsr'] = '0' 
                        data_sublist['CrtDt'] = now_time['ymd_hms']
                        data_sublist['Brf'] = 'apitest'
                        data_sublist['Deleted'] = 'N'   #（N-正常，Y-删除）
                        data_sublist['Uptr'] = '0'
                        data_sublist['UptDtt'] = now_time['ymd_hms']
                        data['List']=[]
                        data['List'].append(data_sublist)
                        print(data)
                        response=requests.post(url=manage['url'] % '/AdPosi/Add',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True             
                except:
   
                        raise 
        #查询广告位分页
        def test_get_advert_position_page(self,headers,manage):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['SubID'] = manage['SubID']
                        data['Name'] = ''
                        data['ShowPosi'] = ''
                        data['AdTyp'] = ''
                        data['Stt'] = ''
                        data['PageIndex'] = '1'
                        data['PageSize'] = '10'
                        data['Sort'] = 'uptDtt desc'
                        response=requests.post(url=manage['url'] % '/AdPosi/GetAdPosiPage',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True                       
                        if response_json['Data']['PageDataList']:
                                for i in response_json['Data']['PageDataList']:
                                        # mysql insert response data
                                        comm_way.sql_insert('advert_position_response',response_json['Data']['PageDataList'][0])
                                        print(i)
                        else:
                                print('没有广告位')
                except:
                        raise
        # # 修改广告位 
        # def test_update_advert_position(self,now_time,headers,manage,advert_position_response_data,upload_advert_response_data):
        #         data={}
        #         data_sublist={}
        #         try:
        #                 data['CpnID'] = manage['CpnID']
        #                 data['SubID'] = manage['SubID']
        #                 data['ID'] = advert_position_response_data['id']
        #                 data['Name'] = '清凉一夏'       #广告位名称
        #                 data['KyWrd'] = ''              #关键词
        #                 data['ShwPosi'] = '1'            #显示位置代码
        #                 data['Clms'] = '1'              #显示列数
        #                 data['AdWidth'] = '0'           #广告位宽度
        #                 data['AdHeight'] = '0'          #广告位高度
        #                 data['AdTyp'] = '0'             #类型（0-手机端，1-pc端）
        #                 data['OpnTyp'] = '0'            #打开方式（0-当前页，-1-新开窗口）
        #                 data['Stt'] = '0'               #状态（0-启用，-1关闭）
        #                 data['StDt'] = now_time['StDt'] #为空立即生效
        #                 data['EdDt'] = now_time['EdDt'] #为空则无过期时间
        #                 data['Brf'] = 'apitest'
        #                 data['Deleted'] = 'N'           #（N-正常，Y-删除）
        #                 data['Uptr'] = manage['username']
        #                 data['UptDtt'] = now_time['ymd_hms']
        #                 data_sublist['ID'] = '1'
        #                 data_sublist['CpnID'] = manage['CpnID']
        #                 data_sublist['SubID'] = manage['SubID']
        #                 data_sublist['Name'] = '清凉一夏'
        #                 data_sublist['AdPosiID'] = '0'
        #                 data_sublist['AdText'] = ''
        #                 data_sublist['KyWrd'] = ''
        #                 data_sublist['Rdx'] = '0'
        #                 data_sublist['StDt'] = now_time['StDt']
        #                 data_sublist['EdDt'] = now_time['EdDt']
        #                 data_sublist['AdTyp'] = '4'     #类型（0-品牌，1-分类，2-商品，3-店铺，4-广告内容）
        #                 data_sublist['Intro'] = upload_advert_response_data['Data']
        #                 data_sublist['ShwTyp'] = '0'    #显示方式（0-图片，1-文字，2-网页，3-视频）
        #                 data_sublist['IsShw'] = '0'     #（0-显示，1-隐藏）
        #                 data_sublist['Stt'] = '50'      #（-1-作废，0-录入，50-审核通过）
        #                 data_sublist['CrtUsr'] = '0' 
        #                 data_sublist['CrtDt'] = now_time['ymd_hms']
        #                 data_sublist['Brf'] = 'apitest'
        #                 data_sublist['Deleted'] = 'N'   #（N-正常，Y-删除）
        #                 data_sublist['Uptr'] = '0'
        #                 data_sublist['UptDtt'] = now_time['ymd_hms']
        #                 data['List']=[]
        #                 data['List'].append(data_sublist)
        #                 data['UpdateProNames'] = 'Name,StDt,EdDt,list'     #修改字段
        #                 print(data)
        #                 response=requests.post(url=manage['url'] % '/AdPosi/Update',data=data,headers=headers)
        #                 response_json = comm_way.response_dispose(response.json())
        #                 print(response_json)
        #                 print(response_json['Message'])
        #                 assert response.status_code == 200
        #                 assert response_json['Success'] == True     
        #         except:
 
        #                 raise
        # 获取单个广告位
        def test_get_advert_position(self,headers,manage,advert_position_response_data):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['id'] = advert_position_response_data['id']
                        print(data)
                        response=requests.post(url=manage['url'] % '/AdPosi/Get',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json)
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        list=[]
                        list.append(response_json['Data']['AdPosi'])
                        for i in list:
                                print(i)

                        
                except:
                        raise
        # 获取首页广告位 
        def test_get_index_advert_position(self,headers,menber):
                data={}
                try:
                        data['CpnID'] = menber['CpnID']
                        data['SubID'] = menber['SubID']
                        data['ShwPosi'] = '1'
                        response=requests.post(url=menber['url'] % '/AdPosi/GetAdPosiByMobileet',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        list=[]
                        list.append(response_json['Data']['AdPosi'])
                        for i in list:
                                print(i)
                        if response_json['Data']['Ad']:
                                for n in response_json['Data']['Ad']:
                                        print(n)
                        else:
                                print('没有广告内容')
                except:
                        raise 


# 券类型
class Test_ticket_type():
        # 获取券类型分页
        def test_get_ticket_type_page(self,headers,manage):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['TknTpID'] = ''
                        data['Name'] = ''
                        data['PageIndex'] = '1'
                        data['PageSize'] = '10'
                        data['Sort'] = 'tknTpID'
                        response=requests.post(url=manage['url'] % '/TknTp/GetTknPage',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        print(response_json)
                        if response_json['Data']['PageDataList']:
                                for i in response_json['Data']['PageDataList']:
                                        # mysql insert response
                                        comm_way.sql_insert('ticket_type_response',response_json['Data']['PageDataList'][0])
                                        print(i)
                        else:
                                print('没有券类型')
                except:
                        raise
        # 修改券类型
        def test_update_ticket_type(self,headers,manage,ticket_type_response_data,now_time):
                print(ticket_type_response_data)
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['TknTpID'] = ticket_type_response_data['tknTpID']
                        data['Name'] = ticket_type_response_data['name']
                        data['TknFrm'] = ticket_type_response_data['tknFrm']
                        data['TknNtu'] = ticket_type_response_data['tknNtu']
                        data['VidScp'] = ticket_type_response_data['vidScp']
                        data['TStt'] = ticket_type_response_data['tStt']
                        data['UseSDy'] = ticket_type_response_data['useSDy']
                        data['UseADy'] = ticket_type_response_data['useADy']
                        data['Brf'] = 'update aa aiptest'
                        data['Stt'] = ticket_type_response_data['stt']
                        data['UptDtt'] = now_time['ymd_hms']
                        data['UpdateProName'] = 'Brf,UptDtt'
                        response=requests.post(url=manage['url'] % '/TknTp/Update',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                except:
                        raise
        # 获取单个券类型
        def test_get_ticket_type(self,headers,manage,ticket_type_response_data):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['TknID'] = ticket_type_response_data['tknTpID']
                        response=requests.post(url=manage['url'] % '/TknTp/Get',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        print(response_json['Data']['Data'])
                except:
                        raise

#券种
class Test_ticket_seed():
        # 新增券种
        def test_add_ticket_seed(self,headers,manage,ticket_data_random,ticket_type_response_data,now_time):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['TknID'] = ticket_data_random['TknID']
                        data['Name'] = ticket_data_random['Name']
                        data['Tknvl'] = ticket_data_random['Tknvl']
                        data['ConsumeMoney'] = ticket_data_random ['ConsumeMoney']
                        data['TknImg'] = ''
                        data['TknDsc'] = ''
                        data['TknTpID'] = ticket_type_response_data['tknTpID']
                        data['SndRul'] = ticket_data_random['SndRul']
                        data['RcvRul'] = ''
                        data['VipTpID'] = ''
                        data['BrfId'] = ''
                        data['SDt'] = now_time['StDt']
                        data['EDt'] = now_time['EdDt']
                        data['TStt'] = 'F'
                        data['UseSDy'] = '0'
                        data['UseADy'] = '0'
                        data['TknSdt'] = ''
                        data['TknEdt'] = ''
                        data['RjcStt'] = 'F'
                        data['Brf'] = 'apitest add'
                        data['ImpCRM'] = '0'
                        data['Stt'] =  '2'
                        data['UptDtt'] = now_time['ymd_hms']
                        response=requests.post(url=manage['url'] % '/Tkn/Add',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                except:
                        raise
        # 获取券种分页
        def test_get_ticket_seed_page(self,headers,manage):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['TknID'] = ''
                        data['Name'] = ''
                        data['RjcStt'] = ''
                        data['Stt'] = ''
                        data['IsSearTime'] = ''
                        data['IsSearValid'] = ''
                        data['SearchVal'] = ''
                        data['TknFrm'] = ''
                        data['TknTpID'] = ''
                        data['PageIndex'] = '1'
                        data['PageSize'] = '10'
                        data['Sort'] = 'uptDtt desc'
                        response=requests.post(url=manage['url'] % '/Tkn/GetTknPage',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        if response_json['Data']['PageDataList']:
                                for i in response_json['Data']['PageDataList']:
                                        # mysql insert response
                                        comm_way.sql_insert('ticket_seed_response',response_json['Data']['PageDataList'][0])
                                        print(i)
                        else:
                                print('没有券种')
                except:
                        raise 
        # 修改券种
        def test_update_ticket_seed(self,headers,manage,ticket_data_random,ticket_seed_response_data,now_time):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['TknID'] = ticket_seed_response_data['tknID']
                        data['Name'] = ticket_data_random['Name']
                        data['Tknvl'] = ticket_data_random['Tknvl']
                        data['ConsumeMoney'] = ticket_data_random['ConsumeMoney']
                        data['TknImg'] = ticket_seed_response_data['tknImg']
                        data['TknDsc'] = ticket_seed_response_data['tknDsc']
                        data['TknTpID'] = ticket_seed_response_data['tknTpID']
                        data['SndRul'] = ticket_data_random['SndRul']
                        data['RcvRul'] = ticket_seed_response_data['rcvRul']
                        data['VipTpID'] = ticket_seed_response_data['vipTpID']
                        data['BrfId'] = ticket_seed_response_data['brfId']
                        data['SDt'] = now_time['StDt']
                        data['EDt'] = now_time['EdDt']
                        data['TStt'] = ticket_seed_response_data['tStt']
                        data['UseSDy'] = ticket_seed_response_data['useSDy']
                        data['UseADy'] = ticket_seed_response_data['useADy']
                        data['TknSdt'] = ''
                        data['TknEdt'] = ''
                        data['RjcStt'] = ticket_seed_response_data['rjcStt']
                        data['Brf'] = 'apitest update'
                        data['ImpCRM'] = ticket_seed_response_data['impCRM']
                        data['Stt'] = ticket_seed_response_data['stt']
                        data['UptDtt'] = now_time['ymd_hms']
                        data['UpdateProName'] = 'Name,Tknvl,ConsumeMoney,SndRul,SDt,EDt,Brf,UptDtt'
                        response=requests.post(url=manage['url'] % '/Tkn/Update',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                except:
                        raise
        # 获取单个券种
        def test_get_ticket_seed(self,headers,manage,ticket_seed_response_data):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['TknID'] = ticket_seed_response_data['tknID']
                        response=requests.post(url=manage['url'] % '/Tkn/Get',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        print(response_json['Data']['Data'])
                except:
                        raise 

