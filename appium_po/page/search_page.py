from selenium.webdriver.remote.webdriver import WebDriver

from appium_po.page.base_page import BasePage


class SearchPage(BasePage):

    # 类型推导 ：driver 传来传去已经不知道它是标准化的driver了，所以需要加上 :WebDriver

    def search(self,keyword):
        #搜索内容
        self.driver.find_element_by_id("search_input_text").send_keys(keyword)
        return self

    def select(self,index):
        # find_elements_by_id 返回多个元素 选择第几个
        self.driver.find_elements_by_id("name")[index].click()
        return self

    def get_price(self,stock_type):
        # 获取价格 传入一个 stock_type 及选中 的元素属性
        price = float(self.driver.find_element_by_xpath(
            "//*[contains(@resource-id,'stockCode'] and @text='"
            + stock_type + "']/../../.."
            "//*[contains(@resource-id,'current_price')]").text)
        return price

    def get_name(self):
        return "ppps"