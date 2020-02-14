# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from hamcrest import *
from selenium.webdriver.support.wait import WebDriverWait


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

    def test_profile(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_agree").click()

        el2 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TabHost/android.widget.LinearLayout/android.widget.TabWidget/android.widget.RelativeLayout[4]")
        el2.click()

    def test_click(self):
        # 点击
        self.driver.tap()

    def test_sendkeys(self):
        # 输入
        self.driver.keyevent()

    def test_getattibute(self):
        # get_attribute() 获取元素属性
        print(self.driver.find_element_by_id("com.xueqiu.android:id/tv_agree").get_attribute("content-desc"))

    def test_swipe(self):

        #滑动，起止点的坐标 (x1,y1,x2,y2,滑动时间 单位ms )
        # self.driver.find_element(By.XPATH, "//*[text='雪球']").click()

        for i in range(5):
            self.driver.swipe(100, 250, 100, 600, 1000)
    def test_swiep_percent(self):
        # 直接填写数据太LOW ，要写成百分比来 获取位置
        # 先获取窗口的大小，在填写滑动比例
        size = self.driver.get_window_size()
        print(size)
        width = size('width')
        height = size('height')
        self.driver.swipe(width*0.8,height*0.8,width*0.2,width*0.2,1000)

    def test_uiautomator(self):
        #自动查找元素 自动滑动， 先找到 uiselector 元素，然后把uiselect 包裹到可滚动对量里面（UiScrollable），这个是找 WebViews 然后点击的操作
        # 但是对ios 没有作用
        self.driver.find_element_by_android_uiautomator('new UiScrollable('
                                                        'new UiSelector().scrollable(true).instance(0))'
                                                        '.scrollIntoView('
                                                        'new UiSelector().text("WebViews").instance(0));').click()

    def test_touchaction(self):
        # 长按 给定一个元素或者一个坐标
        TouchAction(self.driver).long_press()

    def test_source(self):
        # seleium 和 appium  的source 的不一样
        # seleium 源代码
        # appium  html的结构 输出来
        self.driver.find_element_by_xpath("//*[@text='关注']")
        print(self.driver.page_source)

    @pytest.mark.parametrize("keyword,stock_type,exect_price", [
        ('alibaba','BABA',100),
        ('xiaomi','01810',8.1)
    ])
    def test_search(self,keyword,stock_type,exect_price):
        self.driver.find_element_by_id("tv_search").click()
        self.driver.find_element_by_id("search_input_text").send_keys(keyword)
        self.driver.find_element_by_id("name").click()
        # self.driver.find_element_by_xpath("//*[@resource-id='stockName' and @text='阿里巴巴']").click()
        price = float(self.driver.find_element_by_xpath(
            "//*[contains(@resource-id,'stockCode'] and @text='" + stock_type + "']/../../.."
            "//*[contains(@resource-id,'current_price')]"
        ).text)
        #普通断言
        assert price > exect_price
        #  hamcrest 断言
        # https://pypi.org/project/PyHamcrest/
        # 判断值在某个范围内，引入包 from hamcrest import * ，可使用asser_that(),close_to  方法
        #close_to ()接近某个范围值
        assert_that(price, close_to(exect_price, exect_price*0.2))

    def test_webview(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='交易']").click()
        # 返回的是不带webview的组件，默认是找不到webview内的元素，除非设置了等待
        print(self.driver.page_source)
        # 原生定位
        self.driver.find_element(MobileBy.ID, 'page_type_fund').click()

        WebDriverWait(self.driver, 10, 1).until(lambda x: "WEBVIEW_com.xueqiu.android" in self.driver.contexts)
        print("=======webview load")
        # 返回的是带有webview组件树，此时可以使用原生定位去定位webview内的元素
        print(self.driver.page_source)
        # 使用原生定位方式定位webview控件
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "蛋卷基金安全开户").click()

        self.driver.switch_to.context("WEBVIEW_com.xueqiu.android")
        print("======webview enter")
        # 返回的是html，此次可以使用selenium的css定位
        print(self.driver.page_source)
        self.driver.find_element(By.NAME, "tel").send_keys("15600534760")
        self.driver.find_element(By.NAME, "captcha").send_keys("1234")
        self.driver.find_element(By.CSS_SELECTOR, ".dj-button").click()




    def test_gotologin(self):
        el3 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.TextView[1]")
        el3.click()
        el4 = self.driver.find_element_by_id("com.xueqiu.android:id/login_account")
        el4.click()
        el5 = self.driver.find_element_by_id("com.xueqiu.android:id/login_account")
        el5.click()
        el6 = self.driver.find_element_by_id("com.xueqiu.android:id/login_password")
        el6.send_keys(159123655555)
        el7 = self.driver.find_element_by_id("com.xueqiu.android:id/button_next")
        el7.send_keys(111111)
        el8 = self.driver.find_element_by_id("com.xueqiu.android:id/md_buttonDefaultPositive")
        el8.click()
        el9 = self.driver.find_element_by_id("com.xueqiu.android:id/iv_action_back")
        el9.click()
