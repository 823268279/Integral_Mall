import pytest
import requests
from comm.comm_way import Way#公共方法
comm_way=Way()





class Test_sign_in():
        # 签到
        def test_signin(self,headers,menber,vipcard_response_data):
                data={}
                try:
                        data['CpnID'] = menber['CpnID']
                        data['SubID'] = menber['SubID']
                        data['OrgID'] = vipcard_response_data['orgID']
                        data['GstID'] = vipcard_response_data['gstID']
                        data['VipID'] = vipcard_response_data['vipID']
                        data['CrdID'] = vipcard_response_data['crdID']
                        data['InteTyp'] = '1'
                        data['Brf'] = "apitest"
                        print(data)
                        response=requests.post(url=menber['url'] % '/SignIn/SignIn',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json)
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        print(response_json['Message'])
                except:
                        raise
        # 获取签到记录
        def test_signin_record(self,headers,menber,vipcard_response_data,now_time):
                data={}
                try:
                        data['CpnID'] = menber['CpnID']
                        data['SubID'] = menber['SubID']
                        data['gstid'] = vipcard_response_data['gstID']
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




#获取wifi密码
def test_get_wifi_password(headers,menber):
        data={}
        try:
                data['CpnID'] = menber['CpnID']
                data['SubID'] = menber['SubID']
                response=requests.post(url=menber['url'] % '/Guest/GetWiFi',data=data,headers=headers)
                response_json = response.json()
                assert response.status_code == 200
                if response_json:
                        for i in response_json:
                                print(i)
                else:
                        print('没有wifi信息')
        except :
                raise





# 小票
class Test_upload_ticket():
        # 上传小票到s3
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
                
        # 上传小票
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

        # 查询用户小票上传记录分页
        def test_get_upload_ticket_record(self,headers,menber,vipcard_response_data):
                data={}
                try:
                        data['CpnID'] = menber['CpnID']
                        data['SubID'] = menber['SubID']
                        data['CrdID'] = vipcard_response_data['crdID']
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



