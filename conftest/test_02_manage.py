import pytest
import requests
import sys
import json
import datetime

from comm.comm_way import Way#公共方法
comm_way=Way()

CpnID='0001'
SubID='3378049226@qq.com'
url='http://api.newcrm.group.weixin.wuerp.com/manage/v1.0%s'



class Test_login():
        #登录账号
        userid='miscs3'
        password='111111'
        #登录密码
        #获取验证码
        def test_get_auth_code(self):
                response=requests.post(url=url % '/User/GetCode')
                response_json=response.json()
                global auth_code
                auth_code = response_json['data']['Data']
                assert response.status_code == 200
                assert response_json['success'] == True


        #后台正确账号和正确密码登录
        def test_login_correct(self):
                data={
                        "loginID":"",
                        "loginPwd":"",
                        "checkCode":""
                }
                try:
                        data['loginID'] = Test_login.userid
                        data['loginPwd'] = Test_login.password
                        data['checkCode'] = auth_code
                        response=requests.post(url=url % '/User/Login',data=data)
                        response_json=response.json()
                        global loginID
                        loginID = response_json['data']['Data']
                        assert response.status_code == 200
                        assert response_json['success'] == True
                except:
                        raise
        #后台正确账号和错误密码登录
        def test_login_error_pwd(self):
                data={
                        "loginID":"",
                        "loginPwd":"",
                        "checkCode":""
                }
                try:
                        data['loginID'] = Test_login.userid
                        data['loginPwd'] = '123456'
                        data['checkCode'] = auth_code
                        response=requests.post(url=url % '/User/Login',data=data)
                        response_json=response.json()
                        assert response.status_code == 200
                        assert response_json['success'] == False
                except:
                        raise
        #获取用户信息
        def test_get_user_message(self):
                data={
                        "usrFlg":""}
                try:
                        data['usrFlg']=loginID
                        response=requests.post(url=url % '/User/GetUser',data=data)
                        response_json=response.json()
                        assert response.status_code == 200
                        assert response_json['success'] == True
                except:
                        raise
                


class Test_select_vipdata():
        #查询会员资料分页
        def test_select_menber_message_page(self,headers_x):
                data={
                        "CpnID":"0001",
                        "pageIndex":"1",
                        "pageSize":"10",
                        "sort":"1",
                        "Name":"",#查询条件
                        "VipID":"",
                        "CrdID":"",
                        "CrdNo":"",
                        "Stt":""
                        }
                try:
                        data['CpnID']=CpnID
                        response=requests.post(url=url % '/Gst/GetGstPage',data=data,headers=headers_x)
                        response_json=response.json()
                        assert response.status_code == 200
                        assert response_json['message'] == "获取数据成功"
                except:
                        raise
        #根据会员卡面号查询会员资料
        def test_select_menber_message_page_vipid(self,headers_x,menber_register_data):
                data={
                        "CpnID":"",
                        "pageIndex":"1",
                        "pageSize":"10",
                        "sort":"1",
                        "Name":"",#查询条件
                        "VipID":"",
                        "CrdID":"",
                        "CrdNo":"",
                        "Stt":""
                        }
                try:
                        data['CpnID']=CpnID
                        data['VipID']=menber_register_data['crdFaceID']
                        response=requests.post(url=url % '/Gst/GetGstPage',data=data,headers=headers_x)
                        response_json=response.json()
                        assert response.status_code == 200
                        assert response_json['message'] == "获取数据成功"
                except:
                        raise
