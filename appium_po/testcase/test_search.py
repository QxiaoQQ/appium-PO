from appium_po.page.xueqiu_page import XueqiuPage


class TestSearch:

    def setup(self):
        # 不暴露内部元素 只能进入page 页 进行操作
        # 初始化模型 xueqiu
        self.xueqiu = XueqiuPage()

    def test_search(self):

        assert self.xueqiu.goto_search().search("alibaba").select(0).get_price("BABA")>170

    def test_search_us_other(self):
        # xueqiu=XueqiuPage()
        assert "ALIBBA" in self.xueqiu.goto_search().search("alibbab").select(-1).get_name()