# 车辆
class Test_car():
        # 添加会员车辆信息
        def test_add_car_data(self,headers,menber,vipcard_response_data,car_data_random):
                data={}
                try:
                        data['CpnID'] = menber['CpnID']
                        data['SubID'] = menber['SubID']
                        data['GstID'] = vipcard_response_data['gstID']
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
                        # mysql insert response data
                        comm_way.sql_insert('car_data_response',response_json['Data']['Data'][0])
                        
                except:
                        raise
        # 修改用户车辆信息
        def test_update_car_data(self,headers,menber,car_data_response_data,car_data_random,now_time):
                data={}
                try:
                        data['CpnID'] = menber['CpnID']
                        data['SubID'] = menber['SubID']
                        data['ID'] = car_data_response_data['id']
                        data['GstID'] = car_data_response_data['gstID']
                        data['CarID'] = car_data_response_data['carID']  
                        data['CarTp'] = car_data_response_data['carTp']
                        data['IsEv'] = car_data_response_data['isEv']
                        data['IsSupIntgAuto'] = car_data_response_data['isSupIntgAuto']
                        data['Stt'] = car_data_response_data['stt']
                        data['Brf'] = 'update test'
                        data['UptDtt'] = now_time['ymd_hms']
                        data['Parm'] = 'Brf'         #修改字段
                        response=requests.post(url=menber['url'] % '/GstCar/UpGstCar',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                except:
                        raise


        # 获取当前用户车牌号
        def test_get_user_car_data(self,headers,menber,vipcard_response_data):
                data={}
                try:
                        data['CpnID'] = '0001'
                        data['GstID'] = vipcard_response_data['gstID']
                        response=requests.post(url=menber['url'] % '/GstCar/GetGstCar',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        if response_json['Data']:
                                for i in response_json['Data']['Data']:
                                        print(i)
                        else:
                                print('没有车辆信息')
                except:
                        raise



# 券账户
class Test_menber_ticket_account():
        # 发送优惠券
        def test_send_ticket(self,headers,menber,vipcard_response_data,ticket_seed_page_response_data):
                data={}
                try:
                        data['CpnID'] = menber['CpnID']
                        data['CrdNos'] = vipcard_response_data['crdNo']        # 会员卡面号集合
                        data['TknID'] = ticket_seed_page_response_data['tknID']         # 券种编号
                        data['TknAmt'] = ticket_seed_page_response_data['tknvl']        # 券金额
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
        def test_get_user_ticket_seed_number(self,headers,menber,vipcard_response_data):
                data={}
                try:
                        data['CpnID'] = menber['CpnID']
                        data['SubID'] = menber['SubID']     
                        data['VipID'] = vipcard_response_data['vipID']         
                        data['CrdID'] = vipcard_response_data['crdID']  
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
        def test_get_user_ticket_page(self,headers,menber,vipcard_response_data):
                data={}
                try:
                        data['CpnID'] = menber['CpnID']
                        data['VipID'] = vipcard_response_data['vipID']        
                        data['CrdID'] = vipcard_response_data['crdID']        
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
        def test_get_user_past_ticket(self,headers,menber,vipcard_response_data):
                data={}
                try:
                        data['CpnID'] = menber['CpnID']
                        data['VipID'] = vipcard_response_data['vipID']        
                        data['CrdID'] = vipcard_response_data['crdID']        
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
                        raise# 券账户




# 获取首页广告位 
def test_get_index_advert_position(headers,menber):
        data={}
        try:
                data['CpnID'] = menber['CpnID']
                data['SubID'] = menber['SubID']
                data['ShwPosi'] = '1'
                response=requests.post(url=menber['url'] % '/AdPosi/GetAdPosiByMobileet',data=data,headers=headers)
                response_json = comm_way.response_dispose(response.json())
                print(response_json['Message'])
                assert response.status_code == 200
                assert response_json['Success'] == True
                list=[]
                list.append(response_json['Data']['AdPosi'])
                for i in list:
                        print(i)
                if response_json['Data']['Ad']:
                        for n in response_json['Data']['Ad']:
                                print(n)
                else:
                        print('没有广告内容')
        except:
                raise 




# 停车订单
class Test_park_order():
        # 新增停车订单
        def test_add_park_order(self,headers,manage,vipcard_response_data,car_data_response_data,now_time,park_order_data_random):
                data={}
                try:    
                        data['CpnID'] = manage['CpnID']
                        data['SubID'] = manage['SubID']
                        data['JoinDt'] = park_order_data_random['JoinDt'] #入场时间
                        data['ParkDt'] = '0'                              #停车时长
                        data['LeaveDt'] = ''                              #离场时间
                        data['PayTyp'] = '1'                              #支付方式(0-微信支付，1-积分支付，2-金币支付)
                        data['PayMoney'] = '0'                            #支付金额(PayTyp=0有效)
                        data['PayIntg'] = '0'                             #支付积分(PayTyp=1有效)
                        data['PayGold'] = '0'                             #支付金币(PayTyp=2有效)
                        data['GstID'] = vipcard_response_data['gstID']
                        data['CarNum'] = car_data_response_data['carID']#车牌号
                        data['BllNo'] = park_order_data_random['BllNo']                        #订单号
                        data['Stt'] = 0                                 #状体(0-录入，50-成功)
                        data['Deleted'] = '0'
                        data['Uptr'] = manage['username']
                        data['UptDtt'] = now_time['ymd_hms']
                        data['PgIndex'] = 0
                        data['PgSize'] = 0
                        data['MemberTypID'] = '01'
                        response=requests.post(url=manage['url'] % '/Park/AddParkOrder',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True    
                        print(response_json['Data']['ParkCheckPay'])
                        print(response_json['Data']['Data'])     
                except:
                        raise

        # 查询订单分页
        def test_get_park_order_page(self,manage,headers):
                data={}
                try:    
                        data['ID'] = ''
                        data['CpnID'] = manage['CpnID']
                        data['SubID'] = manage['SubID']
                        data['JoinDt'] = ''
                        data['ParkDt'] ='0'
                        data['LeaveDt'] = ''
                        data['PayTyp'] =  '-99'                        
                        data['PayMoney'] =  '0'                    
                        data['PayIntg'] = '0'                    
                        data['PayGold'] = '0'                     
                        data['GstID'] = ''
                        data['CarNum'] = ''
                        data['BllNo'] =  ''                 
                        data['Stt'] = '-99'                          
                        data['Deleted'] = ''
                        data['Uptr'] = ''
                        data['UptDtt'] = ''
                        data['PgIndex'] = '1'
                        data['PgSize'] = '10'
                        data['MemberTypID'] = ''
                        response=requests.post(url=manage['url'] % '/Park/GetParkOrderAll',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True                       
                        if response_json['Data']['PageDataList']:
                                # mysql insert park_order_page response data
                                comm_way.sql_insert('park_order_page_response',response_json['Data']['PageDataList'][0])
                                for i in response_json['Data']['PageDataList']:
                                        print(i)
                        else:
                                print('没有停车订单')
                except:
                        raise
        # 停车缴费
        def test_park_pay(self,headers,manage,menber,menber_register_request_data,park_order_page_response_data):
                data={}
                try:    
                        data['CpnID'] = manage['CpnID']
                        data['SubID'] = manage['SubID']
                        data['PayAppID'] = menber['PayAppID']
                        data['PayAppSecrect'] = menber['PayAppSecrect']
                        data['OpenID'] = menber_register_request_data['OpnID']
                        data['ParkOrderID'] = park_order_page_response_data['id']
                        data['PayOrderType'] = '6'
                        data['FeeType'] = '3'
                        response=requests.post(url=manage['url'] % '/Park/ParkEnd',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True                       
                        print(response_json)
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
                        data['SortType'] = '0'    #排序类型[0-默认、1-热门顺序、3-积分从小到大、4-积分从大到小、5-上架时间倒序、6-上架时间顺序]
                        data['MinIntg'] = '0'
                        data['MaxIntg'] = '0'
                        data['PageIndex'] = '1'
                        data['PageSize'] = '100'
                        print(data)
                        response=requests.post(url=menber['url'] % '/IntgShop/QueryGoodsList',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        if response_json['Data']['GdsList']:
                                # mysql insert get shop commodity_list response data
                                comm_way.sql_insert('shop_commodity_page_response',response_json['Data']['GdsList'][0])
                                for i in response_json['Data']['GdsList']:
                                        print(i)
                        else:
                                print('没有商品')
                except:
                        raise
        # 获取单个商品上架信息
        def test_commodity_putaway_data(self,headers,menber,shop_commodity_page_response_data):
                data={}
                try:
                        data['CpnID'] = menber['CpnID']
                        data['SubID'] = menber['SubID']
                        data['GdsCnvrtID'] = shop_commodity_page_response_data['gdsCnvrtID']    # 商品上架ID
                        response=requests.post(url=menber['url'] % '/IntgShop/QueryGdsCnvrt',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                        # mysql insert get shop commodity_putaway_data response data
                        comm_way.sql_insert('shop_commodity_response',response_json['Data']['GdsCnvrtInfo'])
                        print(response_json['Data']['GdsCnvrtInfo'])
                        
                except:
                        raise
        # 添加/删除用户收藏/感兴趣
        def test_add_user_collect(self,headers,menber,vipcard_response_data,shop_commodity_response_data):
                data={}
                try:
                        data['CpnID'] = menber['CpnID']
                        data['SubID'] = menber['SubID']
                        data['GstID'] = vipcard_response_data['gstID']  
                        data['GdsCnvrtID'] = shop_commodity_response_data['gdsCnvrtID']    # 商品上架ID
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
        def test_get_user_collect(self,headers,menber,vipcard_response_data,shop_commodity_response_data):
                data={}
                try:
                        data['CpnID'] = menber['CpnID']
                        data['SubID'] = menber['SubID']
                        data['GstID'] = vipcard_response_data['gstID']  
                        data['GdsCnvrtID'] = shop_commodity_response_data['gdsCnvrtID']   #商品上架ID[可为空，不为空则查询该上架商品的收藏信息]
                        data['GdsID'] = shop_commodity_response_data['gdsID']        # 商品编码ID
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
        def test_add_shop_order(self,menber,headers,vipcard_response_data,shop_commodity_response_data):
                data={}
                try:
                        data['CpnID'] = menber['CpnID']
                        data['SubID'] = menber['SubID']
                        data['OrgID'] = '0000'        #兑换下单机构
                        data['GstID'] = vipcard_response_data['gstID']       
                        data['CrdID'] = vipcard_response_data['crdID']   
                        data['CrdFace'] = vipcard_response_data['vipID']  
                        data['DeliOrg'] = '0000'      #提货机构
                        data['ChkCode'] = '1234'      #提货验证码
                        data['FcttsIntg'] = float(shop_commodity_response_data['fcttsIntg'])*3    #应付积分
                        data['PaidIntg'] = float(shop_commodity_response_data['fcttsIntg'])*3     #实付积分
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
                        data['VipTp'] = vipcard_response_data['crdTpid']  
                        data['CnvrtIDs'] = shop_commodity_response_data['gdsCnvrtID']     #上架ID 
                        data['GdsCodes'] = shop_commodity_response_data['gdsID']     #商品条码
                        data['SubCodes'] = ''     #商品子码
                        data['Typs'] = '1'         #商品类型
                        data['Names'] = shop_commodity_response_data['gdsName']        #商品名称
                        data['SubNames'] = ''     #子码描述
                        data['ImgUrlss'] = shop_commodity_response_data['imgURL']      #商品主图
                        data['SalPrcs'] = shop_commodity_response_data['salPrc']       #市场价值
                        data['Amts'] = '3'         #兑换数量
                        data['FcttsIntgs'] = shop_commodity_response_data['fcttsIntg']    #所需积分
                        data['Prcs'] = shop_commodity_response_data['prc']          #所需金额
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
        def test_get_shop_order_list(self,menber,headers,vipcard_response_data):
                data={}
                try:
                        data['CpnID'] = menber['CpnID']
                        data['SubID'] = menber['SubID']
                        data['GstID'] = vipcard_response_data['gstID']  
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
                                comm_way.sql_insert('shop_order_page_response',response_json['Data']['Data'][0])
                                for i in response_json['Data']['Data']:
                                        print(i)
                        else:
                                print('没有订单')
                except:
                        raise
        # 积分商城支付
        def test_shop_order_pay(self,headers,menber,shop_order_page_response_data,vipcard_response_data):
                data={}
                try:
                        data['CpnID'] = menber['CpnID']
                        data['SubID'] = menber['SubID']
                        data['BllNO'] = shop_order_page_response_data['id'] 
                        data['PayType'] = '3'   
                        data['IntgAmt'] =int(float(shop_order_page_response_data['paidIntg'])*100)     #支付积分  
                        data['Money'] = int(float(shop_order_page_response_data['paidPrc'])*100)     #支付金额
                        data['OrgID'] = '0000'     
                        data['VipID'] = vipcard_response_data['vipID']    
                        data['CrdNo'] = vipcard_response_data['crdNo']    
                        data['CrdID'] = vipcard_response_data['crdID']   
                        print(data)  
                        response=requests.post(url=menber['url'] % '/IntgShop/PayCnvrtOrder',data=data,headers=headers)
                        response_json = comm_way.response_dispose(response.json())
                        print(response_json)
                        print(response_json['Message'])
                        assert response.status_code == 200
                        assert response_json['Success'] == True
                except:
                        raise