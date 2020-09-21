import pytest
import requests
import json
import random
from comm.comm_way import Way#公共方法
comm_way=Way()



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
                                        comm_way.sql_insert('ticket_type_page_response_data',response_json['Data']['PageDataList'][0])
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
                        data['TknID'] = ticket_data_random['TknID']                 #券种代码
                        data['Name'] = ticket_data_random['Name']                   #券名称
                        data['Tknvl'] = ticket_data_random['Tknvl']                 #券面额
                        data['ConsumeMoney'] = ticket_data_random ['ConsumeMoney']  #消费满多少金额可用
                        data['TknImg'] = ''                                         #券图片
                        data['TknDsc'] = ''                                         #券图文描述
                        data['TknTpID'] = ticket_type_page_response_data['tknTpID'] #券类代码
                        data['SndRul'] = ticket_data_random['SndRul']               #发券规则
                        data['RcvRul'] = ''                                         #受券规则
                        data['VipTpID'] = ''                                        #会员类型
                        data['BrfId'] = ''
                        data['SDt'] = now_time['StDt']                              #开始时间
                        data['EDt'] = now_time['EdDt']                              #结束时间
                        data['TStt'] = 'F'                                          #找补状态
                        data['UseSDy'] = '0'                                        #发放后N天有效
                        data['UseADy'] = '0'                                        #有效期天数
                        data['TknSdt'] = ''                                         #券使用开始日期
                        data['TknEdt'] = ''                                         #券使用结束日期
                        data['RjcStt'] = 'F'                                        #排斥状态
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
                                        comm_way.sql_insert('ticket_seed_page_response_data',response_json['Data']['PageDataList'][0])
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


