from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import expected_conditions as EC

version = 'Using Selenium 4.0 and Edge driver'
author = "A student study in Computer Science"


def driver1():
    print('method driver() start')
    Options = webdriver.EdgeOptions()
    # Options.add_argument("headless") #使用本行可使用无头浏览器
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
    driver.find_element_by_id("username").send_keys(account)
    driver.find_element_by_id("password").send_keys(password)
    submit.click()


def create(driver: webdriver):
    print('method create() start')
    create = driver.find_element_by_id("dw_nBtn")  # 新建
    create.click()
    print('method create.click')
    print("try")
    iframe = [driver.find_element_by_xpath('//*[@id="side_dw_m_page_frame"]')]
    # 如果定位不到iframe，就把下面的iframe改成find_elements_by_tag_name("iframe")
    for i in iframe:
        try:
            driver.switch_to.frame(i)
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
    set24Negative = setInfo.find_element_by_xpath(
        "./span[1]/input").send_keys("其他")  # 24,48,其他 都能识别到
    set24NegResult = setInfo.find_element_by_xpath("./span[2]/ul/li").click()
    setProvince = driver.find_element_by_id(
        "selProvince_SF")  # 可以自己在网页里查各省对应的值
    setProvince.find_element_by_xpath("//option[@value='']").click()
    setCity = driver.find_element_by_id("selCity_SF")
    setCity.find_element_by_xpath("//option[@value='']").click()
    setArea = driver.find_element_by_id("selArea_SF")
    setArea.find_element_by_xpath("//option[@value='']").click()
    save.click()
    save.click()
    print("Save")


if __name__ == '__main__':
    driver = driver1()
    to_page1(
        driver, "http://mcenter.lixin.edu.cn/login.html?ext1=mcenter_mryb")
    login("账号", "密码")  # 学号和密码
    print('method to_page() finish')
    # driver.get("http://mcenter.lixin.edu.cn/login.html?ext1=mcenter_mryb")
    create(driver)
    print("Daily_Report finished")
    driver.close()
