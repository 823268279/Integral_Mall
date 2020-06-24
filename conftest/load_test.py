import requests
import json
from locust import HttpUser, TaskSet, between, task, events


@events.test_start.add_listener
def on_test_start(**kwargs):
    url='http://api.newcrm.group.weixin.wuerp.com/api/v1.0/Token/Get'
    data={
    "id":"m1234567",
    "key":"7947ff3cbf06647f312e4e6ec5e32943"
    }
    response = requests.post(url=url,data=data)
    response_json=response.json()
    #响应断言
    assert response.status_code == 200
    assert response_json['message'] =='获取授权成功'
    global headers
    headers={}
    headers['Authorization']=response_json['data']['Data']['token']



class ForumSection(TaskSet):




    @task(1)
    def get_menber_data(self):
        data={
                "CpnID":"0001",
                "subID":"3378049226@qq.com",
                "gstID":"96"}
        response = self.client.post(url="/Guest/GetMainGst",data=data,headers=headers) 
        response_json=response.json()
        #响应断言
        assert response.status_code == 200
        assert response_json['message'] == '获取成功'



class LoggedInUser(HttpUser):
    tasks = {ForumSection:2}
    wait_time = between(3, 5)
    host='http://api.newcrm.group.weixin.wuerp.com/member/v1.0'