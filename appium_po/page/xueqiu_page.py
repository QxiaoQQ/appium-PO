# from appium import webdriver
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from appium_po.page.Profile_Page import ProfilePage
from appium_po.page.search_page import SearchPage
# 先写用例，在写方法，这是集成测试

class XueqiuPage:

    def __init__(self):

        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "test"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["autoGrantPermissions"] = True  # 处理弹窗权限问题

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # 驱动
        self.driver.implicitly_wait(20)  # 隐式等待

        # 弹窗 点击同意
        # self.driver.find_element_by_id("com.xueqiu.android:id/tv_agree").click()
        # self.driver.find_element_by_xpath("//*[text='雪球']")
        # 显示等待 等待某元素出现
        # 显示等待不是强制等待，只要在这时间范围内 找到既可以不用在等待了
        # WebDriverWait(self.driver, 20).until(
        #     expected_conditions.visibility_of_element_located((By.ID,"com.xueqiu.android:id/tv_agree")) )

    def goto_search(self):
        # 进入搜索页
        self.driver.find_element_by_id("tv_search").click()
        return SearchPage(self.driver)

    def goto_profile(self):
        # 进入个人页
        return ProfilePage()

    def get_default(self):

        # 推荐 推荐没有跳转页面，直接断言本内容 duan
        return False

    def get_ads(self):
        #有无广告
        return False