# 领券活动
class Test_ticket_activity():
        # 添加券活动
        def test_add_ticket_activity(self,headers,manage,ticket_seed_page_response_data,now_time):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['SubID'] = manage['SubID']
                        data['BllNo'] = ""
                        data['Sbjc'] = "国庆大放送"   #主题
                        data['Pic'] = "0"    #活动主图
                        data['Intro'] = ticket_seed_page_response_data['name']    #活动描述
                        data['ActvType'] = "1" #活动类型
                        data['MenuType'] = "0" #菜单类型
                        data['Lktsdt'] = now_time['StDt']   #开始日期
                        data['Lktedt'] = now_time['EdDt']   #结束日期
                        data['TknID'] = ticket_seed_page_response_data['tknID']    #券种
                        data['CrdID'] = "0"    #券套
                        data['VipTp'] = "01"    #会员类型
                        data['TknTyp'] = "0"
                        data['MaxNum'] = "10"   #每人最大领取总数
                        data['ShowOrder'] = "1" #显示顺序
                        data['DayDegre'] = "2" #每人每日领取数
                        data['QityNum'] = "500"  #总数量
                        data['IsDay'] = "1"    #是否每日发放(0-按总量发放、1-每日发放)
                        data['DayNum'] = "100"   #每日发放总数
                        data['Amt'] = ticket_seed_page_response_data['tknvl']      #券金额
                        data['Brf'] = "领券"      #备注
                        data['Stt'] = "0"      #状态
                        data['IsStop'] = "0"   #是否终止
                        data['Deleted'] = "N"  #删除状态
                        data['Uptr'] = manage['username']     #更新人
                        data['UptDtt'] = now_time['ymd_hms']   #更新时间
                        response=requests.post(url=manage['url'] % '/VoucherLkdrw/EditVoucherLkdrw',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json)
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                except:
                        raise
        # pc端查询领券活动中心分页
        def test_pc_get_ticket_activity_page(self,headers,manage):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['SubID'] = manage['SubID']
                        data['BllNo'] = ""
                        data['Sbjc'] = ""
                        data['Lkrsdt'] = ""
                        data['Lkteddt'] = ""
                        data['TknID'] = ""
                        data['PageIndex'] = "1"
                        data['PageSize'] = "10"
                        response=requests.post(url=manage['url'] % '/VoucherLkdrw/QueryVoucherLkdrwList',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        if response_json['Data']['List']['data']:
                                comm_way.sql_insert('ticket_activity_response_data',response_json['Data']['List']['data'][-1])
                                for i in response_json['Data']['List']['data']:
                                        print(i)
                        else:
                                print('没有券活动')
                except:
                        raise
        # 修改券活动
        def test_update_ticket_activity(self,headers,manage,ticket_activity_response_data,now_time):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['SubID'] = manage['SubID']
                        data['BllNo'] = ticket_activity_response_data['bllNo']
                        data['Sbjc'] = ticket_activity_response_data['sbjc']   #主题
                        data['Pic'] = ticket_activity_response_data['pic']    #活动主图
                        data['Intro'] = ticket_activity_response_data['intro']    #活动描述
                        data['ActvType'] = ticket_activity_response_data['actvType'] #活动类型
                        data['MenuType'] = ticket_activity_response_data['menuType'] #菜单类型
                        data['Lktsdt'] = ticket_activity_response_data['lktsdt']   #开始日期
                        data['Lktedt'] = ticket_activity_response_data['lktedt']  #结束日期
                        data['TknID'] = ticket_activity_response_data['tknID']    #券种
                        data['CrdID'] = ticket_activity_response_data['crdID']    #券套
                        data['VipTp'] = ticket_activity_response_data['vipTp']    #会员类型
                        data['TknTyp'] = ticket_activity_response_data['tknTyp']
                        data['MaxNum'] = ticket_activity_response_data['maxNum']   #每人最大领取总数
                        data['ShowOrder'] = ticket_activity_response_data['showOrder'] #显示顺序
                        data['DayDegre'] = ticket_activity_response_data['dayDegre'] #每人每日领取数
                        data['QityNum'] = ticket_activity_response_data['qityNum']  #总数量
                        data['IsDay'] = ticket_activity_response_data['isDay']    #是否每日发放(0-按总量发放、1-每日发放)
                        data['DayNum'] = ticket_activity_response_data['dayNum']   #每日发放总数
                        data['Amt'] = ticket_activity_response_data['amt']      #券金额
                        data['Brf'] = "领券"      #备注
                        data['Stt'] = "50"      #状态
                        data['IsStop'] = "0"   #是否终止
                        data['Deleted'] = "N"  #删除状态
                        data['Uptr'] = manage['username']     #更新人
                        data['UptDtt'] = now_time['ymd_hms']   #更新时间
                        print(data)
                        response=requests.post(url=manage['url'] % '/VoucherLkdrw/EditVoucherLkdrw',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        print(response_json)
                except:
                        raise
        # 微信端查询领券活动中心分页
        def test_wx_get_ticket_activity_page(self,headers,member,register_response_data):
                data={}
                try:
                        data['CpnID'] = member['CpnID']
                        data['SubID'] = member['SubID']
                        data['GstID'] = register_response_data['gstID']
                        data['OpenID'] = register_response_data['opnID']
                        data['IsReceive'] = "received" #展示列表(all所有、received已领取、available未领取)
                        data['PageIndex'] = "1"
                        data['PageSize'] = "10"
                        data['Sort'] = "1"
                        response=requests.post(url=member['url'] % '/VoucherLkdrw/QueryVoucherLkdrwList',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        if response_json['Data']['PageDataList']:
                                for i in response_json['Data']['PageDataList']:
                                        print(i)
                        else:
                                print('没有券活动')
                except:
                        raise
        # 微信端会员领券
        def test_wx_get_ticket(self,headers,member,register_response_data,ticket_activity_response_data):
                data={}   
                try:
                        data['CpnID'] = member['CpnID']
                        data['SubID'] = member['SubID']
                        data['BllNo'] = ticket_activity_response_data['bllNo']
                        data['OpenID'] = register_response_data['opnID']
                        print(data)
                        response=requests.post(url=member['url'] % '/VoucherLkdrw/JoinVoucherLkdrw',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        print(response_json)
                except:
                        raise  

# 活动相关
class Test_activity():
        # 获取活动券列表
        def test_get_activity_ticket(self,headers,member):
                data={}
                try:
                        data['CpnID'] = member['CpnID']
                        data['SubID'] = member['SubID']
                        data['OpnID'] = ''     
                        data['LkdrwBllNo'] = ''        
                        data['LkdrwGftGdsID'] = ''
                        data['PageIndex'] = '1'
                        data['PageSize'] = '10'
                        data['Key'] = '0'        #是否已领取[0-全部，1-已领取，2-未领取]
                        print(data)
                        response=requests.post(url=member['url'] % '/Lkdrw/GetUserLkdrwGftLst',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        print(response_json)
                except:
                        raise 
        # 添加活动等级
        def test_activity_level(self,headers,manage,now_time):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['SubID'] = manage['SubID']
                        data['BllNo'] = '2436425231'   
                        data['Lvl'] = '1'        #档次      
                        data['LvName'] = '活动等级'      #档次名称
                        data['Intro'] = '活动等级'       #描述
                        data['LvlImg'] = '0'      #档次图片
                        data['IsFix'] = '0'       #是否固定奖品[0-固定，1-可选] 
                        data['OptQty'] = '0'      #可选数量
                        data['LttQty'] = '10'      #奖品份数
                        data['LttPrb'] = '0.8'      #中奖几率
                        data['SndQty'] = '1'      #出奖份数
                        data['WinMbl'] = ''      #指定中奖人手机号
                        data['CanlFlg'] = '0'     #取消标志[0-否，1-是]
                        data['UptDtt'] = now_time['ymd']      
                        data['Brf'] = '活动等级'      
                        print(data)
                        response=requests.post(url=manage['url'] % '/Lkdrw/EditLkdrwLvl',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        print(response_json)
                except:
                        raise 




# 获取活动券列表
def test_zz(headers,member):
        data={}
        try:
                data['CpnID'] = member['CpnID']
                data['SubID'] = member['SubID']
                data['OpnID'] = ''
                data['LkdrwBllNo'] = ''
                data['LkdrwGftGdsID'] = ''
                data['PageIndex'] = '1'
                data['PageSize'] = '10'
                data['Key'] = '0'
                print(data)  
                response=requests.post(url=member['url'] % '/Lkdrw/GetUserLkdrwGftLst',data=data,headers=headers)
                response_json = comm_way.response_dispose(response.json())
                print(response_json)
                print(response_json['Message'])
                assert response.status_code == 200
                assert response_json['Success'] == True
        except:
                raise


# 分页查询活动信息
def test_get_activity_page(headers,manage):
        data={}
        try:
                data['CpnID'] = manage['CpnID']
                data['SubID'] = manage['SubID']
                data['BllNo'] = ''
                data['Sbjc'] = ''
                data['ActvType'] = ''
                data['Lktype'] = ''
                data['StartDate'] = ''
                data['EndDate'] = ''
                data['PageIndex'] = '1'
                data['PageSize'] = '10'
                print(data)  
                response=requests.post(url=manage['url'] % '/Lkdrw/QueryLkdrwList',data=data,headers=headers)
                response_json = comm_way.response_dispose(response.json())
                print(response_json)
                print(response_json['Message'])
                assert response.status_code == 200
                assert response_json['Success'] == True
        except:
                raise