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
        data={}
        try:
                data['CpnID'] = menber['CpnID']
                data['SubID'] = menber['SubID']
                data['OpnID'] = menber_data_random['OpnID']
                data['Name'] = menber_data_random['Name']
                data['Tel'] = menber_data_random['Tel']
                data['Brth'] = menber_data_random['Brth']
                data['SMSCode'] = '0000'
                data['OrgID'] = ''
                data['IDSource'] = '100'
                data['UserSource'] = ''
                data['Eml'] = ''
                data['IDntTp'] = ''
                data['IDntNmb'] = ''
                data['Sex'] = '1'
                data['Prvc'] = ''
                data['City'] = ''
                data['Addr'] = ''
                data['UnionID'] = ''
                data['JsCode'] = ''
                data['EmployeeNumber'] = ''
                data['AppID'] = ''
                data['AppSecret'] = ''
                # mysql insert request data
                comm_way.sql_insert('register_request',data)
                response=requests.post(url=menber['url'] % '/Guest/Register',data=data,headers=headers)
                response_json = comm_way.response_dispose(response.json())
                print(response_json['Message'])
                assert response.status_code == 200
                assert response_json['Success'] == True
                # mysql insert response data
                comm_way.sql_insert('register_response',response_json['Data']['Data'][0])
                if response_json['Data']['Data']:
                        for i in response_json['Data']['Data']:
                                print(i)
                else:
                        print('没有会员')
        except:
                raise



