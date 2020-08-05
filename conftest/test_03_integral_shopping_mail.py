import pytest
import json
import requests
from comm.comm_way import Way#公共方法
comm_way=Way()

# 店铺管理
class Test_store_data_manage():
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
                        response=requests.post(url=manage['url'] % '/Store/AddCpnOrg',data=data,headers=headers)
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
                        data['OrgID'] = ''
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
                        response=requests.post(url=manage['url'] % '/Store/GetCpnOrg',data=data,headers=headers)
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
# 商品管理
class Test_commodity_data_manage():
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
        def test_commodity_data_list(self,headers,manage):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['SubID'] = manage['SubID']
                        data['GdsID'] = ''      # 商品编码[可选]
                        data['GdsName'] = ''    # 商品名称[可选]
                        data['PageIndex'] = '1'      
                        data['PageSize'] = '10'   
                        data['sort'] = "uptDtt desc"
                        data['Stt'] = '0'     
                        response=requests.post(url=manage['url'] % '/GdsBase/GdsBaseList',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        if response_json['Data']['GdsList']:
                                # mysql insert response data
                                comm_way.sql_insert('commodity_data_response',response_json['Data']['GdsList'][-1])
                                for i in response_json['Data']['GdsList']:
                                        print(i)
                        else:
                                print('没有商品')
                        
                except:
                        raise
    
        # 获取单个商品信息
        def test_commodity_data(self,headers,manage,commodity_response_data):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['SubID'] = manage['SubID']
                        data['GdsID'] = commodity_response_data['gdsID']     # 商品编码
                        response=requests.post(url=manage['url'] % '/GdsBase/QuerySinleGdsBase',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json)
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                except:
                        raise
class Test_commodity_putaway():
        # 添加商品上架单
        def test_add_commodity_putaway_apply(self,headers,manage,menber_register_response_data,now_time,commodity_response_data,putaway_activity_data_random):
                data={}
                data_sublist={}
                try:
                        data["CpnID"] = manage["CpnID"]
                        data["SubID"] = manage["SubID"]
                        data["ID"] = "0"
                        data["BllNo"] = putaway_activity_data_random['BllNo']
                        data["BizDt"] = now_time["ymd_hms"]
                        data["OrgID"] = "0000"          #活动机构
                        data["Name"] = putaway_activity_data_random['Name']       #活动名称
                        data["StDt"] = now_time["StDt"]
                        data["EdDt"] = now_time["EdDt"]
                        data["VipTp"] = menber_register_response_data['memberTypID']  
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
                        data_sublist["GdsID"] = commodity_response_data["gdsID"]     # 商品编码
                        data_sublist["GdsName"] = commodity_response_data["name"]     # 商品名称
                        data_sublist["FcttsIntg"] = putaway_activity_data_random['FcttsIntg']          #所需积分
                        data_sublist["Prc"] = "0"                       #所需金额
                        data_sublist["SalPrc"] =  commodity_response_data["salPrc"]     # 市场价值
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
                                comm_way.sql_insert('commodity_putaway_list_response',response_json['Data']['List'][0])
                                for i in response_json['Data']['List']:
                                        print(i)
                        else:
                                print('没有订单')
                except:
                        raise
        # 商品上架审批
        def test_commodity_putaway_audit(self,headers,manage,commodity_putaway_list_response_data):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['SubID'] = manage['SubID']
                        data['Auditor'] = manage['username']   #审批人
                        data['BllNo'] = commodity_putaway_list_response_data['bllNo']      #上架申请单票据号
                        data['Brf'] = 'apitest'
                        data['Stt'] = '50'
                        response=requests.post(url=manage['url'] % '/GdsCnvrtRole/ExamGdsCnvrtRole',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json)
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                except:
                        raise


#积分商城
class Test_integral_shop_commodity():
        # 获取积分商城上架列表
        def test_get_shop_commodity_list(self,headers,menber):
                data={}
                try:
                        data['CpnID'] = menber['CpnID']
                        data['SubID'] = menber['SubID']
                        data['SortType'] = '0'    #排序类型[1：默认、热门倒序;2：积分从小到大；3：积分从大到小；4:上架时间]
                        data['MinIntg'] = '0'
                        data['MaxIntg'] = '0'
                        data['PageIndex'] = '1'
                        data['PageSize'] = '10'
                        data['sort'] = "uptDtt desc"
                        response=requests.post(url=menber['url'] % '/IntgShop/QueryGoodsList',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        if response_json['Data']['GdsList']:
                                # mysql insert get shop commodity_list response data
                                comm_way.sql_insert('shop_commodity_list_response',response_json['Data']['GdsList'][-1])
                                for i in response_json['Data']['GdsList']:
                                        print(i)
                        else:
                                print('没有商品')
                except:
                        raise
        # 获取单个商品上架信息
        def test_commodity_putaway_data(self,headers,menber,shop_commodity_list_response_data):
                data={}
                try:
                        data['CpnID'] = menber['CpnID']
                        data['SubID'] = menber['SubID']
                        data['GdsCnvrtID'] = shop_commodity_list_response_data['gdsCnvrtID']    # 商品上架ID
                        response=requests.post(url=menber['url'] % '/IntgShop/QueryGdsCnvrt',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        # mysql insert get shop commodity_putaway_data response data
                        comm_way.sql_insert('shop_commodity_putaway_response',response_json['Data']['GdsCnvrtInfo'])
                        print(response_json['Data']['GdsCnvrtInfo'])
                        
                except:
                        raise
        # 添加/删除用户收藏/感兴趣
        def test_add_user_collect(self,headers,menber,menber_register_response_data,shop_commodity_putaway_response_data):
                data={}
                try:
                        data['CpnID'] = menber['CpnID']
                        data['SubID'] = menber['SubID']
                        data['GstID'] = menber_register_response_data['gstID']  
                        data['GdsCnvrtID'] = shop_commodity_putaway_response_data['gdsCnvrtID']    # 商品上架ID
                        data['FavType'] = '0'       # 收藏类型[0：收藏，1：感兴趣]
                        data['IsAdd'] = 'true'     # 是否添加[true：添加，false：删除收藏数据]
                        response=requests.post(url=menber['url'] % '/IntgShop/AddGstFav',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        
                except:
                        raise

        # 获取用户收藏感兴趣
        def test_get_user_collect(self,headers,menber,menber_register_response_data,shop_commodity_putaway_response_data):
                data={}
                try:
                        data['CpnID'] = menber['CpnID']
                        data['SubID'] = menber['SubID']
                        data['GstID'] = menber_register_response_data['gstID']  
                        data['GdsCnvrtID'] = shop_commodity_putaway_response_data['gdsCnvrtID']   #商品上架ID[可为空，不为空则查询该上架商品的收藏信息]
                        data['GdsID'] = shop_commodity_putaway_response_data['gdsID']        # 商品编码ID
                        data['FavType'] = '0'     # 收藏类型[0：收藏，1：感兴趣]
                        response=requests.post(url=menber['url'] % '/IntgShop/QueryGstFav',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        print(response_json['Data']['GstFavs'])
                        if response_json['Data']['GstFavs']:
                                for i in response_json['Data']['GstFavs']:
                                        print(i)
                        else:
                                print('没有收藏/感兴趣')
                except:
                        raise

class Test_integral_shop_order():
        # 积分商城添加订单
        def test_add_shop_order(self,menber,headers,menber_register_response_data,shop_commodity_putaway_response_data):
                data={}
                try:
                        data['CpnID'] = menber['CpnID']
                        data['SubID'] = menber['SubID']
                        data['OrgID'] = '0000'        #兑换下单机构
                        data['GstID'] = menber_register_response_data['gstID']       
                        data['CrdID'] = menber_register_response_data['crdID']   
                        data['CrdFace'] = menber_register_response_data['crdFaceID']  
                        data['DeliOrg'] = '0000'      #提货机构
                        data['ChkCode'] = '1234'      #提货验证码
                        data['FcttsIntg'] = float(shop_commodity_putaway_response_data['fcttsIntg'])*3    #应付积分
                        data['PaidIntg'] = float(shop_commodity_putaway_response_data['fcttsIntg'])*3     #实付积分
                        data['Prc'] = '0'          #应付金额
                        data['PaidPrc'] = '0'      #实付金额
                        # data['Frei'] = '0'         #运费
                        # data['PaidFrei'] = '0'     #已付金额
                        # data['Consignee'] = '0'    #收货人姓名
                        # data['Tel'] = '0'          #收货人电话
                        # data['Mobile'] = '0'       #收货人手机号
                        # data['Eml'] = '0'          #收货人邮箱
                        # data['Province'] = '0'     #省份
                        # data['City'] = '0'         #城市
                        # data['District'] = '0'     #区/县
                        # data['Addr'] = '0'         #详细地址
                        # data['Zip'] = '0'          #邮政编码
                        # data['Source'] = '0'       #订单来源
                        # data['LgstcsTyp'] = '0'    #物流类型
                        # data['Msg'] = '0'          #订单留言
                        # data['LgstcsCode'] = '0'   #物流配置
                        # data['LgstcsNo'] = ''     #物流单号
                        # data['ExpDt'] = '0'        #失效时间
                        # data['ExcDsc'] = '0'       #异常描述
                        # data['Uptr'] = '0'      
                        data['VipTp'] = menber_register_response_data['memberTypID']  
                        data['CnvrtIDs'] = shop_commodity_putaway_response_data['gdsCnvrtID']     #上架ID 
                        data['GdsCodes'] = shop_commodity_putaway_response_data['gdsID']     #商品条码
                        data['SubCodes'] = ''     #商品子码
                        data['Typs'] = '1'         #商品类型
                        data['Names'] = shop_commodity_putaway_response_data['gdsName']        #商品名称
                        data['SubNames'] = ''     #子码描述
                        data['ImgUrlss'] = shop_commodity_putaway_response_data['imgURL']      #商品主图
                        data['SalPrcs'] = shop_commodity_putaway_response_data['salPrc']       #市场价值
                        data['Amts'] = '3'         #兑换数量
                        data['FcttsIntgs'] = shop_commodity_putaway_response_data['fcttsIntg']    #所需积分
                        data['Prcs'] = shop_commodity_putaway_response_data['prc']          #所需金额
                        data['TknAccID'] = ''     #优惠券账号
                        data['Brf'] = 'apitest'
                        response=requests.post(url=menber['url'] % '/IntgShop/AddCnvrtOrder',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        print(response_json)
                except:
                        raise
        
        # 积分商城查询订单列表
        def test_get_shop_order_list(self,menber,headers,menber_register_response_data):
                data={}
                try:
                        data['CpnID'] = menber['CpnID']
                        data['SubID'] = menber['SubID']
                        data['GstID'] = menber_register_response_data['gstID']  
                        data['PageIndex'] = '1'   
                        data['PageSize'] = '10'      
                        data['Stt'] = '0'     
                        response=requests.post(url=menber['url'] % '/IntgShop/QueryCnvrtOrderList',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        if response_json['Data']['Data']:
                                # mysql insert shop_order_list response data
                                comm_way.sql_insert('shop_order_list_response',response_json['Data']['Data'][0])
                                for i in response_json['Data']['Data']:
                                        print(i)
                        else:
                                print('没有订单')
                except:
                        raise
        # 积分商城支付
        def test_shop_order_pay(self,headers,menber,shop_order_list_response_data,menber_register_response_data,menber_select_response_data):
                data={}
                try:
                        data['CpnID'] = menber['CpnID']
                        data['SubID'] = menber['SubID']
                        data['BllNO'] = shop_order_list_response_data['id'] 
                        data['PayType'] = '3'   
                        data['IntgAmt'] =int(float(shop_order_list_response_data['paidIntg'])*100)     #支付积分  
                        data['Money'] = int(float(shop_order_list_response_data['paidPrc'])*100)     #支付金额
                        data['OrgID'] = '0000'     
                        data['VipID'] = menber_register_response_data['crdFaceID']    
                        data['CrdNo'] = menber_register_response_data['crdFaceID']    
                        data['CrdID'] = menber_register_response_data['crdID']   
                        print(data)  
                        response=requests.post(url=menber['url'] % '/IntgShop/PayCnvrtOrder',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json)
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                except:
                        raise