class Test_menber_message():
        #查询会员单个资料
        def test_select_menber_message(self,headers_x,menber_register_data):
                data={
                "CpnID":"", 
                "gstID":""
                }
                try:
                        data["CpnID"]=CpnID
                        data["gstID"]=menber_register_data['gstID']
                        response=requests.post(url=url % '/Gst/GetSingerData',data=data,headers=headers_x)
                        response_json=response.json()
                        global menber_message
                        menber_message=response_json['data']['Data']  
                        print(menber_message)
                        assert response.status_code == 200
                        assert response_json['message'] == "获取成功"
                except:
                        raise

        #修改会员信息
        def test_modify_menber_message(self,headers_x):
                #获取会员资料
                global random_menber_message
                random_menber_message=comm_way.menber_information_random()
                data={}
                try:
                        data['ID']=menber_message['id']
                        data['CpnID']=menber_message['cpnID']
                        data['UsrFlg']=menber_message['usrFlg']
                        data['NickName']=menber_message['nickName']
                        data['Pwd']=menber_message['pwd']
                        data['PwdDt']=menber_message['pwdDt']
                        data['Tel']=random_menber_message[2]
                        data['Eml']=menber_message['eml']
                        data['Name']=random_menber_message[1]
                        data['IDntTp']='001'
                        data['IDntNmb']=random_menber_message[4]
                        data['VipID']=menber_message['vipID']
                        data['OrgID']=menber_message['orgID']
                        data['VipTpID']=random_menber_message[0]
                        data['Strvlstt']=menber_message['strvlstt']
                        data['LastDate']=menber_message['lastDate']
                        data['RgstApp']=menber_message['rgstApp']
                        data['Lne']=menber_message['lne']
                        data['RegstMonth']=menber_message['regstMonth']
                        data['RgWxMonth']=menber_message['rgWxMonth']
                        data['Rcmd']=menber_message['rcmd']
                        data['EcrpBase']=menber_message['ecrpBase']
                        data['Ecrp1']=menber_message['ecrp1']
                        data['Ecrp2']=menber_message['ecrp2']
                        data['IsUpToERP']=menber_message['isUpToERP']
                        data['Brth']=random_menber_message[3]
                        data['Sex']=menber_message['sex']
                        data['Mrry']=menber_message['mrry']
                        data['BabyStt']=menber_message['babyStt']
                        data['Babydt']=menber_message['babydt']
                        data['Edu']=menber_message['edu']
                        data['Ntn']=menber_message['ntn']
                        data['Prvc']=menber_message['prvc']
                        data['City']=menber_message['city']
                        data['Addr']=menber_message['addr']
                        data['Avt']=menber_message['avt']
                        data['EmployeeNumber']=menber_message['employeeNumber']
                        data['RegDt']=menber_message['regDt']
                        data['Stt']=menber_message['stt']
                        data['Brf']=menber_message['brf']
                        data['Uptr']=menber_message['uptr']
                        data['UptDtt']=menber_message['uptDtt']
                        data['updateProNames']='tel,Name,IDntTp,IDntNmb,VipTpID,Brth'        #修改字段
                        response=requests.post(url=url % '/Gst/Update',data=data,headers=headers_x)
                        response_json=response.json()
                        assert response.status_code == 200
                        assert response_json['message'] == "修改成功"
                except:
                        raise


