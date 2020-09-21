import pytest
import requests
from comm.comm_way import Way#公共方法
comm_way=Way()








class Test_wx_my():
        #获取首页的会员数据
        def test_get_index_member_data(self,headers,member,vipcard_response_data):
                data={}
                try:    
                        data['CpnID'] = member['CpnID']
                        data['SubID'] = member['SubID']
                        data['gstID'] = vipcard_response_data['gstID']
                        print(data)
                        response=requests.post(url=member['url'] % '/Guest/GetMainGst',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        print(response_json)

                except:
                        raise

        #获取某个会员的全部卡
        def test_get_member_allcard(self,headers,member,register_response_data):  
                data={}
                try:
                        data['CpnID'] = member['CpnID']
                        data['SubID'] = member['SubID']
                        data['opnID'] = register_response_data['opnID']
                        response=requests.post(url=member['url'] % '/VipCrd/Get',data=data,headers=headers)
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
        def test_get_vipcard_crdid(self,headers,member,vipcard_response_data):
                data={}
                try:
                        data['CpnID'] = member['CpnID']
                        data['crdID'] = vipcard_response_data['crdID']
                        response=requests.post(url=member['url'] % '/VipCrd/GetByCrdID',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        print(response_json)
                except:
                        raise
        # 获取积分明细
        def test_get_integral_statistics(self,headers,member,vipcard_response_data):
                data={}
                try:
                        data['CpnID'] = member['CpnID']
                        data['VipID'] = vipcard_response_data['vipID']
                        data['CrdNo'] = ''
                        data['BeginDate'] =''
                        data['EndDate'] = ''
                        data['BllType'] = ''
                        data['PageIndex'] = '1'
                        data['PageSize'] = '10'
                        data['Sort'] = ''
                        response=requests.post(url=member['url'] % '/Intg/GetIntgPage',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        if response_json['Data']['Lst']:
                                for i in response_json['Data']['Lst']:
                                        print(i)
                        else:
                                print('没有积分明细')
                except:
                        raise

        #查询某个会员总积分
        def test_get_member_sum_integral(self,headers,member,vipcard_response_data):  
                data={}
                try:
                        data['CpnID'] = member['CpnID']
                        data['OrgID'] = vipcard_response_data['useOrgID']
                        data['vipID'] = vipcard_response_data['vipID']
                        response=requests.post(url=member['url'] % '/Intg/GetIntgSum',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        print(response_json)
                except :
                        raise



class Test_dynamic_code():
        #生成会员动态码
        def test_produce_dynamic_code(self,headers,member,vipcard_response_data):
                data={}   
                try:
                        data['CpnID'] = member['CpnID']
                        data['Code'] = vipcard_response_data['crdID']   #卡账号/券账号
                        data['Tp']=0    #帐号类型 0-会员卡、1-优惠券
                        data['expires']=5       #动态码过期时间(分钟)
                        response=requests.post(url=member['url'] % '/DynamicCode/GetDynamicCode',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        global response_member_dynamic_code
                        response_member_dynamic_code = response_json['Data']
                        print('dynamicCode:%s；' % response_member_dynamic_code['dynamicCode'])
                except:
                        raise

        #根据动态码获取会员卡
        def test_check_dynamic_code(self,headers,member):
                data={} 
                try:
                        data['DynamicCode']=response_member_dynamic_code['dynamicCode'] #动态码
                        response=requests.post(url=member['url'] % '/DynamicCode/QueryDynamicCode',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        print('vipID:%s；' % response_json['Data']['Data'])
                except:
                        raise

# 查询订单分页
def test_get_order_page(headers,member,vipcard_response_data):
        data={}
        try:
                data['CpnID'] = member['CpnID']
                data['SubID'] = member['SubID']
                data['GstID'] = vipcard_response_data['gstID']
                data['PageIndex'] = '1'
                data['PageSize'] = '10'
                data['Stt'] = '-1'
                response=requests.post(url=member['url'] % '/IntgShop/QueryPhoneCnvrtOrderList',data=data,headers=headers)
                response_json = comm_way.response_dispose(response.json())
                print(response_json['Message'])
                assert response.status_code == 200
                assert response_json['Success'] == True
                if response_json['Data']['Data']:
                        comm_way.sql_insert('personal_order_page_response_data',response_json['Data']['Data'][0])
                        for i in response_json['Data']['Data']:
                                print(i)
                else:
                        print('没有订单')
        except:
                raise
        
#会员解绑
def test_member_untie(headers,member):
        data={}
        try:
                data['CpnID'] = member['CpnID']
                data['SubID'] = member['SubID']
                data['Tel']=13183807891
                response=requests.post(url=member['url'] % '/Guest/UntieBind',data=data,headers=headers)
                response_json = comm_way.response_dispose(response.json())
                print(response_json)
                assert response.status_code == 200
                assert response_json['Success'] == True
        except:
                raise
