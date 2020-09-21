import pytest
import requests
import json
from comm.comm_way import Way#公共方法
comm_way=Way()





# 积分规则
class Test_integral_rule():
        # 新增积分规则
        def test_add_integral_rule(self,headers,manage,member_response_data,store_page_response_data,integral_rule_data_random,now_time):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['SubID'] = manage['SubID']
                        data['ID'] = '0'         #序号
                        data['OrgID'] = member_response_data['orgID']      #机构
                        data['VipTp'] = member_response_data['vipTpID']      #会员类型
                        data['SetTp'] = '3'      #设置类型[0-不限，1-类别，2-品牌，3-店铺，4-单品]
                        data['Code'] = store_page_response_data['storeID']       #类型编码
                        data['IntgrTyp'] = '0'   #积分类型[0-积分，1-金币]
                        data['Amt'] = integral_rule_data_random['Amt']        #积分线
                        data['Intgr'] = integral_rule_data_random['Intgr']      #积分值
                        data['RecTyp'] = '1'     #计算方式[0-兑换率，1-消费总额]
                        data['CanlFlg'] = '0'    #取消标志[0-正常，1-取消]
                        data['Brf'] = '积分规则'    
                        data['Uptr'] = manage['username']    
                        data['UptDtt'] = now_time['ymd']
                        print(data)
                        response=requests.post(url=manage['url'] % '/IntgRulexct/EditIntgRule',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        print(response_json)
                except:
                        raise
        # 获取积分规则
        def test_get_integral_rule_page(self,headers,manage,member_response_data):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['SubID'] = manage['SubID']
                        data['OrgID'] = member_response_data['orgID']
                        data['VipTpID'] = member_response_data['vipTpID']
                        data['SetTp'] = ''      #设置类型[0-不限，1-类别，2-品牌，3-店铺，4-单品]
                        data['IntgrTyp'] = ''   #积分类型[0-积分，1-金币]
                        data['PageIndex'] = '1'
                        data['PageSize'] = '100'
                        response=requests.post(url=manage['url'] % '/IntgRulexct/GetIntgRulePage',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        if response_json['Data']['List']:
                                comm_way.sql_insert("integral_rule_response_data",response_json['Data']['List'][0])
                                for i in response_json['Data']['List']:
                                        print(i)
                        else:
                                print('没有积分规则')
                except:
                        raise
        # 获取积分规则
        def test_get_integral_rule(self,headers,manage,integral_rule_response_data):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['SubID'] = manage['SubID']
                        data['IntgRuleID'] = integral_rule_response_data['id']
                        response=requests.post(url=manage['url'] % '/IntgRulexct/GetSingleIntgRule',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        print(response_json)
                except:
                        raise

# 积分系数
class Test_integral_coefficient():
        # 添加积分系数
        def test_add_integral_coefficient(self,headers,manage,member_response_data,store_page_response_data,now_time):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['SubID'] = manage['SubID']
                        data['ID'] = '0'
                        data['BllNo'] = ''
                        data['OrgID'] = member_response_data['orgID']    #ALL表示全部机构
                        data['VipTp'] = member_response_data['vipTpID']
                        data['Tp'] = '0'         #特殊节日[0-非特殊，1-生日积分]
                        data['CodeType'] = '3'   #代码类型[0-不限，1-类别，2-品牌，3-店铺，4-单品]
                        data['Code'] = store_page_response_data['storeID']       #类型编码
                        data['IntgrTyp'] = '1'   #积分类型[0-金币，1-积分]
                        data['Amt'] = '100'        #积分线
                        data['Intgr'] = '300'      #积分值
                        data['RecTyp'] = '1'     #计算方式[0-兑换率，1-消费总额]
                        data['StDt'] = now_time['StDt']      
                        data['EdDt'] = now_time['EdDt']  
                        data['Intgcof'] = '2'    #积分系数
                        data['CanlFlg'] = '0'    #取消标志[1-是，0-否]
                        data['Uptr'] = manage['username']
                        data['UptDtt'] = now_time['ymd_hms']
                        data['Brf'] = 'apitest'
                        response=requests.post(url=manage['url'] % '/IntgCofexct/EditIntgCofexct',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        print(response_json)
                except:
                        raise
        # 获取积分系数分页
        def test_get_integral_coefficient_page(self,headers,manage):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['SubID'] = manage['SubID']
                        data['VipTpID'] = ''
                        data['SetTp'] = ''
                        data['IntgrType'] = ''
                        data['IsBrth'] = ''
                        data['Stt'] = ''
                        data['PageIndex'] = '1'
                        data['PageSize'] = '10'
                        response=requests.post(url=manage['url'] % '/IntgCofexct/GetIntgCofexctPage',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        if response_json['Data']['IntgCofexctList']:
                                comm_way.sql_insert('integral_coefficient_page_response_data',response_json['Data']['IntgCofexctList'][0])
                                for i in response_json['Data']['IntgCofexctList']:
                                        print(i)
                        else:
                                print('没有积分系数')
                except:
                        raise   
        # 获取单个积分系数
        def test_get_integral_coefficient(self,headers,manage,integral_coefficient_page_response_data):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['SubID'] = manage['SubID']
                        data['CofexctID'] = integral_coefficient_page_response_data['id']
                        response=requests.post(url=manage['url'] % '/IntgCofexct/GetSingleIntgCofexct',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        print(response_json)
                except:
                        raise 


# 会员特权
class Test_member_privilege():
        # 添加会员特权
        def test_add_member_privilege(self,headers,manage,member_response_data,now_time):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['SubID'] = manage['SubID']
                        data['ID'] = ''
                        data['VipTpID'] = member_response_data['vipTpID']
                        data['Title'] = '生日特权'      #特权标题
                        data['Intro'] = ''      #特权描述
                        data['Rdx'] = '0'        #排序
                        data['StDt'] = now_time['StDt']       
                        data['EdDt'] = now_time['EdDt']
                        data['Deleted'] = 'Y'    #删除状态[N-正常，Y-删除]
                        data['Uptr'] = now_time['username']
                        data['UptDtt'] = now_time['ymd_hms']
                        data['Brf'] = ''
                        response=requests.post(url=manage['url'] % '/MbrPrv/EditMbrPrc',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        print(response_json)
                except:
                        raise
        # 获取会员特权列表
        def test_get_member_privilege_page(self,headers,manage):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['SubID'] = manage['SubID']
                        data['MbrID'] = ''
                        data['VipTpID'] = ''
                        data['Title'] = ''
                        data['StdtDate'] = ''
                        data['EndDate'] = ''
                        data['PageIndex'] = '1'
                        data['PageSize'] = '10'
                        response=requests.post(url=manage['url'] % '/MbrPrv/QueryMvrPrvList',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json)
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        print(response_json)
                except:
                        raise