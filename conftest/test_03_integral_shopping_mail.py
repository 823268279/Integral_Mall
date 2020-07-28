import pytest
import requests
from comm.comm_way import Way#公共方法
comm_way=Way()



#积分商城
class Test_integral_shopping_mail():
        # 获取积分商城商品列表
        def test_shopping_commodity_list(self,headers,menber):
                data={}
                try:
                        data['CpnID'] = menber['CpnID']
                        data['SubID'] = menber['SubID']
                        data['SortType'] = '0'    #排序类型[1：默认、热门倒序;2：积分从小到大；3：积分从大到小；4:上架时间]
                        data['MinIntg'] = '0'
                        data['MaxIntg'] = '10'
                        data['PageIndex'] = 1
                        data['PageSize'] = 10
                        print(data)
                        response=requests.post(url=menber['url'] % '/IntgShop/QueryGoodsList',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        print(response_json)
                        
                except:
                        raise
        # 获取单个商品上架信息
        def test_commodity_push_data(self,headers,menber):
                data={}
                try:
                        data['CpnID'] = menber['CpnID']
                        data['SubID'] = menber['SubID']
                        data['GdsCnvrtID'] = '32424323'    # 商品上架ID
                        response=requests.post(url=menber['url'] % '/IntgShop/QueryGdsCnvrt',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json)
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        
                        
                except:
                        raise
        # 添加用户收藏/感兴趣
        def test_add_user_collect(self,headers,menber,menber_register_response_data):
                data={}
                try:
                        data['CpnID'] = menber['CpnID']
                        data['SubID'] = menber['SubID']
                        data['GstID'] = menber_register_response_data['gstID']  
                        data['GdsCnvrtID'] = '2424242'   #商品上架ID
                        data['FavType'] = '0'       # 收藏类型[0：收藏，1：感兴趣]
                        data['IsAdd'] = 'true'     # 是否添加[true：添加，false：删除收藏数据]
                        response=requests.post(url=menber['url'] % '/IntgShop/AddGstFav',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        print(response_json)
                        
                except:
                        raise

        # 获取用户收藏感兴趣
        def test_get_user_collect(self,headers,menber,menber_register_response_data):
                data={}
                try:
                        data['CpnID'] = menber['CpnID']
                        data['SubID'] = menber['SubID']
                        data['GstID'] = menber_register_response_data['gstID']  
                        data['GdsCnvrtID'] = ''   #商品上架ID[可为空，不为空则查询该上架商品的收藏信息]
                        data['GdsID'] = ''        # 商品编码ID
                        data['FavType'] = '0'     # 收藏类型[0：收藏，1：感兴趣]
                        response=requests.post(url=menber['url'] % '/IntgShop/QueryGstFav',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json)
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        print(response_json)
                        
                except:
                        raise
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
                        data['Pk'] = '1*1'         #主包装规格
                        data['Unit'] = ''       #基本单位
                        data['SalPrc'] = commodity_data_random['commodity_price']      #市场价
                        data['PurPrc'] = commodity_data_random['commodity_price']       #成本价
                        data['Spc'] = ''          #规格
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
                                comm_way.sql_insert('commodity_data_response',response_json['Data']['GdsList'][-1])
                                for i in response_json['Data']['GdsList']:
                                        print(i)
                        else:
                                print('没有商品资料')
                        
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
                        #     assert response_json['Success'] == True
                except:
                        raise
class Test_commodity_putaway():
        # 添加商品上架单
        def test_add_commodity_putaway_apply(self,headers,manage,now_time,commodity_response_data):
                data={}
                data_sublist={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['SubID'] = manage['SubID']
                        data['ID'] = '0'
                        data['BllNo'] = '0062222222343'
                        data['BizDt'] = now_time['ymd_hms']
                        data['OrgID'] = '1002'          #活动机构
                        data['Name'] = '上架活动'       #活动名称
                        data['StDt'] = now_time['StDt']
                        data['EdDt'] = now_time['EdDt']
                        data['VipTp'] = ''
                        data['Stt'] = '0'
                        data['Deleted'] = 'N'
                        data['CrtUsr'] = '0'
                        data['CrtDt'] = now_time['ymd_hms']
                        data['Auditor'] = '0'
                        data['AuditDt'] = ''
                        data['Brf'] = 'apitest'
                        data['Uptr'] = manage['username']
                        data['UptDtt'] = now_time['ymd_hms']
                        data_sublist['ID'] = '0'
                        data_sublist['BllID'] = '0'
                        data_sublist['GdsID'] = commodity_response_data['gdsID']     # 商品编码
                        data_sublist['GdsName'] = commodity_response_data['name']     # 商品名称
                        data_sublist['FcttsIntg'] = '200'                           #所需积分
                        data_sublist['Prc'] = '0'                       #所需金额
                        data_sublist['SalPrc'] =  commodity_response_data['salPrc']     # 市场价值
                        data_sublist['MaxTotal'] = '0'                  #限制数量
                        data_sublist['Amt'] = '0'                       #计划数量
                        data_sublist['ImgUrls'] = ''
                        data_sublist['Intro'] = ''
                        data_sublist['Brf'] = 'apitest'
                        data_sublist['Uptr'] = manage['username']
                        data_sublist['UptDtt'] = now_time['ymd_hms']
                        data['GdsCnvrtRoleDtlList'] = []
                        data['GdsCnvrtRoleDtlList'].append(data_sublist)
                        print(data)
                        response=requests.post(url=manage['url'] % '/GdsCnvrtRole/EditGdsCnvrt',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json)
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                except:
                        raise
        
        # 商品申请单列表
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
                        response=requests.post(url=manage['url'] % '/GdsCnvrtRole/QueryGdsCnvrtRoleList',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json)
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                except:
                        raise
        # 商品上架审批
        def test_commodity_putaway_audit(self,headers,manage):
                data={}
                try:
                        data['CpnID'] = manage['CpnID']
                        data['SubID'] = manage['SubID']
                        data['Auditor'] = manage['username']   #审批人
                        data['BllNo'] = ''      #上架申请单票据号
                        data['Brf'] = 'apitest'
                        data['Stt'] = '50'
                        response=requests.post(url=manage['url'] % '/GdsCnvrtRole/ExamGdsCnvrtRole',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json)
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                except:
                        raise