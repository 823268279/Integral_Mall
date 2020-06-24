# from mitmproxy import http,ctx

# def request(flow):
#     print(flow.request.host)    #host标头值
#     print(flow.request.url)     #请求的url地址
#     print(flow.request.scheme)  #请求的协议
#     print(flow.request.port)    #请求的端口
#     print(flow.request.method)  #请求的方法
#     print(flow.request.headers) #请求的头信息
#     print(flow.request.cookies) #请求cookies
#     print(flow.request.get_text())  #请求body
# from mitmproxy import http,ctx
# def response(flow):

#     print(flow.repsonse.status_code)    #响应状态码
#     print(flow.request.headers)         #响应头信息
#     print(flow.repsonse.cookies)        #响应cookies
#     print(flow.response.text)           #响应内容


__file__ = r'./img/ticket_one.jpg'
file=open(__file__,'rb')
file.read()
file.close()

print(file)