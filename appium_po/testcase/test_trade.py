from appium_po.page.xueqiu_page import XueqiuPage


class TestTrade:
    def setup(self):
        self.xueqiu = XueqiuPage()
        self.trade=self.xueqiu.goto_trade()

    def teardown(self):
        self.trade.driver.quit()

    def test_a_open(self):
        # 进入沪深 开户
        self.trade.goto_hs()
        self.xueqiu.goto_trade().a_open("15632222222",'123456')

    def test_danjuan_open(self):
        # 进入蛋卷基金 开户
        self.trade.goto_danjuan()
        self.trade.danjuan_open("12322222222","1234")