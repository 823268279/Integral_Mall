# import requests
# from locust import HttpLocust,task,TaskSet
# import xmltodict
# import dicttoxml
# import json
# class Menber_select(TaskSet):
#     def on_start(self):
#         url='http://api.newcrm.group.weixin.wuerp.com/api/v1.0/Token/Get'
#         data={
#         "id":"newcrm.weixin.wuerp.com]",
#         "key":"7947ff3cbf06647f312e4e6ec5e32943"
#     }
#         response = requests.post(url=url,data=data)
#         response_json=response.json()
#         #响应断言
#         assert response.status_code == 200
#         assert response_json['message'] =='获取授权成功'
#         self.headers={}
#         self.headers['Authorization']=response_json['data']['Data']['token']




#     @task(1)
#     def test(self):
#         data={
#                 "CpnID":"0001",
#                 "subID":"3378049226@qq.com",
#                 "gstID":"96"}
#         response = self.client.post(url="/Guest/GetMainGst",data=data,headers=self.headers) 
#         print(response.json())
#         #响应断言
#         assert response.status_code == 200

# class Config(HttpLocust):
#     task_set = Menber_select
#     min_wait = 3000
#     max_wait = 6000
#     host='http://api.newcrm.group.weixin.wuerp.com/member/v1.0'


list_z=[]
if list_z:
    for i in list_z:
        print(i)
else:
    print('null')
