import requests
from selenium import webdriver
from selenium.webdriver.edge.service import Service
import time
import warnings
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging
from logging import handlers

version = 'selenium 4.0'
success = False


def driver1():
    print('method driver() start')
    Options = webdriver.EdgeOptions()
    driver = webdriver.Edge(options=Options, executable_path='.\\msedgedriver')
    driver.implicitly_wait(20)
    print("driver.implicitly_wait=20 Seconds")
    return driver


def to_page1(driver: webdriver, url: str):
    print('method to_page() start')
    driver.get(url)


def login(account: str, password: str):
    print('method login() start')
    submit = driver.find_element_by_name("submit")
    WebDriverWait(driver, 5, 0.5, StaleElementReferenceException).until(
        EC.visibility_of(submit), "运行超时")
    driver.find_element_by_id("username").send_keys(account)
    driver.find_element_by_id("password").send_keys(password)
    submit.click()


def create(driver: webdriver):
    print('method create() start')
    create = driver.find_element_by_id("dw_nBtn")  # 新建
    WebDriverWait(driver, 20, 0.5).until(
        EC.visibility_of(driver.find_element_by_id("dw_nBtn")))
    create.click()
    print('method create.click')
    print("try")
    iframe = [driver.find_element_by_xpath('//*[@id="side_dw_m_page_frame"]')]
    # 如果定位不到iframe，就把下面的iframe改成find_elements_by_tag_name("iframe")
    for i in iframe:
        try:
            driver.switch_to.frame(i)
            WebDriverWait(driver, 2, 0.5).until(
                EC.visibility_of(driver.find_element_by_id("BTN_SAVE")))
            save = driver.find_element_by_id("BTN_SAVE")
            break
        except NoSuchElementException:
            driver.switch_to.default_content()
            continue
    print("switch")
    setDNA = driver.find_element_by_xpath(
        "/html/body/form/div/table/tbody/tr[2]/td/table[1]/tbody[3]/tr[2]/td[2]/span/span")
    setDNA.click()
    setInfo = driver.find_element_by_xpath("/html/body/span/span")
    WebDriverWait(driver, 2, 0.5).until(EC.visibility_of(setInfo))  # 核酸情况
    set24Negative = setInfo.find_element_by_xpath(
        "./span[1]/input").send_keys("其他")  # 24,48,其他 都能识别到
    time.sleep(0.1)
    set24NegResult = setInfo.find_element_by_xpath("./span[2]/ul/li").click()
    setProvince = driver.find_element_by_id(
        "selProvince_SF")  # 可以自己在网页里查各省对应的值
    setProvince.find_element_by_xpath("//option[@value='35']").click()  # 福建
    setCity = driver.find_element_by_id("selCity_SF")
    setCity.find_element_by_xpath("//option[@value='3501']").click()  # 福州
    setArea = driver.find_element_by_id("selArea_SF")
    setArea.find_element_by_xpath("//option[@value='350102']").click()  # 鼓楼区
    save.click()
    save.click()
    print("Save")


def re(text: str):
    webhook = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=4e0a3e41-7c0d-4c88-b380-643c1c550e59"  # 机器人地址
    headers = {"Content-Type": "text/plain"}
    data = {
        "msgtype": "markdown",
        "markdown": {
            "content": text
        }
    }
    r = requests.post(url=webhook, headers=headers, json=data)
    print("提醒发送成功，内容为", text)


if __name__ == '__main__':
    cnt = 0
    t = time.strftime("%H:%M:%S", time.localtime())
    if t > '00:02:00' and t < '12:00:00' and cnt < 3 and not success:
        # if True:
        cnt += 1
        warnings.filterwarnings('ignore')
        flat = True
        count = 1
        while flat:
            try:
                # driver = driver1()
                driver = driver1()  # 调试用
                to_page1(
                    driver, "http://mcenter.lixin.edu.cn/login.html?ext1=mcenter_mryb")
                login("账号", "密码")  # 学号和密码
                print('method to_page() finish')
                # driver.get("http://mcenter.lixin.edu.cn/login.html?ext1=mcenter_mryb")
                create(driver)
                success = True
                print("Daily_Report finished")
                driver.close()
                flat = False

            except Exception as e:
                count += 1
                s = str(e)
                print(s)
                re("每日一报打卡失败！\n原因：" + s + "\n时间：" + time.strftime("%Y-%m-%d %H:%M:%S",
                                                                  time.localtime()) + "正在重试，第" + str(
                    count) + "次")
                if (count == 3):
                    re("每日一报打卡失败！\n原因：" + s + "\n时间：" +
                       time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                    flat = False

        if success:
            re("每日一报打卡成功！时间：" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        else:
            re("每日一报打卡失败！时间：" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
