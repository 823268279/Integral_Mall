import pytest
import requests
from comm.comm_way import Way#公共方法
comm_way=Way()




# 店铺资料
class Test_store_data():
        # 添加店铺
        def test_add_store(self,headers,manage,now_time,store_data_random,commodity_data_random):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['SubID'] = manage['SubID']  
                        data['OrgID'] = '0000'
                        data['StoreID'] = store_data_random['StoreID']    #店铺编码
                        data['Name'] = commodity_data_random['commodity_brand']         #店铺名称
                        data['Logo'] = ''         #店铺logo
                        data['Tel'] = store_data_random['Tel']          #店铺电话
                        data['Cls'] = ''          #业种
                        data['Flr'] = ''         #楼层
                        data['FlrNo'] = ''        #门牌号
                        data['Intro'] = '店铺'        #图文描述
                        data['Stt'] = '0'          #状态[0_正常，-1_禁用]
                        data['Deleted'] = 'N'      #删除状态[N_正常，Y_删除]
                        data['RealImg'] = ''      #店铺照片
                        data['Uptr'] = manage['username']
                        data['UptDtt'] = now_time['ymd_hms']
                        print(data)
                        response=requests.post(url=manage['url'] % '/Store/AddStore',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                except:
                        raise
        # 获取店铺分页
        def test_get_store_page(self,headers,manage):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['SubID'] = manage['SubID']  
                        data['OrgID'] = '0000'
                        data['StoreID'] = ''
                        data['Name'] = ''
                        data['Logo'] = ''
                        data['Tel'] =  ''
                        data['Cls'] = ''
                        data['Flr'] = ''
                        data['FlrNo'] = ''
                        data['Intro'] = ''
                        data['Stt'] = ''
                        data['Deleted'] = ''
                        data['RealImg'] = ''
                        data['Uptr'] = manage['username']
                        data['PgIndex'] = '1'
                        data['PgSize'] = '10'
                        print(data)
                        response=requests.post(url=manage['url'] % '/Store/GetStore',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                except:
                        raise
        # 获取所有可用店铺
        def test_get_store_all_usable(self,headers,manage):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['SubID'] = manage['SubID']  
                        data['Del'] = 'N'       # 删除状态[N_正常，Y_删除]
                        data['Stt'] = '0'       # 启动状态[0_正常，1_禁用]
                        print(data)
                        response=requests.post(url=manage['url'] % '/Store/GetAvailableStore',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                except:
                        raise

# 商品资料
class Test_commodity_data():
        # 新增商品基础资料
        def test_add_commodity_data(self,headers,manage,now_time,commodity_data_random):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['SubID'] = manage['SubID']
                        data['UserID'] = manage['username']
                        data['GdsID'] = commodity_data_random['commodity_code']      #商品编码
                        data['Typ'] = '0'       #商品类型[0-商品,1-优惠券,2-虚拟商品,3-组合商品,4-停车券]
                        data['GdsTypID'] = ''   #分类代码[关联TypID字段]
                        data['GdsBndID'] = ''   #品牌代码[关联BndID字段]
                        data['Name'] = commodity_data_random['commodity_name']       #商品名称
                        data['SubTitle'] = ''   #副标题
                        data['KyWrd'] = ''      #关键词
                        data['Pk'] = '1'         #主包装规格
                        data['Unit'] = '件'       #基本单位
                        data['SalPrc'] = commodity_data_random['commodity_price']      #市场价
                        data['PurPrc'] = commodity_data_random['commodity_price']       #成本价
                        data['Spc'] = '2'          #规格
                        data['Plc'] = commodity_data_random['commodity_place']         #产地
                        data['Fctry'] = ''        #制造商
                        data['VldCyc'] = '0'    #保质周期
                        data['ImgUrls'] = commodity_data_random['commodity_image']      #主图片
                        data['Intro'] = commodity_data_random['commodity_name']        #图片描述
                        data['Stt'] = '0'          #状态
                        data['Deleted'] = 'N'      #删除状态
                        data['CrtUsr'] = '0'       #创建人
                        data['CrtDt'] = now_time['ymd_hms']        #创建时间
                        data['Brf'] = 'apitest'          
                        data['Uptr'] = '0'         
                        data['UptDtt'] = now_time['ymd_hms']
                        data['Images'] = ''       #商品图片列表
                        data['Stores'] = ''       #商品店铺列表
                        print(data)
                        response=requests.post(url=manage['url'] % '/GdsBase/EditGdsBase',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json)
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                except:
                        raise
        # 获取商品资料分页
        def test_get_commodity_data_list(self,headers,manage):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['SubID'] = manage['SubID']
                        data['GdsID'] = ''      # 商品编码[可选]
                        data['GdsName'] = ''    # 商品名称[可选]
                        data['PageIndex'] = '1'      
                        data['PageSize'] = '10'   
                        data['sort'] = "uptDtt desc"
                        data['Stt'] = '-99'     
                        response=requests.post(url=manage['url'] % '/GdsBase/GdsBaseList',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        if response_json['Data']['GdsList']:
                                # mysql insert response data
                                comm_way.sql_insert('commodity_page_response',response_json['Data']['GdsList'][0])
                                for i in response_json['Data']['GdsList']:
                                        print(i)
                        else:
                                print('没有商品')
                        
                except:
                        raise
    
        # 获取单个商品信息
        def test_get_commodity_data(self,headers,manage,commodity_page_response_data):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['SubID'] = manage['SubID']
                        data['GdsID'] = commodity_page_response_data['gdsID']     # 商品编码
                        response=requests.post(url=manage['url'] % '/GdsBase/QuerySinleGdsBase',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json)
                        assert response.status_code == 200
                        # assert response_json['Success'] == True
                except:
                        raise


class Test_commodity_putaway():
        # 添加商品上架单
        def test_add_commodity_putaway_apply(self,headers,manage,vipcard_response_data,now_time,commodity_page_response_data,putaway_activity_data_random):
                data={}
                data_sublist={}
                try:
                        data["CpnID"] = manage["CpnID"]
                        data["SubID"] = manage["SubID"]
                        data["ID"] = "0"
                        data["BllNo"] = putaway_activity_data_random['BllNo']
                        data["BizDt"] = now_time["ymd_hms"]
                        data["OrgID"] = "0000"          #活动机构
                        data["Name"] = commodity_page_response_data["name"]       #活动名称
                        data["StDt"] = now_time["StDt"]
                        data["EdDt"] = now_time["EdDt"]
                        data["VipTp"] = vipcard_response_data['crdTpid']  
                        data["Stt"] = "0"
                        data["Deleted"] = "N"
                        data["CrtUsr"] = "0"
                        data["CrtDt"] = now_time["ymd_hms"]
                        data["Auditor"] = "0"
                        data["AuditDt"] = ""
                        data["Brf"] = "apitest"
                        data["Uptr"] = manage["username"]
                        data["UptDtt"] = now_time["ymd_hms"]
                        data_sublist["ID"] = "0"
                        data_sublist["BllID"] = "0"
                        data_sublist["GdsID"] = commodity_page_response_data["gdsID"]     # 商品编码
                        data_sublist["GdsName"] = commodity_page_response_data["name"]     # 商品名称
                        data_sublist["FcttsIntg"] = putaway_activity_data_random['FcttsIntg']          #所需积分
                        data_sublist["Prc"] = "0"                       #所需金额
                        data_sublist["SalPrc"] =  commodity_page_response_data["salPrc"]     # 市场价值
                        data_sublist["MaxTotal"] = "100"                  #限制数量
                        data_sublist["Amt"] = "100"                       #计划数量
                        data_sublist["ImgUrls"] = ""
                        data_sublist["Intro"] = ""
                        data_sublist["Brf"] = "apitest"
                        data_sublist["Uptr"] = manage["username"]
                        data_sublist["UptDtt"] = now_time["ymd_hms"]
                        data["GdsCnvr"] = '[%s]' % data_sublist
                        print(data)
                        response=requests.post(url=manage['url'] % '/GdsCnvrtRole/EditGdsCnvrt',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                except:
                        raise
        
        
        # 商品上架单列表
        def test_get_commodity_putaway_list(self,headers,manage):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['SubID'] = manage['SubID']
                        data['NameLike'] = ''   #活动名称
                        data['BllNo'] = ''      #活动编号
                        data['StDt'] = ''
                        data['EdDt'] = ''
                        data['PageIndex'] = '1'
                        data['PageSize'] = '10'
                        data['SortType'] = "2"
                        print(data)
                        response=requests.post(url=manage['url'] % '/GdsCnvrtRole/QueryGdsCnvrtRoleList',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        if response_json['Data']['List']:
                                # mysql insert response data
                                comm_way.sql_insert('commodity_putaway_page_response',response_json['Data']['List'][0])
                                for i in response_json['Data']['List']:
                                        print(i)
                        else:
                                print('没有订单')
                except:
                        raise
        # 商品上架审批
        def test_commodity_putaway_audit(self,headers,manage,commodity_putaway_page_response_data):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['SubID'] = manage['SubID']
                        data['Auditor'] = manage['username']   #审批人
                        data['BllNo'] = commodity_putaway_page_response_data['bllNo']      #上架申请单票据号
                        data['Brf'] = 'apitest'
                        data['Stt'] = '50'
                        response=requests.post(url=manage['url'] % '/GdsCnvrtRole/ExamGdsCnvrtRole',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json)
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                except:
                        raise


# 获取上架商品列表
def test_putaway_commodity_list(headers,manage):
        data={}
        try:
                data['CpnID'] = manage['CpnID']
                data['SubID'] = manage['SubID']
                data['GdsCnvrtID'] = ''
                data['PgIndex'] = '1'
                data['PgSize'] = '10'
                response=requests.post(url=manage['url'] % '/GdsCnvrt/GetGdsCnvrt',data=data,headers=headers)
                response_json = comm_way.response_dispose(response.json())
                print(response_json['Message'])
                assert response.status_code == 200
                assert response_json['Success'] == True
                if response_json['Data']['Data']:
                        for i in response_json['Data']['Data']:
                                print(i)
                else:
                        print('没有上架商品')
        except:
                raise



