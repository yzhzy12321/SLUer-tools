import requests as re
import json
import time
null=''
def area():
    filename='getarea.json'
    ls=[]
    for sysid in range(1,3,1):
        params={"sysid":str(sysid)}
        data=getData(filename,params)
        ls.extend(data)#把数据保存在ls中
    tojson(ls,'getarea.json')#写入到文件

def district():
    filename='getdistrict.json'
    with open("getarea.json",'r',encoding='utf-8')as f:
        data=json.load(f)
        print(data)
        f.close()
    areaIds=[]#用于存放所有的areaId
    for i in data:
        areaIds.append(i['areaId'])
    print(areaIds)
    ls=[]
    for sysid in range(1,3,1):
        for areaid in areaIds:
            params={"sysid":str(sysid),'areaid':str(areaid)}
            data=getData(filename,params)
            ls.extend(data)#把数据保存在ls中
    print(ls)
    tojson(ls,filename)

def build():
    pass
def floor():
    pass
def room():
    pass
def tojson(content,filename):#此函数用于将内容写入到对应的json文件中
    json_data = json.dumps(content,ensure_ascii=False, indent=4) #转json
    with open(filename,'w',encoding='utf-8')as f:
        f.write(json_data)
        f.close()
def getData(jsonName:str,params:dict):
    ls=[]
    r=re.get(url='https://yktepay.lixin.edu.cn/ykt/h5/'+jsonName,params=params)
    time.sleep(1)
    content=r.content.decode('utf-8')
    print(content)#输出返回的值
    con=eval(content)#转换成dict
    con['list'][0].update(params)#把params的参数也添加进去
    return con['list']
if __name__=='__main__':
    area()
    # district()