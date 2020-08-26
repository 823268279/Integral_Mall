import pytest
import requests
import random
from comm.comm_way import Way#公共方法
comm_way=Way()

class Test_staff_register_login():
         # 新增店铺员工
        # def test_add_staff(self,manage,headers,now_time):
        #         data={}
        #         try:
        #                 data['CpnID'] = manage['CpnID']
        #                 data['SubID'] = manage['SubID']
        #                 data['ID'] = '0'
        #                 data['StffID'] = '324368'     #员工编号
        #                 data['OrgID'] = '0000'      #机构代码
        #                 data['StoreID'] = 'Mall'    #店铺编号
        #                 data['Name'] = 'wowo'       #员工姓名
        #                 data['Pwd'] = '1001'        #密码
        #                 data['Gnd'] = '0'        #性别
        #                 data['MPhone'] = '13183807891'     #电话
        #                 data['ChkWrd'] = ''     #校验字
        #                 data['Stt'] = '0'        #状态[0-正常，1-禁用]
        #                 data['Deleted'] = 'N'    #删除状态[N-正常，Y-禁用]
        #                 data['Uptr'] = manage['username']
        #                 data['UptDtt'] = now_time['ymd_hms']
        #                 response=requests.post(url=manage['url'] % '/StoreStff/AddStoreStff',data=data,headers=headers)
        #                 response_json = comm_way.response_dispose(response.json())
        #                 print(response_json['Message'])
        #                 assert response.status_code == 200
        #                 assert response_json['Success'] == True
        #         except:
        #                 raise
                
        # 查询员工
        def test_get_staff_list(self,manage,headers):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['SubID'] = manage['SubID']
                        data['IsDel'] = 'N'
                        data['Name'] = 'wowo'
                        data['OrgID'] = '0000'
                        data['StffID'] = '324368'
                        data['StoreID'] = 'Mall'
                        data['MPhone'] = '13183807891'
                        data['PageIndex'] = '0'
                        data['PageSize'] = '10'
                        data['Stt'] = '-1'
                        response=requests.post(url=manage['url'] % '/StoreStff/UpStoreStff',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        if response_json['Data']['Data']:
                                # mysql insert staff_list response data
                                comm_way.sql_insert('staff_page_response_data',response_json['Data']['Data'][0])
                                for i in response_json['Data']['Data']:
                                        print(i)

                        else:
                                print('none staff')
                except:
                        raise
        # 员工登陆
        def test_staff_login(self,manage,headers,staff_page_response_data):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['SubID'] = manage['SubID']
                        data['StffID'] = staff_page_response_data['stffID']
                        data['Pwd'] = staff_page_response_data['pwd']
                        response=requests.post(url=manage['url'] % '/StoreStff/StoreStffLogin',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json)
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                except:
                        raise

# 核销
class Test_check():
        # 订单核销
        def test_order_check(self,headers,manage,personal_order_page_response_data,staff_page_response_data):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['SubID'] = manage['SubID']
                        data['BllID'] = personal_order_page_response_data['bllID']      #订单号
                        data['AccTyp'] = '0'          #核销类型(0-积分商城订单,1-礼品券)  
                        data['StffID'] = staff_page_response_data['stffID']       #核销人
                        data['OrgID'] = '0000'      #机构号
                        data['StoreID'] = ''    #店铺号
                        data['DtlID'] = personal_order_page_response_data['id']    #兑换订单子表ID(不填则核销所有商品)(针对积分商城订单时有效)
                        data['Takeaway'] = '1'   #核销来源[1_电脑提货，2_扫码提货]
                        print(data)
                        response=requests.post(url=manage['url'] % '/StoreStff/WriteOff',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                except:
                        raise
        # 获取核销首页数据
        def test_get_check_system_index(self,headers,manage,staff_page_response_data):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['SubID'] = manage['SubID']
                        data['StffID'] = staff_page_response_data['stffID']      #员工ID
                        data['QueType'] = '1'     #年月日类型[1 全部 0 年 1 月 2 日]
                        response=requests.post(url=manage['url'] % '/StoreStff/GetWriteOff',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        print(response_json['Data']['Data'])
                except:
                        raise
        # 根据订单号获取核销商品详情
        def test_get_check_commodity(self,headers,manage,shop_order_page_response_data):
                data={}
                try:
                        data['BllNO'] = shop_order_page_response_data['id']
                        response=requests.post(url=manage['url'] % '/StoreStff/GetWriteOffData',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        print(response_json['Data']['Data'])

                except:
                        raise
        # 获取核销历史
        def test_get_check_history(self,headers,manage,staff_page_response_data):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['SubID'] = manage['SubID']
                        data['StffID'] = staff_page_response_data['stffID']       #员工ID
                        data['PgIndex'] = '1'
                        data['PgSize'] = '10'


                        print(data)
                        response=requests.post(url=manage['url'] % '/StoreStff/GetWriteOffPg',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        print(response_json['Data']['Data'])

                except:
                        raise