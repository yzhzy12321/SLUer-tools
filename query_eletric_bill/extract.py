import re
import datetime

def html_tag_rm(content: str):#提取出网页上的电表数据
	dr = re.compile(r'<[^>]+>',re.S)
	return dr.sub('',content)
def extract_data(html:str,txt='2.txt'):
    with open(html,'r',encoding='utf-8')as f:
        # print(f.read())
        s=str(html_tag_rm(f.read()))
        # print(s)
        f.close()
    s=s.split()
    index=0
    for i in range(len(s)):
        if s[i]=='充值':
            index=i
            break
    s=s[1:index]#截取到度数
    time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # print(time)
    s.append(time)#添加时间戳
    s=str(s)
    print(s)
    with open(txt,'a',encoding='utf-8')as f:#写入到文件中
        f.writelines('\n'+s)
        f.close()
        
if __name__=='__main__':
    html="1.html"
    txt="2.txt"
    extract_data(html,txt)

