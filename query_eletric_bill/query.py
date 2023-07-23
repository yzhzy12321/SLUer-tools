import requests as re

def get_html_data(sysid:int,areaid:int,districtid:int,buildid:int,floorid:int,roomid:int,filename='1.html'):
  s=re.Session()
  params={'sysid':str(sysid),'areaid':str(areaid),'districtid':str(districtid),'buildid':str(buildid),'floorid':str(floorid),'roomid':str(roomid)}#要查找的宿舍号
  s.headers.update({"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1788.0"})
  res=s.get(url="https://yktepay.lixin.edu.cn/ykt/h5/eleresult?",params=params)#获取电费剩余
  
  with open(filename,'w',encoding='utf-8')as f:#把读取的网页写入filename
    f.write(res.content.decode('utf-8'))
    f.close()
  return filename
if __name__=='__main__':
  sysid=2
  areaid=2
  districtid=1
  buildid=2
  floorid=15
  roomid=1050
  get_html_data(sysid,areaid,districtid,buildid,floorid,roomid)