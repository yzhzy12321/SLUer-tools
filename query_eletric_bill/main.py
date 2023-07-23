import query
import extract
import datetime
import time
if __name__=='__main__':
    while True:
        time_now=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print('执行电费提取，时间：'+time_now)
        filename=query.get_html_data(2,2,1,2,15,1050)
        print("爬取网页成功")
        extract.extract_data(filename)
        print("提取电费数据成功")
        time.sleep(60)

