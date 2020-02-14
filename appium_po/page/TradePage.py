from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from appium_po.page.base_page import BasePage


class TradePage(BasePage):
    # content-desc:A股开户 所以用 MobileBy.ACCESSIBILITY_ID 来定位
    _a_open = (MobileBy.ACCESSIBILITY_ID, 'A股开户')
    _danjuan_open = (By.XPATH, "//*[text='蛋卷基金安全开户'")

    def goto_hs(self):
        self.driver.find_element_by_xpath("//*[@text='沪深']").click()

    def a_open(self,phone,number):
        WebDriverWait(self.driver, 20).until(
            expected_conditions.visibility_of_element_located(self._a_open)
        )
        self.driver.find_element(*self._a_open).click()

    def goto_danjuan(self):
        self.driver.find_element_by_xpath("//*[@text='基金']").click()

    def danjuan_open(self,phone,number):
        WebDriverWait(self.driver, 20).until(
            expected_conditions.visibility_of_element_located(self._danjuan_open)
        )
        self.driver.find_element(*self._danjuan_open).click()