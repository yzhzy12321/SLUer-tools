import requests as re
import json
null=''
def area():
    ls=[]
    for i in range(1,3,1):
        r=re.get(url='https://yktepay.lixin.edu.cn/ykt/h5/getarea.json',params={"sysid":str(i)})
        content=r.content.decode('utf-8')
        print(content)#输出返回的值
        con=eval(content)#转换成dict
        ls.extend(con['list'])#把数据保存在ls中
    json_data=tojson(ls,'getarea.json')#写入到文件

def district():
    pass
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
if __name__=='__main__':
    area()