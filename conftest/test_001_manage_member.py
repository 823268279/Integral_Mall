import pytest
import requests
import sys
import json
import random
from comm.comm_way import Way#公共方法
comm_way=Way()






#短信验证码
# def test_smscode(menber):
#         data={
#                 "cpnID":"",
#                 "SubID":"",
#                 "tel":"13183807891",
#                 }
#         try:
#                 data['CpnID'] = menber['CpnID']
#                 data['SubID'] = menber['SubID']
#                 response=requests.post(url=menber['url'] % '/SMS/SendSMSCode',data=data)
#                 print(response.status_code)
#                 print(response.json())
#         except:
#                 raise



class Test_company_organization():
        #新增门店
        # def test_add_company_organization(self,headers,manage,now_time):
        #         data={}
        #         try:
        #                 data['CpnID'] = manage['CpnID']
        #                 data['SubID'] = manage['SubID']
        #                 data['OrgID'] = '1003'
        #                 data['Name'] = '大卖场三'
        #                 data['HlpCd'] = ''
        #                 data['PrtID'] = ''
        #                 data['Type'] = '004'
        #                 data['SubType'] = '1'
        #                 data['BrchID'] = ''
        #                 data['City'] = '重庆'
        #                 data['Lnkr'] =''
        #                 data['Adr'] = '解放碑'
        #                 data['Tel'] = ''
        #                 data['Phone'] = '18132255675'
        #                 data['Fax'] = ''
        #                 data['Lvl'] = '1'
        #                 data['Stt'] = '0'
        #                 data['EndFlg'] = 'F'
        #                 data['Intgact'] = 'F'
        #                 data['IsMakeCrd'] = '1'
        #                 data['IsSendCrd'] = '1'
        #                 data['Brf'] = 'apitest'
        #                 data['UptDtt'] = now_time['ymd_hms']
        #                 response=requests.post(url=manage['url'] % '/CpnOrg/AddCpnOrg',data=data,headers=headers)
        #                 response_json = comm_way.response_dispose(response.json())
        #                 print(response_json['Message'])
        #                 assert response.status_code == 200
        #                 assert response_json['Success'] == True
        #         except:
        #                 raise

        # 分页获取门店
        def test_get_company_organization_page(self,headers,manage):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['SubID'] = manage['SubID']
                        data['PgIndex'] = '1'
                        data['PgSize'] = '10'
                        data['Stt'] = '-99'
                        print(data)
                        response=requests.post(url=manage['url'] % '/CpnOrg/GetCpnOrgPG',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json)
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        if response_json['Data']['Data']:
                                for i in response_json['Data']['Data']:
                                        print(i)
                        else:
                                print('没有门店')
                except:
                        raise

        # 获取状态正常的所有门店
        def test_get_company_organization_all(self,headers,menber):
                data={}
                try:
                        data['CpnID'] = menber['CpnID']
                        data['SubID'] = menber['SubID']
                        response=requests.post(url=menber['url'] % '/Guest/GetNormalCpnOrg',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        if response_json['Data']['Data']:
                                for i in response_json['Data']['Data']:
                                        # mysql insert organization_response
                                        comm_way.sql_insert('organization_response',response_json['Data']['Data'][-1])
                                        print(i)
                        else:
                                print('没有机构')
                except:
                        raise




#会员注册   
def test_member_register(headers,menber,menber_data_random,organization_response_data):
        data={}
        try:
                data['CpnID'] = menber['CpnID']
                data['SubID'] = menber['SubID']
                data['OpnID'] = menber_data_random['OpnID']
                data['Name'] = menber_data_random['Name']
                data['Tel'] = menber_data_random['Tel']
                data['Brth'] = menber_data_random['Brth']
                data['SMSCode'] = '0000'        #短信验证码
                data['OrgID'] = '0000'
                data['UseOrgID']= organization_response_data['orgID']
                data['IDSource'] = '100'
                data['UserSource'] = ''
                data['Eml'] = ''
                data['IDntTp'] = ''
                data['IDntNmb'] = ''
                data['Sex'] = '1'
                data['Prvc'] = ''
                data['City'] = ''
                data['Addr'] = ''
                data['UnionID'] = menber_data_random['UnionID']
                data['JsCode'] = ''
                data['EmployeeNumber'] = ''
                data['AppID'] = ''
                data['AppSecret'] = ''
                print(data)
                # mysql insert request data
                comm_way.sql_insert('register_request',data)
                response=requests.post(url=menber['url'] % '/Guest/Register',data=data,headers=headers)
                response_json = comm_way.response_dispose(response.json())
                print(response_json['Message'])
                assert response.status_code == 200
                assert response_json['Success'] == True
                if response_json['Data']['Data']:
                        for i in response_json['Data']['Data']:
                                # mysql insert response data
                                comm_way.sql_insert('register_response',response_json['Data']['Data'][0])
                                print(i)
                else:
                        print('没有会员')
        except:
                raise




# 会员登录
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



class Test_login():
        # 获取验证码
        def test_get_code(self,manage,headers):
                try:
                        response=requests.post(url=manage['url'] % '/User/GetCode',headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        global verification_code
                        verification_code = response_json['Data']['Data']
                except:
                        raise

        # 后台正确账号和正确密码登录
        def test_login_correct(self,manage,headers):
                data={}
                try:
                        data['loginID'] = manage['username']
                        data['loginPwd'] = manage['password']
                        data['checkCode'] = verification_code
                        response=requests.post(url=manage['url'] % '/User/Login',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        global loginID
                        loginID = response_json['Data']['Data']
                except:
                        raise

        #后台正确账号和错误密码登录
        def test_login_error_pwd(self,manage,headers):
                data={}
                try:
                        data['loginID'] = manage['username']
                        data['loginPwd'] = '#$%^&***%$#^^%^%$^%$^$^%$%'
                        data['checkCode'] = verification_code
                        response=requests.post(url=manage['url'] % '/User/Login',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == False
                        
                except:
                        raise
                
        #获取用户信息
        def test_get_user_message(self,manage,headers):
                data={}
                try:
                        data['usrFlg'] = loginID
                        response=requests.post(url=manage['url'] % '/User/GetUser',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json)
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                except:
                        raise



class Test_member_select():
        #查询会员单个资料
        def test_get_member_data(self,headers,manage,menber_register_response_data):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data["gstID"] = menber_register_response_data['gstID']
                        print(data)
                        response=requests.post(url=manage['url'] % '/Gst/GetSingerData',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])  
                        assert response.status_code == 200
                        assert response_json['Success'] == True    
                        global member_response_data
                        member_response_data=response_json['Data']['Data']
                        print(response_json['Data']['Data'])
                except:
                        raise

        #修改会员信息
        def test_update_member_data(self,headers,manage,menber_data_random):
                data={}
                try:
                        data['ID'] = member_response_data['id']
                        data['CpnID'] = member_response_data['cpnID']
                        data['UsrFlg'] = member_response_data['usrFlg']
                        data['NickName'] = member_response_data['nickName']
                        data['Pwd'] = member_response_data['pwd']
                        data['PwdDt'] = member_response_data['pwdDt']
                        data['Tel'] = menber_data_random['Tel']
                        data['Eml'] = member_response_data['eml']
                        data['Name'] = menber_data_random['Name']
                        data['IDntTp'] = '001'
                        data['IDntNmb'] = menber_data_random['IDntNmb']
                        data['VipID'] = member_response_data['vipID']
                        data['OrgID'] = member_response_data['orgID']
                        # data['VipTpID'] = menber_data_random['VipTpID']
                        data['VipTpID'] = member_response_data['vipTpID']
                        data['Strvlstt'] = member_response_data['strvlstt']
                        data['LastDate'] = member_response_data['lastDate']
                        data['RgstApp'] = member_response_data['rgstApp']
                        data['Lne'] = member_response_data['lne']
                        data['RegstMonth'] = member_response_data['regstMonth']
                        data['RgWxMonth'] = member_response_data['rgWxMonth']
                        data['Rcmd'] = member_response_data['rcmd']
                        data['EcrpBase'] = member_response_data['ecrpBase']
                        data['Ecrp1'] = member_response_data['ecrp1']
                        data['Ecrp2'] = member_response_data['ecrp2']
                        data['IsUpToERP'] = member_response_data['isUpToERP']
                        data['Brth'] = menber_data_random['Brth']
                        data['Sex'] = member_response_data['sex']
                        data['Mrry'] = member_response_data['mrry']
                        data['BabyStt'] = member_response_data['babyStt']
                        data['Babydt'] = member_response_data['babydt']
                        data['Edu'] = member_response_data['edu']
                        data['Ntn'] = member_response_data['ntn']
                        data['Prvc'] = member_response_data['prvc']
                        data['City'] = member_response_data['city']
                        data['Addr'] = member_response_data['addr']
                        data['Avt'] = member_response_data['avt']
                        data['EmployeeNumber'] = member_response_data['employeeNumber']
                        data['RegDt'] = member_response_data['regDt']
                        data['Stt'] = member_response_data['stt']
                        data['Brf'] = member_response_data['brf']
                        data['Uptr'] = member_response_data['uptr']
                        data['UptDtt'] = member_response_data['uptDtt']
                        data['updateProNames'] = 'Tel,Name,IDntTp,IDntNmb,VipTpID,Brth'        #修改字段
                        print(data)
                        response=requests.post(url=manage['url'] % '/Gst/Update',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json)
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True                      
                except:
                        raise


class Test_select_vipdata():
        #查询会员资料分页
        def test_get_member_data_page(self,headers,manage):
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
                                # mysql insert member_data_page response data
                                comm_way.sql_insert('member_data_page_response',response_json['Data']['PageDataList'][0])
                                for i in response_json['Data']['PageDataList']:
                                        print(i)
                        else:
                                print('没有会员')
                except:
                        raise
        #根据会员姓名查询会员数据
        def test_get_member_data_page_name(self,headers,manage,member_data_page_response_data):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['SubID'] = manage['SubID']
                        data['Name'] = member_data_page_response_data['name']
                        # data['Name'] = '落落大方'
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
                                # mysql insert member data response data
                                comm_way.sql_insert('member_data_response',response_json['Data']['PageDataList'][0])
                                for i in response_json['Data']['PageDataList']:
                                        print(i)
                        else:
                                print('没有会员')
                except:
                        raise
        #根据会员卡面号查询会员数据
        def test_get_member_data_page_vipid(self,headers,manage,member_data_page_response_data):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['SubID'] = manage['SubID']
                        data['Name'] = ""
                        data['VipID'] = member_data_page_response_data['vipID']
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
        def test_get_vipcard_page(self,headers,manage):
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
                        assert response.status_code == 200
                        assert response_json['Success'] == True                       
                        if response_json['Data']['PageDataList']:
                                # mysql insert vipcard page response data
                                comm_way.sql_insert('vipcard_data_page_response',response_json['Data']['PageDataList'][0])
                                for i in response_json['Data']['PageDataList']:
                                        print(i)
                        else:
                                print('没有会员')
                except:
                        raise
        #根据卡账号查询会员卡
        def test_get_vipcard_cardid(self,headers,manage,vipcard_page_response_data):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['CrdID'] = vipcard_page_response_data['crdID']
                        # data['CrdID'] = '188000100000175276'
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
                                # mysql insert vipcard response data
                                comm_way.sql_insert('vipcard_data_response',response_json['Data']['PageDataList'][0])
                                for i in response_json['Data']['PageDataList']:
                                        print(i)
                        else:
                                print('没有会员')
                except:
                        raise

        #根据会员ID查询会员卡
        def test_get_vipcard_gstid(self,headers,manage,vipcard_page_response_data):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['CrdID'] = ""
                        data['CrdNo'] = ""
                        data['GstID'] = vipcard_page_response_data['gstID']
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
        #根据卡面号查询会员卡
        def test_get_vipcard_cardface(self,headers,manage,vipcard_page_response_data):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['CrdID'] = ""
                        data['CrdNo'] = vipcard_page_response_data['crdNo']
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
        
# 积分调整
class Test_integral_adjustment():
        # 添加积分调整单
        def test_add_integral_adjustment(self,headers,manage,vipcard_response_data,now_time):
                data={}
                try:    
                        data['CpnID'] = manage['CpnID']
                        data['BllNo'] = '0'      #单据号
                        data['BizDt'] = now_time['ymd_hms']      #业务日期
                        data['AccOrgID'] = '0000'   #核算机构
                        data['OrgID'] = '0000'      #业务机构
                        data['GstID'] = vipcard_response_data['gstID']      #会员ID
                        data['VipID'] = vipcard_response_data['vipID']      #会员编码
                        data['IntgAva'] = '0'    #当前可用积分
                        data['IntgModi'] = '700'   #积分调整
                        data['IntgModirs'] = '积分调整单' #调整原因
                        data['Brf'] = 'apitest'  
                        data['Stt'] = '0'        #状态[-1:禁用，0:正常，50:通过]
                        data['FlwStt'] = '0'     #流程状态[-1:作废，0:正常，1:结束]
                        data['Uptr'] = manage['username']
                        data['UptDtt'] = now_time['ymd_hms']
                        response=requests.post(url=manage['url'] % '/IntgCrtn/Add',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        print(response_json)
                except:
                        raise

# 停车场
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
        def test_get_park_data_page(self,headers,manage):
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
                                comm_way.sql_insert('park_page_response',response_json['Data']['PageDataList'][0])
                                for i in response_json['Data']['PageDataList']:
                                        print(i)
                        else:
                                print('没有停车场')
                except:
                        raise
        #修改停车场数据
        def test_update_park_data(self,headers,manage,parking_data_random,now_time,park_page_response_data):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['ID'] = park_page_response_data['id']
                        data['ParkID'] = park_page_response_data['parkID']
                        data['PayExplain'] = "apitest"
                        data['Tel'] = park_page_response_data['tel']
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
                        print(response_json)  
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True  
                except:
                        raise
        #获取单个停车场数据
        def test_get_park_data(self,headers,manage,park_page_response_data):
                data={}
                try:
                        data['CpnID']=manage['CpnID']
                        data['ID']=park_page_response_data['id']
                        response=requests.post(url=manage['url'] % '/Park/GetParkConfigSinger',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True    
                        print(response_json['Data']['Data'])                 
                except:
                        raise

# 停车场缴费规则
class Test_park_rule():
        # 添加停车场缴费规则
        def test_add_park_rule(self,headers,manage,now_time,park_page_response_data):
                for i in range(1,random.choice(range(3,6))):
                        data={}
                        try:
                                data['CpnID'] = manage['CpnID']
                                data['SubID'] = manage['SubID']
                                data['ID'] = park_page_response_data['id']
                                data['ParkID'] = park_page_response_data['parkID']    #停车场编号
                                data['VipTpID'] = '0%s'% i                      #会员类型ID
                                data['IsEv'] = "0"                              #是否是新能源车牌(0-所有车型，1-新能源车票)
                                data['CalculaTyp'] = "1"                        #计算类型(0-按次数计算，1-按时长计算)
                                data['FreeMinute'] = "0"                        #免费时长(多少分钟内免费)
                                data['StartMinute'] = "0"                       #起步时长
                                data['StartMoney'] = "5"                        #起步金额
                                data['StartIntg'] = "20"                         #起步积分
                                data['StartGold'] = "0"                         #起步金币
                                data['IntrvalTime'] = "30"                       #单价时间
                                data['IntrvalMoney'] = "20"                      #单价金额
                                data['IntrvalIntg'] = "200"                       #单价积分
                                data['IntrvalGold'] = "0"                       #单价金币
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
        # 获取停车场缴费规则分页
        def test_get_park_rule_page(self,headers,manage,park_page_response_data):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['ParkID'] = park_page_response_data['parkID']
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
                                comm_way.sql_insert('park_rule_page_response',response_json['Data']['PageDataList'][0])
                                for i in response_json['Data']['PageDataList']:
                                        print(i)
                        else:
                                print('没有停车场缴费规则')
                except:
                        raise
        # 获取停车场缴费规则单条
        def test_get_park_rule(self,headers,manage,park_rule_page_response_data):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['id'] = park_rule_page_response_data['id']
                        response=requests.post(url=manage['url'] % '/Park/GetParkRuleSinger',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True     
                        print(response_json['Data']['Data'])  
                except:
                        raise
        # 修改停车场缴费规则
        def test_update_park_rule(self,headers,manage,now_time,park_rule_page_response_data,parking_data_random):
                data={}
                try:
                        data['ID']=park_rule_page_response_data['id']
                        data['CpnID']=park_rule_page_response_data['cpnID']
                        data['SubID']=park_rule_page_response_data['subID']
                        data['ParkID']=parking_data_random['ParkID']
                        data['VipTpID']='02'
                        data['IsEv']=park_rule_page_response_data['isEv']
                        data['CalculaTyp']=park_rule_page_response_data['calculaTyp']
                        data['FreeMinute']=park_rule_page_response_data['freeMinute']
                        data['StartMinute']=park_rule_page_response_data['startMinute']
                        data['StartMoney']=park_rule_page_response_data['startMoney']
                        data['StartIntg']=park_rule_page_response_data['startIntg']
                        data['StartGold']=park_rule_page_response_data['startGold']
                        data['IntrvalTime']=park_rule_page_response_data['intrvalTime']
                        data['IntrvalMoney']=park_rule_page_response_data['intrvalMoney']
                        data['IntrvalIntg']=park_rule_page_response_data['intrvalIntg']
                        data['IntrvalGold']=park_rule_page_response_data['intrvalGold']
                        data['ConsumMoney']=park_rule_page_response_data['consumMoney']
                        data['ConsFreeMinute']=park_rule_page_response_data['consFreeMinute']
                        data['IntgSupportHour']=park_rule_page_response_data['intgSupportHour']
                        data['Uptr']=park_rule_page_response_data['uptr']
                        data['UptDtt']=now_time['ymd_hms']
                        data['updateName']='ParkID'
                        response=requests.post(url=manage['url'] % '/Park/UpdateParkRule',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True                     
                except:
                        raise


# 系统配置表
class Test_system_config():
        # 查询系统配置分页
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
        # 修改wifi密码
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
        # 获取wifi配置信息
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


# 签到规则
class Test_signin_rule():
        # 添加签到规则
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
                        print(response_json)
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True   
                except:
                        raise
        # 获取签到规则分页
        def test_get_signin_rule_page(self,headers,manage):
                data={}
                try:    
                        data['CpnID'] = manage['CpnID']
                        data['SubID'] = manage['SubID']
                        data['Typ'] = '-99'
                        data['Days'] = ''
                        data['Integral'] = '' 
                        data['LngValid'] = '-99'
                        data['StDt'] = ''
                        data['EdDt'] = ''
                        data['IsStop'] = '-99'
                        data['PgIndex'] = '1'
                        data['PgSize'] = '10'
                        data['Stt'] = '-99'
                        response=requests.post(url=manage['url'] % '/SignInRules/GetWhereSignInRules',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True                       
                        if response_json['Data']['PageDataList']:
                                # mysql insert response data
                                comm_way.sql_insert('signin_rule_response',response_json['Data']['PageDataList'][0]) 
                                for i in response_json['Data']['PageDataList']:
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
                        data['Integral'] = "3000"                                 #赠送值
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


# 广告
class Test_advert():
        # 上传广告到s3
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
        # 添加广告位
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
        # 查询广告位分页
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
                        if response_json['Data']['PageDataList']:
                                for i in response_json['Data']['PageDataList']:
                                        # mysql insert response
                                        comm_way.sql_insert('ticket_type_page_response',response_json['Data']['PageDataList'][0])
                                        print(i)
                        else:
                                print('没有券类型')
                except:
                        raise
        # 修改券类型
        def test_update_ticket_type(self,headers,manage,ticket_type_page_response_data,now_time):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['TknTpID'] = ticket_type_page_response_data['tknTpID']
                        data['Name'] = ticket_type_page_response_data['name']
                        data['TknFrm'] = ticket_type_page_response_data['tknFrm']
                        data['TknNtu'] = ticket_type_page_response_data['tknNtu']
                        data['VidScp'] = ticket_type_page_response_data['vidScp']
                        data['TStt'] = ticket_type_page_response_data['tStt']
                        data['UseSDy'] = ticket_type_page_response_data['useSDy']
                        data['UseADy'] = ticket_type_page_response_data['useADy']
                        data['Brf'] = 'update aa aiptest'
                        data['Stt'] = ticket_type_page_response_data['stt']
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
        def test_get_ticket_type(self,headers,manage,ticket_type_page_response_data):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['TknID'] = ticket_type_page_response_data['tknTpID']
                        response=requests.post(url=manage['url'] % '/TknTp/Get',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        print(response_json['Data']['Data'])
                except:
                        raise

# 券种
class Test_ticket_seed():
        # 新增券种
        def test_add_ticket_seed(self,headers,manage,ticket_data_random,ticket_type_page_response_data,now_time):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['TknID'] = ticket_data_random['TknID']
                        data['Name'] = ticket_data_random['Name']
                        data['Tknvl'] = ticket_data_random['Tknvl']
                        data['ConsumeMoney'] = ticket_data_random ['ConsumeMoney']
                        data['TknImg'] = ''
                        data['TknDsc'] = ''
                        data['TknTpID'] = ticket_type_page_response_data['tknTpID']
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
                                        comm_way.sql_insert('ticket_seed_page_response',response_json['Data']['PageDataList'][0])
                                        print(i)
                        else:
                                print('没有券种')
                except:
                        raise 
        # 修改券种
        def test_update_ticket_seed(self,headers,manage,ticket_data_random,ticket_seed_page_response_data,now_time):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['TknID'] = ticket_seed_page_response_data['tknID']
                        data['Name'] = ticket_data_random['Name']
                        data['Tknvl'] = ticket_data_random['Tknvl']
                        data['ConsumeMoney'] = ticket_data_random['ConsumeMoney']
                        data['TknImg'] = ticket_seed_page_response_data['tknImg']
                        data['TknDsc'] = ticket_seed_page_response_data['tknDsc']
                        data['TknTpID'] = ticket_seed_page_response_data['tknTpID']
                        data['SndRul'] = ticket_data_random['SndRul']
                        data['RcvRul'] = ticket_seed_page_response_data['rcvRul']
                        data['VipTpID'] = ticket_seed_page_response_data['vipTpID']
                        data['BrfId'] = ticket_seed_page_response_data['brfId']
                        data['SDt'] = now_time['StDt']
                        data['EDt'] = now_time['EdDt']
                        data['TStt'] = ticket_seed_page_response_data['tStt']
                        data['UseSDy'] = ticket_seed_page_response_data['useSDy']
                        data['UseADy'] = ticket_seed_page_response_data['useADy']
                        data['TknSdt'] = ''
                        data['TknEdt'] = ''
                        data['RjcStt'] = ticket_seed_page_response_data['rjcStt']
                        data['Brf'] = 'apitest update'
                        data['ImpCRM'] = ticket_seed_page_response_data['impCRM']
                        data['Stt'] = ticket_seed_page_response_data['stt']
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
        def test_get_ticket_seed(self,headers,manage,ticket_seed_page_response_data):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['TknID'] = ticket_seed_page_response_data['tknID']
                        response=requests.post(url=manage['url'] % '/Tkn/Get',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        print(response_json['Data']['Data'])
                except:
                        raise