class Test_select_vipcard():
        #查询会员卡分页
        def test_select_vipcard_paging(self,headers_x):
                data={
                        "CpnID":"",    
                        "pageIndex":"1",      
                        "pageSize":"10",       
                        "sort":"1",     
                        "param":{
                                "CrdID":"",     
                                "CrdNo":"",
                                "GstID":""
                                }
                        }
                try:
                        data['CpnID']=CpnID
                        response=requests.post(url=url % '/VipCrd/GetPageByParam',params=data,headers=headers_x)
                        response_json=response.json()
                        assert response.status_code == 200
                        assert response_json['message'] =='获取数据成功'
                except:
                        raise

        #根据卡账号查询会员
        def test_select_vipcard_paging_gstid(self,headers_x,menber_register_data):
                data={
                        "CpnID":"",    
                        "pageIndex":"1",      
                        "pageSize":"10",       
                        "sort":"1",     
                        "param":{
                                "CrdID":"",     
                                "CrdNo":"",
                                "GstID":""
                                }
                        }
                try:
                        data['CpnID']=CpnID
                        data['param']['GstID']=menber_register_data['gstID']
                        response=requests.post(url=url % '/VipCrd/GetPageByParam',params=data,headers=headers_x)
                        response_json=response.json()
                        assert response.status_code == 200
                        assert response_json['message'] =='获取数据成功'
                except:
                        raise
        #根据卡面号查询会员
        def test_select_vipcard_paging_cardface(self,headers_x,menber_register_data):
                data={
                        "CpnID":"",    
                        "pageIndex":"1",      
                        "pageSize":"10",       
                        "sort":"1",     
                        "params":{
                                "CrdID":"",     
                                "CrdNo":"",
                                "GstID":""
                                }
                        }
                try:
                        data['CpnID']=CpnID
                        data['params']['CrdNo']=menber_register_data['crdFaceID']
                        response=requests.post(url=url % '/VipCrd/GetPageByParam',params=data,headers=headers_x)
                        response_json=response.json()
                        assert response.status_code == 200
                        assert response_json['message'] =='获取数据成功'
                except:
                        raise
        #根据卡账号查询会员
        def test_select_vipcard_paging_cardid(self,headers_x,menber_register_data):
                data={
                        "CpnID":"",    
                        "pageIndex":"1",      
                        "pageSize":"10",       
                        "sort":"1",     
                        "param":{
                                "CpnID":"",
                                "CrdID":"",     
                                "CrdNo":"",
                                "GstID":""
                                }
                        }
                try:
                        data['CpnID']=CpnID
                        data['param']['CrdID']=menber_register_data['crdID']
                        response=requests.post(url=url % '/VipCrd/GetPageByParam',params=data,headers=headers_x)
                        response_json=response.json()
                        assert response.status_code == 200
                        assert response_json['message'] =='获取数据成功'
                except:
                        raise