class Test_dynamic_code():
        #生成会员动态码
        def test_produce_dynamic_code(self,headers,menber,menber_register_response_data):
                data={}   
                try:
                        data['CpnID'] = menber['CpnID']
                        data['Code'] = menber_register_response_data['crdID']   #卡账号/券账号
                        data['Tp']=0    #帐号类型 0-会员卡、1-优惠券
                        data['expires']=5       #动态码过期时间(分钟)
                        response=requests.post(url=menber['url'] % '/DynamicCode/GetDynamicCode',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        global response_menber_dynamic_code
                        response_menber_dynamic_code = response_json['Data']
                        print('dynamicCode:%s；' % response_menber_dynamic_code['dynamicCode'])
                except:
                        raise

        #根据动态码获取会员卡
        def test_check_dynamic_code(self,headers,menber):
                data={} 
                try:
                        data['DynamicCode']=response_menber_dynamic_code['dynamicCode'] #动态码
                        response=requests.post(url=menber['url'] % '/DynamicCode/QueryDynamicCode',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        print('vipID:%s；' % response_json['Data']['Data'])
                except:
                        raise
class Test_sign_in():
        #签到
        def test_signin(self,headers,menber,menber_register_response_data):
                data={}
                try:
                        data['CpnID'] = menber['CpnID']
                        data['SubID'] = menber['SubID']
                        data['GstID'] = menber_register_response_data['gstID']
                        data['VipID'] = menber_register_response_data['crdFaceID']
                        data['Brf'] = "apitest"
                        response=requests.post(url=menber['url'] % '/SignIn/SignIn',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        print(response_json['Message'])
                except:
                        raise
        #获取签到记录
        def test_signin_record(self,headers,menber,menber_register_response_data,now_time):
                data={}
                try:
                        data['CpnID'] = menber['CpnID']
                        data['SubID'] = menber['SubID']
                        data['gstid'] = menber_register_response_data['gstID']
                        data['EndTime'] = now_time['ymd_hms']
                        response=requests.post(url=menber['url'] % '/SignIn/GetSign',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        if response_json['Data']['Data']:
                                for i in response_json['Data']['Data']:
                                        print(i)
                        else:
                                print('没有签到记录')
                except:
                        raise
class Test_index_menber_data():
        #获取首页的会员数据
        def test_get_index_menber_data(self,headers,menber,menber_register_response_data):
                data={}
                try:    
                        data['CpnID'] = menber['CpnID']
                        data['SubID'] = menber['SubID']
                        data['gstID'] = menber_register_response_data['gstID']
                        response=requests.post(url=menber['url'] % '/Guest/GetMainGst',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        print(response_json['Data']['Data'])
                except:
                        raise

        #获取某个会员的全部卡
        def test_get_menber_allcard(self,headers,menber,menber_register_response_data):  
                data={}
                try:
                        data['CpnID'] = menber['CpnID']
                        data['SubID'] = menber['SubID']
                        data['opnID'] = menber_register_response_data['opnID']
                        response=requests.post(url=menber['url'] % '/VipCrd/Get',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        if response_json['Data']['Data']:
                                for i in response_json['Data']['Data']:
                                        print(i)
                        else:
                                print('没有会员卡')
                except:
                        raise

        # 根据卡账户获取单张卡
        def test_get_vipcard_crdid(self,headers,menber,menber_register_response_data):
                data={}
                try:
                        data['CpnID'] = menber['CpnID']
                        data['crdID'] = menber_register_response_data['crdID']
                        response=requests.post(url=menber['url'] % '/VipCrd/GetByCrdID',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        print(response_json['Data']['Data'])
                except:
                        raise
        # 获取会员积分统计
        def test_get_integral_statistics(self,headers,manage,menber_register_response_data):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['VipID'] = ''
                        data['Tel'] =''
                        data['Name'] = ''
                        data['PageIndex'] = '1'
                        data['PageSize'] = '10'
                        data['Sort'] = ''
                        response=requests.post(url=manage['url'] % '/Intg/GetIntgPage',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        print(response_json['Data']['Data'])
                except:
                        raise
        # 获取某个会员积分明细
        def test_get_integral(self,headers,menber,menber_register_response_data):  
                data = {}
                try:
                        data['CpnID'] = menber['CpnID']
                        data['vipID'] = menber_register_response_data['crdFaceID']
                        data['pageIndex'] = 1
                        data['pageSize'] = 10
                        data['sort'] = "uptDtt desc"
                        response=requests.post(url=menber['url'] % '/IntgAct/GetIntgActPage',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        if response_json['Data']['PageDataList']:
                                for i in response_json['Data']['PageDataList']:
                                        print(i)
                        else:
                                print('没有积分明细')
                except:
                        raise

        #查询某个会员总积分
        def test_get_menber_sum_integral(self,headers,menber,menber_register_response_data):  
                data={}
                try:
                        data['CpnID'] = menber['CpnID']
                        data['vipID'] =menber_register_response_data['crdFaceID']
                        response=requests.post(url=menber['url'] % '/Intg/GetIntgSum',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        print('SumIntg:%s；'% response_json['Data']['SumIntg'])
                except :
                        raise


#获取wifi密码
def test_get_wifi_password(headers,menber):
        data={}
        try:
                data['CpnID'] = menber['CpnID']
                data['SubID'] = menber['SubID']
                response=requests.post(url=menber['url'] % '/Guest/GetWiFi',data=data,headers=headers)
                response_json = comm_way.response_dispose(response.json())
                assert response.status_code == 200
                if response_json:
                        for i in response_json:
                                print(i)
                else:
                        print('没有wifi信息')
        except :
                raise



#会员解绑
def test_menber_untie(headers,menber):
        data={}
        try:
                data['CpnID'] = menber['CpnID']
                data['SubID'] = menber['SubID']
                data['Tel']=13183807891
                response=requests.post(url=menber['url'] % '/Guest/UntieBind',data=data,headers=headers)
                response_json = comm_way.response_dispose(response.json())
                print(response_json)
                assert response.status_code == 200
                assert response_json['Success'] == True
        except:
                raise



class Test_upload_ticket():
        #上传小票到s3
        def test_upload_ticket_s3(self,headers,menber,get_s3_ticket):   
                data={}
                try:
                        data['CpnID'] = menber['CpnID']
                        response=requests.post(url=menber['url'] % '/Guest/UnloadPic',files=get_s3_ticket['ticket'],data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        # mysql insert response data
                        comm_way.sql_insert('upload_ticket_response',response_json['Data'])
                except:
                        raise
                
        #上传小票
        def test_upload_ticket(self,headers,menber,menber_register_request_data,upload_ticket_response_data):
                data={}
                try:
                        data['CpnID'] = menber['CpnID']
                        data['SubID'] = menber['SubID']
                        data['OpenID'] = menber_register_request_data['OpnID']
                        data['ImgURL'] = upload_ticket_response_data['Data']
                        response=requests.post(url=menber['url'] % '/BllImg/UploadUsrBllImg',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                except:
                        raise

        #查询用户小票上传记录分页
        def test_get_upload_ticket_record(self,headers,menber,menber_register_response_data):
                data={}
                try:
                        data['CpnID'] = menber['CpnID']
                        data['SubID'] = menber['SubID']
                        data['CrdID'] = menber_register_response_data['crdID']
                        data['PageIndex'] = 1
                        data['PageSize'] = 10
                        response=requests.post(url=menber['url'] % '/BllImg/QueryUsrBllImgPage',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        if response_json['Data']['BllImgList']:
                                for i in response_json['Data']['BllImgList']:
                                        print(i)
                        else:
                                print('没有上传记录')
                except:
                        raise


class Test_car():
        # 添加会员车辆信息
        def test_add_car_data(self,headers,menber,menber_register_response_data,car_data_random):
                data={}
                try:
                        data['CpnID'] = menber['CpnID']
                        data['SubID'] = menber['SubID']
                        data['GstID'] = menber_register_response_data['gstID']
                        data['CarID'] = car_data_random['CarID']         #车牌号
                        data['CarTp'] = car_data_random['carTp']
                        data['IsEv'] = 0                                #是否新能源
                        data['IsSupIntgAuto'] = 1                       #是否支持自动积分
                        data['Stt'] = 0
                        data['Brf'] = 'apitest'
                        data['OldCarID']=''
                        response=requests.post(url=menber['url'] % '/GstCar/AddGstCar',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        comm_way.sql_insert('car_data_response',response_json['Data']['Data'][0])
                        
                except:
                        raise
        #修改用户车辆信息
        def test_update_car_data(self,headers,menber,car_data_response_data,car_data_random,now_time):
                data={}
                try:
                        data['CpnID'] = menber['CpnID']
                        data['ID'] = car_data_response_data['id']
                        data['GstID'] = car_data_response_data['gstID']
                        data['CarID'] = car_data_random['CarID']  
                        data['CarTp'] = car_data_random['carTp']
                        data['IsEv'] = car_data_response_data['isEv']
                        data['IsSupIntgAuto'] = car_data_response_data['isSupIntgAuto']
                        data['Stt'] = car_data_response_data['stt']
                        data['Brf'] = 'update test'
                        data['UptDtt'] = now_time['ymd_hms']
                        data['Parm'] = 'CarID,CarTp,Brf'         #修改字段
                        response=requests.post(url=menber['url'] % '/GstCar/UpGstCar',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        # mysql insert response data
                        comm_way.sql_insert('car_data_response',response_json['Data']['Data'][0])  
                except:
                        raise

        #获取当前用户车牌号
        def test_get_user_car_data(self,headers,menber,menber_register_response_data):
                data={}
                try:
                        data['CpnID'] = '0001'
                        data['GstID'] = menber_register_response_data['gstID']
                        response=requests.post(url=menber['url'] % '/GstCar/GetGstCar',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        if response_json['Data']:
                                for i in response_json['Data']['Data']:
                                        print(i)
                        else:
                                print('没有车辆信息')
                except:
                        raise

#积分商城
class Test_integral_shopping_mail():
        def test_commodity_list(self,headers,menber):
                data={}
                try:
                        data['CpnID'] = menber['CpnID']
                        data['SubID'] = menber['SubID']
                        data['SortType'] = '0'    #排序类型[1：默认、热门倒序;2：积分从小到大；3：积分从大到小；4:上架时间]
                        data['MinIntg'] = '0'
                        data['MaxIntg'] = '1000'
                        data['PageIndex'] = 1
                        data['PageSize'] = 10
                        response=requests.post(url=menber['url'] % '/IntgShop/QueryGoodsList',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json)
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                except:
                        raise



# 券账户
class Test_menber_ticket_account():
        # 发送优惠券
        def test_send_ticket(self,headers,menber,menber_register_response_data,ticket_seed_response_data):
                data={}
                try:
                        data['CpnID'] = menber['CpnID']
                        data['CrdNos'] = menber_register_response_data['crdFaceID']        # 会员卡面号集合
                        data['TknID'] = ticket_seed_response_data['tknID']         # 券种编号
                        data['TknAmt'] = '30'        # 券金额
                        data['SendCount'] = 1     # 发送券的数量，默认发送一张
                        data['IsSendMsg'] = 0    # 是否发送模板消息(1-是，0-否，默认是)
                        print(data)
                        response=requests.post(url=menber['url'] % '/Dtkt/SendTknAcc',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json)
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                except:
                        raise
        # 获取用户各个券类型下的优惠券数量
        def test_get_user_ticket_seed_number(self,headers,menber,menber_register_response_data):
                data={}
                try:
                        data['CpnID'] = menber['CpnID']
                        data['SubID'] = menber['SubID']     
                        data['VipID'] = menber_register_response_data['crdFaceID']         
                        data['CrdID'] = menber_register_response_data['crdID']  
                        response=requests.post(url=menber['url'] % '/Dtkt/GetDtktTypeCount',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        if response_json['Data']['Data']:
                                for i in response_json['Data']['Data']:
                                        print(i)
                        else:
                                print('没有券类型/优惠券')
                except:
                        raise
        # 分页获取当前用户的优惠券
        def test_get_user_ticket_page(self,headers,menber,menber_register_response_data):
                data={}
                try:
                        data['CpnID'] = menber['CpnID']
                        data['VipID'] = menber_register_response_data['crdFaceID']        
                        data['CrdID'] = menber_register_response_data['crdID']        
                        data['TknIDS'] = ''    # 券种ID
                        data['PgIndex'] = 1       
                        data['PgSize'] = 10     
                        response=requests.post(url=menber['url'] % '/Dtkt/GetDtkt',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        if response_json['Data']['DtktList']:
                                for i in response_json['Data']['DtktList']:
                                        print(i)
                        else:
                                print('没有优惠券')
                except:
                        raise
        # 查询用户已使用或已过期的优惠券
        def test_get_user_past_ticket(self,headers,menber,menber_register_response_data):
                data={}
                try:
                        data['CpnID'] = menber['CpnID']
                        data['VipID'] = menber_register_response_data['crdFaceID']        
                        data['CrdID'] = menber_register_response_data['crdID']        
                        data['LastUnionID'] = ''    
                        data['pageSize'] = '10'       
                        data['QueryType'] = 0     #查询类型[0:全部，1:已使用，2:过期，默认:0]
                        response=requests.post(url=menber['url'] % '/Dtkt/GetUsedDtkt',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        if response_json['Data']['UsedDtktList']:
                                for i in response_json['Data']['UsedDtktList']:
                                        print(i)
                        else:
                                print('没有过期优惠券')
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


