import pytest
import requests
from comm.comm_way import Way#公共方法
comm_way=Way()








class Test_wx_my():
        #获取首页的会员数据
        def test_get_index_menber_data(self,headers,menber,vipcard_response_data):
                data={}
                try:    
                        data['CpnID'] = menber['CpnID']
                        data['SubID'] = menber['SubID']
                        data['gstID'] = vipcard_response_data['gstID']
                        response=requests.post(url=menber['url'] % '/Guest/GetMainGst',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        print(response_json)
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
        def test_get_vipcard_crdid(self,headers,menber,vipcard_response_data):
                data={}
                try:
                        data['CpnID'] = menber['CpnID']
                        data['crdID'] = vipcard_response_data['crdID']
                        response=requests.post(url=menber['url'] % '/VipCrd/GetByCrdID',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        print(response_json)
                except:
                        raise
        # 获取会员积分统计
        def test_get_integral_statistics(self,headers,manage):
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
                        print(response_json)
                except:
                        raise
        # 获取某个会员积分明细
        def test_get_integral(self,headers,menber,vipcard_response_data):  
                data = {}
                try:
                        data['CpnID'] = menber['CpnID']
                        data['vipID'] = vipcard_response_data['vipID']
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
        def test_get_menber_sum_integral(self,headers,menber,vipcard_response_data):  
                data={}
                try:
                        data['CpnID'] = menber['CpnID']
                        data['vipID'] =vipcard_response_data['vipID']
                        print(data)
                        response=requests.post(url=menber['url'] % '/Intg/GetIntgSum',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        print(response_json)
                except :
                        raise



class Test_dynamic_code():
        #生成会员动态码
        def test_produce_dynamic_code(self,headers,menber,vipcard_response_data):
                data={}   
                try:
                        data['CpnID'] = menber['CpnID']
                        data['Code'] = vipcard_response_data['crdID']   #卡账号/券账号
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