class Test_parking():
        #添加停车场
        def test_add_parking(self,headers_x):
                #获取当前时间
                now_time=comm_way.now_time()
                #获取停车场数据
                parking_data=comm_way.parking_data_random()
                data={  "ID":'0',
                        "CpnID":"",
                        "ParkID":"",
                        "PayExplain":"apitest",
                        "Tel":"",
                        "IsSupWXPay":0,
                        "IsSupIntg":0,
                        "IsSupIntgAuto":0,
                        "ParkUrl":"0",
                        "LoginUrl":"0",
                        "BllNoUrl":"0",
                        "ParkUser":"0",
                        "ParkPwd":"0",
                        "ParkKey":"0",
                        "SecretKey":"0",
                        "Uptr":"miscs3",
                        "UptDtt":""
                        }
                try:
                        data['CpnID']=CpnID
                        data['ParkID']=parking_data[0]
                        data['Tel']=parking_data[1]
                        data['UptDtt'] =now_time[1]
                        response=requests.post(url=url % '/Park/AddParkConfig',data=data,headers=headers_x)
                        response_json=response.json()
                        assert response.status_code == 200
                        assert response_json['message'] =='添加成功'
                except:
                        raise
        #获取停车场信息分页
        def test_select_parking_data_page(self,headers_x):
                data={
                        "CpnID":"",
                        "pageIndex":"1",
                        "pageSize":"10",
                        "sort":"id desc",
                        "ParkID":"",
                        "IsSupWXPay":"",
                        "IsSupIntg":""
                        }
                try:
                        data['CpnID']=CpnID
                        response=requests.post(url=url % '/Park/GetParkConfigPage',data=data,headers=headers_x)
                        response_json=response.json()
                        global parking_data_new
                        parking_data_new=response_json['data']['PageDataList'][0]
                        assert response.status_code == 200
                        assert response_json['message'] =='获取数据成功'
                except:
                        raise
        #修改停车场数据
        def test_modify_parking_data(self,headers_x):
                #获取当前时间
                now_time=comm_way.now_time()
                #获取停车场数据
                parking_data=comm_way.parking_data_random()
                data={  "ID":'',
                        "CpnID":"",
                        "ParkID":"",
                        "PayExplain":"apitest",
                        "Tel":"",
                        "IsSupWXPay":0,
                        "IsSupIntg":0,
                        "IsSupIntgAuto":0,
                        "ParkUrl":"0",
                        "LoginUrl":"0",
                        "BllNoUrl":"0",
                        "ParkUser":"0",
                        "ParkPwd":"0",
                        "ParkKey":"0",
                        "SecretKey":"0",
                        "Uptr":"miscs3",
                        "UptDtt":"",
                        "updateName":""
                        }
                try:
                        data['ID']=parking_data_new['id']
                        data['CpnID']=CpnID
                        data['ParkID']=parking_data[0]
                        data['Tel']=parking_data[1]
                        data['UptDtt'] =now_time[1]
                        data['updateName'] = 'ID,CpnID,ParkID,Tel,UptDtt'
                        response=requests.post(url=url % '/Park/UpdateParkConfig',data=data,headers=headers_x)
                        response_json=response.json()
                        assert response.status_code == 200
                        assert response_json['message'] =='修改成功'
                except:
                        raise
        #获取单个停车场数据
        def test_select_parking_data(self,headers_x):
                data={
                        "CpnID":"",
                        "ID":"",
                        }
                try:
                        data['CpnID']=CpnID
                        data['ID']=parking_data_new['id']
                        response=requests.post(url=url % '/Park/GetParkConfigSinger',data=data,headers=headers_x)
                        response_json=response.json()
                        assert response.status_code == 200
                        assert response_json['message'] =='获取成功'
                except:
                        raise

        #添加停车场规则
        def test_add_parking_rule(self,headers_x):
                #获取当前时间
                now_time=comm_way.now_time()
                data={
                        "ID":"",
                        "CpnID":"",
                        "SubID":"",
                        "ParkID":"",
                        "VipTpID":"03",
                        "IsEv":"0",
                        "CalculaTyp":"0",
                        "FreeMinute":"0",
                        "StartMinute":"0",
                        "StartMoney":"0",
                        "StartIntg":"0",
                        "StartGold":"0",
                        "IntrvalTime":"5",
                        "IntrvalMoney":'5',
                        "IntrvalIntg":"5",
                        "IntrvalGold":"5",
                        "ConsumMoney":"0",
                        "ConsFreeMinute":"0",
                        "IntgSupportHour":"0",
                        "Uptr":"miscs3",
                        "UptDtt":"",
                }
                try:
                        data['ID']=parking_data_new['id']
                        data['CpnID']=CpnID
                        data['SubID']=SubID
                        data['ParkID']=parking_data_new['parkID']
                        # data['VipTpID']=random_menber_message[0]
                        data['UptDtt'] =now_time[1]
                        print(data)
                        response=requests.post(url=url % '/Park/AddParkRule',data=data,headers=headers_x)
                        response_json=response.json()
                        print(response_json)
                        assert response.status_code == 200
                        assert response_json['message'] =='添加成功'
                except:
                        raise



                
#签到规则
def test_signin_rule(headers_x):
        data={
                "ID":"0",
                "CpnID":"",
                "SubID":"",
                "Typ ":"1",
                "Days ":"1",
                "Integral ":"132",
                "LngValid ":"0",
                "StDt ":"",
                "EdDt ":"",
                "IsStop ":"0",
                "Brf ":"apitest",
                "Uptr":"miscs3",
                "UptDtt":"",
                }
        try:    
                data['CpnID']=CpnID
                data['SubID']=SubID
                data['StDt']=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                data['EdDt']=(datetime.datetime.now()+datetime.timedelta(days=3)).strftime('%Y-%m-%d %H:%M:%S')
                data['UptDtt']=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                response=requests.post(url=url % '/SignInRules/AddSignInRules',data=data,headers=headers_x)
                response_json=response.json()
                assert response.status_code == 200
                assert response_json['message'] =='添加成功'
        except:
                raise













