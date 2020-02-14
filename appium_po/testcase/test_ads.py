from appium_po.page.xueqiu_page import XueqiuPage


class TestAds:
    def setup(self):
        self.xueqiu = XueqiuPage()

    def test_ads(self):
        # 测试雪球的广告页有没有展示出来
        assert self.xueqiu.get_ads() == True