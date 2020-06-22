import pytest
import requests
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

        


#会员注册   
def test_menber_register(headers,menber,menber_data_random):
        data={
                "CpnID":"",
                "SubID":"",
                "OpnID":"",
                "SMSCode":"0000",#验证码
                "Name":"",
                "OrgID":"",
                "IDSource":"100",
                "UserSource":"",
                "Tel":"",
                "Eml":"",
                "IDntTp":"",
                "IDntNmb":"",
                "Brth":"",
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
                data['CpnID'] = menber['CpnID']
                data['SubID'] = menber['SubID']
                data['OpnID'] = menber_data_random['OpnID']
                data['Name'] = menber_data_random['Name']
                data['Tel'] = menber_data_random['Tel']
                data['Brth'] = menber_data_random['Brth']
                response=requests.post(url=menber['url'] % '/Guest/Register',data=data,headers=headers)
                response_json=response.json()
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
                test_data[2]=str(response.url)
                test_data[3]=str(data)
                test_data[4]=str(response_json)
                comm_way.xlsx_write_way(2,test_data)
        except:
                raise

#获取首页的会员数据
def test_get_index_menber_data(headers,menber,menber_register_data):
        data={
                "CpnID":"",
                "SubID":"",
                "gstID":""}

        try:    
                data['CpnID'] = menber['CpnID']
                data['SubID'] = menber['SubID']
                data['gstID'] = menber_register_data['gstID']
                response=requests.post(url=menber['url'] % '/Guest/GetMainGst',data=data,headers=headers)
                response_json=response.json()
                assert response.status_code == 200
                assert response_json['message'] == "获取成功"
                print('会员卡号：%s' % response_json["data"]['Data']['vipID'])
                print('我的积分%s' % response_json["data"]['Data']['intgAva'])
                print('优惠券%s' % response_json["data"]['Data']['tknQty'])
                print('签到天数：%s' % response_json["data"]['Data']['signInDay'])
        except:
                raise

        


#获取某个会员的全部卡
def test_select_menber_allcard(headers,menber,menber_register_data):  
        data={
                "CpnID":"",
                "SubID":"",
                "opnID":"",
                }
        try:
                data['CpnID'] = menber['CpnID']
                data['SubID'] = menber['SubID']
                data['opnID'] = menber_register_data['opnID']
                response=requests.post(url=menber['url'] % '/VipCrd/Get',data=data,headers=headers)
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
def test_select_only_card(headers,menber,menber_register_data):
        data={
                "CpnID":"0001",
                "crdID":"",
                }
        try:
                data['CpnID'] = menber['CpnID']
                data['crdID'] = menber_register_data['crdID']
                response=requests.post(url=menber['url'] % '/VipCrd/GetByCrdID',data=data,headers=headers)
                response_json=response.json()
                assert response.status_code == 200
                assert response_json['message'] =='获取数据成功'
                print('会员卡号：%s' % response_json['data']['Data']['vipID'])
        except:
                raise

class Test_dynamic_code():
        #生成会员动态码
        def test_create_dynamic_code(self,headers,menber,menber_register_data):
                data={"CpnID":"0001",   
                        "Code":"",      #卡账号/券账号
                        "Tp":"0",        #帐号类型 0-会员卡、1-优惠券
                        "expires":"5"}   #动态码过期时间(分钟)
                try:
                        data['CpnID'] = menber['CpnID']
                        data['Code'] = menber_register_data['crdID']
                        data['Tp']=0
                        response=requests.post(url=menber['url'] % '/DynamicCode/GetDynamicCode',data=data,headers=headers)
                        response_json=response.json()
                        global response_menber_dynamic_code
                        response_menber_dynamic_code = response_json['data']['dynamicCode']
                        assert response.status_code == 200
                        assert response_json['message'] =='获取数据成功'
                        print('会员动态码：%s' % response_menber_dynamic_code)
                except:
                        raise

        #根据动态码获取会员卡
        def test_check_dynamic_code(self,headers,menber):
                data={"DynamicCode":""} #动态码
                try:
                        data['DynamicCode']=response_menber_dynamic_code
                        response=requests.post(url=menber['url'] % '/DynamicCode/QueryDynamicCode',data=data,headers=headers)
                        response_json=response.json()
                        assert response.status_code == 200
                        assert response_json['message'] =='获取数据成功'
                        print('会员卡账号：%s' % response_json['data']['Data'])
                except:
                        raise
class Test_sign_in():
        #签到
        def test_signin(self,headers,menber,menber_register_data):
                data={
                        "CpnID":"",
                        "SubID":"",
                        "GstID":"",
                        "VipID":"",
                        "Brf":"apitest"
                        }
                try:
                        data['CpnID'] = menber['CpnID']
                        data['SubID'] = menber['SubID']
                        data['GstID']=menber_register_data['gstID']
                        data['VipID']=menber_register_data['crdFaceID']
                        response=requests.post(url=menber['url'] % '/SignIn/SignIn',data=data,headers=headers)
                        response_json=response.json()
                        assert response.status_code == 200
                        assert response_json['message'] =='签到成功'
                        print(response_json['message'])
                except:
                        raise
        #获取签到记录
        def test_signin_record(self,headers,menber,menber_register_data,now_time):
                data={
                        "CpnID":"",
                        "SubID":"",
                        "gstid":"",
                        "EndTime":""
                        }
                try:
                        data['CpnID'] = menber['CpnID']
                        data['SubID'] = menber['SubID']
                        data['gstid']=menber_register_data['gstID']
                        data['EndTime']=now_time['ymd_hms']
                        response=requests.post(url=menber['url'] % '/SignIn/GetSign',data=data,headers=headers)
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

#获取某个会员积分明细
def test_select_integral(headers,menber,menber_register_data):  
        data = {
                 "CpnID":"",
                 "crdNo":"",
                 "pageIndex":"1",
                 "pageSize":"10",
                 "sort":"1",
                }
        try:
                data['CpnID'] = menber['CpnID']
                data['crdNo'] = menber_register_data['crdFaceID']
                response=requests.post(url=menber['url'] % '/IntgAct/GetIntgActPage',data=data,headers=headers)
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
def test_select_menber_sum_integral(headers,menber,menber_register_data):  
        data={
                "CpnID":"",
                "crdNo":""
        }
        try:
                data['CpnID'] = menber['CpnID']
                data['crdNo'] =menber_register_data['crdFaceID']
                response=requests.post(url=menber['url'] % '/Intg/GetIntgSum',data=data,headers=headers)
                response_json=response.json()
                assert response.status_code == 200
                assert response_json['message'] =='数据更新成功'
                print('会员总积分：%s'% response_json['data']['SumIntg'])
        except :
                raise




#获取wifi密码
def test_get_wifi_password(headers,menber):
        data={}
        try:
                data['CpnID'] = menber['CpnID']
                data['SubID'] = menber['SubID']
                response=requests.post(url=menber['url'] % '/Guest/GetWiFi',data=data,headers=headers)
                response_json=response.json()
                assert response.status_code == 200
                if response_json:
                        for i in response_json:
                                print('id:%s；code:%s；name:%s；crtVl:%s;' % (i['id'],i['code'],i['name'],i['crtVl']))
                else:
                        print('没有wifi信息')
        except :
                raise



#会员解绑
def test_menber_untie(headers,menber):
        data={
                "CpnID":"",
                "SubID":"",
                "Tel":""
                }
        try:
                data['CpnID'] = menber['CpnID']
                data['SubID'] = menber['SubID']
                data['Tel']=13183807891
                response=requests.post(url=menber['url'] % '/Guest/UntieBind',data=data,headers=headers)
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


