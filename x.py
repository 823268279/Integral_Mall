import json


data_sublist={}



data_sublist['MaxTotal'] = '0'                  #限制数量
data_sublist['Amt'] = '0'                       #计划数量
data_sublist['ImgUrls'] = ''
data_sublist['Intro'] = ''
data_sublist['Brf'] = 'apitest'


x=json.dumps(data_sublist)
print(data_sublist)
print(type(data_sublist))
print(x)
print(type(x))


