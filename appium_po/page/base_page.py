from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find(self,locator):
        # todo: 处理弹窗 异常处理 同台浮动的元素的处理
        self.driver.find_element(locator)
