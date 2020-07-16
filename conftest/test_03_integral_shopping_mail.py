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
                    data['MaxIntg'] = '1000'
                    data['PageIndex'] = 1
                    data['PageSize'] = 10
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
                    data['GdsCnvrtID'] = '2343242'    # 商品上架ID
                    response=requests.post(url=menber['url'] % '/IntgShop/QueryGdsCnvrt',data=data,headers=headers)
                    response_json = comm_way.response_dispose(response.json())
                    print(response_json['Message'])
                    assert response.status_code == 200
                    assert response_json['Success'] == True
                    print(response_json)
                    
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
                    print(response_json['Message'])
                    assert response.status_code == 200
                    assert response_json['Success'] == True
                    print(response_json)
                
        except:
                raise
    # 获取积分商城商品资料列表
    def test_shopping_commodity_data_list(self,headers,manage):
        data={}
        try:
                    data['CpnID'] = manage['CpnID']
                    data['SubID'] = manage['SubID']
                    data['GdsID'] = ''      # 商品编码[可选]
                    data['GdsName'] = ''    # 商品名称[可选]
                    data['PageIndex'] = '1'      
                    data['PageSize'] = '10'   
                    data['Stt'] = '0'     
                    response=requests.post(url=manage['url'] % '/GdsBase/GdsBaseList',data=data,headers=headers)
                    response_json = comm_way.response_dispose(response.json())
                    print(response_json)

                    print(response_json['Message'])
                    assert response.status_code == 200
                    assert response_json['Success'] == True
                    print(response_json)
                
        except:
                raise
    
    # 获取单个商品信息
    def test_commodity_data(self,headers,manage):
        data={}
        try:
                    data['CpnID'] = manage['CpnID']
                    data['SubID'] = manage['SubID']
                    data['GdsID'] = '23424242'      # 商品编码
                    response=requests.post(url=manage['url'] % '/GdsBase/QuerySinleGdsBase',data=data,headers=headers)
                    response_json = comm_way.response_dispose(response.json())
                    print(response_json['Message'])
                    assert response.status_code == 200
                    assert response_json['Success'] == True
                    print(response_json)
                
        except:
                raise