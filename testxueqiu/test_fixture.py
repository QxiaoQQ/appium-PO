# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from hamcrest import *



class TestXueQiu:
    def setup_class(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "test"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["autoGrantPermissions"] = True   #处理弹窗权限问题

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        #驱动
        self.driver.implicitly_wait(20)   # 隐式等待
        # 弹窗 点击同意
        # self.driver.find_element_by_id("com.xueqiu.android:id/tv_agree").click()
        # self.driver.find_element_by_xpath("//*[text='雪球']")

    def teardown(self):
        self.driver.quit()

    # m默认是方法级
    @pytest.fixture()
    def test_source(self):
        # seleium 和 appium  的source 的不一样
        # seleium 源代码
        # appium  html的结构 输出来
        self.driver.find_element_by_xpath("//*[@text='关注']")
        yield
        #yield 之后相当于 teardown 的方法
        print(self.driver.page_source)


    @pytest.mark.parametrize("keyword,stock_type,exect_price" ,[
        ('alibaba' ,'BABA' ,100),
        ('xiaomi' ,'01810' ,8.1)
    ])
    def test_search(self ,keyword ,stock_type ,exect_price):
        self.driver.find_element_by_id("tv_search").click()
        self.driver.find_element_by_id("search_input_text").send_keys(keyword)
        self.driver.find_element_by_id("name").click()
        # self.driver.find_element_by_xpath("//*[@resource-id='stockName' and @text='阿里巴巴']").click()
        price = float(self.driver.find_element_by_xpath(
            "//*[contains(@resource-id,'stockCode'] and @text='" + stock_type + "']/../../.."
                                                                                "//*[contains(@resource-id,'current_price')]"
        ).text)
        assert price > exect_price
        # https://pypi.org/project/PyHamcrest/
        # 判断值在某个范围内，引入包 from hamcrest import * ，可使用asser_that(),close_to  方法
        # close_to ()接近某个范围值

        assert_that(price, close_to(exect_price, exect_price *0.2))
