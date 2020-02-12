# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver

class TestXueQiu:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "test"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_demo(self):
        el1 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_agree")
        el1.click()
        el2 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TabHost/android.widget.LinearLayout/android.widget.TabWidget/android.widget.RelativeLayout[4]")
        el2.click()
        el3 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.TextView[1]")
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

